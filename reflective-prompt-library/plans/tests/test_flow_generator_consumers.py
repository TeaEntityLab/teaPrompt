"""Selected-preflight gate consumers: failure before work, mutation after work,
initial-success bypass, and quorum-swallowing for generator templates.

Execute the published templates with offline stdin-only stubs in isolated
workspaces. These checks do not prove host write exclusions or model quality.
"""

from __future__ import annotations

import ast
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from prompt_eval_helpers import library_skills_dir  # noqa: E402
from test_skill_verification_panel_record import DAG_TEMPLATE, ORCHESTRATOR_TEMPLATE  # noqa: E402

BASH = shutil.which("bash")
pytestmark = pytest.mark.skipif(BASH is None, reason="Published generators require bash")


def _source() -> str:
    return (library_skills_dir() / "flow-control-generator" / "SKILL.md").read_text(encoding="utf-8")


def _executable(path: Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")
    path.chmod(0o755)


def _orchestrator(
    tmp_path: Path, plan: object, *, goal: str = "goal", state: str = "state",
    preflight: str | None = None, agent_source: str | None = None,
):
    (tmp_path / "checks").mkdir()
    (tmp_path / "goal.md").write_text(goal, encoding="utf-8")
    (tmp_path / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    (tmp_path / "orch.py").write_text(ORCHESTRATOR_TEMPLATE.search(_source()).group(1), encoding="utf-8")
    stub = tmp_path / "stub.py"
    stub.write_text(
        agent_source if agent_source is not None else (
            "import pathlib, sys\n"
            "body = sys.stdin.read()\n"
            "with pathlib.Path('calls.txt').open('a') as f: f.write(str(len(body)) + '\\n')\n"
            "if body.startswith('Decompose'):\n"
            "    pathlib.Path('planner-input.md').write_text(body)\n"
            "    sys.stdout.write(pathlib.Path('plan.json').read_text())\n"
            "elif body.startswith('Synthesize'):\n"
            "    sys.stdout.write(body)\n"
            "else:\n"
            "    print('WORK-' + body)\n"
        ),
        encoding="utf-8",
    )
    _executable(tmp_path / "checks" / "verify-merged.sh", '#!/bin/sh\ntest -s "$1"\n')
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": shlex.join([sys.executable, str(stub)]), "STATE": state}
    if preflight is not None:
        gate = tmp_path / "gate.py"
        gate.write_text(preflight, encoding="utf-8")
        gate.chmod(0o755)
        env["PREFLIGHT"] = str(gate)
    result = subprocess.run(
        [sys.executable, "orch.py", "goal.md"], cwd=tmp_path, env=env,
        capture_output=True, text=True, timeout=30,
    )
    return result, tmp_path / state


@pytest.mark.parametrize("plan", [
    {"id": "a", "task": "X"},
    None,
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


def _dag(tmp_path: Path, *, final_node: str = "assemble", fail_node: str = "", reverse: bool = False,
          preflight: str | None = None, min_ok: str = "3"):
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
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub), "MIN_OK": min_ok,
           "FAIL_NODE": fail_node, "STATE": "deep/state"}
    if preflight is not None:
        gate = tmp_path / "checks" / "preflight"
        _executable(gate, preflight)
        env["PREFLIGHT"] = str(gate)
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


def _router(tmp_path: Path, label: str, *, preflight: str | None = None):
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
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub), "STATE": "state"}
    if preflight is not None:
        gate = tmp_path / "preflight.sh"
        _executable(gate, preflight)
        env["PREFLIGHT"] = str(gate)
    return subprocess.run([BASH, "router.sh", "input.md"], cwd=tmp_path, env=env,
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


PASS_PY = "#!/usr/bin/env python3\nimport sys\nsys.exit(0)\n"
FAIL_PY = "#!/usr/bin/env python3\nimport sys\nsys.exit(1)\n"
FAIL_SH = "#!/bin/sh\nexit 1\n"


def test_orchestrator_selected_gate_failure_blocks_first_dispatch(tmp_path: Path):
    result, state = _orchestrator(tmp_path, [{"id": "a", "task": "X"}], preflight=FAIL_PY)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "calls.txt").exists()
    assert not (state / "final.md").exists()
    assert "preflight gate=1" in (state / "flow.log").read_text()


def test_orchestrator_gate_mutation_after_work_blocks_acceptance(tmp_path: Path):
    gate = (
        "#!/usr/bin/env python3\nimport pathlib, sys\n"
        "seen = sorted(pathlib.Path('.').glob('state/worker-*.md'))\n"
        "sys.exit(1 if seen else 0)\n"
    )
    result, state = _orchestrator(tmp_path, [{"id": "a", "task": "X"}], preflight=gate)
    assert result.returncode == 4, result.stderr
    assert (tmp_path / "calls.txt").is_file()  # planner + worker ran before the post gate
    assert not (state / "final.md").exists()


def test_orchestrator_empty_gate_preserves_attended_path(tmp_path: Path):
    result, state = _orchestrator(tmp_path, [{"id": "a", "task": "X"}])
    assert result.returncode == 0, result.stderr
    assert "WORK-X" in (state / "final.md").read_text()


