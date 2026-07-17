"""Forward activation contracts for dormant roadmap items.

Each test is vacuously green while its item stays dormant and enforces the
item's structural contract the moment the dormant artifact appears -- so an
adoption cannot land silently half-done. This encodes queue discipline
(whole-project roadmap: "a fired trigger authorizes re-litigation, not silent
adoption") as executable checks:

  - the owning ledger row must move off bare "Deferred" (house precedent:
    the P15 row gained "**Resolved 2026-07-11:**" in place), and
  - the arriving artifact must satisfy the structural contract drafted in
    plans/dormant-work-specs-2026-07-11.md.

These are conditional guards, not adoption approvals: passing them never
substitutes for the record + human approval the owning gate requires.
"""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
    library_skills_dir,
)

REPO_ROOT = PROMPT_LIBRARY_ROOT.parent
PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"

GENERATOR = library_skills_dir() / "flow-control-generator" / "SKILL.md"
HARNESS = library_skills_dir() / "flow-loop-harness" / "SKILL.md"
RESEARCH_LEDGER = PLANS_DIR / "agent-flow-control-research-2026-07-11.md"
MANAGED_LEDGER = PLANS_DIR / "managed-skill-promotion-panel-record-2026-07-11.md"

PACK_NAMES = ("flow-control-generator", "flow-loop-harness")
RESOLUTION_TOKENS = ("Adopted", "Resolved", "Superseded", "Re-litigated")


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")

def _markdown_section(text: str, heading_pattern: str) -> str:
    heading = re.search(heading_pattern, text, re.MULTILINE)
    assert heading, f"missing markdown section matching {heading_pattern!r}"
    tail = text[heading.end():]
    next_heading = re.search(r"^##\s+", tail, re.MULTILINE)
    return tail[:next_heading.start()] if next_heading else tail


def _table_row(text: str, prefix: str) -> str:
    for line in text.splitlines():
        if line.startswith(prefix):
            return line
    raise AssertionError(f"ledger row {prefix!r} not found")


def _row_resolved(row: str) -> bool:
    """A deferred row counts as resolved once it carries a resolution token
    (in-place append is house convention, e.g. the P15 row)."""
    return any(token.lower() in row.lower() for token in RESOLUTION_TOKENS)


# ---------------------------------------------------------------------------
# T2 -- zh-TW cheatsheet pack appendix parity (activates when packs appear)
# ---------------------------------------------------------------------------


def test_t2_zh_tw_pack_appendix_parity_when_present():
    zh = _read(cheatsheet_zh_tw_path())
    if not any(pack in zh for pack in PACK_NAMES):
        return  # dormant: T2 waits for the EN-appendix stability gate

    en_section = _markdown_section(
        _read(cheatsheet_en_path()),
        r"^## Domain packs \(host-invoked; not core routing\)\s*$",
    )
    zh_section = _markdown_section(zh, r"^##\s+(?:領域包|Domain packs).*$")
    for pack in PACK_NAMES:
        assert pack in zh_section, f"zh-TW pack appendix landed without {pack!r}"
    assert "reflective-dispatch" in zh_section, (
        "zh-TW appendix must keep the dispatch-still-routes bullet"
    )

    en_bullets = [line for line in en_section.splitlines() if line.startswith("- ")]
    zh_bullets = [line for line in zh_section.splitlines() if line.startswith("- ")]
    assert len(en_bullets) == 4, "EN domain-pack appendix contract changed"
    assert len(zh_bullets) == len(en_bullets), (
        f"pack bullet count mismatch: EN {len(en_bullets)} vs zh-TW "
        f"{len(zh_bullets)}; parity requires all four bullets"
    )




# ---------------------------------------------------------------------------
# P12 / P13 -- new pack templates require their ledger rows to move
# ---------------------------------------------------------------------------


def test_p12_dag_template_requires_ledger_flip():
    headings = re.findall(r"^## Template: .+$", _read(GENERATOR), re.MULTILINE)
    dag = [h for h in headings if re.search(r"dag|dependency", h, re.IGNORECASE)]
    if not dag:
        return  # dormant: no DAG-shaped template exists
    row = _table_row(_read(RESEARCH_LEDGER), "| P12 |")
    assert _row_resolved(row), (
        f"a DAG template {dag} landed while the P12 ledger row still reads "
        f"{row!r}; the flow-coverage deferral requires an adoption record "
        "naming the firing local task (and the /batch caveat evaluated)"
    )


