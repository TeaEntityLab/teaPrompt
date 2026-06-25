"""Anti-drift: 00-core prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import (
    category_prompt_dir,
    sorted_category_prompts,
    PROMPT_LIBRARY_REPO_ROOT,
    make_category_eval_harness_fixture,
    PROMPT_CONTRACT_HEADINGS,
    PROMPT_EVAL_MIN_SCORE,
    assert_primary_workflow_surface_preamble,
    assert_category_workflow_skill_coverage, assert_prompt_contract_headings,
    assert_prompt_references_workflow_skill,
    assert_prompt_meets_eval_harness_floor,  # noqa: E402
    assert_human_review_exempt_have_no_preamble_section,
    assert_human_review_preamble,
    assert_human_review_required_matches_detection,
    assert_human_review_sets_partition,
    prompts_with_human_review,
)

REQUIRED_HEADINGS = PROMPT_CONTRACT_HEADINGS
MIN_SCORE = PROMPT_EVAL_MIN_SCORE

CORE_DIR = category_prompt_dir("00-core")
REPO_ROOT = PROMPT_LIBRARY_REPO_ROOT

CORE_PROMPTS = sorted_category_prompts("00-core")
CORE_COVER_WORKFLOW_SKILLS = (
    "reflective-brief",
    "reflective-dispatch",
)
CORE_HUMAN_REVIEW_REQUIRED = frozenset({
    "core-full.md",
    "core-minimal.md",
    "core-short.md",
    "custom-instruction-en.md",
    "custom-instruction-zh.md",
    "important-task-full.md",
})
CORE_HUMAN_REVIEW_EXEMPT = frozenset({
    "daily-minimal.md",
    "global-controller.md",
    "master-prompt.md",
})

CORE_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(CORE_PROMPTS)


harness = make_category_eval_harness_fixture(REPO_ROOT)


@pytest.mark.parametrize("prompt_path", CORE_PROMPTS, ids=lambda p: p.name)
def test_core_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", CORE_PROMPTS, ids=lambda p: p.name)
def test_core_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    assert_prompt_meets_eval_harness_floor(prompt_path, harness, REPO_ROOT, MIN_SCORE)


def test_core_prompts_reference_workflow_skills():
    for prompt_path in CORE_PROMPTS:
        assert_prompt_references_workflow_skill(prompt_path)


def test_core_prompts_cover_brief_and_dispatch():
    assert_category_workflow_skill_coverage(
        CORE_PROMPTS, CORE_COVER_WORKFLOW_SKILLS, "00-core"
    )


def test_core_prompts_have_primary_workflow_surfaces_line():
    """All 00-core prompts declare Primary workflow surface(s) in Purpose preambles."""
    for prompt_path in CORE_PROMPTS:
        assert_primary_workflow_surface_preamble(prompt_path, category="00-core")


@pytest.mark.parametrize(
    "prompt_path", CORE_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_core_prompt_has_human_review_section(prompt_path: Path):
    """Risk-bearing 00-core prompts declare Human Review escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)


def test_core_human_review_required_set_matches_detection():
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    assert_human_review_required_matches_detection(
        CORE_HUMAN_REVIEW_REQUIRED, CORE_PROMPTS
    )


def test_core_human_review_exempt_prompts_have_no_preamble_section():
    """L1 opener prompts keep Human Review cues in fenced templates only."""
    assert_human_review_exempt_have_no_preamble_section(
        CORE_HUMAN_REVIEW_EXEMPT, CORE_PROMPTS
    )


def test_core_human_review_sets_partition_core_prompts():
    """Required + exempt sets must cover all 00-core prompts without overlap."""
    all_names = frozenset(p.name for p in CORE_PROMPTS)
    assert_human_review_sets_partition(
        all_names,
        CORE_HUMAN_REVIEW_REQUIRED,
        CORE_HUMAN_REVIEW_EXEMPT,
    )
