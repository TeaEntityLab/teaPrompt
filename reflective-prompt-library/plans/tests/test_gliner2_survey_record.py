"""Guard the GLiNER2 survey: record identity and number pins, the quoted
disclosures held byte-exact, six dispositions, the clean-room boundary, and the
index links.

Jev/TypeSafe/Nimble/Bespoke vocabulary is deliberately not in this guard's
token set: the sibling decision-interface survey guards already police those
tokens over the same surfaces; duplicating the regex is weightless.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "gliner2-survey-2026-09-19.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

PIN = "d7c727458bf6929bc9ef5ee04e13c3f717a7c455"
TREE = "ef6b491265e2c3bc0f2ae325739f4618dabb6547"
HF_SHA = "78cea040597df251eedefa9d7ee2a756af39fe64"
CREATED = "2025-07-07"

QUOTES = (
    "Hierarchical structure extraction was not evaluated due to the absence of established zero-shot benchmarks for this task type, which we plan to address in future work.",
    "using task-specific prompts and validated for quality",
    "It dispatches by the saved `architecture` field.",
    "Schema-driven information extraction and classification — entities, labels, records, relations, and span attributes in one local model.",
    "The constrained path forbids that.",
    "Always inspect `result.feasible` in production if you keep the default.",
)
NUMBERS = ("0.590", "0.615", "0.599", "254,334", "205M", "2048", "193,581,591")
CANDIDATE_STATUS = {
    "G2-1": "Noted 2026-09-19 (record-only)",
    "G2-2": "No change 2026-09-19",
    "G2-3": "No change 2026-09-19",
    "G2-4": "No change 2026-09-19",
    "G2-5": "No change 2026-09-19",
    "G2-6": "Noted 2026-09-19 (record-only)",
}
# The project's vocabulary and its benchmark/product names stay in the record.
SURVEY_TOKENS = re.compile(
    r"GLiNER|GLiClass|GLiREL|GLiGuard|[Ff]astino|DeBERTa|CrossNER|Banking77|SNIPS|"
    r"AutoExtractor|propose-then-rerank|Zaratiana",
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


def test_record_identity_and_number_pins():
    text = _read(RECORD)
    assert re.search(r"^> \*\*Status: decided — record-only; no installed change", "\n".join(text.splitlines()[:12]), re.M)
    for pin in (PIN, TREE, HF_SHA, CREATED, "2025.emnlp-demos.10"):
        assert pin in text, pin
    assert "Apache-2.0" in text
    for number in NUMBERS:
        assert number in text, number
    for heading in (
        "Research Question", "Direct Recommendation", "Method", "What the Artifact Is",
        "Concept Map", "Candidate Adoption Ledger", "Shared Findings", "Evidence vs Inference",
        "Evidence Actually Checked", "Falsifiability", "Completion Ledger",
    ):
        assert f"## {heading}" in text, heading
    concept_map = text.split("## Concept Map", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^\| (C\d+) \|", concept_map, re.M) == [f"C{i}" for i in range(1, 11)]


def test_quoted_disclosures_pinned():
    text = _read(RECORD)
    for quote in QUOTES:
        assert quote in text, quote


def test_candidate_ledger_preserves_dispositions():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| G2-\d \|", line)
    ]
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 5, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3], f"missing evidence: {row[0]}"


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert len(surfaces) >= 20, "surface set unexpectedly small"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[plans/{RECORD.name}](plans/{RECORD.name})" in knowledge
    state = _read(CASE_STUDIES).split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert RECORD.name in state
