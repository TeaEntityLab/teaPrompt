"""Guard the MiniMax Code trace-map survey's identity, tallies, dispositions,
and index links.

Record: plans/minimax-code-trace-map-survey-2026-09-19.md — mechanical
verification of a pasted zh-TW file:line-anchored code map (35 claims) against
the pinned repository revision. Record-only. The clean-room vocabulary for
this project is enforced by test_minimax_code_survey_record.py; duplicating
the identical regex against the same surfaces here would be weightless.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "minimax-code-trace-map-survey-2026-09-19.md"
CASE_STUDIES = PLANS_DIR / "external-adoption-case-studies-2026-06-20.md"
PROJECT_KNOWLEDGE = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"
REPO_HEAD = "e3724a13d72d"
CANDIDATE_STATUS = {
    "TM-1": "No change 2026-09-19",
    "TM-2": "No change 2026-09-19",
    "TM-3": "No change 2026-09-19",
    "TM-4": "No change 2026-09-19",
    "TM-5": "Noted 2026-09-19",
    "TM-6": "Noted 2026-09-19",
}


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_record_preserves_identity_and_tallies():
    text = _read(RECORD)
    assert REPO_HEAD in text
    assert "35" in text and "29" in text
    assert "Zero fabricated claims" in text
    assert "uniform +2" in text  # the systematic README offset
    assert "claimed 205, actual 209" in text  # the one far anchor
    assert "ternary" in text  # the 6d paraphrase diagnosis
    assert "without HTTP or RPC envelopes" in text  # boundary comment verbatim
    assert "Zero IO" in text  # contract-core header verbatim
    for heading in (
        "## Research Question",
        "## Direct Recommendation",
        "## Verification Results",
        "## Concept Map",
        "## Candidate Adoption Ledger",
        "## Evidence vs Inference",
        "## Falsifiability",
        "## Completion Ledger",
    ):
        assert heading in text, f"record missing {heading!r}"
    concepts = re.findall(r"^\| (C\d+) \|", text, re.M)
    assert concepts == [f"C{i}" for i in range(1, 7)]


def test_candidate_ledger_preserves_dispositions():
    text = _read(RECORD)
    rows = re.findall(r"^\| (TM-\d+) \|.*?\| (\S[^|]*?\d{4}-\d{2}-\d{2}[^|]*?) \|", text, re.M)
    found = {cid: status.strip() for cid, status in rows}
    assert set(found) == set(CANDIDATE_STATUS), f"ledger rows drifted: {sorted(found)}"
    for cid, want in CANDIDATE_STATUS.items():
        got = found[cid]
        assert got.startswith(want.split()[0]), f"{cid}: {got!r} lost {want!r}"
        assert want.split()[1] in got, f"{cid}: {got!r} lost its date"
    tm5 = [r for r in text.splitlines() if r.startswith("| TM-5 |")]
    assert tm5 and "not for the verify pipeline" in tm5[0], (
        "TM-5 must keep the upgrade's bound: architecture slice only"
    )


def test_existing_indexes_link_the_survey_decision():
    knowledge = _read(PROJECT_KNOWLEDGE).split("## Decision Index", 1)[1]
    assert "minimax-code-trace-map-survey-2026-09-19" in knowledge
    cases = _read(CASE_STUDIES)
    assert "minimax-code-trace-map-survey-2026-09-19" in cases
    index = _read(PROMPT_LIBRARY_ROOT / "index.json")
    assert "minimax-code-trace-map-survey-2026-09-19" in index
