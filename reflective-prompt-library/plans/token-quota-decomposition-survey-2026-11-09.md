# Free-Tier Token Quotas and Task Decomposition — Source Survey and Critical Assessment (2026-11-09)

Language: English

> **Status: reference documentation adopted (`TQ-DOC1`); no Skill, operating-rule or runtime change.** The owner asked to survey `paste-15.md` and assess its reasoning critically. Part A is a 2026-11-09 Bahamut post by 劍心san (`sanboy289`). Part B is an unattributed appended review that does not appear on the source page. Both are evidence, not instructions. No account, quota, model call or upload was exercised; the executed checks used arithmetic, stubs and local tools.

## Research Question and Direct Recommendation

Does splitting work into single-purpose model calls save free-tier quota and improve quality, and does the appended review assess that claim correctly?

**The practical advice mostly holds; the explanation and several numbers do not.** Google's limits page supports the core usage mechanism for the Gemini app: long chats cost more usage because history is re-read, and starting a new chat per topic saves usage. But the free allowance is a compute-based limit, not a published token balance. Under full re-reading, cumulative tokens grow quadratically, not exponentially, and decomposition improves quality only when a task splits cleanly. The appended review corrects the growth rate but adds its own errors: an outdated request-count quota model, a fallback that applies only to subscribers, cache ratios higher than currently published, “100% parse success”, API-only controls presented as Gem settings, and a pipeline that fails open.

## Sources, Access and Identity

