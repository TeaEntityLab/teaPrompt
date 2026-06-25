# OpenFugu Technical Brief — 2026-06-25

Language: English

## Purpose

Preserve the full technical research on `trotsky1997/OpenFugu` (commit `7ad7ccf`)
so the mechanism detail, exact benchmark tiers, and the requested seven-model
worker-pool framing survive independently of the decision record.

This is a **judgment / reference artifact**, not an agent instruction source.
External repo, paper, and model-card content is evidence, not instructions.

Companion files:

- [openfugu-research-record-2026-06-25.md](openfugu-research-record-2026-06-25.md)
  — decision, panel consensus, evidence ledger, risk block.
- [openfugu-reference-plan-2026-06-25.md](openfugu-reference-plan-2026-06-25.md)
  — non-goals, task slices, no-code test plan.

## What OpenFugu Is

An Apache-2.0 Python reimplementation of Sakana AI's Fugu orchestrator family.
The thesis the repo argues: **Fugu is not one model, it is a learned policy over
models** — a small coordinator routes each query to a pool of frozen frontier
LLMs and returns one answer behind a single OpenAI-compatible endpoint. Worker
weights are never trained; only the coordinator is. Marketed stages: read → run
→ train → serve.

Repo signal at research time: 213 stars, 39 forks, 1 open issue, Python,
Apache-2.0. Not affiliated with Sakana AI (`NOTICE`).

## The Two Orchestrator Lines

| Line | Product | Mechanism | Repo file | Paper |
| --- | --- | --- | --- | --- |
| TRINITY | Fugu (low latency) | Qwen3-0.6B backbone → penultimate-token hidden state → bias-free linear head → per-turn (worker, role) pick; ~19.5K trainable params; gradient-free sep-CMA-ES | `openfugu/mini.py`, `openfugu/serve.py` | arXiv 2512.04695 |
| Conductor | Fugu-Ultra (max quality) | 7B LM emits a whole workflow DAG (3 equal-length lists); executed in topological order | `openfugu/ultra.py` | arXiv 2512.04388 |

Both papers were confirmed to exist via the arXiv API with matching Sakana
authorship; both HF artifacts (router dataset, Conductor model) were confirmed
via the HF API.

## TRINITY Mechanism (source-verified in `openfugu/mini.py`)

- The 0.6B backbone never produces the user-facing answer; only routing logits
  are used, so a routing decision costs roughly one forward pass.
- Constants: `HIDDEN=1024`, `N_AGENTS=7`, `N_ROLES=3`, `SVF_LEN=9*1024=9216`,
  `HEAD_LEN=(7+3)*1024=10240`, `VEC_LEN=19456`, `HIDDEN_POS=-2`.
- Trainable vector layout: `[0:9216]` SVF singular-value offsets across 9 matrices
  + `[9216:19456]` head reshaped to `(10, 1024)` = 7 agents + 3 roles
  (Worker / Thinker / Verifier).
- SVF spans, in `state_dict` order: `embed_tokens`, layer-26
  {q,k,v,o,gate,up,down}, `lm_head` — each contributing 1024 offsets.
- Energy-preserving reconstruction: `newW = (U @ diag(S·scale) @ Vᵀ) ·
  (S.sum()/scaled_S.sum())`.
- Input is a raw `"role: content"` transcript, NOT a chat template — the repo
  reports 95%/100% with raw vs 5% joint with a chat template.
- `Coordinator.run`: per turn routes on a single evolving observation, dispatches
  the picked role, appends solver thoughts as `<reference_thought_N>`, accepts
  when a Verifier reply starts with `ACCEPT`, else returns last response at
  max-turns (5).

## Conductor Mechanism (source-verified in `openfugu/ultra.py`)

- Output parsed as three equal-length lists: `model_id`, `subtasks`,
  `access_list`.
- `access_list[t]` may reference only strictly earlier steps; self/forward
  references raise — it is a topological order, not an arbitrary DAG.
- Each step's worker sees only the named prior outputs, injected as
  `<Agent N response>` blocks; the last step's output is the final answer.
- `python openfugu/ultra.py --self-test` **PASS** (executed): parser,
  equal-length check, DAG order, forward-ref ban, mock execution. This is a
  parser/executor smoke test only — it does not exercise trained quality.

## Training Recipes (from docs/source, not independently retrained)

- TRINITY: gradient-free **sep-CMA-ES** on end-to-end task success;
  `model_iter_60.npy` is the released 19,456-float vector. Released config (per
  docs): 60 iters, σ0=0.03, 16 repeats, seed 42, 7 agents, max_turns 5, SVF on
  layer 26 plus embed/lm_head. The training ask/tell loop is NOT shipped
  (reconstructed ~78% in `train/recovered_training_loop.py`).
