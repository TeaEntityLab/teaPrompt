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
