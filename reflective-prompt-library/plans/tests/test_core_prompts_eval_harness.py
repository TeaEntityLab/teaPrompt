"""Anti-drift: 00-core prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import assert_human_review_preamble, prompts_with_human_review  # noqa: E402

CORE_DIR = Path(__file__).parent.parent.parent / "00-core"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)
MIN_SCORE = 80.0

REQUIRED_HEADINGS = (
    "## Purpose",
    "## Scope",
    "## Acceptance Criteria",
    "## Falsifiability",
)

CORE_PROMPTS = tuple(sorted(CORE_DIR.glob("*.md")))
CORE_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(CORE_PROMPTS)


@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", CORE_PROMPTS, ids=lambda p: p.name)
def test_core_prompt_has_contract_headings(prompt_path: Path):
    text = prompt_path.read_text(encoding="utf-8")
    preamble = text.split("```", 1)[0]
    for heading in REQUIRED_HEADINGS:
        assert heading in preamble, f"{prompt_path.name} missing {heading} outside template block"


@pytest.mark.parametrize("prompt_path", CORE_PROMPTS, ids=lambda p: p.name)
def test_core_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    rel = str(prompt_path.relative_to(REPO_ROOT))
    result = harness.evaluate_file(rel)
    assert result["score"] >= MIN_SCORE, (
        f"{prompt_path.name} eval_harness score {result['score']}% < {MIN_SCORE}%: "
        f"{[(c['id'], c['result']) for c in result['checks']]}"
    )


def test_core_prompts_reference_workflow_skills():
    for prompt_path in CORE_PROMPTS:
        text = prompt_path.read_text(encoding="utf-8")
        assert "reflective-" in text, f"{prompt_path.name} should map to at least one workflow skill"


def test_core_prompts_cover_brief_and_dispatch():
    text = "\n".join(p.read_text(encoding="utf-8") for p in CORE_PROMPTS)
    assert "reflective-brief" in text
    assert "reflective-dispatch" in text


def test_core_prompts_have_primary_workflow_surfaces_line():
    """All 00-core prompts declare Primary workflow surface(s) in Purpose preambles."""
    for prompt_path in CORE_PROMPTS:
        preamble = prompt_path.read_text(encoding="utf-8").split("```", 1)[0]
        assert "Primary workflow surface" in preamble, (
            f"{prompt_path.name} Purpose should list Primary workflow surface(s)"
        )


@pytest.mark.parametrize(
    "prompt_path", CORE_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_core_prompt_has_human_review_section(prompt_path: Path):
    """Risk-bearing 00-core prompts declare Human Review escalation outside zh-TW templates."""
    assert_human_review_preamble(prompt_path)
