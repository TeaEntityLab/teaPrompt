"""Guard the handover-docs survey record (2026-09-23) at its surfaces."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS / "handover-docs-survey-2026-09-23.md"
PK = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

# Decision content the record must keep — the five adopted principles and the
# sensitive-keyword audit result.
REQUIRED = (
    "contract-layer vs implementation-layer",
    "快照日期",
    "無停止力的警告等於不存在",
    "no credentials, hosts, or real values",
    "Candidate Adoption Ledger",
    "Falsifiability",
    "HD-1",
    "HD-9",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def test_record_exists_with_required_content():
    text = _read(RECORD)
    for needle in REQUIRED:
        assert needle in text, f"record lost {needle!r}"


def test_record_status_is_record_only():
    text = _read(RECORD)
    assert "**Status: decided — record-only" in text


def test_pk_lesson_exists_and_references_record():
    pk = _read(PK)
    assert "Handover documentation separates contract from implementation" in pk
    assert "handover-docs-survey-2026-09-23.md" in pk
    assert "Review trigger" in pk


def test_no_sensitive_values_in_record():
    # The kit is all placeholders; the record must not invent or embed any
    # credential-shaped content.
    text = _read(RECORD).lower()
    for forbidden in ("password", "secret_key", "api_key=", "bearer ", "-----begin"):
        assert forbidden not in text, f"record contains sensitive-shaped token {forbidden!r}"
