---
name: reflective-implement
description: Use this for coding, refactoring, debugging with edits, or repo-aware implementation tasks. It enforces small safe changes, acceptance criteria traceability, tests, verification, and a final report without weakening requirements.
license: MIT
risk_level: low
human_review_required: false
external_io: false
---

# Reflective Implement

## Purpose

Implement the smallest safe change that satisfies explicit acceptance criteria.

## Module Contract

Trigger:
- Use for coding, refactoring, debugging with edits, or repo-aware implementation work after acceptance criteria are clear enough to verify.

Methods:
- Spec before code
- Small safe changes
- Regression safety
- Tests and static checks
- Local feedback loop

Output:
- Finish with `Goal`, `Files Changed`, `Implementation Summary`, `Acceptance Criteria Status`, `Tests / Checks Run`, `Failures or Skipped Checks`, `Residual Risks`, and `Next Action`.

Never:
- Do not delete, skip, or weaken tests.
- Do not change expected outputs to match broken behavior.
- Do not widen scope beyond the acceptance criteria without a reason.
- Do not claim checks passed unless they were run and read.

Escalation:
- Route unclear requirements to `reflective-brief` or `reflective-spec-plan`.
- Route auth, permissions, security, privacy, migrations, destructive operations, billing, breaking APIs, or production deployment to `reflective-risk`.

## Before Editing

1. Read local instructions such as `AGENTS.md`, `CLAUDE.md`, or equivalent project guidance.
2. Inspect the relevant repository files before changing them.
3. Restate:
   - Goal
   - Assumptions
   - Acceptance criteria
   - Failure conditions
   - Files likely to change
4. If acceptance criteria are missing, create a brief first.
5. If the task is high-risk, run the risk gate before edits.

## During Editing

- Make the smallest reviewable change.
- Preserve existing behavior unless explicitly allowed.
- Prefer existing patterns and utilities.
- Add or update tests for each acceptance criterion.
- Do not delete, skip, or weaken tests.
- Do not change expected outputs to match broken behavior.
- Keep notes in an artifact when the task spans multiple steps.

## Verification

Run the checks that prove the claim:

- Unit tests for changed logic.
- Typecheck or lint when available.
- Integration or manual verification when user-facing behavior changes.
- Static review for security/privacy when relevant.

If verification fails, fix and rerun. If a check cannot run, report why.

## Failure Loop (LOCAL_FEEDBACK)

When blocked or failing, report and iterate with this structure:

```markdown
## Step
## Evidence
## Error Type
## Root Cause
## Correction
## Next Action
## Verification
## Anti-regression Rule
```

Use this loop until acceptance criteria are met or a hard stop requires Human Review.

## Final Report

```markdown
## Goal

## Files Changed

## Implementation Summary

## Acceptance Criteria Status

## Tests / Checks Run

## Failures or Skipped Checks

## Residual Risks

## Next Action
```

## Hard Stop

Request Human Review for auth, permission changes, security-sensitive logic, privacy-sensitive data, database migrations, destructive operations, billing/cost changes, public API breaking changes, or production deployment.

## Prompt Sources

- `02-engineering/implementation-agent.md`
- `02-engineering/test-designer.md`
- `02-engineering/local-feedback.md`
- `06-repo/codex-opencode.md`
