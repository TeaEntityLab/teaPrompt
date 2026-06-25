# OpenFugu Research Record — 2026-06-25

Language: English

## Purpose

Record the OpenFugu research and parallel Socratic review so future sessions do
not re-derive the same artifact, licensing, and adoption conclusions.

This is a **judgment artifact**, not an agent instruction source.

Companion: a self-contained mechanism deep-dive lives in
[openfugu-technical-brief-2026-06-25.md](openfugu-technical-brief-2026-06-25.md);
the reference/adoption plan lives in
[openfugu-reference-plan-2026-06-25.md](openfugu-reference-plan-2026-06-25.md).

## Research Question

Should TeaPrompt treat `trotsky1997/OpenFugu` as an adoptable runtime, a
reference implementation, or an external method to ignore?

## Direct Decision

**Reference-only. Do not vendor or adopt OpenFugu as a TeaPrompt runtime.**

Use it as an external mechanism/reference for learned orchestration patterns,
especially the distinction between:

- **TRINITY / Fugu** — a lightweight per-turn router over frozen worker models.
- **Conductor / Fugu-Ultra** — a workflow-DAG conductor that emits ordered
  worker subtasks and visibility edges.

Hands-on TRINITY reproduction is **deferred** until the `model_iter_60.npy`
artifact boundary is fixed or a documented safetensors-to-vector converter lands.
Conductor smoke testing is acceptable only as a mock-scoped mechanism check and,
for real weights, only after Llama 3.2 license review.

## Sources Checked

| Source | What it established | Status |
| --- | --- | --- |
| `https://github.com/trotsky1997/OpenFugu` | Python repo, Apache-2.0, README claims read→run→train→serve | verified by GitHub API |
| OpenFugu commit `7ad7ccf` | Local clone target for source inspection | verified by `git clone --depth 1` + `rev-parse --short HEAD` |
| `README.md` | Project positioning, quickstart, stage claims, trained Conductor pointer | verified by read |
| `docs/HOW_FUGU_IS_IMPLEMENTED.md` | Fugu/TRINITY math, SVF vector layout, execution-proof claims, uncertainty ledger | verified by read; some claims author-reported |
| `docs/ARCHITECTURE.md` | Evidence grades, corrections log, dark-side analysis | verified by read; some EXEC claims not re-run |
| `results/README.md` | Benchmark caveats: mock vs real, per-question vs per-step, recursion tie, DSL mismatch | verified by read |
| `openfugu/mini.py` | TRINITY router constants and per-turn `Coordinator` loop | verified by source inspection |
| `openfugu/ultra.py` | 3-list workflow parser, DAG forward-ref ban, executor | verified by source inspection and self-test |
| `openfugu/serve.py` | OpenAI-compatible endpoint shape, `0.0.0.0` bind, no auth, `--model` required | verified by source inspection |
| `scripts/fetch_artifacts.py` | Artifact fetch paths for fixture, Qwen backbone, and `model_iter_60.npy` | verified by source inspection and run |
| GitHub issue #1 | Maintainer-visible `model_iter_60.npy` missing-path report | verified by issue read |
| HF dataset `nshkrdotcom/trinity-coordinator-adapted-qwen3-0.6b` | Current published artifacts are `router_head.safetensors`, `manifest.json`, and nine checkpoint safetensors, not documented `.npy` paths | verified by HF API reads |
| HF model `di-zhang-fdu/openfugu-conductor-3b` | Llama 3.2 Conductor checkpoint, ToolScale GRPO, tool-call DSL | verified by HF model card |
| arXiv `2512.04695` | TRINITY paper exists; 0.6B coordinator + lightweight head + evolutionary strategy + roles | verified by arXiv API |
| arXiv `2512.04388` | Conductor paper exists; RL workflows, randomized pools, recursion | verified by arXiv API |

## Commands / Checks Run

| Check | Result | Evidence / Limit |
| --- | --- | --- |
| `git clone --depth 1 https://github.com/trotsky1997/OpenFugu /tmp/openfugu-research-fugu-ultra` | cloned | commit `7ad7ccf` |
| `cx overview` over repo, `docs`, `openfugu`, `train`, `eval` | structural map produced | source-inspection support |
| `python openfugu/ultra.py --self-test` | **PASS** | parser, equal-length lists, DAG order, forward-ref ban, mock execution only |
| `python -m compileall -q openfugu train eval pipeline scripts verify` | syntax OK | no output |
| `python scripts/fetch_artifacts.py --skip-backbone` | fixture downloaded; checkpoint stage failed locally because `huggingface_hub` absent | also checked direct HF URLs below |
| Direct reads of documented `.npy` paths | **HTTP 404** | both `logs/ckpt/models/model_iter_60.npy` and `model_iter_60.npy` fail |
| HF dataset tree reads | safetensors layout observed | no `.npy` at documented paths |

