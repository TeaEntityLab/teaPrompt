"""Trigger-state watch for dormant roadmap items (2026-07-11 register).

Mechanizes the whole-project plan's top risk -- trigger drift: deferred items
whose triggers fire unnoticed (plans/whole-project-plan-2026-07-11.md #Risks).
Per GLOSSARY Adoption Guard Closure, deferred and rejected ledger rows are
guarded for LEDGER PRESENCE and TRIGGER STATE only; nothing here asserts
deferred content as though it were adopted.

Every dormancy assertion is a migration tripwire. A failure means one of:
  - a trigger fired silently (queue-discipline violation): open the
    re-litigation record per plans/whole-project-roadmap-2026-07-11.md; or
  - a legitimate adoption landed: flip the owning ledger row, record the
    decision, and update the watched tokens here in the same change.

Item specs: plans/dormant-work-specs-2026-07-11.md
Green means "no silent drift among the watched tokens" -- never "no trigger
fired anywhere" (regression-guard tier, N13 discipline).
"""

import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_skill_examples import DOMAIN_PACK_SKILLS  # noqa: E402
from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    cheatsheet_en_path,
    glossary_path,
    library_skills_dir,
)

REPO_ROOT = PROMPT_LIBRARY_ROOT.parent
PLANS_DIR = PROMPT_LIBRARY_ROOT / "plans"

GENERATOR = library_skills_dir() / "flow-control-generator" / "SKILL.md"
HARNESS = library_skills_dir() / "flow-loop-harness" / "SKILL.md"
DISPATCH = library_skills_dir() / "reflective-dispatch" / "SKILL.md"

# Registry-driven since the 2026-07-18 governance-pack panel (R9): the
# routing-surface-absence guard protects against EVERY registered pack name.
# P7/N12 decided the two flow packs; G9 (adoption ledger) defers the
# governance pack's collision measurement with its own trigger.
PACK_NAMES = tuple(DOMAIN_PACK_SKILLS)

ROUTING_SURFACES = (
    DISPATCH,
    PLANS_DIR / "route-001-paraphrase-eval.yaml",
    PLANS_DIR / "route-002-holdout-eval.yaml",
    PLANS_DIR / "route-003-adversarial-eval.yaml",
    PLANS_DIR / "route_paraphrase_eval.py",
    PLANS_DIR / "validate_route_fixture.py",
)

SPEC_BOOK = PLANS_DIR / "dormant-work-specs-2026-07-11.md"
RELITIGATE = (
    "if this is a deliberate adoption, follow the amendment discipline: "
    "ledger row + record + update this watch (see "
    "plans/dormant-work-specs-2026-07-11.md); otherwise a trigger fired "
    "silently -- open the re-litigation record"
)


def _read(path: Path) -> str:
    assert path.is_file(), f"missing {path}"
    return path.read_text(encoding="utf-8")


def _table_row(text: str, prefix: str) -> str:
    for line in text.splitlines():
        if line.startswith(prefix):
            return line
    raise AssertionError(f"ledger row {prefix!r} not found")


# ---------------------------------------------------------------------------
# P7 / N12 -- resolved no-core-integration invariant
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("surface", ROUTING_SURFACES, ids=lambda p: p.name)
def test_p7_packs_absent_from_routing_surfaces(surface: Path):
    """P7 resolved no-change: packs remain host-invoked and outside the
    bounded core router after collision holdouts passed pre-tune."""
    text = _read(surface)
    for pack in PACK_NAMES:
        assert pack not in text, (
            f"{pack!r} appeared in routing surface {surface.name}; this violates "
            f"the P7/N12 no-core-integration decision -- {RELITIGATE}"
        )


def test_p7_en_cheatsheet_appendix_stays_outside_fast_routing():
    text = _read(cheatsheet_en_path())
    assert "## Domain packs (host-invoked; not core routing)" in text
    fast_routing = text.split("## Fast Routing Rule", 1)[1]
    fast_routing = fast_routing.split("## Domain packs", 1)[0]
    for pack in PACK_NAMES:
        assert pack not in fast_routing, (
            f"{pack!r} leaked into the Fast Routing Rule; this violates the "
            f"P7 no-core-integration decision -- {RELITIGATE}"
        )


def test_p7_decision_record_is_structural():
    text = _read(PLANS_DIR / "p7-pack-routing-decision-2026-07-11.md")
    for heading in (
        "## Decision",
        "## Evidence Actually Checked",
        "## Candidate Adoption Ledger",
        "## Falsifiability",
    ):
        assert heading in text, f"P7 decision record missing {heading!r}"
    for token in (
        "no core-router integration",
        "pack_vocab_plan_holdout",
        "pack_vocab_route_holdout",
        "pack_vocab_implement_not_plan_trap",
        "9/9",
    ):
        assert token in text, f"P7 decision record missing {token!r}"


