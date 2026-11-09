# Eian: Staged Video Production, Approval Boundaries and Color Evidence (2026-11-09)
Language: English

> **Status: reference documentation adopted (`EI-DOC1`); optional creative-reference navigation adopted (`EI-DOC2`).** The owner requested a survey, then explicitly requested documentation updates and a commit. This record internalizes the completed research, not the article's operating prompts. No Skill, routing, runtime, installed configuration, provider campaign or push is adopted. Earlier survey decisions remain unchanged.

## Research Question and Direct Recommendation

Which parts of Eian's Claude Code / Codex + Seedance production workflow are supported, transferable and useful to TeaPrompt?

**Preserve staged artifacts and checks before expensive generation, not a mandatory four-agent production system.** Story, storyboard, visual references, frame pairs, generation requests and the final audiovisual deliverable require different evidence. A reviewer verdict is not permission to spend, a spending limit in prose is not an enforced budget, and sampled stills are not full audiovisual acceptance.

The useful addition is a source-qualified example discoverable from the existing [creative lens](../05-domain/creative-template.md). [SOP Compiler](../04-agent/sop-compiler.md), [Review](../skills/reflective-review/SKILL.md) and the [runtime trust boundary](../04-agent/runtime-trust-boundary.md) already cover the obligations. No missing Skill contract was established; local usage recurrence and comparative efficacy remain unknown, not zero.

## Sources, Identity and Access

