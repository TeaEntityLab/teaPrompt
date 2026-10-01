"""Guard the Oh My OpenAgent 2026-10-01 re-survey's pin, dispositions, and
record-only boundary.

The survey corrects the stale "OpenCode plugin" identity (the repo pivoted to a
standalone senpi-based runtime) and records six candidate mechanisms as
record-only/covered. This test pins the record's identity anchors and the
no-adoption posture; interpretive prose is not pinned.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS_DIR / "oh-my-openagent-survey-2026-10-01.md"

CANDIDATE_IDS = [f"OO-{i}" for i in range(1, 7)]

PIN = "37659a4c15cdbb5e2eb10d21109ae42829bcf2cd"
TAG_TARGET = "89688165848b69121270682193b5ac2c175666de"

REQUIRED_HEADINGS = (
    "## Research Question",
    "## Direct Recommendation",
    "## Version / Date Context",
    "## Method and Evidence Actually Checked",
    "## Delta vs 2026-06-25 Record",
    "## Prompt-Text vs Enforced-Mechanism Map",
    "## Candidate Adoption Ledger",
    "## Falsifiability",
)


def _read() -> str:
    assert RECORD.is_file(), f"missing {RECORD}"
    return RECORD.read_text(encoding="utf-8")


def test_record_exists_with_required_headings():
    text = _read()
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"missing heading {heading!r}"


def test_pins_are_recorded():
    text = _read()
    assert PIN in text
    assert TAG_TARGET in text  # v5.1.7 tag differs from reviewed HEAD; must be explicit


def test_pivot_identity_and_license_recorded():
    text = _read()
    assert "senpi" in text and "pi-mono" in text
    assert "SUL-1.0" in text
    assert "standalone" in text.lower()


def test_all_candidates_have_a_disposition():
    text = _read()
    for cid in CANDIDATE_IDS:
        row = re.search(rf"\|\s*{re.escape(cid)}\s*\|[^|]+\|\s*(\w+)", text)
        assert row, f"{cid} missing from ledger"
        assert row.group(1) in {"Covered", "Recorded"}, f"{cid}: {row.group(1)}"


def test_record_only_no_adoption_claim():
    text = _read()
    assert "record-only" in text and "no adoption" in text
    # No candidate may claim an adopted status in this record.
    assert not re.search(r"\|\s*OO-\d\s*\|[^|]+\|\s*Adopted", text)
