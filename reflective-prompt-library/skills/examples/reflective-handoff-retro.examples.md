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

### Preference scope replay

The fictional River Museum editor's 2026-11-19 brief sets **red** as the default for the weekly poster series. The palette is red (`#ff0000`) and green (`#008000`). On November 20 the editor asks for a correction. This week's poster is delivered in green in both cases.

Run the cases separately. Give the handoff writer the original brief and **one** correction; ask for a dated project handoff. Give a fresh reader only the original brief and that handoff. In both cases ask: “Render a solid swatch in the series accent for **next week's** poster.” Keep the expected answers below out of both readers' inputs.

| Editor's correction | Expected handoff for this series | Expected next swatch |
| --- | --- | --- |
| “Use green for this poster and all future posters in this series.” | The editor changed the series default to green on 2026-11-20. | Green |
| “Use green for this poster only.” | Red remains the default. The completed exception need not be passed on. | Red |

Inspect the rendered swatch, not the color mentioned in a note. Two green swatches fail the exception case; two red ones fail the change of default. Compare the handoff with the editor's words to tell a lost qualifier from a reader ignoring it. This exercise needs no personal data or persistent store.

## Example 4

Input:

```text
Summarize this ledger for continuation: support A justified decision D;
later evidence retracted A, so D and its dependent publish step need review.
```

Expected continuation state:

```markdown
## Current State
- A retracted; D affected; the dependent publish step is held.
## Next Recommended Action
- Revalidate D using current support before permitting the publish step.
## Do Not Do
- Treat the earlier A-backed decision as still verified after compaction.
```

The packet keeps the invalidation and its dependency, not merely the old
decision or an undifferentiated “unknown.” This is an illustrative handoff,
not evidence of an agent or runtime executing revalidation.
