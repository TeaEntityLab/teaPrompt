"""Structural anti-drift tests for QUALITY_GATES_SUMMARY.md."""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_route_fixture import (  # noqa: E402
    ROUTE_001_MIN_PHRASES,
    ROUTE_002_MIN_HOLDOUT_GROUPS,
    ROUTE_002_MIN_PHRASES,
    ROUTE_003_MIN_ADVERSARIAL_GROUPS,
    ROUTE_003_MIN_PHRASES,
)

SUMMARY_PATH = Path(__file__).parent.parent / "QUALITY_GATES_SUMMARY.md"


@pytest.fixture(scope="module")
def summary_text() -> str:
    assert SUMMARY_PATH.is_file(), f"missing {SUMMARY_PATH}"
    return SUMMARY_PATH.read_text(encoding="utf-8")


def _section_between(text: str, start_heading: str, end_heading: str) -> str:
    start = text.index(start_heading)
    end = text.index(end_heading, start + len(start_heading))
    return text[start:end]


def test_route_eval_sections_are_not_collapsed(summary_text: str):
    """Round-22 regression: 7.3 and 7.4 must not share one heading line."""
    for line in summary_text.splitlines():
        if "### 7.3" in line:
            assert "### 7.4" not in line, "collapsed ROUTE-003 and fixture-gate headings"


def test_route_003_section_structure(summary_text: str):
    section = _section_between(
        summary_text,
        "### 7.3 ROUTE-003 Adversarial Eval ✅",
        "### 7.4 Route Fixture Gate ✅",
    )
    assert "route-003-adversarial-eval.yaml" in section
    assert "**Results:**" in section
    assert "**Usage:**" in section
    assert f"{ROUTE_003_MIN_ADVERSARIAL_GROUPS} adversarial groups" in section
    assert f"{ROUTE_003_MIN_PHRASES} paraphrases" in section
    assert "implement_not_plan_trap" in section or "R11" in section


def test_route_fixture_gate_section_structure(summary_text: str):
    section = _section_between(
        summary_text,
        "### 7.4 Route Fixture Gate ✅",
        "### 7. Small Benchmark Set ✅",
    )
    assert "validate_route_fixture.py" in section
    assert "**What it does:**" in section
    assert "**Usage:**" in section
    assert str(ROUTE_002_MIN_HOLDOUT_GROUPS) in section
    assert str(ROUTE_002_MIN_PHRASES) in section
    assert str(ROUTE_003_MIN_ADVERSARIAL_GROUPS) in section
    assert str(ROUTE_003_MIN_PHRASES) in section


def test_key_metrics_table_matches_fixture_minimums(summary_text: str):
    metrics = _section_between(summary_text, "## Key Metrics", "### Routing Consistency Tracking")
    assert re.search(
        rf"ROUTE-002 \({ROUTE_002_MIN_HOLDOUT_GROUPS} groups, {ROUTE_002_MIN_PHRASES} paraphrases\)",
        metrics,
    )
    assert re.search(
        rf"ROUTE-003 \({ROUTE_003_MIN_ADVERSARIAL_GROUPS} groups, {ROUTE_003_MIN_PHRASES} paraphrases\)",
        metrics,
    )


def test_ci_paraphrase_totals_match_route_minimums(summary_text: str):
    expected_total = (
        f"{ROUTE_001_MIN_PHRASES} + {ROUTE_002_MIN_PHRASES} + {ROUTE_003_MIN_PHRASES}"
    )
    assert expected_total in summary_text

def test_route_fixture_gate_mentions_cheatsheet_parity_tests(summary_text: str):
    section = _section_between(
        summary_text,
        "### 7.4 Route Fixture Gate ✅",
        "### 7. Small Benchmark Set ✅",
    )
    assert "test_cheatsheet_boundary_quick_cues.py" in section
    assert "test_cheatsheet_" in section and "_parity.py" in section

def test_phase2_status_references_post_round_68_maintenance(summary_text: str):
    assert "## Phase 2 Status (post-Round 68 maintenance)" in summary_text
    assert "Round 21 audit" not in summary_text
    assert "test_readme_governance.py" in summary_text

