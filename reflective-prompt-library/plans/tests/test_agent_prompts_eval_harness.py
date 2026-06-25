"""Anti-drift: 04-agent prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import assert_category_workflow_skill_coverage, assert_human_review_preamble, assert_primary_workflow_surface_preamble, prompts_with_human_review, assert_human_review_required_matches_detection, assert_human_review_exempt_have_no_preamble_section, assert_human_review_sets_partition, PROMPT_CONTRACT_HEADINGS, PROMPT_EVAL_MIN_SCORE, assert_prompt_contract_headings, assert_prompt_meets_eval_harness_floor  # noqa: E402

REQUIRED_HEADINGS = PROMPT_CONTRACT_HEADINGS
MIN_SCORE = PROMPT_EVAL_MIN_SCORE

AGENT_DIR = Path(__file__).parent.parent.parent / "04-agent"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)

AGENT_PROMPTS = tuple(sorted(AGENT_DIR.glob("*.md")))
AGENT_COVER_WORKFLOW_SKILLS = (
    "reflective-dispatch",
    "reflective-spec-plan",
    "reflective-review",
    "reflective-handoff-retro",
    "reflective-research",
)
AGENT_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(AGENT_PROMPTS)
AGENT_HUMAN_REVIEW_REQUIRED = frozenset({
    "agent-scaffold-provenance.md",
    "agent-selection.md",
    "memory-consolidation.md",
    "retro.md",
    "review-rating-fix.md",
    "runtime-trust-boundary.md",
    "sop-compiler.md",
})
AGENT_HUMAN_REVIEW_EXEMPT = frozenset({
    "workflow-engine.md",
    "workflow-recipes.md",
})




@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", AGENT_PROMPTS, ids=lambda p: p.name)
def test_agent_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", AGENT_PROMPTS, ids=lambda p: p.name)
def test_agent_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    assert_prompt_meets_eval_harness_floor(prompt_path, harness, REPO_ROOT, MIN_SCORE)

def test_agent_prompts_reference_workflow_skills():
    for prompt_path in AGENT_PROMPTS:
        text = prompt_path.read_text(encoding="utf-8")
        assert "reflective-" in text, f"{prompt_path.name} should map to at least one workflow skill"


def test_agent_prompts_cover_agent_workflow_surfaces():
    assert_category_workflow_skill_coverage(
        AGENT_PROMPTS, AGENT_COVER_WORKFLOW_SKILLS, "04-agent"
    )


def test_agent_prompts_have_workflow_surface_preamble_line():
    """04-agent prompts use Primary workflow surface(s) or Supporting lens (trust boundary)."""
    for prompt_path in AGENT_PROMPTS:
        assert_primary_workflow_surface_preamble(prompt_path, category="04-agent")


@pytest.mark.parametrize(
    "prompt_path", AGENT_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_agent_prompt_has_human_review_section(prompt_path: Path):
    """Prompts with Human Review declare escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)

def test_agent_human_review_required_set_matches_detection():
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    assert_human_review_required_matches_detection(
        AGENT_HUMAN_REVIEW_REQUIRED, AGENT_PROMPTS
    )


def test_agent_human_review_exempt_prompts_have_no_preamble_section():
    """Exempt prompts keep Human Review cues in fenced templates only."""
    assert_human_review_exempt_have_no_preamble_section(
        AGENT_HUMAN_REVIEW_EXEMPT, AGENT_PROMPTS
    )


def test_agent_human_review_sets_partition_prompts():
    """Required + exempt sets must cover all prompts without overlap."""
    all_names = frozenset(p.name for p in AGENT_PROMPTS)
    assert_human_review_sets_partition(
        all_names,
        AGENT_HUMAN_REVIEW_REQUIRED,
        AGENT_HUMAN_REVIEW_EXEMPT,
    )

