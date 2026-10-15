# DF-C2 Protected Pool and Dispatcher — Workflow Spec — 2026-10-15

Language: English

> **Status: design decided; implementation, host setup and real admission unexecuted.** Workflow spec version `3`; campaign protocol remains `DF-C2-2026-10-14` / `2`. Version 3 resolves advisory findings on the working v2 design; v2-keyed implementation/readiness conclusions are stale, not execution evidence. This is a non-authoritative campaign plan, not TeaPrompt harness policy or an adopted runtime.

## Goal, authority and scope

The maintainer requested **“You design and decide plans for both”**: the answer-free manifest/custody arrangement and the protected curator/dispatcher interface. This record makes those design choices rather than asking the maintainer to supply a design. It supersedes the undecided boundary/intake step of session-local `df-c2-custody-workflow-spec.md` v1, without rewriting that pinned artifact.

**Chosen design:** one independently controlled, maintainer-operated Apple Silicon host for protected custody and execution; owner-mediated metadata-file handoff; one private, single-invocation dispatcher adapter using the existing Python consumer. No permanent HTTP service, coordinator SSH access, queue, cloud broker, new skill or TeaPrompt runtime.

Strictness L4. Coordination stays a human-operated Formalization L1 SOP; enforced persistence, tickets, budgets and role execution remain private host-runtime controls (Formalization L4 execution), not guarantees delivered by this document or a new unattended scheduler. Existing campaign permission, seven maintainer-owned human roles/conflicts, reported sealed pool and subscription-only/no-balance-fallback confirmation remain supplied. Planning does not create deployment/source-change/transfer permission, a phase grant or admission evidence.

