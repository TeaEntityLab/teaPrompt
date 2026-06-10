import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from eval_harness import EvalHarness, DEFAULT_RUBRIC


REPO_ROOT = str(Path(__file__).parent.parent.parent.parent)


@pytest.fixture
def harness():
    return EvalHarness(repo_root=REPO_ROOT)


@pytest.fixture
def verbose_harness():
    return EvalHarness(repo_root=REPO_ROOT, verbose=True)


class TestPassCase:
    def test_high_quality_file_returns_high_score(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/00-core/core-full.md"
        )
        assert result["score"] >= 40.0, (
            f"Expected score >= 40, got {result['score']}. "
            f"Summary: {result['summary']}"
        )
        assert result["summary"]["pass"] >= 2
        assert result["summary"]["fail"] <= 3

    def test_all_checks_present_in_result(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/00-core/core-full.md"
        )
        check_ids = {c["id"] for c in result["checks"]}
        expected = {c["id"] for c in DEFAULT_RUBRIC["checks"]}

        for cid in expected:
            assert cid in check_ids, f"Missing check: {cid}"
        assert len(result["checks"]) == len(expected)


class TestFailCase:
    def test_minimal_file_scores_low(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/00-core/core-minimal.md"
        )
        assert result["score"] <= 70.0, (
            f"Expected score <= 70 for minimal file, got {result['score']}"
        )

    def test_minimal_file_has_goal(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/00-core/core-minimal.md"
        )
        goal_check = [
            c for c in result["checks"] if c["id"] == "has-goal"
        ]
        assert len(goal_check) == 1
        assert goal_check[0]["result"] in ("pass", "fail", "warn")

    def test_minimal_file_lacks_acceptance_criteria(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/00-core/core-minimal.md"
        )
        check = [c for c in result["checks"] if c["id"] == "has-acceptance-criteria"][0]
        assert check["result"] == "fail", (
            f"Expected 'fail' for acceptance criteria check, got '{check['result']}'"
        )


class TestBatchMode:
    def test_batch_returns_valid_summary(self, harness):
        batch = harness.evaluate_batch()
        assert batch["total_files"] >= 30, (
            f"Expected at least 30 prompt files, got {batch['total_files']}"
        )
        assert 0 <= batch["average_score"] <= 100
        assert "lowest" in batch
        assert "highest" in batch
        assert batch["lowest"]["file"] is not None
        assert batch["highest"]["file"] is not None
        assert batch["aggregate"]["pass"] >= 0
        assert batch["aggregate"]["fail"] >= 0

    def test_batch_results_sorted_correctly(self, harness):
        batch = harness.evaluate_batch()
        assert batch["lowest"]["score"] <= batch["highest"]["score"], (
            f"Lowest ({batch['lowest']['score']}) should be <= "
            f"highest ({batch['highest']['score']})"
        )

    def test_each_file_result_has_required_fields(self, harness):
        batch = harness.evaluate_batch()
        for fr in batch["file_results"]:
            assert "file" in fr
            assert "checks" in fr
            assert "score" in fr
            assert "summary" in fr
            assert isinstance(fr["score"], (int, float))


class TestVerboseMode:
    def test_verbose_does_not_alter_scores(self, harness, verbose_harness):
        file = "reflective-prompt-library/00-core/core-full.md"
        normal = harness.evaluate_file(file)
        verbose = verbose_harness.evaluate_file(file)

        assert normal["score"] == verbose["score"], (
            f"Verbose score ({verbose['score']}) differs from "
            f"normal ({normal['score']})"
        )
        assert normal["summary"] == verbose["summary"]

    def test_verbose_check_messages_include_details(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/02-engineering/code-reviewer.md"
        )
        for check in result["checks"]:
            assert "message" in check
            assert "result" in check