def test_dag_quorum_cannot_swallow_selected_gate_failure(tmp_path: Path):
    result = _dag(tmp_path, preflight=FAIL_SH, min_ok="1")
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "gate-target.txt").exists()


def test_dag_gate_mutation_after_work_blocks_merged_publish(tmp_path: Path):
    gate = "#!/bin/sh\n[ -z \"$(ls deep/state/*.out 2>/dev/null)\" ]\n"
    result = _dag(tmp_path, preflight=gate, min_ok="1")
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "gate-target.txt").exists()


def test_router_selected_gate_failure_blocks_classify(tmp_path: Path):
    result = _router(tmp_path, "BUG\n", preflight=FAIL_SH)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "handler-call.txt").exists()


def test_router_missing_gate_blocks_dispatch(tmp_path: Path):
    match = re.search(r"## Template: Conditional Router \(bash\)\n.*?```bash\n(.*?)\n```", _source(), re.S)
    (tmp_path / "router.sh").write_text(match.group(1))
    (tmp_path / "prompts").mkdir()
    (tmp_path / "input.md").write_text("user input\n")
    (tmp_path / "label.txt").write_text("BUG\n")
    (tmp_path / "prompts/classify.md").write_text("CLASSIFY\n")
    (tmp_path / "prompts" / "route-bug.md").write_text("ROUTE-bug\n")
    stub = tmp_path / "stub.sh"
    _executable(stub, '#!/bin/sh\ncat label.txt\n')
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub), "STATE": "state",
           "PREFLIGHT": str(tmp_path / "no-such-gate")}
    result = subprocess.run([BASH, "router.sh", "input.md"], cwd=tmp_path, env=env,
                            capture_output=True, text=True, timeout=30)
    assert result.returncode == 4, result.stderr
    assert "preflight gate=4" in (tmp_path / "state/flow.log").read_text()


def _pipeline(tmp_path: Path, *, preflight: str | None = None):
    match = re.search(r"## Template: Sequential Pipeline \(bash\)\n.*?```bash\n(.*?)\n```", _source(), re.S)
    (tmp_path / "pipeline.sh").write_text(match.group(1))
    (tmp_path / "prompts").mkdir()
    for name in ("01-spec", "02-implement", "03-review"):
        (tmp_path / "prompts" / f"{name}.md").write_text(f"{name}\n")
    (tmp_path / "checks").mkdir()
    _executable(tmp_path / "checks" / "run-tests.sh", "#!/bin/sh\nexit 0\n")
    stub = tmp_path / "stub.sh"
    _executable(stub, '#!/bin/sh\nprompt="$(cat)"\necho "calls" >> calls.txt\necho "OUT:$prompt"\n')
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub), "STATE": "state"}
    if preflight is not None:
        gate = tmp_path / "preflight.sh"
        _executable(gate, preflight)
        env["PREFLIGHT"] = str(gate)
    return subprocess.run([BASH, "pipeline.sh"], cwd=tmp_path, env=env,
                          capture_output=True, text=True, timeout=30)


def _fanout(
    tmp_path: Path, *, preflight: str | None = None, min_ok: str = "",
    agent_body: str = 'echo "OUT:$prompt"\n', first_prompt: str = "a",
):
    match = re.search(r"## Template: Parallel Fan-out/Fan-in \(bash\)\n.*?```bash\n(.*?)\n```", _source(), re.S)
    (tmp_path / "fanout.sh").write_text(match.group(1))
    (tmp_path / "prompts" / "fan").mkdir(parents=True)
    for name, content in (("a", first_prompt), ("b", "b")):
        (tmp_path / "prompts" / "fan" / f"{name}.md").write_text(f"{content}\n")
    (tmp_path / "prompts" / "synthesize.md").write_text("SYNTH\n")
    (tmp_path / "checks").mkdir()
    _executable(tmp_path / "checks" / "verify-merged.sh", "#!/bin/sh\nexit 0\n")
    stub = tmp_path / "stub.sh"
    _executable(stub, '#!/bin/sh\nprompt="$(cat)"\n' + agent_body)
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub), "STATE": "state", "MIN_OK": min_ok}
    if preflight is not None:
        gate = tmp_path / "preflight.sh"
        _executable(gate, preflight)
        env["PREFLIGHT"] = str(gate)
    return subprocess.run([BASH, "fanout.sh"], cwd=tmp_path, env=env,
                          capture_output=True, text=True, timeout=30)


def test_pipeline_gate_mutation_after_work_blocks_acceptance(tmp_path: Path):
    gate = "#!/bin/sh\n[ -z \"$(ls state/01-spec.md 2>/dev/null)\" ]\n"
    result = _pipeline(tmp_path, preflight=gate)
    assert result.returncode == 4, result.stderr


