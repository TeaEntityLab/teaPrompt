"""Anti-drift: all nine workflow skills keep Module Contract subsections."""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_skill_examples import CORE_SKILLS  # noqa: E402

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

REQUIRED_SUBSECTIONS = ("Trigger", "Methods", "Output", "Never", "Escalation")


@pytest.mark.parametrize("skill_name", CORE_SKILLS)
def test_core_skill_has_module_contract(skill_name: str):
    content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
    assert "## Module Contract" in content, skill_name


@pytest.mark.parametrize("skill_name", CORE_SKILLS)
def test_core_skill_has_contract_subsections(skill_name: str):
    content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
    for subsection in REQUIRED_SUBSECTIONS:
        pattern = rf"(##\s*{re.escape(subsection)}|^\*?\*?{re.escape(subsection)}:)"
        assert re.search(pattern, content, re.MULTILINE | re.IGNORECASE), (
            f"{skill_name} missing {subsection}"
        )
