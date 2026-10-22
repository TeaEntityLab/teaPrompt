# Survey: Ornith-1.0 — Self-Scaffolding LLMs for Agentic Coding

> Source survey (verified 2026-06-25):
> - Blog: https://deep-reinforce.com/ornith_1_0.html
> - HF org: https://huggingface.co/deepreinforce-ai
> - HF model card: https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B
>
> Status of benchmark numbers: **maintainer-reported, not independently reproduced.**
>
> Record class: reference-only survey. Benchmark numbers are non-load-bearing for TeaPrompt workflow constraints unless independently reproduced.
>
> Refresh pointer (2026-10-22): the team renamed `deepreinforce-ai` → [`ornith-ai`](https://huggingface.co/ornith-ai) and moved the blog to `ornith.ai`; old model-card URLs redirect, the old org URL 404s. A 7th 1.0 repo (`Ornith-1.0-35B-FP8`) exists that the 2026-06-25 survey did not list. The org's current lead release **Ornith-1.5** (397B/122B/35B-A3B/9B) is surveyed current-only in the same refresh section below. No adoption boundary changed.

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

---

## Latest-version refresh — 2026-10-22

**Baseline:** 2026-06-25 prose survey; no exact commit/SHA pins were recorded, so
there is no old pin to diff against — all identities below are **current-only**.
Unchanged claims below mean "matches the prior prose record," not "byte-identical
to a pinned revision."

**Upstream identity moves (verified this session):**

| Old reference | Current state |
|---|---|
| Blog `https://deep-reinforce.com/ornith_1_0.html` | HTTP 301 → `https://ornith.ai/ornith_1_0.html` (content matches prior record: same tables, same 64.4-prose-vs-64.2-table mismatch) |
| HF org `https://huggingface.co/deepreinforce-ai` | HTTP 404 (org renamed) |
| HF card `.../deepreinforce-ai/Ornith-1.0-397B` | HTTP 307 → `https://huggingface.co/ornith-ai/Ornith-1.0-397B` |
| HF org identity | `ornith-ai` ("Ornith"), whose org card states "We're the DeepReinforce team" |

**Current 1.0-family pins** (HF API `sha` + `lastModified`, main branch; no tags/releases on HF model repos):

| Repo | SHA | Last modified |
|---|---|---|
| `ornith-ai/Ornith-1.0-397B` | `5e3e761811e804c295c1d3c0ce68b21da6154209` | 2026-06-25T15:23:42Z |
| `ornith-ai/Ornith-1.0-397B-FP8` | `8b61f97a8512d9d01bff1a9625c9a16730e115bb` | 2026-06-25T15:24:53Z |
| `ornith-ai/Ornith-1.0-35B` | `5df2ed3f675c7beaa490328cc70bb573b65fb660` | 2026-06-25T14:30:28Z |
| `ornith-ai/Ornith-1.0-35B-FP8` | `1ab57ce0b44950e498a88756f40ad1ed4d0f30ca` | 2026-06-26T03:49:39Z |
| `ornith-ai/Ornith-1.0-35B-GGUF` | `383064f72a1ef3087b779f268d3ca117eb989aac` | 2026-07-18T03:15:03Z |
| `ornith-ai/Ornith-1.0-9B` | `83dc1f5e24ef8527af019a6b3bf66ac0f1c2c999` | 2026-06-25T14:08:32Z |
| `ornith-ai/Ornith-1.0-9B-GGUF` | `3296bc7a404871a72ac3f1903f561459c09b5c17` | 2026-06-25T14:12:12Z |

**Material delta vs the prior prose record:**

- `Ornith-1.0-35B-FP8` is a **7th family repo** the 2026-06-25 survey did not list
  (prior: 6 repos). Its `lastModified` (2026-06-26) postdates the prior survey.
- `Ornith-1.0-35B-GGUF` `lastModified` (2026-07-18) also postdates the prior
  survey; without an old SHA its content delta is **unknown** (current files: 5
  GGUF quants Q4_K_M → bf16). All other repos' timestamps fall on the prior
  survey date, consistent with (but not proof of) no change.
- `Ornith-1.0-31B` is **still absent** from the org (API returns the
  nonexistent-repo 401; family listing has exactly the 7 repos above).
- The 397B card text still carries the recorded defects verbatim ("scallfold"
  typo, 397B called "lightweight ... single-GPU", stale `deepreinforce-ai/`
  idents in `license_link` and serve recipes) — card prose unchanged since the
  prior survey's description.
- Benchmark numbers on the moved blog are unchanged (397B: 77.5 TB-2.1 /
  82.4 SWE-Bench Verified; 9B: 43.1 / 69.4). Status stays **maintainer-reported,
  not independently reproduced**.

### Ornith-1.5 — current release survey (current-only, 2026-10-22)
+
The org's current lead release is **Ornith-1.5** ("From Self-Scaffolding to
Self-Improvement"), blog `https://ornith.ai/ornith_1_5.html`. No prior
TeaPrompt record of 1.5 exists, so everything below is **current-only**; 1.0
comparisons quote the maintainer's own 1.0-column figures where the 1.5
sources carry them.
+
**Release / model identities (HF `ornith-ai`, MIT, `qwen3_5_moe`, main-branch
SHAs, no tags/releases):** 29 repos across four base scales —
397B-MoE, **122B-MoE (new scale, released 2026-10-21, i.e. yesterday)**,
35B-A3B-MoE, 9B-Dense — each with FP8 / NVFP4 / GGUF / DFlash / MLX
quant variants. Base-repo pins:
+
| Repo | SHA | Last modified |
|---|---|---|
| `Ornith-1.5-397B` | `8f6cc8a7aea505364523f84ccf37706e8aea0ee7` | 2026-08-23T06:21:27Z |
| `Ornith-1.5-122B` | `7681ef608624e7532d8164128bcffdbdbaf1b1af` | 2026-10-21T08:29:30Z |
| `Ornith-1.5-35B-A3B` | `10fbf86fed7e…` (full in receipt) | 2026-08-23T03:17:39Z |
| `Ornith-1.5-9B` | `489cb97981b8…` (full in receipt) | 2026-08-23T06:24:01Z |
+
Notable quant pins: `397B-NVFP4@065b3455` (2026-10-20), `122B-NVFP4@f049036f`
/ `122B-FP8@40f77767` / `122B-GGUF@8d5893d7` (all 2026-10-21),
`35B-A3B-FP8@b93dbd81` (2026-10-20), `9B-GGUF@abdd624b` (2026-08-24, 5.0M
downloads, the family's most-pulled repo). The 1.5 lineage claim per the
cards: built on Qwen3.5/Gemma4 with continued pretraining, mid-training, and
post-training. The 1.5 cards use current `ornith-ai/` idents (the stale
`deepreinforce-ai/` links of the 1.0 cards are fixed here).
+
**Claimed method change vs 1.0:** the loop expands from two stages (scaffold →
rollout) to three (task → scaffold → rollout). The model proposes
progressively harder tasks from an environment/codebase plus its own
solving history, authors the scaffold/harness, and produces rollouts; rollout
reward propagates across all three stages and every stage is optimized with
GRPO. New reward machinery: task reward `R_task = V × D × N` (validity /
frontier-difficulty with target success rate p\*=0.2 / novelty-vs-buffer) and
harness reward `R_harness = C × F × H` (task alignment / reward fidelity /
hack resistance); rollouts are scored by the generated harness. Transferable
delta for the §1 concept list: **self-generated curriculum with
frontier-difficulty targeting** (p\*≈0.2 Gaussian) layered on the 1.0
scaffold-as-learnable-object thesis. No paper, ablations, datasets, compute,
or monitor/judge prompts are published — same methodology opacity as 1.0.
+
**Claimed benchmark deltas vs 1.0** (all maintainer-reported, 5-run averages
unless noted; not independently reproduced):
+
| Scale | Headline 1.5 claim | Maintainer's 1.0 column |
|---|---|---|
| 397B | TB-2.1 86.1 (Terminus-2) / 85.2 (Claude Code); SWE-Verified 86.0; **DeepSWE 56.0**; HLE-tools 56.1; ClawEval 81.4 — "on par with Claude Opus 4.8" | 77.5 / 78.2; 82.4; **8.0**; 47.5; 77.1 |
| 122B (new) | TB-2.1 81.2; CyberGym 80.0; SWE-Verified(non-hack) 84.5; ClawEval 79.4; card claims single-GPU + `122B-Mobile` edge variant | n/a (no 1.0 counterpart) |
| 35B-A3B (3B active) | TB-2.1 67.8/68.5; SWE-Verified 79.0; DeepSWE 22.0 | 64.2/62.8; 75.6; 0 |
| 9B | TB-2.1 46.2/47.0; SWE-Verified 70.6; `9B-Mobile` iPhone/Android claim | 43.1/40.6; 69.4 |
+
New benchmark surfaces in 1.5 tables (no 1.0 rows to compare): DeepSWE,
Frontier-Bench v0.1, HLE, GPQA-Diamond, MCP-Atlas, Toolathlon-Verified,
WideSearch, BrowseComp, SciCode, CyberGym. The 122B card uses "(non-hack)"
SWE variants and its table header names a 397B-scale "Beam (501B)"
comparator. The 122B card has a minor typo ("efficient.member").
Neither `122B-Mobile` nor `9B-Mobile` appears as an HF repo — the Mobile
variants are card/blog claims only, with no pinned artifact.
+
**1.5 availability subrow:** all four base repos + quants resolve live with
the SHAs above; 122B family published 2026-10-21 (1 day before this refresh).
No code/training-data release beyond weights, cards, chat templates, and the
two blog posts. Untested limits: no weights downloaded, nothing executed;
SHAs are metadata pins, not content audits; eval harnesses (Terminus-2,
OpenHands, Claude Code, mini-SWE-agent) not run.

**Effect on prior findings:** none for the 1.0 record. The transferable concepts (§1), benchmark
table (§3), serving facts (§4), and discrepancy list (§5) all still match the
live sources. Ornith-1.5 adds one transferable concept delta (self-generated
curriculum with frontier-difficulty targeting) recorded above, reference-only.
Adoption boundary unchanged: reference-only, no installed change.

**Inspected links:** moved 1.0 blog URL above; 1.5 blog `https://ornith.ai/ornith_1_5.html`;
`https://huggingface.co/ornith-ai`;
`https://huggingface.co/api/models/ornith-ai/Ornith-1.0-{397B,397B-FP8,35B,35B-FP8,35B-GGUF,9B,9B-GGUF,31B}`;
`https://huggingface.co/api/models?author=ornith-ai&search=Ornith-1.0&limit=100`;
`https://huggingface.co/api/models/ornith-ai/Ornith-1.5-{397B,397B-NVFP4,397B-FP8,397B-GGUF,397B-DFlash,122B,122B-NVFP4,122B-FP8,122B-GGUF,122B-MLX,35B-A3B,35B-A3B-NVFP4,35B-A3B-FP8,35B-A3B-GGUF,35B-A3B-DFlash,35B-A3B-MLX,9B,9B-NVFP4,9B-GGUF,9B-DFlash,9B-MLX}`;
`https://huggingface.co/api/models?author=ornith-ai&search=Ornith-1.5&limit=100`;
raw READMEs of `Ornith-1.5-{397B,122B,9B}` (card heads + 122B table rows parsed).

**Untested limits:** no weights downloaded, nothing executed; SHAs are metadata
pins, not content audits. No prior SHA exists, so "unchanged" for
same-timestamp repos is timestamp-consistent, not proven.
