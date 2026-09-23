# pstack Survey — 2026-09-22

> **Status: record-only.** The user requested the survey and then explicitly requested documentation and a commit. This authorizes preserving the findings, not installing pstack, changing skills, or operating a runtime. This document is evidence and project analysis, not agent operating policy.

## Research question and recommendation

Evaluate three layers: correctness verification, engineering-quality skills, and agent-friendly architecture. The central lesson is not to persuade an agent to obey a longer prompt. It is to turn engineering judgment into repeatable tools, observable evidence, and enforceable constraints.

pstack combines natural-language policy, project-local skill generation, executable bookkeeping, and host integration. Neither “just Markdown” nor “a complete independently enforcing harness” is accurate. Study the mechanisms; do not infer efficacy from PR volume.

## Source identity and provenance

- Repository: https://github.com/cursor/plugins/tree/53e579f1481697931fc44f5445171397cfa2b24b/pstack
- Commit: `53e579f1481697931fc44f5445171397cfa2b24b`; manifest version `0.15.2`; MIT license. Checked 2026-09-22. Recheck the revision and host dependencies before adoption.
- User inputs: two lossy exports titled “The Complete Guide to pstack” Parts 1 and 2, and “High-Trust AI Agent Architectures: Building a Michelin Kitchen,” containing a summary and purported verbatim transcript. Their session names were paste-1.md, paste-2.md, and paste-3.md. They are not dependencies of this record.
- Original X article URLs were not recovered by two targeted searches. The audio file referenced by the transcript existed, but audio-to-text fidelity was not checked. The transcript spells the handle differently from upstream. Treat attribution and verbatim claims as unverified, not fabricated.
- The guides and talk repeat the same author's claims; they are not independent productivity evaluations.

## Findings

### Correctness: verification as maintained infrastructure

The generator requires Launch, Doctor, Drive, Evidence, Cleanup, and Helpers sections grounded in the target repository. It prefers existing harnesses, real user paths, observable side effects, and evidence that survives cleanup. The Feature Map gives subsequent agents a navigable description of features, entry points, commands and expected observations.

The current contract seeds the top 3–5 features and proves ONE mapped feature end to end. It does not automatically establish full-product coverage. Current generated maps live under `features/`, whereas the supplied guide mentions `references/features/` — resolved 2026-09-22: the external `poteto/verification-skill-example` repo uses `references/features/`; both layouts exist.

Maintenance separates concurrent source readers from coordinator-owned live driving. It distinguishes documentation drift, harness gaps, and product regressions; the last must not be concealed by editing the map. A source-clean feature still needs live exercise. These are prompt-level obligations unless target tools and host permissions enforce them.

### Quality: externalized engineering judgment

The architect workflow grounds current mechanics and rationale, writes caller usage before types, compares structurally distinct designs, and revises a sketch when repeated implementation friction contradicts it. Repeated workarounds are stronger evidence than one awkward edge case. Prototypes answer observable questions; model judgments remain advisory.

This is inference-time procedural guidance, not proof that a model became a software engineer. Compare accepted outcomes, escaped defects, operator active time and total cost under fixed models/tasks. The supplied 2,000/2,462 PR-per-month and 100–1000x output claims lack independently checked baselines and quality outcomes.

### Architecture: constrain the error class, not merely the wording

Recurring corrections can become discriminated unions, import boundaries, canonical APIs, lint rules or runtime invariants. Existing code is also an example agents imitate: remove bad patterns rather than explaining why each copy is exceptional.

“Impossible” must name the invariant and enforcement boundary. An import restriction cannot alone guarantee a renderer stays within 16ms/8ms. The supplied summary overstates that connection; Dune's implementation and performance were not verified.

Do not adopt blanket comment deletion. Upstream has legal, public-API, external-constraint and RFC exceptions, but no-comments step 5 still permits deleting some constraint comments when replacement is not approved. Removing the warning does not remove the risk. Preserve the protection until the constraint is disproved or an equivalent mechanism is verified.

