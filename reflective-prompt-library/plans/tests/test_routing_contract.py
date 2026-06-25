"""Structural anti-drift tests for ROUTING_CONTRACT.md."""

from pathlib import Path

import pytest

CONTRACT_PATH = Path(__file__).parent.parent / "ROUTING_CONTRACT.md"

REQUIRED_RULES = (
    "### R8: Holdout-before-tune",
    "### R9: Production-negation and plan-only boundaries",
    "### R10: Brief-before-plan",
    "### R11: Approved-spec delivery",
    "### R12: Boundary quick-cue summary",
)


@pytest.fixture(scope="module")
def contract_text() -> str:
    assert CONTRACT_PATH.is_file(), f"missing {CONTRACT_PATH}"
    return CONTRACT_PATH.read_text(encoding="utf-8")


def test_routing_boundary_rules_present(contract_text: str):
    for heading in REQUIRED_RULES:
        assert heading in contract_text, f"missing routing contract section: {heading}"


def test_r12_mentions_cheatsheet_parity_tests(contract_text: str):
    start = contract_text.index("### R12: Boundary quick-cue summary")
    end = contract_text.index("## Router Output Contract", start)
    section = contract_text[start:end]
    assert "test_cheatsheet_boundary_quick_cues.py" in section
    assert "test_cheatsheet_*_parity.py" in section


def test_related_artifacts_include_cheatsheets_and_parity_tests(contract_text: str):
    section = contract_text.split("## Related Artifacts", 1)[1]
    assert "SKILL_TRIGGER_CHEATSHEET.zh-TW.md" in section
    assert "test_cheatsheet_boundary_quick_cues.py" in section
    assert "test_cheatsheet_*_parity.py" in section
    assert "route-002-holdout-eval.yaml" in section
    assert "route-003-adversarial-eval.yaml" in section