def test_pipeline_missing_gate_blocks_first_dispatch(tmp_path: Path):
    match = re.search(r"## Template: Sequential Pipeline \(bash\)\n.*?```bash\n(.*?)\n```", _source(), re.S)
    (tmp_path / "pipeline.sh").write_text(match.group(1))
    (tmp_path / "prompts").mkdir()
    (tmp_path / "prompts" / "01-spec.md").write_text("spec\n")
    stub = tmp_path / "stub.sh"
    _executable(stub, '#!/bin/sh\ncat\n')
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub), "STATE": "state",
           "PREFLIGHT": str(tmp_path / "no-such-gate")}
    result = subprocess.run([BASH, "pipeline.sh"], cwd=tmp_path, env=env,
                            capture_output=True, text=True, timeout=30)
    assert result.returncode == 4, result.stderr


def test_fanout_quorum_cannot_swallow_gate_failure(tmp_path: Path):
    result = _fanout(tmp_path, preflight=FAIL_SH, min_ok="1")
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/final.md").exists()


def test_fanout_per_branch_captures_avoid_shared_output(tmp_path: Path):
    result = _fanout(tmp_path, preflight="#!/bin/sh\nexit 0\n")
    assert result.returncode == 0, result.stderr
    state = tmp_path / "state"
    assert (state / "preflight-fan-a-pre.out").is_file()
    assert (state / "preflight-synth-pre.out").is_file()


def test_dag_final_publish_gate_failure_is_hold_not_worker_error(tmp_path: Path):
    gate = (
        '#!/bin/sh\n'
        'if grep -q "^assemble.*done" deep/state/dag-ledger.tsv 2>/dev/null; then exit 4; fi\n'
        'exit 0\n'
    )
    result = _dag(tmp_path, preflight=gate)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "gate-target.txt").exists()


def test_orchestrator_worker_failure_cannot_mask_peer_preflight_hold(tmp_path: Path):
    agent = (
        "import json, pathlib, sys, time\n"
        "body = sys.stdin.read()\n"
        "if body.startswith('Decompose'):\n"
        "    print(json.dumps([{'id': 'first', 'task': 'FAIL'}, {'id': 'second', 'task': 'WAIT'}]))\n"
        "elif body == 'FAIL':\n"
        "    pathlib.Path('worker-failed').write_text('failed'); sys.exit(1)\n"
        "elif body == 'WAIT':\n"
        "    deadline = time.monotonic() + 2\n"
        "    while not pathlib.Path('worker-failed').exists():\n"
        "        if time.monotonic() > deadline: raise RuntimeError('first worker control absent')\n"
        "        time.sleep(.01)\n"
        "    print('worker output')\n"
        "else: print('synthesis')\n"
    )
    gate = "#!/usr/bin/env python3\nimport pathlib, sys\nsys.exit(4 if pathlib.Path('worker-failed').exists() else 0)\n"
    result, state = _orchestrator(tmp_path, [], preflight=gate, agent_source=agent)
    assert result.returncode == 4, result.stderr
    assert not (state / "final.md").exists()


def test_router_post_dispatch_hold_precedes_label_rejection(tmp_path: Path):
    gate = '#!/bin/sh\n[ ! -f state/label.txt ]\n'
    result = _router(tmp_path, "bogus\n", preflight=gate)
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "handler-call.txt").exists()


def test_dag_bad_quorum_is_configuration_hold_before_work(tmp_path: Path):
    result = _dag(tmp_path, min_ok="abc")
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "calls.txt").exists()


def test_fanout_bad_quorum_is_configuration_hold(tmp_path: Path):
    result = _fanout(tmp_path, min_ok="abc")
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "state/final.md").exists()


def test_dag_unlaunchable_selected_gate_is_configuration_hold(tmp_path: Path):
    result = _dag(tmp_path, preflight="invalid executable format\n")
    assert result.returncode == 4, result.stderr
    assert not (tmp_path / "calls.txt").exists()


def test_bash_fanout_large_prompt_avoids_argv_limit(tmp_path: Path):
    agent = (
        'case "$prompt" in\n'
        'LARGE:*) echo LARGE-WORK;;\n'
        'b) echo OTHER-WORK;;\n'
        'SYNTH*) echo MERGED-WORK;;\n'
        '*) exit 7;;\n'
        'esac\n'
    )
    result = _fanout(
        tmp_path, agent_body=agent, first_prompt="LARGE:" + "x" * (2 * 1024 * 1024),
    )
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "state/fan-a.md").read_text() == "LARGE-WORK\n"
    assert (tmp_path / "state/final.md").read_text() == "MERGED-WORK\n"


def test_bash_fanout_empty_success_cannot_satisfy_strict_policy(tmp_path: Path):
    agent = (
        'case "$prompt" in\n'
        'a) exit 0;;\n'
        'b) echo GOOD-WORK;;\n'
        'SYNTH*) echo invoked > synthesis-ran; echo MERGED-WORK;;\n'
        'esac\n'
    )
    result = _fanout(tmp_path, agent_body=agent)
    assert result.returncode == 2, result.stderr
    assert not (tmp_path / "state/fan-a.md").exists()
    assert (tmp_path / "state/fan-b.md").read_text() == "GOOD-WORK\n"
    assert not (tmp_path / "synthesis-ran").exists()
    assert not (tmp_path / "state/final.md").exists()