# ---------------------------------------------------------------------------
# P12 / P13 -- pack template sets stay at their adopted composition
# ---------------------------------------------------------------------------

GENERATOR_TEMPLATES = (
    "## Template: Sequential Pipeline (bash)",
    "## Template: Parallel Fan-out/Fan-in (bash)",
    "## Template: Conditional Router (bash)",
    "## Template: Orchestrator-Workers (Python, stdlib only)",
    "## Template: DAG Executor (Python, stdlib only)",
)

HARNESS_TEMPLATES = (
    "## Template: Verify-Gated Fix Loop (bash)",
    "## Template: Evaluator-Optimizer / Writer-Critic (bash)",
    "## Template: Task-Ledger Backlog Loop (bash, ralph-style)",
    "## Template: Multi-Wave Fan-out (bash)",
)


def _template_headings(path: Path) -> tuple[str, ...]:
    return tuple(re.findall(r"^## Template: .+$", _read(path), re.MULTILINE))


def test_p12_generator_template_set_pinned():
    found = _template_headings(GENERATOR)
    assert found == GENERATOR_TEMPLATES, (
        "flow-control-generator template set changed; P12 is user-directed adopted "
        f"and guarded as an exact pack contract -- {RELITIGATE}; found: {found}"
    )


def test_p13_harness_template_set_pinned():
    found = _template_headings(HARNESS)
    assert found == HARNESS_TEMPLATES, (
        "flow-loop-harness template set changed; P13 is user-directed adopted "
        f"and guarded as an exact pack contract -- {RELITIGATE}; found: {found}"
    )


def test_p13_composition_note_still_adopted():
    """P13's adopted alternative (compose parallel template inside the loop
    harness) stays in Topology Selection -- structural invariant of an
    adopted decision, not deferred content."""
    topology = _read(GENERATOR).split("## Topology Selection", 1)[1]
    topology = topology.split("\n## ", 1)[0].lower()
    assert "multi-wave" in topology and "flow-loop-harness" in topology


# ---------------------------------------------------------------------------
# M4 / M6 / M7 -- user-directed adopted destination surfaces stay present
# ---------------------------------------------------------------------------


def test_m4_workflow_acquisition_internalization_delta_present():
    text = _read(PROMPT_LIBRARY_ROOT / "04-agent" / "workflow-acquisition.md").lower()
    for token in ("sentinel-fact", "ephemeral-source", "no-temp-links"):
        assert token in text, f"workflow-acquisition.md lost M4 token {token!r}"


def test_m6_readme_orientation_sections_present():
    en = _read(REPO_ROOT / "README.md")
    zh = _read(REPO_ROOT / "README.zh-TW.md")
    assert re.search(r"^##\s+Orientation\s*$", en, re.MULTILINE)
    assert re.search(r"^##\s+導覽（Orientation）\s*$", zh, re.MULTILINE)
    assert "SKILL_TRIGGER_CHEATSHEET.md" in en
    assert "SKILL_TRIGGER_CHEATSHEET.zh-TW.md" in zh


def test_m7_external_adoption_review_redaction_methodology_present():
    text = _read(PROMPT_LIBRARY_ROOT / "04-agent" / "external-adoption-review.md").lower()
    for token in ("leakage", "packet hash", "sensitive-evidence"):
        assert token in text, f"external-adoption-review.md lost M7 token {token!r}"


# ---------------------------------------------------------------------------
# E2 -- archive surfaces stay in place (destructive restructuring is gated)
# ---------------------------------------------------------------------------


def test_e2_archive_surfaces_unmoved():
    transcript = PLANS_DIR / "multi-agent-panel-consensus-2026-06-25.md"
    assert transcript.is_file(), (
        "panel transcript moved or deleted; E2 restructuring is "
        f"recurrence-gated (rethink record Adoption Update 2) -- {RELITIGATE}"
    )
    for category in ("00-core", "03-context"):
        prompts = list((PROMPT_LIBRARY_ROOT / category).glob("*.md"))
        assert prompts, (
            f"{category}/ is empty or gone; category merges are part of the "
            f"deferred E2 item -- {RELITIGATE}"
        )


# ---------------------------------------------------------------------------
# D4 -- record-hygiene validator adopted and make-all composition matches plan
# ---------------------------------------------------------------------------