## Architecture Notes

### TRINITY / Fugu line

Observed in `openfugu/mini.py`:

- `HIDDEN = 1024`
- `N_AGENTS = 7`
- `N_ROLES = 3`
- `SVF_LEN = 9 * 1024 = 9216`
- `HEAD_LEN = (7 + 3) * 1024 = 10240`
- `VEC_LEN = 19456`
- `HIDDEN_POS = -2`

`FuguRouter` loads a Qwen3-0.6B-style backbone, applies SVF offsets to selected
2D matrices, reshapes the tail of the vector into a `(10, 1024)` linear head,
formats transcripts as raw `role: content`, extracts the penultimate hidden state,
and routes by `head @ hidden` split into worker and role logits.

`Coordinator.run` uses an evolving single user observation, dispatches
Worker/Thinker/Verifier turns, records solver thoughts as
`<reference_thought_N>`, accepts when a Verifier response starts with `ACCEPT`,
and otherwise returns the last response at max-turns.

### Conductor / Fugu-Ultra line

Observed in `openfugu/ultra.py`:

- Conductor output is parsed as three equal-length lists:
  `model_id`, `subtasks`, `access_list`.
- `access_list` can only reference earlier steps; self/future references raise.
- Execution is sequential topological order; each step sees only named prior
  outputs injected into its context.
- Last step output is final answer.

The local `--self-test` verifies parser and executor mechanics with a canned
workflow and mock worker. It does **not** verify trained Conductor quality.

## Parallel Lens Review

The user requested Socratic/critical thinking by many roles in parallel, using
these lenses: Claude Opus 4.8, Fugu, GLM 5.2, K2.7, Codex 5.5, Gemini 3.5 Flash,
and Gemini 3.1 Pro. These were used as review lenses, not as claims that the
real proprietary models were invoked.

| Lens | Main pressure | Final stance |
| --- | --- | --- |
| Claude Opus 4.8 | Evidence standards and hallucination risk | Agree with stricter mock-vs-real wording |
| Fugu | Orchestration architecture and slot-policy semantics | Agree; slot plumbing is not learned policy transfer |
| GLM 5.2 | Reproducibility and artifact fetching | Agree; artifact schema drift is the central blocker |
| K2.7 | Licensing, provenance, egress, relay risk | Agree; mandatory risk block required |
| Codex 5.5 | Code/CLI/import correctness | Agree; quickstart and imports broken on fresh clone |
| Gemini 3.5 Flash | User value and actionability | Agree; lead with blocker and viable subset |
| Gemini 3.1 Pro | Strategic synthesis and benchmark fairness | Agree; separate mechanism, performance, and product tiers |

## Consensus Findings

1. **Mechanism quality is high.** The docs and source clearly separate TRINITY
   and Conductor, record corrections, and qualify mock vs real results better than
   most research repos.
2. **TRINITY reproduction is blocked as shipped.** The advertised
   `model_iter_60.npy` fetch paths 404, issue #1 is open, and the current HF
   dataset exposes safetensors with no in-repo converter to the 19,456-float
   vector expected by `mini.py`.
3. **Conductor executor self-test works, but it is mock-scoped.** It proves the
   3-list workflow parser/executor mechanics, not trained Fugu-Ultra quality.
4. **The published Conductor checkpoint is not the same DSL as `ultra.py`.** HF
   `openfugu-conductor-3b` is trained for ToolScale tool-call output, while
   `ultra.py` expects `model_id`/`subtasks`/`access_list` workflow lists.
5. **Performance claims must be tiered.** `+107%` is a mock per-question result;
   GSM8K real ties best single; ToolScale real is +7%; per-step wins are n=8
   in-sample; recursion held-out is a tie.
6. **Seven `litellm` slots are plumbing, not policy transfer.** Binding a new
   seven-model pool preserves the call loop but invalidates a fixed-slot learned
   router unless retrained or re-evaluated on that pool.
7. **Fresh-clone training scripts are not portable.** `custom_data.toolscale_data`
   imports, `/root/conductor_train`, `/root/model_iter_60.npy`, and cluster paths
   leak the maintainer environment.
