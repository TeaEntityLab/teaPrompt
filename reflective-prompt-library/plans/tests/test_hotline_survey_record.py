"""Guard the hotline verification-redundancy survey: the two historical claims
(1963 wire+radio circuits, 1971 same-day agreement pair), the precision
corrections (satellites operational 1978; accident-risk wording belongs to the
Accidents Measures Agreement), the trust-minimized-not-eliminated assessment,
the five HL-* dispositions, the clean-room boundary, and the index links.

Record-only under DS-1 (bare survey → no adoption direction): nothing installed,
so the clean-room and ledger tests are the load-bearing ones.
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
RECORD = PLANS_DIR / "hotline-verification-redundancy-survey-2026-09-22.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

# Historical pins verified against primary sources.
FACTS = (
    "20 Jun 1963",
    "Tangier",
    "Molniya II",
    "Intelsat",
    "January 1978",
    "Accidents Measures",
)

# Verbatim literals (contiguous in the record).
QUOTES = (
    "Trust is not the architecture",
    "trust minimized and continuously verified",
    "The quick brown fox",
    "accidental or unauthorized use",
)

CANDIDATE_STATUS = {
    "HL-1": "No change — covered as judgment pattern; the four-item list is a checklist instance, not a new contract",
    "HL-2": "No change — installed",
    "HL-3": "No change — installed as methodology",
    "HL-4": "No change — installed",
    "HL-5": "No change — out of scope",
}

# Survey-specific vocabulary — grep-verified absent from installed surfaces this
# session; the record keeps it, the durable surfaces must not.
SURVEY_TOKENS = re.compile(
    r"Molniya|Intelsat|Tangier|hotline|radiotelegraph|teletype|"
    r"Accidents Measures|Six-Day War",
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


def test_record_facts_and_quotes():
    text = _read(RECORD)
    flat = re.sub(r"\s+", " ", text)
    for token in FACTS:
        assert token in flat, f"missing fact: {token}"
    for quote in QUOTES:
        assert quote in flat, quote

def test_corrections_pinned():
    text = _read(RECORD)
    # The 1971 accident-risk wording belongs to the companion treaty, not the
    # modernization agreement; satellites went live in 1978.
    assert "conflates two same-day agreements" in text
    assert "January 1978, not 1971" in text
    # Trust is minimized and verified, not eliminated.
    assert "Trust was *minimized and verified*, not eliminated" in text


def test_candidate_ledger_preserves_dispositions():
    ledger = _section(_read(RECORD), "## Candidate Adoption Ledger")
    seen: dict[str, str] = {}
    for line in ledger.splitlines():
        if not re.match(r"^\| HL-\d+ \|", line):
            continue
        cells = [c.strip() for c in line.split("|")]
        cid, status, evidence, trigger = cells[1], cells[4], cells[3], cells[5]
        seen[cid] = status
        assert evidence, f"missing evidence: {cid}"
        assert trigger, f"missing trigger: {cid}"
    assert seen == CANDIDATE_STATUS, seen


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    for path in _durable_surfaces():
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    decision_index = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert RECORD.name in decision_index, "Decision Index does not link the record"
    assert RECORD.name in _read(CASE_STUDIES), "case-studies State Ledger does not link the record"
