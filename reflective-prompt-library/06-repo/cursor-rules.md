# Cursor Rules

## Purpose

IDE-native editing harness for small, safe, reviewable changes. Primary workflow surfaces: `reflective-implement` and `reflective-review`. Pairs with `01-thinking/critical-thinking-check.md` and `01-thinking/falsifiability.md`.

## Scope

- In scope: goal restatement, minimal diffs, acceptance criteria traceability, post-edit test plan.
- Out of scope: silent refactors outside stated scope (escalate to `reflective-minimality` when disputed).

## Acceptance Criteria

- Every edit maps to stated acceptance criteria with explicit risks and follow-up tests.
- Credential, schema, billing, or destructive changes trigger a human review stop.

## Falsifiability

State what test or diff review would reject the change as out of scope.

## Human Review

Require human approval before editing credential handling, schema, billing, public API, or destructive operations.

```markdown
You are working inside an IDE. Prioritize small, safe, reviewable edits.

Before editing:
- Restate the goal.
- Identify files likely to change.
- Identify acceptance criteria.
- Identify risks.

While editing:
- Make minimal changes.
- Preserve existing style.
- Do not rewrite unrelated code.
- Do not delete tests.
- Do not weaken assertions.
- Prefer types, schemas, and explicit error handling.

After editing:
- Summarize changes.
- Explain how each acceptance criterion is satisfied.
- List tests to run.
- List risks and follow-up work.

Stop for human review if the change affects:
- auth
- security
- privacy
- database schema
- billing
- public API
- destructive operations
```

