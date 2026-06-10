# Harness-1 → State Ledger Adoption (Research Note)

Date: 2026-06-10
Status: Implemented (reflective-research, reflective-implement)

## Research Question

Does Harness-1 (arXiv 2606.02373) support using "the concept of CoT" to improve the
reflective skill library — and what actually transfers?

## Key Finding (and a Reframe)

The paper is **not** a CoT technique — it is close to the opposite. Its problem
statement targets transcript-as-memory:

> "Search agents are often trained as policies over growing transcripts: the model
> must decide how to search while also remembering what it has seen, which evidence
> is useful, which constraints remain open, and which claims have actually been
> checked." — abstract, arXiv 2606.02373 v1 (2026-06-01)

Its solution is to move working memory **out** of the reasoning transcript into
structured, recoverable external state, leaving the model only the semantic decisions:

> "The harness maintains recoverable search state: candidate documents, curated
> evidence, evidence links, verification records, and budget-aware context."
> — pat-jj/harness-1 README

> "The policy keeps the semantic decisions: what to search, which documents to
> inspect or curate, what claims to verify, and when the evidence is sufficient."
> — pat-jj/harness-1 README

## What Transfers to Prompt-Only Skills

A skill's "harness" is its prescribed artifacts and workflow. The prompt-level
analogue of Harness-1's externalized state is a **State Ledger** maintained
*during* the task, not just at task boundaries. Three additions were derived:

1. **State Ledger** — a running table (claim/item, source, status, open constraints)
   updated after each retrieval or edit; later steps read the ledger instead of
   re-deriving from transcript memory.
2. **Sufficiency Gate** — an explicit stopping decision ("when the evidence is
   sufficient" is a policy decision in Harness-1, so it belongs in the prompt):
   stop only when load-bearing items are verified; don't pad after the gate passes.
3. **Budget Rule** — compress raw material into the ledger and drop it; Harness-1's
   stated purpose for externalization is "long-horizon trajectories that exceed
   typical context windows" (DeepWiki).

What does **not** transfer: the RL training pipeline (SFT → RL on a 20B model).
Only the harness design transfers to a prompt library.

## What Was Changed (2026-06-10)

- `skills/reflective-research/SKILL.md`: State Ledger section
  (`unverified/verified/refuted/stale`), Sufficiency Gate before synthesis,
  Budget Rule wired to `03-context/large-context.md`, workflow steps record
  into / read from the ledger, optional final-ledger block in output template.
- `skills/reflective-implement/SKILL.md`: State Ledger
  (`pending/done/verified/failed` with evidence column; `verified` requires a
  check run **and its output read**), Sufficiency Gate (no done-before, no
  improving-after), Budget Rule for logs/failed attempts.
- Both `skills/examples/*.examples.md`: added Example 3 showing mid-task
  ledger shape.

## Evidence vs Inference

- **Evidence:** harness/policy split and the five state categories (README,
  verbatim); transcript-as-memory framed as the problem (abstract); long-horizon
  motivation, tool-mediated retrieval over ChromaDB, two-stage SFT→RL training
  (DeepWiki, indexed 2026-06-10, commit c8384c — consistent with repo layout).
- **Inference:** the mapping from code harness to prompt-prescribed ledger is our
  interpretation; the paper says nothing about prompt-only skills.
- **Caveats:** paper is v1, 9 days old, author-reported results
  (0.730 avg curated recall, +11.4 over next open subagent), no peer review or
  third-party replication. DeepWiki had a spelling artifact
  ("SearchCorusTool"/"SearchCorpusTool") — verify exact identifiers upstream
  before citing.

## Open Follow-Ups

- [ ] Eval: before/after benchmark (skill-creator loop) on a multi-source research
      task — does the ledger measurably reduce dropped constraints and
      unverified claims?
- [ ] Consider ledger pattern for `reflective-review` (claims checked vs asserted).
- [ ] Re-check Harness-1 for v2 / peer review / third-party replication before
      citing performance numbers anywhere load-bearing.

## Sources

- Paper: https://arxiv.org/abs/2606.02373 (v1, 2026-06-01)
- Repo: https://github.com/pat-jj/harness-1
- DeepWiki: https://deepwiki.com/pat-jj/harness-1 (indexed 2026-06-10, commit c8384c)
