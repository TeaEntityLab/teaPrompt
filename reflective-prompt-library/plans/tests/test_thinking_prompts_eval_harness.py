"""Anti-drift: 01-thinking prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from prompt_eval_helpers import (
    category_prompt_dir,
    sorted_category_prompts,
    PROMPT_LIBRARY_REPO_ROOT,
    make_category_eval_harness_fixture,
    PROMPT_CONTRACT_HEADINGS,
    PROMPT_EVAL_MIN_SCORE,
    assert_primary_workflow_surface_preamble,
    assert_prompt_contract_headings,
    assert_prompt_references_workflow_skill,
    assert_prompt_meets_eval_harness_floor,
    assert_human_review_exempt_have_no_preamble_section,
    assert_human_review_preamble,
    assert_human_review_required_matches_detection,
    assert_human_review_sets_partition,
    prompts_with_human_review,
)

sys.path.insert(0, str(Path(__file__).parent.parent))

from eval_harness import EvalHarness  # noqa: E402

REQUIRED_HEADINGS = PROMPT_CONTRACT_HEADINGS
MIN_SCORE = PROMPT_EVAL_MIN_SCORE

THINKING_DIR = category_prompt_dir("01-thinking")
REPO_ROOT = PROMPT_LIBRARY_REPO_ROOT

THINKING_PROMPTS = sorted_category_prompts("01-thinking")
THINKING_COVER_WORKFLOW_SKILLS: tuple[str, ...] = ()  # consumer graph in test_prompt_cross_links.py
THINKING_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(THINKING_PROMPTS)
THINKING_HUMAN_REVIEW_REQUIRED = frozenset({
    "counterargument.md",
    "critical-thinking-check.md",
    "falsifiability.md",
    "socratic-reviewer.md",
    "why-what-how-done.md",
})
THINKING_HUMAN_REVIEW_EXEMPT = frozenset()


harness = make_category_eval_harness_fixture(REPO_ROOT)


@pytest.mark.parametrize("prompt_path", THINKING_PROMPTS, ids=lambda p: p.name)
def test_thinking_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", THINKING_PROMPTS, ids=lambda p: p.name)
def test_thinking_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    assert_prompt_meets_eval_harness_floor(prompt_path, harness, REPO_ROOT, MIN_SCORE)


def test_thinking_prompts_reference_workflow_skills():
    for prompt_path in THINKING_PROMPTS:
        assert_prompt_references_workflow_skill(prompt_path)


def test_thinking_prompts_have_primary_workflow_surfaces_line():
    """All 01-thinking lenses name consumer workflow skills in Purpose preambles."""
    for prompt_path in THINKING_PROMPTS:
        assert_primary_workflow_surface_preamble(prompt_path, category="01-thinking")


@pytest.mark.parametrize(
    "prompt_path", THINKING_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_thinking_prompt_has_human_review_section(prompt_path: Path):
    """All 01-thinking lenses declare Human Review escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)


def test_thinking_human_review_required_set_matches_detection():
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    assert_human_review_required_matches_detection(
        THINKING_HUMAN_REVIEW_REQUIRED, THINKING_PROMPTS
    )


def test_thinking_human_review_exempt_prompts_have_no_preamble_section():
    """Exempt prompts keep Human Review cues in fenced templates only."""
    assert_human_review_exempt_have_no_preamble_section(
        THINKING_HUMAN_REVIEW_EXEMPT, THINKING_PROMPTS
    )


def test_thinking_human_review_sets_partition_prompts():
    """Required + exempt sets must cover all prompts without overlap."""
    all_names = frozenset(p.name for p in THINKING_PROMPTS)
    assert_human_review_sets_partition(
        all_names,
        THINKING_HUMAN_REVIEW_REQUIRED,
        THINKING_HUMAN_REVIEW_EXEMPT,
    )
