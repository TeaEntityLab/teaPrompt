"""Guard the agnix + agent-skills-hook survey's dispositions and cross-link."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402


PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "agnix-agent-skills-hook-survey-2026-08-04.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
AGNIX_COMMIT = "572a860971a18c48c7a830eb00cb411d5b87dd3f"
SKILLS_HOOK_COMMIT = "116e26b85768277026e1b9646d3207451f21344b"


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
    for candidate_id in ("AX1", "AX2", "AX3", "SH1", "SH2"):
        rows[candidate_id] = next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
    return rows


def test_survey_record_shape_and_revisions():
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
    assert AGNIX_COMMIT in text
    assert SKILLS_HOOK_COMMIT in text
    assert "`AGREE WITH CHANGES` (5 of 6 delivered lens verdicts" in text
    assert "**63 skill directories**" in text, "panel-corrected skill count must stay pinned"


def test_survey_record_pins_load_bearing_findings():
    text = _read(RECORD)
    assert "5121" in text and "0 failed" in text, "reproduction result must stay pinned"
    assert "forbids redistribution" in text, "Anthropic license finding must stay pinned"
    assert "`[OMX]` origin markers stripped" in text or "`[OMX]` stripped" in text, (
        "OMX de-branding finding must stay pinned"
    )
    assert "0pp" in text, "Vercel misrepresentation finding must stay pinned"


def test_survey_use_case_rows_block_adoption():
    text = _read(RECORD)
    assert "| `adopt` into TeaPrompt | **no**" in text
    assert (
        "No candidate created a new TeaPrompt skill, lens, verifier, dependency, or\n"
        "runtime surface." in text
    )


def test_candidate_ledger_preserves_dispositions():
    rows = _ledger_rows()
    assert "Concept-only 2026-08-04" in rows["AX1"]
    assert "No-change 2026-08-04" in rows["AX2"]
    assert "Rejected 2026-08-04" in rows["AX3"]
    assert "Deferred" in rows["SH1"], "SH1 must remain deferred until its trigger fires"
    assert "Concept-only 2026-08-04" in rows["SH2"]


def test_external_adoption_case_study_links_survey_record():
    text = _read(CASE_STUDIES)
    row = next(
        line for line in text.splitlines() if "| 2026-08-04 | agnix v0.45.0 + agent-skills-hook |" in line
    )
    assert "[survey](agnix-agent-skills-hook-survey-2026-08-04.md)" in row
    assert "no TeaPrompt skill, lens, verifier, dependency, or runtime adoption" in row
    assert "| agnix + agent-skills-hook survey outcome recorded | done |" in text
