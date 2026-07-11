"""Guard adopted flow-pack contracts at their named surfaces.

Mirrors test_candidate_adoption_state.py: adopted ledger rows (P8-P15 in
plans/agent-flow-control-research-2026-07-11.md) get structural, executable-
symbol, or stable-protocol checks. Deferred rows are guarded only for ledger
presence, never content, per GLOSSARY Adoption Guard Closure.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))


from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
GENERATOR = library_skills_dir() / "flow-control-generator" / "SKILL.md"
HARNESS = library_skills_dir() / "flow-loop-harness" / "SKILL.md"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


# P8 - methodology/operationalization boundary in both Purposes.
@pytest.mark.parametrize("path", [GENERATOR, HARNESS])
def test_p8_methodology_boundary_in_purpose(path: Path):
    text = _read(path)
    purpose = text.split("## Purpose", 1)[1].split("\n## ", 1)[0].lower()
    assert "methodology" in purpose and "operational" in purpose
    assert "external-adoption-case-studies-2026-06-20.md" in purpose


# P8 - demotion triggers section in both skills.
@pytest.mark.parametrize("path", [GENERATOR, HARNESS])
def test_p8_demotion_triggers_section(path: Path):
    assert "## Demotion Triggers" in _read(path)


# P8 - run state is not project memory (harness Never).
def test_p8_run_state_not_project_memory():
    text = _read(HARNESS)
    never = text.split("Never:", 1)[1].split("Escalation:", 1)[0].lower()
    assert "run state" in never and "project memory" in never
    assert "reflective-handoff-retro" in never


# P9 - parallel quorum gate is an explicit policy.
def test_p9_parallel_quorum_gate():
    text = _read(GENERATOR)
    assert "MIN_OK" in text
    assert "quorum" in text


# P10 - router route-trace observability.
def test_p10_router_route_trace():
    text = _read(GENERATOR)
    assert "route-trace" in text
    assert "default-up" in text


# P11 - loop restart stanza.
def test_p11_resumed_stanza():
    text = _read(HARNESS)
    assert "RESUMED" in text


# Ledger presence and shape: coverage rows exist next to the original P1-P7.
def test_ledger_has_coverage_rows():
    ledger = _read(PLANS_DIR / "agent-flow-control-research-2026-07-11.md")
    for row in ("| P8 |", "| P9 |", "| P10 |", "| P11 |", "| P12 |", "| P13 |", "| P14 |", "| P15 |"):
        assert row in ledger, f"ledger missing row {row!r}"


# Panel record exists with the protocol's required sections.
def test_coverage_panel_record_shape():
    text = _read(PLANS_DIR / "flow-coverage-panel-record-2026-07-11.md")
    for heading in (
        "## Panel Consensus",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
    ):
        assert heading in text, f"panel record missing {heading!r}"
