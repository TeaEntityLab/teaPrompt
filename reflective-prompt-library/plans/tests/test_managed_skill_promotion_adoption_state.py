"""Guard: 2026-07-11 managed-skill promotion panel adoptions stay adopted at their named surfaces.

Mirrors test_candidate_adoption_state.py / test_flow_pack_adoption_state.py:
adopted ledger rows (M1-M2 in plans/managed-skill-promotion-panel-record-2026-07-11.md)
get structural checks at their named surfaces; deferred rows (M4/M6/M7) are guarded
for ledger presence only, never content. D1 discipline: headings, tokens, and link
targets - not paragraph pins.
"""

from pathlib import Path

import pytest

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
AGENT_LENS_DIR = PROMPT_LIBRARY_ROOT / "04-agent"
RECIPES = AGENT_LENS_DIR / "workflow-recipes.md"
PROMOTION = AGENT_LENS_DIR / "artifact-promotion.md"
RECORD = PLANS_DIR / "managed-skill-promotion-panel-record-2026-07-11.md"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _plr_section() -> str:
    text = _read(RECIPES)
    marker = "## Parallel Lens Review"
    assert marker in text
    return text.split(marker, 1)[1].split("## Cost Modes", 1)[0]


# M1 - packet and verdict contract subsection inside the recipe section.
def test_m1_packet_contract_subsection_present():
    section = _plr_section()
    assert "### Packet and verdict contract" in section


def test_m1_verdict_vocabulary_present():
    section = _plr_section()
    for token in ("`AGREE`", "`AGREE WITH CHANGES`", "`DISAGREE`"):
        assert token in section, f"verdict token {token} missing"


def test_m1_anti_persona_rule_present():
    section = _plr_section()
    assert "never claim named provider models" in section


def test_m1_ledger_requirement_present():
    section = _plr_section()
    assert "Candidate Adoption Ledger" in section


def test_m1_provenance_and_host_wrapper_quarantine():
    section = _plr_section()
    assert "managed skill" in section  # provenance names the memory-derived source
    assert "host-provided wrappers" in section.lower() or "host-provided wrapper" in section.lower()


def test_m1_packet_path_correction():
    # The misleading host-only local:// example was replaced with a repo-readable path.
    section = _plr_section()
    assert "repo-readable path" in section


# M2 - memory-derived-source rule under Evidence rules.
def test_m2_memory_derived_source_rule():
    text = _read(PROMOTION)
    assert "Evidence rules:" in text
    rules = text.split("Evidence rules:", 1)[1].split("## 3.", 1)[0]
    assert "managed skills" in rules
    assert "memory-write gate" in rules


# Ledger presence and shape.
def test_ledger_has_all_rows():
    record = _read(RECORD)
    for row in ("| M1 |", "| M2 |", "| M3 |", "| M4 |", "| M5 |", "| M6 |", "| M7 |", "| M8 |"):
        assert row in record, f"ledger missing row {row!r}"


def test_record_shape():
    record = _read(RECORD)
    for heading in (
        "## Panel Consensus",
        "## Candidate Adoption Ledger",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
    ):
        assert heading in record, f"panel record missing {heading!r}"


# Decision Index rollup line exists and links the record.
def test_decision_index_line():
    pk = _read(PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md")
    assert "Managed-skill promotion review" in pk
    assert "plans/managed-skill-promotion-panel-record-2026-07-11.md" in pk
