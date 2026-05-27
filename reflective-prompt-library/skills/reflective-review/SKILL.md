---
name: reflective-review
description: Use this to review code, diffs, specs, plans, AI outputs, articles, or decisions. It combines critical thinking, counterargument, test integrity, spec traceability, and actionable required fixes.
license: MIT
---

# Reflective Review

## Purpose

Find what would make the artifact fail in real use, then recommend the smallest useful fix.

## Module Contract

Trigger:
- Use to review code, diffs, specs, plans, AI outputs, articles, decisions, or methodology claims.

Methods:
- Requirement traceability
- Assumption audit
- Evidence and test integrity check
- Steelman counterargument
- Fallacy, overengineering, and reward-hacking scan

Output:
- Output `Findings`, `Traceability`, `Required Fixes`, `Decision`, and `Residual Risks`.

Never:
- Do not bury serious findings behind a summary.
- Do not accept unsupported claims as evidence.
- Do not treat missing tests or weak acceptance criteria as style issues.
- Do not rewrite the artifact unless the task asks for edits.

Escalation:
- Mark `Human review required` when safety, privacy, financial, legal, medical, destructive, or irreversible risk is present.
- Route implementation fixes to `reflective-implement` after review.

## Review Flow

1. Identify the original requirement and acceptance criteria.
2. Extract the artifact's major claims or behavior.
3. Check correctness against the requirement.
4. Audit assumptions.
5. Check evidence and test integrity.
6. Steelman the strongest counterargument.
7. Scan for overengineering, reward hacking, and missing edge cases.
8. Give a decision.

## Review Modes

Choose one mode first, then apply the common review flow:

- `Code Review`: correctness, regressions, tests, security/privacy, maintainability.
- `Plan/Spec Review`: scope clarity, acceptance criteria quality, sequencing, missing gates.
- `Methodology Review`: classification quality, strictness mismatch, framework overreach.
- `AI Output Review`: evidence quality, unsupported claims, hallucination risk, actionability.

If the artifact spans multiple modes, declare a primary mode and list secondary checks.

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
