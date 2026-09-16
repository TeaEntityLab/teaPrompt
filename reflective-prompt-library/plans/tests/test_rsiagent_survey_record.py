"""Guard the RSIAgent survey's identity, dispositions, clean-room boundary, and
the one template repair it landed on the loop pack.

The generator-pack repair (DAG quorum gate requires this run's sink) is guarded
by the DAG dry-run in ``test_skill_verification_panel_record.py`` (owner of that
harness). Interpretive paragraphs are not pinned.
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

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "rsiagent-survey-2026-09-16.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
REPO_REVISION = "dcd4e580c2f4bb65aa28bf4d5ecbf2ac8fe3bfa4"
CANDIDATE_STATUS = {
    "RS-1": "Adopted 2026-09-16",
    "RS-2": "Adopted 2026-09-16",
    "RS-3": "Rejected 2026-09-16",
    "RS-4": "Rejected 2026-09-16",
    "RS-5": "Rejected 2026-09-16",
    "RS-6": "No change 2026-09-16",
    "RS-7": "No change 2026-09-16",
    "RS-8": "No change 2026-09-16",
    "RS-9": "Deferred 2026-09-16",
    "RS-10": "No change 2026-09-16",
    "RS-11": "No change 2026-09-16",
    "RS-12": "No change 2026-09-16",
}
# Clean-room boundary: the surveyed project's names and vocabulary stay in the record.
SURVEY_TOKENS = re.compile(
    r"RSIAgent|AetherLabs|Curriculum Agent|Actor Agent|Verifier Agent|broad-then-deep|"
    r"exam fence|exam_fence|OSWorld|Agents' Last Exam|curriculum_review|verifier_pass|"
    r"\bBRS\b|\bDRS\b|savevm|loadvm|2609\.15364|Kimi-K3|GLM-5\.3",
    re.IGNORECASE,
)
FIX_LOOP_TEMPLATE = re.compile(
    r"## Template: Verify-Gated Fix Loop \(bash\)\n.*?```bash\n(.*?)```", re.S
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _durable_surfaces() -> list[Path]:
    return (
        sorted(library_skills_dir().glob("*/SKILL.md"))
        + sorted(library_skills_dir().glob("examples/*.md"))
        + sorted(PROMPT_LIBRARY_ROOT.glob("SKILL_INSTALLATION*.md"))
        + [glossary_path()]
        + sorted((PROMPT_LIBRARY_ROOT / "04-agent").glob("*.md"))
    )


def test_record_preserves_source_identity_and_shape():
    text = _read(RECORD)
    assert re.search(r"^> \*\*Status:.*two template repairs", "\n".join(text.splitlines()[:12]), re.M)
    for heading in (
        "Research Question", "Direct Recommendation", "Method", "Concept Map",
        "Candidate Adoption Ledger", "Shared Findings", "Evidence vs Inference",
        "Evidence Actually Checked", "Falsifiability", "Completion Ledger",
    ):
        assert f"## {heading}" in text, heading
    assert REPO_REVISION in text
    assert "Apache-2.0" in text
    concept_map = text.split("## Concept Map", 1)[1].split("\n## ", 1)[0]
    concepts = re.findall(r"^\| (C\d+) \|", concept_map, re.M)
    assert concepts == [f"C{i}" for i in range(1, 11)]


def test_candidate_ledger_preserves_dispositions_and_triggers():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| RS-\d+ \|", line)
    ]
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 5, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3] and row[4], f"missing evidence or trigger: {row[0]}"
    deferred = next(row for row in rows if row[0] == "RS-9")
    assert "oscillation" in deferred[4], "RS-9 trigger must name the observed failure that reopens it"


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert len(surfaces) >= 20, "surface set unexpectedly small"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[record](plans/{RECORD.name})" in knowledge
    cases = _read(CASE_STUDIES)
    comparison = cases.split("## Case Comparison", 1)[1].split("\n## ", 1)[0]
    state = cases.split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert f"]({RECORD.name})" in comparison
    assert RECORD.name in state


def _run_fix_loop(tmp_path: Path, loop: str, *, agent_body: str, subdir: bool) -> tuple[int, str]:
    repo = tmp_path / ("sub-run" if subdir else "root-run")
    repo.mkdir(parents=True)
    git = ["git", "-c", "user.email=t@x", "-c", "user.name=t"]
    subprocess.run(git + ["init", "-q"], cwd=repo, check=True)
    (repo / "README.md").write_text("hello\n", encoding="utf-8")
    subprocess.run(git + ["add", "."], cwd=repo, check=True)
    subprocess.run(git + ["commit", "-qm", "init"], cwd=repo, check=True)
    cwd = repo / "sub" if subdir else repo
    (cwd / "checks").mkdir(parents=True)
    (cwd / "prompts").mkdir()
    verify = cwd / "checks" / "verify.sh"
    verify.write_text('#!/bin/sh\necho "still failing"\nexit 1\n', encoding="utf-8")
    verify.chmod(0o755)
    (cwd / "prompts" / "fix.md").write_text("fix it\n", encoding="utf-8")
    stub = tmp_path / "stub.sh"
    stub.write_text("#!/bin/sh\n" + agent_body, encoding="utf-8")
    stub.chmod(0o755)
    (tmp_path / "loop.sh").write_text(loop, encoding="utf-8")
    env = dict(os.environ, AGENT_CMD=str(stub), MAX_ITER="4", STATE="./state")
    r = subprocess.run(["bash", str(tmp_path / "loop.sh")], cwd=cwd, env=env, capture_output=True, text=True, timeout=120)
    return r.returncode, (cwd / "state" / "ledger.md").read_text(encoding="utf-8")


@pytest.mark.skipif(shutil.which("git") is None or shutil.which("bash") is None, reason="git/bash not available")
def test_fix_loop_no_progress_exit_survives_state_inside_worktree(tmp_path: Path):
    """RSIAgent survey 2026-09-16 (C2 family): with the template default
    ``STATE=./state`` inside an un-ignored git worktree, the loop's own per-iteration
    files counted as untracked progress and a no-op agent ran to the cap (exit 2)
    instead of exiting 3 at the first iteration."""
    loop = FIX_LOOP_TEMPLATE.search(_read(library_skills_dir() / "flow-loop-harness" / "SKILL.md")).group(1)
    for subdir in (False, True):
        code, ledger = _run_fix_loop(tmp_path, loop, agent_body='echo "stub: no-op"\n', subdir=subdir)
        assert code == 3, ledger
        assert "NO PROGRESS" in ledger
    # Real progress (a tracked edit each iteration) is still counted: the cap, not exit 3.
    code, ledger = _run_fix_loop(tmp_path / "edit", loop, agent_body="echo x >> README.md\n", subdir=False)
    assert code == 2, ledger
    assert "NO PROGRESS" not in ledger
