"""Guard the 2026-09-06 harness / intent-drift rethink.

Adopted: two GLOSSARY terms, one Adoption Guard Closure clause, one Durable
Lesson, one recipe frame-test bullet. Deferred: the tool-status-line rule (I-1)
- guarded for ledger presence and absence from skills, never as adopted text.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "harness-intent-drift-rethink-2026-09-06.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
RECIPES = PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-recipes.md"
TRUST_BOUNDARY = PROMPT_LIBRARY_ROOT / "04-agent" / "runtime-trust-boundary.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"

HARNESS_TEST = (
    "a sentence that claims this\nlibrary or the skill enforces it is a defect."
)
DRIFT_POINTER = (
    "are the Durable Lesson \"Intent lives with\nhumans; every downstream artifact is a lossy compression read by an optimizer\""
)
DRIFT_TEST = "A glossary entry seals nothing."
CLOSURE_CLAUSE = "executable behavior (for a shipped pack template: a stub\n  dry-run over each gate path that template implements)"
LESSON = "### Lesson: A shipped template drifts from its contract prose; only execution finds it"
FRAME_TEST = "- Frame test: the packet's questions carry the coordinator's frame, so the packet states the frame-test"
DEFERRED_I1 = "A tool status line is a claim about an effect, not the artifact."


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    assert heading in text, heading
    return text.split(heading, 1)[1].split("\n## ", 1)[0]


def test_record_shape_and_ledger():
    text = _read(RECORD)
    assert "> **Status:" in "\n".join(text.splitlines()[:12])
    for heading in (
        "## Research Question", "## Method", "## Panel Consensus", "## Packet Corrections",
        "## The Theses as Held", "## Locus Table", "## Required Wording Changes",
        "## Candidate Adoption Ledger", "## Disagreements / Residual Risks",
        "## Evidence vs Inference", "## Evidence Actually Checked", "## Falsifiability", "## Completion Ledger",
    ):
        assert heading in text, heading
    ledger = _section(text, "## Candidate Adoption Ledger")
    for cid, status in (("G-1", "**Adopted**"), ("G-2", "**Adopted**"), ("L-1", "**Adopted**"),
                        ("L-2", "**Adopted**"), ("R-1", "**Adopted**"), ("I-1", "**Deferred**")):
        row = next(line for line in ledger.splitlines() if line.startswith(f"| {cid} |"))
        assert status in row, cid
    assert "every hit is an `eval_harness` playbook test filename" in text  # packet correction kept
    assert "@" not in text and "http" not in text


def test_glossary_terms_present_once_and_point_rather_than_restate():
    glossary = _read(glossary_path())
    assert glossary.count("## Harness / 執行框架") == 1
    assert glossary.count("## Intent Drift / 意圖漂移") == 1
    harness = _section(glossary, "## Harness / 執行框架")
    for token in ("budget enforcement", "operates none", "`harness-generated`", "`eval_harness`", HARNESS_TEST):
        assert token in harness, token
    drift = _section(glossary, "## Intent Drift / 意圖漂移")
    assert DRIFT_POINTER in drift and DRIFT_TEST in drift
    # Points to the Lesson instead of restating its four-part shape; keeps the ceiling.
    assert "seal it against" not in drift and "re-anchor it to humans" not in drift
    assert "Drift from intent that was never written has no\nreferee" in drift
    closure = _section(glossary, "## Adoption Guard Closure")
    assert CLOSURE_CLAUSE in closure and "stable protocol tokens" in closure


def test_lesson_recipe_and_deferred_row_at_their_surfaces():
    knowledge = _read(PROJECT_KNOWLEDGE)
    assert knowledge.count(LESSON) == 1
    lesson = knowledge.split(LESSON, 1)[1].split("\n## ", 1)[0]
    assert re.search(r"^- Evidence: .*skill-verification-panel-2026-09-05\.md", lesson, re.M)
    assert "- Review trigger: an edit to a fenced executable template inside a registered domain pack" in lesson
    assert not re.search(r"\bthirteen\b", lesson)
    assert "(plans/harness-intent-drift-rethink-2026-09-06.md)" in knowledge
    recipes = _read(RECIPES)
    assert recipes.count(FRAME_TEST) == 1
    assert "not a second epistemic channel" in recipes
    assert "harness-intent-drift-rethink-2026-09-06.md" in _read(CASE_STUDIES)
    # I-1 stays deferred: its sentence is on no skill and not on the trust boundary.
    for skill in library_skills_dir().glob("*/SKILL.md"):
        assert DEFERRED_I1 not in skill.read_text(encoding="utf-8"), skill
    assert DEFERRED_I1 not in _read(TRUST_BOUNDARY)
