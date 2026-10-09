"""Behavioral consumers for required routing policies and hard-gate faults."""

import subprocess
import sys
from pathlib import Path

import pytest

PLANS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLANS))
from route_paraphrase_eval import ParaphraseEval  # noqa: E402

POLICIES = ("forbid_silent_downgrade", "require_route_trace_on_low_confidence")


def _fixture(root: Path, *, omit=None, value="true") -> Path:
    lines = [
        "version: 1", "id: ROUTE-POLICY", "global_expectations:",
        "  phase1_route_consistency_min: 0.50",
        "  aspirational_route_consistency_target: 0.50",
    ]
    lines.extend(f"  {key}: {value}" for key in POLICIES if key != omit)
    lines.extend([
        "trace_required_fields:", "  - canonical_intent", "  - workflow",
        "  - confidence", "  - enhancements_enabled",
        "  - enhancements_available", "  - rationale", "intent_groups:",
        "  - intent: local_patch", "    expected_workflow: reflective-implement",
        "    risk_level: low", "    phrases:", "      - valid patch",
        "      - fault patch",
    ])
    path = root / "route-policy.yaml"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


@pytest.mark.parametrize("policy", POLICIES)
def test_missing_policy_refuses_before_evaluation(tmp_path: Path, policy: str):
    evaluator = ParaphraseEval(str(tmp_path), _fixture(tmp_path, omit=policy))
    calls = []
    evaluator.router.route = lambda text: calls.append(text)

    with pytest.raises(ValueError):
        evaluator.run_eval()

    assert calls == []
    assert evaluator.results["intent_groups"] == []


@pytest.mark.parametrize("value", ["0", "1", "none", '"enabled"'])
def test_non_boolean_policy_refuses_before_evaluation(tmp_path: Path, value: str):
    evaluator = ParaphraseEval(str(tmp_path), _fixture(tmp_path, value=value))
    calls = []
    evaluator.router.route = lambda text: calls.append(text)

    with pytest.raises(ValueError):
        evaluator.run_eval()

    assert calls == []


@pytest.mark.parametrize("fault", ["silent-downgrade", "missing-trace"])
def test_configured_policy_records_fault_without_weakening_threshold(
    tmp_path: Path, fault: str
):
    evaluator = ParaphraseEval(str(tmp_path), _fixture(tmp_path))

    def route(text):
        if text == "valid patch":
            return "reflective-implement", 0.9, [], "Implement the local patch."
        if fault == "silent-downgrade":
            return "reflective-minimality", 0.9, [], "A confident unqualified route."
        return "reflective-implement", 0.2, [], ""

    evaluator.router.route = route
    summary = evaluator.run_eval()["summary"]

    assert summary["consistency_rate"] >= evaluator.phase1_consistency_min
    if fault == "silent-downgrade":
        assert len(summary["silent_downgrade_incidents"]) == 1
        assert summary["silent_downgrade_incidents"][0]["paraphrase"] == "fault patch"
    else:
        assert summary["trace_coverage_rate"] == 0.0
        assert summary["low_confidence_trace_failures"] == [
            {"group": "local_patch", "paraphrase": "fault patch", "missing_trace": True}
        ]


@pytest.mark.parametrize("policy", POLICIES)
def test_cli_missing_policy_does_not_publish_success_report(tmp_path: Path, policy: str):
    plans = tmp_path / "reflective-prompt-library" / "plans"
    plans.mkdir(parents=True)
    script = plans / "route_paraphrase_eval.py"
    script.write_bytes((PLANS / script.name).read_bytes())
    fixture = _fixture(plans, omit=policy)

    result = subprocess.run(
        [sys.executable, str(script), str(fixture)], cwd=tmp_path,
        capture_output=True, text=True, timeout=15,
    )

    assert result.returncode == 2
    assert result.stdout == ""
    assert not (plans / "route-policy-results.json").exists()
