# Stop That Shit: Task Guardrails and Minimality Survey (2026-09-30)

> **Status: decided — record-only; no installed skill, routing, permission, dependency, or runtime change.** Unlike the preceding coordination skill, this source includes executable policy and host adapters. The offline hook scenarios below establish actual response/state behavior, not real-host containment or improved model behavior. A same-day correction run superseded the first offline run. Held or freshly abandoned session locks fail open without reservation or audit, consistent with upstream's documented shared fail-open convention although no upstream doc names this path; recognized prose can reopen change mode; unstated grants persist across task directives. A blocked audit append confirmed the documented best-effort audit. Eight STS-* candidates are decided below; the correction changes evidence and qualifications, not dispositions, and none is promoted into an operating surface.

## Research Question

User direction: continue the preceding survey with `https://github.com/lennney/stop-that-shit` (checked 2026-09-30).

What does this project actually control, how strong is its verification, and does any mechanism fill a verified gap in TeaPrompt? Keep the earlier eval survey's distinction between oracle write sealing, hidden-answer read isolation, and untouched final measurement; do not silently reopen RS-4, FM3, JL-9, pi-warden C12, or SF-C2/SF-2.

## Direct Recommendation

- Study the separation of task-authority policy, native-host translation, reservation accounting, and observed effects. It is executable guardrail code, not merely an anti-bloat prompt.
- Do not read `agents=N`, review mode, or the metadata audit as hard bounds at this pin. A held or freshly abandoned session lock makes the hook exit 0 with empty stdout (the allow shape) and record no reservation or event; recognized prose, including the negated `Fix nothing yet; just list the problems.`, reopened change mode; unstated grants persisted across a later task directive; and, as upstream documents, a blocked audit append was silent.
- Keep the Stop Ladder as corroboration of `reflective-minimality`, not a new workflow skill. A mechanism's omission must fail a named requirement; minimality must preserve the safety floor.
- Do not install this plugin or import its dependencies by default. No verified local host problem or project direction requires that change; local usage recurrence is **unknown**.
- Do not transfer the default hash prohibition as a general engineering rule. Required oracle-integrity hashing, authentication, and other security controls remain protected; the source itself supports explicit `hash=allow`.
- Record STSS's claim-preserving prose-editing method as an adjacent concept. Its specific rewrite/audit procedure is not claimed to be installed in TeaPrompt.

## Version / Date Context

All upstream observations below were checked **2026-09-30**, against an isolated detached checkout unless identified as release metadata or an author-reported historical result.

| Identity | Observed value | Boundary / tracking event |
| --- | --- | --- |
| Reviewed main commit | `749c921e988f1a6714500da4b1c140311684dbbb`, dated 2026-09-29 | Immutable research pin; recheck on the next adapter/policy change. |
| Package version | `0.2.4` | A version string is not the exact reviewed artifact. |
| Latest release/tag checked | `0.2.4`; annotated tag object `7762d2f6c67dd510ce0ee66140f664e4f28d5a6a` peels to `5f668ec10cd3d46b5108808ddd0c500777af6d1e` | Tag and reviewed main have different identities; no behavioral difference is inferred from identity alone. |
| License | MIT, checked in the pinned `LICENSE` | This survey summarizes mechanisms; it does not import source text or code into operational skills. |
| Manifest dependencies | `@opencode/schema` `2.0.18`, `effect` `4.0.0-rc.112`; dev dependency `ajv` `^8.20.0` | Dependencies were inspected, not installed; the Effect dependency is an RC. |
| Local execution runtime | Node `v25.1.0` | Offline core/Codex-hook paths only, not the installed host matrix. |

