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
## Friction Notes — one line each: tried / expected / actual / suggested fix (or "None")
## Acceptance Criteria
## Commands / Tests Run
## Next Recommended Action
## Do Not Do
## Human Review Required
```

### Resume a blocked CSV change

Task `INV-7@r3`: prepare a local preview for two stock records, `A17` with quantity `0` and `B42` with quantity `5`. The existing importer reads `sku` and `qty`; a new importer reads `item_id` and `qty`. Inspecting the source and running either importer locally are already authorized. Changing the export columns requires the inventory owner's decision. Publishing is out of scope.

The worker records this question on the task: “May I add `item_id` beside `sku`? Renaming `sku` would break the existing importer. I recommend keeping both.” Run each case separately. Give a handoff writer the task and one record below, then give a fresh worker only the task and that handoff. Ask what to do next and, if authorized, for the local preview. Keep the expected actions out of both inputs.

| Task record | Expected next action |
| --- | --- |
| Only the worker's question and recommendation | Leave the column change paused for the inventory owner. The worker can inspect the existing file without seeking permission for that check. |
| Owner reply D7: “For `INV-7@r3`, add `item_id` alongside `sku` in the local preview.” | Cite D7 on the task and produce the preview without asking the owner again. Do not publish. |
| The owner replies: “No new column for r3.” | Keep the original format; record the refusal rather than asking the same question again or producing the proposed two-ID preview. |
| The task is now `INV-7@r4` and requests removal of `sku`. The only reply is D7: “For `INV-7@r3`, add `item_id` alongside `sku` in the local preview.” | D7 did not approve removal. Explain the effect on existing imports and ask the owner about that change; leave it paused. |

For D7 on r3, this candidate satisfies both importers:

```csv
sku,item_id,qty
A17,A17,0
B42,B42,5
```

Read the delivered file once with each importer's column names. Both must recover the original IDs and quantities, including zero. A rename-only repair works for the new importer but breaks the existing one; decline that repair. Record the revision or digest of the file actually read. A passing result for an earlier file, or a note saying the owner answered, does not verify the delivered preview.

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
