"""Guard the 2026-09-19 direction-scope docs adoption: DS-1 pinned exactly once
on the external-adoption-review lens (inside Signal Accounting, after the
missing-usage rule) and off every other durable surface, DS-2 pinned in the
quality-gates summary, the record's three dispositions, and the index links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "direction-scope-docs-adoption-2026-09-19.md"
LENS = PROMPT_LIBRARY_ROOT / "04-agent" / "external-adoption-review.md"
GATES_SUMMARY = PLANS_DIR / "QUALITY_GATES_SUMMARY.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

DS1_SENTENCE = (
    "A later user direction is read at the scope it names: direction naming a source or survey "
    "family fires the user-direction-gated candidates that family's records carry; a generic "
    '"adopt what\'s worth it" inside one review fires only that review\'s own candidates, never '
    "a named hold elsewhere. A fired consideration trigger authorizes the consideration it "
    "names, not a landing."
)
DS2_FRAGMENT = (
    "staleness of the committed copy is enforced by "
    "`plans/tests/test_index_json_current.py` in `make test`"
)
CANDIDATE_STATUS = {
    "DS-1": "Adopted 2026-09-19",
    "DS-2": "Adopted 2026-09-19",
    "DS-3": "No change 2026-09-19",
}


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_ds1_pinned_once_inside_signal_accounting():
    text = _read(LENS)
    assert text.count(DS1_SENTENCE) == 1
    section = text.split("## 5. Signal Accounting", 1)[1].split("\n## ", 1)[0]
    assert DS1_SENTENCE in section
    assert section.index("Missing usage data") < section.index(DS1_SENTENCE)


def test_ds1_absent_from_every_other_durable_surface():
    others = (
        sorted(library_skills_dir().glob("*/SKILL.md"))
        + sorted(library_skills_dir().glob("examples/*.md"))
        + sorted(PROMPT_LIBRARY_ROOT.glob("SKILL_INSTALLATION*.md"))
        + [p for p in sorted((PROMPT_LIBRARY_ROOT / "04-agent").glob("*.md")) if p != LENS]
    )
    assert len(others) >= 20, "surface set unexpectedly small"
    for path in others:
        assert DS1_SENTENCE not in _read(path), path


def test_ds2_pinned_in_gates_summary():
    text = _read(GATES_SUMMARY)
    assert text.count(DS2_FRAGMENT) == 1
    assert "after editing any indexed file, not only after adding one" in text


def test_record_preserves_dispositions():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| DS-\d \|", line)
    ]
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 5, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3], f"missing evidence: {row[0]}"
    assert DS1_SENTENCE not in text, "the record paraphrases DS-1; the wording lives on the lens"


def test_indexes_link_the_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[record](plans/{RECORD.name})" in knowledge
    state = _read(CASE_STUDIES).split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert RECORD.name in state