def test_p13_multiwave_template_requires_ledger_flip():
    headings = re.findall(r"^## Template: .+$", _read(HARNESS), re.MULTILINE)
    waves = [h for h in headings if re.search(r"multi-?wave|remom", h, re.IGNORECASE)]
    if not waves:
        return  # dormant: composition note remains the answer
    row = _table_row(_read(RESEARCH_LEDGER), "| P13 |")
    assert _row_resolved(row), (
        f"a multi-wave template {waves} landed while the P13 ledger row still "
        f"reads {row!r}; recurrence evidence + adoption record required"
    )


# ---------------------------------------------------------------------------
# M4 / M6 / M7 -- managed-skill deferrals (activate when destinations change)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "row_prefix,path,tokens,gate",
    [
        (
            "| M4 |",
            PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-acquisition.md",
            ("sentinel-fact", "ephemeral-source"),
            "third documented local occurrence",
        ),
        (
            "| M7 |",
            PROMPT_LIBRARY_ROOT / "04-agent" / "external-adoption-review.md",
            ("leakage", "packet hash"),
            "first TeaPrompt-local sensitive-evidence external review",
        ),
    ],
    ids=("M4", "M7"),
)
def test_lens_extension_requires_ledger_flip(row_prefix, path, tokens, gate):
    text = _read(path).lower()
    if not any(token in text for token in tokens):
        return  # dormant
    row = _table_row(_read(MANAGED_LEDGER), row_prefix)
    assert _row_resolved(row), (
        f"{path.name} gained {tokens} content while ledger row {row_prefix!r} "
        f"still reads {row!r}; the gate is: {gate}"
    )


def test_m6_readme_orientation_requires_ledger_flip():
    text = _read(REPO_ROOT / "README.md")
    if not re.search(r"^##\s+Orientation\s*$", text, re.MULTILINE):
        return  # dormant
    row = _table_row(_read(MANAGED_LEDGER), "| M6 |")
    assert _row_resolved(row), (
        "root README gained '## Orientation' while the M6 ledger row still "
        f"reads {row!r}; adoption requires the recurring-gap evidence"
    )


# ---------------------------------------------------------------------------
# D4 -- record-hygiene validator must arrive fully wired
# ---------------------------------------------------------------------------


def test_d4_validator_arrives_wired():
    hygiene = sorted(PLANS_DIR.glob("validate_record_hygiene*.py"))
    if not hygiene:
        return  # dormant: convention-only, per the rethink deferral
    makefile = _read(REPO_ROOT / "Makefile")
    assert hygiene[0].name in makefile, (
        f"{hygiene[0].name} exists but is not wired into the Makefile "
        "validate target; D4's spec requires validator + wiring + tests in "
        "one change (and the whole-project plan revised: composition change "
        "is its staleness trigger)"
    )
    covering = sorted((PLANS_DIR / "tests").glob("test_validate_record_hygiene*.py"))
    assert covering, (
        f"{hygiene[0].name} landed without a covering negative-test file; "
        "each check must be proven to fire on a synthetic bad record"
    )


# ---------------------------------------------------------------------------
# H3/H4 -- deferred fixture groups need a boundary rule first
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "group,rule_tokens",
    [
        ("scheduled_check_boundary_trap", ("scheduled", "recurring")),
        ("skill_authoring_holdout", ("skill authoring", "skill-authoring")),
    ],
)
def test_h3_h4_fixture_adoption_requires_boundary_rule(group, rule_tokens):
    present = any(
        group in _read(PLANS_DIR / fixture)
        for fixture in ("route-002-holdout-eval.yaml", "route-003-adversarial-eval.yaml")
    )
    if not present:
        return  # dormant: deferred as genuinely ambiguous
    contract = _read(PLANS_DIR / "ROUTING_CONTRACT.md").lower()
    assert any(token in contract for token in rule_tokens), (
        f"fixture group {group!r} landed but ROUTING_CONTRACT.md names no "
        f"matching boundary rule ({rule_tokens}); fixtures must encode decided "
        "contracts, not open hypotheses (routing-holdout plan deferral)"
    )
