"""Guard the 2026-09-05 skill correctness / logical-consistency pass.

Pins one or two landed sentences per skill at the surface that owns them, keeps
both flow packs under the 20,000-character routing budget (the harness bound
pre-exists in test_llm_judge_lifecycle_survey_record.py; the generator bound is
new here), dry-runs the DAG template's quorum path against the merged-result
gate (D7), and checks the record is indexed.
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
LINT_WARNING_CHARS = 20000

DAG_TEMPLATE = re.compile(
    r"## Template: DAG Executor \(Python, stdlib only\)\n.*?```python\n(.*?)```", re.S
)

# skill -> sentences that must be present exactly once (or at least once when noted).
PINS = {
    "reflective-brief": ("11. Write the Minimal Plan: the smallest How that could satisfy the acceptance criteria.",),
    "reflective-dispatch": (
        "safe content ambiguity after routing is handled by stating assumptions, not by a second default-up.",
        "at Strictness L5, create one before yielding if neither exists.",
    ),
    "reflective-handoff-retro": (
        "A continuation packet carries the spec version, the State Ledger, oracle manifest status, open failure signatures, and named unknowns. It also lists the relevant files and the commands and tests run, so a continuation can rebuild the task packet",
    ),
    "reflective-minimality": ("Lean already. No complexity cuts.",),
    "reflective-risk": ("- If the risk cannot be bounded, recommend no-go.", "ungated production changes"),
    "reflective-spec-plan": ("- Formalization L0: prompt only,",),
    "governed-delivery": ("and re-plans the affected slice before work continues.",),
    "agent-governance-scaffold": (
        "exactly one of the literals `**Governance status:** artifact-complete` or `**Governance status:** enforcement-proven`",
    ),
    "flow-control-generator": (
        'run_agent() { $AGENT_CMD "$(cat "$1")" > "$2" && [ -s "$2" ] || { rm -f "$2"; return 1; }; }',
        "    if ok < int(MIN_OK): sys.exit(2)                     # explicit quorum\nelif bad: sys.exit(2)",
        'wid = "".join(c for c in str(t.get("id", "")) if c.isalnum() or c in "-_") or "task"',
        'if not isinstance(tasks, list): raise ValueError("plan is not a list")',
    ),
    "flow-loop-harness": (
        "4. Progress detector: abort when an iteration produces no observable change",
        '"$(git diff HEAD --stat | tail -n1)"',
        'if "$VERIFY" > "$STATE/verify-out.txt" 2>&1; then echo "already converged"; exit 0; fi',
        'summary="$(cat "$STATE"/w${w}-*.md | cksum)"',
    ),
}
# Sentences that legitimately appear more than once (template + companion floor).
AT_LEAST_ONCE = {
    "flow-loop-harness": ("""if [ "$(sed '/^[[:space:]]*$/d' "$STATE/round-$r-critique.md")" = "ACCEPT" ]""",),
    "reflective-risk": ("Sink Inventory", "Unattended Envelope"),
    "flow-control-generator": ("# gate: none (accepted)",),
    "reflective-research": ("| Claim / Item | Source | Status | Checked (date) | How (command + input set, or freshness kind) | Open Constraints |",),
    "reflective-review": ("record-only correction",),
    "reflective-spec-plan": ("hidden-evaluation",),
    "agent-governance-scaffold": ('"tests/governance/**"',),
}


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
    for skill in PINS:
        assert f"`{skill}`" in text, f"record has no row for {skill}"
    assert "reflective-implement" in text and "No text change landed" in text


@pytest.mark.parametrize("skill", sorted(set(PINS) | set(AT_LEAST_ONCE)))
def test_landed_sentences_present_once(skill: str):
    text = _skill(skill)
    for pin in PINS.get(skill, ()):
        assert text.count(pin) == 1, f"{skill}: count != 1 for {pin[:60]!r}"
    for pin in AT_LEAST_ONCE.get(skill, ()):
        assert pin in text, f"{skill}: missing {pin[:60]!r}"


@pytest.mark.parametrize("pack", ["flow-control-generator", "flow-loop-harness"])
def test_flow_packs_stay_under_lint_length_threshold(pack: str):
    # lint_skills.py measures the whole file in characters; so do we.
    assert len(_skill(pack)) <= LINT_WARNING_CHARS, len(_skill(pack))


def test_record_is_indexed():
    knowledge = _read(PROJECT_KNOWLEDGE)
    assert "(plans/skill-verification-panel-2026-09-05.md)" in knowledge
    ledger = _read(CASE_STUDIES)
    assert "`skill-verification-panel-2026-09-05.md`" in ledger


def _run_dag(tmp_path: Path, dag: str, *, fail_node: str | None, min_ok: str, conflict: bool) -> int:
    d = tmp_path / f"{fail_node}-{min_ok}-{conflict}"
    (d / "prompts").mkdir(parents=True)
    (d / "checks").mkdir()
    for n in ("spec", "api", "client", "assemble"):
        (d / "prompts" / f"{n}.md").write_text(f"{n}\n", encoding="utf-8")
    stub = d / "stub.sh"
    body = "#!/bin/sh\n"
    if fail_node:
        body += f'case "$1" in {fail_node}*) exit 1;; esac\n'
    body += 'echo "CONFLICT $1"\n' if conflict else 'echo "stub: $1"\n'
    stub.write_text(body, encoding="utf-8")
    stub.chmod(0o755)
    gate = d / "checks" / "verify-merged.sh"
    gate.write_text('#!/bin/sh\n[ -s "$1" ] && ! grep -q CONFLICT "$1"\n', encoding="utf-8")
    gate.chmod(0o755)
    (d / "dag.py").write_text(dag, encoding="utf-8")
    env = dict(os.environ, AGENT_CMD=str(stub), MIN_OK=min_ok)
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
