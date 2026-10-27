# DeepInfer and deepseek-recipe Source Survey — 2026-10-27

Language: English

> **Status: recorded; documentation-only, reference evidence.** The user supplied both repositories for “Survey” and added “if worth it then update docs or skills”. This authorizes this review's worthwhile documentation or contract repairs, not runtime adoption, model expenditure, deployment, a commit/push, or a change to Standing Non-Goals. DS-DOC1 records the findings; DS-1–DS-7 introduce no skill, pack, route or host-runtime change.

## Research Question and Direct Recommendation

What do these repositories actually supply, what survives selected source inspection and bounded offline execution, and does that evidence establish a missing delivered TeaPrompt instruction?

**Update the research documentation; retain current skills.** The useful result is a source-bound comparison of inference machinery, protocol adaptation and caller-owned guarantees. No new local contract defect was demonstrated. Generic engineering coverage is not a claim that TeaPrompt implements these libraries or that every consumer follows its instructions.

The repositories are complementary layers, not two prompt libraries:

- **DeepInfer:** an optimized, model-specific offline inference engine. The public release is not the complete production service described in its deployment discussion.
- **deepseek-recipe:** Rust libraries and Python bindings for protocol conversion, model-specific prompt/token encoding and output parsing. It is **not a training recipe collection**; callers supply inference, HTTP transport and tool execution.
- **[INFERENCE] Integration opportunity:** an application could place protocol conversion around an inference engine. This survey did not wire the two projects together or establish a turnkey compatibility contract between their selected revisions.

## Version / Date Context

Repository, default-branch commit and contents APIs were checked on 2026-10-27. Branch/release/registry facts are snapshots; immutable pins below identify the actual evidence.

| Surface | Inspected identity | Licence / qualification |
| --- | --- | --- |
| DeepInfer `main` | `553741557a57df44a46fb3ab72b6aafeaf945337`; tree `67d7df235844e4494f179b3d9f0b46523be4b40c` | Apache-2.0; source package label `0.1.0`, not a verified registry release |
| deepseek-recipe `main` | `935817c66f5d6e64838f419692545f06787e485f`; tree `87a3a67b0d12d34534682cf494536aedec5fafa1` | MIT; Rust workspace label `0.2.0`; bundled tokenizer/native-library notices have their own boundaries |
| Recipe artifact executed | PyPI `deepseek_recipe-0.2.0-cp310-abi3-macosx_11_0_arm64.whl`, uploaded `2026-10-20T05:15:05.726523Z` | SHA-256 `624bb4d0fb3ed541b9e34d2ef96ff66057026ded7d6708b0b9088cc6d6723999`; downloaded bytes matched the registry digest |
| GitHub publication status | Both tags/releases listings were empty in the source investigators' checks | Empty listings do not mean there is no published package; PyPI supplies the separately identified recipe wheel |

Matching the recipe workspace and wheel version labels does **not** prove build/source equivalence. Runtime observations below bind to the wheel digest; source observations bind to the commit. Refresh refs, package metadata, dependencies and hardware conditions before any future deployment recommendation.

## Evidence Used and Review Method

Two read-only source scouts investigated independent repository slices. They supplied source navigation and challenges, not runtime measurements or a consensus panel. The coordinator inspected decision-bearing interfaces and ran the bounded mechanisms below. No third-party summary or prior conversation was substituted for upstream evidence.

**DeepInfer sources:** [root README](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/README.md), [package metadata](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/pyproject.toml), [examples and benchmark accounting](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/examples/README.md), [deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/doc/inference_deployment_qa.md), and the implementing paths linked in the findings.

