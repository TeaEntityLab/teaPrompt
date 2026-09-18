# Decision-Model Survey — `dsif2012/Qwen3-4B-Instruct-2507-Decision` and its two inspirations (2026-09-18)

> **Status: decided — record-only; no installed change, no wording adopted.** The object is a pasted zh-TW announcement for a "decision-oriented" inference interface over `Qwen/Qwen3-4B-Instruct-2507` (score candidates from logits instead of generate-then-parse), inspired by TypeSafe's Jev / System One Models post and the `harshatheg/Qwen-2.5-1B-RLCD` parallel-constrained-decoding experiment. All four cited sources were read on 2026-09-18. The paste's claims about its own artifact check out (it is an inference interface, not a trained model; BOOLEAN + CHOICE only; confidence and margin returned; Apache-2.0). Two corrections to the paste's framing: it expands "RLCD" as "Parallel Constrained Decoding" — the decoding experiment's own card never uses the acronym, while TypeSafe's post defines RLCD as *Reinforcement Learning for Calibrated Decisions*, a training method, so the paste conflates two different things sharing one acronym — and it calls the Qwen-2.5 card "1B" where the card's base model is `Qwen2.5-1.5B-Instruct`. Eight concepts mapped against installed TeaPrompt surfaces: every one is already covered or a decided non-goal. Clean-room throughout; surveyed vocabulary is guarded out of installed surfaces.

## Research Question

User instruction: "Survey:" followed by the pasted announcement (Traditional Chinese; four links; a closing invitation to star the repo). Two questions: (1) does the announcement describe its sources and its own artifact accurately; (2) does any concept expose a verified gap on an installed TeaPrompt surface. A bare "survey" carries no adoption direction; the standing bar applied per candidate: a verified gap on one installed surface, a named failure the change defends against, a smaller alternative rejected, and a deterministic guard.

## Direct Recommendation (as of 2026-09-18)

