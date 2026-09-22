"""Guard the teaBrain concepts-and-experiments survey: record identity and tree
pins, the reproduced experiment numbers, the quoted load-bearing literals, the
twelve-concept map, the six candidate dispositions, the clean-room boundary
(teaBrain's neuroscience vocabulary stays off installed prompt/skill surfaces),
and the index links.

This survey is record-only under DS-1 (bare survey → no adoption): nothing was
installed on a durable surface, so the clean-room test is the load-bearing one.
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
RECORD = PLANS_DIR / "teabrain-concepts-experiments-survey-2026-09-21.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

PIN = "27b4d25a9516075c4fe6753e71c2ab1dc1b5465f"
TREE = "0788d2cd29eddb5d5db4da495fefedb943065a2f"

# Numbers reproduced this session at the pin — the survey's distinctive evidence.
NUMBERS = ("78.0%", "14.0%", "73.0%", "62.0%", "44.0%", "12 passed", "+51 pp", "0.15", "94% of Braitenberg")

# Verbatim load-bearing literals: the identical-vocabulary evidence (C1/C3/C5),
# the honest self-correction (C9), and the one-bet framing.
QUOTES = (
    "no backpropagation, no fine-tuning",
    "artifact-complete",
    "control-effective-under-full-disclosure",
    "reward_channel_provenance",
    "freeze_plasticity_and_escalate",
    "63% < 73%",
)

CANDIDATE_STATUS = {
    "TB-1": "No change 2026-09-21",
    "TB-2": "No change 2026-09-21",
    "TB-3": "Not fired 2026-09-21",
    "TB-4": "Noted (record-only)",
    "TB-5": "Noted (record-only)",
    "TB-6": "No change (out of scope)",
}

# teaBrain-specific neuroscience vocabulary — grep-verified absent from installed
# surfaces this session; the record keeps it, the durable surfaces must not.
SURVEY_TOKENS = re.compile(
    r"FlyHash|Kenyon|Braitenberg|chemotaxis|Drosophila|R-STDP|"
    r"node-perturbation|ring attractor|neuromorphic|teaBrain|spiking",
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


def test_record_identity_and_reproduced_numbers():
    text = _read(RECORD)
    assert PIN in text, "HEAD pin missing"
    assert TREE in text, "tree pin missing"
    for number in NUMBERS:
        assert number in text, f"missing reproduced number: {number}"
    # The reproduced-experiments section is what distinguishes this survey.
    assert "## Experiments Reproduced" in text


def test_concept_map_is_complete():
    concept_map = _section(_read(RECORD), "## Concept Map")
    ids = re.findall(r"^\| (C\d+) \|", concept_map, re.M)
    assert ids == [f"C{i}" for i in range(1, 13)], ids


def test_quoted_literals_pinned():
    text = _read(RECORD)
    for quote in QUOTES:
        assert quote in text, quote


def test_candidate_ledger_preserves_dispositions():
    ledger = _section(_read(RECORD), "## Candidate Adoption Ledger")
    seen: dict[str, str] = {}
    for line in ledger.splitlines():
        if not re.match(r"^\| TB-\d+ \|", line):
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


def test_existing_indexes_link_the_survey_decision():
    decision_index = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert RECORD.name in decision_index, "Decision Index does not link the record"
    assert RECORD.name in _read(CASE_STUDIES), "case-studies State Ledger does not link the record"


def test_direction_addendum_records_the_no_fire():
    addendum = _read(RECORD).split("## Direction Addendum", 1)[1]
    assert "byte-unchanged" in addendum
    assert "TB-1" in addendum
    # The generic direction authorizes a consideration, not a landing: the six
    # ledger dispositions above must be exactly the record's committed statuses.
    ledger = _section(_read(RECORD), "## Candidate Adoption Ledger")
    for cid, status in CANDIDATE_STATUS.items():
        assert f"| {cid} |" in ledger and status in ledger, cid
