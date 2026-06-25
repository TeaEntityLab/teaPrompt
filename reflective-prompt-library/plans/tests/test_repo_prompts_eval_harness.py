"""Anti-drift: 06-repo templates must satisfy eval_harness structural rubric."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from eval_harness import EvalHarness  # noqa: E402

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
