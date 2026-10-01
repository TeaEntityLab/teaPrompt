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


def _table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells[0] in {"Item", "Queue item"} or re.fullmatch(r"[-: ]+", cells[0]):
            continue
        rows.append(cells)
    return rows


def _assert_reviewable_rows(rows: list[list[str]]) -> None:
    for row in rows:
        assert len(row) == 3 and row[1], f"missing disposition for {row[0]!r}"
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", row[2])
        assert links, f"missing spec/owning-record pointer for {row[0]!r}"
        for target in links:
            path = target.split("#", 1)[0]
            assert not re.match(r"\w+://", path), "queue pointers must be repository-local"
            destination = SPEC.parent / path if path else SPEC
            assert destination.is_file(), target


def test_current_roadmap_queue_has_reviewable_coverage():
    roadmap = _read(ROADMAP)
    horizon2 = roadmap.split("## Horizon 2", 1)[1].split("\n## ", 1)[0]
    horizon3 = roadmap.split("### Still trigger-gated", 1)[1].split("\n## ", 1)[0]
    queue_rows = _table_rows(horizon2) + _table_rows(horizon3)
    assert queue_rows, "roadmap has no current queue rows to review"
    spec = _read(SPEC)
    coverage = spec.split("## Current queue coverage", 1)[1].split("\n## ", 1)[0]
    mapped_rows = _table_rows(coverage)
    queue_items = [row[0] for row in queue_rows]
    mapped_items = [row[0] for row in mapped_rows]
    assert len(queue_items) == len(set(queue_items)), "duplicate roadmap queue identity"
    assert len(mapped_items) == len(set(mapped_items)), "duplicate coverage identity"
    assert set(mapped_items) == set(queue_items), (
        f"missing coverage: {set(queue_items) - set(mapped_items)}; "
        f"stale coverage: {set(mapped_items) - set(queue_items)}"
    )
    _assert_reviewable_rows(mapped_rows)
    mapped_by_item = {row[0]: row for row in mapped_rows}
    for row in queue_rows:
        owner_paths = {
            target.split("#", 1)[0]
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", row[-1])
        }
        mapped_paths = {
            target.split("#", 1)[0]
            for target in re.findall(
                r"\[[^\]]+\]\(([^)]+)\)", mapped_by_item[row[0]][2]
            )
        }
        assert owner_paths and owner_paths <= mapped_paths, (
            f"coverage for {row[0]!r} lost owning pointers: {owner_paths - mapped_paths}"
        )


def test_roadmap_user_directed_adoptions_are_covered_by_specs():
    roadmap = _read(ROADMAP)
    adopted = roadmap.split("### Adopted 2026-07-12", 1)[1].split("### Still trigger-gated", 1)[0]
    specs = _read(SPEC)
    for token in ROADMAP_ADOPTED_20260712_TOKENS:
        assert token in adopted, f"expected adopted token vanished: {token!r}"
        assert token in specs or token.replace("Writer-critic deterministic companion", "Writer-critic deterministic companion check") in specs




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


def test_domain_dispositions_cover_current_skill_improvement_deferrals():
    source = _read(PLANS_DIR / "skill-improvement-plan-2026-07-24.md")
    ledger = source.split("## Candidate Adoption Ledger", 1)[1].split("\n## ", 1)[0]
    deferred = {
        row[0] for row in _table_rows(ledger)
        if row[0].startswith("WGS-") and row[2].startswith("Deferred")
    }
    spec = _read(SPEC)
    dispositions = spec.split("## Domain and retired-plan dispositions", 1)[1].split("\n## ", 1)[0]
    rows = _table_rows(dispositions)
    _assert_reviewable_rows(rows)
    mapped = {row[0] for row in rows if row[0].startswith("WGS-")}
    assert mapped == deferred, (
        f"missing domain disposition: {deferred - mapped}; "
        f"stale domain disposition: {mapped - deferred}"
    )


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
    from test_checkpoint_2026_10_11 import REQUIRED_OUTCOME_HEADINGS

    runbook = _read(RUNBOOK)
    for heading in REQUIRED_OUTCOME_HEADINGS:
        assert heading in runbook, f"runbook lost outcome field {heading!r}"


