# `governed-delivery` Templates

Portable sibling to [SKILL.md](SKILL.md) in this directory. Its Module Contract and Preflight Evidence Checker requirements govern both emitted files below; read them before emission. These bodies check record coherence, not event authenticity, continuous sealing or product acceptance.

## Contents

- [Preflight checker](#template-checkspreflightpy-python-stdlib-only)
- [Flow-pack executable wrapper](#flow-pack-executable-wrapper)

### Template: checks/preflight.py (Python, stdlib only)

The host writes the emitted file verbatim and marks it executable; the template below is normative.

```python
#!/usr/bin/env python3
"""checks/preflight.py — finite record-coherence checker (stdlib only).

Reads a JSON run note and a JSON binding, checks that every required host
precondition has coherent fresh evidence bound to the current spec/host,
and prints one machine-readable disposition line plus JSON detail.

CLI: python3 checks/preflight.py run-note.json binding.json
Exit 0 only for coherent fresh required evidence with unchanged bound
inputs (disposition "ready"); exit 4 otherwise ("hold" or "stale").

This checker validates evidence record coherence, not event authenticity,
continuous sealing, or accepted product delivery. File and artifact
existence/hash checks are record-coherence evidence, never proof events
happened or sealing holds continuously. Its output is evidence for the
host; it never promotes a run to enforcement-proven. The host owns and
protects this checker, the binding, and the evidence; prose cannot seal
them. Cancellation and run-lifecycle facts are unknown when absent, never
implicit kill assurance.

Relative paths resolve against the task-root working directory.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
import json
import math
import os
import stat
import sys
from datetime import datetime, timezone

KNOWN_CONTROLS = (
    "oracle_sealing",
    "sink_isolation",
    "budget_enforcement",
    "durable_ledger_storage",
    "human_decision_channel",
)
KNOWN_RESULTS = ("met", "unmet", "unknown")


def _fail(kind, reasons):
    detail = {"disposition": kind, "reasons": reasons, "artifact_complete": True}
    print(kind)
    print(json.dumps(detail, indent=2, sort_keys=True))
    return 4


def _is_str(value):
    return isinstance(value, str)


def _nonempty_str(value):
    return _is_str(value) and len(value.strip()) > 0


def _is_number(value):
    # bool is a subclass of int: True/False are not valid numbers here.
    return type(value) is int or (type(value) is float and math.isfinite(value))


def _parse_time(value):
    if not _is_str(value):
        return None
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        moment = datetime.fromisoformat(text)
        if moment.tzinfo is None:
            return None
        return moment.astimezone(timezone.utc)
    except (ValueError, OverflowError):
        return None


@contextmanager
def _regular_file(path, mode):
    fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise ValueError("file source must be regular")
        with os.fdopen(fd, mode, encoding="utf-8" if mode == "r" else None, closefd=False) as handle:
            yield handle
    finally:
        os.close(fd)


def _sha256_file(path):
    digest = hashlib.sha256()
    with _regular_file(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON field: %s" % key)
        result[key] = value
    return result


def _reject_constant(token):
    raise ValueError("non-finite JSON number: %s" % token)


def _load_json(path, label, reasons):
    try:
        with _regular_file(path, "r") as handle:
            data = json.load(handle, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except FileNotFoundError:
        reasons.append("%s not found: %s" % (label, path))
        return None
    except (ValueError, UnicodeDecodeError, OSError, RecursionError) as exc:
        reasons.append("%s unreadable: %s" % (label, exc))
        return None
    if not isinstance(data, dict):
        reasons.append("%s must be a JSON object" % label)
        return None
    return data


def main(argv):
    if len(argv) != 3:
        return _fail("hold", ["usage: python3 checks/preflight.py run-note.json binding.json"])
    note_path, binding_path = argv[1], argv[2]
    task_root = os.getcwd()
    now = datetime.now(timezone.utc)

    reasons = []
    note = _load_json(note_path, "run note", reasons)
    binding = _load_json(binding_path, "binding", reasons)
    if note is None or binding is None:
        return _fail("hold", reasons)

    stale_hits = []
    hold_hits = list(reasons)

    # --- Binding shape: owner input. ---
    spec_version = binding.get("spec_version")
    host_identity = binding.get("host_identity")
    required = binding.get("required_preconditions")
    max_age = binding.get("max_age_seconds")
    bound_files = binding.get("files")
    extra_binding_keys = set(binding) - {"spec_version", "host_identity", "required_preconditions", "max_age_seconds", "files"}
    if extra_binding_keys:
        hold_hits.append("binding has unknown top-level keys: %s" % sorted(extra_binding_keys))
    if not _nonempty_str(spec_version):
        hold_hits.append("binding.spec_version must be a nonempty string")
    if not _nonempty_str(host_identity):
        hold_hits.append("binding.host_identity must be a nonempty string")
    if not isinstance(required, list) or not required:
        hold_hits.append("binding.required_preconditions must be a nonempty list")
        required = []
    elif any(not _is_str(item) for item in required):
        hold_hits.append("binding.required_preconditions must list strings")
        required = [item for item in required if _is_str(item)]
    if len(set(required)) != len(required):
        hold_hits.append("binding.required_preconditions has duplicate rows")
    unknown_controls = [item for item in required if item not in KNOWN_CONTROLS]
    if unknown_controls:
        hold_hits.append("binding.required_preconditions has unknown keys: %s" % sorted(set(unknown_controls)))
    if not _is_number(max_age) or not (max_age > 0):
        hold_hits.append("binding.max_age_seconds must be a positive task-declared number")
        max_age = None
    if not isinstance(bound_files, dict):
        hold_hits.append("binding.files must be an object of path -> sha256")
        bound_files = {}
    else:
        for path, digest in bound_files.items():
            if not _nonempty_str(path) or not _nonempty_str(digest):
                hold_hits.append("binding.files entry must map nonempty path to nonempty sha256")

    # --- Note shape: the five existing keys, JSON-serialized. ---
    if not _nonempty_str(note.get("spec_version")):
        hold_hits.append("note.spec_version must be a nonempty string")
    if not _nonempty_str(note.get("host_identity")):
        hold_hits.append("note.host_identity must be a nonempty string")
    statuses = {}
    for key in KNOWN_CONTROLS:
        if key not in note:
            hold_hits.append("note.%s is missing; serialize unknown explicitly" % key)
        value = note.get(key, "unknown")
        if value not in KNOWN_RESULTS:
            hold_hits.append("note.%s must be met/unmet/unknown" % key)
            value = "unknown"
        statuses[key] = value
    extra_status_keys = [k for k in note if k not in KNOWN_CONTROLS and k not in ("spec_version", "host_identity", "evidence", "status")]
    if extra_status_keys:
        hold_hits.append("note has unknown top-level keys: %s" % sorted(extra_status_keys))
    evidence = note.get("evidence", [])
    if not isinstance(evidence, list):
        hold_hits.append("note.evidence must be a list")
        evidence = []
    if note.get("status") != "artifact-complete":
        hold_hits.append("note.status must be artifact-complete")

    # --- Freshness/spec/host binding checks (stale when bound inputs moved). ---
    if _nonempty_str(spec_version) and _nonempty_str(note.get("spec_version")):
        if note.get("spec_version") != spec_version:
            stale_hits.append("note.spec_version does not match binding.spec_version")
    if _nonempty_str(host_identity) and _nonempty_str(note.get("host_identity")):
        if note.get("host_identity") != host_identity:
            stale_hits.append("note.host_identity does not match binding.host_identity")

    # --- Bound files: immutable task inputs/oracles/verifier unchanged. ---
    for path, digest in bound_files.items():
        if not _nonempty_str(path) or not _nonempty_str(digest):
            continue
        full = path if os.path.isabs(path) else os.path.join(task_root, path)
        try:
            current = _sha256_file(full)
        except ValueError as exc:
            hold_hits.append("bound file source malformed: %s (%s)" % (path, exc))
            continue
        except OSError as exc:
            stale_hits.append("bound file unreadable: %s (%s)" % (path, exc))
            continue
        if current.lower() != digest.strip().lower():
            stale_hits.append("bound file changed: %s" % path)

    # --- Index all evidence before validating any positive claim. ---
    evidence_by_control = {}
    for row in evidence:
        if not isinstance(row, dict):
            hold_hits.append("note.evidence rows must be objects")
            continue
        key = row.get("precondition")
        if not _is_str(key) or key not in KNOWN_CONTROLS:
            hold_hits.append("evidence precondition must name a known control")
            continue
        if key in evidence_by_control:
            hold_hits.append("evidence %s has duplicate or conflicting rows" % key)
        else:
            evidence_by_control[key] = row
        result = row.get("result")
        if result not in KNOWN_RESULTS:
            hold_hits.append("evidence %s result must be met/unmet/unknown" % key)
        elif result != statuses[key]:
            hold_hits.append("evidence %s result contradicts the note" % key)
    for key in KNOWN_CONTROLS:
        status = statuses[key]
        if key not in required and status != "met":
            continue
        if status != "met":
            hold_hits.append("required %s is %s" % (key, status))
            continue
        row = evidence_by_control.get(key)
        if row is None:
            hold_hits.append("%s met without evidence" % key)
            continue
        if row.get("result") != "met":
            hold_hits.append("evidence %s must be met for the note's claim" % key)
            continue
        if row.get("spec_version") != spec_version:
            stale_hits.append("evidence %s spec_version does not match binding" % key)
        if row.get("host_identity") != host_identity:
            stale_hits.append("evidence %s host_identity does not match binding" % key)
        moment = _parse_time(row.get("observed_at", ""))
        if moment is None:
            hold_hits.append("evidence %s observed_at is not a UTC timestamp" % key)
        elif max_age is not None:
            age = (now - moment).total_seconds()
            if age < 0 or age > max_age:
                stale_hits.append("evidence %s is stale (age outside max_age_seconds)" % key)
        command = row.get("command")
        if not isinstance(command, list) or not command or any(not _is_str(part) or not part for part in command):
            hold_hits.append("evidence %s command must be a nonempty string list" % key)
        if not _nonempty_str(row.get("principal")):
            hold_hits.append("evidence %s principal must name the executor/actual checked role" % key)
        if row.get("exit_code") != 0 or isinstance(row.get("exit_code"), bool):
            hold_hits.append("evidence %s needs exit_code 0 for the complete host probe" % key)
        artifacts = row.get("artifacts")
        if not isinstance(artifacts, list) or not artifacts:
            hold_hits.append("evidence %s needs at least one raw-output artifact" % key)
            continue
        for artifact in artifacts:
            if not isinstance(artifact, dict) or not _nonempty_str(artifact.get("path")) or not _nonempty_str(artifact.get("sha256")):
                hold_hits.append("evidence %s artifact rows need path and sha256" % key)
                break
            full = artifact["path"] if os.path.isabs(artifact["path"]) else os.path.join(task_root, artifact["path"])
            try:
                current = _sha256_file(full)
            except ValueError as exc:
                hold_hits.append("evidence %s artifact source malformed: %s (%s)" % (key, artifact["path"], exc))
                break
            except OSError as exc:
                stale_hits.append("evidence %s artifact unreadable: %s (%s)" % (key, artifact["path"], exc))
                break
            if current.lower() != artifact["sha256"].strip().lower():
                stale_hits.append("evidence %s artifact changed: %s" % (key, artifact["path"]))
                break

    if stale_hits:
        return _fail("stale", stale_hits + hold_hits)
    if hold_hits:
        return _fail("hold", hold_hits)
    detail = {
        "disposition": "ready",
        "reasons": ["all required preconditions have coherent fresh evidence"],
        "artifact_complete": True,
        "note": "record coherence only; not event authenticity, continuous sealing, or accepted delivery",
    }
    print("ready")
    print(json.dumps(detail, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

The JSON note carries the five precondition keys with the same `unknown` default, plus `spec_version`, `host_identity`, an `evidence` list, and `status: artifact-complete`. The binding carries `spec_version`, `host_identity`, `required_preconditions`, the task-declared `max_age_seconds`, and `files` (path → SHA256). Neither file may claim `enforcement-proven`; the checker has no such output.

### Flow-pack executable wrapper

Emit `checks/run-preflight.sh`, mark it executable, and set
`PREFLIGHT="$PWD/checks/run-preflight.sh"` from the reviewed task root.
`PREFLIGHT` accepts one pathname, not a command string with arguments.

```sh
#!/bin/sh
exec python3 checks/preflight.py run-note.json binding.json
```

The host protects the wrapper, checker, binding and evidence. Hash checks
do not authenticate their producer or identify the active worker profile.

