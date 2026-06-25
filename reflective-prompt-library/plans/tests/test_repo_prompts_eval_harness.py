"""Anti-drift: 06-repo prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import prompts_with_human_review  # noqa: E402

REPO_DIR = Path(__file__).parent.parent.parent / "06-repo"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)
MIN_SCORE = 80.0

REQUIRED_HEADINGS = (
    "## Purpose",
    "## Scope",
    "## Acceptance Criteria",
    "## Falsifiability",
)

REPO_PROMPTS = tuple(sorted(REPO_DIR.glob("*.md")))
REPO_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(REPO_PROMPTS)


@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", REPO_PROMPTS, ids=lambda p: p.name)
def test_repo_prompt_has_contract_headings(prompt_path: Path):
    text = prompt_path.read_text(encoding="utf-8")
    preamble = text.split("```", 1)[0]
    for heading in REQUIRED_HEADINGS:
        assert heading in preamble, f"{prompt_path.name} missing {heading} outside template block"


@pytest.mark.parametrize("prompt_path", REPO_PROMPTS, ids=lambda p: p.name)
def test_repo_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    rel = str(prompt_path.relative_to(REPO_ROOT))
    result = harness.evaluate_file(rel)
    assert result["score"] >= MIN_SCORE, (
        f"{prompt_path.name} eval_harness score {result['score']}% < {MIN_SCORE}%: "
        f"{[(c['id'], c['result']) for c in result['checks']]}"
    )

def test_repo_prompts_reference_workflow_skills():
    for prompt_path in REPO_PROMPTS:
        text = prompt_path.read_text(encoding="utf-8")
        assert "reflective-" in text, f"{prompt_path.name} should map to at least one workflow skill"


def test_repo_prompts_cover_harness_surfaces():
    text = "\n".join(p.read_text(encoding="utf-8") for p in REPO_PROMPTS)
    for skill in (
        "reflective-dispatch",
        "reflective-implement",
        "reflective-handoff-retro",
    ):
        assert skill in text, f"06-repo should reference {skill}"


def test_agents_md_retains_harness_policy_section():
    text = (REPO_DIR / "AGENTS.md").read_text(encoding="utf-8")
    assert "## Harness Policy (Nine Skills)" in text
    assert "make all" in text


def test_repo_prompts_have_primary_workflow_surfaces_line():
    """All 06-repo prompts declare Primary workflow surface(s) in Purpose preambles."""
    for prompt_path in REPO_PROMPTS:
        preamble = prompt_path.read_text(encoding="utf-8").split("```", 1)[0]
        assert "Primary workflow surface" in preamble, (
            f"{prompt_path.name} Purpose should list Primary workflow surface(s)"
        )


@pytest.mark.parametrize(
    "prompt_path", REPO_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_repo_prompt_has_human_review_section(prompt_path: Path):
    """Prompts with Human Review declare escalation outside zh-TW templates."""
    preamble = prompt_path.read_text(encoding="utf-8").split("```", 1)[0]
    assert "## Human Review" in preamble, f"{prompt_path.name} missing Human Review preamble"
    assert "reflective-risk" in preamble, (
        f"{prompt_path.name} Human Review should route to reflective-risk"
    )
