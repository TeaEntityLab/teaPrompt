"""Pytest mirrors for lint_skills.py (Round 77 anti-drift)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from lint_skills import SkillLinter  # noqa: E402
from validate_skill_examples import CORE_SKILLS  # noqa: E402

REPO_ROOT = Path(__file__).parent.parent.parent.parent


@pytest.fixture(scope="module")
def lint_results():
    return SkillLinter(str(REPO_ROOT)).lint_all()


def test_live_repo_has_no_lint_errors(lint_results):
    assert lint_results["total_errors"] == 0, [
        (item["file"], item["errors"])
        for item in lint_results["file_results"]
        if item["errors"]
    ]


def test_all_nine_core_skills_are_linted_as_skills(lint_results):
    skill_files = {
        item["file"]
        for item in lint_results["file_results"]
        if item["type"] == "skill" and item["file"].endswith("SKILL.md")
    }
    for skill in CORE_SKILLS:
        expected = f"reflective-prompt-library/skills/{skill}/SKILL.md"
        assert expected in skill_files, skill


def test_skill_missing_description_reports_error(tmp_path):
    skill_dir = tmp_path / "reflective-prompt-library" / "skills" / "reflective-brief"
    skill_dir.mkdir(parents=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(
        """---
name: reflective-brief
license: MIT
---
# Brief
""",
        encoding="utf-8",
    )
    result = SkillLinter(str(tmp_path)).lint_file(skill_file)
    assert result["type"] == "skill"
    assert any("description" in err.lower() for err in result["errors"])
