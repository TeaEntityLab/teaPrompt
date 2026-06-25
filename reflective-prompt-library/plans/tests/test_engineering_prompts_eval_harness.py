"""Anti-drift: 02-engineering prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import assert_category_workflow_skill_coverage, assert_human_review_preamble, assert_primary_workflow_surface_preamble, prompts_with_human_review, assert_human_review_required_matches_detection, assert_human_review_exempt_have_no_preamble_section, assert_human_review_sets_partition, PROMPT_CONTRACT_HEADINGS, PROMPT_EVAL_MIN_SCORE, assert_prompt_contract_headings, assert_prompt_references_workflow_skill, assert_prompt_meets_eval_harness_floor  # noqa: E402

REQUIRED_HEADINGS = PROMPT_CONTRACT_HEADINGS
MIN_SCORE = PROMPT_EVAL_MIN_SCORE

ENGINEERING_DIR = Path(__file__).parent.parent.parent / "02-engineering"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)

ENGINEERING_PROMPTS = tuple(sorted(ENGINEERING_DIR.glob("*.md")))
ENGINEERING_COVER_WORKFLOW_SKILLS = (
    "reflective-brief",
    "reflective-spec-plan",
    "reflective-implement",
    "reflective-review",
)
ENGINEERING_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(ENGINEERING_PROMPTS)
ENGINEERING_HUMAN_REVIEW_REQUIRED = frozenset({
    "code-reviewer.md",
    "implementation-agent.md",
    "local-feedback.md",
})
ENGINEERING_HUMAN_REVIEW_EXEMPT = frozenset({
    "spec-writer.md",
    "task-slicer.md",
    "task-start.md",
    "test-designer.md",
    "usage-first.md",
})




@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", ENGINEERING_PROMPTS, ids=lambda p: p.name)
def test_engineering_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", ENGINEERING_PROMPTS, ids=lambda p: p.name)
def test_engineering_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    assert_prompt_meets_eval_harness_floor(prompt_path, harness, REPO_ROOT, MIN_SCORE)

def test_engineering_prompts_reference_workflow_skills():
    for prompt_path in ENGINEERING_PROMPTS:
        assert_prompt_references_workflow_skill(prompt_path)


def test_engineering_prompts_cover_core_workflows():
    """At least one prompt per implement/review/spec-plan/brief surface."""
    assert_category_workflow_skill_coverage(
        ENGINEERING_PROMPTS, ENGINEERING_COVER_WORKFLOW_SKILLS, "02-engineering"
    )


def test_engineering_prompts_have_primary_workflow_surfaces_line():
    """All 02-engineering prompts declare Primary workflow surface(s) in Purpose preambles."""
    for prompt_path in ENGINEERING_PROMPTS:
        assert_primary_workflow_surface_preamble(prompt_path, category="02-engineering")


@pytest.mark.parametrize(
    "prompt_path", ENGINEERING_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_engineering_prompt_has_human_review_section(prompt_path: Path):
    """Prompts with Human Review declare escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)

def test_engineering_human_review_required_set_matches_detection():
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    assert_human_review_required_matches_detection(
        ENGINEERING_HUMAN_REVIEW_REQUIRED, ENGINEERING_PROMPTS
    )


def test_engineering_human_review_exempt_prompts_have_no_preamble_section():
    """Exempt prompts keep Human Review cues in fenced templates only."""
    assert_human_review_exempt_have_no_preamble_section(
        ENGINEERING_HUMAN_REVIEW_EXEMPT, ENGINEERING_PROMPTS
    )


def test_engineering_human_review_sets_partition_prompts():
    """Required + exempt sets must cover all prompts without overlap."""
    all_names = frozenset(p.name for p in ENGINEERING_PROMPTS)
    assert_human_review_sets_partition(
        all_names,
        ENGINEERING_HUMAN_REVIEW_REQUIRED,
        ENGINEERING_HUMAN_REVIEW_EXEMPT,
    )