### Automation: bookkeeping is real, acceptance remains separate

The pinned tree contains orch, a PR watcher, bootstrap and other scripts; the plugin is not Markdown-only. The orchestrate playbook explicitly says orch never spawns, waits or wakes agents: the host Task tool does. Its PR+SHA ledger preserves version-specific attestations, not independently established truth.

The dormant benny automation pack requires explicit setup, committed target configuration, adapters and host integrations. Its declared outcome is a draft PR, not merge or deployment. No automation was enabled during this survey.

## Executed evidence

Two read-only scouts extracted distinct source slices. The coordinator spot-read load-bearing primary files, checked the complete upstream tree, and rejected scout overclaims: serialized maintenance does not disprove a productivity multiplier; prompt-only role restrictions are not sandboxes; and the plugin has executable helpers beyond the plan checker.

### Plan checker

Command shape: `node check-plan.mjs <case.txt>`, Node v25.1.0. Inputs were synthetic plans with the required headings, literal verification rule, ten lanes, perf fields and program markers. No application or tests described by the plans ran.

| Input | Exit | Observed result |
| --- | --- | --- |
| Valid structure, no work or evidence | 0 | 1 PR sections, 0 problems |
| Same input with all boxes checked and nonexistent screenshots | 0 | 1 PR sections, 0 problems |
| First lane lacks Pass when | 1 | lane 1 has no pass predicate |
| Lane 10 relabeled Lane 9 | 1 | lanes are [1,2,3,4,5,6,7,8,9,9], expected 1 to 10 |

The checker validates syntax, not evidence existence or semantic correctness. This is a responsibility boundary, not a claim that the checker violates its purpose. Its fixed ten-lane/model wording is not an appropriate universal verification policy.

### Orchestration store

Command: `bun store-probe.mjs`, importing only the pinned store module. No bootstrap, dependency installation, agent dispatch, GitHub command or frontier refresh was invoked. The probe wrote only to a fresh temporary directory.

Observed output:

```json
{"evidenceFileExists":false,"storedVerdictAfterReopen":"live-ui-verified","changedHeadResult":"NOT-VERIFIED","lockRemovedAfterClose":true}
```

A recorded verdict survived reopening; a changed SHA had no verdict; the nonexistent evidence path did not prevent recording a successful verdict. These observations do not certify concurrent writers, crash recovery or whole-host safety.

Reproduction (place the pinned store.ts beside this file and run with Bun in a disposable directory):

```javascript
import {openStore} from './store.ts';
import {existsSync} from 'node:fs';
import {join} from 'node:path';
const dir=join(import.meta.dir,'scratch-store');
const missing=join(import.meta.dir,'never-produced-proof.png');
const oldSha='a'.repeat(40),newSha='b'.repeat(40);
const store=openStore(dir);
await store.init();
await store.ledger.record({pr:1,sha:oldSha,verdict:'live-ui-verified',evidence:missing,verifier:'synthetic-survey-caller'});
await store.close();
const reader=openStore(dir);
const persisted=await reader.ledger.check({pr:1,sha:oldSha});
let changedHead;
try { await reader.ledger.check({pr:1,sha:newSha}); changedHead='unexpected-pass'; }
catch(e) { changedHead=e.message; }
await reader.close();
console.log(JSON.stringify({evidenceFileExists:existsSync(missing),storedVerdictAfterReopen:persisted.verdict,changedHeadResult:changedHead,lockRemovedAfterClose:!existsSync(join(dir,'.orch.lock'))}));
```

### Source integrity

| Executed source | Git blob SHA-1 | SHA-256 |
| --- | --- | --- |
| scripts/check-plan.mjs | 21d350ac155928bbcf8d29dce193a97974f12748 | 4f5118edf719b481983dc87dfadd5b4b5473d05aad04a7ba65191ff9c73faf1b |
| scripts/orch/store.ts | 5e6c602fb670a6b5598977f5bf85d717cf797ef7 | 0eae7cf69282e827b1227166f2e32cee3560f2f3e65b3f1f2faf6fb83d3b4c5b |

