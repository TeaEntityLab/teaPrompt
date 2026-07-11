"""Anti-drift: all registered core and domain-pack skills keep Module Contracts."""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import library_skills_dir  # noqa: E402
from validate_skill_examples import CORE_SKILLS, DOMAIN_PACK_SKILLS  # noqa: E402

SKILLS_DIR = library_skills_dir()
REGISTERED_SKILLS = CORE_SKILLS + DOMAIN_PACK_SKILLS

REQUIRED_SUBSECTIONS = ("Trigger", "Methods", "Output", "Never", "Escalation")

ESCALATION_SKILL_PATTERN = re.compile(r"`(reflective-[a-z-]+)`")


def _module_contract_block(content: str) -> str:
    marker = "## Module Contract"
    assert marker in content
    block = content.split(marker, 1)[1]
    next_heading = re.search(r"\n## [^#]", block)
    return block[: next_heading.start()] if next_heading else block


def _escalation_section(module_contract: str) -> str:
    match = re.search(
        r"(?:##\s*Escalation|^\*?\*?Escalation:)(.*)",
        module_contract,
        re.MULTILINE | re.IGNORECASE | re.DOTALL,
    )
    assert match, "missing Escalation subsection"
    tail = match.group(1)
    next_sub = re.search(r"\n(?:##\s+\S|###\s+\S)", tail)
    return tail[: next_sub.start()] if next_sub else tail



@pytest.mark.parametrize("skill_name", REGISTERED_SKILLS)
def test_registered_skill_has_module_contract(skill_name: str):
    content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
    assert "## Module Contract" in content, skill_name


@pytest.mark.parametrize("skill_name", REGISTERED_SKILLS)
def test_registered_skill_has_contract_subsections(skill_name: str):
    content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
    for subsection in REQUIRED_SUBSECTIONS:
        pattern = rf"(##\s*{re.escape(subsection)}|^\*?\*?{re.escape(subsection)}:)"
        assert re.search(pattern, content, re.MULTILINE | re.IGNORECASE), (
            f"{skill_name} missing {subsection}"
        )

@pytest.mark.parametrize("skill_name", CORE_SKILLS)
def test_core_skill_escalation_routes_to_valid_workflow_skills(skill_name: str):
    """Escalation bullets must name frozen workflow skills, not invented routes."""
    content = (SKILLS_DIR / skill_name / "SKILL.md").read_text(encoding="utf-8")
    escalation = _escalation_section(_module_contract_block(content))
    targets = ESCALATION_SKILL_PATTERN.findall(escalation)
    if skill_name == "reflective-risk":
        assert "Human Review" in escalation, (
            f"{skill_name} Escalation should require Human Review as terminal gate"
        )
        return
    assert targets, f"{skill_name} Escalation should cite at least one workflow skill"
    invalid = sorted({t for t in targets if t not in CORE_SKILLS})
    assert not invalid, f"{skill_name} Escalation cites unknown skills: {invalid}"

