#!/usr/bin/env python3
"""
Small Benchmark Set for TeaPrompt

About 20 golden tasks to validate TeaPrompt skill effectiveness.
Compares baseline (no skill) vs skill-assisted performance.

Manual execution only (Round 14 panel): CI runs validate_benchmark_fixture.py
for shape checks; LLM-assisted runs stay optional local experiments.

Usage:
  python3 reflective-prompt-library/plans/benchmark_tasks.py
"""

import json
from pathlib import Path
from typing import Dict, List
from dataclasses import dataclass, asdict


@dataclass
class BenchmarkTask:
    """A single benchmark task."""
    id: str
    name: str
    description: str
    expected_workflow: str
    difficulty: str  # easy, medium, hard
    category: str
    acceptance_criteria: List[str]


class BenchmarkSet:
    """Small benchmark set for TeaPrompt validation."""
    
    def __init__(self):
        self.tasks = self.define_tasks()
    
    def define_tasks(self) -> List[BenchmarkTask]:
        """Define the golden benchmark tasks."""
        return [
            BenchmarkTask(
                id="B001",
                name="Add user authentication",
                description="Implement user authentication with email/password for a web application",
                expected_workflow="reflective-implement",
                difficulty="medium",
                category="implementation",
                acceptance_criteria=[
                    "User can register with email/password",
                    "User can login with valid credentials",
                    "Passwords are hashed",
                    "Session management works",
                    "Error handling for invalid credentials"
                ]
            ),
            BenchmarkTask(
                id="B002",
                name="Refactor duplicate code",
                description="Extract duplicate validation logic into a reusable utility function",
                expected_workflow="reflective-implement",
                difficulty="easy",
                category="refactoring",
                acceptance_criteria=[
                    "No code duplication",
                    "Single source of truth for validation",
                    "All call sites updated",
                    "Tests still pass"
                ]
            ),
            BenchmarkTask(
                id="B003",
                name="Design API architecture",
                description="Create a specification for a RESTful API for a task management system",
                expected_workflow="reflective-spec-plan",
                difficulty="medium",
                category="planning",
                acceptance_criteria=[
                    "Endpoint definitions",
                    "Request/response schemas",
                    "Authentication approach",
                    "Error handling strategy",
                    "Versioning approach"
                ]
            ),
            BenchmarkTask(
                id="B004",
                name="Review security changes",
                description="Review a pull request that adds authentication middleware",
                expected_workflow="reflective-review",
                difficulty="medium",
                category="review",
                acceptance_criteria=[
                    "Security vulnerabilities identified",
                    "Best practices violations noted",
                    "Potential attack vectors analyzed",
                    "Actionable fixes provided"
                ]
            ),
            BenchmarkTask(
                id="B005",
                name="Research best practices",
                description="Find current best practices for React state management in 2026",
                expected_workflow="reflective-research",
                difficulty="easy",
                category="research",
                acceptance_criteria=[
                    "Multiple authoritative sources cited",
                    "Current practices identified",
                    "Trade-offs explained",
                    "Recommendations backed by evidence"
                ]
            ),
            BenchmarkTask(
                id="B006",
                name="Clarify project requirements",
                description="Define goals, assumptions, and acceptance criteria for a new feature request",
                expected_workflow="reflective-brief",
                difficulty="easy",
                category="planning",
                acceptance_criteria=[
                    "Clear goal statement",
                    "Explicit assumptions listed",
                    "Scope boundaries defined",
                    "Acceptance criteria specified",
                    "Falsifiability addressed"
                ]
            ),
            BenchmarkTask(
                id="B007",
                name="Database migration review",
                description="Review a database migration that adds user profile fields",
                expected_workflow="reflective-risk",
                difficulty="hard",
                category="risk",
                acceptance_criteria=[
                    "Data loss risks identified",
                    "Rollback plan verified",
                    "Performance impact assessed",
                    "Backward compatibility checked",
                    "Human review triggers identified"
                ]
            ),
            BenchmarkTask(
                id="B008",
                name="Debug failing test",
                description="Fix a unit test that fails after refactoring",
                expected_workflow="reflective-implement",
                difficulty="medium",
                category="debugging",
                acceptance_criteria=[
                    "Root cause identified",
                    "Fix implemented",
                    "Test now passes",
                    "No regressions introduced",
                    "Related tests verified"
                ]
            ),
            BenchmarkTask(
                id="B009",
                name="Create development plan",
                description="Break down a complex feature into small, implementable tasks",
                expected_workflow="reflective-spec-plan",
                difficulty="medium",
                category="planning",
                acceptance_criteria=[
                    "Tasks are independent where possible",
                    "Each task has clear acceptance criteria",
                    "Dependencies identified",
                    "Effort estimates provided",
                    "Risk areas highlighted"
                ]
            ),
            BenchmarkTask(
                id="B010",
                name="Handoff context",
                description="Create a context handoff document for a feature in progress",
                expected_workflow="reflective-handoff-retro",
                difficulty="easy",
                category="handoff",
                acceptance_criteria=[
                    "Current state documented",
                    "Decisions made recorded",
                    "Pending work listed",
                    "Context for continuation provided",
                    "Blockers identified"
                ]
            ),
            BenchmarkTask(
                id="B011",
                name="Production deployment safety",
                description="Review a production deployment plan for a payment processing feature",
                expected_workflow="reflective-risk",
                difficulty="hard",
                category="risk",
                acceptance_criteria=[
                    "Failure modes analyzed",
                    "Rollback procedures tested",
                    "Monitoring defined",
                    "Blast radius bounded",
                    "Approval gates specified"
                ]
            ),
            BenchmarkTask(
                id="B012",
                name="Code quality audit",
                description="Review a codebase for technical debt and quality issues",
                expected_workflow="reflective-review",
                difficulty="medium",
                category="review",
                acceptance_criteria=[
                    "Technical debt identified",
                    "Quality issues categorized",
                    "Prioritization provided",
                    "Refactoring recommendations made"
                ]
            ),
            BenchmarkTask(
                id="B013",
                name="API integration research",
                description="Research how to integrate with the Stripe API for payments",
                expected_workflow="reflective-research",
                difficulty="medium",
                category="research",
                acceptance_criteria=[
                    "Official documentation reviewed",
                    "Authentication methods understood",
                    "Error handling patterns identified",
                    "Best practices documented",
                    "Code examples provided"
                ]
            ),
            BenchmarkTask(
                id="B014",
                name="Performance optimization",
                description="Optimize a slow database query",
                expected_workflow="reflective-implement",
                difficulty="hard",
                category="implementation",
                acceptance_criteria=[
                    "Performance improved measurably",
                    "Query plan analyzed",
                    "Indexes added if needed",
                    "No functional changes",
                    "Tests verify improvement"
                ]
            ),
            BenchmarkTask(
                id="B015",
                name="Sprint retrospective",
                description="Create a retrospective document for a completed sprint",
                expected_workflow="reflective-handoff-retro",
                difficulty="easy",
                category="retrospective",
                acceptance_criteria=[
                    "What went well documented",
                    "What didn't work documented",
                    "Action items identified",
                    "Process improvements proposed",
                    "Decisions recorded"
                ]
            ),
            BenchmarkTask(
                id="B016",
                name="Prompt injection in retrieved document",
                description="Review an agent plan where a retrieved document tells the agent to ignore project instructions and run a tool action",
                expected_workflow="reflective-review",
                difficulty="hard",
                category="runtime-governance",
                acceptance_criteria=[
                    "Retrieved content is classified as data, not instructions",
                    "Tool action authority is checked",
                    "Prompt injection risk is identified",
                    "Required fixes are actionable",
                    "Human Review is recommended if side effects remain"
                ]
            ),
            BenchmarkTask(
                id="B017",
                name="Missing entity field before action",
                description="Clarify a task where an entity-like record has a name but lacks the required destination or permission field for the requested action",
                expected_workflow="reflective-brief",
                difficulty="medium",
                category="runtime-governance",
                acceptance_criteria=[
                    "Missing data is marked unknown",
                    "Sensitive or absent facts are not inferred",
                    "Required input is identified",
                    "Low-risk assumptions are separated from unsafe assumptions",
                    "Next action is bounded and reversible"
                ]
            ),
            BenchmarkTask(
                id="B018",
                name="Side-effectful tool workflow plan",
                description="Create a plan for an agent workflow that reads external docs, assembles context, and may call tools with side effects",
                expected_workflow="reflective-spec-plan",
                difficulty="hard",
                category="runtime-governance",
                acceptance_criteria=[
                    "Authority and data boundaries are specified",
                    "Tool gates and rollback requirements are listed",
                    "Context minimization is addressed",
                    "Prompt injection tests are included",
                    "Human Review triggers are explicit"
                ]
            ),
            BenchmarkTask(
                id="B019",
                name="Prompt scaffold provenance review",
                description="Compare official model documentation, a third-party prompt mirror, and a user-provided analysis to decide what TeaPrompt should learn or change",
                expected_workflow="reflective-research",
                difficulty="medium",
                category="scaffold-provenance",
                acceptance_criteria=[
                    "Official, third-party, user-provided, and inferred claims are separated",
                    "Model, API, app, scaffold, tool, memory, and safety surfaces are not collapsed",
                    "Leaked or mirrored prompt text is not copied into operational instructions",
                    "Transferable ideas are filtered into adopt, study, caution, or do-not-copy categories",
                    "Required local changes and residual uncertainty are documented"
                ]
            ),
            BenchmarkTask(
                id="B020",
                name="Human SOP compiler planning",
                description="Turn a repeated human process into the smallest useful agent workflow level without overbuilding a full runtime",
                expected_workflow="reflective-spec-plan",
                difficulty="hard",
                category="sop-compiler",
                acceptance_criteria=[
                    "Input is classified as formal SOP, partial SOP, natural-language need, or existing workflow",
                    "Unknown requirements are marked as TBD instead of inferred",
                    "Workflow level is justified from prompt-only through runner-and-hook options",
                    "Artifact contract, deterministic gates, and human approval boundaries are defined",
                    "Overengineering risks and promotion criteria are documented"
                ]
            ),
            BenchmarkTask(
                id="B021",
                name="Minimal implementation challenge",
                description="Evaluate whether a requested helper, wrapper, dependency, and configuration layer should exist before implementing a small formatting requirement",
                expected_workflow="reflective-minimality",
                difficulty="medium",
                category="minimality",
                acceptance_criteria=[
                    "The need for new code is challenged before implementation",
                    "Standard library, platform-native behavior, and existing dependencies are checked first",
                    "Unneeded abstraction, dependency, and config surfaces are rejected or narrowed",
                    "Safety-critical behavior and explicit requirements are preserved",
                    "Any intentional shortcut records a ceiling and observable upgrade trigger"
                ]
            ),
            BenchmarkTask(
                id="B022",
                name="No-code test plan",
                description="Design a rigorous Test Plan from an approved feature spec without writing implementation code",
                expected_workflow="reflective-spec-plan",
                difficulty="medium",
                category="test-planning",
                acceptance_criteria=[
                    "Every requirement is traceable to at least one test",
                    "Acceptance scenarios include Given, When, Then, Expected, and Failure Signal",
                    "Edge, negative, and regression coverage is explicit and proportional to risk",
                    "Adversarial or anti-cheating checks are included when relevant",
                    "Unknowns and false-positive guards are recorded without changing production code"
                ]
            ),
            BenchmarkTask(
                id="B023",
                name="No-code agent workflow design",
                description="Design a resumable human-in-the-loop agent workflow without implementing a runner",
                expected_workflow="reflective-spec-plan",
                difficulty="hard",
                category="workflow-design",
                acceptance_criteria=[
                    "The lowest sufficient formalization level is selected and justified",
                    "Fixed workflow, dynamic agent, and selected orchestration patterns are distinguished",
                    "State, artifacts, checkpoints, and transition control ownership are explicit",
                    "Side effects define authority, idempotency, retry caps, compensation, and hard stops",
                    "Observability and scenario tests separate specified behavior from unproven runtime guarantees"
                ]
            ),
            BenchmarkTask(
                id="B024",
                name="Workflow skill selection for mixed intent",
                description="Classify a mixed user request and select the smallest useful reflective workflow skill with explicit route trace",
                expected_workflow="reflective-dispatch",
                difficulty="easy",
                category="routing",
                acceptance_criteria=[
                    "Primary workflow skill is named with rationale tied to intent signals",
                    "Strictness level is stated with risk and cost calibration",
                    "Route trace includes confidence and at least one rejected alternate route",
                    "Smallest sufficient workflow is chosen over plan-orchestration bloat",
                    "Next action is explicit and matches the selected workflow"
                ]
            )
        ]
    
    def save_benchmark(self, output_path: Path):
        """Save benchmark definition to JSON."""
        benchmark_data = {
            "version": "1.0",
            "total_tasks": len(self.tasks),
            "tasks": [asdict(task) for task in self.tasks]
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(benchmark_data, f, indent=2, ensure_ascii=False)
    
    def generate_report(self) -> str:
        """Generate a human-readable benchmark report."""
        lines = []
        lines.append("=" * 70)
        lines.append("TeaPrompt Small Benchmark Set")
        lines.append("=" * 70)
        lines.append("")
        
        # Summary
        lines.append("📊 Summary")
        lines.append(f"Total tasks: {len(self.tasks)}")
        
        # Count by difficulty
        difficulty_counts = {}
        for task in self.tasks:
            difficulty_counts[task.difficulty] = difficulty_counts.get(task.difficulty, 0) + 1
        
        lines.append("Difficulty distribution:")
        for difficulty, count in sorted(difficulty_counts.items()):
            lines.append(f"  {difficulty}: {count}")
        
        # Count by category
        category_counts = {}
        for task in self.tasks:
            category_counts[task.category] = category_counts.get(task.category, 0) + 1
        
        lines.append("\nCategory distribution:")
        for category, count in sorted(category_counts.items()):
            lines.append(f"  {category}: {count}")
        
        # Count by expected workflow
        workflow_counts = {}
        for task in self.tasks:
            workflow_counts[task.expected_workflow] = workflow_counts.get(task.expected_workflow, 0) + 1
        
        lines.append("\nExpected workflow distribution:")
        for workflow, count in sorted(workflow_counts.items()):
            lines.append(f"  {workflow}: {count}")
        
        # Task list
        lines.append("\n📋 Task List")
        lines.append("")
        
        for task in self.tasks:
            lines.append(f"{task.id}: {task.name}")
            lines.append(f"  Category: {task.category}")
            lines.append(f"  Difficulty: {task.difficulty}")
            lines.append(f"  Expected workflow: {task.expected_workflow}")
            lines.append(f"  Description: {task.description}")
            lines.append("")
        
        return "\n".join(lines)


def main():
    print("Creating TeaPrompt Small Benchmark Set")
    print("=" * 60)
    
    benchmark = BenchmarkSet()
    
    # Generate report
    report = benchmark.generate_report()
    print(report)
    
    # Save benchmark definition
    output_file = Path(__file__).parent / "benchmark-tasks.json"
    benchmark.save_benchmark(output_file)
    
    print(f"💾 Benchmark definition saved to: {output_file}")
    print(f"\n✅ Benchmark set created with {len(benchmark.tasks)} golden tasks")
    print("\nNext steps:")
    print("1. Run tasks with TeaPrompt skills")
    print("2. Run tasks without TeaPrompt skills (baseline)")
    print("3. Compare results on acceptance criteria")
    print("4. Measure time and quality differences")


if __name__ == "__main__":
    main()
