"""Guard the 2026-09-10 context-efficiency instruction-profile survey.

Record-only outcome: nothing adopted on any installed surface. The guard pins
the record's identity and dispositions, keeps the two reserved wordings
record-only, and scans a wider surface set than the precedent foreign-token
guards (GLOSSARY and 04-agent were the candidate surfaces this survey named).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "astra-efficiency-rules-survey-2026-09-10.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
AGENT_DOCS = PROMPT_LIBRARY_ROOT / "04-agent"

REPO_REVISION = "5576ceb931c91cc14c19dd4f6a6358996e793f20"
# Surveyed-project vocabulary and the profile's fixed caps: never on a durable surface.
SURVEY_TOKENS = re.compile(r"\bAstra\b|ASTRA_RULES|astra-efficiency-rules|\bsh58702e\b|5576ceb")
CAP_LITERALS = re.compile(r"12,?000[- ]character|3,?000[- ]character|30[-–]60[- ]second")
# Reserved wordings live in the record only until their ledger row flips.
RESERVED_A5 = (
    "Treat a viewer's shortened preview and a truncated tool return as claims about the display, "
    "not about the source"
)
RESERVED_A7A = (
    "Reused verification holds only while the source, inputs, base, dependencies, configuration, "
    "and acceptance it ran against are unchanged"
)
LEDGER_STATUS = {
    "A-1": "**Rejected (record-only)**",
    "A-2": "**Rejected (record-only)**",
    "A-3": "**Rejected as installed**",
    "A-5": "**Deferred beside I-1 (record-only now)**",
    "A-6": "**Rejected (host-specific)**",
    "A-7a": "**Adopted (user-directed 2026-09-10)**",
    "A-7b": "**Rejected as installed**",
    "A-8": "**Record-only (already held)**",
}


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _durable_surfaces() -> list[Path]:
    return (
        sorted(library_skills_dir().glob("*/SKILL.md"))
        + sorted(PROMPT_LIBRARY_ROOT.glob("SKILL_INSTALLATION*.md"))
        + [glossary_path()]
        + sorted(AGENT_DOCS.glob("*.md"))
    )


def test_survey_record_shape_identity_and_panel_provenance():
    text = _read(RECORD)
    assert "> **Status: decided, guarded, and verified — record-only." in "\n".join(text.splitlines()[:12])
    for heading in (
        "## Research Question", "## Direct Recommendation (as of 2026-09-10)", "## Method",
        "## What the Artifact Is", "## Panel Consensus", "## Concept Map",
        "## Socratic Questions and Disposition", "## Candidate Adoption Ledger",
        "## Packet Corrections", "## Disagreements / Residual Risks", "## Evidence Used",
        "## Evidence vs Inference", "## Evidence Actually Checked", "## Falsifiability", "## Completion Ledger",
    ):
        assert heading in text, heading
    assert REPO_REVISION in text and "2026-09-08" in text
    assert "8/8 delivered over hub" in text and "0 `DISAGREE`" in text
    recommendation = text.split("## Direct Recommendation", 1)[1].split("\n## ", 1)[0]
    for line in ("**Study: yes.**", "**Reproduce: not applicable.**", "**Adopt: no.**", "**Deploy: no.**"):
        assert line in recommendation, line
    assert "convergence evidence, not consensus" in recommendation
    assert "No fixed numeric cap" in recommendation
    # The lens tool-divergence claim stays recorded as a lens misreport, with I-1's trigger unfired.
    assert "lens misreport about a tool, not a tool misreport" in text
    assert "did **not** fire" in text


def test_candidate_ledger_preserves_all_dispositions_and_reserved_wordings():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = {line.split("|")[1].strip(): line for line in ledger.splitlines() if line.startswith("| A-")}
    assert set(rows) == set(LEDGER_STATUS), sorted(rows)
    for cid, status in LEDGER_STATUS.items():
        assert status in rows[cid], cid
    assert "skill-verification-panel-2026-09-05.md:46" in rows["A-5"]  # the shared single occurrence
    assert "gate-shop" in rows["A-5"]
    assert text.count(RESERVED_A5) == 1 and text.count(RESERVED_A7A) == 1


def test_no_surveyed_vocabulary_caps_or_reserved_wording_on_durable_surfaces():
    surfaces = _durable_surfaces()
    assert len(surfaces) >= 20, "surface set unexpectedly small"
    for path in surfaces:
        body = path.read_text(encoding="utf-8")
        assert not SURVEY_TOKENS.search(body), path
        assert not CAP_LITERALS.search(body), path
        assert RESERVED_A5 not in body, path
        # A-7a was adopted onto reflective-implement; its wording IS expected there.
        if "reflective-implement" not in str(path):
            assert RESERVED_A7A not in body, path


def test_a7a_adopted_wording_present_once_on_reflective_implement():
    body = _read(library_skills_dir() / "reflective-implement" / "SKILL.md")
    assert body.count(RESERVED_A7A) == 1, "A-7a is adopted; its wording must be pinned at its single surface"


def test_indexes_point_to_the_record():
    knowledge = _read(PROJECT_KNOWLEDGE)
    assert "[record](plans/astra-efficiency-rules-survey-2026-09-10.md)" in knowledge
    assert re.search(r"^- 2026-09-10 Context-efficiency instruction-profile survey", knowledge, re.M)
    case_studies = _read(CASE_STUDIES)
    assert case_studies.count("astra-efficiency-rules-survey-2026-09-10.md") >= 2  # comparison row + state ledger row
