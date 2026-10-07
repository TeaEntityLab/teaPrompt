"""Selected-preflight gate consumers: failure before work, mutation after work,
initial-success bypass, and quorum-swallowing for loop templates.

Execute the published bash recipes with offline stdin-only stubs in isolated
workspaces. These checks do not prove host write exclusions or model quality.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from prompt_eval_helpers import library_skills_dir  # noqa: E402

pytestmark = pytest.mark.skipif(
    shutil.which("bash") is None or shutil.which("git") is None,
    reason="bash/git not available",
)


def _source() -> str:
    return (library_skills_dir() / "flow-loop-harness" / "SKILL.md").read_text(encoding="utf-8")


def _template(name: str) -> str:
    section = _source().split(f"## Template: {name}\n", 1)[1].split("\n## ", 1)[0]
    return re.search(r"```bash\n(.*?)\n```", section, re.S).group(1) + "\n"


def _executable(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("#!/bin/sh\n" + body, encoding="utf-8")
    path.chmod(0o755)


def _workspace(d: Path, *, git: bool = True, verify: str = "echo constant-diagnostic; exit 1\n") -> None:
    (d / "prompts").mkdir(parents=True)
    (d / "prompts" / "fix.md").write_text("fix\n", encoding="utf-8")
    (d / "work.txt").write_text("baseline\n", encoding="utf-8")
    _executable(d / "checks" / "verify.sh", verify)
    if git:
        _git(d, "init", "-q")
        _git(d, "add", ".")
        _git(d, "commit", "-qm", "baseline")


def _git(d: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid", *args],
        cwd=d, check=True, capture_output=True,
    )


def _run(d: Path, script: str, agent: str, **config: str) -> subprocess.CompletedProcess:
    # Scripts/stubs are run-state, so their existence cannot mask a stalled workspace.
    state = d / "state"
    state.mkdir(exist_ok=True)
    _executable(state / "agent.sh", 'prompt="$(cat)"\n' + agent)
    (state / "driver.sh").write_text(script, encoding="utf-8")
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(state / "agent.sh"), "STATE": "./state", **config}
    return subprocess.run(
        ["bash", "state/driver.sh"], cwd=d, env=env,
        capture_output=True, text=True, timeout=60,
    )


COUNT = ('n=0; [ ! -f state/calls ] || n="$(cat state/calls)"\n'
         'n=$((n+1)); echo "$n" > state/calls\n')


@pytest.mark.parametrize("action", [
    'printf "stage%03d\\n" "$n" > work.txt\n',
    'printf "stage%03d\\n" "$n" > new.txt\n',
    'printf "stage%03d\\n" "$n" > work.txt; git add work.txt\n',
    'case "$n" in 1) mv work.txt renamed.txt;; 2) rm renamed.txt;; esac\n',
])
def test_fix_content_progress_survives_equal_churn_and_file_transitions(tmp_path: Path, action: str):
    _workspace(tmp_path)
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"), COUNT + action, MAX_ITER="2")
    assert result.returncode == 2, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "2"
    assert "NO PROGRESS" not in (tmp_path / "state/ledger.md").read_text()


def test_fix_staged_and_unstaged_cancellation_is_still_a_change(tmp_path: Path):
    _workspace(tmp_path)
    action = ('case "$n" in\n'
              '1) echo changed > work.txt; git add work.txt; echo baseline > work.txt;;\n'
              '2) echo revised > work.txt; git add work.txt; echo baseline > work.txt;;\n'
              'esac\n')
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"), COUNT + action, MAX_ITER="2")
    assert result.returncode == 2, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "2"


def test_fix_state_logs_and_probes_do_not_mask_real_stall(tmp_path: Path):
    _workspace(tmp_path)
    # Exclusion must cover tracked/staged STATE as well as new state files.
    (tmp_path / "state").mkdir()
    (tmp_path / "state/probe.txt").write_text("old\n")
    _git(tmp_path, "add", "state/probe.txt")
    _git(tmp_path, "commit", "-qm", "tracked run-state fixture")
    result = _run(
        tmp_path, _template("Verify-Gated Fix Loop (bash)"),
        COUNT + 'echo changed > state/probe.txt; git add state/probe.txt; echo output\n', MAX_ITER="3",
    )
    assert result.returncode == 3, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "1"
    assert "NO PROGRESS" in (tmp_path / "state/ledger.md").read_text()


def test_non_git_constant_diagnostic_is_not_workspace_stall(tmp_path: Path):
    _workspace(tmp_path, git=False)
    result = _run(
        tmp_path, _template("Verify-Gated Fix Loop (bash)"),
        COUNT + 'printf "stage%03d\\n" "$n" > work.txt\n', MAX_ITER="2",
    )
    assert result.returncode == 2, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "2"
    assert "progress disabled" in (tmp_path / "state/flow.log").read_text()
    assert "NO PROGRESS" not in (tmp_path / "state/ledger.md").read_text()


def test_backlog_retires_equal_churn_content_changes(tmp_path: Path):
    _workspace(tmp_path, verify="exit 0\n")
    (tmp_path / "TASKS.md").write_text("first\nsecond\n", encoding="utf-8")
    _git(tmp_path, "add", "TASKS.md")
    _git(tmp_path, "commit", "-qm", "backlog")
    result = _run(
        tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
        COUNT + 'printf "stage%03d\\n" "$n" > work.txt\n', MAX_ITER="3",
    )
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "state/TASKS.canon").read_text() == ""
    assert (tmp_path / "state/calls").read_text().strip() == "2"
    assert "- done: second" in (tmp_path / "state/ledger.md").read_text()


def test_backlog_last_task_retired_on_final_iteration_is_success(tmp_path: Path):
    """Retiring the only task at i == MAX_ITER is completion, not cap exhaustion."""
    _workspace(tmp_path, verify="exit 0\n")
    (tmp_path / "TASKS.md").write_text("only\n", encoding="utf-8")
    _git(tmp_path, "add", "TASKS.md")
    _git(tmp_path, "commit", "-qm", "backlog")
    result = _run(
        tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
        COUNT + 'printf "stage%03d\\n" "$n" > work.txt\n', MAX_ITER="1",
    )
    assert result.returncode == 0, result.stderr
    assert "backlog empty" in result.stdout
    assert "- done: only" in (tmp_path / "state/ledger.md").read_text()


def test_backlog_missing_canon_mid_run_fails_closed(tmp_path: Path):
    """Deleting state/TASKS.canon between iterations must not read as success."""
    _workspace(tmp_path, verify="exit 0\n")
    (tmp_path / "TASKS.md").write_text("first\nsecond\n", encoding="utf-8")
    _git(tmp_path, "add", "TASKS.md")
    _git(tmp_path, "commit", "-qm", "backlog")
    result = _run(
        tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
        COUNT + 'rm -f state/TASKS.canon; echo changed > work.txt\n', MAX_ITER="3",
    )
    assert result.returncode == 4, result.stdout + result.stderr
    assert "canonical backlog missing" in (tmp_path / "state/ledger.md").read_text()


FAIL_GATE = "exit 1\n"


def _gate(d: Path, body: str = "exit 0\n", *, executable: bool = True) -> str:
    path = d / "checks" / "preflight-gate"
    _executable(path, body)
    if not executable:
        path.chmod(0o644)
    return str(path)



@pytest.mark.parametrize("all_bad", [False, True])
def test_wave_only_current_nonempty_successful_evidence_reaches_final(tmp_path: Path, all_bad: bool):
    _workspace(tmp_path, git=False, verify='test -f state/summary.md\n')
    wave = tmp_path / "prompts/wave"
    wave.mkdir()
    for name in ("good", "failed", "empty"):
        (wave / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    state = tmp_path / "state"
    state.mkdir()
    for name in ("w1-ghost.md", "summary.md", "final.md"):
        (state / name).write_text("STALE-DELETED-BRANCH\n", encoding="utf-8")
    (state / "ledger.md").write_text("- prior run\n", encoding="utf-8")
    good = "exit 0" if all_bad else "echo CURRENT-GOOD"
    agent = ('case "$prompt" in *STALE-DELETED-BRANCH*) echo stale-input >&2; exit 1;; esac\n'
             'case "$prompt" in\nfailed*) echo FAILED-EVIDENCE; exit 1;;\nempty*) exit 0;;\n'
             f'good*) {good};;\nesac\n')
    result = _run(tmp_path, _template("Multi-Wave Fan-out (bash)"), agent, VERIFY="./checks/verify.sh", MAX_WAVES="1", MAX_JOBS="2")
    ledger = (state / "ledger.md").read_text()
    assert ledger.startswith("- prior run\n- RESUMED ")
    assert f"{3 if all_bad else 2}/3 branches failed or empty" in ledger
    if all_bad:
        assert result.returncode == 3, result.stderr
        assert not (state / "summary.md").exists()
        assert not (state / "final.md").exists()
    else:
        assert result.returncode == 0, result.stderr
        final = (state / "final.md").read_text()
        assert "CURRENT-GOOD" in final
        assert "STALE-DELETED-BRANCH" not in final
        assert "FAILED-EVIDENCE" not in final
        assert "w1-empty.md" not in final
        assert "w1-failed.md" not in final


def _unattended_writer() -> str:
    script = _template("Evaluator-Optimizer / Writer-Critic (bash)")
    section = _source().split("### Deterministic companion check", 1)[1].split("\n## ", 1)[0]
    preflight, gate = re.findall(r"```bash\n(.*?)\n```", section, re.S)
    marker = "# UNATTENDED PREFLIGHT: insert companion block here, before the draft call."
    script = script.replace(marker, marker + "\n" + preflight)
    return re.sub(
        r'  if \[ "\$\(sed .*?\n  fi', gate, script, count=1, flags=re.S,
    )


@pytest.mark.parametrize("floor", ["missing", "not-executable", "passing", "rejecting"])
def test_unattended_floor_preflight_precedes_every_agent_call(tmp_path: Path, floor: str):
    _workspace(tmp_path, git=False)
    for name in ("draft", "critic-rubric", "revise"):
        (tmp_path / "prompts" / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    floor_path = tmp_path / "checks/links-resolve.sh"
    if floor != "missing":
        _executable(floor_path, "exit 1\n" if floor == "rejecting" else "exit 0\n")
        if floor == "not-executable":
            floor_path.chmod(0o644)
    agent = COUNT + 'case "$prompt" in critic-rubric*) echo ACCEPT;; *) echo clean-draft;; esac\n'
    result = _run(tmp_path, _unattended_writer(), agent, MAX_ROUNDS="1")
    calls = tmp_path / "state/calls"
    if floor == "passing":
        assert result.returncode == 0, result.stderr
        assert calls.read_text().strip() == "2"
        assert (tmp_path / "state/final.md").read_text() == "clean-draft\n"
    elif floor == "rejecting":
        assert result.returncode == 2, result.stderr
        assert calls.read_text().strip() == "3"
        assert not (tmp_path / "state/final.md").exists()
    else:
        assert result.returncode == 4, result.stderr
        assert not calls.exists()
        assert not (tmp_path / "state/final.md").exists()


def test_fix_selected_gate_failure_blocks_first_dispatch(tmp_path: Path):
    _workspace(tmp_path)
    gate = _gate(tmp_path, FAIL_GATE)
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"), COUNT + 'echo changed > work.txt\n',
                  MAX_ITER="2", PREFLIGHT=gate)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()
    assert "preflight gate=1" in (tmp_path / "state/flow.log").read_text()


def test_fix_gate_mutation_after_work_blocks_acceptance(tmp_path: Path):
    _workspace(tmp_path)
    gate = _gate(tmp_path, '[ -z "$(ls state/iter-*-out.md 2>/dev/null)" ]\n')
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"),
                  COUNT + 'echo changed > work.txt; echo done\n', MAX_ITER="2",
                  VERIFY="./checks/verify.sh", PREFLIGHT=gate)
    assert result.returncode == 4, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "1"
    assert "- iter 1: VERIFIED" not in (tmp_path / "state/ledger.md").read_text()


def test_fix_zero_call_already_verified_still_checks_gate(tmp_path: Path):
    _workspace(tmp_path, verify="exit 0\n")
    gate = _gate(tmp_path, FAIL_GATE)
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"), COUNT + 'echo changed > work.txt\n',
                  MAX_ITER="2", PREFLIGHT=gate)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()


def test_fix_empty_gate_preserves_attended_path(tmp_path: Path):
    _workspace(tmp_path)
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"),
                  COUNT + 'printf "stage%03d\\n" "$n" > work.txt\n', MAX_ITER="2")
    assert result.returncode == 2, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "2"


def test_backlog_gate_failure_before_work_retires_nothing(tmp_path: Path):
    _workspace(tmp_path, verify="exit 0\n")
    (tmp_path / "TASKS.md").write_text("first\nsecond\n", encoding="utf-8")
    gate = _gate(tmp_path, FAIL_GATE)
    result = _run(tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
                  COUNT + 'echo changed > work.txt\n', MAX_ITER="3", PREFLIGHT=gate)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()
    assert (tmp_path / "state/TASKS.canon").read_text() == "first\nsecond\n"


def test_backlog_zero_call_empty_queue_still_checks_gate(tmp_path: Path):
    _workspace(tmp_path, verify="exit 0\n")
    (tmp_path / "TASKS.md").write_text("", encoding="utf-8")
    gate = _gate(tmp_path, FAIL_GATE)
    result = _run(tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
                  COUNT + 'echo changed > work.txt\n', MAX_ITER="3", PREFLIGHT=gate)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()


def test_wave_partial_policy_cannot_swallow_gate_failure(tmp_path: Path):
    _workspace(tmp_path, git=False, verify='test -f state/summary.md\n')
    wave = tmp_path / "prompts/wave"
    wave.mkdir()
    for name in ("good", "other"):
        (wave / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    gate = _gate(tmp_path, FAIL_GATE)
    agent = 'case "$prompt" in good*) echo GOOD;; *) echo OTHER;; esac\n'
    result = _run(tmp_path, _template("Multi-Wave Fan-out (bash)"), agent,
                  VERIFY="./checks/verify.sh", MAX_WAVES="1", MAX_JOBS="2", PREFLIGHT=gate)
    assert result.returncode == 4, result.stderr
    assert "preflight gate=4" in (tmp_path / "state/ledger.md").read_text()
    assert not (tmp_path / "state/final.md").exists()


@pytest.mark.parametrize("unattended", [False, True])
@pytest.mark.parametrize(("verdict", "accepted"), [
    ("ACCEPT\nREJECT\n", False),
    ("\nACCEPT\n\n", True),
])
def test_writer_requires_the_whole_critique_to_accept(
    tmp_path: Path, unattended: bool, verdict: str, accepted: bool,
):
    _workspace(tmp_path, git=False)
    for name in ("draft", "critic-rubric", "revise"):
        (tmp_path / "prompts" / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    (tmp_path / "critique.txt").write_text(verdict, encoding="utf-8")
    if unattended:
        _executable(tmp_path / "checks/links-resolve.sh", "exit 0\n")
    agent = COUNT + 'case "$prompt" in critic-rubric*) cat critique.txt;; *) echo clean-draft;; esac\n'
    script = _unattended_writer() if unattended else _template("Evaluator-Optimizer / Writer-Critic (bash)")
    result = _run(tmp_path, script, agent, MAX_ROUNDS="1")
    assert result.returncode == (0 if accepted else 2), result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == ("2" if accepted else "3")
    if accepted:
        assert (tmp_path / "state/final.md").read_text() == "clean-draft\n"
    else:
        assert not (tmp_path / "state/final.md").exists()


@pytest.mark.parametrize("template", [
    "Verify-Gated Fix Loop (bash)",
    "Task-Ledger Backlog Loop (bash, ralph-style)",
    "Multi-Wave Fan-out (bash)",
])
@pytest.mark.parametrize("broken", ["missing", "not-executable"])
def test_declared_broken_verifier_holds_before_loop_work(
    tmp_path: Path, template: str, broken: str,
):
    _workspace(tmp_path, git=False)
    (tmp_path / "TASKS.md").write_text("complete task\n", encoding="utf-8")
    (tmp_path / "prompts/wave").mkdir()
    (tmp_path / "prompts/wave/worker.md").write_text("worker\n", encoding="utf-8")
    verifier = tmp_path / "checks/declared-verify"
    if broken == "not-executable":
        _executable(verifier, "exit 0\n")
        verifier.chmod(0o644)
    result = _run(
        tmp_path, _template(template), COUNT + "echo work\n",
        VERIFY="./checks/declared-verify", MAX_ITER="1", MAX_WAVES="1",
    )
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()
    assert not (tmp_path / "state/final.md").exists()


@pytest.mark.parametrize("changing", [False, True])
def test_wave_stall_uses_evidence_not_changing_wave_headers(tmp_path: Path, changing: bool):
    _workspace(tmp_path, git=False)
    (tmp_path / "prompts/wave").mkdir()
    (tmp_path / "prompts/wave/worker.md").write_text("worker\n", encoding="utf-8")
    agent = COUNT + ('echo "EVIDENCE-$n"\n' if changing else "echo SAME-EVIDENCE\n")
    result = _run(
        tmp_path, _template("Multi-Wave Fan-out (bash)"), agent,
        VERIFY="./checks/verify.sh", MAX_WAVES="3",
    )
    assert result.returncode == (2 if changing else 3), result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == ("3" if changing else "2")
    assert not (tmp_path / "state/final.md").exists()


@pytest.mark.parametrize("cap", ["00", "08", "0", "", "0x2", "-1", "2 ", " 2", "2.0", "9999999999"])
def test_fix_noncanonical_max_iter_is_configuration_hold(tmp_path: Path, cap: str):
    _workspace(tmp_path)
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"), COUNT + "echo changed > work.txt\n", MAX_ITER=cap)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()


def test_fix_canonical_cap_still_dispatches(tmp_path: Path):
    _workspace(tmp_path)
    result = _run(tmp_path, _template("Verify-Gated Fix Loop (bash)"), COUNT + 'printf "stage%03d\\n" "$n" > work.txt\n', MAX_ITER="2")
    assert result.returncode == 2, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "2"


def test_fix_expression_cap_expands_nothing(tmp_path: Path):
    _workspace(tmp_path)
    (tmp_path / "r").write_text("1\n", encoding="utf-8")
    result = _run(
        tmp_path, _template("Verify-Gated Fix Loop (bash)"),
        COUNT + "echo changed > work.txt\n",
        MAX_ITER="r[$(printf marker > state/arithmetic-expanded)]",
    )
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()
    assert not (tmp_path / "state/arithmetic-expanded").exists()


@pytest.mark.parametrize("cap", ["00", "08", "0", "", "0x1", "-1", "9999999999"])
def test_writer_noncanonical_max_rounds_is_configuration_hold(tmp_path: Path, cap: str):
    _workspace(tmp_path, git=False)
    for name in ("draft", "critic-rubric", "revise"):
        (tmp_path / "prompts" / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    result = _run(
        tmp_path, _template("Evaluator-Optimizer / Writer-Critic (bash)"),
        COUNT + "echo clean-draft\n", MAX_ROUNDS=cap,
    )
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()
    assert not (tmp_path / "state/final.md").exists()


def test_writer_expression_rounds_expands_nothing(tmp_path: Path):
    _workspace(tmp_path, git=False)
    for name in ("draft", "critic-rubric", "revise"):
        (tmp_path / "prompts" / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    agent = COUNT + 'case "$prompt" in critic-rubric*) echo ACCEPT;; *) echo clean-draft;; esac\n'
    result = _run(
        tmp_path, _template("Evaluator-Optimizer / Writer-Critic (bash)"), agent,
        MAX_ROUNDS="r[$(printf marker > state/arithmetic-expanded)]",
    )
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()
    assert not (tmp_path / "state/arithmetic-expanded").exists()


@pytest.mark.parametrize("cap", ["00", "08", "0", "", "-1", "9999999999"])
def test_wave_noncanonical_caps_are_configuration_holds(tmp_path: Path, cap: str):
    _workspace(tmp_path, git=False)
    (tmp_path / "prompts/wave").mkdir()
    (tmp_path / "prompts/wave/worker.md").write_text("worker\n", encoding="utf-8")
    result = _run(
        tmp_path, _template("Multi-Wave Fan-out (bash)"), COUNT + "echo work\n",
        VERIFY="./checks/verify.sh", MAX_WAVES=cap, MAX_JOBS="2",
    )
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/calls").exists()
    result = _run(
        tmp_path, _template("Multi-Wave Fan-out (bash)"), COUNT + "echo work\n",
        VERIFY="./checks/verify.sh", MAX_WAVES="1", MAX_JOBS=cap,
    )
    assert result.returncode == 4, result.stderr


def test_wave_canonical_caps_still_dispatch(tmp_path: Path):
    _workspace(tmp_path, git=False)
    (tmp_path / "prompts/wave").mkdir()
    (tmp_path / "prompts/wave/worker.md").write_text("worker\n", encoding="utf-8")
    result = _run(
        tmp_path, _template("Multi-Wave Fan-out (bash)"), COUNT + "echo SAME-EVIDENCE\n",
        VERIFY="./checks/verify.sh", MAX_WAVES="3", MAX_JOBS="2",
    )
    assert result.returncode == 3, result.stderr
    assert (tmp_path / "state/calls").read_text().strip() == "2"


def test_backlog_directory_canon_is_read_error_not_empty(tmp_path: Path):
    _workspace(tmp_path, verify="exit 0\n")
    (tmp_path / "TASKS.md").write_text("an unfinished task\n", encoding="utf-8")
    (tmp_path / "state").mkdir(exist_ok=True)
    (tmp_path / "state/TASKS.canon").mkdir(exist_ok=True)
    result = _run(
        tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
        COUNT + "echo changed > work.txt\n", MAX_ITER="3",
    )
    assert result.returncode == 4, result.stdout + result.stderr
    assert "unreadable" in (result.stdout + result.stderr)
    assert "backlog empty" not in result.stdout
    assert not (tmp_path / "state/calls").exists()


def test_backlog_missing_canon_is_configuration_hold(tmp_path: Path):
    _workspace(tmp_path, git=False, verify="exit 0\n")
    result = _run(
        tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
        COUNT + "echo changed > work.txt\n", MAX_ITER="3",
    )
    assert result.returncode == 4, result.stdout + result.stderr
    assert "canonical backlog missing" in (result.stdout + result.stderr)
    assert not (tmp_path / "state/calls").exists()


def test_backlog_normal_file_still_retires(tmp_path: Path):
    _workspace(tmp_path, verify="exit 0\n")
    (tmp_path / "TASKS.md").write_text("only\n", encoding="utf-8")
    _git(tmp_path, "add", "TASKS.md")
    _git(tmp_path, "commit", "-qm", "backlog")
    result = _run(
        tmp_path, _template("Task-Ledger Backlog Loop (bash, ralph-style)"),
        COUNT + 'printf "stage%03d\\n" "$n" > work.txt\n', MAX_ITER="1",
    )
    assert result.returncode == 0, result.stderr
    assert "backlog empty" in result.stdout


@pytest.mark.parametrize("worker_exit", [1, 4, 127])
def test_writer_raw_worker_exit_is_distinct_from_configuration(tmp_path: Path, worker_exit: int):
    _workspace(tmp_path, git=False)
    for name in ("draft", "critic-rubric", "revise"):
        (tmp_path / "prompts" / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    result = _run(
        tmp_path, _template("Evaluator-Optimizer / Writer-Critic (bash)"),
        f"exit {worker_exit}\n", MAX_ROUNDS="2",
    )
    expected = 5 if worker_exit == 4 else worker_exit
    assert result.returncode == expected, result.stderr
    assert not (tmp_path / "state/final.md").exists()


def test_fix_raw_worker_exit_4_is_distinct_from_configuration(tmp_path: Path):
    _workspace(tmp_path)
    result = _run(
        tmp_path, _template("Verify-Gated Fix Loop (bash)"), "exit 4\n", MAX_ITER="2",
    )
    assert result.returncode == 5, result.stderr
    assert "- iter 1: worker failed agent-exit=4" in (tmp_path / "state/ledger.md").read_text()


@pytest.mark.parametrize("cap, expected", [
    ("999999999", 0), ("1000000000", 0), ("2147483647", 0), ("2147483648", 4),
])
def test_fix_cap_ceiling_does_not_truncate_valid_decimals(tmp_path: Path, cap: str, expected: int):
    _workspace(tmp_path, git=False, verify="exit 0\n")
    result = _run(
        tmp_path, _template("Verify-Gated Fix Loop (bash)"), COUNT + "exit 1\n", MAX_ITER=cap,
    )
    assert result.returncode == expected, result.stderr
    assert not (tmp_path / "state/calls").exists()
