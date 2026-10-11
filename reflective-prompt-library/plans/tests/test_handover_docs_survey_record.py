"""Guard the handover-docs survey record (2026-09-23) at its surfaces."""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS = PROMPT_LIBRARY_ROOT / "plans"
RECORD = PLANS / "handover-docs-survey-2026-09-23.md"
PK = PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md"

# A bounded syntax screen for this record, not proof that arbitrary secrets or
# personal data are absent. Plain mentions of credential names are not values.
_CREDENTIAL_SHAPE = re.compile(
    r"""(?imx)
    \b(?:password|secret[_-]?key|api[_-]?key|(?:auth|access)[_-]?token)
    ["']?\s*[:=]\s*["']?[^\s"']
    | (?:\bauthorization\s*:\s*|^[ \t]*)bearer[ \t]+\S+
    | -----BEGIN[ ]+[A-Z0-9 ]+-----
    """
)

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


def test_record_contains_no_recognized_credential_shapes():
    assert not _CREDENTIAL_SHAPE.search(_read(RECORD)), (
        "record contains a credential assignment, bearer header or PEM boundary; "
        "human review is still required for unrecognized formats"
    )


@pytest.mark.parametrize("text, detected", [
    ('api_key: "SYNTHETIC-NOT-A-SECRET"', True),
    ('{"AUTH_TOKEN": "SYNTHETIC-NOT-A-SECRET"}', True),
    ("access-token=SYNTHETIC-NOT-A-SECRET", True),
    ("Authorization: Bearer SYNTHETIC-NOT-A-SECRET", True),
    ("Bearer SYNTHETIC-NOT-A-SECRET", True),
    ("-----BEGIN PRIVATE KEY-----", True),
    ("No password or secret_key values are recorded.", False),
    ("No bearer tokens are recorded.", False),
    ("api_key=\"\"", False),
])
def test_credential_shape_screen_distinguishes_values_from_mentions(text, detected):
    assert bool(_CREDENTIAL_SHAPE.search(text)) is detected
