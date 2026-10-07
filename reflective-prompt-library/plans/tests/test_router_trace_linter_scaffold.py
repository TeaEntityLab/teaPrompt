"""The router-trace-linter scaffold must accept its own fixtures.

Extracts the emitted checker from the skill and runs the verification
fixtures (complete, rationale, confidence, high-risk, alias, the RV-04
contrastive matrix, and quoted confidence) plus the installed dispatch
traces. A fixture the checker rejects is a contract bug, not a test to
weaken.
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "reflective-prompt-library/skills/router-trace-linter/SKILL.md"
DISPATCH = ROOT / "reflective-prompt-library/skills/examples/reflective-dispatch.examples.md"

COMPLETE = """
Mode: dispatch
Strictness: L1
Goal: reword the onboarding banner to match the style guide
Assumptions: banner text only; no auth, billing, or production surface
Workflow: reflective-minimality
Route Confidence: medium
Enhancements Enabled: none
Enhancements Available: style-guide sweep after this edit (deferred: single string, no logic change)
Human Review: not required — L1 wording change, reversible in one edit
Next Action: run reflective-minimality on the banner copy
"""

CONTROL = """
Mode: dispatch
Strictness: L2
Goal: rename a local variable
Assumptions: Only the actions in Goal are planned.
Workflow: reflective-implement
Route Confidence: medium
Enhancements Enabled: none
Enhancements Available: none
Human Review: not required
Next Action: execute the named change
"""

ALIAS = """
canonical_intent: reword the onboarding banner to match the style guide
workflow: reflective-minimality
confidence: medium
enhancements_enabled: none
enhancements_available: style-guide sweep after this edit (deferred: single string, no logic change)
rationale: the banner is copy only, so a wider workflow would not change the result
"""


def _checker():
    text = SKILL.read_text(encoding="utf-8")
    match = re.search(r"```python\n(.*?)```", text, re.S)
    assert match, "router-trace-linter scaffold fence missing"
    spec = importlib.util.spec_from_loader("lint_route_trace", loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(compile(match.group(1), str(SKILL), "exec"), module.__dict__)
    return module


def _failing(result):
    return [row["field"] for row in result["rows"] if row["status"] not in {"ok", "warning"}]


def test_complete_trace_passes_and_keeps_negated_hazards_quiet():
    checker = _checker()
    result = checker.lint(COMPLETE)
    assert result["verdict"] == "pass"
    assert _failing(result) == []
    assert result["rationale_seat"] == "Enhancements Available"
    assert all(row["status"] == "ok" and row["raw"] != "<absent>" for row in result["rows"])

    named = COMPLETE.replace(
        "Enhancements Available: style-guide sweep after this edit (deferred: single string, no logic change)",
        "Enhancements Available: security review after bounded patch (deferred: L2 scope, no auth surface)",
    )
    named_result = checker.lint(named)
    assert named_result["verdict"] == "pass"
    assert _failing(named_result) == []


def test_missing_rationale_and_blank_confidence_fail():
    checker = _checker()
    missing = COMPLETE.replace(
        "Assumptions: banner text only; no auth, billing, or production surface",
        "Assumptions:",
    ).replace(
        "Enhancements Available: style-guide sweep after this edit (deferred: single string, no logic change)",
        "Enhancements Available: performance review",
    )
    rationale = checker.lint(missing)
    assert rationale["verdict"] == "fail"
    assert _failing(rationale) == ["Assumptions", "Enhancements Available"]
    assert any(row["detail"] == "R5/R7" for row in rationale["rows"])

    blank = checker.lint(COMPLETE.replace("Route Confidence: medium", "Route Confidence:"))
    assert blank["verdict"] == "fail"
    assert _failing(blank) == ["Route Confidence"]
    confidence = next(row for row in blank["rows"] if row["field"] == "Route Confidence")
    assert confidence["raw"].startswith("Route Confidence:")


def test_high_risk_without_review_fails_and_alias_form_warns():
    checker = _checker()
    high = """
