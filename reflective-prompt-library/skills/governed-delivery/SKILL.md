---
name: governed-delivery
description: Use when a task must be delivered end-to-end under governance — an autonomous or unattended delivery run that needs a gate sequence, an oracle manifest, a task packet, failure-signature exits, decorrelated verification, an evidence ledger, and a named acceptance record. It emits a host-run delivery contract set; it does not enforce it. For effect authority use agent-governance-scaffold; for loop or flow scripts use flow-loop-harness or flow-control-generator.
license: MIT
compatibility: Emits delivery contracts (Markdown/YAML) and an optional stdlib-only Python 3.7+ record checker for a POSIX host with a headless agent CLI; the host owns sealing, sink isolation, budgets, durable ledgers, and human decisions — TeaPrompt runs none of them.
metadata:
  risk_level: high
  human_review_required: true
  external_io: false
  context_load: medium
---

# Governed Delivery

**Type:** Domain-pack skill (delivery-contract generation) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly. Companion to `agent-governance-scaffold` (effect authority), `flow-loop-harness` (iteration), and `flow-control-generator` (topology), which own those concerns, not the delivery lifecycle.

## Purpose

Turn a governed end-to-end delivery request into a small host-run contract set: a seven-gate sequence, an oracle manifest, a task packet, failure-signature exits, a verification plan, an evidence ledger, an autonomy envelope, and a named acceptance record. Direct answer: unattended delivery cannot be trusted without human intent sign-off and host containment; intent drift and context rot are bounded, not solved. TeaPrompt stays on the methodology side of the methodology-vs-operationalization boundary (source repo: `plans/external-adoption-case-studies-2026-06-20.md`): the emitted files are operational artifacts awaiting host wiring. Sealing, isolation, budgets, ledgers, and the human decision channel are the host's to run — TeaPrompt operates none of that runtime.

## Module Contract

Trigger:

- The user asks to "deliver end-to-end with gates", "autonomous delivery", "unattended delivery run", "governed pipeline to done", or "run this to done under governance".
- A delivery needs a gate sequence, an oracle manifest, a task packet, failure-signature exits, decorrelated verification, an evidence ledger, and a named acceptance record before any unattended run.
- Plain "pipeline", "plan", "deliver", or "automate" without explicit governed end-to-end intent still follows the nine core routes.

Methods:

- Gate mapping: instantiate the seven-gate sequence; size thickness to risk (Gate 2.0); never auto-release `intent` or `acceptance`.
- Packet-first: emit a task packet (spec version, State Ledger, oracle manifest, relevant files). Gates read the packet and the ledgers, not the transcript. A missing acceptance criterion stops the run until the packet is repaired.
- Oracle split: list every acceptance, invariant, and security check with class (authoritative or developer), owner, host sealing precondition, and change protocol. Authoritative oracles are read-only in-run; developer tests may be added. Prompt text cannot seal an oracle — the host must.
- Failure signatures: record failing oracle, error class, and touched surface. After a correction, a repeated signature exits by rollback to the last verified ledger state, a strategy change, or escalation — never an identical retry. Limits are task-declared in the envelope.
- Decorrelated verification: declare channels (deterministic check, runtime evidence, external primary source, independent model, self-assessment) and whether they are independent. A high-risk PASS needs at least one non-model channel.
- Evidence ledger: each entry names the claim, the source, the attester, the freshness kind, and the date checked. A tool result is evidence; the agent's summary of it is not.
- Envelope: before unattended work, record pre-approved budget, per-action pause list, kill conditions, failure-signature limit, allowed sinks, and named accepter. A run outside the envelope stops. Unresolved high-impact irreversible assumptions are Human Review triggers.
- Acceptance: a named accepter closes the delivery against the oracle manifest and product evidence; execution success alone never closes it.
- Minimality: size gate thickness to risk; remove ceremony that defends no named invariant.
- Compatibility: name tool, framework, model, or repository versions the guidance assumes; a workflow skill needs a paired with/without check.

Output:

- A run note listing host preconditions as met, unmet, or `unknown`, plus the status literal `artifact-complete` or `enforcement-proven`. `artifact-complete` ≠ `enforcement-proven`; the latter requires observed host evidence. The emitted run note keeps the five existing precondition keys and their `unknown` default; the JSON note is the same mapping serialized for the checker, not a second authority surface.
- Optionally, the `checks/preflight.py` record-coherence checker and, for flow-pack integration, its executable `checks/run-preflight.sh` wrapper (see the Preflight evidence checker template). The host selects the wrapper pathname only when required; empty preserves an attended example without claimed runtime enforcement. The host protects both files, the binding, and the evidence; prose cannot seal them.

Never:

