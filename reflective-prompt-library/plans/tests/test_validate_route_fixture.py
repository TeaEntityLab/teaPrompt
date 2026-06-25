"""Tests for route eval fixture validation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from validate_route_fixture import (  # noqa: E402
    ROUTE_002_MIN_HOLDOUT_GROUPS,
    ROUTE_002_MIN_PHRASES,
    ROUTE_003_MIN_ADVERSARIAL_GROUPS,
    ROUTE_003_MIN_PHRASES,
    VALID_WORKFLOWS,
)
from route_paraphrase_eval import load_route_eval_config  # noqa: E402

PLANS = Path(__file__).parent.parent


def test_route_002_meets_minimum_holdout_coverage():
    config = load_route_eval_config(PLANS / "route-002-holdout-eval.yaml")
    groups = config["holdout_sets"]
    phrases = sum(len(group.get("phrases", [])) for group in groups)
    assert len(groups) >= ROUTE_002_MIN_HOLDOUT_GROUPS
    assert phrases >= ROUTE_002_MIN_PHRASES


def test_route_003_meets_minimum_adversarial_coverage():
    config = load_route_eval_config(PLANS / "route-003-adversarial-eval.yaml")
    groups = config["adversarial_sets"]
    phrases = sum(len(group.get("phrases", [])) for group in groups)
    assert len(groups) >= ROUTE_003_MIN_ADVERSARIAL_GROUPS
    assert phrases >= ROUTE_003_MIN_PHRASES


def test_route_fixtures_use_known_workflows():
    for fixture_name, section in (
        ("route-002-holdout-eval.yaml", "holdout_sets"),
        ("route-003-adversarial-eval.yaml", "adversarial_sets"),
    ):
        config = load_route_eval_config(PLANS / fixture_name)
        for group in config[section]:
            assert group["expected_workflow"] in VALID_WORKFLOWS, group["name"]


def test_route_fixture_minimums_match_validator_constants():
    """Anti-drift: fixture actuals must meet exported minimum constants."""
    route_002 = load_route_eval_config(PLANS / "route-002-holdout-eval.yaml")
    route_003 = load_route_eval_config(PLANS / "route-003-adversarial-eval.yaml")
    r2_groups = len(route_002["holdout_sets"])
    r2_phrases = sum(len(g.get("phrases", [])) for g in route_002["holdout_sets"])
    r3_groups = len(route_003["adversarial_sets"])
    r3_phrases = sum(len(g.get("phrases", [])) for g in route_003["adversarial_sets"])
    assert r2_groups == ROUTE_002_MIN_HOLDOUT_GROUPS
    assert r2_phrases == ROUTE_002_MIN_PHRASES
    assert r3_groups == ROUTE_003_MIN_ADVERSARIAL_GROUPS
    assert r3_phrases == ROUTE_003_MIN_PHRASES


ROUND_51_BOUNDARY_PROBES = (
    ("narrow scope and assumptions before writing the PRD", "reflective-brief"),
    ("what dependencies can we remove from this module", "reflective-minimality"),
    ("which skill handles session handoff in this library", "reflective-dispatch"),
    ("review the README for clarity not security", "reflective-review"),
    ("比較兩個 API 設計方案但不要寫 code", "reflective-spec-plan"),
)

# ROUTE-002 holdout phrases that should appear in EN/zh-TW cheatsheets (anti-drift).
BOUNDARY_CHEATSHEET_CUES = tuple(text for text, _ in ROUND_51_BOUNDARY_PROBES) + (
    "write tickets and acceptance criteria without touching the repo",
    "check the diff for readability not production deploy",
    "審查 README 清晰度不是安全風險",
    "把規格寫出來但不要改程式",
)


def test_round_51_boundary_probes():
    """Anti-drift: Rounds 51–55 router boundaries for brief/plan/review/dispatch."""
    from route_paraphrase_eval import ParaphraseRouter  # noqa: E402

    router = ParaphraseRouter()
    for text, expected in ROUND_51_BOUNDARY_PROBES:
        workflow, _, _, _ = router.route(text)
        assert workflow == expected, f"{text!r} -> {workflow}, want {expected}"

IMPLEMENT_NOT_PLAN_IMPLEMENT_PROBES = (
    "implement the approved spec in the repository",
    "在 repository 實作已核准 spec",
    "implement 已核准 spec in the repository",
    "落地已核准規格到 codebase",
    "ship the code fix for the off-by-one bug",
)

IMPLEMENT_NOT_PLAN_SPEC_PLAN_PROBES = (
    "write tickets from the approved spec without implementing",
    "plan the approved spec without repo changes",
    "plan 已核准 spec without repo changes",
)

ROUTE_003_ADVERSARIAL_BOUNDARY_PROBES = (
    ("design a handoff workflow specification without runtime code", "reflective-spec-plan"),
    ("patch the trivial null check in code", "reflective-implement"),
    ("verify production auth change will not expose secrets", "reflective-risk"),
    ("inspect this patch for regressions before merge", "reflective-review"),
    ("six-lens debate on whether to merge these skills", "reflective-research"),
    ("幫我 patch 這個 trivial null check and run tests", "reflective-implement"),
    ("把這個 idea break down into tickets with acceptance criteria", "reflective-spec-plan"),
    ("which workflow skill should run for this library task", "reflective-dispatch"),
    ("lessons learned retro after this sprint", "reflective-handoff-retro"),
    ("compare official docs for both libraries before deciding", "reflective-research"),
    ("which reflective workflow skill covers handoff retro", "reflective-dispatch"),
    ("plan the approved spec without repo changes", "reflective-spec-plan"),
    ("align stakeholders on goals before writing tickets", "reflective-brief"),
    ("釐清目標再拆工單", "reflective-brief"),
)

# One canonical phrase per ROUTE-003 adversarial group (excluding implement_not_plan_trap / R11).
ROUTE_003_ADVERSARIAL_CHEATSHEET_CUES = tuple(text for text, _ in ROUTE_003_ADVERSARIAL_BOUNDARY_PROBES)

# Top-of-cheatsheet boundary quick-cue summary markers (ROUTE-002 holdout + ROUTE-003 adversarial).
BOUNDARY_QUICK_CUE_EN_MARKERS = (
    "Boundary quick cues (ROUTE-002 holdout + ROUTE-003 adversarial):",
    "**Plan-only (no code)**",
    "**Plain review (non-production)**",
    "**Approved spec delivery**",
    "**Brief before plan**",
    "**Research not brief**",
    "**Trivial fix not review**",
    "**Production risk not plain review**",
)

BOUNDARY_QUICK_CUE_ZH_MARKERS = (
    "邊界速查（ROUTE-002 holdout + ROUTE-003 adversarial）：",
    "**僅規劃不寫程式**",
    "**非正式環境審查**",
    "**已核准規格落地**",
    "**規劃前先釐清**",
    "**研究不是釐清**",
    "**小修不是審查**",
    "**正式環境風險不是一般審查**",
)

# Probe-linked snippets that must appear in each quick-cue bullet description (R12 anti-drift).
BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_EN = (
    "explicit no-code context",
    "production risk is out of scope",
    "approved spec in the repository",
    "before PRD/tickets",
    "multi-voice debates",
    "small code patches",
    "auth/production/billing",
)

BOUNDARY_QUICK_CUE_PROBE_SNIPPETS_ZH = (
    "明確不要改程式",
    "排除正式環境風險",
    "已核准 spec",
    "PRD/工單前",
    "多視角",
    "小 patch",
    "auth/production/billing",
)


def test_route_003_adversarial_boundary_probes():
    """Anti-drift: ROUTE-003 adversarial boundaries route as fixture expects."""
    from route_paraphrase_eval import ParaphraseRouter  # noqa: E402

    router = ParaphraseRouter()
    for text, expected in ROUTE_003_ADVERSARIAL_BOUNDARY_PROBES:
        workflow, _, _, _ = router.route(text)
        assert workflow == expected, f"{text!r} -> {workflow}, want {expected}"



def _implement_not_plan_trap_phrases() -> set[str]:
    config = load_route_eval_config(PLANS / "route-003-adversarial-eval.yaml")
    for group in config["adversarial_sets"]:
        if group["name"] == "implement_not_plan_trap":
            return set(group.get("phrases", []))
    raise AssertionError("missing ROUTE-003 implement_not_plan_trap group")


def test_implement_not_plan_trap_holdout_covers_router_probes():
    """Anti-drift: ROUTE-003 holdout must include implement boundary probes."""
    fixture_phrases = _implement_not_plan_trap_phrases()
    missing = [p for p in IMPLEMENT_NOT_PLAN_IMPLEMENT_PROBES if p not in fixture_phrases]
    assert not missing, f"implement_not_plan_trap missing implement probes: {missing}"


def test_implement_not_plan_trap_excludes_spec_plan_probes():
    """Anti-drift: plan-only probes must not live in the implement trap group."""
    fixture_phrases = _implement_not_plan_trap_phrases()
    overlap = [p for p in IMPLEMENT_NOT_PLAN_SPEC_PLAN_PROBES if p in fixture_phrases]
    assert not overlap, f"implement_not_plan_trap must not include spec-plan probes: {overlap}"


def test_implement_approved_spec_not_plan_boundary():
    """Anti-drift: ROUTE-003 implement_not_plan_trap approved-spec delivery."""
    from route_paraphrase_eval import ParaphraseRouter  # noqa: E402

    router = ParaphraseRouter()
    probes = [
        *((text, "reflective-implement") for text in IMPLEMENT_NOT_PLAN_IMPLEMENT_PROBES),
        *((text, "reflective-spec-plan") for text in IMPLEMENT_NOT_PLAN_SPEC_PLAN_PROBES),
    ]
    for text, expected in probes:
        workflow, _, _, _ = router.route(text)
        assert workflow == expected, f"{text!r} -> {workflow}, want {expected}"

def _approved_spec_plan_not_implement_trap_phrases() -> set[str]:
    config = load_route_eval_config(PLANS / "route-003-adversarial-eval.yaml")
    for group in config["adversarial_sets"]:
        if group["name"] == "approved_spec_plan_not_implement_trap":
            return set(group.get("phrases", []))
    raise AssertionError("missing ROUTE-003 approved_spec_plan_not_implement_trap group")


def test_approved_spec_plan_not_implement_trap_covers_probes():
    """Anti-drift: ROUTE-003 plan-only approved-spec probes live in dedicated trap group."""
    fixture_phrases = _approved_spec_plan_not_implement_trap_phrases()
    missing = [p for p in IMPLEMENT_NOT_PLAN_SPEC_PLAN_PROBES if p not in fixture_phrases]
    assert not missing, f"approved_spec_plan_not_implement_trap missing probes: {missing}"

