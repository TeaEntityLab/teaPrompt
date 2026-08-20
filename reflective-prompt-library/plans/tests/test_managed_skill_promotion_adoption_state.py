"""Guard managed-skill promotions and their named canonical surfaces.

The 2026-07-11 M1-M2 panel adoptions stay structurally pinned. The 2026-08-20
cross-survey method repairs extend the same packet/adoption contract without
adding a test item or changing any deferred 3XA/JS/CR candidate status.
D1 discipline: headings, tokens, and link targets, not paragraph pins.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))


from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
AGENT_LENS_DIR = PROMPT_LIBRARY_ROOT / "04-agent"
RECIPES = AGENT_LENS_DIR / "workflow-recipes.md"
PROMOTION = AGENT_LENS_DIR / "artifact-promotion.md"
RECORD = PLANS_DIR / "managed-skill-promotion-panel-record-2026-07-11.md"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_row(text: str, candidate_id: str) -> str:
    prefix = f"| {candidate_id} |"
    return next(line for line in text.splitlines() if line.startswith(prefix))


def _plr_section() -> str:
    text = _read(RECIPES)
    marker = "## Parallel Lens Review"
    assert marker in text
    return text.split(marker, 1)[1].split("## Cost Modes", 1)[0]


# M1 - packet and verdict contract subsection inside the recipe section.
def test_m1_packet_contract_and_cross_survey_method_repairs_present():
    section = _plr_section()
    research = _read(
        PROMPT_LIBRARY_ROOT / "skills" / "reflective-research" / "SKILL.md"
    )
    adoption = _read(AGENT_LENS_DIR / "external-adoption-review.md")
    record = _read(
        PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
    )
    knowledge = _read(PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md")

    assert "### Packet and verdict contract" in section
    for token in (
        "label-to-revision split",
        "schema-failed output is not a lens verdict",
        "never infer its terminal verdict",
    ):
        assert token in section, f"workflow-recipes lost {token!r}"

    for token in (
        "exact commit or artifact digest",
        "repository-owned self-tests and green CI",
        "parent symlinks/junctions",
        "per-install ownership receipts",
        "concurrent-write behavior",
    ):
        assert token in research, f"reflective-research lost {token!r}"

    for token in (
        "exact commit or artifact digest",
        "| Repository self-test / CI passes | no, alone |",
        "parent symlinks/junctions",
        "per-install ownership receipts",
        "concurrent writers",
    ):
        assert token in adoption, f"external-adoption-review lost {token!r}"

    for candidate_id in ("XM-1", "XM-2", "XM-3", "XM-4", "XM-5"):
        assert f"| {candidate_id} |" in record
    assert "test_managed_skill_promotion_adoption_state.py" in record
    assert "Cross-survey external-adoption method repair" in knowledge

    survey_expectations = {
        "3xa-harness-survey-2026-08-20.md": (
            ("3XA-1", "Deferred / study-only"),
            ("3XA-4", "Rejected"),
        ),
        "jspace-cognition-survey-2026-08-20.md": (
            ("JS-1", "Deferred / study-only"),
            ("JS-5", "Rejected"),
        ),
        "code-recall-survey-2026-08-20.md": (
            ("CR-1", "Deferred / study-only"),
            ("CR-5", "Rejected"),
        ),
    }
    for filename, expected_rows in survey_expectations.items():
        survey = _read(PLANS_DIR / filename)
        assert "No candidate created or changed a TeaPrompt skill" in survey
        for candidate_id, expected_status in expected_rows:
            assert expected_status in _ledger_row(survey, candidate_id)


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
