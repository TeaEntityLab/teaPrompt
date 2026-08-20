"""Guard the J-Space Cognition Suite survey's evidence and dispositions."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "jspace-cognition-survey-2026-08-20.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
TARGET_COMMIT = "feac3df52d702ced67dda217f7a5167e1935d442"
PACKET_SHA256 = "94f4cb955e2d60d64382a02f20d83e4a82b3db178f6bf820398b66f9cf21311e"


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
    for candidate_id in ("JS-1", "JS-2", "JS-3", "JS-4", "JS-5", "JS-6"):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_survey_shape_revision_and_panel_dissent():
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
    assert "majority **6 of 7 lens verdicts**" in text
    assert "architecture lens returned `DISAGREE`" in text
    assert "Five scout yields were schema-coerced" in text


def test_record_pins_executed_evidence_and_claim_boundaries():
    text = _read(RECORD)
    for evidence in (
        "18 tests passed",
        "14/20 concurrent retention",
        "symlink wrote externally",
        "unclosed fence returned `clean`",
        "duplicate/unknown headings lost data",
        "2.53× speed",
        "2.21× token-cost improvement",
        "issue #6",
        "issue #10",
        "issue #26",
        "activation-defined J-space",
        "No activation interface",
    ):
        assert evidence in text, f"load-bearing evidence drifted: {evidence!r}"
    assert "Fraud remains unproven" in text


def test_use_case_rows_block_adoption_and_deployment():
    text = _read(RECORD)
    assert "| `adopt` skill/modules/controller | **no**" in text
    assert (
        "| `deploy` in shared, concurrent, sensitive, or untrusted workspaces | "
        "**blocked at this revision** |" in text
    )
    assert (
        "No candidate created or changed a TeaPrompt skill, lens, verifier, dependency,\n"
        "runtime, or project-knowledge rule." in text
    )


def test_candidate_ledger_preserves_all_dispositions():
    rows = _ledger_rows()
    for candidate_id in ("JS-1", "JS-2", "JS-3", "JS-4"):
        assert "Deferred / study-only 2026-08-20" in rows[candidate_id]
    assert "Rejected 2026-08-20" in rows["JS-5"]
    assert "Rejected; deployment blocked 2026-08-20" in rows["JS-6"]
    assert "neutral-framing ablation" in rows["JS-1"]
    assert "repeated local recovery failures" in rows["JS-2"]
    assert "documented local leak" in rows["JS-3"]
    assert "prompt-impossible persistence/reentry" in rows["JS-4"]


def test_external_adoption_case_study_links_survey_record():
    text = _read(CASE_STUDIES)
    row = next(
        line
        for line in text.splitlines()
        if "| 2026-08-20 | J-Space Cognition Suite v3.6.1 |" in line
    )
    assert "[survey](jspace-cognition-survey-2026-08-20.md)" in row
    assert "no TeaPrompt skill, lens, verifier, dependency, or runtime adoption" in row
    assert "| J-Space Cognition Suite survey outcome recorded | done |" in text