Both downloaded files' computed Git blob identities matched the pinned tree. Source inspection and these probes are not end-to-end agent efficacy evidence.

## Candidate Adoption Ledger

| ID | Mechanism | Decision | Evidence / existing surface | Trigger and falsifier |
| --- | --- | --- | --- | --- |
| PS-C1 | Project-local control interface plus maintained feature map | defer target-repository pilot | reflective-implement Verification requires real consumer-surface evidence; does not ship an app-specific adapter/map | A named product and repeated manual driving/context-discovery bottleneck; explicit implementation request. Falsifier: No reduction in operator active time or no improvement in acceptance/escaped-regression outcomes under fixed model and task set |
| PS-C2 | Source/live maintenance separates doc drift, harness gaps and product regressions | concept only; candidate for existing workflow if local failure observed | reflective-implement Verification distinguishes broken check from product failure; local-feedback requests evidence/root cause | A recorded local case wrongly rewrites product or map to satisfy a broken harness. Falsifier: Current workflow already handles representative cases with the same reliable outcome |
| PS-C3 | Repeated corrections become types, import boundaries, lint or runtime invariants | concept only; prefer target-product structural repair over more prompt text | 04-agent/artifact-promotion destinations and verifier/runtime gates; 02-engineering/local-feedback anti-regression rule | A concrete repeated anti-pattern plus a narrow enforceable invariant. Falsifier: Rule rejects legitimate cases or merely moves the failure elsewhere |
| PS-C4 | Usage-first design and empirical prototypes | no new core skill | reflective-spec-plan Workflow step 3; reflective-brief Spike/exploration framing | Specific failure not covered by those contracts. Falsifier: Paired task probe reveals an uncovered design failure |
| PS-C5 | Persistent autonomous execution and effect/acceptance separation | host responsibility; no TeaPrompt runtime adoption | PROJECT_KNOWLEDGE Standing Non-Goals; 04-agent/runtime-trust-boundary §§2a,3 | Explicit direction to implement in a named host plus enforceable authority/effect boundaries. Falsifier: A required operational guarantee remains only prose |
| PS-C6 | Delete constraints without replacement; universal ten-lane/model policy | reject as universal defaults | reflective-minimality Safety Floor and risk-scaled verification in reflective-implement | Only reconsider a bounded rule with failure-specific evidence and approved scope. Falsifier: Replacement preserves the originating protection and fixed overhead improves measured outcomes |

No candidate is adopted into an operating contract. Local recurrence is unknown. Coverage above refers to checked repository-delivered text, not the reviewing host's instructions or provenance-only source links. No tenth core skill, domain pack, dependency or runner is proposed for immediate admission.

## Evidence vs Inference

Separate intent/acceptance, skill-guided execution, controlled product interaction, revision-bound evidence, result evaluation, and authority to merge or deploy. The executor should not silently redefine the criterion it is measured against. Classify product failures, broken checks and unavailable environments separately. Feed recurring failures back into tools, maps and architecture.

The smallest useful next experiment is a named product's control interface and maintained Feature Map, not a new orchestration platform. Hold model, task set and environment constant; compare accepted outcomes, operator active minutes, escaped regressions and total cost with and without those assets. Include failures the verifier must reject, not only successful demonstrations. A pilot is a proposal, not authorized implementation.

Competing perspectives: throughput favors reusable tools; maintainability favors constrained architecture; agent ergonomics favors maps and clear errors; safety requires independent authority and honest unknowns. Blind spots remain the private Dune runtime, full Cursor/cloud integration, transcript authenticity and independently measured quality/productivity.

### Practical pilot: one user journey, not a whole-product harness

Recorded by user direction after clarification of PS-C1. This is an illustrative,
unexecuted experiment proposal, not evidence of local recurrence or permission to
implement it.

