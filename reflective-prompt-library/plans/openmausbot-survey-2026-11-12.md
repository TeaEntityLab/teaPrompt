# OpenMausBot Source Survey — Approval, Portable Teams, and Execution Boundaries (2026-11-12)
Language: English

> **Status: reference documentation and navigation adopted (`OMB-DOC1/2`); no Skill, operating-rule, or runtime change.** The owner asked to survey OpenMausBot and update Docs or Skills where supported. Existing TeaPrompt contracts already require the transferable distinctions. This record preserves the pinned implementation, conflicting upstream descriptions, and a bounded offline receipt. It does not authorize installation, account access, computer control, or deployment.

## Research Question and Direct Recommendation

Which OpenMausBot mechanisms are useful to TeaPrompt, and do they expose a missing delivered contract?

**Keep a source-qualified worked reference; do not add a Skill or adopt the runtime.** OpenMausBot is an application and agent host, not just a prompt pack: an Electron/web interface and local harness coordinate provider CLIs, bots, conversations, computer surfaces, connected apps, skills, memory, and scheduled work. Those operational features are outside TeaPrompt's standing runtime scope. Its useful lessons are narrower: distinguish runtime defaults from marketing descriptions, portable configuration from recipient authority, provider permission from product confirmation, and active-work limits from wall-clock or external-effect guarantees.

The important findings are not a security certification:

- New bots without a stored approval mode resolve to **Full access outside a hosted company workspace**, including the generic file-import path. The README's claim that imports start on Ask conflicts with both the detailed sharing document and source.
- **Ask is not a universal product-mutation confirmation mode.** Selected non-guest product changes can apply directly with an Undo receipt. Trigger changes are explicitly documented as immediate. A provider permission card, an application confirmation, and business acceptance are different boundaries.
- **A Local VM is not synonymous with one isolated computer per bot or denied network egress.** Its default allocation mode is shared; the inspected `network: loopback` status checks published viewer ports. Linux turn boxing is a separate, conditional mechanism.
- **Local-first is not no-egress or all-encrypted storage.** Client analytics defaults on; CLI/server configuration can contain plaintext credentials. The repository also has an enterprise license carve-out.

## Version and Source Identity

Checked 2026-11-12. These are separate distribution identities, not a claim that their bytes or behavior are interchangeable.

| Surface | Observed identity | Evidence boundary |
| --- | --- | --- |
| `main` and `HEAD` | `1a4e4da9f380804ad98c7fd1b141bb0dbfafced4` | `git ls-remote` at start and end; unchanged |
| GitHub release/tag | `v0.1.154`, same commit; release published 2026-11-12 | Releases API and exact-tag sparse checkout; source `package.json` says `0.1.154`; no packaged desktop binary run |
| npm `openmausbot/latest` | `0.1.153`; tarball shasum `1a48eddc4acc44a06d291448b9d74651053c9bb5` | Registry metadata only; tarball neither downloaded nor executed |
| License | Apache-2.0 except `enterprise/`; third-party notices remain separate | Enterprise license permits evaluation but restricts production use and redistribution/hosting; not a blanket Apache grant or a legal opinion |

