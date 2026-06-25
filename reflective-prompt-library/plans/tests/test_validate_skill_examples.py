"""Tests for skill example validation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_skill_examples import CORE_SKILLS, MIN_EXAMPLE_CHARS  # noqa: E402


def test_core_skill_list_is_nine():
    assert len(CORE_SKILLS) == 9


def test_every_core_skill_has_example_file():
    repo_root = Path(__file__).parent.parent.parent.parent
    examples_dir = repo_root / "reflective-prompt-library" / "skills" / "examples"
    for skill in CORE_SKILLS:
        path = examples_dir / f"{skill}.examples.md"
        assert path.is_file(), skill
        assert len(path.read_text(encoding="utf-8").strip()) >= MIN_EXAMPLE_CHARS, skill
