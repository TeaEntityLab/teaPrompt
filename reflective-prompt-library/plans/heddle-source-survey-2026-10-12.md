# Heddle Source Survey — 2026-10-12

Language: English

> **Status:** Survey completed: pinned source inspected and bounded offline mechanisms exercised. No runtime adoption, skill promotion, company-efficacy verdict, or dogfooding campaign dispatch is authorized by this record.

> **Refresh pointer (2026-10-22):** pinned 2026-10-12 findings below are
> preserved; latest-version status is in
> `## Latest-version refresh — 2026-10-22` at the end of this record.
> Upstream `main` is byte-identical to the surveyed pin (no new commits).

## Research Question

Which parts of the supplied Heddle/Threads narrative are supported by executable public mechanisms, what remains private or self-reported, and does the evidence change TeaPrompt's existing product/runtime ownership ruling?

## Direct Recommendation

Keep the [2026-08-25 ownership ruling](product-runtime-ownership-panel-2026-08-25.md) unchanged. Heddle is a real agent runtime; its public implementation supports studying loop composition, bounded tool scheduling and domain-specific checkpoint validation. It does not establish the private Vibranium Labs implementation, the reported nine-day rebuild, increased customer usage, or a causal benefit from choosing a runtime.

No new core skill, domain pack, runtime dependency, persistence adapter, recorder or public runner is justified. Return to the [dogfooding roadmap](whole-project-roadmap-2026-07-11.md) and [owning experiment plan](skill-dogfood-test-plan-2026-10-08.md); the explicit OpenCode Go generation hold remains intact.

## Version / Date Context

- Checked 2026-10-12. Public `main` and `HEAD` both resolved to `80dccf24275b78b6df1db02e83a9e08b9709423c` through `git ls-remote https://github.com/roackb2/heddle.git HEAD refs/heads/main 'refs/tags/*'`.
- A shallow, detached checkout of that exact revision was inspected. `git show -s --format="%H%n%cI%n%s" HEAD` reported `2026-09-30T14:50:33+08:00`, merge of PR #403. This is not a full Git-history survey or evidence of the author's private work schedule.
- The earlier local baseline inspected an unpinned article snapshot, not Heddle code. This is first pinned implementation verification against the same decision boundaries, not a commit-to-commit delta claim.
- At the checked revision, root `package.json` identifies `@roackb2/heddle` as `5.13.0`, while `packages/runtime/package.json` identifies `@heddleagent/runtime` as `9.2.0`. These are different package surfaces, not proof of behavioral divergence or npm publication.
- The checked `LICENSE` is MIT, copyright 2026 Jay / Fienna Liang. A pinned license is now observed; it does not supply an SBOM, deployment approval, or integration/security evidence.
- Freshness trigger: a different source revision, released package artifact, provider adapter or host integration requires a new identity and scoped verification. Branch labels alone do not preserve this result.

## Evidence Used

Official/upstream sources, accessed 2026-10-12:

