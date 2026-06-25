#!/usr/bin/env python3
"""
Route Fixture Validator (deterministic, CI-safe)

Validates ROUTE-001/002/003 YAML shape and minimum coverage before running
paraphrase routing evals. Round 22 panel compromise: gate fixture hygiene without
adding a YAML runtime dependency.
"""

import sys
from pathlib import Path

from route_paraphrase_eval import load_route_eval_config  # noqa: E402

VALID_WORKFLOWS = {
    "reflective-dispatch",
    "reflective-brief",
    "reflective-spec-plan",
    "reflective-implement",
    "reflective-review",
    "reflective-research",
    "reflective-risk",
    "reflective-handoff-retro",
    "reflective-minimality",
}

ROUTE_001_MIN_INTENT_GROUPS = 12
ROUTE_001_MIN_ADVERSARIAL_GROUPS = 4
ROUTE_001_MIN_PHRASES = 128

ROUTE_002_MIN_HOLDOUT_GROUPS = 36
ROUTE_002_MIN_PHRASES = 102

ROUTE_003_MIN_ADVERSARIAL_GROUPS = 14
ROUTE_003_MIN_PHRASES = 37

REQUIRED_TRACE_FIELDS = {
    "canonical_intent",
    "workflow",
    "confidence",
    "enhancements_enabled",
    "enhancements_available",
    "rationale",
}

REQUIRED_EVAL_RULES = {
    "route_equivalence",
    "low_confidence_visibility",
    "enhancement_visibility",
    "no_silent_downgrade",
}


def count_phrases(groups: list) -> int:
    return sum(len(group.get("phrases", [])) for group in groups)


def validate_group_names(groups: list, label: str, errors: list) -> None:
    seen = set()
    for group in groups:
        name = group.get("name") or group.get("intent")
        if not name:
            errors.append(f"{label}: group missing name/intent")
            continue
        if name in seen:
            errors.append(f"{label}: duplicate group name {name!r}")
        seen.add(name)


def validate_workflows(groups: list, label: str, errors: list) -> None:
    for group in groups:
        name = group.get("name") or group.get("intent")
        workflow = group.get("expected_workflow")
        if workflow not in VALID_WORKFLOWS:
            errors.append(f"{label} {name}: invalid expected_workflow {workflow!r}")
        phrases = group.get("phrases", [])
        if not phrases:
            errors.append(f"{label} {name}: phrases must be non-empty")


def validate_fixture(path: Path, errors: list) -> None:
    config = load_route_eval_config(path)
    fixture_id = config.get("id", path.name)

    trace_fields = set(config.get("trace_required_fields", []))
    if not REQUIRED_TRACE_FIELDS.issubset(trace_fields):
        missing = sorted(REQUIRED_TRACE_FIELDS - trace_fields)
        errors.append(f"{fixture_id}: missing trace_required_fields {missing}")

    configured_rules = {rule.get("name") for rule in config.get("evaluation_rules", [])}
    if not REQUIRED_EVAL_RULES.issubset(configured_rules):
        missing = sorted(REQUIRED_EVAL_RULES - configured_rules)
        errors.append(f"{fixture_id}: missing evaluation_rules {missing}")

    intent_groups = config.get("intent_groups", [])
    adversarial_groups = config.get("adversarial_sets", [])
    holdout_groups = config.get("holdout_sets", [])

    if fixture_id == "ROUTE-001":
        if len(intent_groups) < ROUTE_001_MIN_INTENT_GROUPS:
            errors.append(
                f"ROUTE-001: expected >= {ROUTE_001_MIN_INTENT_GROUPS} intent groups; "
                f"found {len(intent_groups)}"
            )
        if len(adversarial_groups) < ROUTE_001_MIN_ADVERSARIAL_GROUPS:
            errors.append(
                f"ROUTE-001: expected >= {ROUTE_001_MIN_ADVERSARIAL_GROUPS} adversarial sets; "
                f"found {len(adversarial_groups)}"
            )
        total_phrases = count_phrases(intent_groups) + count_phrases(adversarial_groups)
        if total_phrases < ROUTE_001_MIN_PHRASES:
            errors.append(
                f"ROUTE-001: expected >= {ROUTE_001_MIN_PHRASES} phrases; found {total_phrases}"
            )
        validate_group_names(intent_groups, "ROUTE-001 intent", errors)
        validate_group_names(adversarial_groups, "ROUTE-001 adversarial", errors)
        validate_workflows(intent_groups, "ROUTE-001 intent", errors)
        validate_workflows(adversarial_groups, "ROUTE-001 adversarial", errors)
        return

    if fixture_id == "ROUTE-002":
        if len(holdout_groups) < ROUTE_002_MIN_HOLDOUT_GROUPS:
            errors.append(
                f"ROUTE-002: expected >= {ROUTE_002_MIN_HOLDOUT_GROUPS} holdout groups; "
                f"found {len(holdout_groups)}"
            )
        total_phrases = count_phrases(holdout_groups)
        if total_phrases < ROUTE_002_MIN_PHRASES:
            errors.append(
                f"ROUTE-002: expected >= {ROUTE_002_MIN_PHRASES} phrases; found {total_phrases}"
            )
        validate_group_names(holdout_groups, "ROUTE-002 holdout", errors)
        validate_workflows(holdout_groups, "ROUTE-002 holdout", errors)
        return

    if fixture_id == "ROUTE-003":
        if len(adversarial_groups) < ROUTE_003_MIN_ADVERSARIAL_GROUPS:
            errors.append(
                f"ROUTE-003: expected >= {ROUTE_003_MIN_ADVERSARIAL_GROUPS} adversarial sets; "
                f"found {len(adversarial_groups)}"
            )
        total_phrases = count_phrases(adversarial_groups)
        if total_phrases < ROUTE_003_MIN_PHRASES:
            errors.append(
                f"ROUTE-003: expected >= {ROUTE_003_MIN_PHRASES} phrases; found {total_phrases}"
            )
        validate_group_names(adversarial_groups, "ROUTE-003 adversarial", errors)
        validate_workflows(adversarial_groups, "ROUTE-003 adversarial", errors)
        return

    errors.append(f"{path.name}: unsupported route fixture id {fixture_id!r}")


def main() -> int:
    plans_dir = Path(__file__).parent
    fixtures = [
        plans_dir / "route-001-paraphrase-eval.yaml",
        plans_dir / "route-002-holdout-eval.yaml",
        plans_dir / "route-003-adversarial-eval.yaml",
    ]

    print("Validating route eval fixtures")
    print("=" * 60)

    errors: list[str] = []
    for fixture in fixtures:
        if not fixture.exists():
            errors.append(f"missing fixture: {fixture}")
            continue
        validate_fixture(fixture, errors)

    if errors:
        print(f"\n❌ {len(errors)} route fixture violation(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("\n✅ Route fixtures valid")
    print(
        f"  ROUTE-001: >= {ROUTE_001_MIN_INTENT_GROUPS} intent + "
        f">= {ROUTE_001_MIN_ADVERSARIAL_GROUPS} adversarial, "
        f">= {ROUTE_001_MIN_PHRASES} phrases"
    )
    print(
        f"  ROUTE-002: >= {ROUTE_002_MIN_HOLDOUT_GROUPS} holdout groups, "
        f">= {ROUTE_002_MIN_PHRASES} phrases"
    )
    print(
        f"  ROUTE-003: >= {ROUTE_003_MIN_ADVERSARIAL_GROUPS} adversarial sets, "
        f">= {ROUTE_003_MIN_PHRASES} phrases"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