**Planning acceptance:** both interfaces have exact data/read boundaries, ownership, dependencies, source-compatibility work, failure dispositions and falsifiers. **Execution acceptance:** unchanged [population, sealing, FTEST-01–08 and phase rules](fresh-dogfood-campaign-preregistration-2026-10-14.md#readiness-sealing-and-authority) plus CUST-AC-1–5 below. No new campaign output is authorized by completing this plan.

Non-goals: recreate or inspect the reported pool here; move/delete its copies; expose finals/answers/arm maps; provision a host/account; copy credentials/operator stores; edit current consumer source; run models/canaries; change caps, decision rules, human ownership, registry or runtime ownership.

## Evidence actually checked

- Current [v2r1 source ledger and seven-obligation disposition](fresh-dogfood-campaign-preregistration-2026-10-14.md#full-seven-obligation-continuation-and-v2r1-repair-2026-10-15); seven-file manifest `fe93c45343a4e3267daecf4845e9668498ed5dc98bdde144b19470ca323cca34`.
- Private `consumer.py:48-105,108-149`: `run_files` reads inputs on the caller's host; `run` checks exact canonical per-session input hashes; only the Python API accepts native contract/backend/common objects. The CLI prints the full result, not an approved metadata projection.
- Private `campaign_support.py:99-175,219-250,332-390`: immutable phase grant/source bindings, same-root grant-change refusal, completed-producer successor restriction and existing locked accounting.
- Private `go_provider.py:89-175,202-225`: live authority before credential access; exact phase/source/grant/credential quota binding; no API setting readback is claimed.
- [Observed UID correction](fresh-dogfood-campaign-preregistration-2026-10-14.md#same-uid-claim-correction-and-distinct-uid-controls-2026-10-15): host exec can select the file-owner UID. Guest DAC and candidate confinement do not exclude the host controller.
- Actual `consumer.py run --help` executed for this planning turn. It exposes fixture/messages/role arguments, but no native-contract/backend input. No phase, input or credential was opened by help.
- `python3 -I -S -B compatibility_probe.py` exercised two current interfaces in new public-only scratch: `Consumer.run_files(..., native_contract=...)` raised `TypeError` before allocation; appending a later successor input binding to the same phase approval raised `BudgetIntegrityError`, with unchanged journal bytes. Zero model/provider/native effects or audit violations. The first probe launch had a synthetic `scratch_root` placement error; only that disposable grant input was corrected, and the failure receipt is retained.

These are source/interface observations, not proof a protected host, eligible pool, authenticated ticket or qualified scorer exists. Host availability, actual pool metadata/copies, operator capability inventory and current-source role/capture evidence remain `unknown`.

## Decisions and rejected alternatives

| Decision / claim | Evidence | Counterargument / unknown | Selected action | Falsifier / verification |
|---|---|---|---|---|
| D1: custody must exclude the coordinator's control, not just its default UID | Current host-exec observation; FTEST-06 all-copy boundary | A carefully administered local boundary might work, but none was demonstrated and this coordinator has host control | Use a separate maintainer-controlled host; coordinator/author have no login, admin, debugger, container-control, screen-sharing, shared-volume, backup/key or tool-relay capability there | Any such recoverable access fails CUST-CHK-02; physical separation alone is not a pass |
| D2: metadata export is an interface, not the authoritative pool | Owner reports a pool; source hashes and projections did not establish custody | An existing owner format may differ | Preserve its bytes/format; curator produces the typed projection below and binds it to the authoritative protected manifest | Missing lineage, semantic freshness or copy evidence fails CHK-01/03; no replacement pool |
| D3: manual bounded dispatch is sufficient | Existing consumer/Budget/worker do execution/accounting; humans already own gates | Manual operation can misbind a case or copy raw stdout | One protected-side adapter selects only a preauthorized session; raw output never enters the coordinator channel; export uses a closed allowlist | Cross-case selection, arbitrary argv/path or content export fails CHK-04/07 |
| D4: a versioned private input-binding extension is necessary | Canonical messages hashes live in immutable phase approval; successors depend on later producer output | Rewriting approval after a producer appears simpler | Use immutable per-session tickets under one fixed phase authority; do not rewrite the phase grant or reset accounting | Changed-parent-grant, forged/stale ticket or fabricated predecessor fails CHK-05/06 |

## 1. Existing pool: manifest and all-copy custody plan

### Source of truth and preservation

The curator works with the **existing reported pool at its actual owner-held location**, not a pool generated by this coordinator. The curator privately reviews six selection and nine final instances against every old instance and each other under FTEST-01. New IDs/digests alone do not establish semantic disjointness. Instances remain `DF-C2-{IMP,REV,HOF}-S01/S02` and `-F01/F02/F03`; existing challenge/healthy/sentinel contracts are unchanged.

Preserve the original pool and manifest. Any relocation, new copy or permission change is a separately reviewed setup action. A readable generator, notebook, log, cache, sync/backup copy or old source constant holds eligibility; later deletion or encryption cannot erase disclosure. Do not silently repair eligibility by rewriting an instance or discarding evidence.

**Authoritative protected manifest P** records campaign/protocol/pool identity, creation/sealing time, instance/content/contract identities, privately supported semantic-freshness findings, frozen functional and authority oracles, applicable rubric dimensions, all current recoverable-copy locations/readers and control-channel evidence. The inventory explicitly includes provider-accessible retained request/response/dashboard history and recoverable credential copies. P predeclares future execution/capture namespaces and owners; the operator records actual copies as they occur in the linked protected ledger, before the dependent effect or evidence release. Undeclared copies/readers stop admission. P and original source manifests stay immutable; append receipts rather than rewrite hashes.

### Answer-free projection contract

`pool-metadata.json` is the curator's export/view, **not** a second authority or a sealed pool. If an owner format already exists, map it to this view without rewriting that original. No real file or identity is invented by this design.

| Field | Required shape / meaning |
|---|---|
| `schema`, `campaign`, `protocol_version` | `df-c2-pool-metadata-v1`, `DF-C2-2026-10-14`, integer `2` |
| `pool_id`, `manifest_sha256`, `curator`, `sealed_at` | Owner-established ID; SHA-256 of actual P bytes; existing designated curator identity; timezone-qualified timestamp |
| `selection`, `final` | Exactly six and nine unique entries; each family contributes S01/S02 and F01/F02/F03 respectively |
| Each entry | `instance_id`, `family`, `split`, `case_kind`, `input_sha256`, `task_contract_sha256`, `functional_oracle_sha256`, `authority_oracle_sha256`, `rubric_dimensions` |
| `freshness_evidence`, `custody_evidence`, `copy_inventory` | Non-sensitive receipt IDs/digests and role/read-grant summaries linked to protected evidence, not self-certified booleans |
| `exported_at`, `export_owner` | Export provenance; does not substitute for creation/sealing time or current denial evidence |

Use lowercase SHA-256 hex digests and a closed schema at every object depth; reject extra/duplicate fields, duplicate IDs, wrong types, missing families, cross-split collisions, mismatched current hashes and unknown versions. IDs, family/split/case-kind and rubric dimensions must belong to the frozen registries; no arbitrary descriptive strings or embedded paths. Missing actual values hold; neither zero-fill nor sample values. Hashes are identity checks, not confidentiality or freshness proofs; low-entropy content may be guessable from a digest.

The projection excludes task bodies, expected answers, oracle implementation, arm maps, judge order/seed, raw prompts/responses/streams, absolute protected paths, keys/cookies and operator memory. Protected evidence locators are opaque owner-held receipt IDs; only this safe projection is handed back to the coordinator.

## 2. Protected dispatcher: boundary and interfaces

### Host and readers

Use a dedicated maintainer-controlled Apple Silicon host to reuse the inspected Apple backend, subject to actual availability and fresh validation. **Not** a VM/container administered by this coordinator. No coordinator/author remote login, browser/tool adoption, mounted/synced home, shared keychain, management socket or raw-console feed. The maintainer operates that host separately. Host labels, account names and a second machine by themselves are not denial evidence.

The control/copy inventory covers coordinator-reachable provider history, historical credential/secret-store/config/tool-history copies, backups, exports and tool/capture channels. Before first dispatch, verify that the admitted credential and any credential granting access to protected run evidence have only inventoried owner-protected copies and no coordinator read/control bypass; residual accessible copies require separately authorized restriction/revocation/rotation, not deletion-as-proof or a live unauthorized POST test. This plan performs none of those actions. Accepted Contributor/non-ZDR and opaque provider-state limitations remain limitations, not an inventoried-clean location, coordinator-denial evidence or a new ZDR requirement. Unknown coordinator-reachable access holds.

| Actor | Allowed content | Explicit exclusion |
|---|---|---|
| Coordinator / candidate author | Answer-free metadata and approved aggregate/status receipts | Protected host control; final inputs; raw execution/capture; oracles; arm maps |
| Existing curator | Pool, freshness comparisons, protected manifest and frozen oracles | No delegated broad read grant to coordinator/author |
| Existing host/capture dispatcher | Assigned public task/common brief/target layer, approved private execution schedule, protected run records | No oracle/answer injection into model inputs; no arbitrary coordinator command execution |
| Model worker / successor | Its assigned public inputs and allowlisted workspace; successor receives only its producer handoff plus common setup | Other cases, hidden answers, oracle internals, operator credentials/memory; no target handoff skill or DECISION sidecar sent to successor |
| Designated oracle / semantic scorer | Its frozen allowlisted scoring packet and applicable reference/rubric | Unneeded pool access, arm map and private judging schedule |

These are process/data capabilities, not newly designated human roles. Existing role overlap/conflicts remain recorded. A human who knows the arm mapping is not made arm-blind by an OS account or opaque filename; unqualified semantic endpoints stay unavailable. No extra human, independent scorer or cognitive blinding is assumed. If staffing cannot produce a required qualified judgment, preserve that null/held endpoint and apply the unchanged eligibility rule; do not manufacture a score or an eligible confirmation.

### Adapter contract — planned, not implemented

A future versioned **private** `dispatch_case.py`, operated only on the protected host, has two bounded commands:

- `run --root APPROVED_CAMPAIGN_ROOT --phase {pilot,confirmation} --session-id PREAUTHORIZED_ID`
- `export --root APPROVED_CAMPAIGN_ROOT --phase {pilot,confirmation} --output OWNER_CHOSEN_METADATA_FILE [--session-id EXISTING_ID --release-id AUTHORIZED_RELEASE_ID]`

These are **unverified proposed adapter commands**, not existing `consumer.py` flags. No arbitrary fixture path, model, tool, code, shell command, callback, cap, deadline or credential is accepted from the coordinator. The operator selects sessions from the frozen execution schedule, not from model/coordinator instructions. `run` does not drive the next case or release a human gate.

Python interface decisions for the later implementation:

- `dispatch_case(root, phase, session_id)`: construct the bound Budget and derive `families` from its validated immutable grant; resolve the ticket and native identities, not task bodies. Use `Consumer.run_files(..., session_ticket=..., native_contract=..., native_backend=..., native_common=...)`. The adapter cannot select arbitrary content or substitute an object for a pinned native identity; live `check_runner` callbacks remain forbidden.
- **Consumer remains the enforcement boundary:** both `run_files` and direct `run` require the authenticated ticket. Budget resolves/revalidates it against the protected issuance record; a caller-supplied dict/digest is not authority. `_bound_input` checks each raw digest during the guarded immutable read, then `run` checks canonical fixture/messages/intervention, complete role/context/relationship equality and actual pinned native configuration/module/object identities before `validate_inputs` and `allocate_session`. A validate-then-read adapter check cannot replace these in-path checks; direct API calls get the same refusals.
- Native materialization uses only the runtime/config/interpreter/backend module and CLI identities in S plus the grant-bound native contract. Instantiate the existing Apple backend/common objects from those exact verified bytes/configuration; reject arbitrary caller objects, callbacks or unknown backends before allocation. Relocation/config changes require new S/A bindings, not a matching display label.
- `export_receipt(root, phase, output, *, session_id=None, release_id=None)`: exclusive-create a closed-schema export from protected persisted accounting/results. Without a verified release record, emit only phase-level status/aggregates; a session/release argument pair must both be supplied and valid. The release record binds G, score-freeze and leak-audit receipt digests, named human release authority and exact permitted export scope. Forged, missing or stale release evidence refuses session-scoped output. Never forward raw returns, exception strings or model-authored status. Re-exporting evidence never reruns a session.

All provider calls remain in the existing transport/Budget path. The adapter adds no accounting engine, remote API, automatic retry, background worker or scheduler.

Clean cutover: remove the old free-argument `consumer.py run` CLI, not a compatibility alias. The protected dispatcher becomes the live CLI; direct Python APIs remain ticket-enforced. Retain `payload` only as offline/public serialization and `snapshot` only as a protected operator phase-aggregate view; neither is a live bypass or a coordinator-facing raw stdout channel. Migrate active private callers and lifecycle regression fixtures to the ticket path; preserve old v2r1 files/receipts as historical evidence.

### Phase authority and late-bound session tickets

Current v2r1 cannot be declared dispatcher-ready: `run_files` lacks the native parameters, its CLI emits raw content, and fixed `approval.session_inputs`/`allowed_inputs` cannot prehash a producer's not-yet-created successor messages. Updating the immutable approval later is rejected by Budget. These are explicit implementation work, not a claimed current feature or permission to bypass the checks.

The future private source revision uses **one uniform ticket path for all roles**, not an old-grant/static-binding fallback. `protocol.py` owns `df-c2-phase-grant-v3`, `df-c2-input-authority-v1`, `df-c2-session-input-ticket-v1` and `df-c2-dispatch-release-v1` schema constants; these private record versions do not change experimental protocol `2`. `_validate_grant` structurally validates `input_authority`: protected ticket directory and issuer UID/principal, source identities, frozen issuance/derivation-policy digest and execution-schedule digest. The schedule freezes allowed canary/trial contexts and conditional producer/replacement derivations; its private arm mapping never leaves the host. Policy/schedule precede G and describe its digest field without containing its later value. Neither may add a scored slot, family, reserve or call.

Each owner-private, exclusive-created immutable `session-inputs/SESSION_ID.json` binds:

- campaign/protocol, phase/root, phase-grant digest, source/pool/readiness identities and the host-verified issuer;
- exact session ID, role/kind/family/canary, distinct nullable `producer_session_id` and `replaces_session_id`, and the schedule entry/derivation identity;
- allowlisted absolute fixture/messages paths and raw-byte digests, their canonical-value digests, and the exact intervention digest or null;
- native contract identity and pair-matched common-setup digest; primary C binds null target-layer digest, primary T binds the full declared target digest, and successors bind null handoff-target digest plus completed producer session/handoff/receipt and derivation-policy digests. Issuance enforces this against the protected arm map; the actual emitted payload/discovery/hook/memory manifests still need the separate FTEST-02 comparison.

Mechanical issuer predicate: the grant-bound protected root/ticket directory must be physical, issuer-owned `0700` directories with no worker/coordinator writer or control path; tickets are bounded owner-only, single-link regular files, exclusive-created then `0400`, opened with no symlink following and stable before/after descriptor identity. Validate the source-pinned policy/schedule, exact issuer UID/principal and a matching `ticket_registered` issuance/digest event in the existing protected hash-chained phase journal before allocation. A file, UID, hash or log alone is insufficient without CHK-02's actual control exclusion. Workers/coordinator cannot mint, replace or edit tickets, inputs, policy, schedule or the trusted journal anchor. Budget revalidates issuance/context under its existing lock, atomically rejects duplicate/pending/unknown/held contexts and retains all original caps/deadlines; registration creates no reserve or call. No grant rewrite or new counter namespace.

A Q-HOF successor ticket is issued **after** its legitimate completed producer seals the handoff; its new message hash is fixed before successor allocation. The derived input is only that handoff and frozen common setup, not producer conversation, target skill, sidecar or oracle feedback. The neutral successor canary has its already-declared synthetic handoff and no producer trial. Authorized replacements retain originals and consume separate producer/successor reserves as applicable.

At the existing Budget boundary, an ordinary successor maps `producer_session_id` to the legacy producer argument; a replacement maps `replaces_session_id` to the replaced attempt and inherits/validates its producer lineage. A replacement successor must retain both relationships. Confusing the two fields cannot create a second successor, replace a completed/censored/unknown endpoint or turn one reserve into whole-chain replacement funding.

### Binding order, locality and durability

Avoid self-referential hashes: protected pool P + executable/locality identities S + zero-model host/custody readiness A precede immutable phase grant G. A records **pre-canary** readiness, not completed model-role qualification, and does not include G's hash. G binds P/S/A and input authority. Current quota proof and native execution contract then bind G; tickets bind those established identities. Canary/call/capture receipts append afterward. None requires rewriting a parent whose digest it contains.

Source relocation changes the required `source_root` metadata. Preserve the current v2r1 manifest/receipts; create an explicitly reviewed new locality/source manifest and include the adapter, ticket policy/verifier, interpreter, native CLI/runtime/config and exact target-skill identities in the host execution manifest. Do not label the resulting manifest `fe93c453…`, reuse historical admission, or pretend the seven-file manifest covers an eighth executable.

P, G, tickets, ledger, raw inputs/outputs, maps and capture stay on the protected host under the artifact owner for the campaign lifetime, with owner-controlled backup/copy grants inventoried. The coordinator keeps only safe projections and digest receipts. Missing protected bytes cannot be reconstructed from those digests; admission/resume holds. Operator/provider credentials stay in the protected secret store, never source, argv, model workspace or export. No product-database credential is required or permitted.

## Fixed workflow, ownership and gates

| Stage | Type / owner | Inputs → output | Transition / gate | Failure and recovery |
|---|---|---|---|---|
| 1. Inventory existing pool | Human/data: curator | Existing artifacts → P and supported freshness/copy findings | Curator freezes before any new model output; CHK-01/03 | Hold unread/unknown/exposed copies; preserve, no silent replacement |
| 2. Establish protected host | Human/action: maintainer/operator | Reviewed host/control/transfer inventory → actual exclusion/assigned-marker evidence | Exact setup authorization, no campaign inference; CHK-02/04 | No local-UID or guest-only substitute |
| 3. Bind source/readiness | Data: existing host/capture operator; artifact owner/leak-audit owner check evidence under recorded role overlap | P, new source/locality and current inventories → A | Full current six-store/eleven-file, native/capture/actor/oracle evidence before provider effect | No eighth human or independent human is assumed; missing stores/delayed ingestion hold, never copy operator DBs or fabricate empty stores |
| 4. Materialize phase authority | Human/data: approver/operator | Existing permitted envelope + P/S/A → G, quota/native bindings | Actual source/phase/credential mapping; no repeated Go-setting confirmation | Changed account/setting or missing current evidence holds; no secret in export |
| 5. Issue ticket and invoke once | Data/action: protected issuer/dispatcher | Approved schedule/G + fixed inputs or completed handoff → immutable ticket and one consumer invocation | CHK-05/06; validate before read/reserve; same original Budget | No arbitrary input/command; duplicate, stale or unknown state cannot rerun |
| 6. Qualify then run pilot | Action: existing host/capture operator; existing artifact/leak-audit owners retain/check canary evidence under recorded overlaps | Five actual canaries → qualified phase → fixed pilot | Existing 624-call/12-reserve/USD 0 pilot; timed arms serial | Censored/failed canary stops phase; no extra smoke funding |
| 7. Judge, freeze and screen | Human/data: scorer/audit/accepter | Protected blinded evidence → frozen scores/audit and unchanged screen | Existing human qualification and explicit freeze/audit; CHK-07/08 | Missing endpoint stays null; no structural/model proxy |
| 8. Confirm only eligible subset | Human/action: approver/operator | Eligible pilot + exact one-subset grant + admitted finals → evidence/outcome proposal | Separate confirmation authority; `198*k + 144*h + 132`, maximum 870; named human outcome acceptance | No pilot headroom transfer, extra repeats, automatic adoption or acceptance |

**Safe export:** `df-c2-dispatch-metadata-v1` has an explicit scope. `phase_aggregate` admits campaign/phase, fixed disposition/error enums, phase-level P/S/A/G receipt identities and typed aggregate allocation/call/reserve counters only; it omits session IDs, ticket/result digests, per-session resource/performance data and arm-reconstructing order. `released_session` additionally admits only the exact IDs/digests/counters allowed by a verified G-bound freeze/audit/human-release record. Both schemas exclude input/output text, paths, argv, arm identity/order, score mapping, arbitrary exception/model strings and unrecognized fields; unavailable values stay null. Score/unblinding exports use their separately permitted scope, never this record as blanket authority. Raw evidence remains protected and unchanged.

## Acceptance and scenario checks — future execution remains unrun

Existing **CUST-AC-1** population/oracle eligibility, **CUST-AC-2** coordinator/author read-and-control exclusion, **CUST-AC-3** assigned-case delivery, **CUST-AC-4** exact consumer binding, **CUST-AC-5** current role/capture/quota requirements remain the acceptance destinations. The following checks specify evidence, not passing assertions.

| Check / coverage | Given / when → required observation | False-positive guard / owning failure |
|---|---|---|
| CUST-CHK-01 / AC-1, FTEST-01 | Curator inspects existing population → six/nine complete unique identities plus private semantic comparisons and pre-output oracle freeze | IDs/hashes alone or renamed old content do not pass; missing content evidence holds |
| CUST-CHK-02 / AC-2, FTEST-06 | Actual coordinator/author profiles attempt non-final marker recovery via filesystem, admin/debugger/container control, remote session, backup/sync/tool/capture and provider-account access through residual credentials → no recovery or unauthorized control, with actual capability evidence | Owner-UID read is not a bypass; physical separation, key absence assertions or store:false are not a pass; never test unauthorized model POSTs |
| CUST-CHK-03 / AC-1/2 | Inventory source/generator/notebook, backup/log/cache, platform indexing/crash/versioning/pending-sync and future request/capture sinks, plus provider-accessible retained records and credential copies → actual observed locations/readers are covered; inject accessible copy → hold | Unknown reachable sink or unbounded inventory coverage holds; checking only the main directory fails. Accepted opaque provider internals are a disclosed limit, not a universal no-copy proof |
| CUST-CHK-04 / AC-3 | On the actual selected host/dispatcher, assigned public marker is delivered and legitimately used; other-case/oracle/operator-memory reads and arbitrary caller paths/commands fail | Pair positive delivery with exact denials and independent actor evidence; ToolGate-only observations are insufficient |
| CUST-CHK-05 / AC-4, FTEST-04 | Direct API and dispatcher try wrong source/phase/grant/ticket/schedule/native object, forged issuer/journal record, read-time byte swap, duplicate ID or changed parent approval → refuse before allocation/provider effect; restore the valid immutable input for an unreserved context → succeeds | Observe raw-read validation, ledger/workspace effects and all entrypoints, not just HELD/exit 4; no G/ticket rewrite or raw-content exposure to fix a mismatch |
| CUST-CHK-06 / AC-3/4, FTEST-02 | Completed Q-HOF producer seals handoff → one matched successor via later ticket; verify C-null/T-full target and common setup against schedule and actual payload manifests; reject forged/unfinished producer, sidecar/target/transcript injection, producer/replacement confusion and extra successor | No predicted handoff hash, replayed task, new scored slot, claim of opaque provider equality or one-reserve whole-chain replacement |
| CUST-CHK-07 / AC-2/3, FTEST-06 | Seed raw outputs/errors with labels/answers/paths/instructions → retain originals protected; pre-freeze export is phase-only; missing/forged/stale release record refuses session scope, valid release grants only its exact allowlist | Raw returns, broad token scrubs, model-written status or a freeze boolean cannot become export/oracle authority |
| CUST-CHK-08 / AC-5, FTEST-03, FTEST-05, FTEST-08 | Fresh role/capture and actual authoritative scoring-join controls plus qualified human intake → admitted evidence; existing artifact/leak-audit owners rehash P and verify G-bound receipt/anchor lineage before freeze/unblinding; missing stores/delayed ingestion, judgments or freeze/audit → hold/null | Good draft over broken workspace, constant/wrong-type result, candidate-written pass and old mechanics do not admit correctness; neither role labels nor append-only ordering alone prove human blindness or issuer independence |
| CUST-CHK-09 / AC-4/5, FTEST-04 | Crash/disconnect after reservation or possible POST and retry same ID → ledger/resources retained, no duplicate dispatch, unknown effect held | Missing receipt is not no-effect proof; no automatic retry or fresh counter root |
| CUST-CHK-10 / AC-4/5, FTEST-07/08 | Try empty/additive confirmation subset, changed caps, early final read/unblinding or automatic acceptance → refusal; valid one-subset flow retains all endpoints | Draft maxima or owner role strings are not allocations, adequate blinding or final acceptance |

## Task plan and definition of done

| Task | Exact deliverable / files | Dependency, acceptance and checks | Risk / parallelism / Human Review |
|---|---|---|---|
| CUST-TASK-01: existing-pool metadata | Protected P, original-manifest lineage and answer-free `pool-metadata.json`; no pool bodies in repo | Curator/private access; AC-1; CHK-01/03 | Confidentiality/freshness; may parallel TASK-02 only before dispatch; curator attestation and any transfer/permission review |
| CUST-TASK-02: selected-host boundary proof | Exact host/account/control/copy inventory; separately authorized non-final assigned-marker/denial receipts | Selected protected host actually available; AC-2/3; CHK-02/04 | Security/permission setup; parallel TASK-01; explicit setup Human Review |
| CUST-TASK-03: versioned private adapter/input binding | New private `protocol.py`/`consumer.py`/`campaign_support.py`, new `dispatch_case.py`, frozen policy/schedule and host execution manifest; SOURCE_NAMES/source manifest cover all eight Python executables. Put schemas in protocol, validate input_authority in Budget, register/resolve authenticated tickets in its journal, enforce raw/canonical/native bindings inside Consumer before reservation, materialize pinned native objects, derive families from G, enforce export release records and remove old live free-argv CLI. Migrate all active callers and six lifecycle regressions without legacy grant/input fallback | Exact code scope approval; preserve v2r1 as immutable baseline. AC-3/4; CHK-04/05/06/07/09; original cap/journal/unknown invariants and no protocol/limit fallback | Authority/transport boundary; public-marker offline development independent of pool bodies; Human Review before deployment; no in-repo runtime export |
| CUST-TASK-04: real admission and continuation | New locality/source/readiness/G/quota/native/ticket/canary records, then existing FP-TASK-003–005 evidence | TASK-01–03 and every real admission gate; AC-1–5; CHK-01–10/FTEST-01–08 | Provider/privacy/spend; sequential timed execution; human scores/audit, exact confirmation subset and final acceptance remain separate |

**Review focus:** late-bound handoff/replacement inputs without grant mutation; validation-before-read/reserve; complete executable coverage after relocation; host management and capture copies; raw-output/side-channel export; role-overlap blinding; zero-dollar binding to the actual protected-host credential; pre-canary readiness versus completed role qualification. Each belongs to the named checks/tasks above, not a vague implementation follow-up.

**Planning done:** both designs and implementation deltas are explicit; current interface assumptions are exercised or marked unverified; docs/navigation checks pass. **Operational done:** only after real CUST-CHK/FTEST evidence and applicable human gates pass. This plan has no completed host, pool, ticket issuer, native adapter or blinded-score claim.

## Risk gate, recovery and stopping

- **Stakeholders / assets:** existing seven human owners; pool/oracle secrecy, role blinding, preserved evidence, credentials and authorized USD 0 boundary.
- **Threat model / worst case:** coordinator control, candidate tools or raw-output export recover a final/oracle or trigger unauthorized provider work; disclosure cannot be rolled back by deletion.
- **Assumption audit / evidence check:** physical host/pool availability, real access exclusions, actual input-issuer authentication and human blinding are unknown. Source/CLI evidence above supports the chosen boundaries and required deltas, not admission.
- **Authority / tool boundary and sink inventory:** this turn may write plan/discovery/report/index and run bounded zero-model interface/record checks only. Protected storage, host accounts/services, credential transfer, provider/network/native execution, publication and memory/policy changes remain outside this planning grant.
- **Unattended envelope / bounded execution:** none selected. Later invocation is one preauthorized role at a time inside the original immutable phase limits; the adapter cannot self-advance, change the envelope or release a human decision.
- **Effect recovery decision / failure modes:** owner checks the existing Budget/call/native receipts before any continuation. Any possibly dispatched request, pending ledger, crash or unconfirmed cleanup holds as `OUTCOME_UNKNOWN`, `retry_safe: false`; repeated calls are not a recovery mechanism. The approver/capture operator owns reconciliation at the next manual gate; no new dispatch while unresolved, within the existing phase ceiling.
- **Safe dry-run:** separately approved public/non-final markers on the exact future host/adapter; actual same-profile positive/negative capabilities, raw export and accounting observations. Synthetic local checks are only development evidence.
- **Rollback plan:** preserve sealed originals, raw receipts and old sources; remove only newly owned authorized disposable resources after evidence capture. No restore/edit of operator stores or old cohorts. Exposure holds eligibility for a revised pre-output decision.
- **Audit log plan / durability:** protected append-only receipt lineage, frozen parent identities and source/copy owners; bounded allowlisted exports. Missing authoritative bytes, changed source/configuration/principal or noninventoried copy invalidates readiness; no generic durability promise.
- **Human Review Required / Human Approval Gate:** exact host/provisioning, transfer/permission and new private implementation/deployment scope need explicit approval; existing campaign authority and Go observation are not asked again. Actual scorer qualification/freeze/audit, exact confirmation subset/envelope and outcome acceptance remain human-controlled.
- **Go / no-go:** GO for this decided plan and source-only compatibility checks; NO-GO for asserting custody/admission or dispatch from the design alone. All seven campaign obligations and old accepted-inconclusive 334-call/12-reserve/USD 0 accounting remain unchanged.

## Candidate Adoption Ledger

| ID | Decided design | Status / authority limit | Next owning action |
|---|---|---|---|
| CUST-D1 | Independent protected Apple Silicon host; coordinator receives metadata only | Selected by delegated design authority; availability/setup unverified, no provisioning permission | Execute TASK-01/02 only under their actual setup/curator authority |
| CUST-D2 | Existing-pool projection plus bounded private dispatcher and per-session tickets | Selected plan; code/deployment unimplemented and separately gated; not a skill/runtime adoption | Review/authorize exact TASK-03 implementation scope before editing sources |

## Falsifiability

Reject this design's claimed readiness if an actual coordinator capability recovers a protected marker, a worker obtains another case/oracle, a forged/late-bound ticket bypasses allocation/input checks, the same immutable phase grant cannot support real Q-HOF handoffs, or an export reveals an arm/final before its permitted gate. Stop and preserve evidence; do not reinterpret a marker, weaken FTEST-01–08, change the denominator or call missing proof a pass. A host that cannot satisfy the unchanged six-store/eleven-file/capture contract remains inadmissible; any proposed replacement criterion needs an explicit versioned pre-output protocol decision, not a fake store or silent exception.

## Advisory review and disposition

### Panel Consensus

Two read-only lenses reviewed working spec v2 against the frozen preregistration
and current v2r1 source: `CustodyBoundaryReview` and `DispatcherBindingReview`
(including its FTEST-02/05 addendum). Both returned **AGREE WITH CHANGES**.
Recommendation: use the corrected v3 **plan**, not deploy/admit from this record.
The coordinator resolved the findings below; no independent v3 operational pass
or extra human/provider qualification is claimed.

### Required Wording Changes

| Review finding | Current v3 disposition / verification owner |
|---|---|
| Dispatcher F1: adapter-only trust leaves direct API/read-time/native gaps | Consumer enforces authenticated tickets and raw/canonical/native identities before reservation; CHK-05, TASK-03 |
| Dispatcher F2: issuer/schedule/relationship predicate missing | Physical issuer-owned directory/file + trusted journal registration, bound schedule/policy and distinct producer/replacement fields; CHK-05/06 |
| Dispatcher F3 + Custody F2: session export conflicts with pre-freeze rule | Phase-only export without a verified G-bound freeze/audit/human-release record; CHK-07 |
| Dispatcher F4: incomplete file/caller/native cutover | Protocol schemas, closed source inventory, Budget grant validation, pinned native construction, grant-derived families and explicit old CLI removal/caller migration; TASK-03 |
| Dispatcher F5: unexplained extra verifier | Existing artifact/leak-audit owners under recorded overlaps; no eighth human or inferred independence |
| Dispatcher correction 6: matched-construction location undefined | Ticket issuance checks C-null/T-full target and pair-common setup; actual payload/discovery/memory comparison remains FTEST-02 |
| Custody F1: provider-account and credential-residue channels omitted | P and CHK-02/03 include reachable provider records and credential copies; accepted opaque internals are not claimed clean |
| Custody minor / questions: future-copy timing, platform sinks and assurance lineage | Predeclare namespaces, record actual copies as created, inventory platform sinks, rehash P/G lineage before release; missing qualified human endpoints remain null/held |

### Shared Findings

The late-bound handoff problem is real: the existing immutable grant cannot
contain the hash of a later producer output. The current native/CLI limitations
are confirmed by source and the coordinator's zero-model compatibility probe.
Unchanged Budget accounting, five-canary admission, no-retry unknown outcomes
and separate human acceptance remain safety floors.

### Disagreements / Residual Risks

No architecture disagreement was reported. The suggestion that the credential
have only one recoverable copy is narrowed to **inventoried owner-protected
copies**: legitimate protected backups are not forbidden, but coordinator access
still holds admission. A journal alone does not independently authenticate its
writer; actual host/control evidence is mandatory. Unobservable provider internals
and absent qualified human scoring remain the already-declared limitations, not
mechanical passes or silently reduced endpoint requirements.

### Evidence Actually Checked

Lenses read source/contracts only; they ran no code. Main ran the current CLI
help and two source-bound compatibility controls, verified all seven current
source hashes and the original manifest, and retained the initial harness-input
failure separately. `local/df-c2-custody-plan-2026-10-15.ddeQjU/probe-preservation.json`
binds the observations/driver before disposable scratch/driver removal.
Final repository/navigation checks are recorded after execution.

