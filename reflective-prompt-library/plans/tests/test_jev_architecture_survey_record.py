"""Guard the Jev architecture-analysis synthesis survey's identity,
dispositions, held-claim pins, clean-room boundary, and index links.

Record: plans/jev-architecture-synthesis-survey-2026-09-19.md — survey of a
pasted architecture-forensics thread (encoder vs no-loop causal decoder
behind a typed-decision API). Fourth pasted-synthesis survey; first whose
attributions all held against their cited pages. Record-only: no installed
change; JA-7/8/9 are dated record-only notes (DM-5 trigger evidence, genre
finding, citation drift after the cited repo's rename).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "jev-architecture-synthesis-survey-2026-09-19.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
SEMIF_HEAD = "b9cb32537e78"
CONFIG_ARCH = "Qwen3_5ForSequenceClassification"
CANDIDATE_STATUS = {
    "JA-1": "No change 2026-09-19",
    "JA-2": "No change 2026-09-19",
    "JA-3": "No change 2026-09-19",
    "JA-4": "No change 2026-09-19",
    "JA-5": "No change 2026-09-19",
    "JA-6": "No change 2026-09-19",
    "JA-7": "Noted 2026-09-19",
    "JA-8": "Noted 2026-09-19",
    "JA-9": "Noted 2026-09-19",
}
# Clean-room boundary: the surveyed thread's names and vocabulary stay in the record.
SURVEY_TOKENS = re.compile(
    r"SemIf|OpenJev|openjev|Archer Hume|archerhume|Roy Chen|RoyChen|\bNoul\b|"
    r"Hydragen|LLM2Vec|Gated DeltaNet|jev-1\.13|Qwen3\.5|2404\.05961|2402\.05099",
    re.IGNORECASE,
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


def test_record_preserves_source_identity_and_shape():
    text = _read(RECORD)
    assert SEMIF_HEAD in text
    assert CONFIG_ARCH in text
    assert "2026-09-17" in text  # probe essay publication date
    assert "348/415" in text  # tokenizer-scoping figure, pinned as read
    for heading in (
        "## Research Question",
        "## Direct Recommendation",
        "## Concept Map",
        "## Candidate Adoption Ledger",
        "## Evidence vs Inference",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"record missing {heading!r}"
    concepts = re.findall(r"^\| (C\d+) \|", text, re.M)
    assert concepts == [f"C{i}" for i in range(1, 9)]


def test_candidate_ledger_preserves_dispositions_and_triggers():
    text = _read(RECORD)
    rows = re.findall(r"^\| (JA-\d+) \|.*?\| (\S[^|]*?\d{4}-\d{2}-\d{2}[^|]*?) \|", text, re.M)
    found = {cid: status.strip() for cid, status in rows}
    assert set(found) == set(CANDIDATE_STATUS), f"ledger rows drifted: {sorted(found)}"
    for cid, want in CANDIDATE_STATUS.items():
        got = found[cid]
        assert got.startswith(want.split()[0]), f"{cid}: {got!r} lost {want!r}"
        assert want.split()[1] in got, f"{cid}: {got!r} lost its date"
    ja7 = [r for r in text.splitlines() if r.startswith("| JA-7 |")]
    assert ja7 and "host integrates" in ja7[0], (
        "JA-7 must keep the host-integration boundary that leaves DM-5 unfired"
    )


def test_record_keeps_the_held_verdict_and_its_bounds():
    text = _read(RECORD)
    assert "all held" in text.lower()
    assert "not independently verified" in text  # the one flagged sub-detail
    assert "unchanged public tokenizer" in text  # negative-probe scoping as read
    assert "Unknown — correctly so" in text  # the underdetermined conclusion stays unknown


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert surfaces, "no installed surfaces found"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert "jev-architecture-synthesis-survey-2026-09-19" in knowledge
    cases = _read(CASE_STUDIES)
    assert "jev-architecture-synthesis-survey-2026-09-19" in cases
    index = _read(PROMPT_LIBRARY_ROOT / "index.json")
    assert "jev-architecture-synthesis-survey-2026-09-19" in index
