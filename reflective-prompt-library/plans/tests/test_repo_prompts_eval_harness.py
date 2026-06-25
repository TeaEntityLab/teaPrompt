"""Anti-drift: 06-repo prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import assert_category_workflow_skill_coverage, assert_human_review_preamble, assert_primary_workflow_surface_preamble, prompts_with_human_review, assert_human_review_required_matches_detection, assert_human_review_exempt_have_no_preamble_section, assert_human_review_sets_partition, PROMPT_CONTRACT_HEADINGS, PROMPT_EVAL_MIN_SCORE, assert_prompt_contract_headings, assert_prompt_references_workflow_skill, assert_prompt_meets_eval_harness_floor  # noqa: E402

REQUIRED_HEADINGS = PROMPT_CONTRACT_HEADINGS
MIN_SCORE = PROMPT_EVAL_MIN_SCORE

REPO_DIR = Path(__file__).parent.parent.parent / "06-repo"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)

REPO_PROMPTS = tuple(sorted(REPO_DIR.glob("*.md")))
REPO_COVER_WORKFLOW_SKILLS = (
    "reflective-dispatch",
    "reflective-implement",
    "reflective-handoff-retro",
)
REPO_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(REPO_PROMPTS)
REPO_HUMAN_REVIEW_REQUIRED = frozenset({
    "AGENTS.md",
    "PROJECT_KNOWLEDGE.template.md",
    "cursor-rules.md",
})
REPO_HUMAN_REVIEW_EXEMPT = frozenset({
    "codex-opencode.md",
})




@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", REPO_PROMPTS, ids=lambda p: p.name)
def test_repo_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", REPO_PROMPTS, ids=lambda p: p.name)
def test_repo_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    assert_prompt_meets_eval_harness_floor(prompt_path, harness, REPO_ROOT, MIN_SCORE)

def test_repo_prompts_reference_workflow_skills():
    for prompt_path in REPO_PROMPTS:
        assert_prompt_references_workflow_skill(prompt_path)


def test_repo_prompts_cover_harness_surfaces():
    assert_category_workflow_skill_coverage(
        REPO_PROMPTS, REPO_COVER_WORKFLOW_SKILLS, "06-repo"
    )


def test_agents_md_retains_harness_policy_section():
    text = (REPO_DIR / "AGENTS.md").read_text(encoding="utf-8")
    assert "## Harness Policy (Nine Skills)" in text
    assert "make all" in text


def test_repo_prompts_have_primary_workflow_surfaces_line():
    """All 06-repo prompts declare Primary workflow surface(s) in Purpose preambles."""
    for prompt_path in REPO_PROMPTS:
        assert_primary_workflow_surface_preamble(prompt_path, category="06-repo")


@pytest.mark.parametrize(
    "prompt_path", REPO_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_repo_prompt_has_human_review_section(prompt_path: Path):
    """Prompts with Human Review declare escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)

def test_repo_human_review_required_set_matches_detection():
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    assert_human_review_required_matches_detection(
        REPO_HUMAN_REVIEW_REQUIRED, REPO_PROMPTS
    )


def test_repo_human_review_exempt_prompts_have_no_preamble_section():
    """Exempt prompts keep Human Review cues in fenced templates only."""
    assert_human_review_exempt_have_no_preamble_section(
        REPO_HUMAN_REVIEW_EXEMPT, REPO_PROMPTS
    )


def test_repo_human_review_sets_partition_prompts():
    """Required + exempt sets must cover all prompts without overlap."""
    all_names = frozenset(p.name for p in REPO_PROMPTS)
    assert_human_review_sets_partition(
        all_names,
        REPO_HUMAN_REVIEW_REQUIRED,
        REPO_HUMAN_REVIEW_EXEMPT,
    )

