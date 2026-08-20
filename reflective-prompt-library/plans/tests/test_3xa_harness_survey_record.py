"""Guard the 3xa-harness survey's evidence, dispositions, and cross-link."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "3xa-harness-survey-2026-08-20.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
TARGET_COMMIT = "bea12d3c0a1b25672fd027f627c148075a7f8ed7"
PACKET_SHA256 = "b86d3e2faeafcfba513b4f91fa949c166f8b92432037275b56ff3f8a9ac175ac"


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
    for candidate_id in ("3XA-1", "3XA-2", "3XA-3", "3XA-4", "3XA-5", "3XA-6"):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_survey_record_shape_revision_and_panel_provenance():
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
        assert heading in text, f"survey record missing {heading!r}"
    assert TARGET_COMMIT in text
    assert PACKET_SHA256 in text
    assert "7 of 7 lens verdicts" in text
    assert "Five scout yields were schema-coerced" in text


def test_survey_record_pins_executed_evidence_and_false_passes():
    text = _read(RECORD)
    for evidence in (
        "SELF_CHECK_OK",
        "16 declarations / eight unique skill targets",
        "58 relative links",
        "zero tests",
        "`sha256-demo`",
        "f4c25b5b45735b3183381384b47a345ce2262a0301a399855a9dd4fe8d052e9f",
        "FAIL-under-DONE",
        "absolute evidence",
        "continue-on-error",
    ):
        assert evidence in text, f"load-bearing evidence drifted: {evidence!r}"
    assert "No behavioral baseline/treatment eval" in text


def test_use_case_rows_block_unchanged_adoption_and_deployment():
    text = _read(RECORD)
    assert "| `adopt` scripts or five-skill lifecycle | **no**" in text
    assert "| `deploy` as a governed repository/fleet gate | **blocked at this revision**" in text
    assert (
        "No candidate created or changed a TeaPrompt skill, lens, verifier, dependency,\n"
        "runtime, or project-knowledge rule." in text
    )


def test_candidate_ledger_preserves_all_dispositions():
    rows = _ledger_rows()
    assert "Deferred / study-only 2026-08-20" in rows["3XA-1"]
    assert "Deferred / study-only 2026-08-20" in rows["3XA-2"]
    assert "No change 2026-08-20" in rows["3XA-3"]
    assert "Rejected 2026-08-20" in rows["3XA-4"]
    assert "Rejected 2026-08-20" in rows["3XA-5"]
    assert "Rejected; deployment blocked 2026-08-20" in rows["3XA-6"]
    assert "documented local reviewed-vs-shipped asset drift" in rows["3XA-1"]
    assert "documented local handoff" in rows["3XA-2"]


def test_external_adoption_case_study_links_survey_record():
    text = _read(CASE_STUDIES)
    row = next(
        line
        for line in text.splitlines()
        if "| 2026-08-20 | 3xa-harness bundle-v0.1.0 |" in line
    )
    assert "[survey](3xa-harness-survey-2026-08-20.md)" in row
    assert "no TeaPrompt skill, lens, verifier, dependency, or runtime adoption" in row
    assert "| 3xa-harness survey outcome recorded | done |" in text
