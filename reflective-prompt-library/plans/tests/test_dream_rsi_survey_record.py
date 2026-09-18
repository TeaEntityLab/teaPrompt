"""Guard the Dream-RSI survey's identity, dispositions, corrections,
clean-room boundary, and index links.

Record: plans/dream-rsi-survey-2026-09-18.md — survey of
zhengkid/Dream-RSI (paper-only repo, no LICENSE, code "being prepared")
and its project site/PDF: discovery history as an exact replay simulator
for off-policy exploration-policy evaluation. Record-only: no installed
change; DR-5 (semantic-guidance caution) deferred with reserved wording;
DR-8/DR-9 are record-only scope corrections.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "dream-rsi-survey-2026-09-18.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
REPO_REVISION = "4149ea9181ab"
CANDIDATE_STATUS = {
    "DR-1": "No change 2026-09-18",
    "DR-2": "No change 2026-09-18",
    "DR-3": "No change 2026-09-18",
    "DR-4": "No change 2026-09-18",
    "DR-5": "Deferred 2026-09-18",
    "DR-6": "No change 2026-09-18",
    "DR-7": "No change 2026-09-18",
    "DR-8": "Corrected 2026-09-18",
    "DR-9": "Corrected 2026-09-18",
    "DR-10": "No change 2026-09-18",
}
# Clean-room boundary: the surveyed project's names and vocabulary stay in the record.
SURVEY_TOKENS = re.compile(
    r"Dream-RSI|dream-rsi|zhengkid|SimpleTES|AlphaEvolve|KernelBench|"
    r"Recursive Fixed Exploration|replay simulator|Gemini-3\.|2609\.14858|"
    r"discovery tree|discovery-agent",
    re.IGNORECASE,
)
# DR-5's reserved wording must stay out of installed surfaces until user direction.
DR5_RESERVED = "Directional guidance distilled from prior runs can shrink the space"


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
    assert "zhengkid/Dream-RSI" in text
    assert "2609.14858" in text
    assert "no LICENSE" in text or "license: none" in text.lower() or "no license" in text.lower()
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
    assert concepts == [f"C{i}" for i in range(1, 11)]


def test_candidate_ledger_preserves_dispositions_and_triggers():
    text = _read(RECORD)
    rows = re.findall(r"^\| (DR-\d+) \|.*?\| (\S[^|]*?\d{4}-\d{2}-\d{2}[^|]*?) \|", text, re.M)
    found = {cid: status.strip() for cid, status in rows}
    assert set(found) == set(CANDIDATE_STATUS), f"ledger rows drifted: {sorted(found)}"
    for cid, want in CANDIDATE_STATUS.items():
        got = found[cid]
        assert got.startswith(want.split()[0]), f"{cid}: {got!r} lost {want!r}"
        assert want.split()[1] in got, f"{cid}: {got!r} lost its date"
    deferred = [r for r in text.splitlines() if r.startswith("| DR-5 |")]
    assert deferred and "directional guidance" in deferred[0], (
        "DR-5 trigger must name the proposed surface that reopens it"
    )


def test_record_keeps_the_scope_corrections():
    text = _read(RECORD)
    assert "average replay score" in text
    assert "policy-development agent" in text


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert surfaces, "no installed surfaces found"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_dr5_reserved_wording_absent_from_installed_surfaces():
    for path in _durable_surfaces():
        assert DR5_RESERVED not in _read(path), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert "dream-rsi-survey-2026-09-18" in knowledge
    cases = _read(CASE_STUDIES)
    assert "dream-rsi-survey-2026-09-18" in cases
    index = _read(PROMPT_LIBRARY_ROOT / "index.json")
    assert "dream-rsi-survey-2026-09-18" in index
