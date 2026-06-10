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

Expected mid-task State Ledger shape:

```markdown
| Claim / Item | Source | Status | Open Constraints |
|---|---|---|---|
| X supports streaming since v2.3 | official changelog | verified | |
| streaming requires async client | blog post | unverified | confirm in API reference |
| v2.3 is current stable | GitHub releases | verified | |
```
