"""Guard the DilinAI Nuwa/Jiyao survey's durable no-change decision."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "dilinai-nuwa-jiyao-survey-2026-07-13.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
SOURCE_HASHES = (
    "6c8af51b6ce816adf2cb32e6709924d67d3f2b3a8693350b3183fe1fceb62613",
    "0d035f71077c531344fab18901e963f24e501eab9a632108bfd0504a4062be5e",
    "a35e9c1b3a84366104de1431930ac156df9c98d6c670c5ad7344f203d5c99072",
    "cf095604d50393a6456b68881fdbfafb330eb2e8555f40208d26f322865edad5",
    "334608fe4881ad18fd24372deae4a82b652f3cf9e4094f3ae26deb62886304e6",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Shared Findings",
        1,
    )[0]
    rows = {}
    for candidate_id in (
        "DJ1",
        "DJ2",
        "DJ3",
        "DJ4",
        "DJ5",
        "DJ6",
        "DJ7",
        "DJ8",
    ):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_dilinai_survey_record_shape_and_source_snapshot():
    text = _read(RECORD)
    for heading in (
        "## Panel Consensus",
        "## Required Wording Changes",
        "## Candidate Adoption Ledger",
        "## Shared Findings",
        "## Evidence vs Inference",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
    ):
        assert heading in text, f"DilinAI survey missing {heading!r}"
    for source_hash in SOURCE_HASHES:
        assert source_hash in text
    assert "| `adopt` into TeaPrompt | **no** |" in text
    assert "| `deploy` | **no** |" in text
    assert "No governed TeaPrompt wording, skill, role, verifier, dependency" in text


def test_dilinai_candidate_ledger_preserves_no_change_dispositions():
    rows = _ledger_rows()
    assert "Partial 2026-07-13 — concept only" in rows["DJ1"]
    for candidate_id in ("DJ2", "DJ3", "DJ4", "DJ5", "DJ6", "DJ7", "DJ8"):
        assert "Deferred" in rows[candidate_id], (
            f"{candidate_id} must remain deferred until its recorded trigger fires"
        )
    assert "regression as published" in rows["DJ5"]
    assert "reject no-loss claim as stated" in rows["DJ6"]
    assert "standing non-goal" in rows["DJ7"]
    assert "blocked" in rows["DJ8"]


def test_external_adoption_case_study_links_dilinai_record():
    text = _read(CASE_STUDIES)
    row = next(
        line
        for line in text.splitlines()
        if "| DilinAI Nuwa + Jiyao / team memory officer |" in line
    )
    assert "[survey](dilinai-nuwa-jiyao-survey-2026-07-13.md)" in row
    assert "no TeaPrompt prompt, skill, role, verifier, dependency, or runtime adoption" in row
    assert "| DilinAI Nuwa/Jiyao no-change outcome recorded | done |" in text
