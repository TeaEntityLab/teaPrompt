# `reflective-handoff-retro` Examples

## Example 1

Input:

```text
Prepare handoff for the next agent. I am ending this session.
```

The handoff template, including the as-of date and Acceptance Criteria. A continuation packet that drops either is not finished.

```markdown
## As-of Date
## Goal
## Current State
## Decisions Made
## Assumptions
## Files / Artifacts
## Completed Work
## Remaining Work
## Risks
## Trust Boundaries / External Data
## Blockers
## Acceptance Criteria
## Commands / Tests Run
## Next Recommended Action
## Do Not Do
## Human Review Required
```

## Example 2

Input:

```text
Run a retro on this failed release and suggest process updates.
```

Expected output shape:

```markdown
## What Went Well
## What Went Wrong
## Misunderstandings
## Wrong Assumptions
## Token or Time Waste
## Weak Gates
## Test Adequacy
## Overengineering / Underspecification
## Reusable Rules
## Skill / Script / Test Candidates
## Next Process Improvement
```

## Example 3

Input:

```text
Consolidate the durable lessons from this completed session.
```

Expected output shape:

```markdown
## Retain
- future-useful, durable, self-contained lesson
- as-of date (`YYYY-MM-DD`)
## Exclude
- live task state or lookup-recoverable fact
## Revalidate
- dated, changeable claim and its current authoritative source
```
