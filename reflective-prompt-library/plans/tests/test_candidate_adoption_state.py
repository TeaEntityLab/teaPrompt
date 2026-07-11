"""Guard adopted 2026-07-06 contracts at their named surfaces.

Adoption ledger: plans/workflow-possibilities-constraints-review-2026-07-06.md
(### Candidate Adoption Ledger). Review record:
plans/governance-rules-rethink-review-2026-07-11.md (tier A). Permanent checks
use structure or stable protocol tokens under GLOSSARY Adoption Guard Closure.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
    glossary_path,
    library_skills_dir,
    methodology_map_en_path,
    skill_map_path,
)
from validate_skill_examples import CORE_SKILLS  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
AGENT_LENS_DIR = PROMPT_LIBRARY_ROOT / "04-agent"

FROZEN_GLOSS = "gated, not never"
LADDER_EQUIVALENCE = "Acquisition L3 and Formalization L3"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_section() -> str:
    text = _read(PLANS_DIR / "workflow-possibilities-constraints-review-2026-07-06.md")
    marker = "### Candidate Adoption Ledger"
    assert marker in text, "adoption ledger missing from 2026-07-06 record"
    return text.split(marker, 1)[1].split("## Shared Findings", 1)[0]


# Candidate 1 — frozen gloss at high-traffic entry points.
@pytest.mark.parametrize(
    "path",
    [
        skill_map_path(),
        methodology_map_en_path(),
        library_skills_dir() / "reflective-dispatch" / "SKILL.md",
        PROMPT_LIBRARY_ROOT / "06-repo" / "AGENTS.md",
    ],
    ids=["skill-map", "methodology-map", "dispatch-skill", "repo-agents"],
)
def test_candidate1_bounded_core_gloss_present(path: Path):
    text = _read(path)
    assert len(CORE_SKILLS) == 9
    assert FROZEN_GLOSS in text


# Candidate 2 — Acquisition ladder disambiguated; no fourth L-ladder.
@pytest.mark.parametrize(
    "path",
    [glossary_path(), methodology_map_en_path()],
    ids=["glossary", "methodology-map"],
)
def test_candidate2_acquisition_ladder_note(path: Path):
    text = _read(path)
    assert LADDER_EQUIVALENCE in text
    assert "fourth L-ladder" in text


# Candidate 3 — L3 verifier route surfaced (adopted half) + deferral recorded.
def test_candidate3_dispatch_route_row():
    text = _read(library_skills_dir() / "reflective-dispatch" / "SKILL.md")
    assert "verifier/test artifact" in text


@pytest.mark.parametrize(
    "path",
    [cheatsheet_en_path(), cheatsheet_zh_tw_path()],
    ids=["cheatsheet-en", "cheatsheet-zh-tw"],
)
def test_candidate3_cheatsheet_quick_cue(path: Path):
    text = _read(path)
    assert "`verifier/test` artifact" in text
    assert "Acquisition L3" in text


def test_candidate3_recipes_note_present():
    text = _read(AGENT_LENS_DIR / "workflow-recipes.md")
    assert "`verifier/test` artifact" in text
    assert "Acquisition L3" in text


def test_candidate3_ledger_row_adopted():
    ledger = _ledger_section()
    row = next(line for line in ledger.splitlines() if line.startswith("| 3 |"))
    assert "Adopted" in row


# Candidate 4 — fail-closed security gates at Acquisition L3.
def test_candidate4_artifact_promotion_gates():
    text = _read(AGENT_LENS_DIR / "artifact-promotion.md")
    assert "fails closed" in text
    assert "prompt-injection" in text
    assert "Memory writes" in text


def test_candidate4_acquisition_l3_row_gates():
    text = _read(AGENT_LENS_DIR / "workflow-acquisition.md")
    assert "fail closed" in text
    assert "memory-write provenance" in text


# Candidate 5 — evidence tiers at the governance layer.
def test_candidate5_glossary_evidence_tier_section():
    text = _read(glossary_path())
    assert "## Evidence Tier" in text
    assert "advisory evidence" in text
    assert "regression guards" in text


def test_candidate5_quality_gates_tier_note():
    text = _read(PLANS_DIR / "QUALITY_GATES_SUMMARY.md")
    assert "regression-guard tier" in text
    assert "advisory/model-vote tier" in text


# Ledger presence and shape.
def test_ledger_has_five_candidate_rows():
    ledger = _ledger_section()
    for candidate_id in ("| 1 |", "| 2 |", "| 3 |", "| 4 |", "| 5 |"):
        assert candidate_id in ledger, f"ledger missing row {candidate_id!r}"


def _necessity_ledger_section() -> str:
    record = _read(PLANS_DIR / "governance-necessity-panel-record-2026-07-11.md")
    return record.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Falsifiability audit",
        1,
    )[0]


def test_governance_necessity_ledger_records_exact_dispositions():
    ledger = _necessity_ledger_section()
    for candidate_id in ("N2", "N3", "N4", "N5", "N6", "N7", "N9", "N10"):
        row = next(line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |"))
        assert "Adopted 2026-07-11" in row

    rejected = next(line for line in ledger.splitlines() if line.startswith("| N8 |"))
    assert "Rejected" in rejected
    for candidate_id in ("N11", "N12"):
        row = next(line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |"))
        assert "Deferred" in row
    no_mass_edit = next(line for line in ledger.splitlines() if line.startswith("| N13 |"))
    assert "No mass edit" in no_mass_edit


def test_governance_necessity_authority_surfaces_are_structural():
    agents = _read(PROMPT_LIBRARY_ROOT / "06-repo" / "AGENTS.md")
    policy = agents.split("## Harness Policy", 1)[1].split("\n---", 1)[0]
    for token in (
        "DOMAIN_PACK_SKILLS",
        "not selectable by",
        "recurrence evidence stays `unknown`",
        "Adoption Guard Closure",
    ):
        assert token in policy

    glossary = _read(glossary_path())
    assert "## Adoption Guard Closure" in glossary
    pk = _read(PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md")
    assert "Governance necessity consensus" in pk
    assert "plans/governance-necessity-panel-record-2026-07-11.md" in pk