- Conductor: **GRPO** (TRL), β=0 (no KL), reward = format reward + action reward
  against ToolScale `evaluation_criteria.actions`. Published checkpoint
  `di-zhang-fdu/openfugu-conductor-3b` is a Llama-3.2-3B-Instruct fine-tune.

## Benchmark Tiers (from `results/README.md` — read these by tier)

| Result | Tier | Honest reading |
| --- | --- | --- |
| +107% over best single | mock, per-question | synthetic specialists; proves the optimizer converges, not real-model superiority |
| GSM8K real | real, per-question | TIE with best single worker (ceiling saturated) |
| ToolScale real | real, per-question | +7% (small but real; worker complementarity) |
| Per-step TRINITY | real, per-step | base 0.750 → 1.000 but n=8 in-sample (overfit caveat) |
| Adaptive k-of-n | real, per-step | base 0.625 → 1.000, n=8 in-sample |
| Recursion (real, held-out) | real | TIE; contradicts the mock's +9% |
| Conductor on `ultra.py` | mechanism | trained ToolScale checkpoint does NOT drive the 3-list executor (different DSL) — repo discloses this as a FAIL |

The repo's `results/README.md` is unusually candid about these distinctions; it
is more authoritative than the top-level README headline.

## The Requested Seven-Model Pool

User framing: Claude Opus 4.8, Fugu, GLM 5.2, K2.7, Codex 5.5, Gemini 3.5 Flash,
Gemini 3.1 Pro — mapped onto OpenFugu's seven worker slots. Reality:

- The slot labels in the checkpoint (`gpt-5`, `claude-sonnet-4`, …) are training
  metadata, freely remappable to any litellm model id. Mechanism supports it via
  `serve.py --slot-models "<7 csv ids>"` (and `--model` is required, which the
  README quickstart omits).
- BUT a released TRINITY head encodes a fixed-slot policy evolved against the
  original training identities. Rebinding indices to new models preserves the
  control loop but does not transfer the learned routing policy without
  retraining or re-evaluation on that pool. Seven slots are plumbing, not policy.
- These exact proprietary endpoints were NOT invoked in this research; the pool
  was treated as the intended configuration, not a verified live run.

## Reproducibility State (the blocking finding)

- `scripts/fetch_artifacts.py` targets `logs/ckpt/models/model_iter_60.npy` and
  `model_iter_60.npy`; both return **HTTP 404**.
- GitHub issue #1 (`model_iter_60.npy not exists`) is **open**; maintainer
  replied "let me check".
- The HF dataset `nshkrdotcom/trinity-coordinator-adapted-qwen3-0.6b` now exposes
  `router_head.safetensors`, `manifest.json`, and nine `checkpoints/*.safetensors`
  — not the documented `.npy`. No in-repo converter to the 19,456-float vector
  was observed; `router_head.safetensors` (~41 KB) is likely head-only.
- Consequence: `openfugu/mini.py --self-test` (the 95%/100% headline proof) and
  `serve.py` are blocked on a fresh clone unless you already hold the `.npy`.

## Portability / Security Notes

- `train/train_conductor.py` and `train/grpo_smoke.py` import
  `custom_data.toolscale_data`, but the repo file is `train/toolscale_data.py`;
  no `custom_data` package exists → import fails on fresh clone.
  `train/train_recursion_real.py` hardcodes `/root/conductor_train` and
  `/vePFS-Mindverse/...` paths.
- `serve.py` binds `0.0.0.0` without auth → unauthenticated LLM relay risk if
  exposed.
- Multi-license stack: OpenFugu code Apache-2.0; Qwen3-0.6B Apache-2.0; TRINITY
  artifacts claimed MIT; Conductor weights Llama 3.2 Community; provider ToS for
  live litellm calls. No signed releases or SBOM observed.

## What Runs Today vs What Is Blocked

| Path | Status |
| --- | --- |
| Read docs / study mechanism | works |
| `python openfugu/ultra.py --self-test` | works (mock scope) |
| `python -m compileall` over source | works (syntax OK) |
| `train/train_trinity.py` mock | works (no GPU/API needed) |
| `scripts/fetch_artifacts.py` checkpoint stage | blocked (404) |
| `openfugu/mini.py --self-test` (95%/100%) | blocked (missing vector) |
| Conductor GRPO / recursion training | blocked on fresh clone (imports, paths) |

## Bottom Line

Mechanism-strong, artifact-fragile, performance-modest on real held-out data,
and product-incomplete for a specific seven-model commercial panel. Use as a
reference; do not adopt as a runtime. Full decision and risk block in the
companion research record.