Primary references, checked 2026-11-12: [pinned repository](https://github.com/milind-soni/OpenMausBot/tree/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4), [release](https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.154), [npm metadata](https://registry.npmjs.org/openmausbot/latest), [licensing](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/LICENSING.md), [enterprise license](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/enterprise/LICENSE).

## Evidence Actually Checked

- Coordinator reads: README, security/licensing, package manifest, Compose configuration, computer/sharing/analytics documents, built-in verification-skill body, and the implementation sections cited below.
- Two read-only scouts traced independent authority/computer and package/scheduler slices. Their findings were leads, not separate empirical verification; decisive claims below were checked against source or exercised by the coordinator. Their cited upstream tests were **not** run.
- Executed original-module functions under Node `v25.1.0` on Darwin arm64, using a temporary checkout, synthetic inputs, a scrubbed environment, a temporary HOME, and checked `sandbox-exec` restrictions. Nineteen observations passed; seven host-boundary controls passed. No upstream service, UI, provider CLI, VM, or model was started.
- Compared the delivered bodies of TeaPrompt's runtime-trust-boundary, artifact-promotion, workflow-acquisition, and risk/review/handoff Skills. This establishes textual coverage, not runtime compliance.
- Semantic `find` failed with HTTP 403 before returning ranked evidence; literal/path searches were the fallback. A failed search was not counted as evidence of absence.

### Source map

All upstream links below are immutable commit links, checked 2026-11-12. Paths and functions scope each claim; unexecuted source is not a live-system result.

| ID | Source read | What it supports |
| --- | --- | --- |
| S1 | [README](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/README.md) — checked 2026-11-12 | Product architecture; import Ask claim at 218–225; immediate triggers at 430–445; credential storage at 522–530 |
| S2 | [Approval resolution](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/shared/approval-mode.ts#L71-L102), [startup default](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/index.ts#L753-L761) — checked 2026-11-12 | Full default, unknown-value and pending-grant Ask behavior; hosted-workspace override |
| S3 | [Permission broker and delegation](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/auto-approve.ts), [safety floor](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/safety-floor-gate.ts#L1-L38) — checked 2026-11-12 | Full branch precedes sandbox-widening/outbound checks; Chief delegation; floor off by default and unable to intercept engines that never ask |
| S4 | [Direct apply](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/direct-apply.ts), [caller](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/index.ts#L3089-L3099), [skill-switch application](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/host/skill-switch-host.ts#L121-L152) — checked 2026-11-12 | Eligible non-guest changes can apply below Full; pending and applied receipts differ |
| S5 | [Security policy](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/SECURITY.md), [service allowlist](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/request-auth.ts#L30-L58), [capability lifecycle](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/index.ts#L1670-L1813) — checked 2026-11-12 | Explicitly acknowledged Slack/service-loopback risk; active generation and lease checks; stable bearer reuse is not the active authority record |
| S6 | [Sharing document](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/docs/team-sharing.md#L79-L105), [package importer](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/package-import.ts), [file-import route](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/routes/teams.ts#L353-L373) — checked 2026-11-12 | File trust is caller-owned; imported bots omit approval mode; skills/routines/connections have distinct activation paths |
| S7 | [Package schema/parser](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/shared/package-format.ts), [skill installation](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/skills.ts#L545-L560) — checked 2026-11-12 | Bounded portable fields, memory seed scope, file publisher stripping, disabled generic skills versus enabled organization skills |
| S8 | [Routine tick](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/routines.ts#L998-L1062), [wait accounting](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/routine-waits.ts#L50-L62) — checked 2026-11-12 | Overlap skip/one queued occurrence; optional limit uses active time excluding human waits |
| S9 | [Local VM defaults](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/local-vm-settings.ts#L14-L45), [container status](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/container-computer.ts#L557-L578), [turn-box detection](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/bot-box/detect.ts#L27-L72) — checked 2026-11-12 | Shared VM default; viewer-port scope of loopback status; Linux/cloud/environment prerequisites for bubblewrap |
| S10 | [Linux capability predicate](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/electron/capabilities.cjs#L19-L67), [computer integration document](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/docs/computer-use-integration.md), [surface selection](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/surface.ts#L51-L85) — checked 2026-11-12 | GNOME Wayland block versus stale beta description; Hyprland plugin predicate; unavailable pinned browser does not authorize host fallback |
| S11 | [Telemetry implementation](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/src/lib/analytics.ts#L9-L105), [analytics document](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/docs/analytics.md) — checked 2026-11-12 | Default on without opt-out; storage exception also returns true; opted-out initialization suppressed; PostHog US endpoint |
| S12 | [Built-in verification-skill authoring](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/skills/create-verification-skill/SKILL.md) — checked 2026-11-12 | Explicit request, real workflow proof, isolated profile, small feature map, cleanup ownership, applied-versus-pending receipt |
| S13 | [Question routing](https://github.com/milind-soni/OpenMausBot/blob/1a4e4da9f380804ad98c7fd1b141bb0dbfafced4/server/host/question-routing.ts#L58-L66) — checked 2026-11-12 | Separate handed-off-work path may suppress non-person-only questions at Full; broker's AskUserQuestion refusal is not a whole-product guarantee |

## Evidence vs Inference

| Mechanism | Observed boundary | Ruling and limits |
| --- | --- | --- |
| Approval defaults | S2 functions return Full for unset non-hosted bots, Ask for invalid values or pending grants; startup sets Ask for hosted workspaces. S6 importer leaves mode unset. | README's universal imported-Ask sentence is contradicted. Default resolution was executed; full HTTP import was not. Do not turn this into a claim that every deployment is Full. |
| Provider permission versus product mutation | S3 broker approves explicit sandbox widening and a named outbound tool at Full; below Full it holds those requests. S4 can return `level` for a non-Full product change and applies skill switches when direct permission is supplied. S1 says triggers apply without confirmation. | SECURITY's blanket description of Full as explicit provider-only approval does not describe all these paths. Undo is after-the-fact state recovery, not prior authorization. No external send, credential operation, or skill mutation was executed. |
| Questions and delegation | Broker holds `AskUserQuestion` even at Full. S13 separately suppresses eligible handed-off-work questions; S3 Chief-to-teammate delegation can raise the receiving thread to Full when supported. | A broker result is not end-to-end assurance that a person always receives a question or that all peer work retains the recipient's previous level. Guest/private/person-only conditions must stay explicit. |
| Internal authority | S5 maps internal capability records to active generation, thread/bot/service context and applicable leases; session bearers can be reused while active records change. The same source explicitly acknowledges session-less service-loopback access to Slack-compatible routes. | A per-turn integration gate does not establish isolation of every HTTP route or of local shell privileges. The documented gap is reported, not newly exploited or certified fixed. |
| Portable team packages | S6/S7 file imports strip claimed publisher identity, do not apply suggested approval, disable generic skills, pause routines, and create disabled connection slots. Organization-channel skills are enabled by a distinct trusted caller. | Activation depends on channel and recipient defaults, not just package bytes. This is not an all-inert payload: memory seeds are written, `recordBrowserSteps: true` is copied without a card, and a package leader becomes Chief within the new team. Redaction/schema checks do not prove harmless instructions. |
| Schedules and recovery | S8 prevents an additional overlapping occurrence unless queue mode has no scheduled run already queued. Limits are optional and subtract human wait time; duration is display metadata. | Overlap control is not exactly-once external effects. The arithmetic was exercised, not scheduler recovery, stop delivery, crash rollback, or sink idempotency. |
| Computer surfaces | S9 default Local VM mode is shared; turn boxing is separately selected and requires Linux/bwrap support. S10 blocks GNOME Wayland and requires an active plugin for Hyprland; an unavailable pinned browser has no host fallback. | Separate placement, allocation, credentials, egress, permission, and input-seat control. Capability predicates were exercised with synthetic Linux inputs on macOS, not on a real compositor or VM. |
| Privacy and licensing | S1/S11 and licensing documents disclose plaintext exceptions, enabled-by-default analytics, and the enterprise carve-out. | These are source/configuration findings. No telemetry client was initialized, credential store opened, hosted deployment audited, or license compatibility decision made. |
| Verification-skill authoring | S12 requires a launch/health/workflow/evidence/cleanup run before saving one compact skill, and distinguishes applied from pending. | A useful procedure, already within TeaPrompt's workflow-acquisition and artifact-promotion discipline. This survey did not invoke the upstream skill or prove a user workflow. |

The strongest counterargument is that a ready-made host with shared teams, triggers, and verification recipes is useful integration material. That is true as product reference, but it neither demonstrates a missing TeaPrompt method nor changes the standing non-goal. An existing-source worked example preserves the useful distinctions without importing runtime dependencies or approval defaults.

## Bounded Execution Receipt

The throwaway probe imported `shared/approval-mode.ts`, `server/auto-approve.ts`, `server/direct-apply.ts`, `server/routine-waits.ts`, and `electron/capabilities.cjs` from the exact checkout. It used `node --experimental-strip-types boundaries.mjs` inside a checked `sandbox-exec` profile, with a 30-second outer deadline. Original modules were used; no rewritten substitutes, model responses, package installation, or fake provider server.

| Case | Input / question | Observed result |
| --- | --- | --- |
| A1 | `approvalModeFor({})` | `full` |
| A2 | Stored mode `unknown` | `ask` |
| A3 | Stored `full` plus pending grant `{requestId: r1, mode: full, phase: prepared}` | `ask` |
| A4 | Set default to `ask`, resolve empty bot, then restore `full` | `ask`; this simulates startup configuration, not a hosted deployment |
| A5 | Broker: Ask + `Bash` | `approve: null`, `source: no-grant` |
| A6 | Broker: Full + `Bash`, `requiresExplicitApproval: true` | `source: full-access` |
| A7 | Broker: Ask + `mcp__composio__GMAIL_SEND_EMAIL` | `source: outbound-guard` |
| A8 | Same tool at Full | `source: full-access`; no email sent |
| A9 | Broker: Full + `AskUserQuestion` | `approve: null`, `source: no-grant` |
| A10 | Chief Full, different recipient Ask, `claudeAgent` driver | Delegated level `full` |
| A11 | Same inputs, sender not Chief | No delegated override (`null`) |
| D1 | `appliesNow({fullAccess: false, ownerMustConfirm: false})` | `level` |
| D2 | `fullAccess: true`, `ownerMustConfirm: true` | `null` |
| T1 | Started at 0; 20 minutes elapsed, 10 minutes previously waiting, open ask since minute 15 | 300,000 ms active, not 1,200,000 |
| T2 | Resolve that ask with matching request ID and `source: timeout` | Explicit nobody-answered stop reason; open ask removed |
| T3 | Active time after settlement | Still 300,000 ms; accumulated wait 900,000 ms |
| C1 | GNOME Wayland with an XWayland `DISPLAY` also set | `linux-wayland-seat-safety-blocked` |
| C2 | Hyprland identity, no active-plugin evidence | `linux-hyprland-plugin-required` |
| C3 | Same identity with synthetic `hyprlandPlugin: active` | Capability predicate `available: true`, not native-control proof |

**Result: 19/19 observations passed; process exit 0.** Seven separate host controls passed: scratch read/write allowed; a harmless real-home file read denied; a separate temporary canary read denied; source-checkout write denied; outside-scratch write denied; child-process outside write denied; loopback TCP connect denied with `EPERM`. These bound this smoke run; they are not an OpenMausBot sandbox test or a complete host-isolation certification.

Harness failures are retained: the first deny-default profile aborted Node/Bun startup with signal 6; a later overly broad read denial blocked Node's ancestor-directory `lstat` with `EPERM` before imports. The final profile allowed metadata lookup while denying protected file contents, writes outside scratch, and networking. Its controls passed before original upstream functions ran. No upstream failure is inferred from those harness errors.

The package parser depends on `zod`, `yaml`, and scheduling helpers; dependencies were not installed, so package import, redaction, filesystem rollback, and organization-channel behavior remain source-only. The complete upstream test/build suite was not run. Temporary probe inputs are disposable; this table internalizes the inputs, outputs, source identity, scope, and failures without depending on a temporary path.

## Local Gap Test

| Candidate lesson | Delivered TeaPrompt coverage | Decision |
| --- | --- | --- |
| Permission, product mutation, and acceptance are separate | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) §§2–4a; [Reflective Risk](../skills/reflective-risk/SKILL.md) authority, sink, and unattended-envelope rules | Existing contract; add only a worked reference outside the prompt fence |
| Imported instructions, memory, or package metadata cannot grant authority by themselves | Runtime Trust Boundary §3; [Artifact Promotion](../04-agent/artifact-promotion.md) §4; [Reflective Handoff/Retro](../skills/reflective-handoff-retro/SKILL.md) provenance and dated-lead discipline | Existing contract; upstream portability is an example, not permission to bypass the memory-write gate |
| Active-time/overlap controls do not prove effect safety | Runtime Trust Boundary §4a; Reflective Risk unknown-outcome and sink-contract rules | Existing contract; no scheduler or retry-policy adoption |
| A flag or successful helper check has a bounded evidentiary scope | [Reflective Review](../skills/reflective-review/SKILL.md) evidence dimensions, tiers, and claims ledger | Existing contract; source/pure-function observations stay distinct from deployed guarantees |
| Verify a real workflow before promoting a reusable recipe | [Workflow Acquisition](../04-agent/workflow-acquisition.md) replay, verifier, and minimum-artifact gates; Artifact Promotion §§4–5 | Existing contract; no new verification Skill |
| Run a desktop/server, VM, MCP catalog, or scheduling service | [Project Knowledge](../PROJECT_KNOWLEDGE.md) Standing Non-Goals | Product/runtime capability, not a missing prompt rule |

No reproduced local consumer defect or missing delivered Skill requirement was established. Local demand/recurrence remains `unknown`, not zero. External feature count and popularity are not promotion evidence.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| OMB-DOC1 | Source-qualified survey, catalogue entry, and discovery metadata | Adopted: reference documentation only | Owner requested Docs/Skills updates; refresh when the pinned source or cited distribution changes |
| OMB-DOC2 | Optional navigation from Runtime Trust Boundary to the worked example below | Adopted: navigation only | Existing rules become concrete without changing the prompt output contract |
| OMB-SK1 | New Skill or expanded existing Skill contract | No change | No verified local structural gap; reopen on a concrete failing local consumer |
| OMB-RUN1 | Install OpenMausBot, providers, computer drivers, packages, or schedules | Not adopted | Runtime non-goal; requires a separate host, purpose, authority, risk, and acceptance decision |
| OMB-RULE1 | Copy Full-by-default, automatic product application, or runtime status as TeaPrompt authorization/acceptance | Rejected | Conflicts with existing source-of-authority and acceptance distinctions; no such operating rule is adopted |

## Optional Worked Reference — Portability Does Not Carry Approval

This applies existing rules to the pinned upstream, not a new workflow or installation recommendation.

| Apparent assurance | What the checked evidence actually establishes | Existing TeaPrompt question |
| --- | --- | --- |
| “The imported package does not carry approval settings.” | The importer leaves approval unset; the recipient default can still be Full. Other settings, memory seeds, and team leadership do travel. | What authority does the receiving environment supply, and which writes happen on import? |
| “The bot is on Ask.” | Provider permissions and selected application mutations use different gates; direct application can return `level`. | Which exact action requires which principal and gate? Is Undo being mistaken for approval? |
| “The computer is isolated / network is loopback.” | Local VM allocation defaults shared; the inspected loopback status concerns viewer-port exposure, not proof of denied egress or isolated accounts. | Which resource, process, credential, network, and input boundary is actually enforced? |
| “A run limit and overlap protection are configured.” | Active-work accounting can exclude human waits; overlap rules bound scheduling, not downstream effect duplication. | What is the clock, stop mechanism, sink idempotency contract, and unknown-outcome path? |
| “The helper checks passed.” | Nineteen synthetic source-function observations passed without a live product. | What claim did the check exercise, and what remains unverified? |

## Falsifiability and Residual Risks

- A reproduced local failure against an existing TeaPrompt acceptance criterion could justify an in-place contract repair. This survey did not produce one.
- A later upstream revision may change defaults, import channels, question routing, or the known service-loopback gap. Re-pin and inspect the delta; do not silently apply a newer claim to this receipt.
- A real generic import resolving to Ask on an otherwise default non-hosted setup would require tracing additional configuration or caller behavior; the executed default function alone cannot exclude that possibility.
- Unknown here: end-to-end HTTP authentication coverage, native driver/VM confinement, enterprise implementation, cloud account policy, live model quality, external-effect cancellation/retry safety, import crash recovery, complete attachment cleanup, and privacy under adversarial content. Neither source inspection nor redaction patterns establish those guarantees.
- GNOME/Hyprland results are pure capability predicates, not compositor certification. Telemetry/storage/license findings are source-qualified, not observed outbound traffic or legal approval.
- No installation, model campaign, account operation, commit, or push is authorized by the record. A future deployment decision belongs to the owner and host operator, with current security, privacy, licensing, and rollback evidence.
