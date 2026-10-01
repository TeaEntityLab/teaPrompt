"""Consumer-visible plan identity, prompt-channel, router and DAG boundaries."""

from __future__ import annotations

import ast
import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from prompt_eval_helpers import library_skills_dir  # noqa: E402
from test_skill_verification_panel_record import DAG_TEMPLATE, ORCHESTRATOR_TEMPLATE  # noqa: E402


def _source() -> str:
    return (library_skills_dir() / "flow-control-generator" / "SKILL.md").read_text(encoding="utf-8")


def _executable(path: Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")
    path.chmod(0o755)


def _orchestrator(tmp_path: Path, plan: object, *, goal: str = "goal", state: str = "state"):
    (tmp_path / "checks").mkdir()
    (tmp_path / "goal.md").write_text(goal, encoding="utf-8")
    (tmp_path / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    (tmp_path / "orch.py").write_text(ORCHESTRATOR_TEMPLATE.search(_source()).group(1), encoding="utf-8")
    stub = tmp_path / "stub.py"
    stub.write_text(
        "import pathlib, sys\n"
        "body = sys.stdin.read()\n"
        "with pathlib.Path('calls.txt').open('a') as f: f.write(str(len(body)) + '\\n')\n"
        "if body.startswith('Decompose'):\n"
        "    pathlib.Path('planner-input.md').write_text(body)\n"
        "    sys.stdout.write(pathlib.Path('plan.json').read_text())\n"
        "elif body.startswith('Synthesize'):\n"
        "    sys.stdout.write(body)\n"
        "else:\n"
        "    print('WORK-' + body)\n",
        encoding="utf-8",
    )
    _executable(tmp_path / "checks" / "verify-merged.sh", '#!/bin/sh\ntest -s "$1"\n')
    env = dict(os.environ, AGENT_CMD=shlex.join([sys.executable, str(stub)]), STATE=state)
    result = subprocess.run(
        [sys.executable, "orch.py", "goal.md"], cwd=tmp_path, env=env,
        capture_output=True, text=True, timeout=30,
    )
    return result, tmp_path / state


@pytest.mark.parametrize("plan", [
    [{"id": "a", "task": "X"}, {"id": "a", "task": "Y"}],
    [{"id": "a/b", "task": "X"}, {"id": "ab", "task": "Y"}],
    ["not a task object"],
    [{"id": "a"}],
    [{"id": "a", "task": None}],
    [{"id": "a", "task": "   "}],
    [{"id": "", "task": "X"}],
    [{"id": "/", "task": "X"}],
    [{"id": 7, "task": "X"}],
])
def test_invalid_plan_is_rejected_before_worker_dispatch(tmp_path: Path, plan: object):
    result, state = _orchestrator(tmp_path, plan)
    assert result.returncode == 2, result.stderr
    assert not list(state.glob("worker-*.md"))
    assert not (state / "final.md").exists()
    assert len((tmp_path / "calls.txt").read_text().splitlines()) == 1


def test_distinct_worker_evidence_survives_sanitization(tmp_path: Path):
    result, state = _orchestrator(tmp_path, [
        {"id": "a/b", "task": "X"}, {"id": "c-d", "task": "Y"},
    ])
    assert result.returncode == 0, result.stderr
    final = (state / "final.md").read_text()
    assert "## ab\nWORK-X" in final
    assert "## c-d\nWORK-Y" in final
    assert (state / "worker-ab.md").read_text() == "WORK-X\n"
    assert (state / "worker-c-d.md").read_text() == "WORK-Y\n"


def test_case_insensitive_worker_id_collision_is_rejected(tmp_path: Path):
    """APFS/HFS+ default case-insensitivity maps A and a to one worker-a.md."""
    result, state = _orchestrator(tmp_path, [
        {"id": "A", "task": "X"}, {"id": "a", "task": "Y"},
    ])
    assert result.returncode == 2, result.stderr
    assert not list(state.glob("worker-*.md"))
    assert not (state / "final.md").exists()
    assert len((tmp_path / "calls.txt").read_text().splitlines()) == 1


def test_large_goal_uses_stdin_and_nested_state_is_created(tmp_path: Path):
    goal = "large-goal:" + "x" * (2 * 1024 * 1024)
    result, state = _orchestrator(tmp_path, [{"id": "a", "task": "X"}], goal=goal, state="deep/nested/state")
    assert result.returncode == 0, result.stderr
    assert "WORK-X" in (state / "final.md").read_text()
    calls = [int(line) for line in (tmp_path / "calls.txt").read_text().splitlines()]
    assert (tmp_path / "planner-input.md").read_text().endswith(goal)
    assert len(calls) == 3  # planner, one worker, synthesis; no fallback/retry


def _dag(tmp_path: Path, *, final_node: str = "assemble", fail_node: str = "", reverse: bool = False):
    # Three sibling sinks so topological tie-break never names the acceptance
    # node: forward order ends at report, reversed ends at lint; neither is
    # FINAL_NODE=assemble, so a regression to order[-1] gating fails both ways.
    nodes = {
        "spec": ((), "prompts/spec.md"),
        "api": (("spec",), "prompts/api.md"),
        "client": (("spec",), "prompts/client.md"),
        "lint": (("spec",), "prompts/lint.md"),
        "assemble": (("api", "client"), "prompts/assemble.md"),
        "report": (("spec",), "prompts/report.md"),
    }
    if reverse:
        nodes = dict(reversed(list(nodes.items())))
    tree = ast.parse(DAG_TEMPLATE.search(_source()).group(1))
    for statement in tree.body:
        if isinstance(statement, ast.Assign):
            names = [target.id for target in statement.targets if isinstance(target, ast.Name)]
            if "NODES" in names:
                statement.value = ast.parse(repr(nodes), mode="eval").body
            elif "FINAL_NODE" in names:
                statement.value = ast.Constant(final_node)
    (tmp_path / "dag.py").write_text(ast.unparse(ast.fix_missing_locations(tree)), encoding="utf-8")
    (tmp_path / "prompts").mkdir()
    (tmp_path / "checks").mkdir()
    for name in nodes:
        (tmp_path / "prompts" / f"{name}.md").write_text(name + "\n")
    stub = tmp_path / "stub.sh"
    _executable(stub,
        '#!/bin/sh\nprompt="$(cat)"\nprintf "%s\\n" "$prompt" >> calls.txt\n'
        'case "$prompt" in "$FAIL_NODE"*) [ -z "$FAIL_NODE" ] || exit 1;; esac\n'
        'printf "RESULT:%s\\n" "$prompt"\n')
    _executable(tmp_path / "checks" / "verify-merged.sh",
        '#!/bin/sh\nprintf "%s\\n" "$1" > gate-target.txt\n'
        'test -s "$1" && grep -q "^RESULT:assemble" "$1"\n')
    env = dict(os.environ, AGENT_CMD=str(stub), MIN_OK="3", FAIL_NODE=fail_node, STATE="deep/state")
    result = subprocess.run([sys.executable, "dag.py"], cwd=tmp_path, env=env,
                            capture_output=True, text=True, timeout=30)
    return result


@pytest.mark.parametrize("reverse", [False, True])
def test_multi_tail_dag_checks_explicit_merge_independent_of_order(tmp_path: Path, reverse: bool):
    result = _dag(tmp_path, reverse=reverse)
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "gate-target.txt").read_text() == "deep/state/assemble.out\n"


def test_quorum_cannot_replace_failed_final_node_with_other_tail(tmp_path: Path):
    result = _dag(tmp_path, fail_node="assemble")
    assert result.returncode == 2, result.stderr
    assert (tmp_path / "deep/state/report.out").is_file()
    assert not (tmp_path / "gate-target.txt").exists()


@pytest.mark.parametrize("final_node", ["missing", "spec"])
def test_missing_or_nonterminal_acceptance_node_is_configuration_failure(tmp_path: Path, final_node: str):
    result = _dag(tmp_path, final_node=final_node)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "calls.txt").exists()


