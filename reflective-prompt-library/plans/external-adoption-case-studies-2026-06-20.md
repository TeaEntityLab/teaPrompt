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
| 2026-06-20 | Codex Record & Replay | OpenAI official docs | operational, not methodological | No change *to TeaPrompt* — the gap is real but operational (acquisition / persistence / replay), which is a standing non-goal; R&R is vendor-locked and uncopyable. Worth using as an external acquisition front-end | this file |
| 2026-06-21 | Hyperplan / multi-agent adversarial planning (OMO) | GitHub repo (code-yeongyu/oh-my-openagent) SKILL.md | no — runtime hits non-goals; methodology mostly covered | No change — Hyperplan runtime is agent swarm + runtime engine (both non-goals); methodology layer overlaps existing lenses; three possible gaps (Defend/Refine/Concede, Evidence Grade, Assumption Ledger) not promoted | this file |
| 2026-06-25 | OpenFugu | GitHub repo + arXiv + HF APIs + local clone | no — mechanism useful, runtime/adoption blocked by artifact, license, and egress risks | No runtime adoption; reference-only; TRINITY hands-on deferred until `model_iter_60.npy` / safetensors boundary fixed | [research](openfugu-research-record-2026-06-25.md), [brief](openfugu-technical-brief-2026-06-25.md), [plan](openfugu-reference-plan-2026-06-25.md) |
| 2026-06-25 | Skills, memory, and agent tooling survey | upstream repos/docs for Superpowers, Spec Kit, Karpathy skills/autoresearch, mem0, ChatGPT Memory, LLM Wiki, MemPalace, Hermes Agent, Oh My Pi, Oh My OpenAgent | mostly no — methodology already covered; memory/runtime surfaces are non-goals unless a local app/runtime gap appears | No new core skill, runtime, or memory dependency; keep as references and reuse existing `reflective-*` workflows plus Markdown project knowledge | [skills](skills-and-spec-systems-research-2026-06-25.md), [memory](memory-mechanisms-research-2026-06-25.md), [tooling](agent-tooling-research-2026-06-25.md) |
| 2026-07-13 | Baton / `baton-dispatch` v0.1.1 | GitHub repository/API + pinned skill/reference files + Anthropic official article | no — methodology present/adjacent; consolidated-checklist recurrence `unknown` | Study/reference only; no TeaPrompt skill, lens, verifier, dependency, or runtime adoption; empirical reproduction deferred | [survey](baton-dispatch-survey-2026-07-13.md) |
| 2026-07-13 | DilinAI Nuwa + Jiyao / team memory officer | five public share/API snapshots + platform terms + NASA, Anthropic, and Claude official sources | no — methodology present/adjacent; source-lineage recurrence `unknown`; runtime is a non-goal | Study traceability and artifact separation; no TeaPrompt prompt, skill, role, verifier, dependency, or runtime adoption; outcome reproduction and installation blocked | [survey](dilinai-nuwa-jiyao-survey-2026-07-13.md) |

## The Recurring Evaluation Procedure

This is the transferable output. When evaluating a new external tool or method:

1. **Verify from the one-hand source** (repo API, official docs), not the
   circulating summary or "N-prompts" re-telling.
2. **Separate transferable mechanism from product form.** Adopt mechanisms;
   reject runtimes, retrievers, citation pipelines, dashboards, and quotas.
3. **Gate any change on a verified *local* structural gap.** STORM had one and
   warranted a change; Loop-Skill, preflight, and Record & Replay did not, so
   they warranted none. "Interesting" is not a gap. When desired usage data
   cannot be observed, record it as `unknown`; absence of data is not zero
   demand and cannot become a permanent veto. Use the best available local
   structural evidence and prefer a bounded, reversible repair when it is
   directly testable.
4. **Check against standing non-goals** (runtime engine, vendor lock-in,
   RAG/vector store). An out-of-scope capability is not a missing capability.
5. **Apply the promotion gate only to new durable surface area** (≥3
   cross-session recurrences before a new skill, directory, runner, or similar
   surface). Prefer folding into an existing skill or a supporting lens. The
   gate does not block a narrow repair to an existing skill's declared contract.
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

## Decision-Rule Correction

The earlier rule overreached in two ways: it treated unavailable local usage
data as if it proved no demand, and it applied a promotion gate for new surface
area to an in-place repair. The corrected rule is proportional and traceable:

1. Local project authority and verified repository evidence come first.
2. Current external or official evidence is required when the claim depends on
   changing facts, unfamiliar technology, standards, comparisons, or high-risk
   guidance; it is not mandatory ceremony for self-contained repo-local facts.
3. Logic, Socratic questioning, counterargument, and critical thinking test the
   evidence and expose assumptions. They do not create evidence.
4. Unmeasurable or unavailable evidence remains `unknown` and is documented.
5. Reversibility, blast radius, cost of delay, and testability determine whether
   to implement a bounded repair, defer, or reject.
6. Every material decision records a falsifier and the check that would verify
   or overturn it.

This follows mixed-evidence guidance from
[Google Research](https://research.google/pubs/bridging-the-gap-from-research-to-practical-advice/)
and NIST's guidance to combine qualitative and quantitative methods, document
uncertainty and unmeasurable risks, and prioritize by impact, likelihood, and
available resources in the
[AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

### Applied Counterexample: Test Plan Routing

The source prompt `02-engineering/test-designer.md` declares test design without
implementation, while its only operational mapping was an implementation skill
whose trigger requires edits. Installation copies `SKILL.md`, so a Prompt
Sources pointer alone does not provide the mode to installed users. This is a
verified local structural gap. Adding a conditional no-code Test Plan mode to
`reflective-spec-plan` is a narrow, reversible, route-tested repair; it does not
create a new skill or runtime and therefore does not require three observed
sessions.

## Methodology Layer vs Operationalization Layer

Correction (2026-06-20): an earlier framing treated "the SOP Compiler spec
exists" as equivalent to "the capability exists." It is not. Two distinct layers:

- **Methodology layer** — prompts, design lenses, triggerable skills
  ([sop-compiler.md](../04-agent/sop-compiler.md),
  [reflective-review](../skills/reflective-review/SKILL.md)). TeaPrompt is
  effectively complete here.
- **Operationalization layer** — a recorder that captures a real workflow, a
  skill generator, persisted execution state, and replay verification (what
  Record & Replay does; what immutable iteration / event log / feedback reopen
  would *guarantee*). TeaPrompt deliberately does not provide this.

So "complete" is true only of the methodology layer. A source-agnostic *prompt*
does not become an acquisition or persistence *capability* by being
source-agnostic — that earlier reasoning was an overclaim. This does not flip the
decision: the operational/runtime layer stays a standing non-goal (not an
oversight), the local promotion gate is unmet, and Record & Replay is
vendor-locked and uncopyable. "Learn it" therefore means *use it externally* — its
output feeds `sop-compiler` review → `reflective-review` — not *build it in*.

## Decision

The external-adoption decision remains unchanged for Loop-Skill,
preflight-checker, and Record & Replay: do not add their runtime or a new skill.
The corrected rule does require one separate in-place repair: operationalize a
conditional no-code Test Plan mode in `reflective-spec-plan` and test its route.
Keep the adoption procedure as a lesson, not a new skill, because it is a
specialization of existing
[reflective-research](../skills/reflective-research/SKILL.md),
[reflective-minimality](../skills/reflective-minimality/SKILL.md), and
[reflective-dispatch](../skills/reflective-dispatch/SKILL.md).

The 2026-07-13 Baton survey applies the same rule: its dispatch brake and
ownership/verification vocabulary are useful reference material, but no verified
local gap or recurrence warrants a new or repaired TeaPrompt surface. The
candidate dispositions and re-evaluation triggers are recorded in the
[Baton survey](baton-dispatch-survey-2026-07-13.md).

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
| Four no-change outcomes recorded | done | Case Comparison table |
| Recurring procedure captured | done | this file + PROJECT_KNOWLEDGE Durable Lesson |
| Durable Lesson + Decision Index added | done | PROJECT_KNOWLEDGE.md |
| No new skill or directory created | done | Rejected Alternatives |
| Evidence/promotion rule corrected | done | Decision-Rule Correction |
| No-code Test Plan route repaired | done | `reflective-spec-plan` + ROUTE fixtures |
| Baton no-change outcome recorded | done | `baton-dispatch-survey-2026-07-13.md` + Case Comparison table |
| DilinAI Nuwa/Jiyao no-change outcome recorded | done | `dilinai-nuwa-jiyao-survey-2026-07-13.md` + Case Comparison table |