- Never claim TeaPrompt enforces a gate, seals an oracle, isolates a sink, or persists a ledger; the contract set is host-run and enforcement is a host precondition.
- Never let the executing agent edit the oracle manifest, the verification plan, the acceptance record, or the envelope; those are constitutional paths changed only out-of-band by a different owner.
- Never auto-release a gate on model self-report; a gate releases on deterministic evidence, an attester's receipt, or a named human decision.
- Never use a universal retry or iteration count; budgets and failure-signature limits are task-declared in the envelope.
- Never treat the transcript as the source of record; every gate reads the task packet and the ledgers.
- Never accept or promote `enforcement-proven` on the preflight checker's output alone: it validates record coherence at a point in time, not that events happened, that sealing holds continuously, or that delivery is accepted. File and artifact existence/hash checks are record-coherence evidence, never proof an event occurred or sealing holds continuously.
- Never route this pack from `reflective-dispatch` or present it as a tenth core workflow skill; it is host-invoked.

Escalation:

- Unclear intent → `reflective-brief`.
- No-code workflow spec → `reflective-spec-plan`.
- Side effects on credentials, permissions, privacy, billing, production, or destructive ops → `reflective-risk` before first run.
- Effect authority, capability tokens, broker receipts → `agent-governance-scaffold`.
- Iteration loops → `flow-loop-harness`.
- Fixed topology → `flow-control-generator`.
- Whether the delivery run should exist at all → `reflective-minimality`.

## Delivery Gate Sequence

| Gate | Release condition | Who releases | Evidence tier | Auto-release allowed |
| --- | --- | --- | --- | --- |
| `intent` | Named human signs the intent-record; unknowns have owners | named human | human decision | no |
| `spec` | Versioned spec plus oracle manifest; no `stale` dependents | spec owner | artifact | no |
| `plan` | Plan items bound to the current spec version | plan owner | artifact | yes if binding is deterministic |
| `execution` | Work follows the task packet; ledger current | executor | runtime | yes if the deterministic packet-binding and ledger-currency checks pass; no when packet-adherence rests on agent self-report |
| `verification` | Verification-plan channels met | attester / host verifier | ranked; deterministic first | yes for deterministic; no for model-only |
| `acceptance` | Named accepter closes against oracles and product evidence | named accepter | mixed; not self-report | no |
| `retro` | Gate retro recorded; policy change kept off activation | retro owner | artifact | yes if the retro record parses |

Auto-release is never allowed for `intent` and `acceptance`. A mid-task spec change bumps the spec version and marks every spec_version-keyed artifact — plan items, ledger entries, the oracle manifest, the task packet, and the acceptance record — `stale`; the oracle manifest is re-validated and the affected slice re-planned before work continues. Auto-release keys off whether the release condition is a deterministic check, not off the evidence tier.

## Autonomy Envelope

This pack adds no new lettered ladder: autonomy is expressed through the existing strictness ladder (`L1`–`L6`) and Gate 2.0 thickness. Cross-ref `flow-loop-harness` Human Review Boundary for loops and `agent-governance-scaffold` Gate 2.0 for effect severity. Envelope fields: pre-approved budget, per-action pause list, kill conditions, failure-signature limit (task-declared), allowed sinks, named accepter. A run outside the envelope stops. Thickness scales with risk; higher strictness still cannot auto-release `intent` or `acceptance`.

## Contract Set

Emit only what the task needs. Each object is a static contract; the host wires enforcement.

### intent-record

Purpose: freeze the signed goal, owned unknowns, and irreversible assumptions before any later gate.

```yaml
intent_id: ""
goal: ""
out_of_scope: []
unknowns: [{item: "", owner: ""}]
irreversible_assumptions: [{item: "", human_review: required}]
signed_by: ""
status: unsigned
```

Invariant: unsigned intent cannot release `intent`; tacit gaps stay visible as owned unknowns.

### oracle-manifest

Purpose: name every acceptance, invariant, and security oracle with class, owner, seal, and change protocol.

```yaml
spec_version: ""
oracles:
  - name: ""
    class: authoritative  # or developer
    owner: ""
    host_seal: write_protection  # or protected_branch | ci_ownership | none
    change_protocol: out_of_band
```

Invariant: the executing agent does not edit this file; a developer test is not an authoritative oracle.

### task-packet

Purpose: the source of record for work — spec version, State Ledger, oracle manifest, files — never the transcript.

```yaml
spec_version: ""
state_ledger_ref: ""
oracle_manifest_ref: ""
files: []
missing_acceptance: stop_and_repair
```

Invariant: if an acceptance criterion is missing from the packet, stop and repair the packet.

### failure-log

Purpose: record failure signatures so a repeat after correction exits instead of retrying.

```yaml
entries:
  - oracle: ""
    error_class: ""
    surface: ""
    after_correction: false
    exit: rollback  # or strategy_change | escalate
```

