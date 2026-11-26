# WGS-X4b No-Op Hunt — Preregistered Plan (2026-11-26)

Language: English
> **Status:** interrupted, partial diagnostic evidence (`X4B-RUN1`); the 144-job pilot is not complete. Drafted 2026-11-26 as plan only (`X4B-PLAN1`); the owner's third-round answer ("2. ok, 你自己決定") authorized the pilot and delegated caps, families and unit selection. The fixed configuration and qualification amendments below are retained. A 3,600-second host deadline interrupted execution; current no-tool qualification is unverified. No further provider call, unit deletion, permission widening, commit or push is authorized by this record.

## Question

Which units of the nine core skills change agent behavior on a task that exercises them, and which show no observable effect on any tested model family? A no-op verdict is model-relative ([A8](skill-improvement-plan-2026-07-24.md)) and fixture-relative. The hunt can nominate a deletion; it never deletes.

## Relation to Existing Work

- [WGS-X4b](skill-improvement-plan-2026-07-24.md): evidence gate ruled fired on 2026-11-26 ([SCR-P3](skills-survey-corpus-rethink-2026-11-26.md)); this plan is its next step.
- [DF-C2](fresh-dogfood-campaign-preregistration-2026-10-14.md) and [DF-PB1](procedural-blind-dogfood-preregistration-2026-10-15.md) measure whole-skill effects for `reflective-implement`, `reflective-review` and `reflective-handoff-retro`. Both are held. Neither measures single units, so this plan does not wait on them and does not reuse their pools.
- [P6](skills-survey-corpus-rethink-2026-11-26.md#owner-decisions-and-landing-2026-11-26) and [T1](skills-survey-corpus-rethink-2026-11-26.md#t1-results) are small prototypes of this method on host subagents only. P6 tied 3/3 versus 3/3 because a single-focus fixture let both arms pass. T1 tied on two trims and lost the third to a rubric clause that failed every run in both arms.

## Units and Selection Rule

A unit is one bullet, one numbered step, or one obligation-carrying sentence in a core skill's Module Contract, workflow steps, rules, `Never` list, or verification section. Frontmatter, headings, example pointers and Prompt Sources are out of scope.

The pilot covers twelve units, frozen in a manifest before the first run and reviewed by the owner:

1. Four units whose adoption record cites external evidence only, with no recorded local incident.
2. Four units from the three longest core skills (`reflective-spec-plan`, `reflective-implement`, `reflective-research`).
3. Four units with a recorded reader concern, such as a positive duty inside a prohibition list.

Units pinned by guard tests stay eligible; a later deletion would update those pins in the same change.

## Arms and Fixtures

- **C:** the full skill. **T:** the skill with the unit deleted byte-exactly, with no rewording.
- One synthetic fixture per unit. Each fixture places the unit's behavior inside a multi-part task so the behavior is one detail among several, because P6 showed that a single-focus fixture saturates both arms.
- Fixtures, rubrics and both contract copies are hashed and frozen before any run and live outside the repository during runs.

## Substrate (owner permission, 2026-11-26)

The owner wrote "若要做實驗可以呼叫本機的 agent cli 像 cursor-agent or agy 這種的". Inventory checked 2026-11-26 with no inference: `cursor-agent` 2026.11.22-e9042b2 lists GPT-5.3 Codex, Composer, Claude, Grok and GPT-5.6 models; `agy` 1.5.17 lists Gemini 4, Gemini 3.8, Claude and GPT-OSS models.

- Use at least two model families other than the host's, for example one GPT-5.3 Codex model through `cursor-agent` and one Gemini 4 model through `agy`. Host subagents may form a third family. Prefer models without a "NO ZDR" marking.
- Every invocation follows [`headless-agent-cli-contract`](../skills/headless-agent-cli-contract/SKILL.md): a recipe per CLI and mode, then one qualifying canary per recipe before trial runs.
- Read-only units run in each CLI's plan mode. Units that need writes run only in disposable fixture copies and only under a permission configuration the owner approves. `--force`, `--yolo` and `--dangerously-skip-permissions` stay unused without that approval. A blocked recipe drops its family; it never widens permissions.
- Receipts keep stdout and stderr separately and retain raw output; the strip list removes known side-channels such as `cursor-agent` stderr `claude-mem` lines.

## Measurement and Decision Rules

Fixed before any run:

- Three runs per arm, per family, per unit in the pilot. Outputs are scored with arm labels stripped, using the `arm-blinded-eval-harness` scaffold and a rubric frozen per unit.
- Before freezing, each rubric is applied to two hand-written outputs, one that should pass and one that should fail; a clause that fails the passing output is rewritten before any run. T1-B showed that one miswritten clause can fail every run in both arms.
- **Load-bearing:** in any family, C passes at least two more runs than T.
- **No-op candidate:** in every tested family, T passes at least as many runs as C and at least two of three.
- **Inconclusive:** every other outcome.
- A no-op candidate becomes a deletion proposal only. Deletion needs a per-unit owner approval, lands with its pin updates and a record row, and never rests on one family.
- Stop after the twelve-unit pilot and report. If every non-host recipe is blocked, report `BLOCKED` rather than substituting host-only results.

## Proposed Budget

The owner sets the final caps; these are proposals.

| Item | Runs | Cost basis |
| --- | --- | --- |
| Qualification canaries | ≤ 4 | Owner's Cursor and Antigravity plan quotas |
| Pilot on two CLI families | 12 units × 2 arms × 3 runs × 2 families = 144 | Same quotas; a reported quota exhaustion stops that family, with no API key or overage |
| Optional host-subagent family | 72 | Host session usage |

Wall-clock time and per-run quota draw are unknown until qualification.

## Pilot Configuration (2026-11-26)

Fixed by the coordinator under the owner's delegation, before the first model call. The manifest, fixtures, scorers, contract copies, prompts and receipts live in a session-private directory outside the repository; this section pins them by hash.

- **Manifest:** `manifest.json` sha256 `8844de3597db405a3343cdbacbe6d322d6b048d774dd0076ab98288b30508eea`. It pins each unit's text, both contract copies, both prompts, the scorer, the shared wrapper and the `arm-blinded-eval-harness` scaffold, extracted byte-for-byte from that skill's `TEMPLATES.md`.
- **Families:** `cursor-agent` with `grok-4.7-medium` in `--mode ask` (read-only) with `--sandbox enabled`, and `agy` with `gemini-4-hydrogen-medium` in `--mode plan`. No host-subagent family. Qualification below changed both recipes before the first pilot job.
- **Caps:** at most 5 qualification canaries (raised from 4; see Qualification) and 144 valid pilot jobs. An invalid job is rerun at most twice. A family stops after 18 invalid jobs or at the first quota or rate-limit refusal. No API key, overage or paid add-on.
- **Prompt:** one message holding a fixed wrapper (answer from this message alone, no tools), the contract copy, the task and its materials. The two arms differ only by the deleted unit bytes.
- **Validity:** a job counts only if the CLI exits 0, its stream ends with a successful result, non-empty final text and zero tool events, and its fresh workspace stays empty. For `agy`, the stored conversation must also show the `<PLAN>` block that plan mode injects. Invalid jobs are reported per arm; a unit-family cell whose arms differ by two or more invalid jobs is inconclusive.
- **Isolation (configuration-time intent, not an enforcement result):** a fresh empty workspace per job; `ORCA_*` and provider API-key variables removed from the child environment; `CLAUDE_MEM_INTERNAL=1`; no `--force`, `--yolo` or `--dangerously-skip-permissions`. User rules, skill lists and CLI-side state were not isolated. Shared instructions may interact with the ablation or saturate both arms; receiving similar context does not establish independence or cancel that confound. The inspected canaries establish only their own context, not all subsequent jobs.
- **Order:** each family runs its 72 jobs in a seeded shuffle (seed `x4b-2026-11-26`), so arms interleave in time.
- **Scoring:** one deterministic scorer per unit, frozen in the manifest and run through the scaffold with arm labels stripped. Calibration on 2026-11-26: all 24 hand-written samples scored as intended (each pass sample passed, each fail sample failed), and no arm token appeared in scorer output.
- **Scorer check:** if all twelve verdicts for a unit are identical, the coordinator checks the scorer blind on two outputs before unblinding. If the scorer misjudges them, the unit is inconclusive (rubric defect) and is never rescored for a verdict.
- **Qualification history (2026-11-26, before any pilot job):** Canary 1 (`cursor-agent`, `gpt-5.3-codex`) stopped at workspace trust before inference. `--trust` was then added for the runner-created empty directory. Canary 2 (`agy` with `--disable-slash-commands`) answered, but warned that the flag disables `--mode plan`, so it was dropped. Canary 3 refused Codex 5.3 as not included in weekly usage and suggested buying credits or switching to Grok; Codex stopped and no credits were bought. Canary 4 (`agy`, final recipe) exited 0 with a successful result and zero observed tool steps; its stored conversation contains `/plan`, unlike canary 2. Both reported `permission_mode: proceed-in-sandbox`; that field does not identify plan mode. Canary 5 (`cursor-agent`, `grok-4.7-medium`) succeeded with zero observed tool events. The coordinator raised the canary cap from 4 to 5 and switched the model before pilot dispatch. Those calls are not scored; the model-population and qualification changes nevertheless remain protocol amendments. **Resumption correction:** these receipts establish transport and observed behavior, not a verified no-tool configuration. The current [headless contract](../skills/headless-agent-cli-contract/SKILL.md) does not accept a no-tools prompt, workspace trust, or one tool-free answer as that boundary.
- **Shared context observed in the inspected canaries:** `agy` injected `~/.gemini/GEMINI.md` as user rules (the `cx` requirement, Why → What → How → Done, Steelman and Falsifiability), a 46,067-character skill list and, with the final recipe, a plan-mode block. `cursor-agent` injected four user rules, including "Act as a Reflective Engineering Agent" and "Acceptance Criteria & Falsifiability", a Postman block, a 20,944-character skill list naming all nine reflective skills, and a claude-mem status notice. No earlier-session memory content was identified in those inspected canaries. That is not a cohort-wide absence finding or proof that `CLAUDE_MEM_INTERNAL=1` disables every hook. U08/U10 overlap this background guidance; retained skill clauses can also carry the deleted obligation.

| Unit | Selection class | Skill | Unit deleted in T | Origin |
| --- | --- | --- | --- | --- |
| U01 | External evidence only | `reflective-spec-plan` | Spec-silence sentence feeding a bounded Review Focus | SP-1 (Superpowers v6.4.2), 2026-10-03 |
| U02 | External evidence only | `reflective-review` | `Never` bullet sending declined behaviors to `Declined to Judge` | SP-2 (Superpowers v6.4.2), 2026-10-03 |
| U03 | External evidence only | `reflective-handoff-retro` | `## Friction Notes` template line | SUR-ED2 (Uber papercuts), 2026-11-25 |
| U04 | External evidence only | `reflective-review` | `Number / text` row of the evidence-dimension table | SUR-ED1 wording (official cookbooks), 2026-11-25 |
| U05 | Longest skills | `reflective-implement` | Twin-sweep bullet | FM1, 2026-07-16 (local reproduction) |
| U06 | Longest skills | `reflective-implement` | Consumer-map bullet | MC-5, 2026-09-19 |
| U07 | Longest skills | `reflective-research` | Known-present control for absence claims | XM-11, 2026-09-30 |
| U08 | Longest skills | `reflective-spec-plan` | Decision-record field sentence (`Claim` … `Falsifier / Verification`) | Implementation Decision Gate |
| U09 | Reader concern | `reflective-research` | Tally-reconciliation clause inside `Never` | Positive duty in a prohibition list; P6 tied 3/3 versus 3/3 |
| U10 | Reader concern | `reflective-implement` | Step 4 decision traceability | Restates the spec-plan gate (September review C16) |
| U11 | Reader concern | `reflective-research` | State Ledger `stale` downgrade bullet | Restates the status rule (September review C22) |
| U12 | Reader concern | `reflective-review` | `Never` bullet on spec silence | Positive duty in a prohibition list |

## Execution Steps

Each step needs the authorization named beside it.

1. Owner approves caps, families and this plan (authorization A).
2. Freeze the twelve-unit manifest, fixtures and rubrics with hashes; the owner reviews the unit list.
3. Qualify one recipe per CLI and mode.
4. Run the pilot, score blind, assign verdicts.
5. Report; send deletion proposals to the owner one unit at a time.

## Evidence vs Inference

- **Verified:** CLI versions and model lists on 2026-11-26 without inference; the WGS-X4b ruling; DF-C2's whole-skill scope; the P6 tie; the T1 results, including the T1-B rubric defect.
- **Inferred:** multi-part fixtures raise sensitivity; two non-host families reduce single-family bias.
- **Unknown / unverified at resumption:** a host-enforced no-tool configuration, exact quota debit (including two interrupted calls), cohort-wide context stability, and the missing Grok outcomes. Stored successful receipts report token usage for their own calls; they are not provider billing evidence.

## Falsifiability

- If both arms saturate on most units, the fixtures were insensitive; the pilot is inconclusive and is not evidence that units are no-ops.
- If a deleted no-op candidate later coincides with a recorded regression on its behavior, the verdict was wrong and the unit returns.

## Interruption and Recovery (2026-11-26)

The host terminated job `bg_54` at its 3,600-second deadline (16:49:21 +0800). No aggregate `pilot/jobs.json` was emitted: that driver writes it only after both family threads join. A post-timeout process snapshot found no remaining pilot driver or pilot CLI process. No provider call was relaunched during recovery.

| Family / model | Completed receipts | Dispatched, outcome unknown | Not dispatched | Complete pairs | Completed orphan outputs |
| --- | --- | --- | --- | --- | --- |
| `agy` / `gemini-4-hydrogen-medium` | 72 | 0 | 0 | 36 | 0 |
| `cursor-agent` / `grok-4.7-medium` | 53 | 2 | 17 | 21 | 11 |

The two unknown invocations are `cur-U02-control-r1` and `cur-U01-treatment-r1`: each has an empty runner-created receipt directory, not a result receipt. Their provider outcome and quota debit remain `OUTCOME_UNKNOWN`, `retry_safe: false`. A missing receipt is not proof that inference never ran. The other seventeen slots have no invocation directory. All 125 completed receipts record exit 0, non-empty successful output, zero observed tool events and an empty workspace; these are observations, not host no-tool enforcement.

**Recovery evidence:** the session-private `x4b-pilot-2026-11-26/recovery/snapshot.json` hashes all 500 retained receipt/stdout/stderr/output artifacts. Its per-slot receipt IDs match the independently parsed completed-job IDs in `pilot/progress.log`; a separate filesystem inventory finds 125 output files. All 24 prompts, twelve frozen scorers, the wrapper and extracted scaffold still match manifest `8844de3597db405a3343cdbacbe6d322d6b048d774dd0076ab98288b30508eea`. The frozen prompts are the selection-time baseline, not a claim that later T1-B landing changed the trial inputs.

**Scoring boundary:** only the 57 complete pairs enter the unchanged scaffold in a fresh `diagnostic/` namespace (114 candidates). Eleven completed orphans remain preserved and unscored, outside that paired denominator. Nineteen missing slots remain unknown/not-dispatched, never failed outputs. The unused preliminary `score.py` would drop an incomplete pair and initialize missing pass counts to zero; recovery does not execute that unblind path or generate a replacement `pilot/jobs.json`.

The frozen graders run through a separate host launcher under macOS `sandbox-exec`. A local probe read scorer code and its allowed candidate while denying the manifest, recovery inventory, an arm output, a receipt, writes and network access. This bounds those scorer paths; it does not establish model-worker containment or grader validity. The first shell/stdin probe emitted no receipt content and was reported as a tool issue; the corrected array-form subprocess probe produced the retained proof. Captured scorer output contains zero `control`/`treatment` tokens.

**Current disposition:** partial diagnostic evidence only. No load-bearing/no-op label, deletion proposal, or efficacy claim follows from an incomplete and underqualified cohort. Unit-level observations and blind grader review are recorded below after scoring; the original thresholds and falsifiability rules above are not rewritten.

**Continuation gate:** qualify a no-tool configuration at the pinned CLI version, reconcile the two unknown dispatched outcomes or have the owner explicitly resolve their retry/cost risk, and record a bounded continuation protocol without reusing altered fixtures or graders as if they were the same cohort. DF-C2 and DF-PB1 remain held; this interruption supplies neither custody inputs nor human scoring/acceptance.

## Diagnostic Scores and Unit Disposition (2026-11-26)

`C` is the full frozen skill; `T` deletes exactly the selected unit. Each cell is **frozen predicate passes / scored outputs in complete pairs**, not successful tasks out of three intended repetitions. The different Grok denominators are observed missingness, not a changed repeat target. Eleven orphans and nineteen missing slots are excluded as stated above.

| Unit | Grok C | Grok T | Gemini C | Gemini T |
| --- | --- | --- | --- | --- |
| U01 | 1/1 | 0/1 | 1/3 | 0/3 |
| U02 | 1/1 | 1/1 | 3/3 | 3/3 |
| U03 | 1/1 | 0/1 | 3/3 | 0/3 |
| U04 | 1/1 | 1/1 | 3/3 | 3/3 |
| U05 | 2/2 | 0/2 | 3/3 | 0/3 |
| U06 | 1/3 | 0/3 | 2/3 | 0/3 |
| U07 | 2/2 | 0/2 | 3/3 | 0/3 |
| U08 | 2/2 | 0/2 | 3/3 | 2/3 |
| U09 | 3/3 | 3/3 | 3/3 | 3/3 |
| U10 | 2/2 | 0/2 | 3/3 | 0/3 |
| U11 | 1/1 | 1/1 | 3/3 | 3/3 |
| U12 | 2/2 | 2/2 | 3/3 | 3/3 |

**Every unit's formal disposition is `inconclusive`.** None is promoted to load-bearing or a no-op candidate from this interrupted, underqualified cohort. Some predicates distinguish full versus deleted text; that is diagnostic output sensitivity, not execution efficacy. Five units have identical pass labels across all their available paired outputs; only U09 has all twelve intended outputs. This does not silently trigger or waive the original "most units saturate" falsifier.

### Blind review and measurement limits

Before the sealed arm map was opened, two read-only reviewers examined two predetermined opaque candidates for each of U02/U04/U09/U11/U12. The coordinator also read both U09 outputs in full, satisfying the full-twelve identical-score check before unblinding. All ten samples support their *scored obligation*: actual declined-scope entries, a rejected/misattributed Q2, population-based tally reconciliation, a stale ledger status, or an empty-cart finding. No original label was changed.

One U09 sample exceeds the task's under-350-word limit, which the scorer does not measure. Thus "predicate pass" is explicitly narrower than task acceptance. The blind review is same-host advisory judgment, not another experimental family or independent non-model proof.

The static grader review found concrete limitations; the coordinator checked the U04/U08/U11 predicates directly. These were not repaired or re-pinned after observing outputs:

| Units | Limit on interpretation |
| --- | --- |
| U01 | A fixed keyword window after `Review Focus` can include a later section and misses other valid input-class wording. |
| U02 | T still requires `Declined to Judge` elsewhere in the contract; a pass cannot establish the deleted bullet is generally unnecessary. |
| U03 | Keyword presence does not check the required tried/expected/actual/fix entry. The selected unit is a heading/template entry despite headings being excluded by the original selection rule. |
| U04 | The negative-verdict regex includes `search service`, so an endorsing sentence can pass. The selected table row also falls outside the literal bullet/step/sentence selection shape. Both sampled outputs genuinely rejected Q2. |
| U05 | The predicate checks the verbatim `TWINS: searched` prefix, not the correct pattern, site count, repair or an executed search. |
| U06 | Three label/keyword lines need not constitute a complete, reasoned consumer map. |
| U07 | The predicate tests a known-present-check phrase, not the searched population or a performed negative-result check. |
| U08 / U10 | Only `counterargument` and `falsifi` substrings are required, not all six decision fields; surviving text and global guidance overlap the duty. |
| U09 | Same-line numbers/population keywords can accept a hedged tally and miss a valid multiline reconciliation; word budget and license diligence are unscored. |
| U11 | A same-line `4.2.0`/`stale` match does not distinguish a genuine downgrade from "not stale"; other freshness clauses survive deletion. |
| U12 | Keyword and nearest-heading heuristics miss equivalent phrasings and some declined/deferred headings; empty-input crash detection may already be ordinary reviewer behavior. |

All fixtures asked for a single text response with no tools. These observations measure emitted wording/proposals, not completed twin sweeps, consumer propagation or repository repairs. U03/U04's selection-shape mismatch is recorded as a protocol defect, not retrospectively admitted. The raw scores, blind audit, sealed map and per-slot recovery inventory remain under the session-private `x4b-pilot-2026-11-26/diagnostic/` and `recovery/` directories; the decision-bearing counts and limits are reproduced here so a fresh checkout does not depend on those paths.



### Protocol review adjudication

The protocol reviewer independently recounted 72 Gemini completions, 53 Grok completions, 21 Grok complete pairs and eleven orphans, supporting the preserved-denominator recovery. The coordinator did not adopt three stronger interpretations: a plan-mode block is not no-tool enforcement for Gemini either; shared priming can interact with an ablation, so it cannot be assumed incapable of affecting a C–T gap; and five saturated units out of twelve do not establish the preregistration's "most units" condition. The observed Gemini U08 count is C 3/3, T 2/3, not the conflicting shorthand in that advisory.

The operative reason to withhold formal labels is the incomplete/underqualified cohort plus the recorded measurement defects, not a post-hoc rule replacing the preregistered thresholds. A verified no-tool mode, explicit handling of U03/U04's selection shape, acceptable grader/task coverage, stable background context and untouched final-evaluation inputs are prerequisites for a stronger future claim. Grok's ZDR status and exact provider quota debits remain unverified; a successful included-plan call does not establish either.

## Continuation Authorization and Preflight (2026-11-26)

After local commit `7e5841d512`, the owner said **"continue"**. A separate form then explicitly authorized one replacement invocation for each of the two unknown slots, accepting that the original requests may already have consumed quota (`authorize_two_replacements_accept_possible_duplicate_quota`). That resolves the owner's retry/cost disposition, not the original provider outcomes: both originals remain `OUTCOME_UNKNOWN`, and changing invocation IDs does not make them idempotent or prove zero debit.

The continuation envelope is **at most twenty CLI invocations**: one qualification canary, seventeen never-dispatched slots, and two owner-authorized replacements. No automatic slot retries, credits purchase, overage or push. The CLI's opaque internal provider requests/retries are not equated with CLI invocation count. The nineteen slots retain the original Cursor seeded order after filtering out completed slots; prompts and scorer bytes remain frozen. No completed original slot is resent.

Version inventory without inference: `cursor-agent` is still `2026.11.22-e9042b2`; `agy` is now `1.5.18`, versus the original `1.5.17`. The 72 completed Gemini outputs are retained without re-execution. Only the missing Cursor/Grok slots are in the continuation manifest, held in the session-private `continuation-2026-11-26/slot-manifest.json`.

### Unknown-call reconciliation

The canonical `/private/tmp/x4b-ws/...` workspace-to-store MD5 mapping was checked against the known completed Cursor canary, then used to inspect only the two synthetic interrupted conversations. U02 has `hasConversation: false`, an empty latest-root ID, four stored blobs and no stored assistant message. U01 has `hasConversation: false` and no message database. Both worker logs stop at workspace indexing; neither contains a provider result. No final answer was recovered and no replay/resume request was sent. These local observations cannot establish that the original provider request was never accepted or billed.

A metadata diagnostic inadvertently printed conversation-local encryption fields from the synthetic chats. They were not used for authentication or decryption, no account token/API-key file was opened, and subsequent metadata output uses a field allowlist. No user conversation data was deleted or rewritten to conceal the event.

### No-tool qualification remains a prerequisite

Official [CLI permissions](https://cursor.com/docs/cli/reference/permissions), [configuration](https://cursor.com/docs/cli/reference/configuration), [third-party/native hooks](https://cursor.com/docs/reference/third-party-hooks) and [headless behavior](https://cursor.com/docs/cli/headless) were read on 2026-11-26. Permissions support project deny rules for Shell/Read/Write/WebFetch/MCP; generic `preToolUse` can return `permission: deny`. Public documentation alone does not establish coverage in the pinned build.

An initial scout's negative search missed the relevant lazy chunk. A complete byte scan over all 99 installed JS files (34,619,850 bytes), with `sessionStart`/`executeHookForStep` as positive controls, found `preToolUse` in `9622.index.js`, `index.js` and `connect-pool-worker.js`. The pinned `hooks-exec` module contains the generic rejection gate, streamed/MCP paths, deny-dominant response merging and `failClosed` handling. That refutes the earlier absence inference, not every possible dispatch bypass. An offline qualifier must exercise the actual installed loader/merge/gate logic and identify unmapped or remote tool paths before admission; no guessed JSON setting or tool-free model answer substitutes for it.

An isolated-HOME/config `cursor-agent status` probe requested no inference and reported not logged in. No credential file was copied, linked or read to repair that profile. Any qualified recipe must separately identify ordinary CLI setup/auth/logging and unisolated session hooks rather than claiming those processes are absent.

**Continuation admission: HELD.** Zero new pilot CLI invocations. Host research agents and documentation retrieval are separate from the experimental call count. The offline outcome below does not satisfy the no-tool prerequisite, so neither the canary nor the nineteen slots was dispatched. Any later host-configuration change remains a recorded context change; filling 144 output slots would still not repair the original grader, selection or causal-inference limitations.

### Offline qualification outcome

The qualifier exercised installed module factories in a Node process with a bash-backed transport stub and a sentinel executor. This was not an OS-isolated or whole-CLI run. Source pins: `index.js` SHA-256 `860ce5cc5c313fbd6447d00973f0fce087b43fa1e1543cf91c4e4aa065ef8b6a`; `9622.index.js` `5cf1067834cad1a15e7db9eb08de2841408123404829c8c3906499eb12670206`; `696.index.js` `20bd0ad03b5581ada5c18ba8314e23c2cdc12c579fc8fcb774b8373927220720`.

| Receipt | Explicit PASS | Explicit FAIL | OBSERVED | Unasserted diagnostic |
| --- | --- | --- | --- | --- |
| Module probe | 36 | 0 | 3 | 4 |
| Recipe probe | 18 | 0 | 0 | 1 |

The receipts prove that a valid project hook loads, deny dominates a conflicting allow response, six hook-command failure cases deny with `failClosed:true`, and the tested Shell wrapper rejects before its sentinel executes. Empty/nonzero hook output without `failClosed` produces no denial. Invalid project configuration and a symlinked configuration path leave the project hooks absent. Merely passing 21 synthetic tool names directly to the hook does **not** establish coverage of those tools' actual dispatch paths. The probe's process exit is not an admission token; the recorded result fields and residual boundaries control the decision.

The coordinator declined the qualifier's **conditional admission** recommendation:

- The accessor returns an unwrapped executor for an unmapped symbol. Which registered internal executors are model-callable remains unverified; this is not a reproduced model-facing exploit.
- Necessity of the engine-side hook RPC for Task, subagent, web-search and glob operations was not established. A direct hook call bearing one of those names does not test that integration.
- The MCP wrapper skips its hook on `smartModeApprovalOnly`. That source branch establishes a hook shortcut, not a demonstrated unapproved MCP operation; the inner operation's behavior and model-facing reachability were not proven.
- Global/team/plugin hooks remain additive. Permission-result merging is deny-dominant, but that does not isolate their commands or environment changes.
- Only the candidate `hooks.json` was schema/loader exercised. The candidate's project `cli.json` is not runtime-qualified: official configuration documentation permits only permissions at project scope, so its extra approval/sandbox fields do not establish enforcement. No candidate configuration was installed in the user's host or used for a model call.

The remaining gap is complete end-to-end tool coverage, or a separately demonstrated host boundary that covers the residual. It cannot be closed by another generic execution approval, a tool-free answer, or silently excluding tool classes. A different bounded execution mode would require an explicit owner decision and a newly demonstrated safety boundary. No new scoring namespace was populated; the original 125 outputs, 57 scored complete pairs, eleven unscored orphans and all twelve inconclusive dispositions remain unchanged.

Receipts and runnable module probes remain session-private under `continuation-2026-11-26/qualification/`; the raw qualifier recommendation is retained as advisory, not adopted authority. Their counts, source pins and decision-bearing limits are recorded here so a fresh checkout does not depend on that directory to understand the hold.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Next decision |
| --- | --- | --- | --- |
| X4B-PLAN1 | This plan | Drafted 2026-11-26; the owner authorized execution the same day | — |
| X4B-RUN1 | Pilot execution | Interrupted 2026-11-26: 125 completed receipts of 144 intended slots; no completed-cohort verdict | Preserve partial diagnostics; X4B-CONT1 records the later authorized but held continuation |
| X4B-DEL1 | Any unit deletion | Not authorized | Per-unit owner approval after verdicts |
| X4B-CONT1 | Missing-slot continuation | Owner authorized 2026-11-26, including two replacements with accepted duplicate-quota risk; one canary plus nineteen slot invocations; HELD after offline qualification | Demonstrate complete no-tool coverage or a separate host boundary; changing execution mode needs an explicit owner decision |

## Standing Non-Goals

- No skill edit, installation, permission widening, commit or push follows from this plan. The pilot's model calls stay within the caps in Pilot Configuration.