Mode: routing
Strictness: L4
Goal: deploy the auth-service migration to production
Assumptions: production deploy window
Workflow: reflective-risk
Route Confidence: high
Enhancements Enabled: risk gate
Enhancements Available: none
Human Review: none
Next Action: stop for review
"""
    refused = checker.lint(high)
    assert refused["verdict"] == "fail"
    assert _failing(refused) == ["Human Review"]

    alias = checker.lint(ALIAS)
    assert alias["verdict"] == "pass"
    assert alias["warnings"] == ["Mode", "Strictness", "Human Review", "Next Action"]
    absent = {row["field"]: row["raw"] for row in alias["rows"] if row["status"] == "warning"}
    assert absent == {
        "Mode": "<absent>",
        "Strictness": "<absent>",
        "Human Review": "<absent>",
        "Next Action": "<absent>",
    }

    hazard = checker.lint(ALIAS.replace(
        "reword the onboarding banner to match the style guide",
        "reword the production onboarding banner",
    ))
    assert hazard["verdict"] == "fail"
    assert _failing(hazard) == ["Human Review"]


def _sub(trace, field, replacement):
    updated = []
    for line in trace.strip().splitlines():
        if line.startswith(field + ":"):
            updated.append(f"{field}: {replacement}")
        else:
            updated.append(line)
    return "\n".join(updated) + "\n"


def test_r4_contrastive_matrix_denies_bypasses_and_holds_controls():
    checker = _checker()

    denied = [
        ("No auth changes, deploy to production, and rotate credentials", "not required", "reflective-implement"),
        ("deploy to production", "false", "reflective-implement"),
        ("deploy to production", "not applicable", "reflective-implement"),
        ("deploy to production", "not-applicable", "reflective-implement"),
        ("deploy to production", "tbd", "reflective-implement"),
        ("deploy to production", "**none**", "reflective-implement"),
        ('deploy to production', '"none"', "reflective-implement"),
        ("rename a local variable", "not required", "Reflective-Risk"),
    ]
    for goal, review, workflow in denied:
        trace = _sub(_sub(_sub(CONTROL, "Goal", goal), "Human Review", review), "Workflow", workflow)
        result = checker.lint(trace)
        assert result["verdict"] == "fail", (goal, review, workflow)
        row = next(r for r in result["rows"] if r["field"] == "Human Review")
        assert row["status"] not in ("ok", "warning"), (goal, review, workflow)
        assert row["detail"] == "R4", (goal, review, workflow)

    low_risk = checker.lint(CONTROL)
    assert low_risk["verdict"] == "pass"
    assert _failing(low_risk) == []

    for review in ("none", "skipped"):
        trace = _sub(_sub(CONTROL, "Goal", "deploy to production"), "Human Review", review)
        result = checker.lint(trace)
        assert result["verdict"] == "fail", review
        row = next(r for r in result["rows"] if r["field"] == "Human Review")
        assert row["status"] not in ("ok", "warning"), review
        assert row["detail"] == "R4", review


def test_quoted_confidence_passes_and_prose_still_fails():
    checker = _checker()
    for confidence in ('"medium"', "'medium'", "**medium**", '"high"', '"low"', '"0.8"'):
        result = checker.lint(_sub(CONTROL, "Route Confidence", confidence))
        assert result["verdict"] == "pass", confidence
        assert _failing(result) == [], confidence

    for confidence in ("maybe", "confident", "80%", "a whole prose sentence about routing today"):
        result = checker.lint(_sub(CONTROL, "Route Confidence", confidence))
        assert result["verdict"] == "fail", confidence
        assert _failing(result) == ["Route Confidence"], confidence


def test_dispatch_examples_are_not_false_positives():
    checker = _checker()
    traces = re.findall(r"```markdown\n(.*?)```", DISPATCH.read_text(encoding="utf-8"), re.S)
    assert len(traces) == 2
    for trace in traces:
        result = checker.lint(trace)
        assert result["verdict"] == "pass", _failing(result)
