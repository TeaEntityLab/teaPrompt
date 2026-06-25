"""Regression checks for the project-knowledge promotion surface."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    category_prompt_dir,
    library_skills_dir,
)

HANDOFF_SKILL = library_skills_dir() / "reflective-handoff-retro" / "SKILL.md"
PROJECT_TEMPLATE = category_prompt_dir("06-repo") / "PROJECT_KNOWLEDGE.template.md"


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

    assert "project-local skill" in content
    assert "human confirmation" in content


def test_reusable_template_declares_non_authoritative_boundary():
    content = PROJECT_TEMPLATE.read_text(encoding="utf-8")

    assert "NON-AUTHORITATIVE" in content
    assert "AGENTS.md" in content
    assert "SKILL.md" in content
    assert "project-local skill" in content
