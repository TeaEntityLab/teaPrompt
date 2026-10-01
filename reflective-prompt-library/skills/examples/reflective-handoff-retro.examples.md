# `reflective-handoff-retro` Examples

## Example 1

Input:

```text
Prepare handoff for the next agent. I am ending this session.
```

Proportional subset of the handoff template; it keeps the non-optional continuation state (assumptions, blockers, commands/tests, Human Review) that the Never clause forbids losing.

```markdown
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