class TestScoreCalculation:
    def test_all_pass_gives_100(self, harness):
        results = [
            {"result": "pass", "id": "a"},
            {"result": "pass", "id": "b"},
            {"result": "pass", "id": "c"},
        ]
        score = harness._calculate_score(results)
        assert score == 100.0

    def test_all_fail_gives_0(self, harness):
        results = [
            {"result": "fail", "id": "a"},
            {"result": "fail", "id": "b"},
        ]
        score = harness._calculate_score(results)
        assert score == 0.0

    def test_skip_excluded_from_score(self, harness):
        results = [
            {"result": "pass", "id": "a"},
            {"result": "fail", "id": "b"},
            {"result": "skip", "id": "c"},
        ]
        score = harness._calculate_score(results)
        assert score == 50.0

    def test_mixed_scores_average_correctly(self, harness):
        results = [
            {"result": "pass", "id": "a"},
            {"result": "warn", "id": "b"},
            {"result": "fail", "id": "c"},
        ]
        score = harness._calculate_score(results)
        assert score == 50.0

    def test_warn_scores_50(self, harness):
        results = [
            {"result": "warn", "id": "a"},
            {"result": "warn", "id": "b"},
        ]
        score = harness._calculate_score(results)
        assert score == 50.0

    def test_empty_relevant_returns_100(self, harness):
        results = [
            {"result": "skip", "id": "a"},
            {"result": "skip", "id": "b"},
        ]
        score = harness._calculate_score(results)
        assert score == 100.0


class TestContentInverted:
    def test_clean_file_passes(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/00-core/core-full.md"
        )
        check = [c for c in result["checks"] if c["id"] == "no-weak-language"][0]
        assert check["result"] == "pass", (
            f"Expected pass for weak language check, got {check['result']}"
        )

    def test_weak_language_detected(self, harness):
        content = "# Test\n\nYou should be careful and think deeply about this.\n"
        results = harness._run_checks(content, "test.md")
        check = [c for c in results if c["id"] == "no-weak-language"][0]
        assert check["result"] == "warn", (
            f"Expected warn for weak language, got {check['result']}"
        )
        assert check["details"]["count"] >= 2


class TestPlaceholders:
    def test_file_with_placeholders_gets_warn(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/02-engineering/code-reviewer.md"
        )
        check = [c for c in result["checks"] if c["id"] == "defined-placeholders"][0]
        assert check["result"] == "warn", (
            f"Expected warn for placeholder check, got {check['result']}"
        )

    def test_file_without_placeholders_gets_skip(self, harness):
        content = "# Simple Prompt\n\nJust a prompt with no placeholders.\n"
        results = harness._run_checks(content, "test.md")
        check = [c for c in results if c["id"] == "defined-placeholders"][0]
        assert check["result"] == "skip", (
            f"Expected skip, got {check['result']}"
        )


class TestRiskCondition:
    def test_high_risk_file_triggers_human_review_check(self, harness):
        result = harness.evaluate_file(
            "reflective-prompt-library/05-domain/high-risk.md"
        )
        check = [c for c in result["checks"] if c["id"] == "has-human-review"][0]
        assert check["result"] != "skip", (
            "Human review check should NOT be skipped for high-risk file"
        )

    def test_low_risk_file_skips_human_review_check(self, harness):
        content = "# Simple Prompt\n\nA basic prompt.\n"
        results = harness._run_checks(content, "test-low-risk.md")
        check = [c for c in results if c["id"] == "has-human-review"][0]
        assert check["result"] == "skip", (
            f"Human review check should be skipped for low-risk, got {check['result']}"
        )


class TestCustomRubric:
    def test_custom_rubric_overrides_default(self):
        custom = {
            "version": "1.0",
            "checks": [
                {
                    "id": "custom-check",
                    "name": "Custom Check",
                    "severity": "error",
                    "patterns": [r"## Custom"],
                    "match": "heading",
                }
            ],
        }
        h = EvalHarness(repo_root=REPO_ROOT, rubric=custom)
        result = h.evaluate_file(
            "reflective-prompt-library/00-core/core-full.md"
        )
        assert len(result["checks"]) == 1
        assert result["checks"][0]["id"] == "custom-check"