**Recipe sources:** [root README](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/README.md), [workspace](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/Cargo.toml), [streaming guide](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/docs/streaming.md), [breaking-change history](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/CHANGELOG.md), selected protocol/encoding/stream/image source, and [PyPI metadata](https://pypi.org/pypi/deepseek-recipe/0.2.0/json). The executed wheel's import module, interface stubs and metadata were inspected before its isolated import.

Perspectives came from the supplied artifacts: engine operators care about latency/throughput and hardware; API integrators about semantic conversion, completion and effects; TeaPrompt maintainers about delivered-contract gaps rather than runtime novelty. Blind spots: full engine operation, integrated service behavior, independent performance replication and adversarial network-policy enforcement.

Semantic discovery failed with 403. Literal searches over `plans/` and `PROJECT_KNOWLEDGE.md` found no prior exact repository-name record and did find existing `DeepSeek` references as a positive control. That is a bounded discovery result, not a claim of global absence.

## DeepInfer: Mechanisms and Limits

### Offline engine versus production service

The README supports DeepSeek-V4.1-Flash on NVIDIA SM100 and Huawei Ascend 950; its build instructions require Linux, Python 3.12, GCC 13+, and platform-specific CUDA/CANN. Optimized attention/GEMM/expert kernels, attention DP/CP, MoE EP/EPLB, speculative decoding and asynchronous scheduling are engine mechanisms.

The README explicitly excludes a complete KV cache system, full VE/prefill/decode disaggregation and load balancing across replicas. The released engine still has GPU cache/block management: “complete-service cache system absent” must not become “no KV cache exists”. Empty integration hooks in [the engine base](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/deepinfer/engine/llm_engine.py#L797-L819) and the Q&A's internal/open-source distinction bound the production claim.

### Confidence schedules token verification, not agent trust

[The DFlash confidence head](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/deepinfer/model_executor/models/mtp/dflash.py#L44-L75) predicts acceptance probability of draft tokens. [The scheduler](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/csrc/engine/mtp_varlen.hpp#L150-L265) uses acceptance estimates and a profiled cost curve to allocate verification lengths; it is not estimating correctness of a business answer or authority for an effect.

**[INFERENCE] Do not transplant the mechanism into “a confident agent needs less review”.** The probability's measured target and the verifier's role differ. The existing [Confidence recipe](../04-agent/workflow-recipes.md#looper-topologies) preserves risk-required rigor; this survey does not reopen PW-1 or supply calibration evidence for an agent-confidence threshold.

### Reproducibility and bounded replay are conditional

The deterministic recipe is NVIDIA-only: enable batch invariance, disable variable-length MTP and supply a fixed `seq_seed`. An omitted seed is randomized in [SamplingParams](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/deepinfer/sampling_params.py#L84-L90). A fixed seed alone is not the documented guarantee. The included batch-invariance comparison uses a teacher-forced single trajectory; it is not universal cross-platform reproducibility evidence.

Decoder SWA replay retains a bounded suffix. The Q&A calls its reconstructed cache approximate; the implementation requires a compatible model and enough retained tokens for the window plus maximum backtracking. The [mask/compact comparison](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/examples/yoco/README.md) is not equivalence to unrestricted replay. Likewise, “zero-overhead” scheduling names a dependency-aware pipeline: its default applies to NORMAL/COMPLETION, not PROMPT mode, and configuration can override it. None of these engine guarantees was executed on this host.

### Actual grammar enforcement has completion boundaries

[XGrammar compilation](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/deepinfer/structure_output/compiler.py#L53-L67) supports strict JSON schema, regex and EBNF. [Sampler masks](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/deepinfer/model_executor/layers/sampler.py#L350-L385) participate in generation/verification, unlike a schema merely written into a prompt. Triggered constraints may allow an unconstrained prefix, and a token cap can end before a structure completes. The [example](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/examples/_structured_output.py#L41-L62) checks stop/EOS and validates the result. Syntax restriction still does not prove semantic correctness or tool authorization.

### Benchmark and evaluation labels need their own checks

The README's curves are author-reported measurements on four SM100 devices for prefill and 64 for decode, not measurements reproduced here. The benchmark uses synthetic prompts, a warmed/shared prefix, selected steady-state windows and profiler/logging exclusions. Raw decode accounting assumes full draft acceptance; [plotting](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/examples/sweep/plot_pareto.py#L56-L64) can apply a supplied acceptance assumption. Engine-step throughput is not end-to-end service throughput, equal-cost superiority or an observed agent-quality gain.

The model checkpoint is another identity boundary: [example loading](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/examples/_config.py#L32-L48) downloads by name without a revision argument; configuration enables remote model code, and the evaluator loads checkpoint encoding code. Pinning the engine does not pin those executable/model bytes. No model download or remote-code execution was performed.

The actual rule-scoring CLI also yielded counterexamples to relying on summary labels; see the executed controls below. These qualify the release's evaluator, not the model's real benchmark accuracy.

## deepseek-recipe: Mechanisms and Limits

### Conversion changes semantics, not just JSON field names

Messages, Chat Completions and Responses become a shared ConversationRequest; callers then choose the appropriate model encoder. Unknown model names require an explicit alias or are rejected. V4/V4.1 differ: V4 images become `[Unsupported Image]`, while [Responses developer-role conversion](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe/src/protocol/openai/responses/request/convert.rs#L420-L456) maps to user on V4 and system on V4.1. A compatible protocol surface is not proof of identical role, image or tool semantics across models.

Thinking mode, reasoning effort and prefix continuation have model-specific conversion/rendering rules. Their existence is not evidence that a particular reasoning effort improves outcomes. Public servers are mock-backend examples, not supplied inference or tool execution.

### Structural token provenance is narrower than injection resistance

[Prompt tokenization](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe-encoding/src/tokenizer.rs#L90-L115) distinguishes structural special-token ranges from ordinary text containing the same spelling. Python exposes code-point ranges whereas Rust uses byte ranges. The wheel probe observed the rendering distinction for a literal user-token spelling embedded after Chinese text; it did not attach a tokenizer or establish token-ID behavior. This is not a semantic prompt-injection defense or an authority gate.

### Declared output constraints need a backend enforcer

[Constraint selection](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe/src/protocol/output_constraint.rs#L8-L59) produces JSON/schema/regex or tool-call metadata. Active tools take precedence; specified incompatible strict-tool combinations are rejected. The caller chooses whether its backend applies the constraint. The [JSON recognizer](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe/src/stream/output_parser.rs#L35-L55) explicitly does not validate JSON syntax.

Observed on the pinned wheel: request regex `YES|NO`, supply synthetic backend text `MAYBE`, then finish normally. The response retains `MAYBE`. This matches the declared ownership boundary; it is not a demonstrated bypass of an enforced decoder. Tool definitions and client tool-search/deferred-loading conversion similarly do not execute or authorize a tool.

### Budget resolution and stream completion need caller policy

[resolve_max_tokens](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe/src/request/mod.rs#L180-L235) is called after encoding; the caller supplies prompt length, including image-token adjustment, and the context limit. Explicit overflowing requests are rejected. However, the source ends with `.min(remaining).max(1)`, and the wheel returned 1 when an unspecified output limit met a prompt exactly filling the context. A service needing a free output slot must enforce that admission condition independently. This survey did not test a backend's response to that request.

[StreamProcessor](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe/src/stream/processor.rs#L102-L215) separates parser/tokenizer errors from normal completion. But natural input EOF is an EndOfStream result, and the [Chat adapter](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe/src/protocol/openai/chat_completion/response/schema.rs#L143-L151) maps it to `stop`. The wheel reproduced this with no backend Finish chunk. Application receipt/completion policy cannot infer an explicit backend completion from that normalized field alone. This is an adapter semantic, not proof of a network-disconnect vulnerability.

### Image fetching exposes a separate outbound sink

The README warns that ReqwestImageFetcher connects to any address by default. [The implementation](https://github.com/deepseek-ai/deepseek-recipe/blob/935817c66f5d6e64838f419692545f06787e485f/deepseek-recipe-image/src/fetcher.rs#L130-L182) supports a caller-supplied DestinationFilter over resolution/redirect destinations; that facility is not itself a safe destination policy. Untrusted image URLs need service-owned outbound policy. No image URL, DNS/redirect filter or SSRF exploit was exercised here.

## Executed Verification

Execution used clean-environment CPython 3.14.7 under native macOS Seatbelt. Before upstream imports the driver checked scratch read/write, an explicit outside-read refusal, outside-write refusal, blocked loopback networking and inherited child-process read refusal. `/Users` reads were denied; writes were limited to the owned scratch directory and `/dev/null`. Other system reads remained permitted, so this is a bounded containment observation, not a complete confidentiality or hostile-native-code security certification.

The initial stricter allowlist profile exited 134 even for `/usr/bin/true`. Those setup failures produced no upstream result. The corrected explicit-denial profile passed the controls before mechanism execution. No global/repository package installation, GPU inference, hosted model call, image fetch, HTTP server, container or metered benchmark was run.

The inspected source modules were executed unchanged. The recipe wheel was hash-verified and unpacked into scratch with absolute/traversal/symlink archive members refused; no pip installation was used. Counts below enumerate named driver observations, not independent benchmark trials or a general test-suite pass.

### DeepInfer environment module

Source SHA-256: `c63414c101ce21e199f2d7df27ec01ca53e3b0dc7a688f6047469551f6449f47`.

Observed: valid boolean spellings accepted; invalid spellings refused; a changed environment value remained cached until explicit rearm; configuration errors named their variable; an unsupported replay mode was refused; backtracking respected `max(requested, draft_length + 1)` on both sides of the boundary; confidence-temperature tuple length had to match the draft length. These are seven configuration scenarios, not evidence for kernel determinism, SWA equivalence or DSpark efficacy.

### Recipe public Python API

Eleven scenarios completed: structural/literal marker ranges; unknown-model refusal; valid/overflow token budgets; the zero-remaining-context edge; prefix continuation; regex constraint metadata; strict-tool constraint selection; a split reasoning marker with explicit stop; EOF without backend Finish; backend text outside the requested regex; and a missing-tokenizer error remaining terminal. Inputs were synthetic requests/backend chunks; outputs came from the actual native bindings, not a rewritten parser or an inference model.

### DeepInfer rule-scoring CLI

Executed the pinned `eval/score.py --judge rule` with its actual AIME scorer and common IO/loader/Pass@k/path modules. Source SHA-256 for `score.py`: `af3755cd5c0a1bb050296b03999773d6aead6360e197234b1bd8438fbcb293a4`.

Fixture: tasks A and B, gold answer `1`, declared `n_sample=2`; expected identities `(A,0),(A,1),(B,0),(B,1)`. An independent set difference checked actual identities, not just the scorer's aggregate totals. All invocations exited zero.

| Synthetic input | Reported coverage_complete | Reported ragged_samples | Independently missing / unexpected identities | Other observation |
| --- | --- | --- | --- | --- |
| Expected four pairs, all stop | true | false | none / none | Positive control |
| Omit `(B,1)` | false | true | `(B,1)` / none | Ordinary missing-row negative control detected |
| Replace both index-1 samples with index 9; one boxed-correct row marked length | true | false | `(A,1),(B,1)` / `(A,9),(B,9)` | `truncated_rollouts=1`, that row scored correct; `Pass@1=1.0` |

[Coverage code](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/eval/score.py#L120-L160) checks task presence and total row count, not exact expected task/sample membership. The [rule scorer](https://github.com/deepseek-ai/DeepInfer/blob/553741557a57df44a46fb3ab72b6aafeaf945337/eval/aime/bench.py#L157-L165) scores extracted answers without enforcing finish reason; the CLI's “all counted as wrong” warning is therefore not true of this exercised path. The explicit rule judge is not the default LLM judge. These controls do not establish the behavior of published real-data scores or adversarial LLM judging.

Reproduction shape, from the isolated scratch root:

```text
env -i PATH=/usr/bin:/bin:/opt/homebrew/bin HOME=<scratch> TMPDIR=<scratch> \
  /usr/bin/sandbox-exec -f <scratch>/smoke.sb \
  /opt/homebrew/opt/python@3.14/bin/python3.14 -I <scratch>/<driver>.py
```

Drivers were `smoke.py`, `recipe_smoke.py`, and `scorer_smoke.py`. Their SHA-256 values are respectively `b863d2e9d8577054d80a2bea2bb6b85fa226d80fd72f559efc31cfbc46b220ca`, `4d867acd6c6837e0bcbd456b2c015e9f318feca68e986840b6b27e955342a9c5`, and `c09e4816c276c5c674f7afdbf9f341d884fc582c89e819ab37580ccac2be2fac`. Profile SHA-256: `70e600118c5ab8efc4780bf0cfc392d796976f1b585145002001ca640d0b1985`.

The supplemental session receipt `deepseek-survey-smoke-2026-10-27.json` preserves driver/profile contents, source hashes and raw scorer output. The evidence and limitations necessary for this decision are embedded here; temporary scripts and the wheel are not repository dependencies. No permanent upstream smoke fixture or survey-wording test is added.

## Candidate Adoption Ledger

Conditional update authority was present throughout this assessment. Permission to repair is not evidence that a repair is needed; a source's implementation gap is not automatically a TeaPrompt instruction gap.

| ID | Candidate / decision | Checked local delivery and evidence | Reopening evidence / falsifier |
| --- | --- | --- | --- |
| DS-DOC1 | Record this paired survey and catalogue/navigation entry — completed as reference documentation | One source-bound record preserves the version, semantic and execution qualifications; avoids new wrapper/skill/runtime surface | Consolidate if a current duplicate appears; correct if contrary pinned-source or artifact evidence changes a finding |
| DS-1 | Adopt inference/service or protocol runtime — not adopted; host/application territory | [Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals); [spec-plan Workflow Design Mode](../skills/reflective-spec-plan/SKILL.md#workflow-design-mode). These can specify ownership, not provide GPU kernels, HTTP, caches or adapters | Explicit project-direction change plus a demonstrated local runtime need; external releases alone are not local recurrence |
| DS-2 | Replace risk-based review with DSpark confidence scheduling — reject this transfer; no PW-1 edit | [Confidence topology row](../04-agent/workflow-recipes.md#looper-topologies); token-acceptance prediction is not an answer-correctness or effect-risk estimate | Controlled local evidence for the proposed agent-verification policy against its actual outcome/risk target |
| DS-3 | Add hardware-specific reproducibility recipes to generic research/eval skills — no change | [Research Source Priority, External Adoption Checks and State Ledger](../skills/reflective-research/SKILL.md); [golden runner Paired arms / Measurement preflight](../skills/golden-benchmark-runner/SKILL.md#methods); [implementation Verification](../skills/reflective-implement/SKILL.md#verification). Exact setup and changed configuration already qualify evidence; no local missing instruction demonstrated | A local comparison falsely attributed to guidance because effective runtime conditions were omitted, exposing a missing delivered instruction rather than noncompliance |
| DS-4 | Strengthen declaration-versus-enforcement/acceptance wording — no change | [Governance scaffold Methods, Four-Power Split and Verification](../skills/agent-governance-scaffold/SKILL.md); [runtime trust boundary](../04-agent/runtime-trust-boundary.md#2a-product--runtime-ownership-boundary). Grammar syntax, parsing and authority remain different layers | A delivered contract accepts a schema, tool declaration, EOF-normalized stop or metadata label as sufficient acceptance/effect authorization |
| DS-5 | Add a general adapter/continuation skill — no change; preserve concrete examples here | [Implementation Consumer map](../skills/reflective-implement/SKILL.md#verification) covers alternate entry points and final observable propagation; [spec-plan State/artifacts and Errors/gates](../skills/reflective-spec-plan/SKILL.md#workflow-design-mode) covers ownership and failure state. This does not claim coverage of every model-specific conversion rule | A repeated local adapter loss outside those declared checks, or a specific portable-contract defect demonstrated by a consumer probe |
| DS-6 | Add another evaluation-completeness rule — no change; document the exercised scorer counterexample | [Review Four Evidence Dimensions / Evidence Tiers](../skills/reflective-review/SKILL.md#four-evidence-dimensions), [research independent same-population checks](../skills/reflective-research/SKILL.md#state-ledger), and [golden runner receipt/allocation discipline](../skills/golden-benchmark-runner/SKILL.md#methods). This is generic methodological coverage, not an audit of every TeaPrompt evaluator's sample-identity join | A local consumer misreports expected allocations/identity membership or truncation disposition and the existing instruction cannot state the required repair |
| DS-7 | Add a URL-fetch/tool-authority safety skill — no change | [Risk Never and Sink Inventory](../skills/reflective-risk/SKILL.md), [governance scaffold trust-boundary-first rule](../skills/agent-governance-scaffold/SKILL.md#module-contract). Destination policy and tool effects require host enforcement, not another prompt label | A demonstrated missing portable instruction; a missing network enforcer alone calls for host work, not prose promotion |

## Evidence vs Inference and Sufficiency

- **Observed source/metadata:** the pinned implementations, declared features, public-release omissions, model/protocol differences and artifact identities. A source read establishes code/text, not executed GPU behavior.
- **Observed execution:** only the bounded configuration, published-wheel and synthetic rule-scoring scenarios above. Wheel/source equality remains unknown. The initial sandbox startup failures were setup failures, not upstream test failures.
- **Author-reported:** production lineage, benchmark curves, performance/quality results and kernel/runtime guarantees not exercised here. Reading a table, test or reproduction command does not independently reproduce its results.
- **[INFERENCE]:** these examples make enforcement ownership and evidence provenance worth preserving, but do not demonstrate a new delivered TeaPrompt instruction gap or a beneficial new skill. Counterargument: engine/adapter-specific detail could improve an integrator's checklist. Decision: retain concrete examples in this record rather than impose model-specific runtime requirements on generic workflows.

The evidence is sufficient for the documentation-only decision: both objects are identified, important mechanisms and counterexamples have source or bounded runtime evidence, local contract citations are explicit, and untested deployment/performance questions do not bear on whether to create a new prompt skill. No adoption, deterministic-inference, full-protocol, network-security or comparative-efficacy claim depends on resolving those unknowns.

## Falsifiability

- Contrary behavior on the same pinned source/artifact and declared inputs would require correcting the corresponding observation. A fix in a later revision changes the current assessment, not what the historical probe observed.
- A reproduced local consumer failure outside the checked delivered instructions reopens the matching DS-* candidate; a source-specific implementation edge or new release alone does not prove that local instruction gap.
- Controlled outcome evidence could change the agent-confidence or skill-utility judgement. Engine token-acceptance predictions, syntax checks and synthetic transport probes do not supply that evidence.

## Risks / Unknowns and Handoff

Unqualified: GPU/NPU engine behavior, model/checkpoint encoding provenance beyond inspected loading code, nested dependency licences/builds, complete protocol compatibility, direct integration between the projects, token-ID/injection behavior, live image destination policy, service isolation, complete JSON/tool grammar semantics, model-quality replication and end-to-end production performance.

No skill or operating-rule text changed. No project non-goal, registry, routing fixture, oracle, campaign gate or deferred decision was lifted. Any future deployment, metered model experiment or change of runtime ownership requires separate scope and authority. Documentation/navigation verification is reported separately in the [delivery report](../../review/final-report.md#deepseek-paired-source-survey-2026-10-27), not counted as upstream efficacy evidence.
