"""Guard the MiniMax Code survey's identity, dispositions, deferral trigger,
clean-room boundary, and index links.

Record: plans/minimax-code-survey-2026-09-19.md — survey of
MiniMax-AI/minimax-code (terminal coding agent published as the reviewed
public projection of an internal monorepo; Pi-lineage vendored agent core;
five co-located repo skills). Nine concepts covered or host territory;
MC-5 (tri-state consumer map) adopted 2026-09-19 under same-day user
direction as one additive Verification bullet on reflective-implement,
pinned once below; MC-7/MC-10 dated record-only notes.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "minimax-code-survey-2026-09-19.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
REPO_HEAD = "e3724a13d72d"
CANDIDATE_STATUS = {
    "MC-1": "No change 2026-09-19",
    "MC-2": "No change 2026-09-19",
    "MC-3": "No change 2026-09-19",
    "MC-4": "No change 2026-09-19",
    "MC-5": "Adopted 2026-09-19",
    "MC-6": "No change 2026-09-19",
    "MC-7": "Noted 2026-09-19",
    "MC-8": "No change 2026-09-19",
    "MC-9": "No change 2026-09-19",
    "MC-10": "Noted 2026-09-19",
}
# Clean-room boundary: the surveyed project's names and vocabulary stay in the record.
SURVEY_TOKENS = re.compile(
    r"MiniMax|minimax|\bmcode\b|MCode|pi-mono|pi-turn-runner|@mavis|\bMavis\b|"
    r"sandbox-runtime|public-source\.json|extraction\.json|vitest-suites",
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
    assert REPO_HEAD in text
    assert "MiniMax-AI/minimax-code" in text
    assert "2026-06-01" in text  # repo creation date
    assert "listing is not approval" in text.lower()
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
    rows = re.findall(r"^\| (MC-\d+) \|.*?\| (\S[^|]*?\d{4}-\d{2}-\d{2}[^|]*?) \|", text, re.M)
    found = {cid: status.strip() for cid, status in rows}
    assert set(found) == set(CANDIDATE_STATUS), f"ledger rows drifted: {sorted(found)}"
    for cid, want in CANDIDATE_STATUS.items():
        got = found[cid]
        assert got.startswith(want.split()[0]), f"{cid}: {got!r} lost {want!r}"
        assert want.split()[1] in got, f"{cid}: {got!r} lost its date"
    mc5 = [r for r in text.splitlines() if r.startswith("| MC-5 |")]
    assert mc5 and "never becomes a ledger row" in mc5[0], (
        "MC-5 must keep the verified-gap evidence and its retire condition"
    )


def test_record_keeps_the_bounded_tiers():
    text = _read(RECORD)
    assert "Author-claimed" in text  # gates-pass claims stay author-claimed
    assert "docs-to-code fidelity was not audited" in text  # scope bound vs the RSIAgent survey
    assert "independence beyond absence of citation" in text  # convergence claim bounded


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert surfaces, "no installed surfaces found"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert "minimax-code-survey-2026-09-19" in knowledge
    cases = _read(CASE_STUDIES)
    assert "minimax-code-survey-2026-09-19" in cases
    index = _read(PROMPT_LIBRARY_ROOT / "index.json")
    assert "minimax-code-survey-2026-09-19" in index


MC5_BULLET = "Consumer map, whenever a change alters a contract, field, default, schema, prompt, or identity"


def test_mc5_consumer_map_pinned_once_at_its_surface():
    hits = [p.name for p in _durable_surfaces() if MC5_BULLET in _read(p)]
    assert hits == ["SKILL.md"], hits
    skill = library_skills_dir() / "reflective-implement" / "SKILL.md"
    text = _read(skill)
    assert text.count(MC5_BULLET) == 1
    line = next(l for l in text.splitlines() if MC5_BULLET in l)
    for token in ("`covered`", "`not applicable`", "`unknown`", "Sufficiency Gate", "final observable consumer"):
        assert token in line, f"MC-5 bullet lost {token!r}"
