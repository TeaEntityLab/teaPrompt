"""Guard the Software Factory Rethink panel record (2026-09-28) at its surfaces."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
)

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "software-factory-rethink-panel-record-2026-09-28.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
WORKFLOW_RECIPES = PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-recipes.md"
EN_CHEATSHEET = cheatsheet_en_path()
ZH_CHEATSHEET = cheatsheet_zh_tw_path()

CANDIDATES = {
    "SFR-1": "Adopted 2026-09-28",
    "SFR-2": "Adopted 2026-09-28",
    "SFR-3": "Rejected 2026-09-28",
    "SFR-4": "Deferred 2026-09-28",
}

REQUIRED_HEADINGS = (
    "## Panel Consensus",
    "## Required Wording Changes",
    "## Shared Findings",
    "## Disagreements / Residual Risks",
    "## Candidate Adoption Ledger",
    "## Evidence vs Inference",
    "## Evidence Actually Checked",
    "## Falsifiability",
)

EN_CUE = "Deliver end-to-end under governance (Software Factory / AI-native SDLC)"
ZH_CUE = "在治理之下端到端交付（軟體工廠／AI 原生 SDLC）"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_record_preserves_structure_and_headings():
    text = _read(RECORD)
    assert "**Status: decided — two surfaces updated; new core skill and domain pack rejected" in text
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"panel record missing heading {heading!r}"


def test_candidate_adoption_ledger_dispositions():
    text = _read(RECORD)
    for cid, expected_status in CANDIDATES.items():
        pattern = re.compile(rf"\|\s*\*\*{cid}\*\*\s*\|[^|]*\|\s*{re.escape(expected_status)}")
        assert pattern.search(text), f"Candidate {cid} missing or status mismatch in ledger"


def test_cheatsheet_in_place_cues_present():
    en_text = _read(EN_CHEATSHEET)
    zh_text = _read(ZH_CHEATSHEET)
    assert EN_CUE in en_text, f"EN cheatsheet missing cue {EN_CUE!r}"
    assert ZH_CUE in zh_text, f"zh-TW cheatsheet missing cue {ZH_CUE!r}"


def test_workflow_recipes_contains_autonomous_software_factory():
    text = _read(WORKFLOW_RECIPES)
    assert "## Autonomous Software Factory (AI-Native SDLC)" in text
    assert "Phase 1: Intent & Specification (Outer Loop)" in text
    assert "Phase 2: Governance & Containment (Contract Boundary)" in text
    assert "Phase 3: Bounded Headless Execution (Inner Loop)" in text
    assert "Phase 4: Verification, Acceptance & Durability (Audit Loop)" in text
    # Clean-room compliance: verify the banned token 'sealed oracle' is absent
    assert not re.search(r"sealed oracle", text, re.IGNORECASE), "workflow-recipes contains banned 'sealed oracle' token"


def test_project_knowledge_decision_index_links_panel_record():
    pk = _read(PROJECT_KNOWLEDGE)
    index = pk.split("## Decision Index", 1)[1]
    assert "software-factory-rethink-panel-record-2026-09-28.md" in index