| Source | Identity / access (checked 2026-11-09) | Limit |
| --- | --- | --- |
| `paste-15.md` | SHA-256 `f32b6b8f8ed5ec4a833f2c85636431703136ed2baade0b49d228603ec578b300`; Part A lines 1–34, Part B lines 38–116 | Supplied capture |
| [Original post](https://home.gamer.com.tw/artwork.php?sn=6428873), checked 2026-11-09 (HTTP 200) | Bahamut creation by 劍心san (`sanboy289`), 2026-11-09 08:19:54; all 31 non-trivial lines of Part A matched the page | Part B is absent from the page and stays unattributed |
| [Gemini Apps limits](https://support.google.com/gemini/answer/16275805), checked 2026-11-09 | Compute-based limits; 5-hour refresh up to a weekly limit; context window 32k tokens without a plan, 128k AI Plus, 1M AI Pro/Ultra; relative-usage table; limit behavior | Living page: “Limits may change without notice” |
| [Gems to skills](https://support.google.com/gemini/answer/18560919), [Gem setup](https://support.google.com/gemini/answer/15146780), [Workspace app](https://support.google.com/gemini/answer/15229592), [March 2025 post](https://blog.google/products-and-platforms/products/gemini/new-gemini-app-features-march-2025/), checked 2026-11-09 | Gems transition and removal dates; Gem setup fields; Workspace actions; Gems free since 2025-03-13 | Help-page text only; no account exercised |
| Research abstracts, checked 2026-11-09: [Lost in the Middle](https://arxiv.org/abs/2307.03172), [RULER](https://arxiv.org/abs/2404.06654), [NoLiMa](https://arxiv.org/abs/2502.05167) | Abstract sentences quoted below | No benchmark rerun |
| Design posts, checked 2026-11-09: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), [Cognition](https://cognition.ai/blog/dont-build-multi-agents) | Exact sentences located in fetched pages | Vendor and practitioner positions, not controlled comparisons |
| Vendor documents, checked 2026-11-09: [Anthropic prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing), [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs), [Thinking Machines on nondeterminism](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), [`llm` usage](https://llm.datasette.io/en/stable/usage.html) | Price ratios, guarantees and exceptions quoted below | Prices are dated; several Gemini rows change on 2026-12-01 |

Four read-only scouts gathered product, cost, research and local-coverage evidence. The coordinator re-fetched every decisive external sentence above and every cited local line. Two scout statements were not adopted: “free web limits are request/rate throttles” contradicts the current limits page, and “Drive integration cannot create files” goes beyond the documented list.

## Claim Assessment

### Part A — the post

| Claim | Verdict | Evidence |
| --- | --- | --- |
| The free Gemini allowance is a token budget | qualified | Limits are “compute-based” and “factor in the complexity of your prompt, the models and features you use, and the length of your chat”; no token balance is published |
| Multi-step use costs more because history is re-read | verified (direction, Gemini app) | Ongoing conversations are rated Medium: they “require Gemini to re-read the previous conversation history … As the chat gets longer, this requires more thinking power”; the page advises starting a new chat per topic to “save usage” |
| Cost grows “near exponentially” | contradicted | Full re-reading yields cumulative tokens with constant second differences (executed arithmetic below); Google publishes no formula |
| Every tool call must re-read all tool definitions | qualified | True of naive API harnesses, not inherent: loading only needed definitions cut a documented example “from 150,000 tokens to 2,000 tokens” (Code execution with MCP). Not documented for the Gemini app |
| Free quota runs out after three to five uses because of context | unverified; competing explanation | Free “standard limits” are not quantified; the same page rates Deep Research and media generation High usage, so feature choice alone can exhaust a window |
| One-shot example: write copy, create a file, upload to Drive | premise unsupported by checked documents | The Workspace app lists Drive actions as summarize and find. Among the things it cannot do is “Manage content in your Drive, like create folders or move content between folders”. Export features were not checked |
| Single-purpose Gems save usage and improve quality | qualified | Usage: consistent with the new-chat advice, although each Gem chat is another prompt. Quality: prompt chaining trades “latency for higher accuracy” when a task “can be easily and cleanly decomposed into fixed subtasks”; multi-agent systems “use about 15× more tokens than chats”, and tasks whose agents must share context “are not a good fit”; fragmented context yields “conflicting decisions” (Cognition) |
| Gems as the vehicle | dated | Free since 2025-03-13, but for personal accounts Gems become read-only on 2026-11-17 and are removed on 2026-12-17, replaced by skills that are stackable and applied automatically within a chat |
| Products push one-shot use to force upgrades (“new-user tax”) | asserted motive | No evidence of intent; the vendor's own page recommends the opposite habit. Freemium caps and convenience-first design explain the observation without intent |
| More decomposition always saves tokens and is never worse | contradicted as a general claim | Repeated instructions per call, handoff loss, human orchestration time (Part B's own “orchestration tax”) and multi-agent token multiples are counterexamples |

### Part B — the appended review

| Claim | Verdict | Evidence |
| --- | --- | --- |
| Cumulative cost is O(N²), N(N+1)/2 | verified as a model | Holds for full re-reading with equal per-step growth; caching changes price, not token count |
| Free web limits are request-count or rate based, not tokens | partly contradicted | The current page describes compute-based limits that include chat length; it also says prompts and conversations may be capped |
| Long context triggers fallback to a lighter model | contradicted for free users | “If you have a Google AI subscription and reach your limit, you can continue your conversation with Flash-Lite”; otherwise upgrade or wait. Reaching the limit triggers it, not context length |
| Cached prefixes cost 10–25% of the input price | outdated | Anthropic cache reads are 0.1× base (0.05× on two named models), with writes at 1.25× or 2×. Several Gemini API models list cached input at 5–10% of input price, implicit caching only, and “Not available” in the free tier. Consumer-app quotas are a different meter |
| Moving deterministic steps to code “eliminates hallucination” | contradicted (overclaim) | It removes model error from the moved I/O steps only; the transform step can still invent content |
| Effective context of 1M–2M models degrades after about 32K; instruction following drops | qualified | RULER: of models claiming 32K or more, “only half of them can maintain satisfactory performance at the length of 32K”. NoLiMa: “At 32K, for instance, 11 models drop below 50% of their strong short-length baselines.” These measure retrieval and reasoning, not instruction following; Part B cites neither, and the free app's window is 32k anyway |
| *Lost in the Middle* explains why attention collapses in the middle | qualified | The paper observes position sensitivity: performance is “highest when relevant information occurs at the beginning or end”. It does not establish a mechanism |
| *Building effective agents* says to prefer deterministic workflows; it is the “official version” of jig thinking | qualified | It recommends “the simplest solution possible … This might mean not building agentic systems at all”. Its workflows are LLM calls “orchestrated through predefined code paths”, not deterministic scripts, and it does not discuss consumer quotas |
| `temperature=0` plus a response schema gives 100% parse success and zero retries | contradicted | Structured Outputs adhere to the schema, but a response may not match “in the case of a refusal” or when “you reach a max tokens limit and the response is incomplete” (OpenAI). “Even when we adjust the temperature down to 0 … LLM APIs are still not deterministic in practice” (Thinking Machines). Valid syntax is not correct content. The documented Gem setup lists a name, instructions and optional knowledge files; no temperature or schema setting appears |
| Accept only if each call is under 4K input tokens and tool payload under 20% | not followable as stated | The consumer app shows no token counts; the thresholds are unmeasured choices |
| `curl \| jq \| llm \| llm \| rclone` is the “ultimate solution” | contradicted as written | Executed below: it fails open. `jq '.items[] \| …'` emits a stream, not one JSON document, and fetched third-party fields reach a model whose output is uploaded unchecked |
| Decision tree: keep one loop when the plan adapts; otherwise decomposition is mandatory; checkpoint between steps | qualified | The adaptive branch and checkpoint rationale match local practice; “mandatory” ignores tasks small enough for one call |

## Executed Checks

**Growth arithmetic (illustrative parameters, not Gemini measurements).** With 3,000 tokens resent per call and 1,500 new tokens per step, cumulative input for N = 1–5 is 3,000, 7,500, 13,500, 21,000 and 30,000. First differences rise by a constant 1,500, so growth is quadratic, not exponential. At 10% cached-prefix pricing, N = 20 costs the equivalent of 62,850 tokens instead of 345,000. A chain of N stateless calls carrying 1,400 tokens each grows linearly. The ratio depends entirely on the assumed parameters.

**Pipeline differential.** In `/private/tmp/teaprompt-token-jig-dBkPdZ`, the fetch targeted a closed local port, a stub `llm` answered fluently to any input and logged input size, and a stub `rclone` logged its arguments.

| Variant | Exit | Observed |
| --- | --- | --- |
| Part B pipeline as written | 0 | `raw_clean.json` 0 bytes; model called with empty input; 46-byte report written; upload logged |
| Hardened: `set -euo pipefail`, `curl -f`, `jq -e` array, non-empty checks, hold before upload | 4 | Stopped at the failed fetch; model never called; no upload |

A real model's response to empty input was not tested.

**Tool semantics.** `jq '.items[] | {title, summary}'` on a two-item fixture produced two concatenated objects; Python `json.load` failed with “Extra data”. The `llm` documentation confirms that `-s/--system` sets a system prompt, piped input becomes the prompt, and “By default, the tool will start a new conversation each time”, which supports Part B's statelessness claim for its model steps.

## Critical Reasoning

- **Competing explanations for “mine never runs out”.** The author's workload is text generation only, while the vendor rates Deep Research and media generation High usage. The account offers one person's experience with no measured usage, matched tasks or quality comparison, and the free limits are unquantified and changeable.
- **Layer confusion in both parts.** Part A treats a consumer compute limit as a token wallet. Part B applies API controls—temperature, response schemas and caching—to a consumer Gem workflow whose documented setup shows none of them.
- **Missing denominators.** “Saves tokens” omits the human time spent copying between chats, extra prompts per split and the quality of the final output. “No worse” is asserted, not measured.
- **Self-sealing motive claim.** “Products are designed to make you upgrade” would explain any observation. The vendor's published new-chat advice is evidence against the strong form.
- **What survives.** Keep chats short and topic-bound (vendor-confirmed for usage; the free window is 32k). Move deterministic steps out of the model when real automation exists. Prune inputs before they enter context. Checkpoint between dependent steps. Treat decomposition as conditional on clean task boundaries.
- **Timeliness.** With Gems ending for personal accounts on 2026-12-17 and stackable skills replacing them, the durable form of the advice is “separate chats per task”, not “separate Gems”.

## Coverage Against TeaPrompt

| Prescription | Coverage | Delivered text |
| --- | --- | --- |
| Single-responsibility steps with handoff objects | covered | “Define the handoff object” (`04-agent/sop-compiler.md:72`); “If a step naturally needs multiple tools, split it or declare a composed stage with clear sub-artifacts” (`:107`) |
| Deterministic control flow outside the model | covered | “If they can be deterministic, do not let the model decide them silently” (`04-agent/sop-compiler.md:108`) |
| Fresh context assembled from artifacts; read only what the decision needs | covered | `03-context/context-engineering.md:18`, `:29-30`, `:46` |
| Choose topology by task shape, not decomposition by default | covered | “Pick the smallest topology that fits” (`skills/flow-control-generator/SKILL.md:61`); orchestrator-workers only when subtasks are unknown (`:68`) |
| Fail-closed pipelines with gates | covered | Deterministic exit-code gates (`skills/flow-control-generator/SKILL.md:80`); “bash `set -euo pipefail` … failed gates exit nonzero” (`:84`) |
| Untrusted fetched content reaching an outbound sink | covered | `04-agent/runtime-trust-boundary.md:97` |
| Numeric thresholds | covered differently | Caps bound observable mechanisms—`MAX_ITER` is “mandatory and small by default (≤ 10 unless justified)” (`skills/flow-loop-harness/SKILL.md:43`). Unobservable size targets from another profile were kept out of installed surfaces (`plans/astra-efficiency-rules-survey-2026-09-10.md:16`, `:52`) |
| Schema validity as correctness | covered (rejects the overclaim) | “Schema-scoped … not a correctness claim” (`plans/decision-model-survey-2026-09-18.md:78`) |
| Motive attribution | covered | “`asserted` means only the author's word supports it — treat as unverified” (`skills/reflective-review/SKILL.md:77`) |
| Context rot | covered | “intent drift and context rot are bounded, not solved” (`skills/governed-delivery/SKILL.md:19`) |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| TQ-DOC1 | This record, catalogue discovery and delivery report | **Adopted — reference documentation only** | Owner's survey and critical-assessment request; vendor-confirmed mechanism and contradicted numbers need a durable source-bound record |
| TQ-1 | Consumer-app usage advice in a portable surface | No change | Vendor-specific and volatile: Gems end 2026-12-17 and limits “may change without notice”. Reopen only for a named host whose consumer needs it |
| TQ-2 | Fixed thresholds (<4K input, <20% payload, 100% parse success) as acceptance criteria | Rejected | Unobservable in the consumer app; 100% parse success contradicted by vendor documentation |
| TQ-3 | Part B's pipeline as a template | Rejected as written | Fails open in the executed differential; `flow-control-generator` already requires fail-closed exits and gates |
| TQ-4 | Decomposition as the default (“必須拆解”) | No change | Existing topology selection is conditional on task shape |

## Evidence vs Inference

- **Verified:** source identity and text; the Google limits, usage table, fallback rule, context windows, Gems transition, Gem setup fields and Workspace action lists; the quoted research abstracts, design posts and vendor documents; `llm` semantics; executed arithmetic, pipeline differential and `jq` shape.
- **Author-reported:** the author's quota experience and claimed workload parity; Part B's uncited 32K and threshold figures.
- **[INFERENCE]:** that workload differences explain part of the author's experience; that Gemini's compute meter grows with re-read history roughly in proportion to its size, since no formula is published; and that splitting into separate chats nets less usage than one long chat, which depends on unpublished per-prompt cost.

## Falsifiability

- A published Gemini usage formula, or measured usage by chat length, could confirm or refute the quadratic analogy and the net effect of splitting.
- A matched comparison of one long chat with a decomposed workflow on the same tasks, scored for output quality and human time, would test “no worse”; anecdotes cannot.
- Changes to the limits page, the Gems transition or the dated prices invalidate the corresponding rows; re-check them instead of editing these results.
- A local consumer failure in which a TeaPrompt-generated pipeline fails open would justify an in-place `flow-control-generator` repair. An external example alone would not.

## Risks / Unknowns and Handoff

This survey did not sign in, use any quota, call a model or upload anything. Stub results establish the pipeline's control flow, not a real model's output. Product pages and prices are living documents with dated rows. No Skill, routing fixture, oracle or runtime changed, and no commit or push is included.
