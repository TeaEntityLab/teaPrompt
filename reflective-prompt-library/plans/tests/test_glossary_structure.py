"""Anti-drift checks for GLOSSARY.md structure and round references."""

from pathlib import Path
import re

import pytest

GLOSSARY = Path(__file__).parent.parent.parent / "GLOSSARY.md"


@pytest.fixture(scope="module")
def glossary_text() -> str:
    assert GLOSSARY.is_file(), f"missing {GLOSSARY}"
    return GLOSSARY.read_text(encoding="utf-8")


def test_no_duplicate_section_separators(glossary_text: str):
    """Adjacent --- blocks indicate accidental merge/corruption."""
    assert "\n---\n\n\n---\n" not in glossary_text


def test_round_boundary_terms_present(glossary_text: str):
    required = (
        "## Brief-before-Plan",
        "## Approved-Spec Delivery",
        "## Boundary Quick Cues",
        "## Governance Maintenance Playbook",
    )
    for heading in required:
        assert heading in glossary_text, f"missing glossary section: {heading}"


def test_maintenance_playbook_references_round_99(glossary_text: str):
    playbook = glossary_text.split("## Governance Maintenance Playbook", 1)[1]
    assert "Rounds 1–99" in playbook
    assert "Rounds 1–98" not in playbook and "Rounds 1-91" not in playbook




def test_maintenance_playbook_steps_on_separate_lines(glossary_text: str):
    """Numbered playbook steps must not merge onto one line (Round 86 corruption guard)."""
    playbook = glossary_text.split("## Governance Maintenance Playbook", 1)[1]
    assert re.search(r"guards\.\d+\.", playbook) is None, (
        "playbook steps merged without newline between numbers"
    )
    for step in ("17.", "18.", "19.", "20.", "21.", "22.", "23.", "24.", "25.", "26.", "27.", "28.", "29.", "30.", "31."):
        assert step in playbook




def test_maintenance_playbook_mentions_benchmark_nine_skill_coverage(glossary_text: str):
    playbook = glossary_text.split("## Governance Maintenance Playbook", 1)[1]
    assert "test_benchmark_covers_all_nine_workflows" in playbook
    assert "MIN_TASK_COUNT" in playbook


def test_maintenance_playbook_mentions_cheatsheet_probe_parity_tests(glossary_text: str):
    playbook = glossary_text.split("## Governance Maintenance Playbook", 1)[1]
    assert "test_validate_route_fixture.py" in playbook
    assert "test_cheatsheet_" in playbook and "_parity.py" in playbook
    assert "test_cheatsheet_dispatch_meta_parity.py" in playbook


def test_approved_spec_delivery_separated_from_playbook(glossary_text: str):
    """Playbook must not run into Approved-Spec without a separator."""
    pattern = re.compile(
        r"routes to spec-plan\.\n\n## Governance Maintenance Playbook",
        re.MULTILINE,
    )
    assert not pattern.search(glossary_text), (
        "missing --- between Approved-Spec Delivery and Governance Maintenance Playbook"
    )
