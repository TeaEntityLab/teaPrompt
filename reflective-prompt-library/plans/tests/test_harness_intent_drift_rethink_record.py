"""Guard the 2026-09-06 harness / intent-drift rethink and its skill-layer addendum.

Adopted: two GLOSSARY terms, one Adoption Guard Closure clause, one Durable
Lesson, one recipe frame-test bullet. Deferred: the tool-status-line rule (I-1)
- guarded for ledger presence and absence from skills, never as adopted text.

The 2026-09-06 skill-layer re-evaluation adopted no skill text (dated negative
audit) and hardened I-1's reserved wording. This guard therefore pins the
addendum's ledger, the hardened wording as record-only, and the continued
absence of every rejected candidate from the installed skills.
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
ADDENDUM = "## Skill Adoption Addendum — 2026-09-06 (user-directed, skill layer)"
HARDENED_I1 = (
    "compare it against an oracle that does not share the writer's channel — a copy taken "
    "before the write, or the version-control index; re-reading the bytes the writer just "
    "returned is not that check."
)
# Wording the 2026-09-06 panel rejected for the installed unit; the recipe owns these duties.
REJECTED_ON_SKILLS = ("asker's altitude", "two artifacts", "failed synthesis", "Test the frame too")


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


def test_skill_adoption_addendum_is_a_dated_negative_audit():
    text = _read(RECORD)
    assert text.count(ADDENDUM) == 1
    section = text.split(ADDENDUM, 1)[1]
    for heading in (
        "### Gate ruling", "### Method", "### Panel Consensus",
        "### Candidate Adoption Ledger (skill layer)", "### Packet corrections",
        "### Observed divergences", "### Disagreements / Residual Risks",
        "### Evidence vs Inference", "### Falsifiability", "### Completion Ledger",
    ):
        assert heading in section, heading
    assert "**adopt no skill text.**" in section
    # The gate ruling must keep the instruction separate from I-1's own trigger.
    assert "It did **not** fire I-1's recorded trigger" in section
    assert "is gate-shopping" in section
    rows = {line.split("|")[1].strip(): line for line in section.splitlines() if line.startswith("| S-")}
    assert set(rows) == {f"S-{n}" for n in range(1, 8)}, sorted(rows)
    assert "**Deferred; reserved wording hardened**" in rows["S-1"]
    for cid in ("S-2", "S-3", "S-4", "S-5", "S-6", "S-7"):
        assert "**Rejected" in rows[cid], cid
    assert "zero defects" in rows["S-5"] and "First application of the §Harness operational test" in rows["S-5"]


def test_hardened_i1_wording_is_recorded_but_stays_unadopted():
    text = _read(RECORD)
    assert text.count(HARDENED_I1) == 1
    # The vacuous disjunct five lenses rejected must not survive anywhere.
    assert "read the file or diff it against a copy taken before the write" not in text
    for skill in library_skills_dir().glob("*/SKILL.md"):
        body = skill.read_text(encoding="utf-8")
        assert HARDENED_I1 not in body, skill
    assert HARDENED_I1 not in _read(TRUST_BOUNDARY)


def test_rejected_skill_candidates_stayed_off_the_installed_unit():
    for skill in library_skills_dir().glob("*/SKILL.md"):
        body = skill.read_text(encoding="utf-8")
        for token in REJECTED_ON_SKILLS:
            assert token not in body, f"{skill.parent.name}: {token}"
    # The rejections are destination decisions: the recipe still owns both duties once.
    recipes = _read(RECIPES)
    assert recipes.count("asker's altitude") == 1
    assert "A correct panel memo shipped as the first answer is a failed answer." in recipes
    # And the panel method the candidates targeted is unchanged.
    research = _read(library_skills_dir() / "reflective-research" / "SKILL.md")
    assert "5. Output: consensus table, rejected options with reason" in research
    assert "3. Run a critical-thinking pass: evidence vs inference, counterargument, silent-downgrade check." in research