Start in a concrete product repository with one meaningful user journey. For a
task-list app, an example is: create a task through the UI, reload, and confirm the
task persists exactly once. This small journey exercises both interaction and
persistence; a screenshot immediately after creation would miss a persistence bug.

Keep two assets distinct:

| Asset | Question answered | Minimum useful content |
| --- | --- | --- |
| Control tools | How can the agent perform the operation reliably? | Launch/readiness, existing browser or API operations, observable completion, evidence capture, cleanup of this run's data |
| Feature Map | Where is the feature, and what should be observed? | Preconditions, user-facing entry point, operation recipe, requirement-derived success/failure observations, known timing or state pitfalls |

Reuse existing browser automation, test utilities, or host tools first. A new CLI
is not required. Wrap only repeated or unreliable steps that justify the extra
maintenance. Wait for an observable completion condition rather than an arbitrary
delay. Use isolated test accounts/data and keep evidence after cleanup.

The map describes navigation and verification, not the whole source architecture.
Its success criteria come from product requirements; observed current behavior is
not automatically the oracle. A broken implementation must not become “correct”
because the agent rewrites the map to describe it.

Try the journey with a fresh agent that has no prior conversation, using the tools
and map as its product-specific context. Check whether it can:

- Complete the journey without the operator supplying missing navigation steps.
- Detect a seeded failure such as a task disappearing after reload.
- Distinguish a product regression from expired authentication or a broken driver.
- Preserve evidence and clean up only the resources the run created.

Success means independent operation and reliable discrimination between success
and failure, not a count of generated skill files. Compare operator intervention
and accepted outcomes against the existing approach before expanding coverage.
Failure to improve those outcomes is a reason to revise or stop the pilot.

Evaluation design for this pilot is recorded in the follow-on synthesis survey
(`plans/pstack-synthesis-survey-2026-09-22.md`, PS2-7): a three-arm controlled
experiment (agent / +pstack / +governance gates) over a matched task set with
ten falsification scenarios (ambiguous intent, protected-test weakening, stale
feature map, mid-run crash, post-effect timeout, SHA change, injected
instruction, repeated failure, unvetted skill promotion, clean delivery) and an
effective-throughput metric (accepted deliverables / total cost including human
intervention and rework). Recorded, not executed at design time — see the
2026-09-22 execution addendum below.

These assets belong with the product whose startup, authentication, navigation and
behavior they describe. TeaPrompt supplies reusable methodology; it does not need
to become that product's control harness.

### Pilot execution addendum (2026-09-22)

Executed at small scale on `TeaEntityLab/wsgiLite.js` (public repo, user-named
scope: johnteee/TeaEntityLab projects only). Assets committed to the product
repo as `VERIFY.md` + `features/` (routing, csrf-upload, errors) — no new CLI;
curl and the existing demo server sufficed.

Two fresh-agent runs, no prior context:

- **Run 1 (uncorrected docs):** 7/14 routes passed; the agent found 7
  map-vs-behavior deviations — a wrong launch directory in VERIFY.md, a
  first-request `undefined` CSRF token (cookie set on the same response), a
  wrong form-field name (`_csrf` vs `CSRF_token`), a header-only `/upload2`
  claim (both header and form field required), a cert-error fast-fail on
  `/timeout`, a `404 File not found.` body prefix, and a real path-traversal
  quirk (`/file/../package.json` serves repo-root `package.json` when launched
  from root). The map was wrong, not the product — the loop caught doc drift.
- **Run 2 (corrected docs):** 15/15 routes passed, zero deviations, negative
  controls confirmed (403 without token, traversal reproduced as documented).

The pilot's own success criteria held: a fresh agent completed the journeys
independently, distinguished doc drift from product behavior, preserved
evidence, and cleaned up. The traversal quirk is a product finding the map now
records rather than hides. This is one product, one agent, one pass — it does
not yet measure acceptance rate, operator time, or escaped regressions at
scale; the PS2-7 protocol remains the design for that.

### Discrimination and A/B addendum (2026-09-22, same day)

