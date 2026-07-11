# Harness-1 → State Ledger Adoption (Research Note)

Date: 2026-06-10
Status: Prompt pattern implemented (reflective-research, reflective-implement); upstream Harness-1 performance claims remain author-reported and non-load-bearing until independently replicated

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

- [ ] Eval: before/after benchmark (skill-creator loop) — **iteration 1 done
      2026-06-10**: 3 research tasks × (new skill vs pre-ledger skill).
      Result: new skill 18/18 assertions, old 15/18; all three old-skill
      failures were the missing verification-status ledger; cost +~2.5% tokens,
      +6s. Caveat: both configs passed all factual-trap assertions, so
      iteration 1 proves the ledger appears reliably at negligible cost but NOT
      that it prevents real errors. Remaining: (a) user review of iteration-1
      outputs (workspace: /tmp/reflective-research-workspace), (b) iteration 2
      with adversarial tasks (conflicting sources, planted misinformation)
      where dropped constraints actually occur.
      **Iteration 2 done 2026-06-10** (adversarial: planted false premises on
      Python 3.13 GIL/asyncio; 6-constraint Caddy-vs-nginx with a rate-limit
      direction trap; MySQL 8.4 claims needing tier qualification). Result:
      new skill 18/18, old 15/18 — identical pattern to iteration 1; the only
      discriminator is ledger presence. **Both configs passed every factual
      trap**, so two iterations consistently show the ledger adds auditability
      (explicit refuted/needs-qualification statuses) at +2–11% tokens, with
      no measured error-rate difference at this task difficulty. Conclusion:
      keep the ledger for auditability and handoff legibility; do not claim
      error-prevention benefits without harder evidence (e.g., longer-horizon
      tasks where context actually overflows, or noisier source environments).
      User review of both iterations pending in the eval viewer.
- [x] Ledger pattern for `reflective-review` — added 2026-06-10 as Claims Ledger
      (`asserted/verified/refuted/unverifiable`), motivated by the CoT
      faithfulness literature (reasoning narratives are not verification records).
- [ ] Re-check Harness-1 for v2 / peer review / third-party replication before
      citing performance numbers anywhere load-bearing.
      (Checked 2026-06-10: still v1, no replication or critique found — only
      launch coverage (MarkTechPost, Digg, HF papers page). New detail: built on
      `openai/gpt-oss-20b`; paper calls the pattern "stateful cognitive
      offloading". Re-check in a month or two.)
      (Re-checked 2026-07-02: still v1 on arXiv (2606.02373); no peer review,
      third-party replication, or critique found. Material change: authors
      released the full checkpoint and training data on 2026-06-15 — weights at
      https://huggingface.co/pat-jj/harness-1, code at
      https://github.com/pat-jj/harness-1, 899 SFT trajectories, 3,453 RL SEC
      train examples, corpus shards. Reproducibility standing improved;
      performance numbers remain author-reported. Next re-check when citing
      numbers anywhere load-bearing.)
- [x] Read in full: NLAH (arXiv 2603.25723) and the externalization review
      (arXiv 2604.08224) — done 2026-06-10; positioning section in both
      methodology maps deepened with NLAH's five harness-policy design
      principles and the review's ledger success criterion ("did we make the
      current decision legible?"). Key extra findings:
      - NLAH explicitly cites AGENTS.md / CLAUDE.md / SKILL.md as inspiration;
        NLAH docs ≈ code harnesses on SWE-bench Verified / Terminal-Bench 2.0
        at 10–20x fewer policy tokens (e.g., 60.1k → 2.9k).
      - NLAH limitation relevant to us: parent→child Information Handoff Recall
        drops from 1.00 (direct context) to 0.322–0.553 — supports keeping
        handoff artifacts explicit (`reflective-handoff-retro`).
      - Externalization review's skill failure modes worth a future audit pass
        over this library: semantic alignment, portability/staleness, unsafe
        composition, context-dependent degradation.
- [x] Verify CoT-faithfulness numbers against the papers (done 2026-06-10):
      - arXiv 2602.11201 **verified** — abstract states "a consistent Reasoning
        Horizon (k*) at 70--85% of chain length, beyond which reasoning tokens
        have little or negative effect on the final answer" (metric: NLDD).
      - arXiv 2603.26410 **refuted** — the "87.5% vs 28.6%" figures from the
        search summary do NOT appear in the abstract. Actual abstract figures:
        55.4% of divergence cases have hint keywords in thinking tokens that the
        visible answer omits; 0.5% reverse. Do not cite 87.5/28.6 anywhere.
        (Object lesson: search-layer summaries can fabricate statistics — the
        Claims Ledger rule exists for exactly this.)
> **Standing constraint (not a task):** reddit.com blocks Anthropic's crawler —
> community surveys must rely on secondary sources or manual browsing.

## Sources

- Paper: https://arxiv.org/abs/2606.02373 (v1, 2026-06-01)
- Repo: https://github.com/pat-jj/harness-1
- DeepWiki: https://deepwiki.com/pat-jj/harness-1 (indexed 2026-06-10, commit c8384c)
