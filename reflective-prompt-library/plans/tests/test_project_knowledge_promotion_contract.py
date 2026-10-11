"""Regression checks for the project-knowledge promotion surface."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import library_skills_dir  # noqa: E402

HANDOFF_SKILL = library_skills_dir() / "reflective-handoff-retro" / "SKILL.md"


def test_handoff_skill_exposes_complete_promotion_candidate_contract():
    content = HANDOFF_SKILL.read_text(encoding="utf-8")

    required_fields = [
        "Candidate:",
        "Claim / Procedure:",
        "Evidence of recurrence:",
        "Destination:",
        "Authority class:",
        "Proposed action:",
        "Human approval:",
        "Source artifacts:",
        "Review / retirement trigger:",
    ]

    for field in required_fields:
        assert field in content, f"promotion contract is missing {field}"

