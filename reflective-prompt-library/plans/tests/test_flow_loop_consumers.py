"""Consumer regressions for loop evidence, content progress and unattended floors.

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
    env = dict(os.environ, AGENT_CMD=str(state / "agent.sh"), STATE="./state", **config)
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


@pytest.mark.parametrize("floor", ["missing", "not-executable", "passing"])
def test_unattended_floor_preflight_precedes_every_agent_call(tmp_path: Path, floor: str):
    _workspace(tmp_path, git=False)
    for name in ("draft", "critic-rubric", "revise"):
        (tmp_path / "prompts" / f"{name}.md").write_text(name + "\n", encoding="utf-8")
    floor_path = tmp_path / "checks/links-resolve.sh"
    if floor != "missing":
        _executable(floor_path, "exit 0\n")
        if floor == "not-executable":
            floor_path.chmod(0o644)
    agent = COUNT + 'case "$prompt" in critic-rubric*) echo ACCEPT;; *) echo clean-draft;; esac\n'
    result = _run(tmp_path, _unattended_writer(), agent, MAX_ROUNDS="1")
    calls = tmp_path / "state/calls"
    if floor == "passing":
        assert result.returncode == 0, result.stderr
        assert calls.read_text().strip() == "2"
        assert (tmp_path / "state/final.md").read_text() == "clean-draft\n"
    else:
        assert result.returncode == 4, result.stderr
        assert not calls.exists()
        assert not (tmp_path / "state/final.md").exists()
