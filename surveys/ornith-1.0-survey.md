# Survey: Ornith-1.0 — Self-Scaffolding LLMs for Agentic Coding

> Source survey (verified 2026-06-25):
> - Blog: https://deep-reinforce.com/ornith_1_0.html
> - HF org: https://huggingface.co/deepreinforce-ai
> - HF model card: https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B
>
> Status of benchmark numbers: **maintainer-reported, not independently reproduced.**
>
> Record class: reference-only survey. Benchmark numbers are non-load-bearing for TeaPrompt workflow constraints unless independently reproduced.

---

## 1. Abstract Concepts (the reusable ideas)

These are the transferable patterns worth remembering independent of this specific release.

### 1.1 Scaffold-as-learnable-object
The agent **harness/scaffold is treated as a first-class object that is trained**, not hand-engineered and frozen. Instead of humans writing the orchestration (memory, retry, error-handling, search trajectory, tool plan), the model learns to author it.

### 1.2 Self-scaffolding RL (scaffold–policy co-evolution)
A two-stage RL step where a single model both **proposes the scaffold** and **executes the rollout** under it:
1. Given a task + the previous scaffold → propose a **refined scaffold**.
2. Given that scaffold + the task → generate a **solution rollout**.
3. Reward from the rollout is **propagated to both stages** (scaffold-authoring and solution-generating).

Effect: per-task-category orchestration strategies emerge automatically via mutation + selection toward higher-reward trajectories. The scaffold co-evolves with the policy.

### 1.3 Reward-hacking defense as a layered trust architecture
Letting the model author its own scaffold invites verifier-gaming (e.g. reading hidden test files, touching the checked-for artifact, copying an oracle solution). Defense generalizes as **three layers**:
1. **Fixed outer trust boundary** — environment, tool surface, test isolation are immutable; only the *inner* policy scaffold is mutable.
2. **Deterministic monitor** — exact-spec rule checker; flags forbidden reads / verification-script edits / out-of-surface tool calls → zero reward + excluded from advantage.
3. **Frozen LLM-judge veto** — catches *intent-level* gaming that stays within the allowed tool surface; sits **on top of** the verifier, not as the primary reward.

Abstract takeaway: **specify exactly what you can (deterministic), judge what you cannot (frozen LLM), and make the boundary itself unreachable by the learner.**

### 1.4 Staleness-weighted off-policy correction (pipeline-RL)
For long rollouts in asynchronous/pipeline RL, weight tokens by age $d_t$:
$$ w(d_t)= \begin{cases} 1, & d_t \le K_1 \\ \exp(-\lambda(d_t-K_1)), & K_1 < d_t \le K_2 \\ 0, & d_t > K_2 \end{cases} $$
Applied to a token-level GRPO objective:
$$ L_t=\min\!\big(r_t A_t,\ \mathrm{clip}(r_t,1-\epsilon^{-},1+\epsilon^{+})A_t\big)\cdot w(d_t) $$
Abstract takeaway: **fresh tokens count fully, mid-age tokens decay exponentially, stale tokens are dropped** — a graceful off-policy discount rather than a hard cutoff.

---

## 2. What Is Being Announced

DeepReinforce released **Ornith-1.0**, an MIT-licensed open-source family of **agentic-coding** LLMs, post-trained on **Gemma 4** and **Qwen 3.5** bases.

| Variant | Type | Positioning |
|---|---|---|
| Ornith-1.0-9B | Dense | edge / efficient |
| Ornith-1.0-31B | Dense | mid-size dense (named in blog; not seen in HF org listing) |
| Ornith-1.0-35B | MoE | mid-tier |
| Ornith-1.0-397B | MoE | flagship |

HF repos observed: 397B, 397B-FP8, 35B, 35B-GGUF, 9B, 9B-GGUF.

---

## 3. Benchmark Claims (maintainer-reported)

### 397B flagship
| Benchmark | Ornith-397B | Context |
|---|---|---|
| Terminal-Bench 2.1 (Terminus-2) | 77.5 | > Opus 4.7 (70.3); < Opus 4.8 (85), GLM-5.2 (81.0) |
| Terminal-Bench 2.1 (Claude Code) | 78.2 | ≈ Opus 4.8 (78.9); < GLM-5.2 (82.7) |
| SWE-Bench Verified | 82.4 | > Opus 4.7 (80.8); < Opus 4.8 (87.6) |
| SWE-Bench Pro | 62.2 | ≈ GLM-5.2 (62.1); < Opus |
| NL2Repo | 48.2 | ≈ GLM-5.2 (48.9); < Opus 4.8 (69.7) |
| ClawEval Avg | 77.1 | ≈ Opus 4.7 (78.2) |

Defensible framing: strong among open/comparable-size models, competitive with **Claude Opus 4.7** on several agentic benchmarks — but **not** the table's top model (Opus 4.8 and GLM-5.2 lead several rows).

### 9B (efficiency story)
Terminal-Bench 2.1 (Terminus-2) 43.1 · SWE-Bench Verified 69.4 · ClawEval Avg 63.1 — claimed to match/exceed much larger Gemma/Qwen models on some rows.

---

## 4. Serving / Release Facts (verified on HF)
- License **MIT**; `text-generation`; tags include `qwen3_5_moe`, `safetensors`, `transformers`.
- Reasoning model: emits `<think>...</think>`; serve with Qwen3 reasoning parser + Qwen XML/tool-call parser.
- Recipes: vLLM / SGLang, TP=8 on 8×80GB, 262k context.

---

## 5. Discrepancies / Unknowns
- **35B score mismatch**: prose 64.4 vs table 64.2 (Terminal-Bench 2.1).
- **397B doc error**: card calls 397B "lightweight ... single-GPU" yet recipe is 8×80GB TP=8 — likely copy/paste.
- **Typo** "scallfold" on the model card.
- **31B** named in blog, not visible in HF org listing checked.
- No paper-grade methodology: no ablations, datasets, compute, monitor rules, judge prompts, or attack evals.
- Benchmark comparisons depend on harness, tool budget, context, temperature, retries, timeout.

---

## 6. Bottom Line
Credible maintainer release with real HF artifacts and one genuinely distinctive thesis: **train the model to author the scaffold that guides its own coding rollouts.** Treat leaderboard claims as **strong vendor claims awaiting independent reproduction.**
