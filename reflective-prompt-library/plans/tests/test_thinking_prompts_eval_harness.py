"""Anti-drift: 01-thinking prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from prompt_eval_helpers import (
    PROMPT_CONTRACT_HEADINGS,
    PROMPT_EVAL_MIN_SCORE,
    assert_prompt_contract_headings,
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

THINKING_DIR = Path(__file__).parent.parent.parent / "01-thinking"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)

THINKING_PROMPTS = tuple(sorted(THINKING_DIR.glob("*.md")))
THINKING_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(THINKING_PROMPTS)
THINKING_HUMAN_REVIEW_REQUIRED = frozenset({
    "counterargument.md",
    "critical-thinking-check.md",
    "falsifiability.md",
    "socratic-reviewer.md",
    "why-what-how-done.md",
})
THINKING_HUMAN_REVIEW_EXEMPT = frozenset()


@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", THINKING_PROMPTS, ids=lambda p: p.name)
def test_thinking_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", THINKING_PROMPTS, ids=lambda p: p.name)
def test_thinking_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    rel = str(prompt_path.relative_to(REPO_ROOT))
    result = harness.evaluate_file(rel)
    assert result["score"] >= MIN_SCORE, (
        f"{prompt_path.name} eval_harness score {result['score']}% < {MIN_SCORE}%: "
        f"{[(c['id'], c['result']) for c in result['checks']]}"
    )


def test_thinking_prompts_reference_workflow_skills():
    for prompt_path in THINKING_PROMPTS:
        text = prompt_path.read_text(encoding="utf-8")
        assert "reflective-" in text, f"{prompt_path.name} should map to at least one workflow skill"


def test_thinking_prompts_have_primary_workflow_surfaces_line():
    """All 01-thinking lenses name consumer workflow skills in Purpose preambles."""
    for prompt_path in THINKING_PROMPTS:
        preamble = prompt_path.read_text(encoding="utf-8").split("```", 1)[0]
        assert "Primary workflow surfaces" in preamble, (
            f"{prompt_path.name} Purpose should list Primary workflow surfaces"
        )


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
