# Agentflow 8.4.1 — Delta Survey — 2026-09-30

> **Status: decided — nine upstream candidates not adopted; one local recipe correction adopted (AF841-M1); no skill, routing, permission, dependency, or runtime change.** The delta starts at the 8.3.3 baseline `738d0b3f4aa1df870835813d9dcc015136628434`, recorded in the [2026-09-28 factory rethink panel](software-factory-rethink-panel-record-2026-09-28.md), downstream of the [8.3.2](agentflow-8.3.2-delta-survey-2026-09-22.md), [8.3.0](agentflow-8.3-delta-survey-2026-09-21.md), [8.2.0](agentflow-8.2-delta-survey-2026-09-13.md), and [2026-09-05](agentflow-survey-2026-09-05.md) surveys. The user authorized worthwhile doc/skill updates, not automatic promotion. The span carries 8.3.4, 8.4.0, and 8.4.1; the requested 8.4.1 patch itself is documentation/metadata-only. Existing guards cover the doc repair; no new paragraph-pin test is added.

## Research Question and Scope

User instruction: "Fix advisor notes; Survey agfnow/agentflow v8.4.1; Survey https://github.com/google-research/rrsi; and if worth it then update docs or skills" (checked 2026-09-30). Which changes since the recorded 8.3.3 pin alter the methodology, which are host implementation or relocated prose, and does any concept expose a **verified local gap**? The conditional update direction permits a narrow worthwhile repair; it does not supply evidence that an upstream candidate's named promotion trigger fired.
Scope: resolve the immutable 8.4.1 identity from tags/commits/file
version/changelog (never assume current main — main is already 8.4.2);
inventory the **full 8.3.3→8.4.1 delta**, not only the newest patch; scope
8.4.2 as later identity/date context only; inspect notebook
ownership/permissions, closeout, worker/reviewer authority, and model/default
changes where actually present; separate prose, enforcing code, host
verification, and author preference. Failure: substituting current main for
8.4.1, reporting author benchmark numbers as replicated, or treating source/CI
presence as efficacy.

## Direct Recommendation (as of 2026-09-30)

- **Study — the goal-vs-method split and the review-only bounded checker.**
  The 8.3.4 host-obligation rewrite tells the host to infer outcome/user/
  success/limits, **distinguish those from a proposed method**, and stop an
  unsafe or infeasible method; the requirements advisor records any material
  goal–method gap with consequence plus an evidence-backed alternative **for
  the host to discuss, never silently promoted into a requirement**. The
  review-only closeout path is the same honesty instinct in enforcing code: a
  deliberately bounded intent matcher (unknown prose cannot authorize the
  exception), a captured Git baseline, a SHA-256 report binding, and a ban on
  replacing an existing file with review evidence. Both are clean external
  corroborations of TeaPrompt's evidence-tier and trust-boundary discipline —
  executed in host code; no qualifying local skill-contract gap was established.
- **Reproduce — bounded (settings boundary + CLI containment).** Two sandboxed
  native probes at the requested pin (below): template defaults
  (`notebook-ownership: off`, `threeways: better`), validate exit 0, bogus
  ownership rejected, `threeways: off` fails validation, `agf review` usage/
  outside-project refusal. Review-decision semantics themselves were not
  exercised (needs a full notebook fixture; upstream's own
  `review-only.test.js` covers that in-source and formal suites are parent's
  gate, skipped here). Every other behavior is source-tier at the pin.
- **Adopt — no upstream mechanism; repair one local recipe sentence.** Nine upstream candidates remain unadopted: three methodology corroborations, four host-runtime references, and two vendor-policy dispositions. AF841-M1 corrects the recipe's attribution of oracle sealing to the contract generator; the host owns enforcement. This is a documentation repair under the user's conditional direction, not adoption of Agentflow runtime behavior.
- **For citers:** 8.4.1 is now a **real git tag** (`v8.4.1` →
  `ab80a4db168742042afec790c5b446c745499ab4`), unlike all prior surveyed
  "versions," which were file labels with empty tag lists. Config schema stays
  **8**. License unchanged (Apache-2.0). The 8.4.1 release changes no user
  settings (changelog says so; the model-name edit touches README templates
  only). Speed/Windows claims for the new changes are explicitly **unproven**
  by the author's own changelog — not replicated here.

