"""Guard the DevOps and Agentic AI Architecture Trends survey record (2026-09-28)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "devops-agentic-trends-survey-2026-09-28.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

NO_CHANGE = ["DT-1", "DT-2", "DT-3", "DT-5", "DT-6", "DT-7"]
CONCEPTS = [f"C{i}" for i in range(1, 8)]
SKILL = PROMPT_LIBRARY_ROOT / "skills" / "agent-governance-scaffold" / "SKILL.md"
ADOPTED = (
    "A `delegated_to` grant is monotone non-increasing (invariant #11): "
    "`allowed_effects` and `resource_scope` are the intersection with the "
    "delegator's authority, `forbidden_effects` is the union, and the token "
    "must not grant a capability the delegator does not hold."
)

REQUIRED_HEADINGS = (
    "## Research Question",
    "## Direct Recommendation (as of 2026-09-28)",
    "## Method",
    "## Source Identity and Claim Verification",
    "## Concept Map",
    "## Candidate Adoption Ledger",
    "## Evidence vs Inference",
    "## Evidence Actually Checked",
    "## Falsifiability",
    "## Shared Findings and Architectural Synthesis",
)

KEY_CITATIONS = (
    "Why Isn't AI Adoption Showing Up in Your P&L?",
    "Faros AI",
    "Docker Cloud Sandboxes",
    "DigitalOcean Action Gateway",
    "Monotonic Delegation",
    "The AI-Native SDLC Playbook",
    "Own the Outer Loop",
    "TypeSafe AI's Jev",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_record_preserves_source_identity_and_structure():
    text = _read(RECORD)
    assert "**Status: decided — one sentence adopted" in text
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"record missing heading {heading!r}"
    for citation in KEY_CITATIONS:
        assert citation in text, f"record missing key citation {citation!r}"


def test_concept_map_covers_all_seven_concepts():
    text = _read(RECORD)
    for c in CONCEPTS:
        pattern = re.compile(rf"\|\s*{c}\s*\|")
        assert pattern.search(text), f"Concept {c} missing in Concept Map"


def test_candidate_adoption_ledger_dispositions():
    text = _read(RECORD)
    for dt in NO_CHANGE:
        pattern = re.compile(rf"\|\s*{dt}\s*\|[^|]*\|\s*No change")
        assert pattern.search(text), f"Candidate {dt} missing or not 'No change' in ledger"
    adopted = re.compile(r"\|\s*DT-4\s*\|[^|]*\|\s*Adopted 2026-09-28")
    assert adopted.search(text), "DT-4 ledger row is not the adopted sentence"


def test_monotone_delegation_sentence_is_on_the_token_block():
    text = _read(SKILL)
    token = text.split("### Authorization + capability token", 1)[1].split("### ", 1)[0]
    assert ADOPTED in token
    assert "only the broker enforces it" in token


def test_project_knowledge_decision_index_links_survey():
    pk = _read(PROJECT_KNOWLEDGE)
    index = pk.split("## Decision Index", 1)[1]
    assert "devops-agentic-trends-survey-2026-09-28.md" in index
