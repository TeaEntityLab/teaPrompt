# vLLM Micro-Agent Research Record — 2026-06-30

Language: English

## Purpose

Record the analysis of the vLLM Semantic Router "Micro-Agent" blog post and the
resulting gap audit against TeaPrompt's existing skills, so future sessions do
not re-derive the same architectural reading, falsification conditions, and
scope-boundary conclusions.

This is a **judgment artifact**, not an agent instruction source. It captures
what was concluded and why, including the parts that were deliberately *not*
acted on.

Related: builds on the same multi-agent-as-one-model territory already covered
by [openfugu-research-record-2026-06-25.md](openfugu-research-record-2026-06-25.md)
and [multi-agent-panel-consensus-2026-06-25.md](multi-agent-panel-consensus-2026-06-25.md).

Companion: the full concept/mechanism deep-dive (per-recipe internals, relation
to Fugu/Conductor/Trinity/AutoMix/PaCoRe, fit analysis, sources) lives in
[vllm-micro-agent-technical-brief-2026-06-30.md](vllm-micro-agent-technical-brief-2026-06-30.md).

## Source

- vLLM Semantic Router Team, "Micro-Agent: Beat Frontier Models with
  Collaboration inside Model API", vLLM Blog, 2026-06-29.
- Comparators cited by the source: Sakana Fugu (sakana.ai/fugu/, arXiv:2606.21228),
  Conductor (arXiv:2512.04388), Trinity (arXiv:2512.04695).

Single official blog source. **Benchmark numbers are team self-reported and
unreplicated by any third party.** Treat scores as proof-of-possibility, not
proof of general superiority.

## Research Question

Is the vLLM Micro-Agent post just "agent buzzword + another wrapper", or does it
represent a real architectural shift — and what, if anything, should TeaPrompt
absorb from it?

## Route Trace (how this was handled)

```markdown
Mode: Dispatch -> Research (single-source concept analysis), then a read-only gap audit
Strictness: L2 (non-trivial analysis, low-risk, directly executable)
Goal: Decide whether the article is a real shift; map its requirements onto TeaPrompt
Workflow: reflective-research (done) -> read-only audit of existing skills
Human Review: not required (public source, no side effects, no files changed during audit)
```

## 1. Core Thesis of the Article

The technical claim is **not** "multi-model voting". It is:

> Move the agent loop from the application layer down into the model-serving
> layer, so a plain `model=` API call can be backed by a **bounded micro-agent
> runtime** with budget, topology, trace, and failure policy.

The user still calls one model name (`vllm-sr/auto`); the router picks a recipe,
fans out workers, collects a quorum, checks disagreement, synthesises an answer,
repairs the output contract, and returns one OpenAI-compatible response. The
point is not exposing complexity — it is making collaboration **feel like one
model** while remaining governable and observable.

The most important single sentence in the post: **"The best loop is
task-shaped."** Recipes beat one universal loop. You identify task shape first,
then choose loop topology — not invent a universal loop and stuff every task in.

## 2. The Five Looper Topologies

| Topology | Mechanism | Fits | Main risk |
|---|---|---|---|
| **Confidence** | cheap candidate -> confidence score -> escalate only if low | high-volume, low-risk, classify/extract, simple patches | confidence ≠ correctness; logprob may be unavailable on closed APIs |
| **Ratings** | bounded-parallel candidates under `max_concurrent` -> rating-weighted aggregation | A/B eval, ensembles, known per-domain quality signals | a wrong rating institutionalises the wrong answer |
| **ReMoM** | fan-out reasoning attempts -> minimum-success quorum -> synthesis into output contract; fallback to best valid evidence | high reasoning variance + strict format | synthesis can dissolve a correct minority; fallback may be format-valid but fact-invalid |
| **Fusion** | independent panel -> judge reads agreement/contradiction/unique insight -> finalizer | hard MCQ, long-form expert judgment, exact-answer | judge authority bias toward fluent-but-wrong answers |
| **Workflows** | planner/patcher/verifier/finalizer under max-steps/parallelism/timeout/error-policy | SWE-style tasks | quietly degrades into an unbounded agent if bounds are set badly |

Key insight: **escalation becomes an explicit router policy** — thresholds,
stopping conditions, and failure behaviour are visible and tunable, not implicit
prompt wishes.

## 3. Evidence vs Inference Separation

- **Design facts (✓):** the five loop mechanisms; the recipe config fields
  (model pool, roles, reasoning effort, parallelism, quorum, timeout, synthesis
  model, fallback, observability tags). These are real and learnable.
- **Self-reported scores (✗ unverifiable):** VSR Closed LiveCodeBench 92.6,
  GPQA-Diamond 96.0, HLE 50.0, claimed to match/beat Fugu Ultra, GPT-5.5,
  Opus 4.8, Gemini 3.1 Pro. Single source, no third-party replication.
