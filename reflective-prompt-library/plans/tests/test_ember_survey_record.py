"""Guard the EMBER survey: preprint identity pins, the paste=source finding, the
quoted literals, the six EM-* dispositions, the clean-room boundary (EMBER
neuroscience vocabulary stays off installed surfaces), the TB-1 cross-link framed
as witness-not-authorization, and the index links.

Record-only under DS-1 (bare survey → no adoption direction): nothing installed,
so the clean-room and cross-link tests are the load-bearing ones.
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
RECORD = PLANS_DIR / "ember-snn-llm-survey-2026-09-22.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

# Preprint identity and load-bearing numbers.
IDENTITY = ("2604.12167v1", "14 Apr 2026", "CC BY-NC-ND", "William Savage")
FACTS = ("82.2%", "220,000-neuron", "N=1")

# Verbatim literals (contiguous in the record).
QUOTES = (
    "no claims about consciousness",
    "cannot be filtered like prompt-injected text",
    "Jennifer Aniston neuron",
    "reach_out",
)

CANDIDATE_STATUS = {
    "EM-1": "No change (out of scope)",
    "EM-2": "No change",
    "EM-3": "No change",
    "EM-4": "No change (cross-linked to TB-1)",
    "EM-5": "No change (out of scope)",
    "EM-6": "No change (out of scope)",
}

# EMBER-specific vocabulary — grep-verified absent from installed surfaces this
# session; the record keeps it, the durable surfaces must not.
SURVEY_TOKENS = re.compile(
    r"EMBER|STDP|spiking|reach_out|digitalember|Jennifer Aniston|"
    r"z-score|cascade-scaled|concept cell",
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


def test_record_identity_and_facts():
    text = _read(RECORD)
    for token in IDENTITY:
        assert token in text, f"missing identity token: {token}"
    for fact in FACTS:
        assert fact in text, f"missing fact: {fact}"


def test_paste_is_a_copy_of_the_source():
    text = _read(RECORD)
    assert re.search(r"lossy reader-mode copy", text), "record must state the paste is a copy"
    assert "the paste *is* the source" in text


def test_quoted_literals_pinned():
    text = _read(RECORD)
    for quote in QUOTES:
        assert quote in text, quote


def test_candidate_ledger_preserves_dispositions():
    ledger = _section(_read(RECORD), "## Candidate Adoption Ledger")
    seen: dict[str, str] = {}
    for line in ledger.splitlines():
        if not re.match(r"^\| EM-\d+ \|", line):
            continue
        cells = [c.strip() for c in line.split("|")]
        cid, status, evidence, trigger = cells[1], cells[3], cells[4], cells[5]
        seen[cid] = status
        assert evidence, f"missing evidence: {cid}"
        assert trigger, f"missing trigger: {cid}"
    assert seen == CANDIDATE_STATUS, seen


def test_cross_link_to_tb1_is_witness_not_authorization():
    section = _read(RECORD).split("## Cross-Link", 1)[1]
    assert "TB-1" in section
    assert "second external witness" in section
    # The honest recurrence rule: a preprint strengthens evidence, it does not fire
    # TB-1's user-direction trigger.
    assert re.search(r"still zero|not its\s+authorization|n=0 user directions", section)


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    for path in _durable_surfaces():
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    decision_index = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert RECORD.name in decision_index, "Decision Index does not link the record"
    assert RECORD.name in _read(CASE_STUDIES), "case-studies State Ledger does not link the record"
