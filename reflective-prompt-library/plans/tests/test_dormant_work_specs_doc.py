"""Self-guard for the dormant-work spec book and checkpoint runbook.

The spec book exists to reduce trigger archaeology, but an incomplete or stale
register would create false confidence. These tests guard:
  - roadmap queue -> spec coverage,
  - uniform per-item fields (trigger, acceptance, tests, non-adoption),
  - rejected-item reopen preconditions,
  - explicit non-authority / evidence-tier boundaries,
  - bidirectional runbook links.

They check structure and coverage, not prose wording or adoption outcomes.
"""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import PROMPT_LIBRARY_ROOT  # noqa: E402

PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"
SPEC = PLANS_DIR / "dormant-work-specs-2026-07-11.md"
RUNBOOK = PLANS_DIR / "checkpoint-2026-10-11-runbook.md"
ROADMAP = PLANS_DIR / "whole-project-roadmap-2026-07-11.md"

QUEUE_SECTIONS = (
    "P6 — pack merge re-litigation",
    "T2 — zh-TW cheatsheet domain-pack appendix parity",
    "P12 — Conductor-style DAG executor template",
    "P13 — dedicated multi-wave ReMoM template",
    "M4 — ephemeral-source internalization deltas",
    "M5 — managed-skill re-audit",
    "M6 — README",
    "M7 — redaction methodology",
    "E2 — archive restructuring",
    "D4 — record-hygiene lint",
    "Writer-critic deterministic companion check",
    "`reflective-implement` default-invokes `reflective-minimality`",
    "Localized trigger cues beyond cheatsheet/glossary",
    "S3 — distribution packaging",
    "H3/H4 — deferred holdout groups",
)

REJECTED_PRECONDITION_SECTIONS = (
    "N8 — meta:product ratio",
    "M8 — blanket other-project skill promotion",
)

ROADMAP_QUEUE_TOKENS = (
    "E2",
    "reflective-implement` default-invokes `reflective-minimality",
    "Localized trigger cues beyond cheatsheet/glossary",
)

