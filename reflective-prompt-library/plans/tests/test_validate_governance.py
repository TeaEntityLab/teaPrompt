"""Pytest mirrors for validate_governance.py (Round 77 anti-drift)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_governance import CANONICAL_CONTEXT_LOAD, GovernanceValidator  # noqa: E402
from validate_skill_examples import CORE_SKILLS, DOMAIN_PACK_SKILLS  # noqa: E402

REPO_ROOT = Path(__file__).parent.parent.parent.parent


@pytest.fixture(scope="module")
def governance_results():
    return GovernanceValidator(str(REPO_ROOT)).validate_all()


def test_canonical_context_load_matches_core_skills():
    assert set(CANONICAL_CONTEXT_LOAD) == set(CORE_SKILLS)
    assert len(CANONICAL_CONTEXT_LOAD) == 9


def test_all_skills_pass_governance_validation(governance_results):
    assert governance_results["total_skills"] == len(CORE_SKILLS) + len(DOMAIN_PACK_SKILLS)
    assert len(CORE_SKILLS) == 9
    assert governance_results["invalid_skills"] == 0, governance_results["errors"]


def test_unregistered_skill_directory_fails_validation(tmp_path):
    """Option B guard: a SKILL.md outside CORE+DOMAIN_PACK registries is an error."""
    skills_dir = tmp_path / "reflective-prompt-library" / "skills" / "rogue-skill"
    skills_dir.mkdir(parents=True)
    skills_dir.joinpath("SKILL.md").write_text(
        """---
name: rogue-skill
description: test
risk_level: low
human_review_required: false
external_io: false
context_load: low
---
# Test
""",
        encoding="utf-8",
    )
    results = GovernanceValidator(str(tmp_path)).validate_all()
    assert any(
        "Unregistered skill directory" in err
        for item in results["errors"]
        for err in item["errors"]
    )


@pytest.mark.parametrize("skill,expected_load", sorted(CANONICAL_CONTEXT_LOAD.items()))
def test_live_skill_context_load_matches_panel_table(skill, expected_load):
    skill_path = (
        REPO_ROOT / "reflective-prompt-library" / "skills" / skill / "SKILL.md"
    )
    validator = GovernanceValidator(str(REPO_ROOT))
    frontmatter = validator.extract_frontmatter(skill_path.read_text(encoding="utf-8"))
    assert frontmatter.get("context_load", "").lower() == expected_load


def test_wrong_context_load_fails_validation(tmp_path):
    skills_dir = tmp_path / "reflective-prompt-library" / "skills" / "reflective-dispatch"
    skills_dir.mkdir(parents=True)
    skills_dir.joinpath("SKILL.md").write_text(
        """---
name: reflective-dispatch
description: test
risk_level: low
human_review_required: false
external_io: false
context_load: high
---
# Test
""",
        encoding="utf-8",
    )
    results = GovernanceValidator(str(tmp_path)).validate_all()
    assert results["invalid_skills"] == 1
    assert any(
        "context_load must be 'low'" in err
        for item in results["errors"]
        for err in item["errors"]
    )


def test_missing_governance_field_fails_validation(tmp_path):
    skills_dir = tmp_path / "reflective-prompt-library" / "skills" / "reflective-brief"
    skills_dir.mkdir(parents=True)
    skills_dir.joinpath("SKILL.md").write_text(
        """---
name: reflective-brief
description: test
---
# Test
""",
        encoding="utf-8",
    )
    results = GovernanceValidator(str(tmp_path)).validate_all()
    assert results["invalid_skills"] == 1
    assert any(
        "Missing required field" in err
        for item in results["errors"]
        for err in item["errors"]
    )
