"""Anti-drift: 05-domain prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import assert_human_review_preamble, prompts_with_human_review, assert_human_review_required_matches_detection, assert_human_review_exempt_have_no_preamble_section, assert_human_review_sets_partition, PROMPT_CONTRACT_HEADINGS, PROMPT_EVAL_MIN_SCORE, assert_prompt_contract_headings  # noqa: E402

REQUIRED_HEADINGS = PROMPT_CONTRACT_HEADINGS
MIN_SCORE = PROMPT_EVAL_MIN_SCORE

DOMAIN_DIR = Path(__file__).parent.parent.parent / "05-domain"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)

DOMAIN_PROMPTS = tuple(sorted(DOMAIN_DIR.glob("*.md")))
DOMAIN_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(DOMAIN_PROMPTS)
DOMAIN_HUMAN_REVIEW_REQUIRED = frozenset({
    "creative-template.md",
    "high-risk.md",
})
DOMAIN_HUMAN_REVIEW_EXEMPT = frozenset({
    "business-strategy.md",
    "deep-analysis.md",
    "learning-coach.md",
    "research.md",
    "writing-article.md",
})




@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", DOMAIN_PROMPTS, ids=lambda p: p.name)
def test_domain_prompt_has_contract_headings(prompt_path: Path):
    assert_prompt_contract_headings(prompt_path)


@pytest.mark.parametrize("prompt_path", DOMAIN_PROMPTS, ids=lambda p: p.name)
def test_domain_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    rel = str(prompt_path.relative_to(REPO_ROOT))
    result = harness.evaluate_file(rel)
    assert result["score"] >= MIN_SCORE, (
        f"{prompt_path.name} eval_harness score {result['score']}% < {MIN_SCORE}%: "
        f"{[(c['id'], c['result']) for c in result['checks']]}"
    )

def test_domain_prompts_reference_workflow_skills():
    for prompt_path in DOMAIN_PROMPTS:
        text = prompt_path.read_text(encoding="utf-8")
        assert "reflective-" in text, f"{prompt_path.name} should map to at least one workflow skill"


def test_domain_prompts_cover_domain_workflow_surfaces():
    text = "\n".join(p.read_text(encoding="utf-8") for p in DOMAIN_PROMPTS)
    for skill in (
        "reflective-risk",
        "reflective-research",
        "reflective-brief",
        "reflective-spec-plan",
        "reflective-review",
    ):
        assert skill in text, f"05-domain should reference {skill}"


def test_domain_prompts_have_primary_workflow_surfaces_line():
    """All 05-domain prompts declare Primary workflow surface(s) in Purpose preambles."""
    for prompt_path in DOMAIN_PROMPTS:
        preamble = prompt_path.read_text(encoding="utf-8").split("```", 1)[0]
        assert "Primary workflow surface" in preamble, (
            f"{prompt_path.name} Purpose should list Primary workflow surface(s)"
        )


@pytest.mark.parametrize(
    "prompt_path", DOMAIN_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_domain_prompt_has_human_review_section(prompt_path: Path):
    """Prompts with Human Review declare escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)

def test_domain_human_review_required_set_matches_detection():
    """Frozen required set must match prompts that declare ## Human Review in preambles."""
    assert_human_review_required_matches_detection(
        DOMAIN_HUMAN_REVIEW_REQUIRED, DOMAIN_PROMPTS
    )


def test_domain_human_review_exempt_prompts_have_no_preamble_section():
    """Exempt prompts keep Human Review cues in fenced templates only."""
    assert_human_review_exempt_have_no_preamble_section(
        DOMAIN_HUMAN_REVIEW_EXEMPT, DOMAIN_PROMPTS
    )


def test_domain_human_review_sets_partition_prompts():
    """Required + exempt sets must cover all prompts without overlap."""
    all_names = frozenset(p.name for p in DOMAIN_PROMPTS)
    assert_human_review_sets_partition(
        all_names,
        DOMAIN_HUMAN_REVIEW_REQUIRED,
        DOMAIN_HUMAN_REVIEW_EXEMPT,
    )