Two further experiments on the same product:

- **Failure discrimination (seeded):** a fresh agent on a broken copy
  (`/heartbeat` → `pong`) reported FAIL and classified it **product
  regression**; a second fresh agent on the healthy product with a stale map
  (claiming `pong`) classified it **doc drift**, citing the source
  (`redirect('/heartbeat')` → `ok`), the map's self-contradiction, and the
  repo's correct copy. Both classifications correct — the three-way split
  (product / doc / harness) held under seeded adversarial conditions.
- **Mini A/B (docs vs no docs):** two fresh agents verified the identical
  healthy product. With docs: 19/19 PASS, zero deviations, 4m08s. Without
  docs: 26/26 PASS, 5m58s — all routes still found by reading source, but the
  agent had to reverse-engineer the CSRF dual-token requirement and discovered
  two undocumented quirks the map then absorbed (`redirect()` is internal
  re-dispatch, not HTTP 302; every request without a CSRF cookie gets
  `Set-Cookie` globally). Docs did not change correctness on a healthy
  product; they changed time-to-verify and removed the need for source
  archaeology. On a broken product the map is what makes the regression
  visible.

- **Sealed-oracle contradiction (T01/T02):** a fresh agent on the healthy
  product with a locked `acceptance.yaml` claiming `/heartbeat` → `pong`
  reported FAIL but classified it **spec/oracle error**, not product
  regression — citing the source (`return "ok"` at line 103), VERIFY.md, and
  routing.md as the ground truth. The oracle-vs-product distinction held.

All three discrimination classes (product regression, doc drift, spec/oracle
error) are now demonstrated under seeded adversarial conditions on one
product. The remaining PS2-7 scenarios (ambiguous intent, protected-test
weakening, repeated failure, unvetted skill promotion, clean delivery,
effective throughput) require a named product and explicit authorization for
the full A/B/C protocol.

### Full arm×scenario matrix (2026-09-23)

User authorized the full pilot ("yes for all"). Ten fresh-agent runs on
wsgiLite.js demo copies; seeded bug = `/heartbeat` → `pong` (self-labeled
`// SEEDED BUG` in source — no-docs detection is assisted by the label, a
known limitation):

| Cell | Product | Docs | Locked spec | Result |
| --- | --- | --- | --- | --- |
| A×S1 | healthy | none | none | 26/26 PASS, 5m58s |
| A×S2 | broken | none | none | FAIL heartbeat+heartbeat2 → **product regression**; `/timeout` → **harness failure** (external TLS outage) |
| A×S4 | broken | none | correct | FAIL heartbeat+heartbeat2 → **product regression** |
| B×S1 | healthy | map | none | 19/19 PASS, 4m08s |
| B×S2 | broken | map | none | FAIL → **product regression** |
| B×S3 | healthy | stale map | none | **doc drift** classified |
| C×S1 | healthy | map | correct | 23/23 PASS, 2m49s — fastest arm |
| C×S2 | broken | map | correct | FAIL heartbeat+heartbeat2 → **product regression** |
| C×S3 | healthy | stale map | correct | PASS + **doc drift** flagged; spec corroborated product over map |
| C×S4 | healthy | map | wrong (`pong`) | FAIL → **spec/oracle error**, not product regression |

All four failure classes demonstrated under seeded adversarial conditions:
product regression, doc drift, spec/oracle error, harness failure. Correct
spec + map was the fastest arm; the spec acted as a second oracle that
outranked the stale map (C×S3) and was itself correctly indicted when wrong
(C×S4). Effective-throughput and operator-time metrics remain unmeasured —
single product, single model, single pass per cell.

### Second product: fpGo (2026-09-23)

User directed the same experiment at `TeaEntityLab/fpGo` (generics branch) —
a Go *library*, not a server. The control surface changed shape: `go test
-mod=mod` + scratch drivers via `replace` directives replace curl; the
product's own 1013-test suite is the primary oracle, so the map's job shifts
from defining expected behavior to routing features → `-run` regexes and
capturing environment quirks (the stale `vendor/` requiring `-mod=mod` was
documented and handled cleanly by the agent).

