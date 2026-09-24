"""Tests for skill example validation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import validate_skill_examples  # noqa: E402
from validate_skill_examples import (  # noqa: E402
    CORE_SKILLS,
    DOMAIN_PACK_SKILLS,
    MIN_EXAMPLE_CHARS,
)


def test_core_skill_list_is_nine():
    assert len(CORE_SKILLS) == 9


def test_every_registered_skill_has_example_file():
    repo_root = Path(__file__).parent.parent.parent.parent
    examples_dir = repo_root / "reflective-prompt-library" / "skills" / "examples"
    for skill in CORE_SKILLS + DOMAIN_PACK_SKILLS:
        path = examples_dir / f"{skill}.examples.md"
        assert path.is_file(), skill
        assert len(path.read_text(encoding="utf-8").strip()) >= MIN_EXAMPLE_CHARS, skill


def test_every_registered_skill_points_to_installed_example_path():
    repo_root = Path(__file__).parent.parent.parent.parent
    skills_dir = repo_root / "reflective-prompt-library" / "skills"
    for skill in CORE_SKILLS + DOMAIN_PACK_SKILLS:
        skill_file = skills_dir / skill / "SKILL.md"
        pointer = f"<skills-root>/examples/{skill}.examples.md"
        assert pointer in skill_file.read_text(encoding="utf-8"), skill



def test_validator_fails_when_core_registry_shrinks(monkeypatch, capsys):
    # Every remaining entry still has its files, so only the cardinality
    # self-check can catch the dropped skill (the 2026-09-23 seeded-bug arm).
    monkeypatch.setattr(validate_skill_examples, "CORE_SKILLS", CORE_SKILLS[:-1])
    assert validate_skill_examples.main() == 1
    assert "CORE_SKILLS has 8 entries, expected 9" in capsys.readouterr().out


def test_validator_fails_on_duplicate_core_entry(monkeypatch, capsys):
    monkeypatch.setattr(
        validate_skill_examples, "CORE_SKILLS", CORE_SKILLS[:-1] + CORE_SKILLS[:1]
    )
    assert validate_skill_examples.main() == 1
    assert "CORE_SKILLS contains duplicates" in capsys.readouterr().out


def test_validator_fails_when_pack_registry_shrinks(monkeypatch, capsys):
    monkeypatch.setattr(
        validate_skill_examples, "DOMAIN_PACK_SKILLS", DOMAIN_PACK_SKILLS[:-1]
    )
    assert validate_skill_examples.main() == 1
    assert "DOMAIN_PACK_SKILLS has 4 entries, expected 5" in capsys.readouterr().out