## Version and Source Identity

Checked 2026-09-30 (all identities from `git ls-remote` + local tag fetch):

| Identity | Observation | Tracking point |
| --- | --- | --- |
| Baseline (8.3.3) | `738d0b3f4aa1df870835813d9dcc015136628434`, 2026-09-22 ("release: agentflow @ a874dc0") | Bound by the 2026-09-28 panel record |
| 8.3.4 | `df6e7cac7e74e204ff07c0eb3d14a374ceac7dfd`, 2026-09-29 ("release: agentflow @ 14d636f") | Intermediate; read via diff |
| 8.4.0 | `d7310d7455159ff5c7593fbf931bc451c4000b3a`, 2026-09-30 14:10 +0800 ("release: agentflow @ a9b89e1") | Intermediate; read via diff |
| **Requested 8.4.1** | **`ab80a4db168742042afec790c5b446c745499ab4`**, 2026-09-30 15:49 +0800 ("release: agentflow @ 4e122a4"); `v8.4.1` tag → this commit; `plugin.json`/`README`/`SKILL.md` all read `8.4.1` | **Recheck `main`/tags before any later reliance** |
| Later 8.4.2 (context only) | `a20951b051822a38ba9b7bbe97c6152f28a0fe6f`, 2026-09-30 15:59 +0800; model-tier value changes + one `writing.md` line | **Not** the requested version; no behavior claimed from it |
| Upstream `main` | `a20951b` (i.e. 8.4.2) — ahead of the requested pin | Never substitute for 8.4.1 |
| Config schema | **8 — unchanged** across the whole span | Separate from the release version |
| License | Apache-2.0, unchanged (`LICENSE` diff empty) | Concepts restated in original prose |
| Delta size 8.3.3→8.4.1 | 62 files, +1643/−364; 8.4.0→8.4.1 alone is 5 files, +16/−8 (docs only) | Bulk is host scripts + tests |

