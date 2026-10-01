# `reflective-research` Examples

## Example 1

Input:

```text
Research best practices for resumable agent workflows with citations.
```

Expected output shape:

```markdown
## Research Question
## Direct Recommendation
## Evidence Used
## Version / Date Context
## Evidence vs Inference
## Risks / Unknowns
## Handoff
```

## Example 2

Input:

```text
Classify these methodology ideas into what we already do vs what to add.
```

Expected output shape:

```markdown
## Classification (Optional)
- Already Present:
- Adjacent / Missing:
- Recommended Core Additions:
```


## Example 3

Input:

```text
Does library X support streaming responses in the current stable release?
```

Expected mid-task State Ledger shape (illustrative rows showing ledger literals and freshness columns, not proof that library X was checked):

```markdown
| Claim / Item | Source | Status | Checked (date) | How (command + input set, or freshness kind) | Open Constraints |
|---|---|---|---|---|---|
| X supports streaming since v2.3 (as checked) | official changelog (example) | verified | 2026-09-30 (example) | read v2.3 changelog section (example) | |
| streaming requires async client | blog post (example) | unverified | 2026-09-30 (example) | summary only; confirm in API reference | confirm in API reference |
| v2.3 was latest stable at check time | releases page seen 2026-09-30 (example) | verified | 2026-09-30 (example) | viewed releases listing; recheck on new release (example freshness kind) | recheck if a newer release appears |
```
