"""Guard the prime-agent survey's dispositions and cross-link."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "prime-agent-survey-2026-08-06.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PRIME_AGENT_COMMIT = "c22549a37b73cc603c6f0d202517cb0ca856c7d3"


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
    for candidate_id in ("PA-1", "PA-2", "PA-3", "PA-4", "PA-5"):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_survey_record_shape_and_revision():
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
    assert PRIME_AGENT_COMMIT in text
    assert "`AGREE WITH CHANGES` (6 of 7 lens verdicts" in text


def test_survey_record_pins_load_bearing_findings():
    text = _read(RECORD)
    assert "62 passed, 2 failed" in text, "reproduction result must stay pinned"
    assert "No module named 'mcp'" in text, (
        "optional-dep-only failure classification must stay pinned"
    )
    assert "extension auto-load RCE" in text.lower() or "auto-load RCE" in text, (
        "extension auto-load blocker must stay pinned"
    )
    assert "harness.py:285-298" in text, "non-atomic write finding must stay pinned"
    assert "Python runtime tests omitted from CI" in text or (
        "Python tests absent from CI" in text
    ), "CI coverage gap must stay pinned"
    assert "config-persistence" in text, (
        "self-improving reframe must stay pinned"
    )


def test_survey_use_case_rows_block_adoption():
    text = _read(RECORD)
    assert "| `adopt` runtime as dependency | **no**" in text
    assert "| `deploy` (use as an agent on real work) | **blocked until fixed**" in text
    assert (
        "No candidate created a new TeaPrompt skill, lens, verifier, dependency, or\n"
        "runtime surface." in text
    )


def test_candidate_ledger_preserves_dispositions():
    rows = _ledger_rows()
    assert "Deferred 2026-08-06" in rows["PA-1"]
    assert "Deferred 2026-08-06" in rows["PA-2"]
    assert "Concept-only 2026-08-06" in rows["PA-3"]
    assert "Rejected 2026-08-06" in rows["PA-4"]
    assert "Blocked 2026-08-06" in rows["PA-5"]


def test_external_adoption_case_study_links_survey_record():
    text = _read(CASE_STUDIES)
    row = next(
        line
        for line in text.splitlines()
        if "| 2026-08-06 | Prime Agent v0.7.0 |" in line
    )
    assert "[survey](prime-agent-survey-2026-08-06.md)" in row
    assert "no TeaPrompt skill, lens, verifier, dependency, or runtime adoption" in row
    assert "| Prime Agent survey outcome recorded | done |" in text
