"""Behavioral tests for the governed-delivery preflight checker template.

Execute the emitted checks/preflight.py template (extracted verbatim from
governed-delivery SKILL.md) against coherent and incoherent evidence in
isolated task-root workspaces. These checks exercise record-coherence
behavior only: they do not prove host write exclusions, event authenticity,
continuous sealing, model quality, or accepted delivery.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from prompt_eval_helpers import library_skills_dir  # noqa: E402

SKILL = library_skills_dir() / "governed-delivery" / "SKILL.md"
CONTROLS = (
    "oracle_sealing",
    "sink_isolation",
    "budget_enforcement",
    "durable_ledger_storage",
    "human_decision_channel",
)


def _template_source() -> str:
    text = SKILL.read_text(encoding="utf-8")
    section = text.split("### Template: checks/preflight.py", 1)[1]
    match = re.search(r"```python\n(.*?)```\n", section, re.S)
    assert match, "preflight template fence missing"
    body = match.group(1)
    return body + "\n"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _workspace(monkeypatch, tmp_path: Path) -> Path:
    monkeypatch.chdir(tmp_path)
    oracle = tmp_path / "oracle.md"
    oracle.write_text("pinned oracle\n", encoding="utf-8")
    raw = tmp_path / "raw" / "probe-sink_isolation.out"
    raw.parent.mkdir(parents=True)
    raw.write_text("sandbox egress denied as expected\n", encoding="utf-8")
    return oracle


def _write_checker(tmp_path: Path) -> Path:
    checks = tmp_path / "checks"
    checks.mkdir(exist_ok=True)
    checker = checks / "preflight.py"
    checker.write_text(_template_source(), encoding="utf-8")
    checker.chmod(0o755)
    return checker


def _evidence_row(
    tmp_path: Path,
    precondition: str,
    *,
    spec: str = "spec-7",
    host: str = "host-cli-1.0/profile-a",
    age_seconds: int = 60,
    exit_code=0,
    command=("probe", "--check", "sink"),
    principal: str = "executor:host-probe",
    raw_name: str = "probe-sink_isolation.out",
    result: str = "met",
) -> dict:
    raw = tmp_path / "raw" / raw_name
    if not raw.exists():
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text("probe output\n", encoding="utf-8")
    observed = (datetime.now(timezone.utc) - timedelta(seconds=age_seconds)).isoformat()
    return {
        "precondition": precondition,
        "result": result,
        "spec_version": spec,
        "host_identity": host,
        "observed_at": observed,
        "command": list(command),
        "principal": principal,
        "exit_code": exit_code,
        "artifacts": [{"path": str(raw.relative_to(tmp_path)), "sha256": _sha(raw)}],
    }


def _note(tmp_path: Path, required, *, spec="spec-7", host="host-cli-1.0/profile-a", rows=None) -> dict:
    statuses = {key: "unknown" for key in CONTROLS}
    for key in required:
        statuses[key] = "met"
    note = {
        "spec_version": spec,
        "host_identity": host,
        **statuses,
        "evidence": rows if rows is not None else [],
        "status": "artifact-complete",
    }
    return note


def _binding(tmp_path: Path, required, *, spec="spec-7", host="host-cli-1.0/profile-a",
              max_age=3600, files=None) -> dict:
    oracle = tmp_path / "oracle.md"
    pinned = {**(files or {})}
    if oracle.exists() and "oracle.md" not in pinned:
        pinned["oracle.md"] = _sha(oracle)
    return {
        "spec_version": spec,
        "host_identity": host,
        "required_preconditions": list(required),
        "max_age_seconds": max_age,
        "files": pinned,
    }


def _run(checker: Path, note: dict, binding: dict, tmp_path: Path):
    note_path = tmp_path / "run-note.json"
    binding_path = tmp_path / "binding.json"
    note_path.write_text(json.dumps(note), encoding="utf-8")
    binding_path.write_text(json.dumps(binding), encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(checker), str(note_path), str(binding_path)],
        capture_output=True, text=True, timeout=30,
    )
    first = proc.stdout.splitlines()[0] if proc.stdout.splitlines() else ""
    return proc, first


def test_coherent_evidence_is_ready(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation")]
    proc, first = _run(checker, _note(tmp_path, required, rows=rows), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert first == "ready"
    assert "enforcement-proven" not in proc.stdout


def test_met_without_evidence_is_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    proc, first = _run(checker, _note(tmp_path, required, rows=[]), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "without evidence" in proc.stdout


def test_unknown_required_is_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    note = _note(tmp_path, [], rows=[])
    proc, first = _run(checker, note, _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "unknown" in proc.stdout


def test_unmet_required_is_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    note = _note(tmp_path, [], rows=[])
    note["sink_isolation"] = "unmet"
    proc, first = _run(checker, note, _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "unmet" in proc.stdout


def test_stale_observation_is_stale(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation", age_seconds=7200)]
    proc, first = _run(checker, _note(tmp_path, required, rows=rows), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "stale"


def test_stale_spec_binding_is_stale(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation", spec="spec-8")]
    note = _note(tmp_path, required, spec="spec-8", rows=rows)
    proc, first = _run(checker, note, _binding(tmp_path, required, spec="spec-7"), tmp_path)
    assert proc.returncode == 4
    assert first == "stale"


def test_stale_host_binding_is_stale(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation", host="host-cli-2.0/profile-a")]
    note = _note(tmp_path, required, host="host-cli-2.0/profile-a", rows=rows)
    proc, first = _run(checker, note, _binding(tmp_path, required, host="host-cli-1.0/profile-a"), tmp_path)
    assert proc.returncode == 4
    assert first == "stale"


def test_mutated_oracle_is_stale(monkeypatch, tmp_path: Path):
    oracle = _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation")]
    binding = _binding(tmp_path, required)
    oracle.write_text("owner-edited oracle\n", encoding="utf-8")
    proc, first = _run(checker, _note(tmp_path, required, rows=rows), binding, tmp_path)
    assert proc.returncode == 4
    assert first == "stale"


def test_changed_raw_artifact_is_stale(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation")]
    note = _note(tmp_path, required, rows=rows)
    (tmp_path / "raw" / "probe-sink_isolation.out").write_text("rewritten bytes\n", encoding="utf-8")
    proc, first = _run(checker, note, _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "stale"


def test_denial_exit_code_is_not_a_met(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation", exit_code=1)]
    proc, first = _run(checker, _note(tmp_path, required, rows=rows), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "exit_code 0" in proc.stdout


def test_malformed_inputs_are_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    note_path = tmp_path / "run-note.json"
    binding_path = tmp_path / "binding.json"
    note_path.write_text("{not json", encoding="utf-8")
    binding_path.write_text(json.dumps(_binding(tmp_path, ["sink_isolation"])), encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(checker), str(note_path), str(binding_path)],
        capture_output=True, text=True, timeout=30,
    )
    assert proc.returncode == 4
    assert proc.stdout.splitlines()[0] == "hold"


def test_duplicate_required_rows_are_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation", "sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation")]
    proc, first = _run(checker, _note(tmp_path, ["sink_isolation"], rows=rows),
                        _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "duplicate" in proc.stdout


def test_duplicate_evidence_rows_are_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    row = _evidence_row(tmp_path, "sink_isolation")
    rows = [row, dict(row)]
    proc, first = _run(checker, _note(tmp_path, required, rows=rows), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "duplicate" in proc.stdout


def test_boolean_max_age_is_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation")]
    binding = _binding(tmp_path, required, max_age=True)
    proc, first = _run(checker, _note(tmp_path, required, rows=rows), binding, tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "max_age_seconds" in proc.stdout


def test_boolean_exit_code_is_not_zero(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation", exit_code=False)]
    proc, first = _run(checker, _note(tmp_path, required, rows=rows), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"


def test_impossible_proof_label_is_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation")]
    note = _note(tmp_path, required, rows=rows)
    note["status"] = "enforcement-proven"
    proc, first = _run(checker, note, _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "artifact-complete" in proc.stdout


def test_unknown_control_key_is_hold(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sandbox_escape_hatch"]
    proc, first = _run(checker, _note(tmp_path, [], rows=[]), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4
    assert first == "hold"
    assert "unknown keys" in proc.stdout


def test_cli_usage_error_is_hold():
    with tempfile.TemporaryDirectory() as td:
        checker = Path(td) / "preflight.py"
        checker.write_text(_template_source(), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(checker)], capture_output=True, text=True, timeout=30,
        )
        assert proc.returncode == 4
        assert proc.stdout.splitlines()[0] == "hold"


@pytest.mark.parametrize(
    "kind",
    ("nonfinite-age", "overflow-age", "timezone-missing", "timezone-overflow", "binding-proof", "duplicate-json-field"),
)
def test_ambiguous_or_unbounded_records_do_not_release(monkeypatch, tmp_path: Path, kind: str):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    rows = [_evidence_row(tmp_path, "sink_isolation")]
    note = _note(tmp_path, required, rows=rows)
    binding = _binding(tmp_path, required)
    if kind in ("nonfinite-age", "overflow-age"):
        binding["max_age_seconds"] = float("inf")
        rows[0]["observed_at"] = "2000-01-01T00:00:00+00:00"
    elif kind == "timezone-missing":
        rows[0]["observed_at"] = datetime.now(timezone.utc).replace(tzinfo=None).isoformat()
    elif kind == "timezone-overflow":
        rows[0]["observed_at"] = "0001-01-01T00:00:00+14:00"
    elif kind == "binding-proof":
        binding["status"] = "enforcement-proven"
    note_text = json.dumps(note)
    binding_text = json.dumps(binding)
    if kind == "duplicate-json-field":
        note_text = '{"sink_isolation": "unmet", ' + note_text[1:]
    elif kind == "overflow-age":
        binding_text = binding_text.replace("Infinity", "1e400")
    (tmp_path / "run-note.json").write_text(note_text, encoding="utf-8")
    (tmp_path / "binding.json").write_text(binding_text, encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(checker), "run-note.json", "binding.json"],
        capture_output=True, text=True, timeout=30,
    )
    assert proc.returncode == 4, proc.stdout + proc.stderr
    assert proc.stdout.splitlines()[0] == "hold"


def test_probe_commands_are_record_data_and_inputs_are_not_rewritten(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    row = _evidence_row(tmp_path, "sink_isolation")
    row["command"] = [
        sys.executable, "-c",
        "from pathlib import Path; Path('unexpected-probe-effect').write_text('executed')",
    ]
    inputs = [tmp_path / "oracle.md", tmp_path / "raw" / "probe-sink_isolation.out", checker]
    before = {path: (_sha(path), path.stat().st_mode) for path in inputs}
    proc, first = _run(checker, _note(tmp_path, required, rows=[row]), _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert first == "ready"
    assert not (tmp_path / "unexpected-probe-effect").exists()
    assert {path: (_sha(path), path.stat().st_mode) for path in inputs} == before


@pytest.mark.parametrize("result", ("unmet", ["met"]))
def test_conflicting_required_observations_cannot_release(monkeypatch, tmp_path: Path, result):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    row = _evidence_row(tmp_path, "sink_isolation")
    newer = dict(row, result=result, exit_code=1, observed_at=datetime.now(timezone.utc).isoformat())
    proc, first = _run(
        checker, _note(tmp_path, required, rows=[row, newer]), _binding(tmp_path, required), tmp_path,
    )
    assert proc.returncode == 4, proc.stdout + proc.stderr
    assert first == "hold"


@pytest.mark.parametrize("missing", tuple(key for key in CONTROLS if key != "sink_isolation"))
def test_note_cannot_omit_nonrequired_preconditions(monkeypatch, tmp_path: Path, missing: str):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    note = _note(tmp_path, required, rows=[_evidence_row(tmp_path, "sink_isolation")])
    del note[missing]
    proc, first = _run(checker, note, _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4, proc.stdout + proc.stderr
    assert first == "hold"


def test_optional_positive_claim_still_needs_evidence(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    note = _note(tmp_path, required, rows=[_evidence_row(tmp_path, "sink_isolation")])
    note["human_decision_channel"] = "met"
    proc, first = _run(checker, note, _binding(tmp_path, required), tmp_path)
    assert proc.returncode == 4, proc.stdout + proc.stderr
    assert first == "hold"


def test_unknown_evidence_control_is_not_silently_dropped(monkeypatch, tmp_path: Path):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    row = _evidence_row(tmp_path, "sink_isolation")
    unknown = dict(row, precondition="unregistered-control")
    proc, first = _run(
        checker, _note(tmp_path, required, rows=[row, unknown]), _binding(tmp_path, required), tmp_path,
    )
    assert proc.returncode == 4, proc.stdout + proc.stderr
    assert first == "hold"


@pytest.mark.parametrize("source", ("bound", "artifact"))
@pytest.mark.parametrize("bad_path", ("bad\x00path", "bad\ud800path"))
def test_malformed_file_sources_emit_hold_not_traceback(
    monkeypatch, tmp_path: Path, source: str, bad_path: str,
):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    row = _evidence_row(tmp_path, "sink_isolation")
    binding = _binding(tmp_path, required)
    if source == "bound":
        binding["files"][bad_path] = "0" * 64
    else:
        row["artifacts"][0]["path"] = bad_path
    proc, first = _run(checker, _note(tmp_path, required, rows=[row]), binding, tmp_path)
    assert proc.returncode == 4, proc.stdout + proc.stderr
    assert first == "hold"
    assert json.loads(proc.stdout.partition("\n")[2])["disposition"] == "hold"


@pytest.mark.skipif(os.name != "posix", reason="Published checker targets POSIX regular files")
@pytest.mark.parametrize("source", ("record-fifo", "bound-device", "artifact-device"))
def test_nonregular_file_sources_hold_without_consuming_streams(monkeypatch, tmp_path: Path, source: str):
    _workspace(monkeypatch, tmp_path)
    checker = _write_checker(tmp_path)
    required = ["sink_isolation"]
    row = _evidence_row(tmp_path, "sink_isolation")
    note = _note(tmp_path, required, rows=[row])
    binding = _binding(tmp_path, required)
    note_path = tmp_path / "run-note.json"
    if source == "record-fifo":
        os.mkfifo(note_path)
    else:
        if source == "bound-device":
            binding["files"]["/dev/zero"] = "0" * 64
        else:
            row["artifacts"][0]["path"] = "/dev/zero"
        note_path.write_text(json.dumps(note), encoding="utf-8")
    binding_path = tmp_path / "binding.json"
    binding_path.write_text(json.dumps(binding), encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(checker), str(note_path), str(binding_path)],
        capture_output=True, text=True, timeout=2,
    )
    assert proc.returncode == 4, proc.stdout + proc.stderr
    assert proc.stdout.splitlines()[0] == "hold"
    assert json.loads(proc.stdout.partition("\n")[2])["disposition"] == "hold"
