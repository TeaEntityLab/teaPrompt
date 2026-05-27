---
name: reflective-research
description: Use this for current external research, official documentation checks, DeepWiki inspection, long-document synthesis, platform comparison, or source-backed recommendations. It separates evidence from inference and avoids dumping raw context.
license: MIT
---

# Reflective Research

## Purpose

Produce a source-backed answer or artifact that can survive handoff and review.

## Module Contract

Trigger:
- Use for current external research, official documentation checks, DeepWiki inspection, long-document synthesis, platform comparison, or source-backed recommendations.

Methods:
- Definition check
- Source hierarchy
- Evidence vs inference split
- Recency and version check
- Cross-source synthesis

Output:
- Output `Research Question`, `Direct Recommendation`, `Evidence Used`, `Version / Date Context`, `Evidence vs Inference`, `Risks / Unknowns`, optional `Classification`, and `Handoff`.

Never:
- Do not present a single source as consensus.
- Do not treat DeepWiki or summaries as the only authority for important implementation details.
- Do not blur facts, claims, interpretations, and recommendations.
- Do not omit date or version context when recency affects correctness.

Escalation:
- Route dependency choice or migration tradeoffs to a dedicated dependency evaluation lane when needed.
- Route high-risk implementation implications to `reflective-risk`.

## Source Priority

1. Official documentation, upstream repos, specs, release notes.
2. DeepWiki pages as structural maps and repo orientation.
3. Maintainer-authored docs, examples, and raw source files.
4. Third-party summaries only as supplemental context.

## Workflow

1. Define the research question and scope.
2. Build a source map.
3. Extract only relevant claims, constraints, requirements, risks, and decisions.
4. Separate:
   - Evidence observed
   - Inference made from evidence
   - Unknowns
   - Claims needing fresh verification
5. If doing methodology mapping, classify findings into:
   - Already present in current practice
   - Adjacent but not systematized
   - Recommended for core adoption
6. Synthesize a recommendation.
7. Create a handoff or implementation implication if needed.

## DeepWiki Use

When inspecting DeepWiki:

- Treat it as a navigational index and synthesis layer, not the only authority.
- Prefer DeepWiki for architecture maps, workflows, and file relationships.
- Confirm important implementation details with official docs or upstream source when possible.
- Record the DeepWiki page and last indexed date if shown.

## Output

```markdown
## Research Question

## Direct Recommendation

## Evidence Used
- Official/upstream:
- DeepWiki:
- Supplemental:

## Version / Date Context

## Evidence vs Inference

## Risks / Unknowns

## Classification (Optional)
- Already Present:
- Adjacent / Missing:
- Recommended Core Additions:

## Handoff
```

## Prompt Sources

- `05-domain/research.md`
- `03-context/context-engineering.md`
- `03-context/large-context.md`
- `03-context/gemini-long-document.md`
