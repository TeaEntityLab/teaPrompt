# External-Adoption Case Studies — 2026-06-20

## Dispatch

Synthesize the recent "should TeaPrompt adopt this external tool/method?"
evaluations into one case study, and capture the recurring evaluation procedure
so future sessions do not re-derive it from scratch or re-litigate settled
outcomes.

## Why This Record Exists

Each individual evaluation correctly produced a small or null change. This record
is not a duplicate of them: it captures the pattern *across* them — the same
evaluation method, re-run each session, plus the fact that three outcomes had no
record and would otherwise be re-litigated. The synthesis crosses the project's
own promotion gate (≥3 cross-session recurrences); the individual tools did not.

## Case Comparison

| Date | External item | One-hand source verified | Verified local gap? | Outcome | Record |
| --- | --- | --- | --- | --- | --- |
| 2026-06-13 | agentic-sop-to-work | repo + CHANGELOG | concept under-specified | Adopt SOP-compiler concept at prompt layer; defer runner | [agentic-sop](agentic-sop-workflow-reflection-2026-06-13.md) |
| 2026-06-17 | Knowie | repo | no project-rationale layer | Adopt minimal project-knowledge contract; reject full toolchain | [knowie](knowie-project-knowledge-reflection-2026-06-17.md) |
| 2026-06-18 | STORM / Co-STORM | README + NAACL/EMNLP papers | **yes** — no question-space expansion | Fold optional perspective-discovery into `reflective-research` | [storm](storm-perspective-discovery-reflection-2026-06-18.md) |
| 2026-06-20 | Loop-Skill | GitHub API (created 2026-06-17, no LICENSE, 19★, single-day) | no | No change — methodology complete, runtime is a non-goal, gate unmet | this file |
| 2026-06-20 | preflight-checker | GitHub API (created 2026-06-19, no LICENSE, 0★, 0.1.0) | no | No change — UX patterns already in `reflective-review`; missing items out of scope | this file |
| 2026-06-20 | Codex Record & Replay | OpenAI official docs | no | No change — out of scope (vendor lock-in non-goal); `sop-compiler` intake already source-agnostic; does not close the runtime gap | this file |

## The Recurring Evaluation Procedure

This is the transferable output. When evaluating a new external tool or method:

1. **Verify from the one-hand source** (repo API, official docs), not the
   circulating summary or "N-prompts" re-telling.
2. **Separate transferable mechanism from product form.** Adopt mechanisms;
   reject runtimes, retrievers, citation pipelines, dashboards, and quotas.
3. **Gate any change on a verified *local* structural gap.** STORM had one and
   warranted a change; Loop-Skill, preflight, and Record & Replay did not, so
   they warranted none. "Interesting" is not a gap.
4. **Check against standing non-goals** (runtime engine, vendor lock-in,
   RAG/vector store). An out-of-scope capability is not a missing capability.
5. **Apply the promotion gate** (≥3 cross-session recurrences before a new skill
   or directory). Prefer folding into an existing skill or a supporting lens.
6. **Record the outcome — including "no change"** — so the next session does not
   re-evaluate a settled item.
7. **No-copy boundary:** until an upstream repo carries a license, learn the
   concept only; do not copy text, checklists, or code.

## Signal Accounting (do not miscount)

Two external tools now point at the same deferred runtime: agentic-sop-to-work
and Loop-Skill. These are **external signals**. They do **not** advance the
**local** promotion gate for a runner, which counts at least three real local
workflows (each repeated ~5×, with observed drift or rework). Keep the two counts
separate: external interest is not local evidence. The runner stays deferred.
See the runner gate in [agentic-sop](agentic-sop-workflow-reflection-2026-06-13.md).

## Decision

No code or skill change. Record the three previously-unrecorded outcomes
(Loop-Skill, preflight, Record & Replay) here, add one Durable Lesson and one
Decision Index entry to [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md), and keep
the evaluation procedure above as the reusable artifact. The procedure lives as a
lesson, not a new skill, because it is a specialization of existing
[reflective-research](../skills/reflective-research/SKILL.md),
[reflective-minimality](../skills/reflective-minimality/SKILL.md), and
[reflective-dispatch](../skills/reflective-dispatch/SKILL.md).

## Rejected Alternatives

- A new `reflective-adopt` skill or `evaluation/` directory: rejected —
  promotion gate met for *recording the procedure*, not for new surface area;
  the Durable Lesson "prefer a source doc or lens over a new core skill" applies.
- A dispatch route for "external-tool evaluation": rejected — it is research +
  minimality, already routable today.
- Per-tool reflection files for the three no-change cases: rejected — they would
  near-duplicate the agentic-sop runner-defer logic; one consolidated case study
  carries the only non-duplicate content (the procedure and signal accounting).

## Falsifiability

This record is wrong if the procedure is never consulted on the next external
evaluation, or if a future tool reveals a real local gap that this synthesis
caused us to dismiss. Either signal means promote the procedure into a lens (or a
skill) or correct the gap. Until then it stays a lesson plus this case study.

## State Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Three no-change outcomes recorded | done | Case Comparison table |
| Recurring procedure captured | done | this file + PROJECT_KNOWLEDGE Durable Lesson |
| Durable Lesson + Decision Index added | done | PROJECT_KNOWLEDGE.md |
| No new skill/dir/route created | done | Rejected Alternatives |
