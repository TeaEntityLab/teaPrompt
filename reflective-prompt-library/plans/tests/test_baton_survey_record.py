"""Guard the Baton survey's durable no-change decision and cross-link."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "baton-dispatch-survey-2026-07-13.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PINNED_COMMIT = "77f12e600406065a6e62a22a66347355e278a9d7"


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
    for candidate_id in ("BA1", "BA2", "BA3", "BA4", "BA5", "BA6", "BA7"):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_baton_survey_record_shape_and_revision():
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
        assert heading in text, f"Baton survey missing {heading!r}"
    assert PINNED_COMMIT in text
    assert "`baton-dispatch` v0.1.1" in text
    assert "| `adopt` into TeaPrompt | **no** |" in text


def test_baton_candidate_ledger_preserves_no_change_dispositions():
    rows = _ledger_rows()
    assert "Partial 2026-07-13 — concept only" in rows["BA1"]
    for candidate_id in ("BA2", "BA3", "BA4", "BA5", "BA6", "BA7"):
        assert "Deferred" in rows[candidate_id], (
            f"{candidate_id} must remain deferred until its recorded trigger fires"
        )


def test_external_adoption_case_study_links_baton_record():
    text = _read(CASE_STUDIES)
    row = next(line for line in text.splitlines() if "| Baton / `baton-dispatch`" in line)
    assert "[survey](baton-dispatch-survey-2026-07-13.md)" in row
    assert "no TeaPrompt skill, lens, verifier, dependency, or runtime adoption" in row
    assert "| Baton no-change outcome recorded | done |" in text
