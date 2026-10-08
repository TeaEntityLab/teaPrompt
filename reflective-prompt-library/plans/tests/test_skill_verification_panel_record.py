"""Guard the 2026-09-05 skill correctness / logical-consistency pass.

Preserves record structure and indexing and dry-runs quorum/final-sink and
empty-worker behavior. Exact live-skill prose and incidental source-size
assertions are not acceptance oracles.
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

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "skill-verification-panel-2026-09-05.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"

DAG_TEMPLATE = re.compile(
    r"## Template: DAG Executor \(Python, stdlib only\)\n.*?```python\n(.*?)```", re.S
)
ORCHESTRATOR_TEMPLATE = re.compile(  # the body holds a literal ``` in a string; end at a fence on its own line
    r"## Template: Orchestrator-Workers \(Python, stdlib only\)\n.*?```python\n(.*?)\n```\n", re.S
)



def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _skill(name: str) -> str:
    return _read(library_skills_dir() / name / "SKILL.md")


def test_record_has_required_shape():
    text = _read(RECORD)
    assert "> **Status:**" in "\n".join(text.splitlines()[:12])
    for heading in (
        "## Research Question", "## Method", "## Landed Fixes by Skill", "## Not Changed",
        "## Evidence vs Inference", "## Evidence Actually Checked", "## Falsifiability", "## Completion Ledger",
    ):
        assert heading in text, heading
    assert "reflective-implement" in text and "No text change landed" in text





def test_record_is_indexed():
    knowledge = _read(PROJECT_KNOWLEDGE)
    assert "(plans/skill-verification-panel-2026-09-05.md)" in knowledge
    ledger = _read(CASE_STUDIES)
    assert "`skill-verification-panel-2026-09-05.md`" in ledger


def _run_dag(
    tmp_path: Path,
    dag: str,
    *,
    fail_node: str | None,
    min_ok: str,
    conflict: bool,
    empty_node: str | None = None,
    stale_sink: bool = False,
) -> int:
    d = tmp_path / f"{fail_node}-{min_ok}-{conflict}-{empty_node}-{stale_sink}"
    (d / "prompts").mkdir(parents=True)
    (d / "checks").mkdir()
    for n in ("spec", "api", "client", "assemble"):
        (d / "prompts" / f"{n}.md").write_text(f"{n}\n", encoding="utf-8")
    stub = d / "stub.sh"

    def write_stub(fail: str | None) -> None:
        body = '#!/bin/sh\nprompt="$(cat)"\n'
        if fail:
            body += f'case "$prompt" in {fail}*) exit 1;; esac\n'
        if empty_node:
            body += f'case "$prompt" in {empty_node}*) exit 0;; esac\n'
        body += 'echo "CONFLICT $prompt"\n' if conflict else 'echo "stub: $prompt"\n'
        stub.write_text(body, encoding="utf-8")
        stub.chmod(0o755)

    gate = d / "checks" / "verify-merged.sh"
    gate.write_text('#!/bin/sh\n[ -s "$1" ] && ! grep -q CONFLICT "$1"\n', encoding="utf-8")
    gate.chmod(0o755)
    (d / "dag.py").write_text(dag, encoding="utf-8")
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub), "MIN_OK": min_ok}
    if stale_sink:  # a prior clean run in the same STATE leaves every node's .out on disk
        write_stub(None)
        assert subprocess.run([sys.executable, "dag.py"], cwd=d, env=env, capture_output=True, timeout=120).returncode == 0
    write_stub(fail_node)
    r = subprocess.run([sys.executable, "dag.py"], cwd=d, env=env, capture_output=True, text=True, timeout=120)
    return r.returncode


@pytest.mark.skipif(shutil.which("sh") is None, reason="sh not available")
def test_dag_template_quorum_path_still_reaches_the_merged_gate(tmp_path: Path):
    """D7: MIN_OK satisfied must not bypass checks/verify-merged.sh."""
    match = DAG_TEMPLATE.search(_skill("flow-control-generator"))
    assert match, "DAG template missing"
    dag = match.group(1)
    assert _run_dag(tmp_path, dag, fail_node=None, min_ok="", conflict=False) == 0
    assert _run_dag(tmp_path, dag, fail_node="api", min_ok="", conflict=False) == 2      # strict default
    assert _run_dag(tmp_path, dag, fail_node=None, min_ok="4", conflict=False) == 0      # quorum, clean merge
    assert _run_dag(tmp_path, dag, fail_node=None, min_ok="4", conflict=True) == 2       # quorum met, merge rejected
    assert _run_dag(tmp_path, dag, fail_node="assemble", min_ok="1", conflict=False) == 2  # quorum met, sink missing
    # RSIAgent survey 2026-09-16 (C8 family): a sink left by a prior run in the same
    # STATE must not satisfy the merged gate when this run's sink failed or was blocked.
    assert _run_dag(tmp_path, dag, fail_node="assemble", min_ok="3", conflict=False, stale_sink=True) == 2
    assert _run_dag(tmp_path, dag, fail_node="api", min_ok="2", conflict=False, stale_sink=True) == 2


@pytest.mark.skipif(shutil.which("sh") is None, reason="sh not available")
def test_python_templates_treat_empty_success_as_failure(tmp_path: Path):
    """Second-pass review 2026-09-14: a node or worker that exits 0 with no output
    must not be marked done and feed empty text downstream (the bash templates
    already gate on `[ -s ]`)."""
    dag = DAG_TEMPLATE.search(_skill("flow-control-generator")).group(1)
    assert _run_dag(tmp_path, dag, fail_node=None, min_ok="", conflict=False, empty_node="api") == 2

    orch = ORCHESTRATOR_TEMPLATE.search(_skill("flow-control-generator")).group(1)
    d = tmp_path / "orch"
    (d / "checks").mkdir(parents=True)
    (d / "goal.md").write_text("goal\n", encoding="utf-8")
    stub = d / "stub.sh"
    stub.write_text(
        '#!/bin/sh\nprompt="$(cat)"\n'
        'case "$prompt" in Decompose*) printf \'[{"id":"a","task":"x"},{"id":"b","task":"y"}]\';;'
        " x) exit 0;; *) echo out;; esac\n",
        encoding="utf-8",
    )
    stub.chmod(0o755)
    gate = d / "checks" / "verify-merged.sh"
    gate.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    gate.chmod(0o755)
    (d / "orch.py").write_text(orch, encoding="utf-8")
    env = {"PATH": os.environ["PATH"], "AGENT_CMD": str(stub)}
    r = subprocess.run([sys.executable, "orch.py", "goal.md"], cwd=d, env=env, capture_output=True, text=True, timeout=120)
    assert r.returncode != 0, r.stdout
    assert "no output" in r.stderr
