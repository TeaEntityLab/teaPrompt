"""Guard the fable-method survey's dispositions, cross-link, and adopted wording."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "fable-method-survey-2026-07-16.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
IMPLEMENT_SKILL = PROMPT_LIBRARY_ROOT / "skills" / "reflective-implement" / "SKILL.md"
RISK_SKILL = PROMPT_LIBRARY_ROOT / "skills" / "reflective-risk" / "SKILL.md"
PINNED_COMMIT = "88b5cf36b10ee3679e08ee0f0181b9774d481508"


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    text = _read(RECORD)
    ledger = text.split("## Candidate Adoption Ledger", 1)[1].split(
        "## Local Reproduction",
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
        "## Local Reproduction — 2026-07-16 (FM1/FM2 gate)",
        "## Shared Findings",
        "## Evidence vs Inference",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
    ):
        assert heading in text, f"fable-method survey missing {heading!r}"
    assert PINNED_COMMIT in text
    assert "`v1.4.0`" in text
    assert "| `adopt` into TeaPrompt | **partial — FM1/FM2 adopted 2026-07-16** |" in text
    assert "| `deploy` | **no** |" in text
    assert "AGREE WITH CHANGES` (7/7" in text


def test_fable_method_candidate_ledger_preserves_dispositions():
    rows = _ledger_rows()
    for candidate_id in ("FM1", "FM2"):
        assert "Adopted 2026-07-16" in rows[candidate_id], (
            f"{candidate_id} was adopted after the local reproduction; "
            "changing its status requires a superseding decision record"
        )
        assert "Weak-tier re-run" in rows[candidate_id] or "weak-tier re-run" in rows[candidate_id]
    assert "Deferred" in rows["FM3"], (
        "FM3 must remain deferred until its recorded trigger fires"
    )
    assert "Rejected 2026-07-16" in rows["FM4"], (
        "FM4 (parallel-skill install) was rejected; re-litigation requires its recorded trigger"
    )


def test_reproduction_results_recorded_deterministically():
    text = _read(RECORD)
    repro = text.split("## Local Reproduction", 1)[1].split("## Shared Findings", 1)[0]
    assert "| control ×3 | 1, 5, 5 (Σ 11) | 0/3 | 3/3 | 3/3 |" in repro
    assert "| treatment ×3 | 5, 5, 5 (Σ 15) | 3/3 | 3/3 | 3/3 |" in repro
    assert "| control ×3 | 3/3 | **3/3** | 0/3 | 0/3 |" in repro
    assert "| treatment ×3 | 3/3 | 0/3 | 3/3 | 3/3 |" in repro
    assert "pre-registered decision rule" in repro


def test_adopted_twin_sweep_wording_pinned_in_reflective_implement():
    text = _read(IMPLEMENT_SKILL)
    assert "Twin sweep, whenever a defect was fixed" in text
    assert 'TWINS: searched <pattern> - found <N> other sites: <files, or "none">' in text
    assert "plans/fable-method-survey-2026-07-16.md" in text


def test_adopted_authorization_gate_wording_pinned_in_reflective_risk():
    text = _read(RISK_SKILL)
    assert "Authorization gate for outward-facing actions" in text
    assert "Documentation is not authorization" in text
    assert "PENDING: <the action> - awaiting your authorization" in text
    assert "plans/fable-method-survey-2026-07-16.md" in text


def test_external_adoption_case_study_links_fable_method_record():
    text = _read(CASE_STUDIES)
    row = next(
        line for line in text.splitlines() if "| fable-method v1.4.0 |" in line
    )
    assert "[survey](fable-method-survey-2026-07-16.md)" in row
    assert "narrow wording repairs" in row
    assert "no new TeaPrompt skill, lens, verifier, dependency, or runtime surface" in row
    assert "| fable-method survey outcome recorded | done |" in text
    assert "| fable-method FM1/FM2 reproduction and adoption recorded | done |" in text
