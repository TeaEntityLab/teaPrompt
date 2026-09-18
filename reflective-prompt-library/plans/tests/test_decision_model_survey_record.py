"""Guard the decision-model survey's identity, dispositions, corrections,
clean-room boundary, and index links.

Record: plans/decision-model-survey-2026-09-18.md — survey of
dsif2012/Qwen3-4B-Instruct-2507-Decision (inference interface over stock
Qwen3 weights) and its two inspirations (TypeSafe Jev / System One;
harshatheg/Qwen-2.5-1B-RLCD parallel-constrained-decoding card).
Record-only: no installed change; the two corrections (the RLCD acronym
conflation and the 1B/1.5B base-model mismatch) live in the record.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "decision-model-survey-2026-09-18.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
REPO_REVISION = "88e919834d2eee2af181300c0b8504e96b86ae7d"
CANDIDATE_STATUS = {
    "DM-1": "No change 2026-09-18",
    "DM-2": "No change 2026-09-18",
    "DM-3": "No change 2026-09-18",
    "DM-4": "No change 2026-09-18",
    "DM-5": "Rejected 2026-09-18",
    "DM-6": "Rejected 2026-09-18",
    "DM-7": "Corrected 2026-09-18",
    "DM-8": "Corrected 2026-09-18",
    "DM-9": "No change 2026-09-18",
}
# Clean-room boundary: the surveyed projects' names and vocabulary stay in the record.
SURVEY_TOKENS = re.compile(
    r"RLCD|TypeSafe|\bJev\b|System One|dsif2012|harshatheg|drinkmoonshine|"
    r"Parallel Constrained Decoding|Qwen3-4B|Qwen2\.5-1\.5B|pcd-cuda",
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
    assert REPO_REVISION in text
    assert "dsif2012/Qwen3-4B-Instruct-2507-Decision" in text
    assert "harshatheg/Qwen-2.5-1B-RLCD" in text
    assert "Apache-2.0" in text
    assert "does not ship new weights" in text
    for heading in (
        "## Research Question",
        "## Direct Recommendation",
        "## Concept Map",
        "## Candidate Adoption Ledger",
        "## Claim Check",
        "## Evidence vs Inference",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"record missing {heading!r}"
    concepts = re.findall(r"^\| (C\d+) \|", text, re.M)
    assert concepts == [f"C{i}" for i in range(1, 9)]


def test_candidate_ledger_preserves_dispositions_and_triggers():
    text = _read(RECORD)
    rows = re.findall(r"^\| (DM-\d+) \|.*?\| (\S[^|]*?\d{4}-\d{2}-\d{2}[^|]*?) \|", text, re.M)
    found = {cid: status.strip() for cid, status in rows}
    assert set(found) == set(CANDIDATE_STATUS), f"ledger rows drifted: {sorted(found)}"
    for cid, want in CANDIDATE_STATUS.items():
        got = found[cid]
        assert got.startswith(want.split()[0]), f"{cid}: {got!r} lost {want!r}"
        assert want.split()[1] in got, f"{cid}: {got!r} lost its date"
    dm5 = [r for r in text.splitlines() if r.startswith("| DM-5 |")]
    assert dm5 and "real candidate scores" in dm5[0], (
        "DM-5 trigger must name the structural signal that reopens it"
    )


def test_record_keeps_the_two_corrections():
    text = _read(RECORD)
    assert "Reinforcement Learning for Calibrated Decisions" in text
    assert "Qwen2.5-1.5B-Instruct" in text
    assert "Conflation" in text


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert surfaces, "no installed surfaces found"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert "decision-model-survey-2026-09-18" in knowledge
    cases = _read(CASE_STUDIES)
    assert "decision-model-survey-2026-09-18" in cases
    index = _read(PROMPT_LIBRARY_ROOT / "index.json")
    assert "decision-model-survey-2026-09-18" in index
