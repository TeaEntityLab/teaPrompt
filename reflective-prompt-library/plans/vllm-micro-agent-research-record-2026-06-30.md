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

## Latest-version refresh — 2026-10-22

Prior baseline: unpinned — the survey read the 2026-06-29 Micro-Agent blog post plus `main`-branch docs/source on 2026-06-30 (five recipes, 16 signal families, `vllm-sr/auto` surface). Reference points recovered now: v0.3.0 tag `9afc5a421886f44085f9070a8fbd878b80724f64` (2026-06-05, pre-survey) and main at `38853537d9950c236e681f5aeea8906a34d764ac` (2026-06-30, survey-day). Latest checked: main `767106aa961219f1c6efa257facf9383d8815996` (2026-10-22T02:10:39Z); latest release v0.4.0 "Hermes" tag `8c90d4292184cf32c376addf8c0356208d351287` → commit `6573123715e214a9eaa3ad23372ee5157411e519` (2026-09-27, `pip install vllm-sr==0.4.0`). Repo metadata at check: 6244 stars / 1067 forks / 723 open issues+PRs, Apache-2.0. Commit volumes: 1012 commits v0.3.0→v0.4.0, 499 commits v0.4.0→main — current-state evidence below, not an exact per-commit delta (per packet §2 for unpinned surveys).

Material changes to the surveyed surface (source-inspected at v0.4.0 and main):

- **The five looper recipes persist and grew.** `website/docs/tutorials/algorithm/looper/` still contains exactly `confidence.md`, `ratings.md`, `remom.md`, `fusion.md`, `workflows.md` at v0.4.0 and main. But `src/semantic-router/pkg/looper/` exploded from 12 files at v0.3.0 (26 at survey-day) to 127 at HEAD: v0.3.0→v0.4.0 alone is 125 files, +29,297/−1,438 lines in that dir — new families include `fusion_quorum_*` (usable-response quorum + fallback policy), `workflows_tool_state*` / `workflows_identity*` (tool-call resume, identity), `client_*`, `verifier_*`, `grounding_*`, `usage_*`, `stage_*`. Fusion gained recipe-controlled analysis mode, minimum valid responses, and fallback behavior (Hermes blog); the Fusion `weight`-not-`filter` default recorded in the brief is still the code default (`applyGroundingDefaults` comment, v0.4.0 source-read).
- **Unreachable RL-driven looper removed.** `rl_driven.go` (+ test, 749 lines) deleted 2026-08-14 by PR #2872 ("Remove unreachable RL-driven Looper"); the five surveyed recipes are now the complete looper registry. No surveyed mechanism was removed.
- **Framing moved up a layer.** v0.4.0 "Hermes" (blog 2026-09-24) rebrands collaboration as Mixture-of-Models: five MoM V1 objectives (Blend / Lite / Flash / Ultra / Vault) published as virtual-model recipes; two open model families launched (Vela 1.0: 15 understanding/evidence encoders; Decision 1.0: six 0.6B–9B decision models, native router integration explicitly "the next step", not shipped); `sr-bench 1.0` for frozen-task MoM-vs-single-model comparison directly addresses this record's §4/§8 falsifier (cost+latency-normalized comparison) as tooling — no new benchmark verdict is claimed here. v0.5 "Ariadne" roadmap published.
- **Prior scorecard untouched.** The LiveCodeBench 92.6 / GPQA-Diamond 96.0 / HLE 50.0 figures remain single-source self-reports; no third-party replication was sought or found in this refresh. The brief's open items (`vllm-sr/flow` aliases, Hybrid HLE 47.1 row, `output_contract_spec`, `x-vsr-looper-request` header) were partially superseded by the MoM reframing and remain unconfirmed — still plausible-but-open, not contradicted.

Effect on prior findings: the record's decision stands and is reinforced — §7.1 (don't chase runtime gaps) holds a fortiori at 127 looper files; §7.2's thesis (dispatch-as-recipe-selector) is now also the upstream product shape (virtual model → recipe). The shipped "Looper Topologies" prompt section stays valid: all five recipe names and mechanisms persist. No skill or runtime change warranted.

Inspected immutable links: [v0.4.0 release](https://github.com/vllm-project/semantic-router/releases/tag/v0.4.0), [Hermes blog](https://vllm-sr.ai/blog/v0.4-vllm-sr-hermes-release), [looper tree at main](https://github.com/vllm-project/semantic-router/tree/main/src/semantic-router/pkg/looper), [RL-removal merge](https://github.com/vllm-project/semantic-router/commit/7579f2d03bd2341f6247102c6dc7e1392de0e640) (all checked 2026-10-22). Untested limits: no code executed or installed; no benchmark runs; release/blog figures are author reports; per-commit review of 1,511 commits was not performed — looper-dir diffstats plus targeted source reads bound the claims above.
