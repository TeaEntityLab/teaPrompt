"""Anti-drift: 02-engineering prompts must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from eval_harness import EvalHarness  # noqa: E402

ENGINEERING_DIR = Path(__file__).parent.parent.parent / "02-engineering"
REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)
MIN_SCORE = 80.0

REQUIRED_HEADINGS = (
    "## Purpose",
    "## Scope",
    "## Acceptance Criteria",
    "## Falsifiability",
)

ENGINEERING_PROMPTS = tuple(sorted(ENGINEERING_DIR.glob("*.md")))


@pytest.fixture(scope="module")
def harness() -> EvalHarness:
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.mark.parametrize("prompt_path", ENGINEERING_PROMPTS, ids=lambda p: p.name)
def test_engineering_prompt_has_contract_headings(prompt_path: Path):
    text = prompt_path.read_text(encoding="utf-8")
    preamble = text.split("```", 1)[0]
    for heading in REQUIRED_HEADINGS:
        assert heading in preamble, f"{prompt_path.name} missing {heading} outside template block"


@pytest.mark.parametrize("prompt_path", ENGINEERING_PROMPTS, ids=lambda p: p.name)
def test_engineering_prompt_meets_eval_harness_floor(prompt_path: Path, harness: EvalHarness):
    rel = str(prompt_path.relative_to(REPO_ROOT))
    result = harness.evaluate_file(rel)
    assert result["score"] >= MIN_SCORE, (
        f"{prompt_path.name} eval_harness score {result['score']}% < {MIN_SCORE}%: "
        f"{[(c['id'], c['result']) for c in result['checks']]}"
    )


def test_engineering_prompts_reference_workflow_skills():
    for prompt_path in ENGINEERING_PROMPTS:
        text = prompt_path.read_text(encoding="utf-8")
        assert "reflective-" in text, f"{prompt_path.name} should map to at least one workflow skill"


def test_engineering_prompts_cover_core_workflows():
    """At least one prompt per implement/review/spec-plan/brief surface."""
    text = "\n".join(p.read_text(encoding="utf-8") for p in ENGINEERING_PROMPTS)
    for skill in (
        "reflective-brief",
        "reflective-spec-plan",
        "reflective-implement",
        "reflective-review",
    ):
        assert skill in text, f"02-engineering should reference {skill}"