Release metadata: [release](https://github.com/lennney/stop-that-shit/releases/tag/0.2.4), [annotated tag object](https://api.github.com/repos/lennney/stop-that-shit/git/tags/7762d2f6c67dd510ce0ee66140f664e4f28d5a6a) (checked 2026-09-30). No registry artifact parity is claimed.

## Method and Evidence Actually Checked

- Read the pinned architecture, main skill, STSS writing skill, host contract, security/privacy statements, package manifest, and license. Two read-only scouts independently traced core guard/state and host/evidence slices; they did not build, install, test, or call providers.
- Traced `contracts.cjs`, `decision.cjs`, `controller.cjs`, `delegation-state.cjs`, `state.cjs`, `runtime-audit.cjs`, `runtime-storage.cjs`, the hook entrypoint, the Codex adapter/classifier, and OpenCode V1/V2 promotion code. Host-specific scope beyond the directly traced paths is source evidence, not local runtime proof.
- Ran the real `hooks/stop-that-shit.cjs` entrypoint as fresh Node subprocesses with synthetic stdin payloads in two runs at the same pin. The correction run supersedes the first, whose privacy check lacked a positive control and whose two-process check covered only successful lock acquisition. It adds positive audit controls, empty-stderr checks on every healthy response, natural-language authority, grant inheritance, held and abandoned session locks, and a blocked audit append. Lock holders called the pinned `src/state.cjs` `acquireSessionLock`; no upstream file was modified. Test shell strings remained data; no corresponding command, real delegated agent, or real host was launched.
- Ran `node scripts/evaluate-cases.cjs` against the pinned `cases/0.0.1/*.json` population. An independent glob enumerated the same 18 fixtures.
- Used macOS `sandbox-exec` under `env -i`: network denied, `/Users` reads denied, writes allowed only under the owned scratch root. The driver received only PATH plus scratch HOME/TMPDIR; hook children also received scratch `PLUGIN_DATA` and `STS_RUNTIME_DATA`, binding state and audit to one root. No ambient provider credentials were inherited. No global configuration or host plugin installation was changed.
- Compared checked repository contracts, not this research agent's own host instructions. Prior record corrections remain evidence clarifications, not new operational controls.
- Attributed upstream documentation from a sweep of all 41 Markdown files at the pin: root docs, `docs/agents/`, skills, cases, evals, `.hermes-plugin/`, and `.github/`. Narrow patterns covered lock timeout and stale takeover, fail-open, natural corrections, and field inheritance; they re-found the known fail-open and natural-correction passages as positive controls. This supersedes an earlier check of root docs and the main skill.

## What the Artifact Is

### Advisory methodology versus executable guard

The `stop-that-shit` skill's Stop Ladder asks what the task owns, which existing capability suffices, what concrete gap remains, whether a defense changes a real outcome, and when evidence is sufficient to stop. That is advisory reasoning; it does not establish model adherence or automatically prove business necessity.

Separately, five adapter families translate native events into `ControlEvent v2`. A shared controller evaluates normalized tool facts against a session contract and returns context or a denial. It stores schema-4 task state, correlates supported delegation facts, and appends `RuntimeEvent v1` metadata. The host still owns hook trust, execution, native permissions, process lifecycle, and final postconditions.

### Arming and authority

- Fresh state is `mode=unconfirmed`, `level=watch`, unlimited agent budget, unbounded file paths, `hash=deny`, `deps=ask`. Unconfirmed mode does not enforce those policy fields.
- A recognized task-mode directive without an explicit level moves watch to guard. Explicit watch stays advisory only until a recognized natural correction arrives, which also moves watch to guard (observed). The docs say `watch` always observes without blocking (`README_EN.md` lines 332-334) and do not mention this exit. Guard/lock can return denial; off bypasses the decision path.
- Formal directive fields belong on the first non-empty directive line, before its task separator; quoted, fenced, and example text does not become authorization (observed for a fenced directive and a quoted sentence).
- Natural-language corrections are a second authority path in the shared core, not an OpenCode-only feature. Review-only, answer-only, and monitor-only phrases arm guard; a leading `fix|implement|change|apply|patch` verb (optionally after `please`), or a listed Chinese edit verb, moves answer/review/monitor to change. Upstream documents that the prompt hook reads natural explicit corrections (`INSTALL.md` lines 26-27) and that a direct review request selects review (`HOST-ADAPTER-CONTRACT.md` lines 123-127); no doc enumerates the leading-verb change rule, which `test/contracts.test.cjs` covers. The match is lexical: `Fix nothing yet; just list the problems.` reopened change, and the next Write received no deny.
- Grants are session-scoped, not task-scoped: fields a later directive or correction does not restate are inherited. After `change hash=allow deps=allow files=src/** agents=1`, a `review -- inspect another task` directive plus `Fix the bug.` kept all four grants, and a hashing write received no deny. Explicit `hash=deny` / `deps=deny` revoked them. The docs say an invalid directive keeps the previous contract (`INSTALL.md` lines 104-105) but do not state that a valid directive inherits omitted grants. The nearest line, `CHANGELOG.md` 0.2.1 #34 (omitting `files` "preserves the existing behavior"), does not say which boundary is preserved.
- A native permission grant is not task authorization. Conversely, no STS denial is not a native permission grant.
- **OpenCode exception:** eligible root user messages under an edit-capable agent can additionally promote review to change without any STS directive or recognized correction. V1 treats unknown named-agent capabilities as edit-capable; V2 consults the applicable edit permission. Other contract settings remain. Neither this host policy nor the shared-core prefix rule is a model for TeaPrompt's diagnostic-not-authorization rule.

### Reservation accounting, not orchestration

Before an admitted delegation action, the controller reserves capacity under a session lock shared with prompt/completion updates. It deduplicates action IDs and distinguishes pending units, bound children, unresolved activity, and supported terminal facts. Unknown results retain capacity; a session-end notification alone does not release it.

Codex UUID spawn/terminal-wait facts can release capacity. Named-task/mailbox responses lack the completion identity this adapter requires, so finite capacity can remain occupied. STS does not schedule, cancel, or terminate workers; a returned tool result or mailbox message cannot substitute for a supported terminal fact.

The session lock bounds that accounting. `acquireSessionLock` waits 1500 ms and treats a lock older than 10 s as stale; the hook entrypoint catches the timeout and exits 0 with only a stderr diagnostic, leaving stdout in the same empty shape as an allow. With the pinned lock function holding the session, an `agents=0` spawn failed open after 1542 ms with no reservation or audit event, and a concurrent `Review only. Do not edit anything.` was dropped. A lock left by an exited process caused the same fail-open (1554 ms) until its mtime was aged past 10 s; the next spawn then removed it, reserved one unit, and the following spawn was denied. `ARCHITECTURE.md` (lines 42-44) says the lock keeps concurrent Hook processes from oversubscribing the active agent limit; a timed-out process does not oversubscribe the ledger, but it neither reserves nor denies. This fail-open is consistent with the shared fail-open convention in `HOST-ADAPTER-CONTRACT.md` (line 452); none of the 41 Markdown files names lock-acquisition timeout or stale-lock takeover. What a host does after the empty response was not observed.

### Privacy and failure posture

Runtime audit stores bounded metadata, not raw prompts, commands, file paths, code, outputs, or raw session IDs. `hostEffect` is always `unobserved`. Session state is different: it can retain `files=` strings, delegation IDs/aliases, directive-error tokens, and generated contract context; inspect it before sharing. `ARCHITECTURE.md` (lines 162-163) documents that audit write failures fail open without changing the decision. The blocked-directory probe confirmed that posture: a deny was still returned, stderr stayed empty, and no event was written. A missing event is not evidence that no hook ran or no decision was returned.

The runtime's privacy statement reports no automatic network/telemetry. A manually invoked `sts doctor --check-update` requests public GitHub release metadata; this was not invoked. Host/model-provider data handling remains separate. The native hook catches errors and fails open; malformed JSON and held or abandoned session locks demonstrated that posture locally.

## Host Coverage and Material Limits

These are **pinned source bounds checked 2026-09-30**, not five installed-host runs in this survey.

| Host family | Implemented surface | Material limit |
| --- | --- | --- |
| Codex | Prompt, pre-tool, selected spawn/wait post-tool, session-end hooks | Approval requirements map to deny; named-task/mailbox completion is unsupported by the UUID correlation path. |
| Claude Code | Plugin hooks with subagent/tool lifecycle translation | Stop attempts are not terminal evidence; unsupported background completion retains capacity; unbounded Workflow and finite-limit unversioned resumes are denied. |
| OpenCode | Native V1 and V2 adapters | Implicit review-to-change promotion; finite-limit continuations lack run identity; direct Code Mode JS/network effects are not fully covered. |
| Hermes Agent CLI | Native Python plugin calling bundled Node runtime | Declared CLI-dispatcher scope, not all Gateway/cron/ACP/Desktop paths; wrapper timeout/errors fail open. |
| Pi | In-process extension tool/input/result hooks | Separate child Pi processes do not have proven parent-contract inheritance; direct user `!`/`!!` commands bypass tool-call hooks; unproven background results retain capacity. |

Installation is an executable-host change, not loading a harmless text pack. Codex hook trust, host-owned persisted data, OpenCode configuration/cache changes, and Pi's full-process access need a named host/version review. Installation, uninstall ownership receipts, and host-package parity were not exercised here.

## Verification Evidence: Three Different Bars

### 1. Local offline behavior — observed in this survey

Correction-run invocation: `env -i PATH=… HOME=<scratch>/home TMPDIR=<scratch>/ sandbox-exec -p <profile> node <scratch>/smoke.cjs <pinned-checkout> <scratch>`; parent exit **0**, and every healthy hook response had empty stderr. The disposable driver invoked the published evaluator and native hook, asserted the outcomes below, and was removed afterward. The first run's overlapping rows reproduced; its table is superseded.

Reproduction inputs (angle brackets are owned, canonicalized scratch paths; one JSON object per hook process):

```text
profile    (version 1) (allow default) (deny network*) (deny file-write*)
           (allow file-write* (subpath "<scratch>"))
           (deny file-read* (subpath "/Users")) (deny file-read* (subpath "/private/Users"))
driver     PATH=/opt/homebrew/bin:/usr/bin:/bin HOME=<scratch>/home TMPDIR=<scratch>/
hook       driver env + PLUGIN_DATA=<run>/data STS_RUNTIME_DATA=<run>/data; cwd <run>/workspace
prompt     {"session_id":S,"turn_id":"turn-1","hook_event_name":"UserPromptSubmit","cwd":W,"prompt":P}
pre        {...,"hook_event_name":"PreToolUse","tool_name":T,"tool_input":I,"tool_use_id":ID}
post       {...,"hook_event_name":"PostToolUse","tool_name":T,"tool_input":I,"tool_response":R,"tool_use_id":ID}
end        {...,"hook_event_name":"SessionEnd"}
inputs     Write {"file_path":F,"content":C}; Bash {"command":X}
UUID       spawn R {"agent_id":U}; wait I {"targets":[U]}, R {"timed_out":false,"status":{U:{"completed":"done"}}}
mailbox    spawn I {"task_name":"scout","message":M}, R {"task_name":"scout"}; wait R {"message":"finished","timed_out":false}
held       driver calls <checkout>/src/state.cjs acquireSessionLock(S, <run>/data) around two hook runs
abandoned  node -e "require(<state.cjs>).acquireSessionLock(S, <run>/data)" exits; later utimes(lock, now - 11 s)
blocked    <gap>/runtime is a regular file; PLUGIN_DATA=STS_RUNTIME_DATA=<gap>
```

Published evaluator result: **18/18 paired-case arms passed**. Input set: all 18 JSON files under pinned `cases/0.0.1`; these are deterministic decision fixtures, not model A/B results.

| Native scenario / input | Observed response or postcondition |
| --- | --- |
| Fresh session + Write; neutral `Summarize the repository layout.` + Write | No deny; mode stays `unconfirmed`. |
| `$stop-that-shit watch review` + Write, then `Review only. Do not edit anything.` + Write | First Write: context with `MODE_FORBIDS_MUTATION`, no deny. After the prose: level `guard`, Write denied. |
| `$stop-that-shit review` + Write / Read | Mode-only directive arms guard; Write returns `permissionDecision=deny`, Read returns no deny. |
| Review + fenced change directive and `Fix the bug.`, then a quoted `"Fix the bug"` sentence | Mode stays review; the next Write is denied. |
| Review + `rg --hostname-bin=...` supplied as Bash data | `MUTABILITY_UNPROVEN` deny; no command executed. |
| `Review only. Do not edit anything.` → `Fix the bug.`; `只看不改。` → `修改 src/config.cjs。`; `Review only.` → `Fix nothing yet; just list the problems.` | Each review phrase armed guard; each later sentence set `change`, and the next Write received no deny. |
| `change` without grants + hashing-code Write / `npm install example-package` | `HASH_NOT_AUTHORIZED` / `DEPENDENCY_NOT_AUTHORIZED`. |
| `change hash=allow deps=allow files=src/** agents=1` → `review -- inspect another task` → `Fix the bug.` | State kept all four grants; hashing Write no deny; README Write `PATH_OUTSIDE_CONTRACT`; install without a proven write path `WRITE_PATH_UNPROVEN` (path boundary precedes dependency policy); after `hash=deny deps=deny`, the hashing Write was denied. |
| `change deps=allow` → review directive → `Fix the bug.` + install; then `deps=deny` | Inherited grant: no deny. After revocation: `DEPENDENCY_NOT_AUTHORIZED`. |
| `change files=src/**` + inside / README / existing `src/linked/file.cjs` whose parent symlink points to scratch `outside/` | Inside no deny; README `PATH_OUTSIDE_CONTRACT`; symlinked path no deny although its realpath is outside `src`. The target stayed untouched; no host write was executed. |
| `lock change files=src/config.cjs` + inside / README | Inside no deny; README `PATH_OUTSIDE_CONTRACT`. |
| `change agents=1` + UUID spawn result, second spawn, SessionEnd, correlated terminal wait, next spawn | Second spawn denied; session end retains one unit; terminal wait releases it; the next spawn is admitted and reserves one unit. |
| Same finite contract + `{task_name}` spawn and `{message, timed_out:false}` wait | One unit retained; next spawn denied. No real agent launched. |
| Two concurrent hook processes, distinct spawn IDs, one `agents=1` session, lock free | One admitted, one `AGENT_BUDGET_EXHAUSTED`; one unit reserved. Healthy lock path only; not a stress test. |
| `agents=0`; driver holds the session lock during a spawn and a `Review only. Do not edit anything.` prompt | Both exit 0 with empty stdout and stderr `Stop That Shit hook failed open: Error` (1542 / 1569 ms); no reservation, no audit event, mode stays `change`. After release: `AGENT_BUDGET_EXHAUSTED`, and the correction applies. |
| `agents=1`; lock left by an exited process, then its mtime aged 11 s | Fresh lock: the same fail-open (1554 ms), no reservation or event. Aged lock: removed; spawn admitted with one unit; next spawn denied. |
| Private session/path/content/command markers with a positive audit control | The marked session wrote its expected 2 events (`PATH_OUTSIDE_CONTRACT`, `WITHIN_CONTRACT`) at the hashed event path; 35 events were read across the run at that point; no marker appeared in audit; state retained the `files=` marker; every `hostEffect` was `unobserved`; a wrong data root returned 0 events. |
| Runtime directory replaced by a regular file; review + Write | Deny returned; empty stderr; no event; blocker unchanged. Confirms the documented audit fail-open. |
| Malformed stdin `{` | Exit 0, empty stdout, diagnostic `Stop That Shit hook failed open: SyntaxError`. |

The path probe establishes **lexical filtering, not canonical-root containment**; the lock probes establish that contention skips reservation and audit at the hook boundary. Neither claims an undisclosed real-host exploit; the source already identifies the guard as not a security sandbox. Second-method checks: an independent glob recounted 18 fixture files, and `wc -l` over the run's audit files counted 39 rows — the 35 read at the check plus 2 rows each under the `timeout` and `abandoned` session keys, which were written afterwards.

### 2. Installed-host postconditions — upstream-reported, not repeated here

`EVIDENCE.md` reports packing the candidate with lifecycle scripts disabled, installing into disposable workspaces, and running actual OpenCode **1.18.18 / 2.0.18** CLI processes with deterministic local model responses: review denied a native write and the target stayed absent; a read then succeeded; a fresh process resumed the session under explicit change and wrote the expected file. This is stronger than mocked unit coverage, but covers those installed-host paths, not model effectiveness, Code Mode, or child lifecycle.

The same document reports **428 tests passed, 3 optional host checks skipped**, plus a **205-file** release allowlist check. Those counts were read as author reports, not run or independently recounted here.

### 3. Model improvement — not established

The author-reported four-cell Intent pilot had two unchanged pairs and no improvement; its source was dirty and diagnostic. Three single-seed HERO-derived pairs also reported null effect plus necessary-work non-regression because baseline already behaved correctly. A runtime diagnostic excluded plugin cells due to stale cache; a synthetic community scenario was not reproduced and excluded from efficacy counts.

The documented **144-session** default matrix had not been run/published at this pin. A green fixture evaluator, a RuntimeEvent, a denial count, or a generated plan cannot supply the missing model comparison. No provider/model benchmark was performed in this survey.

## Concept Map and Candidate Adoption Ledger

Coverage below names the **checked repository delivery**. It does not imply a standalone skill imports every repository lens or provides the source's runtime behavior.

| ID | Candidate / classification | Decision | Checked local coverage or missing guarantee | Falsifier / reopen condition |
| --- | --- | --- | --- | --- |
| STS-1 | Stop Ladder; Already Present | No change | `reflective-minimality` §Minimality Ladder and §Safety Floor: existing capability first, named invariant, preserve required protection. | A local case demonstrates those clauses permit unnecessary structure; repair the existing contract first. |
| STS-2 | Explicit review/change and scope authority; Already Present at policy level | No change | `reflective-implement` §Module Contract forbids diagnostic-as-edit authorization and scope expansion; runtime enforcement still belongs to a host. Importing the observed lexical prefix promotion or session-scoped grants would weaken that rule. | A checked installed delivery loses that authority rule; neither OpenCode implicit promotion nor the shared-core imperative-prefix rule is imported as a substitute. |
| STS-3 | Default anti-hash rule; mechanism-specific, not a general principle | Reject blanket transfer | `reflective-minimality` §Safety Floor protects security and explicit requirements; `reflective-implement` protects authoritative oracles. SF-C2/SF-2 oracle hashing/write sealing stays compatible with separately needed read isolation. | A measured local unnecessary-hashing defect may justify a narrow existing-contract repair; never remove required integrity/security hashing to satisfy it. |
| STS-4 | Locked reservation ledger and versioned lifecycle; Host Boundary | No change | `runtime-trust-boundary` §§2a/4a distinguish run identity, terminal truth, unknown outcomes, and execution from acceptance; this text is not a reservation implementation. `reflective-implement` §Module Contract already limits catch-all fallbacks to documented external boundaries that preserve failure evidence and are tested on both paths. | Named host integration requirements plus supported terminal facts and actual concurrency/recovery proof, including held/abandoned-lock outcomes that do not reuse the empty allow shape; project-direction/admission review if a new runtime surface is proposed. |
| STS-5 | Metadata runtime audit; Host Boundary | No change | `reflective-research` §State Ledger scopes evidence; `runtime-trust-boundary` §§2a/4a separate record classes and sink postconditions. No metadata recorder is supplied by those prompts. | Named host need with a privacy/retention/ownership contract, visible append failures, and effect observations independent of returned responses. |
| STS-6 | Null-result reporting, Bad/Good acceptance, cache provenance; Already Present / specimen | No change | `reflective-research` §External Adoption Checks and §State Ledger; `reflective-implement` §Verification requires actual output and unchanged source/input/config for verification reuse. | A reproducible local reporting/cache defect bypasses those clauses; repair at its owning surface, not by adding a second verifier. |
| STS-7 | STSS claim-preserving decision-facing prose cleanup; Adjacent | Concept-only, not installed | Minimality's instruction/prose cuts and research's evidence qualifiers are adjacent, not the full DROP/CALIBRATE/RELOCATE/KEEP writing procedure. STSS is not an AI-authorship detector or general humanizer. | Repeated local claim/uncertainty loss in decision-facing edits establishes a concrete gap; assess an existing lens before a dedicated skill. |
| STS-8 | Five-host plugin distribution/integration; Host Boundary | No change / no installation | `PROJECT_KNOWLEDGE.md` §Standing Non-Goals; `artifact-promotion` §Promotion Gates requires named enforcement ownership and runtime proof. | Explicit named-host pilot direction, reviewed executable hooks/dependencies, tested bypass/fail-open/cleanup boundaries, and a useful baseline/treatment comparison. |

**Recommended Core Additions: none.** No local recurrence count is invented. A useful external implementation is evidence to inspect, not authority to add a tenth core skill, unregistered pack, telemetry recorder, or side-effect enforcer.

## Evidence vs Inference / Final State Ledger

| Claim | Status | Attester / method, checked 2026-09-30 | Scope remaining |
| --- | --- | --- | --- |
| Exact pin, release identity, manifest, MIT license | verified | Upstream GitHub metadata plus pinned file bytes | Registry parity not checked; next upstream change invalidates latest-version assertions. |
| Executable policy, five adapter families, arming, lexical path decisions, lifecycle/state/audit mechanics | verified | Pinned source traces and read-only scout reports | Adapter existence/code paths, not all installed hosts. |
| Published 18-case evaluator and correction-run native hook/state observations above | verified | Parent-run isolated program output and scratch postconditions; second-method recounts of fixtures (18) and audit rows (39) | Deterministic payloads; no actual tool/agent/model effects. The first run's table is superseded. |
| OpenCode installed-host smoke and historical pilot numbers are reported as described | verified | Maintainer's pinned EVIDENCE.md | Existence/text/attribution checked; underlying runs not replicated. Generalization unknown. |
| This guard reliably prevents all out-of-scope effects | refuted | SECURITY.md; source bypasses/fail-open; native lexical/symlink, held/abandoned-lock, and malformed-input probes | Guardrail cannot be represented as a sandbox or complete effect authority. |
| Only explicit `$stop-that-shit` directives change task authority, and grants end with their task | refuted | `contracts.cjs` correction and field-inheritance paths; native prose and grant probes | Lexical classifier: untested sentences and hosts unknown. |
| Runtime audit is a complete record of hook runs and returned denials | refuted | `runtime-audit.cjs` swallowed append errors; blocked-append and lock-timeout probes; `ARCHITECTURE.md` audit fail-open statement | A missing event is not absence evidence; host effects remain unobserved. |
| This pin improves general coding-agent outcomes | unknown | No sufficient published matrix or fresh comparison | Small author pilots do not establish benefit; installation remains unapproved/unperformed. |
| New TeaPrompt operating surface is warranted | needs-qualification | Candidate ledger and checked local contracts | No verified local gap for promotion; host guarantees are not claimed already implemented by prompts. |

**[INFERENCE] Adoption judgement:** existing methodology covers the transferable minimality/authority/evidence obligations; the executable extras are host integrations. A record-only outcome is sufficient without settling general model efficacy. The strongest counterargument is that runtime hooks can constrain behavior where prose cannot; accepted, but it argues for a named host integration and proof, not for relabeling TeaPrompt as an enforcer.

Observed perspectives: complete-but-minimal delivery, task authority, heterogeneous host lifecycle, and privacy-conscious measurement. Blind spots: reliable real-host effect containment on untested paths, child/run identity across hosts, model benefit, and local usage recurrence. Every one is kept separate from source/fixture proof.

## Falsifiability

The STS-1–STS-8 ledger names the evidence that would overturn each disposition. A reproducible local gap in the checked delivery can reopen an in-place repair; explicit host direction and runtime proof can reopen an integration. General model benefit remains unknown until a clean, version-bound comparison demonstrates task improvement without sacrificing necessary-work acceptance. Self-tests, denial counts, or source popularity do not satisfy those conditions. Later revisions require fresh checks; they do not retroactively change the observations at this pin.

## Continuity, Risks, and Handoff

- The preceding [eval/coordination record](coordinate-codex-tasks-eval-survey-2026-09-30.md) now qualifies author-local/UTC timestamps, separates write sealing from read isolation/final measurement, and preserves the exact synthetic selection seeds/probe construction. This survey adds no hidden-eval or judge benchmark.
- [RS-4](rsiagent-survey-2026-09-16.md), [FM3](fable-method-survey-2026-07-16.md), [JL-9](llm-judge-lifecycle-survey-2026-09-05.md), [pi-warden C12](pi-warden-survey-2026-09-20.md), and [SF-C2/SF-2](software-factory-sdlc-inner-outer-loop-survey-2026-09-28.md) keep their recorded boundaries. A new source's reservation smoke is not a trigger for unrelated loop, private-fixture, judge, or timed-wake adoption.
- Do not equate watch context or returned denial with blocked execution. An independent sink postcondition is required. A finite reservation limit also needs supported terminal/run identity to remain usable, and it holds only while the session lock is acquired: contention or a fresh abandoned lock fails open.
- Preserve necessary work: conservative classification, hash/dependency rules, or a hook failure can interrupt valid work or leave an action unconstrained. Host-native permissions and security containment must remain separate and sufficient.
- No upstream fixes, dependency installs, live provider calls, global configuration changes, or plugin installation are part of this delivery. Disposable source/scenario directories are removed after recording observations.
- All eight candidates have a disposition and falsifier. A later pilot must name host/version, task acceptance, necessary-work controls, data/permission ownership, bounded cost, final effects, and a comparison before adoption. That is a reopening condition, not unfinished work in this survey.

## Repository Guards and Completion

The existing record-hygiene, link, project-knowledge, and generated-index guards cover this archive; no source-text/wording-pin test or runtime code is added. `generate_index.py` refreshes the discovery artifact; `make all` is the repository consistency gate. These checks do not establish source truth, agent adherence, or runtime safety. The final invocation and result are reported in the delivery report.

Traceability: version/license → Version / Date Context; actual execution → local offline table; source versus efficacy → three verification bars; local fit → STS-1–STS-8; preserved decisions and risk → Continuity / Handoff. No human approval is required for this record-only closure; any future permission/runtime adoption retains its existing Human Review boundary.

## Evidence Used

All primary links below were checked **2026-09-30** against the immutable research pin. Historical results remain upstream-attributed.

- [Architecture](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/ARCHITECTURE.md), [Stop Ladder skill](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/skills/stop-that-shit/SKILL.md), [STSS skill](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/skills/stss/SKILL.md) (checked 2026-09-30).
- [Host adapter contract](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/HOST-ADAPTER-CONTRACT.md), [decision core](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/src/decision.cjs), [controller](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/src/controller.cjs), [Codex adapter](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/src/adapters/codex-hooks.cjs) (checked 2026-09-30).
- [OpenCode V1](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/opencode/stop-that-shit.mjs), [OpenCode V2](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/opencode/v2.mjs), [Privacy](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/PRIVACY.md), [Security](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/SECURITY.md) (checked 2026-09-30).
- [Evidence](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/EVIDENCE.md), [fixture evaluator](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/scripts/evaluate-cases.cjs), [manifest](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/package.json), [license](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/LICENSE) (checked 2026-09-30).
- [Contract parser](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/src/contracts.cjs), [session state and lock](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/src/state.cjs), [runtime audit](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/src/runtime-audit.cjs), [runtime storage](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/src/runtime-storage.cjs), [hook entrypoint](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/hooks/stop-that-shit.cjs), [contract tests](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/test/contracts.test.cjs) (checked 2026-09-30).
- [Install guide](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/INSTALL.md), [English README](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/README_EN.md), [changelog](https://github.com/lennney/stop-that-shit/blob/749c921e988f1a6714500da4b1c140311684dbbb/CHANGELOG.md) (checked 2026-09-30).
