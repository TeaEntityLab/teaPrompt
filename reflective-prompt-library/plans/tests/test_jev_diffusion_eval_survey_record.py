"""Guard the Jev-vs-diffusion eval survey's identity, claim-check pins,
dispositions, clean-room boundary, and index links.

Record: plans/jev-diffusion-eval-survey-2026-09-19.md — author-reported eval
thread (Jev vs an open diffusion LM served through a Jev-like vLLM patch).
Record-only: artifacts verified (main PR + two merged prerequisites + the
model), eval numbers author-claimed, planning-boundary finding recorded as
corroboration of the installed fast-path/deliberation split; MV-3/MV-6 dated
record-only notes (third substrate; DM-5 structural-signal evidence).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, glossary_path, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "jev-diffusion-eval-survey-2026-09-19.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
MAIN_PR = "57250"
CANDIDATE_STATUS = {
    "MV-1": "No change 2026-09-19",
    "MV-2": "No change 2026-09-19",
    "MV-3": "Noted 2026-09-19",
    "MV-4": "No change 2026-09-19",
    "MV-5": "No change 2026-09-19",
    "MV-6": "Noted 2026-09-19",
}
# Clean-room boundary: the surveyed thread's names and vocabulary stay in the
# record. "vLLM" is deliberately NOT a token here: it already appears
# legitimately on an installed surface (workflow-recipes' consensus-amplification
# caution, which predates this survey).
SURVEY_TOKENS = re.compile(
    r"mmastrac|Mastracci|DiffusionGemma|diffusiongemma|DGX Spark|26B-A4B|"
    r"Towers of Hanoi|pseudo-thinking",
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


def test_record_preserves_identity_and_claim_checks():
    text = _read(RECORD)
    assert MAIN_PR in text
    assert "google/diffusiongemma-26B-A4B-it" in text
    assert "two already merged" in text.lower() or "both merged" in text.lower()
    assert "Author-claimed" in text  # eval numbers stay author-claimed
    assert "canvas positions" in text  # mechanism as read from the PR
    assert "entropy" in text  # structural confidence signal
    for heading in (
        "## Research Question",
        "## Direct Recommendation",
        "## What the Thread Claims, and What Checked",
        "## Concept Map",
        "## Candidate Adoption Ledger",
        "## Evidence vs Inference",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"record missing {heading!r}"
    concepts = re.findall(r"^\| (C\d+) \|", text, re.M)
    assert concepts == [f"C{i}" for i in range(1, 7)]


def test_candidate_ledger_preserves_dispositions():
    text = _read(RECORD)
    rows = re.findall(r"^\| (MV-\d+) \|.*?\| (\S[^|]*?\d{4}-\d{2}-\d{2}[^|]*?) \|", text, re.M)
    found = {cid: status.strip() for cid, status in rows}
    assert set(found) == set(CANDIDATE_STATUS), f"ledger rows drifted: {sorted(found)}"
    for cid, want in CANDIDATE_STATUS.items():
        got = found[cid]
        assert got.startswith(want.split()[0]), f"{cid}: {got!r} lost {want!r}"
        assert want.split()[1] in got, f"{cid}: {got!r} lost its date"
    mv6 = [r for r in text.splitlines() if r.startswith("| MV-6 |")]
    assert mv6 and "not host integration" in mv6[0], (
        "MV-6 must keep the boundary that leaves DM-5 unfired"
    )


def test_survey_vocabulary_stays_out_of_installed_surfaces():
    surfaces = _durable_surfaces()
    assert surfaces, "no installed surfaces found"
    for path in surfaces:
        assert not SURVEY_TOKENS.search(_read(path)), path


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert "jev-diffusion-eval-survey-2026-09-19" in knowledge
    cases = _read(CASE_STUDIES)
    assert "jev-diffusion-eval-survey-2026-09-19" in cases
    index = _read(PROMPT_LIBRARY_ROOT / "index.json")
    assert "jev-diffusion-eval-survey-2026-09-19" in index
