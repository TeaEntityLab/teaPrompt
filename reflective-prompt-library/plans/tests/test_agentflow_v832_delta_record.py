"""Guard the Agentflow 8.3.2 delta survey: pin identity (current + previous +
tree), the two-patch-release / schema-unchanged facts, the quoted source
literals, the three AF832-* host dispositions, the clean-room boundary, prior
adoptions untouched, and the index links.

Record-only under DS-1 (bare survey → no adoption direction): 8.3.1/8.3.2 are
host-only patch releases, so every candidate is `No change (host)`.
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
RECORD = PLANS_DIR / "agentflow-8.3.2-delta-survey-2026-09-22.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
PRIOR_GUARDS = (
    PLANS_DIR / "tests" / "test_agentflow_v83_delta_record.py",
    PLANS_DIR / "tests" / "test_agentflow_v82_delta_record.py",
    PLANS_DIR / "tests" / "test_agentflow_survey_record.py",
)

PIN = "6d699038ea14bf246c7bfaaef1ea4348a467d639"
PREV = "0abf416ccfe10016f16893239bf6c9fd9d4d71e9"
TREE = "697b93dc832041fcf2a7b287ca0de69de551aded"

FACTS = ("8.3.2", "ahead_by 4", "8 — unchanged")

QUOTES = (
    "--include-answered true",
    "committed empty notebook as proof",
    "preserve-before-destroy",
)

CANDIDATE_STATUS = {
    "AF832-1": "No change (host)",
    "AF832-2": "No change (host)",
    "AF832-3": "No change (host)",
}

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
        if not re.match(r"^\| AF832-\d+ \|", line):
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
    for guard in PRIOR_GUARDS:
        assert guard.is_file(), f"prior guard missing: {guard}"
    assert re.search(r"intentionally\s+unchanged", _read(RECORD)), "record must state prior ledger untouched"


def test_existing_indexes_link_the_survey_decision():
    decision_index = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert RECORD.name in decision_index, "Decision Index does not link the record"
    assert RECORD.name in _read(CASE_STUDIES), "case-studies State Ledger does not link the record"
