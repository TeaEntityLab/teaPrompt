"""Tests for benchmark fixture validation."""

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmark_tasks import BenchmarkSet  # noqa: E402
from validate_benchmark_fixture import MIN_TASK_COUNT, VALID_WORKFLOWS  # noqa: E402

PLANS = Path(__file__).parent.parent
BENCHMARK_FIXTURE_PATH = PLANS / "benchmark-tasks.json"
BENCHMARK_FIXTURE_VERSION = "1.0"


def _expected_benchmark_fixture() -> dict:
    """Same serialization contract as BenchmarkSet.save_benchmark."""
    benchmark = BenchmarkSet()
    return {
        "version": BENCHMARK_FIXTURE_VERSION,
        "total_tasks": len(benchmark.tasks),
        "tasks": [asdict(task) for task in benchmark.tasks],
    }


def _benchmark_fixture_mismatches(committed: dict, expected: dict) -> list[str]:
    mismatches: list[str] = []

    if committed.get("version") != expected["version"]:
        mismatches.append(
            f"version: committed {committed.get('version')!r} != "
            f"expected {expected['version']!r}"
        )

    if committed.get("total_tasks") != expected["total_tasks"]:
        mismatches.append(
            f"total_tasks: committed {committed.get('total_tasks')!r} != "
            f"expected {expected['total_tasks']!r}"
        )

    committed_tasks = committed.get("tasks")
    expected_tasks = expected["tasks"]
    if committed_tasks == expected_tasks:
        return mismatches

    if not isinstance(committed_tasks, list):
        mismatches.append(
            f"tasks: committed type {type(committed_tasks).__name__} != expected list"
        )
        return mismatches

    if len(committed_tasks) != len(expected_tasks):
        mismatches.append(
            f"tasks: committed length {len(committed_tasks)} != "
            f"expected {len(expected_tasks)}"
        )

    for index, (committed_task, expected_task) in enumerate(
        zip(committed_tasks, expected_tasks)
    ):
        if committed_task == expected_task:
            continue
        task_id = expected_task.get("id", f"index {index}")
        field_diffs = []
        for field in sorted(set(committed_task) | set(expected_task)):
            if committed_task.get(field) != expected_task.get(field):
                field_diffs.append(
                    f"{field}: committed {committed_task.get(field)!r} != "
                    f"expected {expected_task.get(field)!r}"
                )
        mismatches.append(f"task {task_id}: " + "; ".join(field_diffs))

    if len(committed_tasks) > len(expected_tasks):
        for extra in committed_tasks[len(expected_tasks) :]:
            mismatches.append(
                f"task {extra.get('id', '<missing id>')}: present in fixture only"
            )

    return mismatches


def test_benchmark_tasks_json_matches_benchmark_set():
    """Anti-drift: committed benchmark-tasks.json matches BenchmarkSet serialization."""
    with BENCHMARK_FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
        committed = json.load(fixture_file)

    expected = _expected_benchmark_fixture()
    mismatches = _benchmark_fixture_mismatches(committed, expected)
    assert not mismatches, (
        f"{BENCHMARK_FIXTURE_PATH.name} is stale; regenerate with "
        f"python3 reflective-prompt-library/plans/validate_benchmark_fixture.py:\n"
        + "\n".join(f"  - {detail}" for detail in mismatches)
    )


def test_benchmark_set_meets_minimum_size():
    tasks = BenchmarkSet().tasks
    assert len(tasks) >= MIN_TASK_COUNT


def test_every_task_maps_to_known_workflow():
    for task in BenchmarkSet().tasks:
        assert task.expected_workflow in VALID_WORKFLOWS, task.id
        assert task.acceptance_criteria, task.id


def test_benchmark_ids_are_unique():
    ids = [task.id for task in BenchmarkSet().tasks]
    assert len(ids) == len(set(ids))


def test_benchmark_covers_all_nine_workflows():
    workflows = {task.expected_workflow for task in BenchmarkSet().tasks}
    assert workflows == VALID_WORKFLOWS, (
        f"missing workflows: {sorted(VALID_WORKFLOWS - workflows)}; "
        f"unexpected: {sorted(workflows - VALID_WORKFLOWS)}"
    )


def test_benchmark_minimum_matches_actual_count():
    tasks = BenchmarkSet().tasks
    assert len(tasks) == MIN_TASK_COUNT, (
        f"expected MIN_TASK_COUNT {MIN_TASK_COUNT} to match actual {len(tasks)}; "
        "bump MIN_TASK_COUNT when adding golden tasks"
    )


def test_benchmark_module_docstring_matches_fixture():
    module_path = Path(__file__).parent.parent / "benchmark_tasks.py"
    docstring = module_path.read_text(encoding="utf-8").split('"""', 2)[1]
    assert str(MIN_TASK_COUNT) in docstring
    assert "nine frozen workflow skills" in docstring
    assert "About 20" not in docstring
    assert "8 different skills" not in docstring