The supplied [post](https://x.com/eianlu/status/2118317430665613741) and [article](https://x.com/i/article/2118298893238845441), checked 2026-11-09, were unavailable through native X. The complete structured mirror identifies the article as *Claude code/Codex+Seedance AI视频：从一个想法到成片的全流程*, with creation and modification time `2026-11-05T12:20:06.000Z`. It is not publisher-authenticated historical provenance.

The inventory covers **165 body blocks**, independently counted through the parsed array and raw block-type enumeration; **13 Markdown entities**, including embedded prompts/tables; six body illustrations plus the cover. It does not establish video quality or author execution. `B001`–`B165` below refer to the survey's one-based body order, not line numbers in a live webpage.

| ID | Source / evidence inspected | Access and scope |
| --- | --- | --- |
| S01 | [Complete FxTwitter mirror](https://api.fxtwitter.com/eianlu/status/2118317430665613741) | Checked 2026-11-09: complete structured body and seven images inspected; mirror authenticity and actual production receipts not verified. |
| S02 | [Official Codex imagegen sample](https://raw.githubusercontent.com/openai/codex/14a477ea89712071944244022e8a10142845456e/codex-rs/skills/src/assets/samples/imagegen/SKILL.md) | Checked 2026-11-09: fixed source commit `14a477ea89712071944244022e8a10142845456e`, not an installed-version pin or proof of the author's configuration. |
| S03 | [Official developer CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | Checked 2026-11-09: `codex exec`, image input, stdin and sandbox flags; no CLI generation run. |
| S04 | [Official Image API guide](https://developers.openai.com/api/docs/guides/tools-image-generation) | Checked 2026-11-09: distinct API surface; not a specification of Codex subscription quotas or the author's bill. |
| S05 | [Claude Code subagents](https://code.claude.com/docs/en/sub-agents.md) | Checked 2026-11-09: context, fork/resume exceptions, tool/permission controls and agent-message approval limits; no configured-host test. |
| S06 | [Seedance model catalogue](https://docs.volcengine.com/docs/ark/model-list?lang=zh) | Checked 2026-11-09: named model IDs, resolutions and duration ranges. |
| S07 | [Create video-generation task API](https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh) | Checked 2026-11-09: first/last-frame roles, activation prerequisites and request endpoint; no request submitted. |
| S08 | [Official model pricing](https://docs.volcengine.com/docs/ark/model-pricing) | Checked 2026-11-09: conditional video price examples and token/success billing; no account or invoice inspected. |
| S09 | [Cancel/delete video-generation tasks](https://docs.volcengine.com/docs/ark/cancel-or-delete-video-generation-tasks-api?lang=zh) | Checked 2026-11-09: state-dependent cancellation/deletion table; no remote mutation. |
| S10 | [Seedance 2.5 prompt guide](https://docs.volcengine.com/docs/ark/seedance-2-5-prompt-guide?lang=zh) | Checked 2026-11-09: timeline advice and scoped editing-duration caveat; linked installation instructions were not executed. |
| S11 | [FFmpeg filter documentation](https://www.ffmpeg.org/ffmpeg-filters.html) | Checked 2026-11-09: `setparams`, `colorspace` and `scale`; separate synthetic FFmpeg 9.0.2 execution below. |

These are the survey's support sources, not eleven independent empirical replications or eleven links claimed to be cited by the article. Refresh live product documentation, model IDs, prices and account requirements before any execution.

## Article Coverage

| Blocks / stage | Transferable idea | Qualification |
| --- | --- | --- |
| B008–B023: tool division | Separate creative direction, production, review and approval | Specific vendors are replaceable; documented capabilities do not prove account operability. |
| B026–B051: story | Check causality, audience interpretation and feasibility before generating | A reviewer retelling the story can expose ambiguity; this is not measured efficacy. |
| B052–B092: storyboard | Specify camera, motion, continuity, palette and readable composition | Golden-ratio positions and limits on frontal views are author preferences, not universal rules. |
| B093–B101: style and references | Confirm style and preserve character/prop/location invariants | References constrain intent, not guaranteed model output. |
| B102–B116: first/last frames | Inspect geometry, props, overlays and small-screen readability | Local edits may alter other pixels; crop/composite is a conditional repair, not a vendor-mandated universal method. |
| B117–B129: requests and preflight | Compare descriptions with actual assets before approval | Seven-part prompts and sub-second cues are not deterministic timing interfaces. |
| B130–B141: generation and repair | Try a difficult sample, retain candidates, consider editing before retrying | Low retry rates and prompt-blame heuristics have no controlled denominator here. |
| B142–B146: post-production | Use deterministic editing and inspect transitions/color | Upscaling is not recovery of native detail; color interpretation requires actual media evidence. |
| B147–B151: final review | Disclose what decoding/still sampling did and did not observe | The article explicitly leaves motion/audio unverified; retain that limit. |
| B152–B160: four roles | Separate maker, reviewer, requirements monitor and preference proxy | Optional roles, not proof of isolation, current intent, accepted results or enforced spending limits. |

## Product Claims and Interpretation Boundaries

**Codex (S02–S04).** The checked sources support `exec`, `--skip-git-repo-check`, `-s read-only`, `-i`, stdin `-`, built-in image generation/editing and output beneath `$CODEX_HOME/generated_images/`. `CODEX_HOME` is configurable; a particular session subpath is not a permanent interface. `-i` attaches an image; it does not guarantee pixel invariance. Sandbox flags for model-generated commands do not establish that every tool output or billing effect is absent. The author's no-extra-money redraw claim remains account-specific; subscription usage, purchased capacity and API billing are different. No fixed image/text quota multiplier was established.

**Seedance identity and inputs (S06–S07).** `doubao-seedance-2-5-260628` is listed for 4–30 seconds and 480p/720p/1080p; `doubao-seedance-2-0-mini-260615` for 4–15 seconds and 480p/720p. The POST task API supports `content[].role` values `first_frame` and `last_frame`, distinct from generic `reference_image` semantics. Do not assume input modes can be mixed arbitrarily. No generation or activation was attempted. “Do not recharge” does not assert zero pre-existing balance; activation requirements therefore do not by themselves contradict the article.

**Conditional pricing (S08).** The checked examples are **720p, 16:9, five output seconds, with no input video**, in RMB:

| Model | Example clip price | Rounded price per second |
| --- | ---: | ---: |
| Seedance 2.5 | 7.56 | 1.51 |
| Seedance 2.0 Mini | 2.48 | 0.50 |

“About three times” fits these examples, not every configuration or an exact ratio. Actual usage is reported through `usage.completion_tokens`; resolution and input video affect cost. The documentation's successful-generation billing condition does not make a successfully generated but unwanted clip free. Total project cost also includes retries, other tools and human work, none measured here.

**Cancellation and delegation (S05, S09).** `queued` tasks can be cancelled; `running` does not support DELETE; deleting a successful task removes its record, not the historical expenditure. Stopping a local agent cannot establish remote cancellation or refund. This is a boundary on adopting the workflow, not an allegation that the article explicitly promised to cancel running work. B023's per-request human approval and B160's proposed bounded delegation are different modes, not necessarily contradictory. A preference proxy cannot infer new authority; an enforced total budget must account for already-submitted work. No such implementation was tested.

**Reviewer context and permissions (S05).** A non-fork subagent starts a separate context but receives the delegating task and configured context; fork/resume exceptions matter. Fresh context is not cognitive independence. Read-only prose is not confinement: effective tool permissions and Bash/MCP capabilities matter, not just disabling Write/Edit. Agent messages do not satisfy a pending human permission prompt. The article's four-role execution and budget enforcement remain unverified, not proven impossible.

**Timing and image fidelity (S02, S07, S10).** The article already calls timing approximate. Second-scale narrative organization does not guarantee 0.2/0.3-second event placement. The guide's roughly 0.3-second input/output duration caveat concerns video editing, not a bound on every generation task. The prompt guide and API use differing stretch/crop descriptions for tail-frame adjustment; same-aspect inputs plus actual inspection avoid assuming either untested behavior. Whole-image changes, patch seams, lighting and encoding still need evaluation when compositing a local repair.

**Color (S11, B146).** The claim that every Seedance MP4 should be read as BT.601 then labeled BT.709 has no original-bitstream or metadata evidence in the survey. `setparams` changes frame properties; `colorspace` can transform pixel representations. `in_color_matrix`/`out_color_matrix` belong to `scale`, not `setparams`; `colorspace` uses options such as `ispace`. A file extension or resolution does not determine matrix, range, transfer or primaries. Inspect actual media and state unresolved assumptions before interpreting or converting it.

## Executed Color Boundary Check

The completed survey ran three commands with **FFmpeg 9.0.2**, one 64×64 synthetic frame and raw `yuv444p` output. No Seedance input, model call or audiovisual file was used. This is a deliberately declared input-color scenario, not a claim that the synthetic source or any vendor file naturally has the declared metadata.

Common argv: `/opt/homebrew/bin/ffmpeg -hide_banner -loglevel error -f lavfi -i testsrc2=size=64x64:rate=1 -frames:v 1 -vf FILTER -pix_fmt yuv444p -f rawvideo pipe:1`. `FILTER` was replaced by each exact string below; output bytes were captured in memory and SHA-256 hashed, not written to a media file.

```text
baseline:
format=yuv444p,setparams=range=limited:color_primaries=bt709:color_trc=bt709:colorspace=smpte170m

retag:
format=yuv444p,setparams=range=limited:color_primaries=bt709:color_trc=bt709:colorspace=smpte170m,setparams=colorspace=bt709

matrix conversion:
format=yuv444p,setparams=range=limited:color_primaries=bt709:color_trc=bt709:colorspace=smpte170m,colorspace=ispace=smpte170m:iprimaries=bt709:itrc=bt709:irange=tv:space=bt709:primaries=bt709:trc=bt709:range=tv:format=yuv444p:fast=1
```

| Case | Exit | Raw output bytes | SHA-256 |
| --- | ---: | ---: | --- |
| baseline | 0 | 12288 | `063b165491d5dc3d1938b4128b0cdf4f7b336d48cc477241f18a016a2197a9d2` |
| retag | 0 | 12288 | `063b165491d5dc3d1938b4128b0cdf4f7b336d48cc477241f18a016a2197a9d2` |
| matrix conversion | 0 | 12288 | `4d159b1fcaf061c60f24761f0dd756c452e62ba404dd2f543f359e022e3f3151` |

All stderr strings were empty. Retagging preserved the pixel bytes; conversion changed them. This proves the bounded distinction, not the correct interpretation of unexamined Seedance footage. It also does not test all range, transfer, primaries or encoder combinations. The recorded executable path and version scope the receipt, not a portable installation requirement.

## Optional Worked Reference: Staged Video Acceptance

**[INFERENCE] Illustrative application of existing contracts, not an executed production run or a new workflow.** Suppose a creator wants a short product video with a fixed character and final voiceover:

| Decision point | Artifact and question | Acceptance boundary |
| --- | --- | --- |
| Intent and story | Current brief, audience, message, non-goals and a readable story | Preserve rejected/changed requirements separately; the entire chat is not the canonical current spec. |
| Low-cost visual checks | Storyboard, palette/character references and frame pairs | Compare actual assets with requested continuity and composition; a story-blind review still needs enough context for its assigned question. |
| Before generation | Exact model/input settings, quoted cost, retry limit and outstanding commitments | The owner or an explicitly delegated policy decides; the host must enforce permissions and spending. Existing [Risk](../skills/reflective-risk/SKILL.md) / Human Review applies before costly external effects. |
| Returned clips | Actual motion, continuity, timing, input/output media properties | Check what was produced rather than trusting the prompt. Do not treat successful generation as creative acceptance. |
| Final deliverable | Rendered video plus audio, captions and brand/rights requirements | Frame sampling and decoding are partial evidence; leave unobserved motion/audio unresolved until actually reviewed. |

The example does not require four agents, any named vendor, a fixed aesthetic ratio or blanket BT.601 interpretation. Use the smallest sufficient tool/role arrangement. Public release and rights decisions remain with the relevant human owner.

## Existing Coverage and Candidate Adoption Ledger

| Concept | Checked delivered surface | Result |
| --- | --- | --- |
| Artifacts, stage gates and failure handling | [SOP Compiler](../04-agent/sop-compiler.md) §4–7 | Already covered; LLM review is advisory, not a hard gate. |
| Scene constraints and actual-preview evidence | [Creative Template](../05-domain/creative-template.md), Acceptance Criteria / Validation Rules | Already covered; optional example adds discoverability, not a new output contract. |
| Bounded review context and correlated errors | [Workflow Recipes](../04-agent/workflow-recipes.md), Parallel Lens Review; [Review](../skills/reflective-review/SKILL.md), Claims Ledger | Already covered; separate story interpretation from constraints/compliance review. |
| Current intent and handoff | [Brief](../skills/reflective-brief/SKILL.md), Intent Fidelity; [Context Handoff](../03-context/context-handoff.md) | Already covered; preserve withdrawn/unknown assumptions. |
| Authority, costs and external effects | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md), sections 3–4a | Already covered as methodology; operational enforcement remains host-owned. |

### Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| EI-DOC1 | Durable source record, bounded color receipt, worked reference and catalogue discovery | Adopted; reference documentation only | Explicit owner request; otherwise the completed survey existed only in session artifacts. Revise on material source/product changes or a reproducible error in the receipt. |
| EI-DOC2 | Optional reference link from existing creative documentation | Adopted; navigation outside the prompt fence | Makes the example discoverable while preserving the existing creative output contract. Remove if redundant or misleading. |
| EI-SK1 | New video/four-role Skill or duplicate generic rules | No change | Existing contracts cover the mechanisms. A named local gap could reopen consideration; external anecdotes alone do not satisfy promotion gates. |
| EI-RULE1 | Universal free redraws, fixed aesthetic thresholds, exact prompt timing or blanket color interpretation | Rejected as universal rules | Account, task and media conditions are missing or explicitly variable. Retain source-qualified experience instead. |
| EI-RUN1 | Install/generate/publish or automate approvals and spending | Not adopted; outside documentation scope | Requires separate authority, configured-host evidence, account/budget conditions and actual audiovisual acceptance. |

Promotion boundary: readers planning or reviewing generated media are the trigger; source-qualified observations, their creative brief and existing contracts are inputs. The output is a better-specified decision or artifact, not an executable runner. Authority class: non-authoritative reference; approval: the owner's explicit documentation request. Source/tool changes, absent enforcement or a reader mistaking the example for generation/release permission trigger review. Composition and consistency checks verify publication, not creative efficacy.

## Evidence vs Inference and Verification

- **Observed in the survey:** complete mirrored body/entity extraction, viewed illustrations, the named official-source passages, current local coverage and three executed FFmpeg cases. Source verification means the text was checked, not that its claimed outcome was reproduced.
- **Author-reported:** low retry frequency, the reviewer catching a 13% cup-size difference, model preferences, local edit drift, darkening across clips and creative heuristics. No independent trial, sample denominator, full cost ledger or author workflow audit supports a general effect.
- **[INFERENCE]:** earlier artifact checks can expose avoidable errors before a costly step. Neither the best agent count nor a measured cost/quality improvement follows from this survey.
- **Unknown:** native-X authenticity, account-specific availability/billing, real Seedance media properties, complete video/audio quality and four-role enforcement. These are not prerequisites for reference publication; they are prerequisites for stronger operational claims.

The source snapshot's resolved block text SHA-256 is `5ccb5c2a01875c31a90d64902a2b11144d63375339b9c3f595776396f38d36f0`. It fingerprints the UTF-8 serialization of the survey's numbered block/type/text plus expanded entity content, excluding image binaries and external-document bytes; it is not publisher authentication. Session receipts are named `eian-video-ledger-2026-11-09.json`, `eian-video-color-smoke-2026-11-09.json` and `eian-video-delivery-2026-11-09.json`. This document retains the sources, methods, results and limits without depending on those temporary files.

Two source-research slices informed the survey, not an independent efficacy panel. Integration rejected unsupported draft claims about a fixed 3–5x image quota multiplier, mandatory compositing and cryptographic approval; it also corrected the zero-balance/recharge conflation and the overbroad editing-duration interpretation. Reviewer agreement was not accepted as source evidence.

Publication verification for this follow-through is recorded in the [delivery report](../../review/final-report.md#eian-video-workflow-documentation-follow-through-2026-11-09). No new permanent wording test, Skill change or live generation experiment is required for this documentation-only outcome.

## Falsifiability and Handoff

- Recovered original text or changed official documentation can reopen the affected source claim; a stale price or model ID must not become a standing recommendation.
- Actual media metadata plus controlled pixel comparisons can resolve a color question that this synthetic check cannot.
- Matched production tasks with full cost, failures and audiovisual acceptance could establish efficacy; a plausible recipe, successful subprocess or reviewer consensus cannot.
- A current delivered-contract failure could justify an in-place repair. A new Skill or runtime still needs its own promotion and authority gates.
- Sufficiency: the useful concepts have source/coverage maps, the bounded experiment is reproducible from this record, and unknowns are not silently treated as approval or acceptance.

No model generation, account/credential inspection, package installation, media-rights clearance or runtime certification was performed or authorized by this documentation delivery. The requested commit is separate from any future operational adoption; no push is included.
