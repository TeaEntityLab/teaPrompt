"""Regression checks for the project-knowledge promotion surface."""

from pathlib import Path


LIBRARY_ROOT = Path(__file__).parent.parent.parent
HANDOFF_SKILL = LIBRARY_ROOT / "skills" / "reflective-handoff-retro" / "SKILL.md"
PROJECT_TEMPLATE = LIBRARY_ROOT / "06-repo" / "PROJECT_KNOWLEDGE.template.md"


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
