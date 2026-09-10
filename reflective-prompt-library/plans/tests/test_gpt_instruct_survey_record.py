"""Guard the survey's identity, decisions, and non-adoption boundary.

Interpretive report paragraphs are deliberately not pinned. Deferred wording
stays in the record; these checks bind repository authors, not host sessions.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "gpt-instruct-survey-2026-09-10.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
REPO_REVISION = "0ad8ec58e1989f4a058e01ce4e15cf226e8067bf"
LENSES = {
    "GIEvidence", "GIMethodology", "GIRedTeam", "GIProvenance",
    "GIUsability", "GIMinimality", "GIMeasurement", "GIStrategy",
}
CANDIDATE_STATUS = {
    "E-2": "Record-only",
    "E-5": "Deferred",
    "E-11": "Record-only",
    "E-12": "Record-only",
}
SURVEY_TOKENS = re.compile(
    r"gpt-instruct|MDX-Tom|codex-instruct|gpt-6-astra|gpt-5\.[0-9]|sol-v45|astra-v1|"
    r"\be\d+b\d+\b|model_instructions_file|issue-bank|prompt-bank|"
    r"batched_json_screen|raw_first_turn|semantic-completion|broad-completion|"
    r"issue-regression|yynxxxxx|破甲",
    re.IGNORECASE,
)
CAP_LITERALS = re.compile(
    r"\b(?:52/66|66/66|60/74|120/120)\b|8,?000[- ](?:UTF-8 )?byte|"
    r"5,?200[- ]char|900[- ]char|ten consecutive",
    re.IGNORECASE,
)
RESERVED_E5 = "when a named decision closes it against an oracle that did not hold"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _durable_surfaces() -> list[Path]:
    return (
        sorted(library_skills_dir().glob("*/SKILL.md"))
        + sorted(PROMPT_LIBRARY_ROOT.glob("SKILL_INSTALLATION*.md"))
        + [glossary_path()]
        + sorted((PROMPT_LIBRARY_ROOT / "04-agent").glob("*.md"))
    )


def test_record_preserves_source_identity_and_complete_panel():
    text = _read(RECORD)
    assert re.search(r"^> \*\*Status:.*record-only", "\n".join(text.splitlines()[:12]), re.M)
    for heading in (
        "Research Question", "Direct Recommendation", "Method", "Panel Consensus",
        "Shared Findings", "Required Wording Changes", "Disagreements / Residual Risks",
        "Evidence Used", "Evidence vs Inference", "Evidence Actually Checked", "Falsifiability",
    ):
        assert f"## {heading}" in text, heading
    assert REPO_REVISION in text
    panel = text.split("## Panel Consensus", 1)[1].split("\n## ", 1)[0]
    rows = [line.split("|")[1:-1] for line in panel.splitlines() if line.startswith("| GI")]
    assert len(rows) == len(LENSES)
    assert {row[0].strip() for row in rows} == LENSES
    assert all(row[1].strip() == "AGREE WITH CHANGES" for row in rows)
    sources = text.split("## Evidence Used", 1)[1].split("\n## ", 1)[0]
    source_rows = [line for line in sources.splitlines() if re.match(r"^\| S\d+ \|", line)]
    assert len(source_rows) == 7
    assert {line.split("|")[1].strip() for line in source_rows} == {f"S{i}" for i in range(1, 8)}
    for row in source_rows:
        assert REPO_REVISION in row and "accessed 2026-09-10" in row, row


def test_all_concepts_and_candidate_trigger_states_remain_recorded():
    text = _read(RECORD)
    concept_map = text.split("## Concept Map", 1)[1].split("\n## ", 1)[0]
    concepts = re.findall(r"^\| (E-\d+) \|", concept_map, re.M)
    assert len(concepts) == 13 and set(concepts) == {f"E-{i}" for i in range(1, 14)}
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in ledger.splitlines() if re.match(r"^\| E-\d+ \|", line)
    ]
    assert len(rows) == len(CANDIDATE_STATUS)
    assert {row[0] for row in rows} == set(CANDIDATE_STATUS)
    for row in rows:
        assert len(row) == 6, row
        assert row[2] == CANDIDATE_STATUS[row[0]], row
        assert row[3] == "untriggered", row
        assert row[4] and row[5], f"missing evidence or trigger/destination: {row[0]}"
    # This is a deferred draft, not adopted wording or an execution guarantee.
    assert RESERVED_E5 in ledger


def test_excluded_content_and_deferred_contract_do_not_enter_installed_surfaces():
    surfaces = _durable_surfaces()
    assert len(surfaces) >= 20, "surface set unexpectedly small"
    assert PROMPT_LIBRARY_ROOT / "SKILL_INSTALLATION.zh-TW.md" in surfaces
    for path in surfaces:
        body = _read(path)
        assert not SURVEY_TOKENS.search(body), path
        assert not CAP_LITERALS.search(body), path
        assert RESERVED_E5 not in body, path
    pack = _read(library_skills_dir() / "governed-delivery" / "SKILL.md")
    acceptance = pack.split("### acceptance-record", 1)[1].split("\n### ", 1)[0]
    assert not re.search(r"^unmet_oracles\s*:", acceptance, re.M)


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert f"[record](plans/{RECORD.name})" in knowledge
    cases = _read(CASE_STUDIES)
    comparison = cases.split("## Case Comparison", 1)[1].split("\n## ", 1)[0]
    state = cases.split("## State Ledger", 1)[1].split("\n## ", 1)[0]
    assert f"]({RECORD.name})" in comparison
    assert RECORD.name in state