def _router(tmp_path: Path, label: str):
    match = re.search(r"## Template: Conditional Router \(bash\)\n.*?```bash\n(.*?)\n```", _source(), re.S)
    (tmp_path / "router.sh").write_text(match.group(1))
    (tmp_path / "prompts").mkdir()
    (tmp_path / "input.md").write_text("user input\n")
    (tmp_path / "label.txt").write_text(label)
    (tmp_path / "prompts/classify.md").write_text("CLASSIFY\n")
    for route in ("bug", "feature", "question"):
        (tmp_path / "prompts" / f"route-{route}.md").write_text(f"ROUTE-{route}\n")
    stub = tmp_path / "stub.sh"
    _executable(stub,
        '#!/bin/sh\nprompt="$(cat)"\ncase "$prompt" in CLASSIFY*) cat label.txt;; '
        '*) printf "HANDLED:%s\\n" "$prompt" > handler-call.txt; cat handler-call.txt;; esac\n')
    env = dict(os.environ, AGENT_CMD=str(stub), STATE="state")
    return subprocess.run(["/bin/bash", "router.sh", "input.md"], cwd=tmp_path, env=env,
                          capture_output=True, text=True, timeout=30)


@pytest.mark.parametrize("label", ["bug2\n", "bug extra\n", "bug\nfeature\n", "bug\n\n", ""])
def test_invalid_classifier_cannot_authorize_a_route(tmp_path: Path, label: str):
    result = _router(tmp_path, label)
    assert result.returncode == 2, result.stderr
    assert not (tmp_path / "handler-call.txt").exists()
    assert (tmp_path / "state/label.txt").read_text() == label
    assert "route gate=2" in (tmp_path / "state/flow.log").read_text()


def test_whole_case_insensitive_classifier_label_routes_and_keeps_raw(tmp_path: Path):
    result = _router(tmp_path, "BUG\n")
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "state/final.md").read_text().startswith("HANDLED:ROUTE-bug\n")
    assert (tmp_path / "state/label.txt").read_text() == "BUG\n"
    trace = (tmp_path / "state/flow.log").read_text()
    assert "raw=" in trace and "BUG" in trace and "label=bug" in trace


def test_skill_source_stays_under_lint_warning_size():
    assert len(_source()) < 20_000