EXPECTED_VALIDATE_COMMANDS = (
    "python3 $(PLANS)/validate_links.py",
    "python3 $(PLANS)/lint_skills.py",
    "python3 $(PLANS)/validate_governance.py",
    "python3 $(PLANS)/validate_project_knowledge.py",
    "python3 $(PLANS)/validate_record_hygiene.py",
    "python3 $(PLANS)/validate_benchmark_fixture.py",
    "python3 $(PLANS)/validate_skill_examples.py",
    "python3 $(PLANS)/validate_route_fixture.py",
    "python3 $(PLANS)/route_paraphrase_eval.py",
    "python3 $(PLANS)/route_paraphrase_eval.py $(PLANS)/route-002-holdout-eval.yaml",
    "python3 $(PLANS)/route_paraphrase_eval.py $(PLANS)/route-003-adversarial-eval.yaml",
)


def _makefile_recipe(target: str) -> tuple[str, ...]:
    lines = _read(REPO_ROOT / "Makefile").splitlines()
    recipe: list[str] = []
    in_target = False
    for line in lines:
        if line.startswith(f"{target}:"):
            in_target = True
            continue
        if in_target:
            if line.startswith("\t"):
                recipe.append(line.strip())
            elif line.strip():
                break
    return tuple(recipe)


def test_d4_record_hygiene_validator_present_and_tested():
    assert (PLANS_DIR / "validate_record_hygiene.py").is_file()
    assert (PLANS_DIR / "tests" / "test_validate_record_hygiene.py").is_file()
    assert "validate_record_hygiene.py" in _read(REPO_ROOT / "Makefile")


def test_make_all_composition_matches_plan_snapshot():
    """The whole-project plan declares itself stale if `make all` composition
    changes materially (validator added or removed). Mechanized here."""
    assert _makefile_recipe("validate") == EXPECTED_VALIDATE_COMMANDS, (
        "Makefile validate composition changed; revise "
        "plans/whole-project-plan-2026-07-11.md (its Falsifiability names "
        "composition change as a staleness trigger) and update this snapshot "
        "in the same change"
    )
    test_recipe = _makefile_recipe("test")
    assert any("pytest" in cmd and "tests" in cmd for cmd in test_recipe)


# ---------------------------------------------------------------------------
# H3/H4 -- deferred holdout groups stay out of the fixtures
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "group", ("scheduled_check_boundary_trap", "skill_authoring_holdout")
)
def test_h3_h4_deferred_groups_absent_from_fixtures(group: str):
    for fixture in ("route-002-holdout-eval.yaml", "route-003-adversarial-eval.yaml"):
        text = _read(PLANS_DIR / fixture)
        assert group not in text, (
            f"{group!r} entered {fixture}; H3/H4 were deferred as genuinely "
            f"ambiguous -- a boundary rule decision must land first "
            f"(routing-holdout plan) -- {RELITIGATE}"
        )


# ---------------------------------------------------------------------------
# Ledger presence -- deferred/rejected rows stay on record (closure rule scope)
# ---------------------------------------------------------------------------

LEDGER_TOKENS = (
    ("flow-coverage-panel-record-2026-07-11.md", "## Deferred / Escalated (P12, P13, P15)"),
    ("flow-coverage-panel-record-2026-07-11.md", "Trigger: first such local task."),
    ("flow-coverage-panel-record-2026-07-11.md", "Trigger: recurrence of real multi-wave runs."),
    ("governance-necessity-panel-record-2026-07-11.md", "**Deferred under existing P6**"),
    ("governance-necessity-panel-record-2026-07-11.md", "**Resolved 2026-07-11 — no core-router integration**"),
    ("governance-rules-rethink-review-2026-07-11.md", "E2 + 00-core/03-context merges — deferred"),
    ("governance-rules-rethink-review-2026-07-11.md", "D4 — adopted 2026-07-12"),
    ("skills-surface-plan-2026-07-11.md", "packaging still trigger-gated"),
    (
        "multi-agent-panel-consensus-2026-06-25.md",
        "| `reflective-implement` default-invokes `reflective-minimality` | **Deferred** |",
    ),
    (
        "multi-agent-panel-consensus-2026-06-25.md",
        "| Localized trigger cues beyond cheatsheet / glossary | **Deferred** |",
    ),
)


@pytest.mark.parametrize("record,token", LEDGER_TOKENS, ids=lambda v: str(v)[:48])
def test_deferred_ledger_rows_stay_on_record(record: str, token: str):
    assert token in _read(PLANS_DIR / record), (
        f"ledger token {token!r} vanished from {record}; deferred/rejected "
        "rows must stay visible (Adoption Guard Closure) or be superseded by "
        "an explicit re-litigation record"
    )


