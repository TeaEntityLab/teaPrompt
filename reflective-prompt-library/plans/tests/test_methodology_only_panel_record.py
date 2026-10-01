"""Guard the methodology-only rethink panel record and its adopted wording.

The 2026-10-01 panel kept the non-goal (no shipped runtime/runner) but amended
two authoritative texts: the Standing Non-Goals bullet gained an owner-sentence
condition, a bounded CI-fixture clause, and a reachable falsifier; the adoption
lesson gained an inquiry-vs-owner-sentence authority rule; AGENTS.md gained the
"distributed/user-facing runner" phrasing. This test pins those adopted
sentences; interpretive prose is not pinned.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

ROOT = PROMPT_LIBRARY_ROOT
RECORD = ROOT / "plans" / "methodology-only-rethink-panel-2026-10-01.md"
PK = ROOT / "PROJECT_KNOWLEDGE.md"
AGENTS = ROOT / "06-repo" / "AGENTS.md"

MR_IDS = [f"MR-{i}" for i in range(1, 7)]

# Adopted wording that must survive verbatim at exactly one surface each.
ADOPTED = {
    PK: (
        "must never be exported, published, or promoted into a host execution layer",
        "falsified if \u22653 documented real-world host-agent executions",
    ),
    AGENTS: (
        "multi-agent runtime or any distributed/user-facing runner",
        "author-side extracted-template test harnesses stay developer-only CI fixtures",
    ),
}


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_record_headings_and_verdict():
    text = _read(RECORD)
    for heading in ("## Shared Findings", "## Disagreements / Residual Risks",
                    "## Required Wording Changes", "## Candidate Adoption Ledger",
                    "## Evidence Actually Checked", "## Falsifiability"):
        assert heading in text, f"missing {heading}"
    assert "AGREE WITH CHANGES" in text


def test_all_candidates_have_dispositions():
    text = _read(RECORD)
    for mid in MR_IDS:
        row = re.search(rf"\|\s*{mid}\s*\|[^|]+\|\s*([A-Za-z]+)", text)
        assert row, f"{mid} missing"
        assert row.group(1) in {"Adopted", "Deferred", "Rejected"}, f"{mid}: {row.group(1)}"


def test_adopted_wording_at_exactly_one_surface():
    for path, sentences in ADOPTED.items():
        text = _read(path)
        for s in sentences:
            assert text.count(s) == 1, f"{path.name} lost or duplicated: {s[:60]!r}"


def test_owner_sentence_and_falsifier_pins():
    pk = _read(PK)
    assert "explicit human owner sentence" in pk
    assert "inquiry or rethink prompt authorizes evaluation, not revision" in pk
    # The posture itself still forbids shipping a runtime.
    assert "does not operate or ship its own multi-agent runtime" in pk