| Arm | Result | Classification |
| --- | --- | --- |
| Baseline (healthy + docs) | 1013/1013 PASS, 1m42s | — |
| Broken — **unlabeled** `Distinct` returns receiver | FAIL `distinct-dedupes` + collections feature | **product regression** — named `stream.go` Distinct, listed TestStreamDistinct/TestFilter/TestStreamSetOperation |
| Wrong spec (`Just(nil).IsPresent()==true`) | FAIL `just-nil-is-present` | **spec-oracle error** — cited `maybe.go` lines + core.md + existing tests |

The unlabeled seeded bug was caught — the wsgiLite self-labeled-bug caveat
does not repeat. Second-product adoption of the pattern is confirmed; the
review trigger in PROJECT_KNOWLEDGE's verification-map lesson has fired.

### Third and fourth products: fpEs + fpRust (2026-09-23)

User extended the experiment to `TeaEntityLab/fpEs` (mocha/`should`, 528
tests) and `TeaEntityLab/fpRust` (cargo, 120 unit + 24 doc tests). Same
three arms each:

| Product | Baseline | Unlabeled seeded bug | Wrong spec |
| --- | --- | --- | --- |
| fpEs (`fp.unique` returns input) | 528/528, 1m39s | **product regression** — `fp.js:148` named | **spec-oracle error** |
| fpRust (`fp::reverse` returns input) | 144/144, 1m41s | **product regression** — `src/fp.rs:297` named | **spec-oracle error** |

Both agents also caught a real doc drift in the generator's own VERIFY.md
(`Maybe.Just` vs `Maybe.just` casing) — the classification table indicted
its own author. Pattern confirmed across four products and three control
surfaces (curl, go test, mocha, cargo). Recurrence + stable I/O + failure
signals satisfied the domain-pack gate: `verification-map-generator`
registered in `plans/validate_skill_examples.py`.

## Falsifiability

The candidate ledger names a falsifier per proposal. In particular, a controlled product pilot that does not improve acceptance, operator effort or escaped regressions defeats the adoption case; a check that accepts deliberately invalid evidence cannot support an independent-verification claim.

## Verification and scope

- Three requested survey themes: addressed with source/claim distinctions.
- Actual execution: plan-checker fixtures and isolated store API probe only.
- Not executed: full plugin installation, target-app driving, cloud agents, Slack integration, PR mutation, merge or deploy.
- No operational skills, routing, governance policy or runtime configuration changed by this record.
- Documentation verification is reported by the recording commit's accompanying delivery message; historical probe results above are scoped to their exact inputs.

## Primary source map

All links below name the reviewed immutable revision, accessed 2026-09-22.

- [.cursor-plugin/plugin.json](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/.cursor-plugin/plugin.json)
- [LICENSE](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/LICENSE)
- [skills/create-verification-skill/SKILL.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/create-verification-skill/SKILL.md)
- [skills/maintain-verification-skill/SKILL.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/maintain-verification-skill/SKILL.md)
- [skills/architect/SKILL.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/architect/SKILL.md)
- [skills/principle-encode-lessons-in-structure/SKILL.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/principle-encode-lessons-in-structure/SKILL.md)
- [skills/no-comments/SKILL.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/no-comments/SKILL.md)
- [agents/comment-sicko.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/agents/comment-sicko.md)
- [skills/poteto-mode/playbooks/orchestrate.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/playbooks/orchestrate.md)
- [skills/poteto-mode/scripts/check-plan.mjs](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/scripts/check-plan.mjs)
- [skills/poteto-mode/scripts/orch/store.ts](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/scripts/orch/store.ts)
- [skills/poteto-mode/scripts/watch-pr/policy.ts](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts)
- [automations/benny/FOR_AGENTS.md](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/automations/benny/FOR_AGENTS.md)