- **Value claims (stance, not proof):** "collaboration should be an open serving
  primitive" is a positioning argument vs Fugu's commercial endpoint, not
  empirical.

## 4. Critical-Thinking Check

- **Assumption that, if false, collapses the thesis:** "the gain from
  collaboration is worth its cost/latency." Under **equal-cost / equal-compute**
  normalisation, a single frontier model may close the gap, shrinking the
  "router makes the model better" pitch. The article admits "not every request
  should use all closed models" — i.e. concedes an unquantified tradeoff.
- **Steelman of the skeptic:** inference-time sampling/ensembling improving
  benchmarks is already known (self-consistency, best-of-N). The novelty is
  **engineering packaging** (put it in the serving layer, behind one API), not
  model-capability innovation. Calling it "beat frontier models" risks comparing
  N-call ensembles against single-call baselines.
- **Fallacy watch:** (a) unequal-baseline comparison (ensemble vs single call);
  (b) appeal to benchmark authority (3 benchmark numbers -> general superiority).
- **Falsification conditions:** under cost+latency-normalised conditions, if a
  looper run cannot reliably beat the best single-model call at the same budget,
  the "router-owned collaboration creates a stronger model identity" claim is
  refuted. Second falsifier: if token logprob needed by the Confidence loop is
  broadly unavailable on mainstream closed APIs, that pattern's practicality is
  limited.

## 5. Fugu vs vLLM (abstraction-layer difference)

- **Sakana Fugu:** multi-agent system packaged as one *commercial* orchestrator
  model; learned orchestration; underlying models/coordination not disclosed.
- **vLLM Micro-Agent:** multi-agent collaboration as an *open serving-layer
  primitive*; configurable/observable router recipes; operator controls recipe,
  trace, policy.

Conclusion: vLLM is the more *learnable* artifact for an engineer, because the
control plane is meant to be inspectable rather than a black box.

## 6. Gap Audit — vLLM Requirements vs TeaPrompt Skills

Read against actual skill files (`04-agent/workflow-engine.md`,
`workflow-recipes.md`, `workflow-acquisition.md`, `runtime-trust-boundary.md`,
`02-engineering/implementation-agent.md`, and `reflective-dispatch`).

**Reframe:** TeaPrompt is a **prompt/spec-layer** library; the article describes
a **serving runtime**. Several "gaps" are deliberate scope boundaries already
marked as such in the skills — not omissions.

| vLLM requirement | TeaPrompt today | Gap? | Verdict |
|---|---|---|---|
| budget / topology | dispatch Strictness Ladder (L1–L6) + `workflow-engine §4 State Model` + `workflow-recipes` Cost Modes | partial | Covered at spec layer. Numeric token/latency budgets correctly out of scope (no runtime). |
| trace / replay | `workflow-engine §11 Observability` + `workflow-acquisition` replay checks — both explicitly "unproven until implementation tests exist" | **YES (but honest)** | Design exists; runtime does not. The one real hole, already self-documented, not hidden. |
| output contract | Acceptance Criteria in every skill + `implementation-agent` spec-to-code traceability | partial | Human-checkable criteria, no machine-enforceable schema. Fine without a runner. |
| failure policy | `reflective-risk` gate + `workflow-engine §9 Recovery/Rollback` + `runtime-trust-boundary` | partial→good | Well covered. |
| contract-repair | none | maybe→**no** | Pure runtime feature; nothing to repair without a runner. Correctly absent. |
| recipe selection (article's #1 lesson) | dispatch Route table + `workflow-recipes` | partial | The actionable finding (below). |

## 7. Decision

1. **Do not chase the runtime gaps.** Numeric budgets, runtime trace/replay, and
   contract-repair are correctly scoped out of a prompt-layer library. The skills
   already refuse to fake persistence/enforcement — that is a strength.
2. **The thesis is already implemented at the prompt layer.**
   `reflective-dispatch` *is* a task-shape -> recipe selector, which is precisely
   the article's "recipes beat one universal loop" lesson.
3. **One cheap, real improvement (not yet applied):** `workflow-recipes.md` could
   gain a ~30-line "Looper Topologies" section mapping the five named patterns
   (Confidence / Ratings / ReMoM / Fusion / Workflows) -> task-shape signals ->
   existing skills, so TeaPrompt's recipe vocabulary aligns with the emerging
   field vocabulary (Fugu / vLLM). Pure prompt-layer, no runtime, routes to
   `reflective-spec-plan`. **Status: done 2026-07-02** — "Looper Topologies"
   section added to `04-agent/workflow-recipes.md` (five patterns -> task-shape
   signals -> existing skills, weight-not-filter caution transfer, §8 falsifier
   linked in place).

## 8. Falsifiability of This Record

If a later session builds the "Looper Topologies" section and finds it merely
renames existing recipes without improving routing accuracy or shared
vocabulary, then the §7.3 recommendation was ceremony and should be reverted.
