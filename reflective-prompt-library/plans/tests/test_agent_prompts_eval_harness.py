"""Anti-drift: 04-agent prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from eval_harness import EvalHarness  # noqa: E402
from prompt_eval_helpers import prompts_with_human_review  # noqa: E402

AGENT_DIR = Path(__file__).parent.parent.parent / "04-agent"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)
MIN_SCORE = 80.0

REQUIRED_HEADINGS = (
    "## Purpose",
    "## Scope",
    "## Acceptance Criteria",
    "## Falsifiability",
)

AGENT_PROMPTS = tuple(sorted(AGENT_DIR.glob("*.md")))
AGENT_PROMPTS_WITH_HUMAN_REVIEW = prompts_with_human_review(AGENT_PROMPTS)
SUPPORTING_LENS_AGENT_PROMPTS = frozenset({"runtime-trust-boundary.md"})


@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", AGENT_PROMPTS, ids=lambda p: p.name)
def test_agent_prompt_has_contract_headings(prompt_path: Path):
    text = prompt_path.read_text(encoding="utf-8")
    preamble = text.split("```", 1)[0]
    for heading in REQUIRED_HEADINGS:
        assert heading in preamble, f"{prompt_path.name} missing {heading} outside template block"


@pytest.mark.parametrize("prompt_path", AGENT_PROMPTS, ids=lambda p: p.name)
def test_agent_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    rel = str(prompt_path.relative_to(REPO_ROOT))
    result = harness.evaluate_file(rel)
    assert result["score"] >= MIN_SCORE, (
        f"{prompt_path.name} eval_harness score {result['score']}% < {MIN_SCORE}%: "
        f"{[(c['id'], c['result']) for c in result['checks']]}"
    )

def test_agent_prompts_reference_workflow_skills():
    for prompt_path in AGENT_PROMPTS:
        text = prompt_path.read_text(encoding="utf-8")
        assert "reflective-" in text, f"{prompt_path.name} should map to at least one workflow skill"


def test_agent_prompts_cover_agent_workflow_surfaces():
    text = "\n".join(p.read_text(encoding="utf-8") for p in AGENT_PROMPTS)
    for skill in (
        "reflective-dispatch",
        "reflective-spec-plan",
        "reflective-review",
        "reflective-handoff-retro",
        "reflective-research",
    ):
        assert skill in text, f"04-agent should reference {skill}"


def test_agent_prompts_have_workflow_surface_preamble_line():
    """04-agent prompts use Primary workflow surface(s) or Supporting lens (trust boundary)."""
    for prompt_path in AGENT_PROMPTS:
        preamble = prompt_path.read_text(encoding="utf-8").split("```", 1)[0]
        if prompt_path.name in SUPPORTING_LENS_AGENT_PROMPTS:
            assert "Supporting lens for" in preamble, (
                f"{prompt_path.name} Purpose should use Supporting lens for workflow skills"
            )
        else:
            assert "Primary workflow surface" in preamble, (
                f"{prompt_path.name} Purpose should list Primary workflow surface(s)"
            )


@pytest.mark.parametrize(
    "prompt_path", AGENT_PROMPTS_WITH_HUMAN_REVIEW, ids=lambda p: p.name
)
def test_agent_prompt_has_human_review_section(prompt_path: Path):
    """Prompts with Human Review declare escalation outside zh-TW templates."""
    preamble = prompt_path.read_text(encoding="utf-8").split("```", 1)[0]
    assert "## Human Review" in preamble, f"{prompt_path.name} missing Human Review preamble"
    assert "reflective-risk" in preamble, (
        f"{prompt_path.name} Human Review should route to reflective-risk"
    )
