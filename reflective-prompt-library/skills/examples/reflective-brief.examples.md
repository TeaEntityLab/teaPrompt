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
The same brief as Example 1 with a vaguer prompt. The heading set is identical; assumption status and unknown-handling notes sit inside the required headings.
```text
Can we add AI to this workflow?
```

The same brief as Example 1. The ellipsis is not a shorter contract: assumption status and unknown-handling notes sit inside the required headings.

```markdown
## Goal
## Why
## Intended Outcome (JTBD)
## Assumptions
- status is `open`, `confirmed`, `refuted`, or `stale`
- reversible assumption stated explicitly
## Authority / Missing Data Notes
- missing fields are marked unknown, not inferred, and name an owner
- before any clarification, name the local evidence checked and the material fork left unresolved
## Scope
## Inputs / Outputs
## Failure Conditions
## Acceptance Criteria
## Falsifiability
## Minimal Plan
## Human Review Triggers
## Next Action
- one narrow experiment with measurable acceptance criteria
```
