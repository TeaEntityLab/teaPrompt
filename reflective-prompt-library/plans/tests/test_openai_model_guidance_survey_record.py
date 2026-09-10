"""Guard the 2026-09-10 OpenAI model guidance survey.

Tests:
- Survey record exists with correct structure
- Four adopted sentences are present at their single surfaces in the skills
- Vendor model names are absent from the four skill surfaces (clean-room)
- Panel verdicts and adopted wording are in the record
- Decision Index and case studies point to the record
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "openai-model-guidance-survey-2026-09-10.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

# Vendor model names that must not appear on durable skill surfaces. Excludes bare "codex" which appears in TeaPrompt source file names (codex-opencode.md).
VENDOR_TOKENS = re.compile(r"\bGPT-?[0-9]|gpt-?[0-9]|OpenAI\b|openai\b|Astra\b|astra\b")

# The four adopted sentences — each must appear exactly once at its single surface.
OG1_SENTENCE = "state each instruction once"
OG2_SENTENCE = "let the model choose the path unless a specific path is required"
OG3_SENTENCE = "Calibrate the depth of verification to the risk and reversibility of the change"
OG4_SENTENCE = "Do not search again to improve phrasing, add examples, or cite nonessential details"

SKILLS = library_skills_dir()


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _durable_surfaces() -> list[Path]:
    """All four skill surfaces that received adopted sentences."""
    return [
        SKILLS / "reflective-minimality" / "SKILL.md",
        SKILLS / "reflective-spec-plan" / "SKILL.md",
        SKILLS / "reflective-implement" / "SKILL.md",
        SKILLS / "reflective-research" / "SKILL.md",
    ]


def test_survey_record_exists_and_has_structure():
    text = _read(RECORD)
    assert "# OpenAI Model Guidance Survey" in text
    assert "## Candidate Adoption Ledger" in text
    assert "## Panel Verdicts" in text
    assert "## Adopted Wording" in text
    assert "## Source" in text
    assert "## Cross-Model Themes" in text


def test_og1_adopted_on_minimality():
    text = _read(SKILLS / "reflective-minimality" / "SKILL.md")
    assert OG1_SENTENCE in text, "OG-1 sentence missing from reflective-minimality"
    assert text.count(OG1_SENTENCE) == 1, "OG-1 sentence should appear exactly once"


def test_og2_adopted_on_spec_plan():
    text = _read(SKILLS / "reflective-spec-plan" / "SKILL.md")
    assert OG2_SENTENCE in text, "OG-2 sentence missing from reflective-spec-plan"
    assert text.count(OG2_SENTENCE) == 1, "OG-2 sentence should appear exactly once"


def test_og3_adopted_on_implement():
    text = _read(SKILLS / "reflective-implement" / "SKILL.md")
    assert OG3_SENTENCE in text, "OG-3 sentence missing from reflective-implement"
    assert text.count(OG3_SENTENCE) == 1, "OG-3 sentence should appear exactly once"


def test_og4_adopted_on_research():
    text = _read(SKILLS / "reflective-research" / "SKILL.md")
    assert OG4_SENTENCE in text, "OG-4 sentence missing from reflective-research"
    assert text.count(OG4_SENTENCE) == 1, "OG-4 sentence should appear exactly once"


def test_no_vendor_tokens_on_durable_surfaces():
    """Vendor model names must not appear on the four skill surfaces (clean-room)."""
    for path in _durable_surfaces():
        body = _read(path)
        matches = VENDOR_TOKENS.findall(body)
        assert not matches, f"vendor token {matches} found in {path.name}"


def test_panel_verdicts_in_record():
    text = _read(RECORD)
    for token in (
        "OG-1",
        "OG-2",
        "OG-3",
        "OG-4",
        "OG-5",
        "Adopted",
        "Rejected",
    ):
        assert token in text, f"panel verdict token {token!r} missing from record"


def test_og5_rejection_rationale_in_record():
    text = _read(RECORD)
    assert "implicit" in text, "OG-5 rejection rationale missing"
    assert "wrong surface" in text or "Durable Lesson" in text, "OG-5 surface objection missing"


def test_indexes_point_to_record():
    knowledge = _read(PROJECT_KNOWLEDGE)
    assert "openai-model-guidance-survey-2026-09-10.md" in knowledge, "Decision Index missing record link"
    case_studies = _read(CASE_STUDIES)
    assert "openai-model-guidance-survey-2026-09-10.md" in case_studies
    # Case comparison row + state ledger row = at least 2
    assert case_studies.count("openai-model-guidance-survey-2026-09-10.md") >= 2


def test_record_has_nine_model_names():
    """The survey record should name all nine models surveyed."""
    text = _read(RECORD)
    for model in (
        "gpt-4.1",
        "gpt-5",
        "gpt-5.1",
        "gpt-5.2",
        "gpt-5.3-codex",
        "gpt-5.4",
        "gpt-5.5",
        "gpt-5.6",
        "gpt-6-astra",
    ):
        assert model in text, f"model {model!r} missing from survey record"
