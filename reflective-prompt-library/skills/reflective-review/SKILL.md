---
name: reflective-review
description: Use this to review code, diffs, specs, plans, AI outputs, articles, or decisions. It combines critical thinking, counterargument, test integrity, spec traceability, and actionable required fixes.
---

# Reflective Review

## Purpose

Find what would make the artifact fail in real use, then recommend the smallest useful fix.

## Review Flow

1. Identify the original requirement and acceptance criteria.
2. Extract the artifact's major claims or behavior.
3. Check correctness against the requirement.
4. Audit assumptions.
5. Check evidence and test integrity.
6. Steelman the strongest counterargument.
7. Scan for overengineering, reward hacking, and missing edge cases.
8. Give a decision.

## For Code Review

Prioritize findings by severity:

- Critical: security or data-loss risk.
- High: likely bug or acceptance failure.
- Medium: maintainability, edge case, test gap.
- Low: minor clarity or style issue.

Lead with findings. Include file and line references when available.

## Traceability Table

```markdown
| Acceptance Criteria | Artifact Evidence | Test Evidence | Status |
| --- | --- | --- | --- |
```

## Decision

Use one:

- Approve
- Comment
- Request changes
- Reject
- Human review required

## Output Shape

```markdown
## Findings

## Traceability

## Required Fixes

## Decision

## Residual Risks
```

## Prompt Sources

- `01-thinking/critical-thinking-check.md`
- `01-thinking/counterargument.md`
- `02-engineering/code-reviewer.md`
- `04-agent/review-rating-fix.md`

