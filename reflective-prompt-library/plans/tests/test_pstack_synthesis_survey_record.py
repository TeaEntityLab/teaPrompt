"""Guard the pstack synthesis survey: the pin, the verified repo claims
(23 playbooks, shipping patch-id binding, autopilot-full merge rule), the
"Gardener" absence finding, the external-citation verdicts (METR/DORA/OpenAI),
the eight PS2-* dispositions, the clean-room boundary, and the index links.

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
RECORD = PLANS_DIR / "pstack-synthesis-survey-2026-09-22.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

# Pins and verified facts.
FACTS = (
    "53e579f1481697931fc44f5445171397cfa2b24b",
    "23 playbooks",
    "git patch-id",
    "19% slower",
    "Gardener",
)

# Verbatim literals (contiguous in the record).
QUOTES = (
    "omitted on purpose",
    "Engineer the Environment, Govern the Effects",
    "zero hits in the pinned tree",
)
CANDIDATE_STATUS = {
    "PS2-1": "No change — installed",
    "PS2-2": "No change — installed",
    "PS2-3": "Deferred — pilot design input only",
    "PS2-4": "No change — host responsibility",
    "PS2-5": "No change — installed",
    "PS2-6": "No change — reframing of installed coverage",
    "PS2-7": "**Record as pilot design** — the protocol is the correct evaluation shape if PS-C1 is ever triggered",
    "PS2-8": "Closed — no mechanism exists to evaluate; the underlying need (human maintenance authority) is already covered by runtime-trust-boundary",
}

# Survey-specific vocabulary — grep-verified absent from installed surfaces this
# session; the record keeps it, the durable surfaces must not.
SURVEY_TOKENS = re.compile(
    r"poteto|pstack|Molniya|Intelsat|Atlas|Harbor Labs|patch-id|"
    r"Gardener|Sealed Oracle|paste-4",
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


def test_gardener_absence_pinned():
    text = _read(RECORD)
    assert "zero hits in the pinned tree" in text
    assert "Not a pstack mechanism" in text


def test_candidate_ledger_preserves_dispositions():
    ledger = _section(_read(RECORD), "## Candidate Adoption Ledger")
    seen: dict[str, str] = {}
    for line in ledger.splitlines():
        if not re.match(r"^\| PS2-\d+ \|", line):
            continue
        cells = [c.strip() for c in line.split("|")]
        cid, status = cells[1], cells[4]
        seen[cid] = status
        assert cells[3], f"missing evidence: {cid}"
        assert cells[5], f"missing trigger: {cid}"
    assert seen == CANDIDATE_STATUS, seen


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    for path in _durable_surfaces():
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    decision_index = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert RECORD.name in decision_index, "Decision Index does not link the record"
    assert RECORD.name in _read(CASE_STUDIES), "case-studies State Ledger does not link the record"