Primary sources (immutable at the pins; checked 2026-09-30): [v8.4.1 tag](https://github.com/agfnow/agentflow/tree/v8.4.1),
[8.4.1 commit](https://github.com/agfnow/agentflow/commit/ab80a4db168742042afec790c5b446c745499ab4),
[`docs/CHANGELOG.md` @ 8.4.1](https://github.com/agfnow/agentflow/blob/ab80a4db168742042afec790c5b446c745499ab4/docs/CHANGELOG.md),
[`SKILL.md` @ 8.4.1](https://github.com/agfnow/agentflow/blob/ab80a4db168742042afec790c5b446c745499ab4/skills/agentflow/SKILL.md) (checked 2026-09-30),
plus per-release diffs read locally (`738d0b3..df6e7ca`, `df6e7ca..d7310d7`, `d7310d7..ab80a4d`, and `ab80a4d..a20951b` for 8.4.2 scope only).

## State Ledger and Changed Mechanisms

Entries are source-tier at the pin except the two sandboxed probes below.
"Author-claimed" = changelog/prose behavior text; "enforcing" = shipped code
that refuses/throws on violation.

### 8.3.3 → 8.3.4 (host hardening + obligation rewrite + review-only path)

| Change | Evidence at the pin | Status / limit | Disposition |
| --- | --- | --- | --- |
| I-062 host-obligation rewrite: infer outcome/user/success/limits, distinguish from method, challenge mistaken/unsafe/ineffective/complex methods, stop unsafe-or-infeasible, ask only on remaining material owner choice; no silent goal change | `SKILL.md` Scope-and-evidence diff | Verified source delta; prompt text | AF841-1, no change (held) |
| Scope-discipline rewrite: "authorized outcome and constraints"; host recommendation alone authorizes nothing; implementation wish may authorize file choice without naming files; material-choice hatch | `SKILL.md` diff | Verified source delta; prompt text | AF841-2, no change (held) |
| Acceptance advisor: `Outcome: BLOCKING` when a conforming implementation still cannot achieve the accepted goal in an ordinary user journey | `references/advisors/acceptance.md` diff | Verified source delta; prompt text | AF841-3, no change |
| Requirements advisor: record material goal–method gap + consequence + evidence-backed alternative; never silently promote it | `references/advisors/requirements.md` diff | Verified source delta; prompt text | Folds into AF841-1 |
| `agf review` read-only precheck (`--notebook`, `--host`, inside-project containment, usage errors) | `agf.js` `review_main` (absent at 8.3.3: `grep -c review_main` = 0; present at 8.3.4: 3; positive control holds) | Verified source delta + sandboxed run | AF841-5, record-only (host) |
| Review-only completion: `purpose: review-only` + `report_sha256`, truthful BLOCKING/UNRESOLVED closeout, bounded `review_only_intent` matcher, Git-baseline + no-replace guards, plain-stamp equivalence, host-attributed dispatch-record fallback | `closeout.md`, `round-linter.js`, `review-only.test.js` (+160), `review-only-journey.js` | Verified source delta; enforcing code read, semantics not executed here | AF841-4, record-only (host) |
| `pipeline-roles.threeways` tier role (default `better`, rejects `off`, no silent downgrade) | `ag.md`, `delegation.md`, `ag-settings.js` (18 `threeways` hits at 8.3.4 vs `notebook-ownership` count 0 — absence with positive control) | Verified source delta; vendor-tier half + no-downgrade half | AF841-7, rejected class |
| Windows portability (#15), hook idempotence (#14), historical RUN/WIP timestamps (#19), `inline-reply: off` delivery-receipt sentence | CHANGELOG 8.3.4; `SKILL.md`; `notebook-owner.js` 8.3-alias guard | Verified source delta; host mechanics | AF841-9, record-only (host) |

### 8.3.4 → 8.4.0 (optional notebook ownership)

| Change | Evidence at the pin | Status / limit | Disposition |
| --- | --- | --- | --- |
| `notebook-ownership: on\|off`, optional, defaults `off` incl. when absent; off skips owner checks/metadata but retains locks, safe paths, current-Ask checks, snapshots, routing; policy-change-during-op aborts; rename publication refused on settings drift | `SKILL.md`, `streams.md`, `looper.md`, `AG_GUIDE.md` + `.zh-tw`, `scripts/README.md`, `ag-settings.js`, `notebook-owner.js`; new `ownership-controls.test.js` (+171) + journey | Verified source delta; defaults + rejection paths sandboxed; full semantics not executed | AF841-6, record-only (host) |

### 8.4.0 → 8.4.1 (documentation only)

| Change | Evidence at the pin | Status / limit | Disposition |
| --- | --- | --- | --- |
| Codex coordinator recommendation `gpt-5.6-sol/low` → `gpt-6.1-sol/medium` (README EN + zh-tw, model name + effort + link; grammar fix "we recommends" → "we recommend"); release reminder to compare rendered READMEs; version labels | 5-file diff; CHANGELOG "This does not change user settings" | Verified source delta; prose only | AF841-8, rejected (vendor policy) |

### 8.4.2 (later identity/date context — not requested-version behavior)

8.4.2 (`a20951b`, 15:59 +0800, ~10 min after 8.4.1) retunes worker-tier
template values (`gpt-6.1-sol/high`, `gpt-6.1-sol/low`, `gpt-6-luna/high`),
touches one `writing.md` line, and bumps labels. Scoped here to identity/date
only; no 8.4.2 behavior is claimed or dispositioned.

## Candidate Adoption Ledger

The user permitted worthwhile doc/skill updates. Each upstream row still needs a verified local gap or its named reopening evidence; none was established here. IDs are AF841-* (no collision with AF/EP/AF82/AF83/AF832/SFR); AF841-M1 is the separate local documentation repair.

| ID | Candidate | Status | Evidence / local gap | Reopen trigger / falsifier |
| --- | --- | --- | --- | --- |
| AF841-1 | I-062 rewrite: infer outcome/user/success/limits; method-vs-goal split; stop unsafe/infeasible | No change | Held: `01-thinking/counterargument` (attack plan, lower-cost alternative, minimum viable) + `reflective-risk` stop rules; independent arrival is corroboration | A local case where installed text authorizes acting on a method that cannot achieve the stated goal |
| AF841-2 | Scope rewrite: authorized outcome/constraints; host recommendation authorizes nothing; wish may choose files | No change | Held: AF-2 (finding ≠ authorization), AF82-9 (question ≠ authorization), implement scope; the "wish may choose files" narrowing is consistent, not a gap | A local scope-widening via a host recommendation treated as authorization |
| AF841-3 | Acceptance `Outcome: BLOCKING` on goal-mismatch in an ordinary journey | No change | Methodology-shaped but prompt text; acceptance authority lives in `governed-delivery` gates; no local literal-implementation case | A local case where a conforming-but-goal-missing delivery passed a gate |
| AF841-4 | Review-only truthful closeout (bounded intent, baseline, SHA-256, no-replace) | Record-only (host) | Host closeout machinery; corroborates evidence-integrity + honesty-about-limits; TeaPrompt runs no review-record store | A user directs review-record scaffolding for a stateful agent (gated) |
| AF841-5 | `agf review` read-only precheck | Record-only (host) | Host CLI; containment + usage sandboxed below | Runtime remains a Standing Non-Goal |
| AF841-6 | `notebook-ownership: on\|off` default off + policy-drift guards | Record-only (host) | Runtime concurrency/lease option; lease parallels stay in `agent-governance-scaffold`; novelty alone per parent fires nothing | A user directs shared-notebook lease scaffolding (→ pack lease semantics, gated) |
| AF841-7 | `threeways` tier role; no silent downgrade on unavailable tier | Rejected (tier class) / held (no-downgrade half) | Tier values are vendor policy (AF82-7/AF83-7 stand); no-downgrade held by dispatch R4 + silent-downgrade semantics | Only the original named triggers reopen the tier rows |
| AF841-8 | Coordinator recommendation `gpt-6.1-sol/medium`; template tier values | Rejected | Vendor/operator policy; 8.4.1 changes no user settings by its own changelog | Only a named model-policy trigger reopens |
| AF841-9 | Windows portability, hook idempotence, timestamp tolerance, delivery-receipt sentence | Record-only (host) | Host mechanics; receipt sentence restates EP-1-adjacent packet-as-record substance | A local irreversible-cleanup or dropped-evidence case, not an upstream fix |
| AF841-M1 | **Local follow-through, not upstream adoption:** Factory recipe #2 attributed oracle sealing to governed-delivery, contradicting the pack's Methods/Never/Host Preconditions and recipe #4 | Adopted in place 2026-09-30 — docs-only | [Recipe](../04-agent/workflow-recipes.md#factory-composition-rules) now declares the oracle split, owner, host seal and change protocol; the host enforces the seal. No skill/pack/runtime change; SFR gates and R8 hold preserved | Reopen if a consumer attributes actual sealing to TeaPrompt again, or a future host integration changes the declared preconditions; repair that owning surface, not the core routing set |

Recurrence is `unknown`; three upstream releases are not local recurrence.
Prior AF/EP/AF82/AF83/SFR rows, pins, dates, and adopted sentences are
unchanged; ECT-2/4 (noise vs improvement; repeated selection vs untouched
final data) stand as parent-reported context, not re-litigated here.

## Evidence Actually Checked

- `git ls-remote` HEAD/main/tags (2026-09-30): HEAD = main = `a20951b`
  (8.4.2); `v8.4.1` → `ab80a4d`; `v8.4.0` → `d7310d7`; `v8.3.4` → `df6e7ca`.
  Local tag fetch confirmed all four pins with dates/messages.
- Per-release diffs read: full `738d0b3..ab80a4d` stat (62 files,
  +1643/−364); prose diffs (`SKILL.md`, `closeout.md`, `ag.md`,
  `delegation.md`, `streams.md`, `looper.md`, advisors, guides, READMEs);
  code diffs (`ag-settings.js`, `agf.js` `review_main`, `notebook-owner.js`,
  `round-linter.js` review-only path); `LICENSE` diff empty; schema
  `const schema_version = 8` at the pin; absence-with-control
  (`notebook-ownership` 0 hits at 8.3.4 settings vs present at 8.4.1;
  `review_main` 0 at 8.3.3 vs 3 at 8.3.4).
- Installed-surface mapping: `01-thinking/counterargument.md` acceptance
  criteria (lower-cost alternative, minimum viable) re-read; prior ledger
  rows cited, not re-derived.
- Not done: formal suites/lint/builds (parent's gate); review-decision
  end-to-end semantics; live hosts/providers; private source builds
  (`14d636f`, `a9b89e1`, `4e122a4` uninspected); 8.4.2 behavior.

### Local Documentation Repair and Consumer Map

The parent observed the incorrect sealing attribution before editing and changed only Factory Composition Rule #2. The [delivery contract](../skills/governed-delivery/SKILL.md#host-preconditions) already assigns sealing to the host. The repair preserves the existing unversioned-spec/unlocked-manifest stop and executor immutability requirement; no new guarantee is introduced.

| Consumer class | Coverage / boundary |
| --- | --- |
| Direct recipe reader | Corrected in place; run-note consumer smoke uses the actual recipe and delivery contract |
| Core skills, domain packs, installed entry points | Intentionally unchanged; their existing host-enforcement boundary is already correct |
| Generated discovery index | Rebuilt after integration; includes the edited recipe |
| Fixtures, persisted adoption rows, exact-string guards | Prior AF/SFR/RS-4/FM3/JL-9/XM-3 dispositions unchanged; existing affected checks run in the final repository gate |
| Documentation / decision trail | AF841-M1, this record, case ledger and Decision Index track the local repair separately from upstream candidates |

One stateless completion consumed the actual edited recipe and delivery contract; both saved inputs were checked against current repository bytes. Three synthetic run notes were classified correctly: declared seal fields without host observations → sealing unknown; an observed write-denial receipt with answers readable → sealing met but read isolation unmet; executor self-report alone → both unknown. All remained `artifact-complete` because the other host preconditions lacked evidence. **3/3 boundary cases passed**, saved in `local://af841-recipe-consumer-smoke.json`. This is sampled recipe consumption, not measured improvement, general adherence or host enforcement. Final repository commands/results are reported after integration.

## Native Smoke (observed at the requested pin)

Isolated scratch `/private/tmp/af841-smoke` (archived `ab80a4d` scripts
only; disposable). Both probes ran `env -i PATH=/usr/bin:/bin:/opt/homebrew/bin
HOME=<scratch> TMPDIR=<scratch>` under `sandbox-exec` (network denied,
`/Users` reads denied, writes confined to scratch). Node v25.1.0.

Probe 1 — settings boundary (`ag-settings.js` at 8.4.1):

```text
template notebook-ownership = "off"
template threeways tier = "better"
init done; ag.json present = true
valid ag.json for codex
validate template exit = 0
notebook-ownership: off → on
set ownership on exit = 0
bogus ownership rejected: "settings change rejected: configuration.switches.notebook-ownership must be one of on, off"
notebook-ownership: on → off
threeways-off errors = ["configuration.pipeline-roles.threeways: off is not supported"]
EXIT=0
```

Probe 2 — `agf review` containment (`agf.js` at 8.4.1, same sandbox):

```text
help exit = 1 | review listed = true        # --help renders usage incl. review line (exit 1 = usage-render convention)
review exit = 1 | msg = "review precheck failed: completed round has no Ask identifier for its review decision"
outside-notebook exit = 1 | msg = "review precheck failed: notebook must be a regular file inside the project"
unknown-subcommand exit = 1 | names it = true
EXIT=0
```

What this establishes: template defaults and validate-accept at the pin (positive controls), unsupported ownership and threeways values rejected by their validators, and the review entry refusing an outside-project path, an unknown subcommand, and an unready notebook. The ownership option arrived in 8.4.0; threeways arrived in 8.3.4. This does **not** establish review-decision correctness, ownership concurrency, Windows behavior, or efficacy. No hooks were installed or workers launched. Executed source wrote only inside scratch, which was removed after recording.

## Evidence vs Inference

- **Observed:** tag/commit identities and dates; per-release diff text and
  line counts; schema 8; Apache-2.0; both smoke transcripts above with exits.
- **Author-claimed / unexercised:** ownership mixing and full concurrency behavior, review-only truthfulness, hook idempotence, native Windows verification, and the "most stable coordinator" model recommendation. The changelog marks startup-speed gain and native Windows execution of the new changes **unproven**; no improvement was measured here.
- **[INFERENCE]:** that the span is "host-dominated with held methodology
  prose" — from changed-file families and the mapped local coverage, not from
  executing each path.
- **Unknown / not done:** recurrence; private source revs; full-suite status
  (two pre-existing skill-size/wording assertions remain unresolved per the
  changelog); live providers/hosts; 8.4.2 behavior.

## Falsifiability

- Wrong if any pin identity, date, schema-8, tag-exists, or "8.4.1 is
  docs-only" fact is misread — all are quoted from tags/commits/diffs at the
  pins above.
- Wrong if any AF841 row's "held" claim fails: the counterargument acceptance
  criteria, AF-2/AF82-9 scope sentences, or dispatch R4 no-downgrade text does
  not say what is cited — each is named to the file.
- Wrong if a recorded "host" row enforces a methodology duty TeaPrompt
  surfaces lack and a local case needs — that case, not this survey, reopens
  the row.
- AF841-M1 reopens if the recipe again attributes actual sealing to a TeaPrompt contract generator, or the contract's host-enforcement precondition changes. A successful generated artifact alone does not falsify the need for host evidence.

## Residual Risks

- Upstream default-off ownership normalizes mixed-session notebooks; if a
  future TeaPrompt surface ever leans on Agentflow notebooks, the lease
  assumption must be re-pinned — currently no such surface exists.
- The `threeways` role and model-template values will keep churning with
  vendor releases (8.4.2 already did); pin, don't track.
- A reported unavailable check is not a negative result: unrun semantics
  (review-decision, concurrency, Windows) stay unknown, not passing.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Immutable 8.4.1 pin resolved from tags/commits/files/changelog, main-ahead noted | done | Version and Source Identity |
| Full 8.3.3→8.4.1 delta inventoried per release; 8.4.2 scoped to context | done | State Ledger and Changed Mechanisms |
| Nine upstream candidates and one bounded local documentation repair decided | done | Candidate Adoption Ledger; AF841-M1 |
| Conditional doc/skill direction preserved without automatic mechanism promotion | done | Scope and local consumer map; no skill/runtime change |
| Sandboxed native smoke with positive + adversarial controls | done | Native Smoke |
| Owned upstream-probe scratch removed; no installation, worker launch or commit/push | done | Native Smoke; repository edits limited to the local documentation repair and survey/decision records |

## Latest-version refresh — 2026-10-22

Scope: latest default-branch and release/tag identities for `agfnow/agentflow` and the separate project `kunchenguid/firstmate` (Firstmate is its own survey object, not an Agentflow component). Two baselines are distinguished: this durable record's 8.4.1 pin, and a chat/session-only 2026-10-05 survey pinning Agentflow v8.4.14 and Firstmate `f470a01` without a repo record. Source/ref inspection only; no builds, tests, smokes, installs, commits, or adoption changes. All prior AF/AF82/AF83/AF841/SFR dispositions and AF841-M1 stand.

### Agentflow: prior baselines and latest identities

| Identity | Observation |
| --- | --- |
| Durable-record baseline | `v8.4.1` → `ab80a4db168742042afec790c5b446c745499ab4` (2026-09-30), config schema 8, Apache-2.0 |
| Chat-history baseline (session-only, 2026-10-05) | `v8.4.14` → `d0a6dd0a00d2d0914c900a0a5851764b32b50fb1` (2026-10-05); covered the 8.4.1→8.4.14 span (notebook archiving, inline-request recovery, message controls) with isolated CLI probes; no repo file changed |
| Latest checked `main` | `80fcd7f81e21b2c1cbcaeda53a40a0ede8fcab1d` (2026-10-09, "release: agentflow @ de0a13c") via `git ls-remote` |
| Latest release/tag | `v8.4.15` → tag object `a4642eb32b61cf3ef3ffa736180028a9442d9822` → commit `80fcd7f` (published 2026-10-09); `main` == `v8.4.15`, no ahead commits |
| Version split | Release 8.4.15; config schema still 8 (`schema_version = 8` at the latest pin); `plugin.json`/`SKILL.md` read 8.4.15; license Apache-2.0 |
| Delta since 8.4.14 | 25 files; branch/tag/release refs all queried 2026-10-22, no newer public release found |

### Agentflow: 8.4.14→8.4.15 change families (actual diffs read, not only notes)

1. **Claude prompt-capture downgrade to manual (#27).** `UserPromptSubmit` cannot reliably identify generated messages, so setup now removes owned Claude prompt hooks, `stop-hook.js` silently ignores stale Claude prompt calls (early `return 0`), Stop enforcement stays, and Codex automatic capture is unchanged. Startup reports `session_id` plus manual-capture instructions for Claude. The SKILL.md every-message rule now scopes automatic capture to Codex. This narrows a former automatic host mechanism to a manual owner step on one host; it does not change TeaPrompt methodology coverage.
2. **Init refuses damaged established notebooks (#28).** `init_main` validates an existing notebook (STATUS region, status block, open final Ask) before host detection or setup writes, and refuses reconstruction with restore/repair guidance. Additive fail-closed guard; host mechanics.
3. **Notebook-compact keeps the latest completed round even under force.** The archive loop now stops before the latest round with reply text (`findLastIndex`), so forced compaction retains one completed round beside the current Ask. The prior finding stands: `--include-answered true` still accepts only the literal `true` and still performs no mechanical check that the request was handled (latest `notebook-compact.js:88-181`); the added message text only advises verifying answers first.
4. **zh-TW setup fallback parity (#29)** plus version labels, changelog, and 8.4.7-template `away-gates` default flip in `ag-settings.js` (`off` → `on` in the host template; the persisted/absent default documented at 8.4.5 stays `off` unless explicitly set — template value vs documented default, not a behavior re-verification).

Effect on prior findings: the 8.4.14 chat baseline's core limits are confirmed at 8.4.15 — the answered-round override still bypasses retention without proving completeness, hash verification still protects bytes not intent, and the author still makes no full-suite-green claim (8.4.15 notes: "Three broader fixtures reproduce on the pre-change source"). No new methodology candidate; no gate fired. Inspected immutable links: [v8.4.15 tag](https://github.com/agfnow/agentflow/tree/v8.4.15), [8.4.15 commit](https://github.com/agfnow/agentflow/commit/80fcd7f81e21b2c1cbcaeda53a40a0ede8fcab1d), [CHANGELOG @ 8.4.15](https://github.com/agfnow/agentflow/blob/80fcd7f81e21b2c1cbcaeda53a40a0ede8fcab1d/CHANGELOG.md), [v8.4.15 release](https://github.com/agfnow/agentflow/releases/tag/v8.4.15). Untested: all runtime behavior (no smoke run in this refresh), live hosts, Windows.

### Firstmate (separate project): prior baseline and latest identity

| Identity | Observation |
| --- | --- |
| Chat-history baseline (session-only, 2026-10-05) | `main` → `f470a01c098c1536d83b802874bd954a2c04b506` (2026-10-04, "speed up remote-job sequence claim cleanup"); releases/tags empty then; no dedicated durable file exists |
| Latest checked `main` | `6eb8b7f8277dc37637e3ba58c2fc461d88dc4ff3` (2026-10-22, "withhold a child's PR-ready line until checks green behind an opt-in flag") via `git ls-remote` |
| Release/tag identity | Still none: `git ls-remote --tags` returns empty and the [releases page](https://github.com/kunchenguid/firstmate/releases) carries no releases (checked 2026-10-22). Commit identity only; MIT license unchanged |
| Delta since baseline | 105 commits, 307 files (+37955/−2132); families below from commit subjects plus pinned source reads |

Change families since `f470a01` (source-tier; no execution in this refresh): (a) **new worker/session adapters** — Commandcode (`bin/fm-commandcode-mod.ts`, harness adapter + verification doc), Polytoken (`bin/fm-polytoken-lib.sh`, adapter + verification doc), Paseo experimental session backend (`bin/backends/paseo.sh`, `docs/paseo-backend.md`, backend smokes); (b) **new forge/review rails** — `forge=external` never-push review rail (`bin/fm-external-review-lib.sh`, `docs/external-review-forge.md`), Forgejo/Gitea via `tea` CLI (`docs/forgejo-tea-integration.md`), Git push guard (`bin/fm-git-push-guard.sh`), review check (`bin/fm-review-check.sh`), PR-thread re-raise and PR-ready withholding behind opt-in flags; (c) **governance tightening** — self-repo boundary (`config/firstmate-role` maintainer opt-in required to publish upstream; `docs/configuration.md`), explicit authority for upstream contributions (#7172), unguarded Herdr lifecycle-brief refusal at spawn behind an opt-in flag, per-home worker tool exclusions; (d) **capacity/observability** — `bin/fm-capacity.sh` (open lanes + host headroom), per-project spawn capacity caps, pipeline spend recording, task-status-history archival, wedge-escalation caps and operator evidence guards; (e) **supervision/compat fixes** — Pi/OpenCode/Grok/Cursor/Opencode adapter fixes, secondmate busy-contract/convergence/relaunch fixes, stale-alarm bounds.

Former limits re-checked at the latest pin and still holding: the lease threat model is still explicitly confused-agent-grade — "A deliberately forging shell running as the same uid ... can evade any in-process discriminator ... adversarial-grade separation is explicitly out of scope" (`bin/fm-lease-lib.sh`); worker launch still defaults to bypass-grade permissions (`CLAUDE_PERMISSION_MODE=bypass` default in `bin/fm-spawn.sh`, `--dangerously-skip-permissions`); the worktree-is-not-a-sandbox boundary stands. Preserved contracts: `bin/fm-brief.sh` still refuses `--yolo` ("it is firstmate's merge authority, not a [worker input]") and still separates Captain's intent from generated spec; delivery-mode vs merge-authority split unchanged in the README. Effect: prior chat findings corroborated, none contradicted; the contract-separation patterns remain study/reference material, the fleet runtime remains non-adopted. Inspected immutable links: [latest commit](https://github.com/kunchenguid/firstmate/commit/6eb8b7f8277dc37637e3ba58c2fc461d88dc4ff3), [README @ latest](https://github.com/kunchenguid/firstmate/blob/6eb8b7f8277dc37637e3ba58c2fc461d88dc4ff3/README.md), [lease threat model @ latest](https://github.com/kunchenguid/firstmate/blob/6eb8b7f8277dc37637e3ba58c2fc461d88dc4ff3/bin/fm-lease-lib.sh), [brief yolo guard @ latest](https://github.com/kunchenguid/firstmate/blob/6eb8b7f8277dc37637e3ba58c2fc461d88dc4ff3/bin/fm-brief.sh). Untested: all runtime behavior; "zero-token watcher" and "restart-proof" remain author descriptions, not verified here.
