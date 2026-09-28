"""Guard the Autonomous Software Factory SDLC survey record (2026-09-28)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "software-factory-sdlc-inner-outer-loop-survey-2026-09-28.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

CANDIDATES = [f"SF-{i}" for i in range(1, 7)]
CONCEPTS = [f"SF-C{i}" for i in range(1, 7)]

REQUIRED_HEADINGS = (
    "## Research Question & Core Objective",
    "## Direct Recommendation (as of 2026-09-28)",
    "## Executive Architectural Blueprint: The 5-Layer Software Factory",
    "## Method & Evidence Actually Checked",
    "## Detailed Findings Across the Three Parallel Lenses",
    "## Concept Map",
    "## Candidate Adoption Ledger",
    "## Evidence vs Inference",
    "## Falsifiability",
    "## Canonical Contract Artifact Blueprints",
    "## Architectural Synthesis",
)

KEY_CITATIONS = (
    "AI-Native SDLC Playbook",
    "Louis Claxton",
    "Own the Outer Loop",
    "Addy Osmani",
    "Faros AI",
    "The Inner Loop is Eating the Outer Loop",
    "criteria.yaml",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_record_preserves_source_identity_and_structure():
    text = _read(RECORD)
    assert "**Status: decided — record-only" in text
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"record missing heading {heading!r}"
    for citation in KEY_CITATIONS:
        assert citation in text, f"record missing key citation {citation!r}"


def test_concept_map_covers_all_six_concepts():
    text = _read(RECORD)
    for c in CONCEPTS:
        pattern = re.compile(rf"\|\s*\*\*{c}\*\*")
        assert pattern.search(text), f"Concept {c} missing in Concept Map"


def test_candidate_adoption_ledger_covers_all_candidates_as_no_change():
    text = _read(RECORD)
    for sf in CANDIDATES:
        pattern = re.compile(rf"\|\s*\*\*{sf}\*\*\s*\|[^|]*\|\s*No change")
        assert pattern.search(text), f"Candidate {sf} missing or not 'No change' in ledger"


def test_project_knowledge_decision_index_links_survey():
    pk = _read(PROJECT_KNOWLEDGE)
    index = pk.split("## Decision Index", 1)[1]
    assert "software-factory-sdlc-inner-outer-loop-survey-2026-09-28.md" in index
