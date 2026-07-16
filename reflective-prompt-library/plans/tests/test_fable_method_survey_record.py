"""Guard the fable-method survey's durable dispositions and cross-link."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "fable-method-survey-2026-07-16.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PINNED_COMMIT = "88b5cf36b10ee3679e08ee0f0181b9774d481508"


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
    for candidate_id in ("FM1", "FM2", "FM3", "FM4"):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_fable_method_survey_record_shape_and_revision():
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
        assert heading in text, f"fable-method survey missing {heading!r}"
    assert PINNED_COMMIT in text
    assert "`v1.4.0`" in text
    assert "| `adopt` into TeaPrompt | **deferred** |" in text
    assert "| `deploy` | **no** |" in text
    assert "AGREE WITH CHANGES` (7/7" in text


def test_fable_method_candidate_ledger_preserves_dispositions():
    rows = _ledger_rows()
    for candidate_id in ("FM1", "FM2", "FM3"):
        assert "Deferred" in rows[candidate_id], (
            f"{candidate_id} must remain deferred until its recorded trigger fires"
        )
    assert "Rejected 2026-07-16" in rows["FM4"], (
        "FM4 (parallel-skill install) was rejected; re-litigation requires its recorded trigger"
    )
    assert "same-harness reproduction" in rows["FM1"]
    assert "reflective-risk" in rows["FM2"]
    assert "deterministic anchor" in rows["FM3"] or "deterministic floor" in rows["FM3"]


def test_external_adoption_case_study_links_fable_method_record():
    text = _read(CASE_STUDIES)
    row = next(
        line for line in text.splitlines() if "| fable-method v1.4.0 |" in line
    )
    assert "[survey](fable-method-survey-2026-07-16.md)" in row
    assert "no TeaPrompt skill, lens, verifier, dependency, or runtime adoption" in row
    assert "| fable-method survey outcome recorded | done |" in text