ROADMAP_ADOPTED_20260712_TOKENS = (
    "P12",
    "P13",
    "M4",
    "M6",
    "M7",
    "D4",
    "Writer-critic deterministic companion",
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _section(text: str, heading_prefix: str) -> str:
    pattern = re.compile(
        rf"^###\s+{re.escape(heading_prefix)}[^\n]*\n(.*?)(?=^###\s+|^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    assert match, f"spec book missing section starting {heading_prefix!r}"
    return match.group(1)


def test_spec_book_contract_shape():
    text = _read(SPEC)
    for heading in (
        "## Why",
        "## Scope",
        "## How the register hangs together (inference)",
        "## Spec template",
        "## Date-gated items (Horizon 2)",
        "## Trigger-gated queue (Horizon 3)",
        "## Rejected items — precondition specs (do not re-litigate without these)",
        "## New deterministic guards (what the four test files defend)",
        "## Risks",
        "## Falsifiability (retirement/staleness triggers for this book)",
        "## Verification (this change)",
    ):
        assert heading in text, f"spec book missing {heading!r}"


def test_spec_book_declares_non_authority_and_non_adoption():
    preamble = _read(SPEC).split("## Why", 1)[0]
    assert "non-authoritative" in preamble.lower()
    assert "NOT adoption" in preamble
    assert "a fired trigger authorizes re-litigation, not silent" in preamble
    assert "owning record" in preamble and "record wins" in preamble


@pytest.mark.parametrize("heading", QUEUE_SECTIONS)
def test_each_queue_spec_has_reviewable_fields(heading: str):
    body = _section(_read(SPEC), heading)
    for field in (
        "**Status:**",
        "**Owning record:**",
        "**Trigger",
        "**Draft acceptance criteria:**",
        "**Test plan:**",
        "**Non-adoption note:**",
    ):
        assert field in body, f"{heading!r} missing review field {field!r}"
    assert "this spec prepares re-litigation; it decides nothing" in body

def test_p7_resolved_section_points_to_successor_decision():
    body = _section(_read(SPEC), "P7 — pack trigger phrases in core router")
    for field in (
        "**Status:**",
        "**Successor record:**",
        "**Evidence:**",
        "**Decision:**",
        "**Structural guard:**",
        "**Re-open trigger:**",
    ):
        assert field in body, f"resolved P7 section missing {field!r}"
    assert "p7-pack-routing-decision-2026-07-11.md" in body

    roadmap = _read(ROADMAP)
    closed = roadmap.split("## Rejected — do not re-litigate without new evidence", 1)[1]
    assert "P7/N12 pack routing integration" in closed
    assert "no-change decided 2026-07-11" in closed


@pytest.mark.parametrize("heading", REJECTED_PRECONDITION_SECTIONS)
def test_rejected_items_have_reopen_preconditions(heading: str):
    body = _section(_read(SPEC), heading)
    assert "**Owning record:**" in body
    assert "**Reopen bar (verbatim):**" in body
    assert "**Precondition spec:**" in body
    assert "**Test plan:**" in body


def test_roadmap_horizon3_queue_is_covered_by_specs():
    roadmap = _read(ROADMAP)
    horizon3 = roadmap.split("## Horizon 3", 1)[1].split("\n## ", 1)[0]
    specs = _read(SPEC)
    for token in ROADMAP_QUEUE_TOKENS:
        assert token in horizon3, f"expected roadmap queue token vanished: {token!r}"
        normalized = token.replace(" / N12", "")
        assert normalized in specs, (
            f"roadmap queue token {token!r} has no corresponding spec section"
        )

def test_roadmap_user_directed_adoptions_are_covered_by_specs():
    roadmap = _read(ROADMAP)
    adopted = roadmap.split("### Adopted 2026-07-12", 1)[1].split("### Still trigger-gated", 1)[0]
    specs = _read(SPEC)
    for token in ROADMAP_ADOPTED_20260712_TOKENS:
        assert token in adopted, f"expected adopted token vanished: {token!r}"
        assert token in specs or token.replace("Writer-critic deterministic companion", "Writer-critic deterministic companion check") in specs


def test_date_and_event_gated_siblings_are_covered():
    roadmap = _read(ROADMAP)
    horizon2 = roadmap.split("## Horizon 2", 1)[1].split("\n## ", 1)[0]
    specs = _read(SPEC)
    for token in ("P6 / N11", "T2 stability check", "M5 managed-skill re-audit"):
        assert token in horizon2
    for token in ("### P6", "### T2", "### M5"):
        assert token in specs


def test_domain_plan_only_dormant_items_are_explained():
    specs = _read(SPEC)
    # These intentionally sit outside the whole-project Horizon 3 table but are
    # still dormant in their domain plans; documenting that distinction avoids
    # the false inference that the roadmap silently adopted or forgot them.
    for token, source in (
        ("### S3", "skills-surface-plan-2026-07-11.md"),
        ("### H3/H4", "routing-holdout-plan-2026-07-11.md"),
    ):
        assert token in specs and source in specs


def test_guard_inventory_matches_files_on_disk():
    text = _read(SPEC)
    named = (
        "test_dormant_item_watch.py",
        "test_dormant_conditional_contracts.py",
        "test_checkpoint_2026_10_11.py",
        "test_dormant_work_specs_doc.py",
    )
    for name in named:
        assert name in text, f"spec guard inventory lost {name!r}"
        assert (PLANS_DIR / "tests" / name).is_file(), f"documented guard missing: {name}"
    assert "regression guard" in text.lower()
    assert re.search(r'never\s+"triggers cannot fire unnoticed"', text)


def test_runbook_and_spec_are_bidirectionally_linked():
    spec = _read(SPEC)
    runbook = _read(RUNBOOK)
    assert "checkpoint-2026-10-11-runbook.md" in spec
    assert "dormant-work-specs-2026-07-11.md" in runbook


def test_runbook_outcome_contract_matches_deadman_test():
    runbook = _read(RUNBOOK)
    test_text = _read(PLANS_DIR / "tests" / "test_checkpoint_2026_10_11.py")
    outcome = "checkpoint-2026-10-11-outcome.md"
    assert outcome in runbook and outcome in test_text
    for heading in (
        "## P6 outcome",
        "## T2 decision",
        "## F4 re-check",
        "## Roadmap self-review",
        "## Ledger and index updates",
    ):
        assert heading in runbook and heading in test_text


def test_spec_retirement_trigger_prevents_archive_ossification():
    section = _read(SPEC).split(
        "## Falsifiability (retirement/staleness triggers for this book)", 1
    )[1]
    assert "two consecutive checkpoints" in section
    assert "retire" in section.lower()
    assert "roadmap's queue gains an item with no section" in section