@pytest.mark.parametrize(
    "row_prefix,expected",
    [
        ("| M4 |", "Adopted 2026-07-12"),
        ("| M6 |", "Adopted 2026-07-12"),
        ("| M7 |", "Adopted 2026-07-12"),
        ("| M8 |", "Rejected"),
        ("| M5 |", "Re-audit on next governance panel"),
    ],
)
def test_managed_skill_ledger_rows(row_prefix: str, expected: str):
    row = _table_row(
        _read(PLANS_DIR / "managed-skill-promotion-panel-record-2026-07-11.md"),
        row_prefix,
    )
    assert expected in row, (
        f"managed-skill ledger row {row_prefix!r} no longer says {expected!r}; "
        "if state changed, the flip needs its own record + Decision Index "
        "entry, then update this watch"
    )


def test_n8_ledger_row_stays_rejected():
    row = _table_row(
        _read(PLANS_DIR / "governance-necessity-panel-record-2026-07-11.md"),
        "| N8 |",
    )
    assert "**Rejected**" in row


# ---------------------------------------------------------------------------
# N8 -- rejected ratio stays off load-bearing surfaces
# ---------------------------------------------------------------------------

LOAD_BEARING_SURFACES = (
    REPO_ROOT / "README.md",
    PROMPT_LIBRARY_ROOT / "README.md",
    PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md",
    PROMPT_LIBRARY_ROOT / "GLOSSARY.md",
    PROMPT_LIBRARY_ROOT / "METHODOLOGY_MAP.md",
    PLANS_DIR / "QUALITY_GATES_SUMMARY.md",
)


@pytest.mark.parametrize("surface", LOAD_BEARING_SURFACES, ids=lambda p: p.name)
def test_n8_ratio_absent_from_load_bearing_surfaces(surface: Path):
    """PK Standing Non-Goals context: the meta:product ratio is retired unless
    someone defines and guards a stable formula first (necessity record N8).
    Historical plans records keep their mentions; load-bearing surfaces may not
    cite the number. The PK section listing exceptions: none."""
    assert "meta:product" not in _read(surface), (
        f"{surface.name} cites the retired meta:product ratio; N8 requires a "
        "defined, guarded formula first (necessity record N8 next-action)"
    )


# ---------------------------------------------------------------------------
# Direction-gated parity -- roadmap Horizon 4 rows match their owning surfaces
# ---------------------------------------------------------------------------


def test_horizon4_rows_match_owning_surfaces():
    roadmap = _read(PLANS_DIR / "whole-project-roadmap-2026-07-11.md")
    horizon4 = roadmap.split("## Horizon 4", 1)[1].split("\n## ", 1)[0]
    pk = _read(PROMPT_LIBRARY_ROOT / "PROJECT_KNOWLEDGE.md")
    non_goals = pk.split("### Standing Non-Goals", 1)[1].split("\n## ", 1)[0]
    backlog = _read(PLANS_DIR / "multi-agent-panel-consensus-2026-06-25.md")

    # Roadmap rows present.
    for token in (
        "multi-agent runtime",
        "tenth core workflow skill",
        "localization",
        "benchmark comparisons in CI",
        "Enforcing runtime guarantees",
    ):
        assert token in horizon4, f"roadmap Horizon 4 lost its {token!r} row"

    # Owning surfaces still carry the matching direction.
    assert "multi-agent runtime" in non_goals
    assert "tenth core skill" in non_goals
    assert "localization is not current direction" in non_goals
    assert "does not enforce or warrant them" in non_goals
    assert "| LLM benchmark in CI | **Rejected** |" in backlog


def test_checkpoint_date_consistent_across_surfaces():
    for path in (
        PLANS_DIR / "whole-project-roadmap-2026-07-11.md",
        PLANS_DIR / "whole-project-plan-2026-07-11.md",
        PLANS_DIR / "flow-pack-usage-log.md",
        PLANS_DIR / "checkpoint-2026-10-11-runbook.md",
        SPEC_BOOK,
    ):
        assert "2026-10-11" in _read(path), (
            f"{path.name} lost the 2026-10-11 checkpoint date; the date-gated "
            "horizon must stay consistent across planning surfaces"
        )


def test_glossary_closure_rule_still_scopes_this_suite():
    """This suite's legitimacy rests on the Adoption Guard Closure rule
    (deferred rows: presence + trigger state only). If the rule moves or is
    renamed, re-audit this file against its replacement."""
    assert "## Adoption Guard Closure" in _read(glossary_path())
