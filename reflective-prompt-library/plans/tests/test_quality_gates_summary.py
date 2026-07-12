"""Structural anti-drift tests for QUALITY_GATES_SUMMARY.md."""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_benchmark_fixture import MIN_TASK_COUNT  # noqa: E402
from validate_route_fixture import (  # noqa: E402
    ROUTE_001_MIN_PHRASES,
    ROUTE_002_MIN_HOLDOUT_GROUPS,
    ROUTE_002_MIN_PHRASES,
    ROUTE_003_MIN_ADVERSARIAL_GROUPS,
    ROUTE_003_MIN_PHRASES,
)
from prompt_eval_helpers import library_skills_dir  # noqa: E402
from validate_skill_examples import CORE_SKILLS, DOMAIN_PACK_SKILLS  # noqa: E402

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


def test_holdout_tracking_paragraph_matches_fixture_minimums(summary_text: str):
    section = _section_between(
        summary_text, "### Holdout Tracking", "## Phase 2 Status (post-Round 68 maintenance)"
    )
    assert f"{ROUTE_002_MIN_PHRASES} ROUTE-002 phrases" in section
    assert (
        f"{ROUTE_003_MIN_ADVERSARIAL_GROUPS} ROUTE-003 adversarial groups / "
        f"{ROUTE_003_MIN_PHRASES} phrases"
    ) in section
    assert "approved_spec_plan_not_implement_trap" in section
    assert "dispatch_meta_skill_trap" in section
    assert "minimality_not_implement_trap" in section
    assert "100 phrases" not in section


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

def test_research_alignment_lists_nine_frozen_skills(summary_text: str):
    section = _section_between(summary_text, "## Research Alignment", "## Key Metrics")
    assert "nine frozen workflow skills" in section
    assert "8 lifecycle skills" not in section
    # Wording must match reality: nine frozen core contracts on disk, plus
    # registered domain packs only (Option B, 2026-07-11 flow-control panel).
    on_disk = {p.parent.name for p in library_skills_dir().glob("*/SKILL.md")}
    assert on_disk == set(CORE_SKILLS) | set(DOMAIN_PACK_SKILLS)
    assert len(CORE_SKILLS) == 9

def test_benchmark_section_covers_nine_workflows(summary_text: str):
    section = summary_text.split("### 7. Small Benchmark Set", 1)[1].split("## Research Alignment", 1)[0]
    assert "nine frozen workflow skills" in section
    assert "8 different skills" not in section
    assert "24 golden tasks" in section or "24 benchmark tasks" in section
    on_disk = {p.parent.name for p in library_skills_dir().glob("*/SKILL.md")}
    assert on_disk == set(CORE_SKILLS) | set(DOMAIN_PACK_SKILLS)
    assert len(CORE_SKILLS) == 9



def _pytest_item_count() -> int:
    import subprocess

    result = subprocess.run(
        ["python3", "-m", "pytest", str(Path(__file__).parent), "--collect-only", "-q"],
        capture_output=True,
        text=True,
        check=True,
    )
    for line in reversed(result.stdout.splitlines()):
        if " tests collected" in line:
            return int(line.split()[0])
    raise AssertionError("could not determine pytest collection count")


def test_key_metrics_benchmark_task_count_matches_fixture(summary_text: str):
    metrics = _section_between(summary_text, "## Key Metrics", "### Routing Consistency Tracking")
    assert f"| Benchmark tasks | {MIN_TASK_COUNT} |" in metrics

def test_phase2_pytest_floor_matches_collection(summary_text: str):
    """Anti-drift: Phase 2 Done bullet must not under-report collected pytest count."""
    collected = _pytest_item_count()
    match = re.search(r"(\d+)\+ pytest anti-drift suite in CI", summary_text)
    assert match, "missing pytest floor in Phase 2 Done bullet"
    documented = int(match.group(1))
    assert documented <= collected, (
        f"QUALITY_GATES documents {documented}+ pytest but {collected} collected"
    )
    assert documented >= collected - 20, (
        f"QUALITY_GATES pytest floor {documented} is stale vs {collected} collected"
    )
