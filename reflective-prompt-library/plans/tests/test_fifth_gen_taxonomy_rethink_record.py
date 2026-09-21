"""Guard the fifth-generation prompt-taxonomy rethink: record identity pins,
the pasted instruction held verbatim, the seven category names, five
dispositions, the coaxing-sweep result line, the clean-room boundary, and the
index links.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "fifth-gen-prompt-taxonomy-rethink-2026-09-21.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

INSTRUCTION_LINES = (
    "Rethink: 第五代大模型(astra/fable)問市後最新 prompt 技巧指引如下：",
    "超出上開列表的提示皆屬多餘甚至可能阻礙模型表現",
)
CATEGORIES = (
    "requirements",
    "output contracts",
    "invariants",
    "validation",
    "transformation",
    "knowledge",
    "observation",
)
CANDIDATE_STATUS = {
    "RT-1": "No change 2026-09-21",
    "RT-2": "Rejected 2026-09-21",
    "RT-3": "No change 2026-09-21",
    "RT-4": "No change 2026-09-21",
    "RT-5": "Adopted 2026-09-21 (record-only)",
}
# The surveyed vocabulary stays in the record, off installed surfaces.
SURVEY_TOKENS = re.compile(
    r"Astra|Fable|GPT-6|fifth-generation|5th-gen|Requirement-Oriented Prompt Engineering",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _durable_surfaces() -> list[Path]:
    return (
        sorted(library_skills_dir().glob("*/SKILL.md"))
        + sorted(library_skills_dir().glob("examples/*.md"))
        + sorted(PROMPT_LIBRARY_ROOT.glob("SKILL_INSTALLATION*.md"))
        + [glossary_path()]
        + sorted((PROMPT_LIBRARY_ROOT / "04-agent").glob("*.md"))
    )


def test_record_identity_and_shape():
    text = _read(RECORD)
    assert "Status: decided — record-only" in text
    for line in INSTRUCTION_LINES:
        assert line in text, line
    for category in CATEGORIES:
        assert category in text, category
    concept_map = text.split("## Concept Map", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^\| (C\d+) \|", concept_map, re.M) == [f"C{i}" for i in range(1, 10)]


def test_sweep_result_and_verdict_pinned():
    text = _read(RECORD)
    assert "three benign role headers" in text
    assert "zero persona/style/few-shot-coaxing content" in text
    assert "category error" in text


def test_candidate_ledger_preserves_dispositions():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    for candidate, status in CANDIDATE_STATUS.items():
        row = next(r for r in ledger.splitlines() if r.startswith(f"| {candidate} |"))
        assert status in row, row
        assert row.rstrip().endswith("|"), row


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    for path in _durable_surfaces():
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_rethink():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[record](plans/{RECORD.name})" in knowledge
    state = _read(CASE_STUDIES).split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert RECORD.name in state