- **Study: yes, briefly.** The artifact is a clean statement of a real pattern — when a step needs only a decision, score an enumerated candidate set rather than generate prose and parse it — and the two inspirations bracket its honest scope: TypeSafe trained a model for this (proprietary, early access); the Qwen-2.5 experiment and this package get the same interface from stock weights at inference time.
- **Reproduce: not undertaken.** Serving needs vLLM on CUDA/Linux; nothing was executed. The Space demo was not driven. Benchmark numbers on both inspiration cards are author-claimed.
- **Adopt: nothing.** The prompt-level half of the pattern — typed verdicts over explicit candidate sets, emitted as the whole output — is already installed across the verdict contracts, the dispatch route table, and the panel consensus rows. The model-side half (logit access, KV-cache broadcast, calibration, trained heads) is a runtime TeaPrompt does not own and does not want (P7: no owned runtime; packs stay out of route fixtures).
- **Deploy: not applicable to TeaPrompt.** For the author's own systems the package is plausibly useful; that is outside this record's scope.
- **Corrections for the author** (the paste reads as the author's own announcement): (a) "RLCD" names two different things in the two inspirations — TypeSafe's training method and, by the paste's own coinage, the decoding experiment, whose card calls itself "Parallel Constrained Decoding" and never uses the acronym; (b) the Qwen-2.5 card's base model is the 1.5B instruct, not 1B; (c) "decision-oriented 實驗版本" is accurate — the HF card itself says "inference interface … does not ship new weights", so "model" in the title oversells slightly; (d) TypeSafe's "can't hallucinate" is schema-scoped (no type errors), not a correctness claim — worth keeping distinct when citing them.

## Method

Coordinator reads (2026-09-18): the TypeSafe announcement post in full; the `harshatheg/Qwen-2.5-1B-RLCD` HF model card in full; the `dsif2012/Qwen3-4B-Instruct-2507-Decision` HF model card in full; the GitHub repository README, file tree, and API metadata (HEAD `88e919834d2eee2af181300c0b8504e96b86ae7d`, 2026-09-16T14:15:19Z; repo created 2026-09-16T13:52:19Z; 2 stars; Apache-2.0). No scouts: the corpus is four documents. No Parallel Lens panel: no wording was proposed for adoption and no TeaPrompt template was touched. Coverage check: installed surfaces grepped for `margin|confidence|runner-up` and the verdict-contract rows re-read.

**Scope / acceptance:** verify the paste's claims against its four cited sources; map the concept set against installed surfaces; decide every candidate with evidence and a trigger; land nothing without a verified gap; keep the clean-room boundary; run `make all` from the repository root.

## What the Artifact Is

`dsif2012/Qwen3-4B-Instruct-2507-Decision` (GitHub `88e9198`, Apache-2.0, Python): a `pcd` package that serves `POST /decision` over vLLM with prefix caching. A request carries one `context` plus a list of typed questions (`BOOLEAN`, `CHOICE` with ≥2 unique labels); the engine reads candidate-token logits, softmaxes over each candidate set, and returns value, confidence, margin, and full ranking — the response JSON is assembled programmatically, never parsed from generated text. The HF card ships no weights ("v0.1 is an inference interface … does not ship new weights"). Repo contents include backends (MLX Qwen2.5/Qwen3.5, vLLM), a dual-mode path, numeric-head and LoRA training scripts, BoolQ import, and a test suite — i.e., the roadmap items exist as scaffolding; v0.1 supports only BOOLEAN and CHOICE, and the README says so.

The two inspirations, as their own pages describe them:

- **TypeSafe "System One Models & Jev"** (post dated Sep 15, 2026; frontmatter Sep 17): a new model class trained with "Reinforcement Learning for Calibrated Decisions (RLCD)" — a *training method* — plus a new architecture and parallel sampler. Claims: typed structured outputs defined in advance, calibrated probabilities on every answer, 70–500 ms end-to-end, output tokens "free", "can't hallucinate" (nuance section: schema matching is guaranteed, so 0% type errors is "not empirical … mathematically impossible" — a type-safety claim, not a correctness claim), workflow evals referenced to the average of "GPT-6 Astra and Fable 5.1" (the post itself flags the bias), cardinality ≤255 with a two-stage score-then-choose fallback. Early access; proprietary.
- **`harshatheg/Qwen-2.5-1B-RLCD`** (HF card; Apache-2.0; MLX; base `Qwen/Qwen2.5-1.5B-Instruct`): "Parallel Constrained Decoding for Apple Silicon" — an inference engine: single broadcast prefill, KV-cache broadcast across schema fields, sub-vocabulary logit slicing, per-field softmax, token-tree disambiguation for shared multi-token prefixes, programmatic JSON assembly. Author-claimed 5.6–7.0× latency reduction vs autoregressive on an M4 Max with 100% schema validity. The card never uses the string "RLCD"; the acronym in the repo name is unexplained there. Its `git clone` URL is a `your-org` placeholder.

## Concept Map

Tier is what the surveyed artifact is (inference interface over stock weights). Coverage names the nearest installed TeaPrompt sentence.

| ID | Concept (clean-room) | Source tier | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- | --- |
| C1 | Typed decision contract over an explicit candidate set (BOOLEAN / CHOICE; the candidate list is data, not prose) | code (repo `schema.py`, `contract.py`; README API) | Verdict contracts everywhere: writer-critic exact `ACCEPT` token; DAG `done`/`failed` statuses; panel verdict schemas; dispatch route table | No change — installed |
| C2 | Decision without generation: score candidates, never produce the answer string | code (logit slicing + softmax; "does not free-form generate") | Prompt-level analog installed: decision-only steps emit only the verdict token; the residual gap (a host agent still *generates* the token) is a runtime property TeaPrompt cannot hold | No change — model-side mechanism |
| C3 | Dynamic candidate sets per call | code (`choices` per question, ≥2 unique) | Packs parameterize task lists, DAG node sets, and candidate files as data | No change — installed |
| C4 | Shared-prefix / KV-cache reuse across many decisions on one context | code (vLLM prefix caching; `cache.py`) | Prompt-level analog: packet contract amortizes one shared evidence packet across lenses | No change — host/runtime concern |
| C5 | Confidence + margin + full ranking on every decision | code (response schema) | Split: confidence-as-routing-signal installed (`reflective-dispatch` Route Confidence, low-confidence → probe/default-up; `workflow-recipes.md` escalate-on-low-confidence row); calibrated probabilities are a non-goal at prompt level — TeaPrompt's rule is "evidence over confidence" because self-reported confidence is unreliable; margin/runner-up's function (recorded dissent → Human Review) is installed in the panel contract | No change — covered; the margin mechanism itself is rejected (DM-5) |
| C6 | Batched multi-question decision calls over one context | code (`questions[]` request) | Packet contract: one packet, many judgments | No change — installed |
| C7 | Programmatic assembly of the structured result | code (response built from verified values) | Host-side by construction; TeaPrompt verdicts are consumed as tokens, not parsed from prose | No change — installed |
| C8 | Roadmap: multi-select, policy distribution, numeric heads, calibration, decision LoRA, vision decisions | scaffolding (`training/`, `heads.py`, `numeric_*`; README "Not in v0.1") | none — model-side capabilities | No change — non-goal |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| DM-1 | A "decision step emits only a typed verdict over an enumerated candidate set" sentence for the packs | No change 2026-09-18 | Already the installed contract: writer-critic exact-match `ACCEPT`, DAG `done`/`failed`, panel verdict schemas, route table rows | Reopen if a pack template is added whose step consumes free-form prose where a verdict suffices |
| DM-2 | "Enumerate the candidate set explicitly in the prompt" guidance | No change 2026-09-18 | Route tables, verdict schemas, and task-file formats already enumerate candidates as data | None |
| DM-3 | Shared-context amortization guidance (one context, many decisions) | No change 2026-09-18 | Packet contract (XM-6 lineage): one repo-readable packet feeds every lens; the KV-cache mechanism itself is host-side | None |
| DM-4 | Batched decision calls | No change 2026-09-18 | Same packet contract; a prompt-level "batch" is one packet with N questions, already the lens pattern | None |
| DM-5 | Margin/runner-up reporting on verdicts (escalate when the top two candidates are close) | Rejected 2026-09-18 | The function is installed differently: panels record the strongest rejected option and unresolved dissent goes to Human Review; dispatch escalates on low Route Confidence. A self-reported margin would be the agent's self-report — the gate class the loop pack forbids — and TeaPrompt's standing rule is "evidence over confidence" (`reflective-dispatch`; `PROJECT_KNOWLEDGE.md`) | Reopen only if a host exposes real candidate scores (logit-derived margin) to a TeaPrompt-run step; then the rule would consume a structural signal, not a self-report |
| DM-6 | Calibrated probability outputs as a prompt-level requirement | Rejected 2026-09-18 | Calibration is a training/eval property; asking a chat model for calibrated probabilities yields self-reported numbers with no calibration evidence — the failure TypeSafe's own table names for LLMs | None |
| DM-7 | Record correction: the paste's "RLCD = Parallel Constrained Decoding" expansion | Corrected 2026-09-18 (record-only) | TypeSafe post defines RLCD as Reinforcement Learning for Calibrated Decisions (a training method); the Qwen-2.5 card calls itself Parallel Constrained Decoding and never uses the acronym. Two different things share the acronym in the paste | — |
| DM-8 | Record correction: "Qwen-2.5-1B" | Corrected 2026-09-18 (record-only) | The card's `base_model` is `Qwen/Qwen2.5-1.5B-Instruct`; the repo name says 1B | — |
| DM-9 | "Decision model" as a TeaPrompt concept worth a glossary entry | No change 2026-09-18 | The artifact is an inference interface (its own card: "does not ship new weights"); the transferable pattern is C1/C2, already installed | Reopen if TeaPrompt ever ships a runtime that can read logits |

Deterministic guard: `plans/tests/test_decision_model_survey_record.py` (identity, dispositions, corrections, clean-room boundary, index links).

## Claim Check (the paste against its sources)

| Paste claim | Verdict | Basis |
| --- | --- | --- |
| "RLCD" is "Parallel Constrained Decoding" | **Conflation** | The Qwen-2.5 card's technique is named Parallel Constrained Decoding; "RLCD" appears only in its repo name, unexplained. TypeSafe's RLCD is a training method. The paste merges them |
| `Qwen-2.5-1B-RLCD` | **Name mismatch** | Card base model: `Qwen/Qwen2.5-1.5B-Instruct` |
| Inspired by Jev / System One and the Qwen-2.5 experiment | Plausible, self-reported | The mechanism (candidate scoring over logits, programmatic assembly) matches the Qwen-2.5 card's engine; the API shape (typed questions, probabilities per candidate) resembles TypeSafe's |
| "不是 TypeSafe RLCD 的重現，也沒有宣稱使用 Jev 的 proprietary training method" | **Accurate** | HF card: "inference interface … does not ship new weights"; no training claim anywhere in card or README |
| BOOLEAN + CHOICE only in v0.1 | **Accurate** | README "Supported in v0.1" table and "Not in v0.1" list agree |
| Returns ranking, confidence, margin | **Accurate** | README response schema |
| Dynamic candidate sets; prompt reprograms the task | **Accurate** | `choices` per question; no per-task weights exist |
| Shared prefix / KV cache utilization | **Accurate as designed** | vLLM serving path with prefix caching; not benchmarked here |
| Roadmap items (multi-select, policy distribution, numeric, calibration, LoRA, vision) | **Scaffolding, not shipped** | `training/`, `heads.py`, `numeric_*` files exist; README versions them v0.2–v0.4 |
| TypeSafe "can't hallucinate" (context the paste cites) | **Schema-scoped** | TypeSafe's own nuance: 0% type errors is guaranteed by schema matching, "not empirical"; it is not a correctness claim |

## Shared Findings

1. **The acronym collision is the survey's main factual yield.** "RLCD" currently names a proprietary training method (TypeSafe) and, by community coinage, an inference-time decoding technique (the Qwen-2.5 repo name). The paste inherits the collision; anyone citing "RLCD" needs to say which one they mean.
2. **The honest scope line is in the artifact's own card.** "Inference interface … does not ship new weights" is the correct framing; the announcement's "實驗版本" agrees with it, and the "model" title oversells only slightly.
3. **TeaPrompt already lives at this pattern's prompt-level ceiling.** Typed verdicts over enumerated candidates, emitted as the whole output, is what the verdict contracts, route table, and panel rows are. What the artifact adds — real candidate scores, margins, calibration — requires logit access a prompt-only library cannot hold; the one prompt-level echo (self-reported margin) is a self-report, the gate class the packs forbid.
4. **The inspirations bracket the cost axis.** TypeSafe bought calibrated decisions with a new architecture and training method; the two Qwen packages buy the same interface with inference-time logit surgery on stock weights — cheaper, uncalibrated by default, and bounded by the base model's judgment. The paste's roadmap (calibration, decision LoRA) is the bridge between them.
5. **Vendor claims stayed scoped on inspection.** TypeSafe's nuance sections disclose the reference-model bias in their evals, the laptop-on-West-Coast latency caveat, and that "0% type errors" is definitional rather than measured — the same disclosure discipline the RSIAgent docs showed.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Repo identity, license, HEAD `88e9198`, creation/push dates, star count | Observed | GitHub API, accessed 2026-09-18 |
| HF card contents (both models), tags, base models, licenses | Observed | HF API model endpoints, read 2026-09-18 |
| TypeSafe post contents, claims, nuance disclosures, dates | Observed | Post read in full 2026-09-18 (body "Sep 15, 2026"; frontmatter "Sep 17, 2026") |
| The Qwen-2.5 card never uses "RLCD" | Observed | Full card read; case-insensitive check |
| v0.1 scope (BOOLEAN/CHOICE), response schema, vLLM path, roadmap versioning | Observed (docs) | README + HF card; source files listed but not executed |
| TypeSafe speed/cost/eval numbers; Qwen-2.5 latency table | Author-claimed | Vendor post and model card; no independent eval |
| The mechanism match between the artifact and the Qwen-2.5 engine | `[INFERENCE]` | README/card descriptions compared; `src/pcd` internals not audited |
| No installed surface carries the surveyed vocabulary | Observed | `test_survey_vocabulary_stays_out_of_installed_surfaces` |

## Evidence Actually Checked

- GitHub API: repo metadata, `commits` (HEAD `88e9198…`), file tree, README — 2026-09-18.
- HF API: `dsif2012/Qwen3-4B-Instruct-2507-Decision` and `harshatheg/Qwen-2.5-1B-RLCD` model cards — 2026-09-18.
- TypeSafe blog post in full — 2026-09-18.
- Installed surfaces grepped for `margin|confidence|runner-up`; `reflective-dispatch` Route Confidence rows and `workflow-recipes.md` confidence row re-read — 2026-09-18.
- Not executed: the `pcd` package, the Space demo, any benchmark; no clone.

## Falsifiability

- The "no sentence needed" mapping is wrong if an installed skill is later shown to lack a rule the Concept Map credits to it (the coverage rows name the surfaces; re-grep them).
- DM-5's rejection of self-reported margin is wrong if a TeaPrompt-run host exposes real candidate scores; the trigger row says what would reopen it.
- The acronym-conflation correction is wrong if the Qwen-2.5 repository elsewhere defines "RLCD" as Parallel Constrained Decoding (the model card — the cited page — does not); the verdict is bounded to the inspected sources.
- The mechanism-match finding is inference from docs; reading `src/pcd/engine.py` and `scoring.py` could revise it.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| All four cited sources read; artifact pinned (`88e9198`) | done | this record |
| Paste claims checked against sources; two corrections recorded | done | Claim Check |
| Eight concepts mapped with tier and coverage | done | Concept Map |
| Nine candidates decided with evidence and triggers | done | Candidate Adoption Ledger, dispositions guarded |
| Clean-room boundary on installed surfaces | done | `test_survey_vocabulary_stays_out_of_installed_surfaces` |
| Guard written | done | `plans/tests/test_decision_model_survey_record.py` |
| Decision Index row, case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`, `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |

## Review Addendum (2026-09-18, same day)

A four-lens review panel was attempted twice (scout and task backends); all eight assignments died on provider quota with zero assistant turns, so this review is coordinator-executed — **no independent lens verdicts exist**. Findings fixed: DM-5's ledger status read "No change" while the record's own Falsifiability line, the Decision Index bullet, the case-studies row, and the commit message all call it a rejection — the ledger now reads Rejected (it is a declined mechanism, the RS-3/4/5 precedent, not a covered concept; C5's disposition cell now says so precisely). Guard probes: the ledger regex captures the Status cell on all nine rows; status-flip, date-deletion, and row-deletion mutations are all caught.
