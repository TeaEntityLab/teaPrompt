"""Guard the agentflow survey record (record-only outcome).

Adopted rows: none. Per GLOSSARY Adoption Guard Closure, record-only and
rejected rows are guarded for ledger presence and disposition only. The guard
also pins the negative space: no TeaPrompt skill surface may carry agentflow
vocabulary, incident citations, a fixed worker-start ceiling, or an install
pointer to the surveyed repository.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT, library_skills_dir  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "agentflow-survey-2026-09-05.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
INSTALL_GUIDE = PROMPT_LIBRARY_ROOT / "SKILL_INSTALLATION.md"
PINNED_COMMIT = "b2935f5381d6469243440e080b43d0092a591663"
PACKET_SHA256 = "2b95cecfc40b0ac7320082355167867659ed71927f8a8557852f5200164116c2"
REPO_REVISION = "2d61cf836eedd9492ae7fcd2e6762bf094a36849"
FOREIGN_TOKENS = re.compile(
    r"agentflow|agfnow|\bI-0\d\d\b|external-runner-v1|devlog\.md|godev|"
    r"three total worker starts|at most three (worker )?starts"
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _ledger_rows() -> dict[str, str]:
    ledger = _read(RECORD).split("## Candidate Adoption Ledger", 1)[1].split(
        "## Evidence Used", 1
    )[0]
    return {
        candidate_id: next(
            line for line in ledger.splitlines() if line.startswith(f"| {candidate_id} |")
        )
        for candidate_id in (f"AF-{n}" for n in range(1, 19))
    }


def test_record_shape_identity_and_unanimity():
    text = _read(RECORD)
    for heading in (
        "## Research Question",
        "## Direct Recommendation (as of 2026-09-05)",
        "## Panel Consensus",
        "## Required Wording Changes (final)",
        "## Findings",
        "### Evidence-tier findings (Evidence Auditor corrections to the packet)",
        "## Comparisons",
        "## Socratic Questions and Disposition",
        "## Disagreements / Residual Risks",
        "## Candidate Adoption Ledger",
        "## Evidence Used (external source ledger)",
        "## Evidence vs Inference",
        "## Risks / Unknowns",
        "## Reproduction Contracts (host-only; not run)",
        "## Evidence Actually Checked",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"survey record missing {heading!r}"
    for identity in (PINNED_COMMIT, PACKET_SHA256, REPO_REVISION):
        assert identity in text, f"survey identity drifted: {identity}"
    assert "`AGREE` **7 of 7** (record-only)" in text
    assert "**Reason tally" in text and "verdict split and reason split coincide" in text
    assert "no provider persona or model routing is claimed" in text
    assert "## Required Wording Changes (final)\n\n**None.**" in text


def test_direct_recommendation_and_relation():
    text = _read(RECORD)
    answer = text.split("## Direct Recommendation (as of 2026-09-05)", 1)[1].split(
        "## Panel Consensus", 1
    )[0]
    assert "**peer methodology with an attached host harness**" in answer
    assert "not a TeaPrompt competitor and not a TeaPrompt host" in answer
    assert "the clone is not an OS sandbox" in answer
    assert "18 of 73 incidents cited inline" in answer
    assert "Read as evidence for the Durable Lesson" in answer


def test_evidence_corrections_are_preserved_not_upgraded():
    text = _read(RECORD)
    for correction in (
        "**Inline citation coverage is 18/73**",
        "not a green release signal",
        "**Dangling load rule.**",
        "`[yyyy] [name of copyright owner]` placeholder unfilled",
        "three squashed release commits",
    ):
        assert correction in text, correction
    inference = text.split("## Evidence vs Inference", 1)[1].split("## Risks / Unknowns", 1)[0]
    assert "898 tests / 889 pass / 9 fail" in inference
    assert "exclusively the `release.test.js` ENOENT cascade" in inference


def test_ledger_dispositions():
    rows = _ledger_rows()
    for record_only in ("AF-1", "AF-2", "AF-4", "AF-5", "AF-7", "AF-8", "AF-11"):
        assert "**Record-only" in rows[record_only], record_only
    for no_change in ("AF-3", "AF-12", "AF-13", "AF-18"):
        assert "**No change** 2026-09-05" in rows[no_change], no_change
    for rejected in ("AF-9", "AF-10", "AF-14"):
        assert "**Rejected** 2026-09-05" in rows[rejected], rejected
    assert "ATT-7" in rows["AF-9"]
    assert "Standing Non-Goal" in rows["AF-14"]
    assert "**Record-only; rejected as skill**" in rows["AF-6"]
    assert "**Record-only, author-claimed**" in rows["AF-15"]
    assert "**Record-only (agentflow defect)**" in rows["AF-16"]
    assert "**Rejected as install path**" in rows["AF-17"]
    assert "Never add to TeaPrompt install docs" in rows["AF-17"]


def test_no_surveyed_vocabulary_on_skill_or_install_surfaces():
    for path in list(library_skills_dir().glob("*/SKILL.md")) + [INSTALL_GUIDE]:
        assert not FOREIGN_TOKENS.search(path.read_text(encoding="utf-8")), path.name


def test_indexes_point_to_the_record():
    knowledge = _read(PROJECT_KNOWLEDGE)
    decision = next(
        line
        for line in knowledge.splitlines()
        if line.startswith("- 2026-09-05 agentflow survey")
    )
    for token in (
        "peer methodology with an attached host harness",
        "`AGREE` 7 of 7",
        "record-only",
        "18 of 73",
        "[record](plans/agentflow-survey-2026-09-05.md)",
    ):
        assert token in decision, f"decision index lost {token!r}"

    case_studies = _read(CASE_STUDIES)
    assert "| 2026-09-05 | agentflow (agfnow/agentflow @ `b2935f5`)" in case_studies
    assert "[survey](agentflow-survey-2026-09-05.md)" in case_studies
    assert "| agentflow survey recorded (record-only; findings and comparisons) | done |" in case_studies