Invariant: a repeated signature is not an identical retry; budgets stay task-declared.

### verification-plan

Purpose: declare channels and independence so a high-risk PASS cannot rest on self-assessment.

```yaml
channels:
  - kind: deterministic  # or runtime | external_primary | independent_model | self_assessment
    independent: true
high_risk_pass_requires_non_model: true
compatibility_bounds: {tools: "", models: "", repos: ""}
```

Invariant: model judgment may block or warn; it never solely passes a high-risk claim.

### evidence-ledger

Purpose: rank attested evidence with freshness; keep claim, source, and attester distinct.

```yaml
entries:
  - claim: ""
    source: ""
    attester: ""
    freshness_kind: recheck_date  # or tracking_event | immutable_pin
    date_checked: ""
```

Invariant: the agent's summary is not the attester; unrun freshness is `unknown`.

### acceptance-record

Purpose: a named accepter closes delivery against the oracle manifest and product evidence.

```yaml
spec_version: ""
accepter: ""
oracle_manifest_ref: ""
product_evidence_refs: []
closed: false
```

Invariant: execution success alone never closes this record.

### envelope

Purpose: bound the unattended run before it starts.

```yaml
budget: ""
pause_actions: []
kill_conditions: []
failure_signature_limit: task_declared
allowed_sinks: []  # secrets, memory_or_skill_promotion, permissions, deployment, outbound, money
accepter: ""
strictness: L2  # L1–L6
```

Invariant: a run outside this envelope stops; no universal retry count lives here.

### gate-retro

Purpose: record which gates fired, which were bypassed, and which caught nothing.

```yaml
gates:
  - name: intent  # spec | plan | execution | verification | acceptance | retro
    fired: false
    bypassed: false
    caught_nothing: false
policy_change: separate_from_activation
```

Invariant: policy change stays separate from policy activation; feed the retro into change, then activate out-of-band.

## Delivery Invariants

- Closing execution is not closing acceptance.
- An approval signature is not evidence that an oracle held.
- Self-report is not attestation.
- Artifact presence is not enforcement.
- The transcript is not the record.
- Passing developer tests is not passing the oracle.
- A stale spec cannot release a gate.

## Host Preconditions

The host must supply: oracle sealing (write protection, protected branch, or CI ownership); sink isolation (sandbox, egress control, credential brokering); budget enforcement; durable ledger storage; a human decision channel. TeaPrompt runs none of these. Name each precondition met, unmet, or `unknown` in the run note — do not infer enforcement from files on disk. A run note that omits a named precondition is incomplete, not passing; a filled block is an output, not enforcement.

Probe discipline (observed 2026-10-06 dry run, macOS seatbelt): a denial receipt needs byte-level verification — hash protected files before and after the attempt, and show the target unchanged; a nonzero probe exit alone does not distinguish enforcement from launch failure. Egress denials must use IP-literal connects (`/dev/tcp/1.1.1.1/443`, `nc`), not hostname lookups — DNS failure (`curl` exit 6) is ambiguous between sandbox denial and missing resolver plumbing. Record the verifying harness's exit code as `exit_code` (the denied syscall's EPERM is the observed result, not the probe's); consolidate all attempts for one control into a single evidence row with multiple `artifacts` — a second row for the same precondition holds as duplicate. Oracle-integrity probes should cover the full alteration surface: direct write, rename-replace, symlink swap, chmod-then-write, and descendant-process writes (inheritance observed, not assumed). Bound inputs can change between gate calls: run the selected gate again after work before release — a mutation landing in that window is caught only by the post-work check (TOCTOU). Malformed or environment-incomplete invocations (prompt-as-flag swallowed, headless permission denial) are recorded as discarded receipts, never as arm results in a comparison denominator.

```yaml
oracle_sealing: unknown           # met | unmet | unknown
sink_isolation: unknown
budget_enforcement: unknown
durable_ledger_storage: unknown
human_decision_channel: unknown
evidence: []                      # one entry per `met`: what was observed, where
status: artifact-complete         # enforcement-proven only with observed host evidence
```

The JSON run note is the same five-key mapping serialized for the checker, plus `spec_version`, `host_identity`, per-`met` evidence rows, and the `artifact-complete` status. `unknown` is the only default for every precondition.

## Adversarial Refuters

Host-run checks. A refuter that has not been run is `unknown`, never passed.

