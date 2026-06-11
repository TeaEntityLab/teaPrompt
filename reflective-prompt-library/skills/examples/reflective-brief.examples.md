# `reflective-brief` Examples

## Example 1

Input:

```text
I want to improve API performance but I am not sure where to start.
```

Expected output shape:

```markdown
## Goal
## Why
## Intended Outcome (JTBD)
## Assumptions
## Authority / Missing Data Notes
## Scope
## Inputs / Outputs
## Failure Conditions
## Acceptance Criteria
## Falsifiability
## Minimal Plan
## Human Review Triggers
## Next Action
```

## Example 2

Input:

```text
Can we add AI to this workflow?
```

Expected output shape:

```markdown
## Goal
...
## Assumptions
- reversible assumption stated explicitly
## Authority / Missing Data Notes
- missing fields are marked unknown, not inferred
## Next Action
- one narrow experiment with measurable acceptance criteria
```
