"""Guard the Agentflow 8.3.0 delta survey: pin identity (current + previous +
tree), the single-squashed-commit and schema-8 facts, the quoted source
literals, the ten AF83-* dispositions, the clean-room boundary (agentflow
vocabulary stays off installed surfaces), that prior adoptions are untouched,
and the index links.

This delta is record-only under DS-1 (bare survey → no adoption direction):
nothing was installed, so the clean-room and prior-adoptions-untouched tests are
the load-bearing ones.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    glossary_path,
    library_readme_path,
    library_skills_dir,
    methodology_map_en_path,
)

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "agentflow-8.3-delta-survey-2026-09-21.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
PRIOR_GUARDS = (
    PLANS_DIR / "tests" / "test_agentflow_v82_delta_record.py",
    PLANS_DIR / "tests" / "test_agentflow_survey_record.py",
)

PIN = "0abf416ccfe10016f16893239bf6c9fd9d4d71e9"
PREV = "fcb6878be0b2316cdba5a111f040655f161bfe03"
TREE = "f57233450a1a301a65dafb85be3157de69421fff"

# The delta's load-bearing identity facts: single squashed commit, schema bump,
# the compaction threshold, and the cited incident.
FACTS = ("8.3.0", "ahead_by 1", "schema 7 → 8", "768 KiB", "I-062")

# Verbatim source literals (contiguous in the record).
QUOTES = (
    "its order has no execution meaning",
    "does not claim Pi, Gemini, or OpenCode live verification",
    "Respectfully challenge mistaken, risky, or needlessly complex ideas",
    "prefer-independent",
)

CANDIDATE_STATUS = {
    "AF83-1": "No change",
    "AF83-2": "Record-only (host)",
    "AF83-3": "No change",
    "AF83-4": "Record-only (host)",
    "AF83-5": "Record-only (host)",
    "AF83-6": "No change",
    "AF83-7": "Rejected",
    "AF83-8": "Record-only (host)",
    "AF83-9": "No change",
    "AF83-10": "Record-only (host)",
}

# agentflow-specific vocabulary — grep-verified absent from installed surfaces
# this session; the record keeps it, the durable surfaces must not.
SURVEY_TOKENS = re.compile(
    r"agentflow|godev|devlog|allowed-worker|external-runner|"
    r"AGENTFLOW_SESSION|gpt-5\.6-sol|prefer-independent|fast-lane",
    re.IGNORECASE,
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    body = text.split(heading, 1)[1]
    return re.split(r"\n## ", body, maxsplit=1)[0]


def _durable_surfaces() -> list[Path]:
    surfaces: list[Path] = [
        glossary_path(),
        library_readme_path(),
        methodology_map_en_path(),
    ]
    surfaces += sorted(library_skills_dir().rglob("SKILL.md"))
    for category in ("00-core", "01-thinking", "02-engineering", "03-context",
                     "04-agent", "05-domain", "06-repo"):
        surfaces += sorted((PROMPT_LIBRARY_ROOT / category).glob("*.md"))
    return [p for p in surfaces if p.is_file()]


def test_record_identity_and_delta_facts():
    text = _read(RECORD)
    for pin in (PIN, PREV, TREE):
        assert pin in text, f"missing pin: {pin}"
    for fact in FACTS:
        assert fact in text, f"missing delta fact: {fact}"


def test_quoted_literals_pinned():
    text = _read(RECORD)
    for quote in QUOTES:
        assert quote in text, quote


def test_candidate_ledger_preserves_dispositions():
    ledger = _section(_read(RECORD), "## Candidate Adoption Ledger")
    seen: dict[str, str] = {}
    for line in ledger.splitlines():
        if not re.match(r"^\| AF83-\d+ \|", line):
            continue
        cells = [c.strip() for c in line.split("|")]
        cid, status, evidence, trigger = cells[1], cells[3], cells[4], cells[5]
        seen[cid] = status
        assert evidence, f"missing evidence: {cid}"
        assert trigger, f"missing trigger: {cid}"
    assert seen == CANDIDATE_STATUS, seen


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    for path in _durable_surfaces():
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_prior_adoptions_untouched():
    # A bare survey installs nothing: the prior agentflow guards must still exist,
    # and this record must state the old ledger is unchanged (no re-adoption).
    for guard in PRIOR_GUARDS:
        assert guard.is_file(), f"prior guard missing: {guard}"
    assert re.search(r"intentionally\s+unchanged", _read(RECORD)), "record must state prior adoptions untouched"


def test_existing_indexes_link_the_survey_decision():
    decision_index = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert RECORD.name in decision_index, "Decision Index does not link the record"
    assert RECORD.name in _read(CASE_STUDIES), "case-studies State Ledger does not link the record"


def test_direction_addendum_records_the_no_fire():
    addendum = _read(RECORD).split("## Direction Addendum", 1)[1]
    assert "unchanged" in addendum, "addendum must record the ledger is unchanged"
    # The skill-update re-run's load-bearing finding: AF83-6 is the counterargument
    # lens, not a skill gap (the corrected citation).
    assert "counterargument" in addendum, "addendum must cite the counterargument lens"
