"""Tests for benchmark fixture validation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmark_tasks import BenchmarkSet  # noqa: E402
from validate_benchmark_fixture import MIN_TASK_COUNT, VALID_WORKFLOWS  # noqa: E402


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

