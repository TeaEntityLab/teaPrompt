"""Guard the graph-engineering synthesis survey: record shape, ten dispositions,
the reserved GE-1 wording kept OFF every installed surface until user direction
lands it, the fired-but-held Durable-Lesson trigger, the clean-room boundary,
and the index links.

Interpretive paragraphs are not pinned. If GE-1 is later landed by direction,
flip `test_ge1_reserved_wording_stays_out_of_installed_surfaces` to pin it once.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "graph-engineering-synthesis-survey-2026-09-16.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
LESSON_HEADING = "### Lesson: A pasted synthesis is a claim about its source, not the source"
GE1_SENTENCE = (
    "A summary's citation is the summary's claim about a source, not the source's evidence: "
    "a claim that arrived through a summary keeps the summary in its Source column until the "
    "cited page is read, however real the link; then record what the page says beside what "
    "the summary said it says."
)
CANDIDATE_STATUS = {
    "GE-1": "Deferred 2026-09-16 (considered at the fired gate; lands only on user direction)",
    "GE-2": "No change 2026-09-16",
    "GE-3": "No change 2026-09-16",
    "GE-4": "No change 2026-09-16",
    "GE-5": "Rejected 2026-09-16",
    "GE-6": "No change 2026-09-16",
    "GE-7": "No change 2026-09-16",
    "GE-8": "No change 2026-09-16",
    "GE-9": "No change 2026-09-16",
    "GE-10": "Refuted 2026-09-16 (record-only)",
}
# The synthesis's vocabulary and the vendor product names stay in the record.
SURVEY_TOKENS = re.compile(
    r"LangGraph|GraphRAG|LazyGraphRAG|[Gg]raph [Ee]ngineering|Agentic RAG|aibuilderclub|"
    r"CSDN|Harrison Chase|Send API|recursion_limit|RemainingSteps|DRIFT Search|Copilot Studio",
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


def test_record_shape_and_source_verdicts():
    text = _read(RECORD)
    assert re.search(r"^> \*\*Status:.*record-only; no installed change", "\n".join(text.splitlines()[:12]), re.M)
    for heading in (
        "Research Question", "Direct Recommendation", "Method", "What the Artifact Is",
        "Concept Map", "Candidate Adoption Ledger", "Shared Findings", "Evidence vs Inference",
        "Evidence Actually Checked", "Falsifiability", "Completion Ledger",
    ):
        assert f"## {heading}" in text, heading
    artifact = text.split("## What the Artifact Is", 1)[1].split("\n## ", 1)[0]
    for verdict in ("**Not substantiated by the inspected sources.**", "**Real sources, overclaimed.**", "**Thesis inverted.**", "**Real page, claim absent.**"):
        assert verdict in artifact, verdict
    concept_map = text.split("## Concept Map", 1)[1].split("\n## ", 1)[0]
    assert re.findall(r"^\| (G\d) \|", concept_map, re.M) == [f"G{i}" for i in range(1, 9)]


def test_candidate_ledger_preserves_dispositions():
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| GE-\d+ \|", line)
    ]
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 5, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3], f"missing evidence: {row[0]}"


def test_ge1_reserved_wording_stays_out_of_installed_surfaces():
    """The fired trigger authorized a consideration, not a landing: the drafted
    sentence lives in the record's ledger only (PROJECT_KNOWLEDGE.md header;
    06-repo/AGENTS.md: project judgement never grants agent authority)."""
    ledger = _read(RECORD).split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    assert GE1_SENTENCE in ledger
    for path in _durable_surfaces():
        assert GE1_SENTENCE not in _read(path), path


def test_durable_lesson_records_the_fired_trigger():
    knowledge = _read(PROJECT_KNOWLEDGE)
    lesson = knowledge.split(LESSON_HEADING, 1)[1].split("### Lesson:", 1)[0]
    assert f"[plans/{RECORD.name}](plans/{RECORD.name})" in lesson
    assert "Review trigger: fired 2026-09-16" in lesson
    assert "pending user direction" in lesson
    assert "now sits on" not in lesson, "the lesson must not claim the sentence is installed"


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert len(surfaces) >= 20, "surface set unexpectedly small"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[record](plans/{RECORD.name})" in knowledge
    cases = _read(CASE_STUDIES)
    comparison = cases.split("## Case Comparison", 1)[1].split("\n## ", 1)[0]
    state = cases.split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert f"]({RECORD.name})" in comparison
    assert RECORD.name in state
