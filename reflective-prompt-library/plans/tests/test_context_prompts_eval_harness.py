"""Anti-drift: 03-context prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import PROMPT_LIBRARY_REPO_ROOT, make_category_eval_harness_fixture, assert_category_workflow_skill_coverage, assert_human_review_preamble, assert_primary_workflow_surface_preamble, prompts_with_human_review, assert_human_review_required_matches_detection, assert_human_review_exempt_have_no_preamble_section, assert_human_review_sets_partition, PROMPT_CONTRACT_HEADINGS, PROMPT_EVAL_MIN_SCORE, assert_prompt_contract_headings, assert_prompt_references_workflow_skill, assert_prompt_meets_eval_harness_floor  # noqa: E402

REQUIRED_HEADINGS = PROMPT_CONTRACT_HEADINGS
MIN_SCORE = PROMPT_EVAL_MIN_SCORE

CONTEXT_DIR = Path(__file__).parent.parent.parent / "03-context"
REPO_ROOT = PROMPT_LIBRARY_REPO_ROOT

CONTEXT_PROMPTS = tuple(sorted(CONTEXT_DIR.glob("*.md")))
CONTEXT_COVER_WORKFLOW_SKILLS = (
    "reflective-dispatch",
    "reflective-brief",
    "reflective-handoff-retro",
    "reflective-research",
)
CONTEXT_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(CONTEXT_PROMPTS)
CONTEXT_HUMAN_REVIEW_REQUIRED = frozenset({
    "context-handoff.md",
    "low-token.md",
    "small-context.md",
})
CONTEXT_HUMAN_REVIEW_EXEMPT = frozenset({
    "context-engineering.md",
    "gemini-long-document.md",
    "large-context.md",
    "medium-context.md",
})




harness = make_category_eval_harness_fixture(REPO_ROOT)


@pytest.mark.parametrize("prompt_path", CONTEXT_PROMPTS, ids=lambda p: p.name)
def test_context_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", CONTEXT_PROMPTS, ids=lambda p: p.name)
def test_context_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    assert_prompt_meets_eval_harness_floor(prompt_path, harness, REPO_ROOT, MIN_SCORE)

def test_context_prompts_reference_workflow_skills():
    for prompt_path in CONTEXT_PROMPTS:
        assert_prompt_references_workflow_skill(prompt_path)


def test_context_prompts_cover_context_workflow_surfaces():
    assert_category_workflow_skill_coverage(
        CONTEXT_PROMPTS, CONTEXT_COVER_WORKFLOW_SKILLS, "03-context"
    )


def test_context_prompts_have_primary_workflow_surfaces_line():
    """All 03-context prompts declare Primary workflow surface(s) in Purpose preambles."""
    for prompt_path in CONTEXT_PROMPTS:
        assert_primary_workflow_surface_preamble(prompt_path, category="03-context")


@pytest.mark.parametrize(
    "prompt_path", CONTEXT_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_context_prompt_has_human_review_section(prompt_path: Path):
    """Prompts with Human Review declare escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)

def test_context_human_review_required_set_matches_detection():
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    assert_human_review_required_matches_detection(
        CONTEXT_HUMAN_REVIEW_REQUIRED, CONTEXT_PROMPTS
    )


def test_context_human_review_exempt_prompts_have_no_preamble_section():
    """Exempt prompts keep Human Review cues in fenced templates only."""
    assert_human_review_exempt_have_no_preamble_section(
        CONTEXT_HUMAN_REVIEW_EXEMPT, CONTEXT_PROMPTS
    )


def test_context_human_review_sets_partition_prompts():
    """Required + exempt sets must cover all prompts without overlap."""
    all_names = frozenset(p.name for p in CONTEXT_PROMPTS)
    assert_human_review_sets_partition(
        all_names,
        CONTEXT_HUMAN_REVIEW_REQUIRED,
        CONTEXT_HUMAN_REVIEW_EXEMPT,
    )

