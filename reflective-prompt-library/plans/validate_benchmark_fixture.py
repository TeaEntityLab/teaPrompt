#!/usr/bin/env python3
"""
Benchmark Fixture Validator (deterministic, CI-safe)

Validates the golden-task definition in benchmark_tasks.py without running
LLM-assisted benchmark executions. This is the compromise for Round 6: reject
full benchmark-in-CI, but gate the fixture shape on every change.
"""

import json
import sys
from dataclasses import asdict
from pathlib import Path

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

VALID_DIFFICULTIES = {"easy", "medium", "hard"}
MIN_TASK_COUNT = 24


def main() -> int:
    repo_root = Path(__file__).parent.parent.parent
    plans_dir = Path(__file__).parent
    sys.path.insert(0, str(plans_dir))

    from benchmark_tasks import BenchmarkSet  # noqa: E402

    print(f"Validating benchmark fixture in: {repo_root}")
    print("=" * 60)

    benchmark = BenchmarkSet()
    errors = []

    if len(benchmark.tasks) < MIN_TASK_COUNT:
        errors.append(
            f"Expected at least {MIN_TASK_COUNT} benchmark tasks; found {len(benchmark.tasks)}"
        )

    workflows = {task.expected_workflow for task in benchmark.tasks}
    missing_workflows = VALID_WORKFLOWS - workflows
    if missing_workflows:
        errors.append(
            "Benchmark tasks missing workflows: "
            + ", ".join(sorted(missing_workflows))
        )

    seen_ids = set()
    for task in benchmark.tasks:
        if not task.id:
            errors.append("Task missing id")
            continue
        if task.id in seen_ids:
            errors.append(f"Duplicate benchmark task id: {task.id}")
        seen_ids.add(task.id)

        if task.expected_workflow not in VALID_WORKFLOWS:
            errors.append(
                f"{task.id}: invalid expected_workflow {task.expected_workflow!r}"
            )
        if task.difficulty not in VALID_DIFFICULTIES:
            errors.append(f"{task.id}: invalid difficulty {task.difficulty!r}")
        if not task.name.strip():
            errors.append(f"{task.id}: missing name")
        if not task.description.strip():
            errors.append(f"{task.id}: missing description")
        if not task.category.strip():
            errors.append(f"{task.id}: missing category")
        if not task.acceptance_criteria:
            errors.append(f"{task.id}: acceptance_criteria must be non-empty")

    # The committed JSON is a generated artifact: compare, never rewrite.
    # Rewriting here would silently heal drift between benchmark_tasks.py and
    # benchmark-tasks.json instead of failing on it.
    output_file = plans_dir / "benchmark-tasks.json"
    expected = {
        "version": "1.0",
        "total_tasks": len(benchmark.tasks),
        "tasks": [asdict(task) for task in benchmark.tasks],
    }
    if not output_file.exists():
        errors.append(
            "benchmark-tasks.json missing — regenerate with "
            "`python3 -c 'from benchmark_tasks import BenchmarkSet; "
            "BenchmarkSet().save_benchmark(\"reflective-prompt-library/plans/benchmark-tasks.json\")'`"
        )
    else:
        committed = json.loads(output_file.read_text(encoding="utf-8"))
        if committed != expected:
            errors.append(
                "benchmark-tasks.json is stale vs benchmark_tasks.py — "
                "regenerate it; the validator does not rewrite committed artifacts"
            )

    if errors:
        print(f"\n❌ {len(errors)} benchmark fixture violation(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        f"\n✅ Benchmark fixture valid: {len(benchmark.tasks)} tasks, "
        f"{len(workflows)}/{len(VALID_WORKFLOWS)} workflow skills"
    )
    print(f"📎 Committed artifact in sync: {output_file.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
