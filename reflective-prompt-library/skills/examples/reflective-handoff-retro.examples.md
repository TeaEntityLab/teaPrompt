# `reflective-handoff-retro` Examples

## Example 1

Input:

```text
Prepare handoff for the next agent. I am ending this session.
```

Expected output shape:

```markdown
## Goal
## Current State
## Decisions Made
## Files / Artifacts
## Completed Work
## Remaining Work
## Risks
## Trust Boundaries / External Data
## Next Recommended Action
## Do Not Do
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
## Wrong Assumptions
## Weak Gates
## Trust-boundary lesson
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
## Exclude
- live task state or lookup-recoverable fact
## Revalidate
- dated, changeable claim and its current authoritative source
```
