"""Guard the Code Recall survey's evidence, dispositions, and cross-link."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "code-recall-survey-2026-08-20.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
TARGET_COMMIT = "116512be98ce6ee8b8a4ba190ca229e99b42515b"
PACKET_SHA256 = "277f6e544ade938170463b7eae5bb1dddaf1a731b1763f2e4ed1394d8afc4c95"
TAG_COMMIT = "03f09e7ad45783f13dc23c0a434d0f222a8a3b34"
NPM_GITHEAD = "81f0bb188c03ea06629e64656faa015606d08cbc"


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
    for candidate_id in ("CR-1", "CR-2", "CR-3", "CR-4", "CR-5", "CR-6"):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_survey_shape_revision_and_panel_consensus():
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
    assert TAG_COMMIT in text
    assert NPM_GITHEAD in text
    assert "unanimous, **7 of 7 lens verdicts**" in text
    assert "usability lens additionally dissents on *general*" in text
    assert "Five scout yields were schema-coerced" in text


def test_record_pins_executed_evidence_and_claim_boundaries():
    text = _read(RECORD)
    for evidence in (
        "93/93",
        "deleted the external target",
        "removes ONLY our entries",
        "false success without `TASK.md`",
        "forged extra entries",
        "`expires: today` stayed current",
        "excluded from the npm `files` allowlist",
        "cross-project race",
        "rk_live_",
        "mysql://",
    ):
        assert evidence in text, f"load-bearing evidence drifted: {evidence!r}"
    # Version split is identity, not divergent behavior.
    assert "identity, not\n  behavior" in text or "identity, not behavior" in text
    # Efficacy remains unproven.
    assert "No efficacy evidence" in text


def test_use_case_rows_block_adoption_and_deployment():
    text = _read(RECORD)
    assert "| `adopt` the runtime (hooks/MCP/installers/ledger) | **no**" in text
    assert "environments | **blocked at this revision**" in text
    assert (
        "No candidate created or changed a TeaPrompt skill, lens, verifier, dependency,\n"
        "runtime, or project-knowledge rule." in text
    )


def test_candidate_ledger_preserves_all_dispositions():
    rows = _ledger_rows()
    for candidate_id in ("CR-1", "CR-2", "CR-4"):
        assert "Deferred / study-only 2026-08-20" in rows[candidate_id]
    assert "No change 2026-08-20" in rows["CR-3"]
    assert "Rejected; deployment blocked 2026-08-20" in rows["CR-5"]
    assert "Rejected 2026-08-20" in rows["CR-6"]
    assert "file→decision advisory" in rows["CR-1"]
    assert "staleness lifecycle" in rows["CR-2"]
    assert "status-weighted retrieval" in rows["CR-3"]
    assert "receipt discipline" in rows["CR-4"]
    assert "persistent-memory runtime" in rows["CR-5"]
    assert "the ledger wins" in rows["CR-6"]


def test_external_adoption_case_study_links_survey_record():
    text = _read(CASE_STUDIES)
    assert "[survey](code-recall-survey-2026-08-20.md)" in text
    assert "Code Recall `@erikhuang/coderecall` 2.10.0" in text
    assert "| Code Recall survey outcome recorded | done |" in text
