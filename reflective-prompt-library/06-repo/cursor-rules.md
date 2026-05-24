# Cursor Rules

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

