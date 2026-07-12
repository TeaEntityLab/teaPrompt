"""Negative + positive tests for validate_record_hygiene.py (D4).

Each hygiene check must fire on a synthetic bad record and pass on a good one,
and the live repository corpus must validate clean.
"""

import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_record_hygiene import ADOPTION_DATE, check_record, record_date, main  # noqa: E402

GOOD = """\
# Example Decision Record — 2026-07-12

> **Status: decided (non-authoritative).** Example record for hygiene tests.

## Decision

Do the thing.

## Evidence Actually Checked

- Read the relevant files this session.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Trigger |
| --- | --- | --- | --- | --- |
| X1 | example | Adopted 2026-07-12 | this record | none |

## Falsifiability

Wrong if the thing was not needed.
"""


def _write(tmp_path: Path, name: str, text: str) -> Path:
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return p


def test_good_record_passes(tmp_path):
    errors, warnings = check_record(_write(tmp_path, "good-2026-07-12.md", GOOD))
    assert errors == [], errors


def test_missing_status_banner_fails(tmp_path):
    bad = GOOD.replace("> **Status: decided (non-authoritative).** Example record for hygiene tests.\n", "")
    errors, _ = check_record(_write(tmp_path, "bad-2026-07-12.md", bad))
    assert any("status banner" in e for e in errors)


def test_missing_evidence_and_inference_fails(tmp_path):
    bad = GOOD.replace("## Evidence Actually Checked", "## Notes")
    errors, _ = check_record(_write(tmp_path, "bad-2026-07-12.md", bad))
    assert any("evidence-separation" in e for e in errors)


def test_inference_label_satisfies_evidence_rule(tmp_path):
    bad = GOOD.replace("## Evidence Actually Checked", "## Notes")
    bad = bad.replace("Do the thing.", "Do the thing. [INFERENCE]")
    errors, _ = check_record(_write(tmp_path, "ok-2026-07-12.md", bad))
    assert not any("evidence-separation" in e for e in errors)


def test_missing_falsifiability_fails(tmp_path):
    bad = GOOD.replace("## Falsifiability\n\nWrong if the thing was not needed.\n", "")
    errors, _ = check_record(_write(tmp_path, "bad-2026-07-12.md", bad))
    assert any("Falsifiability" in e for e in errors)


def test_candidates_without_ledger_fails(tmp_path):
    bad = GOOD.replace("## Candidate Adoption Ledger", "## Candidate list")
    errors, _ = check_record(_write(tmp_path, "bad-2026-07-12.md", bad))
    assert any("Candidate Adoption Ledger" in e for e in errors)


def test_external_claim_without_date_warns(tmp_path):
    bad = GOOD.replace("Do the thing.", "Do the thing. See https://example.com/spec for detail.")
    _, warnings = check_record(_write(tmp_path, "warn-2026-07-12.md", bad))
    assert any("access date" in w for w in warnings)


def test_external_claim_with_date_is_clean(tmp_path):
    ok = GOOD.replace(
        "Do the thing.",
        "Do the thing. See https://example.com/spec (checked 2026-07-12).",
    )
    _, warnings = check_record(_write(tmp_path, "ok-2026-07-12.md", ok))
    assert not any("access date" in w for w in warnings)


def test_record_date_parsing():
    assert record_date(Path("x-2026-07-12.md")) == date(2026, 7, 12)
    assert record_date(Path("no-date.md")) is None


def test_historical_records_are_out_of_scope():
    assert date(2026, 6, 25) < ADOPTION_DATE  # older panel records not enforced


def test_live_repo_record_hygiene_passes():
    assert main() == 0
