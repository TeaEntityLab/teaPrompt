"""Behavioral consumers for required routing policies and hard-gate faults."""

import subprocess
import sys
from pathlib import Path

import pytest

PLANS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLANS))
from route_paraphrase_eval import ParaphraseEval, ParaphraseRouter  # noqa: E402

POLICIES = ("forbid_silent_downgrade", "require_route_trace_on_low_confidence")

SUPPORTED_TRACE_FIELDS = (
    "canonical_intent",
    "workflow",
    "confidence",
    "enhancements_enabled",
    "enhancements_available",
    "rationale",
)


def _fixture(
    root: Path,
    *,
    omit=None,
    value="true",
    threshold="0.50",
    aspirational="0.50",
    omit_threshold=False,
    trace_fields=None,
    omit_trace=False,
) -> Path:
    if trace_fields is None:
        trace_fields = list(SUPPORTED_TRACE_FIELDS)
    lines = [
        "version: 1", "id: ROUTE-POLICY", "global_expectations:",
    ]
    if not omit_threshold:
        lines.append(f"  phase1_route_consistency_min: {threshold}")
    lines.append(f"  aspirational_route_consistency_target: {aspirational}")
    lines.extend(f"  {key}: {value}" for key in POLICIES if key != omit)
    if not omit_trace:
        lines.append("trace_required_fields:")
        lines.extend(f"  - {field}" for field in trace_fields)
    lines.extend([
        "intent_groups:",
        "  - intent: local_patch", "    expected_workflow: reflective-implement",
        "    risk_level: low", "    phrases:", "      - valid patch",
        "      - fault patch",
    ])
    path = root / "route-policy.yaml"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _refuses_before_routing(repo_root: Path, fixture: Path) -> None:
    calls = []
    original = ParaphraseRouter.route

    def spy(self, text):
        calls.append(text)
        return original(self, text)

    ParaphraseRouter.route = spy
    try:
        with pytest.raises(ValueError):
            evaluator = ParaphraseEval(str(repo_root), fixture)
            evaluator.run_eval()
    finally:
        ParaphraseRouter.route = original
    assert calls == []


@pytest.mark.parametrize("policy", POLICIES)
def test_missing_policy_refuses_before_evaluation(tmp_path: Path, policy: str):
    _refuses_before_routing(tmp_path, _fixture(tmp_path, omit=policy))


@pytest.mark.parametrize("value", ["0", "1", "none", '"enabled"'])
def test_non_boolean_policy_refuses_before_evaluation(tmp_path: Path, value: str):
    _refuses_before_routing(tmp_path, _fixture(tmp_path, value=value))


def test_missing_threshold_refuses_before_evaluation(tmp_path: Path):
    _refuses_before_routing(tmp_path, _fixture(tmp_path, omit_threshold=True))


@pytest.mark.parametrize(
    "threshold",
    ["-1", "-0.10", "1.10", "2", "true", "false", "none", '"high"', "1.0e999", "9" * 320],
)
def test_invalid_threshold_refuses_before_evaluation(tmp_path: Path, threshold: str):
    _refuses_before_routing(tmp_path, _fixture(tmp_path, threshold=threshold))


@pytest.mark.parametrize(
    "aspirational",
    ["-0.10", "1.10", "true", "none", "1.0e999", "9" * 320],
)
def test_invalid_aspirational_threshold_refuses_before_evaluation(
    tmp_path: Path, aspirational: str
):
    _refuses_before_routing(tmp_path, _fixture(tmp_path, aspirational=aspirational))


@pytest.mark.parametrize(
    "field",
    ["phase1_route_consistency_min", "aspirational_route_consistency_target"],
)
def test_nonfinite_threshold_refuses_before_evaluation(tmp_path: Path, field: str):
    evaluator = ParaphraseEval(str(tmp_path), _fixture(tmp_path))
    evaluator.config["global_expectations"][field] = float("nan")
    calls = []
    real_route = evaluator.router.route

    def route(text):
        calls.append(text)
        return real_route(text)

    evaluator.router.route = route

    with pytest.raises(ValueError):
        evaluator.run_eval()

    assert calls == []


@pytest.mark.parametrize("threshold", ["0", "1", "0.50", "0.70"])
def test_valid_threshold_boundaries_evaluate(tmp_path: Path, threshold: str):
    evaluator = ParaphraseEval(str(tmp_path), _fixture(tmp_path, threshold=threshold))
    evaluator.router.route = (
        lambda text: ("reflective-implement", 0.9, [], "Implement the local patch.")
    )

    summary = evaluator.run_eval()["summary"]

    assert evaluator.phase1_consistency_min == float(threshold)
    assert evaluator.results["thresholds"]["phase1_route_consistency_min"] == float(
        threshold
    )
    assert summary["consistency_rate"] == 1.0


@pytest.mark.parametrize("trace_kwargs", [{"omit_trace": True}, {"trace_fields": []}])
def test_missing_or_empty_trace_fields_refuse_before_evaluation(
    tmp_path: Path, trace_kwargs: dict
):
    _refuses_before_routing(tmp_path, _fixture(tmp_path, **trace_kwargs))


def test_supported_trace_subset_evaluates(tmp_path: Path):
    evaluator = ParaphraseEval(
        str(tmp_path), _fixture(tmp_path, trace_fields=["rationale"])
    )
    evaluator.router.route = (
        lambda text: ("reflective-implement", 0.9, [], "Implement the local patch.")
    )

    summary = evaluator.run_eval()["summary"]

    assert summary["consistency_rate"] == 1.0
    assert summary["trace_coverage_rate"] == 1.0


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


@pytest.mark.parametrize(
    "fixture_kwargs",
    [
        {"omit_threshold": True},
        {"threshold": "1.10"},
        {"threshold": "true"},
        {"threshold": "none"},
        {"omit_trace": True},
        {"trace_fields": []},
        {"aspirational": "9" * 320},
        {"aspirational": "true"},
        {"aspirational": "none"},
        {"aspirational": "1.0e999"},
    ],
    ids=[
        "missing-threshold",
        "out-of-range-threshold",
        "boolean-threshold",
        "string-threshold",
        "missing-trace",
        "empty-trace",
        "overflowing-aspirational",
        "boolean-aspirational",
        "string-aspirational",
        "infinite-aspirational",
    ],
)
def test_cli_invalid_config_does_not_publish_success_report(
    tmp_path: Path, fixture_kwargs: dict
):
    plans = tmp_path / "reflective-prompt-library" / "plans"
    plans.mkdir(parents=True)
    script = plans / "route_paraphrase_eval.py"
    script.write_bytes((PLANS / script.name).read_bytes())
    fixture = _fixture(plans, **fixture_kwargs)

    result = subprocess.run(
        [sys.executable, str(script), str(fixture)], cwd=tmp_path,
        capture_output=True, text=True, timeout=15,
    )

    assert result.returncode == 2
    assert result.stdout == ""
    assert not (plans / "route-policy-results.json").exists()
