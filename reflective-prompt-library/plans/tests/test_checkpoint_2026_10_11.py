"""Evidence-base and deadman guards for the 2026-10-11 checkpoint.

The whole-project roadmap defines "the checkpoint passes undocumented" as a
falsifier. This module makes that falsifier executable without failing early:
  - before/on 2026-10-11, it guards the evidence base and runbook;
  - after 2026-10-11, it requires the outcome record;
  - whenever the outcome exists, it guards the record's structural contract.

This is a deterministic calendar/evidence guard, not a decision about P6, T2,
or F4. Owning decisions remain in their cited records.
"""

from datetime import date
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
CHECKPOINT = date(2026, 10, 11)
OUTCOME = PLANS_DIR / "checkpoint-2026-10-11-outcome.md"
RUNBOOK = PLANS_DIR / "checkpoint-2026-10-11-runbook.md"

REQUIRED_OUTCOME_HEADINGS = (
    "## P6 outcome",
    "## T2 decision",
    "## F4 re-check",
    "## Roadmap self-review",
    "## Ledger and index updates",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def checkpoint_is_overdue(today: date, outcome_exists: bool) -> bool:
    """Return true only after the checkpoint date with no outcome artifact.

    Kept pure so date-boundary behavior is directly testable; the real deadman
    call below passes date.today() and OUTCOME.exists().
    """
    return today > CHECKPOINT and not outcome_exists


@pytest.mark.parametrize(
    "today,outcome_exists,expected",
    [
        (date(2026, 10, 10), False, False),
        (date(2026, 10, 11), False, False),
        (date(2026, 10, 12), False, True),
        (date(2027, 1, 1), False, True),
        (date(2026, 10, 12), True, False),
    ],
)
def test_checkpoint_deadman_boundary(today, outcome_exists, expected):
    assert checkpoint_is_overdue(today, outcome_exists) is expected


def test_checkpoint_cannot_pass_undocumented():
    assert not checkpoint_is_overdue(date.today(), OUTCOME.exists()), (
        "the 2026-10-11 checkpoint has passed with no "
        "plans/checkpoint-2026-10-11-outcome.md; run "
        "plans/checkpoint-2026-10-11-runbook.md now. The roadmap names an "
        "undocumented checkpoint passage as a falsifier. Do not postpone by "
        "changing the date -- write the outcome record."
    )


def test_outcome_contract_when_record_exists():
    if not OUTCOME.exists():
        return  # valid only until/on the checkpoint date; deadman owns overdue
    text = _read(OUTCOME)
    for heading in REQUIRED_OUTCOME_HEADINGS:
        assert heading in text, f"checkpoint outcome missing {heading!r}"
    assert "2026-10-11" in text, "outcome must identify the checkpoint date"
    assert "PROJECT_KNOWLEDGE.md" in text, (
        "outcome's ledger/index section must show its Decision Index update"
    )


def test_usage_log_evidence_contract():
    text = _read(PLANS_DIR / "flow-pack-usage-log.md")
    for heading in ("## Convention", "## Entries", "## Review checkpoints"):
        assert heading in text, f"usage log missing {heading!r}"
    columns = "| Date | Skill | Host / context | Task shape | Outcome + evidence pointer |"
    assert text.count(columns) >= 2, (
        "usage log must publish the five-column schema at the convention and "
        "entry table; P6 consumes rows under that schema"
    )
    assert "Zero-state recorded 2026-07-11" in text
    assert "empty log means" in text and "unknown" in text.lower(), (
        "usage log lost the unknown-vs-zero caveat; P6 must not reinterpret "
        "missing telemetry as zero demand"
    )
    assert "2026-10-11" in text and "P6" in text




def test_demotion_evaluation_is_consumable_evidence():
    text = _read(PLANS_DIR / "flow-pack-demotion-evaluation-2026-07-11.md")
    for heading in ("## Decision", "## Ledger", "## Falsifiability"):
        assert heading in text, f"demotion evaluation missing {heading!r}"
    assert "not fired" in text.lower(), (
        "the checkpoint runbook assumes the 2026-07-11 F1 verdict is "
        "'not fired'; if a later record supersedes it, update the runbook and "
        "this evidence pointer together"
    )


def test_checkpoint_runbook_structure():
    text = _read(RUNBOOK)
    for heading in (
        "## Pre-checkpoint evidence checklist (run first, before any discussion)",
        "## Agenda item 1 — P6 / N11: pack merge re-litigation",
        "## Agenda item 2 — pack utility claims re-verification",
        "## Agenda item 3 — T2: zh-TW pack-appendix parity",
        "## Agenda item 4 — T4/F1 residue: F4 watch-table re-check",
        "## Agenda item 5 — roadmap self-review",
        "## Outcome record contract (`plans/checkpoint-2026-10-11-outcome.md`)",
        "## Falsifiability (this runbook)",
    ):
        assert heading in text, f"checkpoint runbook missing {heading!r}"
    for source in (
        "flow-pack-usage-log.md",
        "flow-pack-demotion-evaluation-2026-07-11.md",
        "flow-control-roadmap-2026-07-11.md",
        "whole-project-plan-2026-07-11.md",
        "PROJECT_KNOWLEDGE.md",
        "dormant-work-specs-2026-07-11.md",
    ):
        assert source in text, f"checkpoint runbook lost source {source!r}"


def test_horizon2_agenda_and_runbook_stay_in_parity():
    roadmap = _read(PLANS_DIR / "whole-project-roadmap-2026-07-11.md")
    horizon2 = roadmap.split("## Horizon 2", 1)[1].split("\n## ", 1)[0]
    runbook = _read(RUNBOOK)
    for token in (
        "P6 / N11",
        "Pack utility claims re-verification",
        "T2 stability check",
        "T4 / F1",
        "Roadmap self-review",
    ):
        assert token in horizon2, f"roadmap Horizon 2 lost agenda item {token!r}"
    for token in ("P6", "utility claims", "T2", "F4", "roadmap self-review"):
        assert token.lower() in runbook.lower(), (
            f"checkpoint runbook no longer covers Horizon 2 token {token!r}"
        )