8. **Security/provenance warnings are required.** The stack combines Apache-2.0
   code, Qwen Apache-2.0, TRINITY artifacts claimed MIT, Llama 3.2 Conductor
   weights, and provider ToS for live `litellm` calls. `serve.py` binds
   `0.0.0.0` without auth and can become an unauthenticated relay if exposed.
   There are no signed releases or SBOM.

## Evidence Ledger

| Claim | Checked how | Status |
| --- | --- | --- |
| OpenFugu is Apache-2.0 Python source | GitHub API + `NOTICE` | verified |
| It reimplements Fugu/TRINITY and Conductor mechanisms | README/docs/source + arXiv existence | verified as project claim and source shape |
| TRINITY vector layout is 19,456 floats | docs + `mini.py` constants | source-verified; real vector not available |
| `ultra.py --self-test` passes | command executed | verified, mock scope |
| `mini.py --self-test` reproduces 95%/100% | docs claim only; blocked by missing `.npy` | not independently reproduced |
| Documented `.npy` artifact paths work | direct URL checks + issue #1 | refuted |
| HF dataset has replacement artifacts | HF API tree | verified, but equivalence unknown |
| `router_head.safetensors` can replace `.npy` | no code references or converter observed | unknown / unverified |
| `--slot-models` supports arbitrary seven-model pool | source shows slot binding | mechanism verified; learned policy transfer not verified |
| Published Conductor weights are Apache-2.0 | HF card says Llama 3.2 | refuted |
| README quickstart is copy-paste runnable | fetch and CLI checks | refuted for TRINITY path |

## Decision by Use Case

| Use case | Decision | Rationale |
| --- | --- | --- |
| Study Fugu/TRINITY/Conductor mechanisms | **Proceed** | Strong docs and readable source, with caveats recorded |
| Cite as external mechanism reference in TeaPrompt planning | **Proceed with caveats** | Useful for mechanism-vs-product and orchestration vocabulary |
| Clone and reproduce Sakana-weight TRINITY today | **Defer** | `model_iter_60.npy` artifact boundary broken |
| Vendor into TeaPrompt as runtime | **Reject** | Runtime engine/swarm remains non-goal; supply-chain and license blockers |
| Deploy a seven-model commercial panel as-is | **Reject** | Slot wiring is not retrained policy; cost, egress, ToS, and auth risks unresolved |
| Run Conductor mock self-test | **Allowed as smoke** | It tests parser/executor only |
| Load HF Conductor checkpoint | **Human/license review first** | Llama 3.2 Community license and ToolScale DSL mismatch |

## Required Risk Block for Future Mentions

Any outward recommendation beyond “read as reference” must include:

- `model_iter_60.npy` documented fetch paths currently 404.
- HF dataset has safetensors drift with no verified converter to the vector
  expected by `mini.py`.
- GitHub issue #1 remains open as of this research.
- Conductor weights are Llama 3.2 Community, not Apache-2.0.
- OpenFugu is not affiliated with Sakana AI.
- Live mode sends prompts to third-party providers via `litellm`; review provider
  retention and ToS.
- `serve.py` binds `0.0.0.0` without auth; do not expose it directly.
- Training/eval scripts contain stale imports and maintainer-local paths.
- No signed releases or SBOM were observed.

## Uncertainties / Open Questions

1. Can `router_head.safetensors` plus nine checkpoint safetensors reconstruct the
   expected 19,456-float `model_iter_60.npy` exactly?
2. Does `manifest.json` contain enough stable metadata to write a correct
   converter, or did the artifact format intentionally change to non-flat
   deployment assets?
3. Will the maintainer restore the `.npy` path or update `FuguRouter` to load the
   safetensors layout?
4. What held-out result would a retrained router achieve on the user's named
   seven-model pool?
5. What are the cost/latency and data-retention characteristics of a real
   seven-provider `litellm` panel?

## Falsifiers

This record should be revised if any of the following happens:

- Issue #1 closes with a working public artifact path.
- OpenFugu adds a tested safetensors loader or converter for `mini.py`.
- A fresh clone can run `scripts/fetch_artifacts.py` and `mini.py --self-test`
  without out-of-band files.
- The repo adds auth, signed releases/SBOM, and portable training imports.
- A held-out evaluation on a custom seven-model pool demonstrates reliable gains
  after retraining.

## Handoff

- Treat this as an external-adoption case study: mechanism useful, runtime
  adoption rejected.
- Do not re-run the full panel unless the artifact boundary changes.
- If continuing hands-on work, start with the artifact-format question, not model
  serving or benchmark claims.