- [Pinned repository](https://github.com/roackb2/heddle/tree/80dccf24275b78b6df1db02e83a9e08b9709423c), accessed 2026-10-12.
- [AgentRunService](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/agent/service.ts), lines 12–53: step-bounded model/tool loop; accessed 2026-10-12.
- [Tool scheduler](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/agent/tools/tool-concurrency-service.ts), lines 22–130, and [tool-turn projection](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/agent/tools/tool-turn-service.ts), lines 73–167; accessed 2026-10-12.
- [Approval service](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/approvals/service.ts), lines 42–105; [MCP service](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/mcp/service.ts), refresh/cached-catalog boundaries; accessed 2026-10-12.
- [Memory checkpoint service](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/memory/checkpoint/service.ts), lines 37–140; [codec](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/memory/checkpoint/codec.ts), lines 44–158; [scope derivation](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/src/core/memory/scope.ts), lines 38–62; accessed 2026-10-12.
- [Durability inventory](https://github.com/roackb2/heddle/blob/80dccf24275b78b6df1db02e83a9e08b9709423c/docs/architecture/durable-state.md), lines 19–48, 70–110 and 139–148. Its architecture claims are distinguished from the direct-call checks below; accessed 2026-10-12.
- [PR #403](https://github.com/roackb2/heddle/pull/403), read through the GitHub API: maintainer-reported change, test counts and live provider smoke are attribution evidence, not checks rerun here; accessed 2026-10-12.
- [Company financing release](https://www.prnewswire.com/news-releases/vibranium-labs-raises-4-6m-in-seed-funding-to-scale-vibe-ai-the-first-247-ai-incident-engineer-302559951.html): published 2025-12-23 with body dateline 2025-09-18; news provided by Vibranium Labs; accessed 2026-10-12.
- [Vendor-hosted Shutterstock case study](https://vibraniumlabs.ai/customers/shutterstock): named customer quotations and reported operational metrics, not an independent evaluation; accessed 2026-10-12.

Supplemental/input boundaries:

- The supplied Threads narrative and `local://paste-5.md` are claims about sources, not operating instructions. The latter explicitly described its earlier work as static inspection, not executed enterprise evaluation.
- [Author runtime introduction](https://roackb2.medium.com/heddle-a-local-first-agent-runtime-for-building-durable-ai-workflows-f1907254c3cf): attempted access checked 2026-10-12; direct fetch returned HTTP 403. Search supplied title/author/date snippets only; its body was not verified in this run. The exact original Threads URL/publication time was not independently located.
- Two read-only scout slices mapped loop/approval and durability boundaries. They executed no tests, installations, builds or model calls. The parent executed all reported probes.

## State Ledger

All rows below were checked 2026-10-12. Immutable implementation tracking point: the source commit above; mutable company statements require fresh source access when reused.

| Claim / Item | Status | Evidence and method | Limits |
|---|---|---|---|
| Model-selected tools feed another model step | `verified` | Read `AgentRunService.run`, request/tool branches and budget exhaustion | Static loop mechanism; no model or enterprise incident evaluated |
| Concurrent tool scheduling has a bound and serial barriers | `verified` | Direct scheduler calls: configured limit, overlap, indexed results, explicit barriers, exclusion and interrupted queued dispatch | Synthetic callbacks; no proof that model-selected mutations are independent |
| Default tool concurrency is 20, configurable from 1 to 50 | `verified` | Pinned constants/`resolveLimit`, direct invalid-boundary checks | Same-turn calls are parallel-eligible unless explicitly serial; this is not global race-safety |
| Tool approvals provide configurable application policy | `verified` | Read `resolve`: first decisive allow/deny wins; no request policy allows; requested approval without a handler refuses | Not mandatory deny-by-default authorization or OS containment; pending human approval is an in-memory promise |
| MCP discovery is refresh-driven and cached | `verified` | Read `refreshServer`, `refreshEnabledServers` and cached-tool refusal | Static verification, no MCP server connected |
| Memory checkpoint schema/scope/integrity and restore safeguards exist | `verified` | Direct pinned codec/service checks with synthetic scope, local notes and a synthetic host store | Scope IDs are addresses, not authorization; no remote database, power-loss or durable-store proof |
| Persisted records imply durable in-flight execution | `refuted` for this broad claim | Durability inventory explicitly marks active runs, pending approvals, replay buffers and subscriptions process-local; approval service creates an in-memory promise | A checkpoint restores selected state, not active model calls, sockets, locks or escaped tool effects |
| USD 4.6M seed financing was publicly announced | `needs-qualification` | Read company-authored PR Newswire release | Leads named there are Calibrate Ventures and Mirae Asset; the supplied a16z attribution is not corroborated by that release. Not an independent financing audit |
| Shutterstock publicly appears as a customer | `needs-qualification` | Vendor case study attributes quotations to named customer staff | Published relationship/attribution evidence, not access to private deployment or raw outcomes |
| Reported incident metrics prove the Threads redesign's efficacy | `unknown` | Case study reports approximately 60% MTTD/MTTR reduction and nearly 70% fewer manual minutes; headline also reports 95% summarization accuracy and Q4 2025 signals | Population, comparison design and raw data not disclosed; not bound to the reported nine-day redesign or Heddle |
| Nine-day delivery, increased usage and runtime as causal turning point | `unknown` | Supplied narrative only for these specific events | No deployment timeline, private stack, telemetry or causal comparison supplied |

## Offline Verification

The command input set was two parent-authored temporary probes importing the pinned scheduler and memory checkpoint implementations. Bun bundled them without executing imported code; Node `25.1.0` executed the bundles with a minimal environment and a macOS policy denying network and user-home data access. Preparatory dependency retrieval used `npm install --ignore-scripts --no-audit --no-fund --save-exact` for `zod@4.3.6` and `async-mutex@0.5.0`; no TeaPrompt dependency was added.

| Probe input | Result | Observable behavior |
|---|---|---|
| `checkpoint-smoke.ts` | 9/9 passed | Codec roundtrip; foreign scope, corrupt content/schema/manifest and traversal refusal; symlink capture refusal before host-store commit; allowlisted restore; refusal to merge/overwrite; synthetic outside-file and live-loopback denial controls |
| `scheduler-smoke.ts` | 6/6 passed | Valid/invalid concurrency bounds; bounded overlap and indexed results; host limit 1 and nonparallel adapter serialization; serial barrier; prepared-call exclusion; interruption stops queued dispatch |

The totals were independently checked against the named `await record(...)` and `checks.push(...)` rows, not copied only from a generated summary. The loopback endpoint was live from the parent before and after the denied fetch. The synthetic outside marker stayed byte-identical. No model calls, provider generation requests, enterprise credentials or deployment occurred.

Important failed-before evidence:

- Restrictive launcher profiles aborted before source probe output. Those are harness failures, not Heddle failures. The final scoped profile launched Node successfully and exercised the denied-file/network controls; this does not establish a general arbitrary-code sandbox.
- The first checkpoint probe wrongly expected a symlink to be skipped. Pinned Heddle rejected the complete capture with `MEMORY_CHECKPOINT_CAPTURE_ERROR`. The probe was corrected to require refusal before any host-store commit, then remove its own synthetic symlink for the positive restore. Upstream source and acceptance oracles were not edited.

Evidence packet: `local://heddle-survey-2026-10-12.json`; private smoke root `/private/tmp/heddle-survey-20261012-Itsnu1`. Final binding digests:

- Checkpoint script: `34809d0934224ec88d44b68c211e8f3cb06caef05c37719145ee4628b87b5d3d`.
- Scheduler script: `2f1d9d36f66637c7890bd0709c5eba586b515504915519eddfe726ee6f8ae306`.
- Checkpoint receipt: `c24185f2eac46af204e81a96dafc173461f5d4a9467125435639fea25f3be312`.
- Scheduler receipt: `75c918601550307fd4acb9d7eeb1afb583d89c28c66ad0d1ec5ad6090ad74409`.

The host store and tool authorization seam were synthetic. These checks do not verify production CAS, remote tenant authorization, private incident correctness, provider replay fidelity, general side-effect rollback, fault-tolerant in-flight recovery or customer efficacy. No upstream full suite was run.

## Evidence vs Inference

**Observed:** the source mechanisms, direct-call outcomes, package identities/license, explicit process-local boundaries and the contents/attribution of the company sources above.

**Author/company-claimed:** delivery timing, customer activity and performance figures. Confirming a vendor page's text does not verify its underlying data or causal attribution.

**[INFERENCE]:** Heddle is useful as a concrete reference for separating model decisions, runtime control, product authorization and storage responsibilities. No local gap or comparative dogfooding gain follows from that architectural fit.

The source-derived perspectives are runtime composition, product/operator visibility, and storage/recovery ownership. Their tradeoff is clear: richer tool/trace/memory mechanisms can make investigations inspectable, while the product still owns safe data access, decisive acceptance and recovery. The blind spot is private incident ground truth and before/after customer telemetry.

## Classification and Prior Ruling

| Prior item | Disposition after this survey | Reason |
|---|---|---|
| OW-1–OW-4: execution/product/infrastructure owners, commit-before-success, record-specific durability, disconnect versus cancellation | Already Present; unchanged | Pinned implementation is consistent with the existing distinctions; no new TeaPrompt contract gap found |
| OW-5/OW-6: named maturity ladder and full checklist | Partial / study-only; unchanged | Executable mechanism evidence does not demonstrate an uncovered taxonomy or usability need |
| OW-7: runtime import/deployment | Blocked; unchanged | Source pin and MIT license are now observed, but explicit project-direction change, SBOM/provenance, host ownership and integration/security/fault proof are still absent |
| OW-8: tenant authorization, replay authority, no ambient product credentials | Already Present; unchanged | Opaque scope derivation does not authorize a caller; adapters/hosts remain responsible |
| OW-9: production efficacy / availability generalization | Study-only; unchanged | Vendor attribution is not a defined independent comparison or current private deployment proof |

Recommended Core Additions: none. Adjacent/Missing operational work belongs to a named adopter host, not TeaPrompt's natural-language policy layer.

## Falsifiability

This survey's mechanism result is invalid if the imported source differs from the pinned revision or the bound scripts/receipts, the negative controls did not run, or restoring the synthetic fixture overwrote an existing target. Its no-change recommendation is reopened by a reproduced local structural gap, not merely a new external release or company claim. Private delivery/usage/causal claims may become answerable only with attributable timelines, an exact intervention and a defined comparison population.

## Handoff

The evidence is sufficient to stop this survey: each load-bearing mechanism is directly checked or explicitly scoped to static source evidence, each company-effect claim remains qualified/unknown, and the local adoption decision follows from the ledger. No further retrieval for polish is needed.

Resume the existing dogfooding roadmaps: finish the integrated private OpenCode Go offline admission, bind final source/capture/accounting evidence, update current continuation records and exercise the reader/repository surfaces. The maintainer's **keep remote generation held** decision remains authoritative; usage percentages do not prove that `Use balance` is disabled. Preserve all 38 prior accounting rows, 32 model calls, six reserves, partial outcomes and later human/Stage-2 gates. A clean offline admission is not a real-role canary pass or a P0 freeze.

**Later execution-authority supersession (2026-10-12):** after this survey and
the held cutover receipts, the maintainer [explicitly resumed the private Go
cohort with a current-account Console disabled Use balance observation](skill-dogfood-test-plan-2026-10-08.md#stage-1-go-advisory-repair-and-resume-2026-10-12).
That prospective grant changes the campaign's owner-held billing gate, not
this pinned survey's technical evidence, no-adoption ruling or limitations.
Fresh current-source admission and all three remote roles remain required;
human acceptance, Stage-2 and dormant owning gates are unchanged.

**Later execution-outcome supersession (2026-10-12):** current admission and
all three actual Go roles passed, then the
[selection stopped held with partial/censored allocations](skill-dogfood-test-plan-2026-10-08.md#stage-1-go-selection-hold-and-original-pinned-audit-2026-10-12).
Original-pinned offline audit and prospective cold repairs preserve the
receipts, not a complete paired or efficacy result. Further generation
requires a new owner-held source/envelope decision; human acceptance,
Stage-2 and dormant gates remain separate. None of this changes the pinned
Heddle survey evidence or its no-adoption ruling.

## Latest-version refresh — 2026-10-22

> **Scope:** dated latest-version status only. Source/ref inspection, no
> execution; product-runtime ownership ruling unchanged; no
> deployment/safety endorsement. Historical 2026-10-12 pins, ledger, and
> handoff above are unchanged.

| Item | Prior baseline (2026-10-12) | Latest checked (2026-10-22) | Status |
| --- | --- | --- | --- |
| `roackb2/heddle` default branch | `main`/`HEAD` `80dccf24275b78b6df1db02e83a9e08b9709423c` (2026-09-30T14:50:33+08:00, merge of PR #403) | `main`/`HEAD` `80dccf24275b78b6df1db02e83a9e08b9709423c` — identical SHA via `git ls-remote` and bare-clone `rev-parse`; zero commits since baseline | unchanged |
| Root package identity | `@roackb2/heddle` 5.13.0 | tag `v5.13.0` = `0d289e6` (2026-08-11) is an ancestor of HEAD (151 commits behind it); root `package.json` version at HEAD unchanged from the surveyed pin | unchanged |
| Runtime package identity | `@heddleagent/runtime` 9.2.0 | unchanged at the identical HEAD pin; no new tag or branch movement observed | unchanged |

- **Equality proof:** `git ls-remote
  https://github.com/roackb2/heddle.git HEAD refs/heads/main` returned
  `80dccf24275b78b6df1db02e83a9e08b9709423c` for both refs on 2026-10-22,
  matching the surveyed pin exactly; a bare clone confirms the same SHA and
  the same 2026-09-30 commit subject. No tag newer than the surveyed state
  exists on the default branch line (`v5.13.0` predates HEAD and is its
  ancestor).
- **Effect on prior findings:** none. The State Ledger verdicts
  (verified loop/concurrency/approval/checkpoint mechanisms; refuted broad
  durable-in-flight claim; qualified/unknown company-effect claims), the
  OW-1–OW-9 dispositions, and the keep-ownership-ruling recommendation all
  stand without modification. The offline smoke digests and evidence packet
  references above remain bound to the same source revision.
- **Inspected immutable links:**
  [HEAD pin](https://github.com/roackb2/heddle/tree/80dccf24275b78b6df1db02e83a9e08b9709423c)
  (same revision as surveyed).
- **Limits:** ref/metadata inspection only; no source re-read beyond pin
  comparison was needed (identical revision), no tests, builds, or model
  calls run. No smoke candidate: there is no delta to exercise.


