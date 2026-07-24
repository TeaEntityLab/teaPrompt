"""Guard the Claude Code prompt survey, dispositions, and adopted local wording."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "claude-code-system-prompts-survey-2026-07-24.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
BRIEF_SKILL = PROMPT_LIBRARY_ROOT / "skills" / "reflective-brief" / "SKILL.md"
TASK_START = PROMPT_LIBRARY_ROOT / "02-engineering" / "task-start.md"
REVIEW_SKILL = PROMPT_LIBRARY_ROOT / "skills" / "reflective-review" / "SKILL.md"
CODE_REVIEWER = PROMPT_LIBRARY_ROOT / "02-engineering" / "code-reviewer.md"
HANDOFF_SKILL = PROMPT_LIBRARY_ROOT / "skills" / "reflective-handoff-retro" / "SKILL.md"
MEMORY_CONSOLIDATION = PROMPT_LIBRARY_ROOT / "04-agent" / "memory-consolidation.md"
GOVERNANCE_SKILL = (
    PROMPT_LIBRARY_ROOT / "skills" / "agent-governance-scaffold" / "SKILL.md"
)
PINNED_COMMIT = "b9895f5556e962e6aec60aba7cccfc18790ace3a"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Shared Findings",
        1,
    )[0]
    return {
        candidate_id: next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
        for candidate_id in (
            "CCSP1",
            "CCSP2",
            "CCSP3",
            "CCSP4",
            "CCSP5",
            "CCSP6",
            "CCSP7",
            "CCSP8",
        )
    }


def test_prompt_survey_record_shape_revision_and_evidence_tiers():
    text = _read(RECORD)
    for heading in (
        "## Panel Consensus",
        "## Required Wording Changes",
        "## Candidate Adoption Ledger",
        "## Shared Findings",
        "## Evidence vs Inference",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
    ):
        assert heading in text, f"prompt survey missing {heading!r}"
    assert PINNED_COMMIT in text
    assert "Claude Code `2.1.218`" in text
    assert "603/603 renderer reconstruction" in text
    assert "416/603 fresh public-extractor count" in text
    assert "`AGREE WITH CHANGES` (7/7" in text
    assert "| `reproduce` | **partial** |" in text
    assert "| `deploy` | **no** |" in text
    assert "No behavioral A/B evaluation was run" in text


def test_prompt_survey_candidate_ledger_preserves_dispositions():
    rows = _ledger_rows()
    assert "Adopted 2026-07-24" in rows["CCSP1"]
    assert "Partial 2026-07-24" in rows["CCSP2"]
    assert "Adopted 2026-07-24" in rows["CCSP3"]
    assert "Deferred" in rows["CCSP4"]
    assert "PENDING: CCSP4" in rows["CCSP4"]
    for candidate_id in ("CCSP5", "CCSP6"):
        assert "No change" in rows[candidate_id]
    for candidate_id in ("CCSP7", "CCSP8"):
        assert "Rejected 2026-07-24" in rows[candidate_id]


def test_ccsp1_research_before_clarification_is_pinned_at_both_surfaces():
    brief = _read(BRIEF_SKILL)
    source = _read(TASK_START)
    assert "Before asking for clarification, make a brief, targeted check" in brief
    assert "Ask only about a material fork the evidence cannot resolve" in brief
    assert "Any clarifying question names the local evidence checked" in source


def test_ccsp2_reachable_failure_scenario_is_pinned_without_tri_state_expansion():
    review = _read(REVIEW_SKILL)
    source = _read(CODE_REVIEWER)
    assert "Every reported code defect must name either a reachable failure scenario" in review
    assert "label the claim unverified rather than confirmed" in review
    assert "Every reported defect names a reachable failure scenario" in source
    assert "precision (default)" not in review
    assert "max 15 findings" not in review


def test_ccsp3_memory_quality_and_revalidation_are_pinned_at_both_surfaces():
    handoff = _read(HANDOFF_SKILL)
    source = _read(MEMORY_CONSOLIDATION)
    assert "future-useful, durable beyond the current task, and self-contained" in handoff
    assert "Exclude live task state and facts a routine source lookup can recover" in handoff
    assert "treat recalled memory as a dated lead" in handoff
    assert "Each retained memory is future-useful, durable beyond the current task" in source
    assert "Live task state and lookup-recoverable facts are excluded" in source


def test_ccsp4_remains_unadopted_until_superseding_approval_and_host_proof():
    row = _ledger_rows()["CCSP4"]
    governance = _read(GOVERNANCE_SKILL)
    assert "explicit human approval" in row
    assert "concrete host broker" in row
    assert "proposal_sha256" not in governance


def test_external_adoption_and_project_knowledge_link_the_survey():
    case_studies = _read(CASE_STUDIES)
    project_knowledge = _read(PROJECT_KNOWLEDGE)
    assert "| 2026-07-24 | Claude Code v2.1.218 prompt snapshot" in case_studies
    assert "[survey](claude-code-system-prompts-survey-2026-07-24.md)" in case_studies
    assert "| Claude Code prompt snapshot outcome recorded | done |" in case_studies
    assert "2026-07-24 Claude Code prompt snapshot survey" in project_knowledge
    assert "plans/claude-code-system-prompts-survey-2026-07-24.md" in project_knowledge
