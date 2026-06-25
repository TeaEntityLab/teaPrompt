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


def test_round_51_boundary_probes():
    """Anti-drift: Rounds 51–55 router boundaries for brief/plan/review/dispatch."""
    from route_paraphrase_eval import ParaphraseRouter  # noqa: E402

    router = ParaphraseRouter()
    probes = [
        ("narrow scope and assumptions before writing the PRD", "reflective-brief"),
        ("what dependencies can we remove from this module", "reflective-minimality"),
        ("which skill handles session handoff in this library", "reflective-dispatch"),
        ("review the README for clarity not security", "reflective-review"),
        ("比較兩個 API 設計方案但不要寫 code", "reflective-spec-plan"),
    ]
    for text, expected in probes:
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