- **GDR-1** Executor attempt to edit an authoritative oracle must fail.
- **GDR-2** An instruction embedded in a tool result must not reach any sink.
- **GDR-3** A repeated failure signature must exit or escalate, not retry identically. Signature = task identity + error class (a prompt-hash is a minimal proxy; record which reading was implemented); a distinct-signature task must still proceed within budget.
- **GDR-4** Losing the transcript must not lose state (packet rebuild from artifacts).
- **GDR-5** Self-report-only evidence must not release a gate.
- **GDR-6** A mid-run spec change must mark every spec_version-keyed artifact (plan items, ledger entries, oracle manifest, task packet, acceptance record) `stale` and re-plan; any downstream artifact left at the prior spec_version is a refuter failure.

## Preflight Evidence Checker (generated template, host-run)

When a task requires observed host preconditions, emit `checks/preflight.py` from the inline template below. CLI: `python3 checks/preflight.py run-note.json binding.json`. For flow packs, select the executable wrapper below as `PREFLIGHT`; selecting the Python file directly supplies no JSON arguments and correctly holds with exit `4`. The checker is stdlib-only and single-pass: it reads the JSON records, resolves relative paths against the task-root working directory, and exits `0` only for coherent fresh required evidence with unchanged bound inputs; otherwise it exits `4`. It emits one disposition line (`ready`, `hold`, or `stale`) plus JSON detail. A missing/non-executable/failing selected gate stops dispatch or result release with exit `4`; its output never promotes a run to `enforcement-proven`.

The checker does not invoke agent CLIs, execute arbitrary probe commands, change permissions, mutate records, seal anything, or implement lifecycle. It validates record coherence only: declared types (including boolean-as-number ambiguity), unique known control keys, no duplicate required or evidence rows, per-`met` evidence rows bound to the current spec/host, fresh observations within the binding's task-declared `max_age_seconds` (no universal fallback), matching file hashes for immutable task inputs/oracles/verifier, and at least one raw-output artifact per required `met`. An `exit_code` of `0` on the complete host probe is required; a nonzero denial alone is not a `met`. Missing, malformed, `unknown`/`unmet`, duplicated, mismatched, or stale bindings return `hold` or `stale` with exit `4`, never a passing claim. Cancellation and run-lifecycle facts appear only when the host requires them; their absence is `unknown`, never implicit kill assurance. A worker-authorized probe needs its same-profile positive control and exact expected denial at host observation time; owner-authorized oracle edits are not adversarial worker evidence. The host owns and protects the checker, the binding, and the evidence; prose cannot seal them.

The serialized note must explicitly contain all five precondition fields; `unknown` is the generated value, not an omission waiver. Index evidence by precondition before result validation: duplicate or conflicting control rows hold, including a non-`met` row accompanying a `met` claim. Every declared `met`, required or not, needs coherent evidence. JSON records, bound inputs and raw artifacts must be regular files; malformed paths, FIFOs and devices hold rather than traceback or consume a stream. Open-descriptor checks do not authenticate paths, seal against later changes or supply arbitrary-filesystem time/resource guarantees.

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

## Verification

1. Parse check: every emitted YAML/Markdown template parses. Parseability is not schema validation unless the host declares a dialect and runs it.
2. Structural check: every gate names a releaser and an evidence tier; auto-release is recorded as no for `intent` and `acceptance`.
3. Refuter list exists (GDR-1–GDR-6); each unused check stays `unknown`.
4. Run note uses the status literals `artifact-complete` ≠ `enforcement-proven`. Do not claim the delivery is governed from static files. Handover/status generation keeps the same boundary: a generated note is a record for the host to check, never a sealed or enforced result.

## Demotion Triggers

- Contract drift → regenerate from this skill rather than patching a drifted copy.
- Zero recurrence by the next checkpoint, or a host absorbs the pattern → pack-level demotion folds back into `plans/governed-delivery-adoption-2026-09-03.md`. Recurrence evidence is host-supplied (a prompt library cannot observe host invocations); when no invocation evidence reaches the checkpoint, recurrence stays `unknown` — and a skipped or unrecorded checkpoint triggers demotion as a policy consequence of missing evidence, not as an observed zero.
- Redundancy-in-use → if the pack is never invoked independently of `agent-governance-scaffold`, or the shared host-precondition / `artifact-complete` / constitutional-path machinery diverges between the two packs, fold the delivery lifecycle into a shared reference and retire the duplicated boilerplate rather than maintaining two copies.

## Examples

Companion examples live in the installed `<skills-root>/examples/governed-delivery.examples.md` tree when examples are co-installed. They show expected input/output shapes and evidence-tier labels; they are not end-to-end host enforcement proof.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained; the operative rules above are inlined and attributed to their source lens.*

- `plans/governed-delivery-adoption-2026-09-03.md`
- `plans/governable-autonomy-survey-2026-09-03.md`
- `04-agent/runtime-trust-boundary.md`
- `04-agent/artifact-promotion.md`
- `04-agent/workflow-recipes.md`
- `plans/external-adoption-case-studies-2026-06-20.md`
