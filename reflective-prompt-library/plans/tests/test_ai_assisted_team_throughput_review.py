"""Guard the AI-assisted team throughput review's evidence tiers and dispositions."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "ai-assisted-team-throughput-review-2026-08-12.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"


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
        "ATT-1",
        "ATT-2",
        "ATT-3",
        "ATT-4",
        "ATT-5",
        "ATT-6",
        "ATT-7",
        "ATT-8",
        "ATT-9",
    ):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_review_record_shape_and_panel_execution():
    text = _read(RECORD)
    for heading in (
        "## Panel Consensus",
        "## Required Wording Changes",
        "## Claims Ledger",
        "## Candidate Adoption Ledger",
        "## Shared Findings",
        "## Minimal Operating Playbook",
        "## Evidence vs Inference",
        "## Disagreements / Residual Risks",
        "## Evidence Actually Checked",
        "## Falsifiability",
    ):
        assert heading in text, f"review record missing {heading!r}"
    assert "> **Status: decided (non-authoritative).**" in text
    assert "`AGREE WITH CHANGES` (6 of 7 formal verdicts)" in text
    assert "All seven full deliverables were recovered by tier-1 DM-wake" in text


def test_record_preserves_evidence_tiers_and_citation_correction():
    text = _read(RECORD)
    assert text.count("`author-claimed`") >= 6
    assert "warning signal, not a controlled experiment" in text
    assert 'MIT found more than three parallel AI sessions cause "brain rot."' in text
    mit_row = next(line for line in text.splitlines() if line.startswith("| E3 |"))
    assert "`refuted`" in mit_row
    assert "survey association, not causal trial" in text


def test_candidate_ledger_preserves_adopted_and_deferred_scope():
    rows = _ledger_rows()
    for candidate_id in ("ATT-1", "ATT-2", "ATT-3"):
        assert "Adopted 2026-08-12" in rows[candidate_id]
    for candidate_id in ("ATT-4", "ATT-5", "ATT-9"):
        assert "Deferred 2026-08-12" in rows[candidate_id]
    assert "repeated local routing errors" in rows["ATT-4"]
    assert "local workflow repeatedly" in rows["ATT-5"]
    assert "three local recurrences" in rows["ATT-9"]


def test_candidate_ledger_rejects_unjustified_policy_and_runtime():
    rows = _ledger_rows()
    for candidate_id in ("ATT-6", "ATT-7", "ATT-8"):
        assert "Rejected 2026-08-12" in rows[candidate_id]
    assert "Universal two-session or two-retry rule" in rows["ATT-7"]
    assert "New coordinator agent, workflow skill, or TeaPrompt runtime" in rows["ATT-8"]


def test_external_adoption_case_study_links_review_record():
    text = _read(CASE_STUDIES)
    row = next(
        line
        for line in text.splitlines()
        if "| 2026-08-12 | AI-assisted team throughput / unlimited-token discussion |"
        in line
    )
    assert "[review](ai-assisted-team-throughput-review-2026-08-12.md)" in row
    assert "reject hard session/retry limits" in row
    assert "| AI-assisted team throughput review recorded | done |" in text
