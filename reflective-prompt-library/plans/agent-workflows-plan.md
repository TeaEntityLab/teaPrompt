# Plan: Agent Workflows

## Goal

Define reusable agent workflows implied by the prompt library without implementing a full workflow engine yet.

## Workflow 1: Engineering Delivery

```text
Task Start
-> Spec Writer
-> Usage-first
-> Task Slicer
-> Implementation Agent
-> Test Designer
-> Code Reviewer
-> Retro
```

### Artifacts

- `spec.md`
- `usage.md`
- `task-plan.md`
- `test-plan.md`
- `review.md`
- `final-report.md`
- `retro.md`

### Gates

- Do not implement until acceptance criteria exist.
- Do not claim completion until tests or evidence are recorded.
- Do not weaken tests or acceptance criteria to pass.

### Human Review

Required for auth, security, privacy, migrations, destructive operations, billing, public API changes, or production deployment.

## Workflow 2: High-risk Change

```text
High-risk Review
-> Threat Model
-> Safe Dry-run Plan
-> Human Review
-> Implementation
-> Review
-> Rollback Check
```

### Artifacts

- `threat-model.md`
- `dry-run-plan.md`
- `rollback-plan.md`
- `approval-record.md`
- `verification-report.md`

### Stop Conditions

- No rollback path.
- No dry-run path.
- Unclear asset ownership.
- Missing authority to proceed.

## Workflow 3: Long Research

```text
Research Prompt
-> Document Map
-> Evidence Check
-> Counterargument
-> Synthesis
-> Context Handoff
```

### Artifacts

- `document-map.md`
- `evidence-map.md`
- `counterarguments.md`
- `research-summary.md`
- `handoff.md`

### Gates

- Separate evidence from inference.
- Mark claims that require current verification.
- Do not cite sources that were not actually inspected.

## Workflow 4: Agent System Design

```text
Agent Selection
-> Why / What / How / Done
-> Spec Writer
-> Usage-first
-> Task Slicer
-> Workflow Engine Plan
-> Review-Rating-Fix
```

### Artifacts

- `agent-selection.md`
- `workflow-spec.md`
- `state-model.md`
- `role-contracts.md`
- `review-rating-fix.md`

### Gates

- Prompt-only must be rejected with evidence before building an agent system.
- State model must exist before multi-step automation.
- Eval or acceptance tests must exist before autonomous execution.

## Workflow 5: Context Handoff

```text
Current Work
-> Context Engineering
-> Handoff Summary
-> Next Agent
-> Verification
```

### Artifacts

- `handoff.md`
- `decisions.md`
- `open-risks.md`
- `commands-run.md`

### Gates

- Include current state, decisions made, completed work, remaining work, blockers, and do-not-do items.
- Omit irrelevant chat history.

## Implementation Notes

- These workflows can remain manual until repetition, risk, or state-management overhead justifies automation.
- A future workflow engine should persist artifacts, enforce gates, resume safely, and produce audit logs.

