# Agentflow 8.3.0 — Delta Survey — 2026-09-21

> **Status: decided — record-only; no installed change, no wording adopted.** A
> delta from the [8.2.0 survey](agentflow-8.2-delta-survey-2026-09-13.md) (which is
> a delta from the [2026-09-05 survey](agentflow-survey-2026-09-05.md)), not a
> replacement for their evidence or decisions. The instruction is a **bare
> "survey"**, which under the installed direction-scope rule carries **no adoption
> direction**: candidates are decided with evidence and triggers, and nothing is
> installed. The prior AF/EP/AF82 adoptions were all made under *explicit*
> skill-update direction; none is present here. The 8.3.0 delta is a single squashed
> release commit dominated by **host implementation** (portable hookless-host
> support, a schema-8 `allowed-worker` permission engine, a session-ownership model,
> review-policy, new settings) plus doc/reference prose; its methodology-bearing text
> is already held or is Standing-Non-Goal runtime. Method per the 8.2 coordinator
> reflection: **coordinator-owned top-level diff, no panel, no probing** (nothing is
> drafted, so nothing is probed). Guard: `plans/tests/test_agentflow_v83_delta_record.py`.

## Research Question and Scope

User instruction: "Survey agfnow/agentflow v8.3.0" (repository checked 2026-09-21).
Which changes since the 8.2.0 pin alter the methodology, which are host
implementation or relocated prose, and does any concept expose a **verified gap** on
an installed TeaPrompt surface? A bare survey carries no adoption direction; the
standing bar per candidate is a verified local gap, a named failure the change
defends against, a smaller alternative rejected, and a deterministic guard. Scope:
pin the current source; distinguish new material from previous coverage; record each
disposition and its trigger; preserve every prior gate and adopted sentence; land
nothing. Failure: treating a source recommendation, a squashed release, or a
passing upstream test as local recurrence or as authorization to install.

## Direct Recommendation (as of 2026-09-21)

- **Study — the portability re-scope and its honesty.** 8.3.0 generalizes Agentflow
  from "works with Codex and Claude Code" to "**verified integrations** for
  Codex/Claude plus a **portable core** for any host with file+command tools and
  enough state retention," and is blunt about the boundary: generic hosts get
  `hooks: not_available`, receive no model/effort/permission/identity "by
  inference," and the Limits section states the release "**does not claim Pi,
  Gemini, or OpenCode live verification**." This verified-vs-portable-vs-unavailable
  tiering is the same evidence-tier discipline TeaPrompt records require, applied by
  an external harness to its own capability claims.
- **Reproduce — not done, on purpose.** Bare survey → nothing drafted → nothing to
  probe (per the 8.2 reflection: probe only when a sentence is drafted). Unlike the
  8.2 survey, no CLI was run this pass; every behavior and number here is source-tier
  at the pin. The 8.2 sandboxed CLI evidence stands for that pin only.
- **Adopt — nothing.** Bare survey → DS-1 record-only. Ten delta concepts map to
  installed thinking/minimality/trust-boundary surfaces (held, corroboration) or to
  host runtime (Standing Non-Goal). The one genuinely methodology-shaped addition —
  the "**challenge mistaken, risky, or needlessly complex ideas**" host obligation
  (I-062) — is already the installed `01-thinking/counterargument` lens in substance
  (attack the plan, name a lower-cost alternative, minimum viable version), referenced
  by implement/minimality/review, so it is a corroboration, not a gap.
- **For citers:** GitHub tags and Releases are still **empty** (`[]`); "v8.3.0" is a
  label in `plugin.json`/`README`/`SKILL.md`, not a git tag, and the release is one
  squashed commit whose source build (`9571389`) is uninspected. The config-format
  bump is **schema 7 → 8** (separate from the release version); existing v7 files
  "migrate conservatively." License unchanged (Apache-2.0). Nothing was executed.

## Version and Source Identity

Checked 2026-09-21:

| Identity | Observation | Tracking point |
| --- | --- | --- |
| Previous public revision (8.2.0) | `fcb6878be0b2316cdba5a111f040655f161bfe03` (2026-09-13) | Historical 8.2 survey remains bound to this pin |
| Current public `main` (8.3.0) | `0abf416ccfe10016f16893239bf6c9fd9d4d71e9`, tree `f57233450a1a301a65dafb85be3157de69421fff`, committed 2026-09-21T22:36:59Z; **direct child** of the 8.2 pin (ahead_by 1, one squashed commit) | Recheck `main` before any later reliance |
| Original survey pin (8.0.x) | `b2935f5381d6469243440e080b43d0092a591663` (2026-09-04) | Earliest surveyed revision |
| Release label | `8.3.0` in `.claude-plugin/plugin.json`, `README`, `SKILL.md` | Label, not a git tag |
| Configuration schema | `7` → **`8`** (`allowed-worker`, `review-policy` added; v7 migrates conservatively) | Separate from the release version |
| Commit message | `release: agentflow @ 9571389` | Source-build label only; that source revision is uninspected |
| GitHub tags / Releases | Both API lists **empty** (`[]`) at the pin | No independently published tag |
| License / copy boundary | Apache-2.0, unchanged | Concepts restated in original prose; no upstream text copied |
| Delta size | ~40 files, +6,933 / −2,024, one commit | Bulk is host scripts; see below |

Primary sources (all 2026-09-21): [HEAD commit](https://api.github.com/repos/agfnow/agentflow/commits/main), [8.2→8.3 compare](https://api.github.com/repos/agfnow/agentflow/compare/fcb6878be0b2316cdba5a111f040655f161bfe03...main), [tags](https://api.github.com/repos/agfnow/agentflow/tags), [releases](https://api.github.com/repos/agfnow/agentflow/releases), and the compare's `docs/CHANGELOG.md`, `SKILL.md`, `README.md` patches read in full.

## State Ledger and Changed Mechanisms

The changed-file set (from the compare API) is dominated by host code: new
`scripts/delegation-route.js` (+399, the `allowed-worker`/`review-policy` engine),
new `scripts/default-branch.js` (shared default-branch resolver), new
`branch-safety-terminal.test.js`, and large rewrites of `agf.js` (+424),
`ag-settings.js` (+293), and their tests (`agf.test.js` +484, `ag-settings.test.js`
+240, `delegation-route.test.js` +240). Methodology-bearing prose changed in
`SKILL.md`, `references/{ag,closeout,delegation,looper,progress,streams,writing}.md`,
both `AG_GUIDE`s, and `docs/CHANGELOG.md` (relocated from repo root). `.setup-checked`
removed. Entries below are source-tier at the pin; source establishes the written
contract, not compliance by an installed agent.

| Claim / mechanism (8.3.0) | Evidence at the pin | Status / evidence limit | TeaPrompt disposition |
| --- | --- | --- | --- |
| Portable hookless-host support: any host with file+command tools + state retention; safe explicit host ID + `--session <id>` + optional `--host-family`; `hooks: not_available`; generic hosts get no hooks/transcript/model/effort/permission "by inference" | `SKILL.md` startup §; `README` Install; CHANGELOG Added | Verified source delta; a scope generalization beyond Codex/Claude; not exercised | Held: `04-agent/runtime-trust-boundary.md` (never infer unverified capability) + "missing evidence is unknown"; runtime is a Standing Non-Goal (AF83-1) |
| Schema-8 `allowed-worker` unordered permission policy (external/internal/host; "its order has no execution meaning"; per-task host picks an eligible kind + records a reason; v7 migrates to `["external","host"]`) | `SKILL.md` Settings; `README`; CHANGELOG; `delegation-route.js` (+399) | Verified source delta; host capability config | Governance-flavored (capability_class analog) but host-owned; record-only (AF83-2) |
| `review-policy: prefer-independent \| require-independent` — independent review preferred; labelled host review only after independent unavailability; finite availability-only fallback; write ownership settled before replacement | `SKILL.md`/`README`; CHANGELOG; `delegation-route.js` | Verified source delta; review-independence + graceful degradation | Held: Parallel Lens Review independence + `governed-delivery` decorrelated verification; config is host (AF83-3) |
| Version-1 shared review records (external/native/host) | CHANGELOG Added | Source-only; host artifact format | Host territory; record-only (AF83-4) |
| Session-ownership model: one owner per Ask; `agf owner inspect/adopt --expect <token\|unowned> --sha256 <hash>`; explicit release authorizes next-Ask claim; conflicting identity refuses before mutation; never expire owner from age/PID | `SKILL.md` startup § | Verified source delta; runtime concurrency/lease | Striking parallel to `agent-governance-scaffold` lease semantics (authorization-is-a-lease, state_predicate/TOCTOU sha), but runtime; record-only (AF83-5) |
| **Host obligation (new, I-062):** "Respectfully challenge mistaken, risky, or needlessly complex ideas with evidence, explain the tradeoff, and propose the simplest useful alternative … do not invent debate, override informed owner choices, or broaden scope" | `SKILL.md` Scope and evidence § | Verified source delta; prompt text | Held: installed `01-thinking/counterargument` lens (attack the plan, lower-cost alternative, minimum viable, "strictest but fair") — referenced by implement/minimality/review — + `reflective-minimality`/`reflective-risk`; corroboration (AF83-6) |
| New settings `git-timeout-ms` (`AGF_GIT_TIMEOUT_MS`, 30 s default), `log-verbosity: off\|wip\|all`, `inline-reply: on\|off`, completion-cleanup interval | `SKILL.md` Settings; CHANGELOG | Verified source; fixed vendor/operator config | Rejected class (AF82-7 precedent: numeric/vendor policy) (AF83-7) |
| Compaction threshold now 1,000 lines **or 768 KiB**; `agf compact`; verifies each Ask span by id+byte-length+SHA-256; conservatively retains rounds with nonempty inline answers; never truncates a single large open round | `SKILL.md` startup §; CHANGELOG Fixed | Verified source; host mechanics | Evidence-preservation held (A-7a/AF82-4); record-only (AF83-8) |
| Honesty deltas: "verified integrations" vs "portable core" vs "unavailable optional named integrations"; Limits "does not claim Pi, Gemini, or OpenCode live verification"; **removed** the dangling `eval/evaluation-harness.md` load rule; changelog moved to `docs/` | `README`; CHANGELOG; `SKILL.md` (eval line gone) | Verified source delta; resolves the prior surveys' "public skill not self-contained for that trigger" finding | Held: evidence-tier / author-claimed-vs-verified / "unknown not zero"; corroboration (AF83-9) |
| Standalone looper hands pending work back to an interactive host when no external capability is permitted/available; generated queues refuse to launch without their authority envelope; cleanup refuses uncertain/diverged/ignored Git state | `SKILL.md` looper bullet (I-075 extended); CHANGELOG Fixed | Verified source; host safety mechanics | Host territory; record-only (AF83-10) |

## Candidate Adoption Ledger

All rows are decided under a **bare survey** (no adoption direction); none is
installed. IDs continue the AF/AF82 lineage as AF83-*.

| ID | Candidate | Status | Evidence / local text gap | Reopen trigger |
| --- | --- | --- | --- | --- |
| AF83-1 | Portable hookless-host support; never infer capability/identity | No change | Held by trust-boundary don't-infer rule + "unknown not zero"; runtime is a Standing Non-Goal | An explicit skill-update direction *and* a local case where a TeaPrompt surface infers unverified host capability |
| AF83-2 | Schema-8 `allowed-worker` unordered permission policy | Record-only (host) | Capability-config analog of the governance pack's `capability_class`/`allowed_effects`; TeaPrompt runs no worker permission engine | A user directs governance scaffolding needing an unordered multi-route permission set (→ `agent-governance-scaffold`, gated) |
| AF83-3 | `review-policy` prefer/require-independent with availability fallback | No change | Reviewer independence held (Parallel Lens Review, `governed-delivery` decorrelated verification); the fallback policy is host config | A local gap where a TeaPrompt review surface lacks a stated independent-unavailable fallback |
| AF83-4 | Version-1 shared review records | Record-only (host) | Host artifact format; no TeaPrompt deliverable is a review-record store | Runtime remains a Standing Non-Goal |
| AF83-5 | Session-ownership model (`agf owner adopt`, sha256, no age/PID expiry) | Record-only (host) | Lease/optimistic-lock parallel to the governance pack, but runtime concurrency | A user directs lease/ownership scaffolding for a stateful agent (→ pack lease semantics, gated) |
| AF83-6 | Host obligation: challenge mistaken/risky/complex ideas (I-062) | No change | Held: installed `01-thinking/counterargument` lens (referenced by implement/minimality/review) + `critical-thinking-check` + `reflective-minimality`/`reflective-risk`; independent arrival via I-062 is corroboration | A local case where a skill or lens lacks the challenge-the-premise duty the counterargument lens already states |
| AF83-7 | `git-timeout-ms`/`log-verbosity`/`inline-reply`/cleanup-interval settings | Rejected | Fixed vendor/operator config; AF-9/AF-14/AF-17/AF82-7 stand; a version bump fires none of them | Only their original named triggers reopen them |
| AF83-8 | Compaction 768 KiB + `agf compact` + retain-inline-answers + never-truncate-open-round | Record-only (host) | Evidence-preservation held (A-7a, AF82-4); the thresholds/commands are host mechanics | A local dropped-evidence case, not an upstream threshold change |
| AF83-9 | Verified-vs-portable-vs-unavailable integration honesty; no Pi/Gemini/OpenCode claim; removed dangling eval load rule | No change | Held evidence-tier discipline; corroboration; the removal resolves the prior surveys' dangling-load finding (now moot at this pin) | None; the resolved finding is dated record-only |
| AF83-10 | Standalone-looper hand-back; queues refuse without authority envelope; cleanup refuses uncertain Git | Record-only (host) | Host safety mechanics; fail-closed gates corroborate `governed-delivery` | Runtime remains a Standing Non-Goal |

Recurrence is `unknown`; a squashed upstream release is not local recurrence. Old
AF/EP/AF82 ledger rows, dates, pins, and adopted sentences are intentionally
unchanged, and the 8.3.0 text does not contradict any adopted sentence (the
question-is-not-a-change and mid-task-continuation clauses remain consistent with
`SKILL.md`'s "a diagnostic follow-up does not cancel the unfinished task").

## Evidence vs Inference

- **Observed:** API identities (HEAD `0abf416`, tree, parent, ahead_by 1); empty
  tags/releases; the `plugin.json`/`README`/`SKILL.md`/`docs/CHANGELOG.md` patches in
  the compare; the changed-file list and per-file line counts.
- **Author-claimed:** every runtime behavior (portable-host handoff, session adopt,
  compaction, permission routing), the incident narrative (I-062, I-075), and the
  `gpt-5.6-sol/low` model preference. Reading source or its tests does not verify them.
- **[INFERENCE]:** that the delta is "mostly host implementation" — from the
  changed-file families and line counts, not an execution of each path.
- **Unknown / not done:** recurrence; the private source build `9571389`; any CLI run
  this pass; migration behavior; live hosts; whether the shipped tests pass at this pin.

## Evidence Actually Checked

- GitHub API 2026-09-21: `commits/main`, `compare/fcb6878...main`, `tags`, `releases`.
- Read in full from the compare: the `docs/CHANGELOG.md` 8.3.0 section, the `SKILL.md`
  diff, and the `README.md`/`README.zh-tw.md` diffs; changed-file inventory enumerated.
- Installed-surface grep 2026-09-21: agentflow vocabulary (`agentflow`, `godev`,
  `devlog`, `allowed-worker`, `external-runner`, `AGENTFLOW_SESSION`, `gpt-5.6-sol`,
  `prefer-independent`, `fast-lane`) absent from every skill and category surface.
- Not done: no CLI execution (nothing drafted → nothing probed); the ~30 changed
  script/reference files beyond the three read in full; the private build revision.

## Falsifiability

- Wrong if the pin, schema bump (7→8), or empty-tags fact is misread — all are quoted
  from the API at `0abf416`.
- Wrong if any 8.3.0 concept exposes a verified local gap a candidate marked "held"
  actually leaves open (the guard greps the coverage tokens off installed surfaces).
- AF83-6 "held" is wrong if `01-thinking/counterargument` (referenced by
  implement/minimality/review) does not carry the challenge-the-premise duty; it does.
- A squashed upstream release is not local recurrence; only an explicit skill-update
  direction re-runs these rows at the "would the skill be better" bar, as the 8.2 and
  original surveys did — and even then, only a verified local gap lands anything.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Current pin, schema bump, empty tags, delta size recorded | done | Version and Source Identity |
| 8.2→8.3 compare read; methodology deltas separated from host code | done | State Ledger and Changed Mechanisms |
| Ten delta concepts decided with evidence and reopen triggers | done | Candidate Adoption Ledger |
| Bare-survey direction-scope rule applied: no adoption, nothing installed | done | Status; Research Question |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_agentflow_v83_delta_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |

## Direction Addendum (2026-09-21, skill-update direction)

Follow-up: "anything should updated into skills" — a generic skill-update direction.
For this source it is the precedented trigger the 2026-09-05 and 2026-09-13 surveys
acted on: re-run the ledger at the "would the installed skill be better?" bar (name
the failure, name the smaller alternative rejected, show the existing skill text does
not already say it). All ten AF83-* rows re-ran with the actual skill/lens text
grepped and read; none clears the bar, and the ledger rows above are **unchanged**.

- **AF83-6 (the only methodology candidate) — no.** The I-062 "challenge mistaken,
  risky, or needlessly complex ideas, propose the simplest alternative" duty is
  already the installed `01-thinking/counterargument.md` lens in substance: "attack a
  proposed plan, architecture, or feature scope for fatal flaws and cheaper
  alternatives", "at least one lower-cost alternative named", "Minimum viable version
  stated", framed as the "strictest but fair" opposing architect (I-062's "do not
  invent debate"). The lens is referenced by `reflective-implement`,
  `reflective-minimality`, and `reflective-review`. It is a cross-cutting reasoning
  duty that lives in the lens layer by design; duplicating it into a skill body is the
  bloat `reflective-minimality` forbids. **Citation correction:** the initial draft
  cited "harness § Escalation," which is the runtime harness, not a TeaPrompt
  installed surface (`06-repo/AGENTS.md` carries no such clause); the accurate
  installed home is the counterargument lens, verified by grep and read this pass.
- **AF83-1 / AF83-3 / AF83-9 — no, held.** Don't-infer-capability
  (`04-agent/runtime-trust-boundary`), review independence (`governed-delivery` +
  Parallel Lens), and verified-vs-author-claimed honesty (evidence-tier discipline)
  are installed; the deltas restate them.
- **AF83-2 / AF83-4 / AF83-5 / AF83-8 / AF83-10 — no, host runtime.** Permission
  engine, review-record store, session ownership, compaction, looper hand-back are
  operationalization; runtime is a Standing Non-Goal, so a skill sentence cannot own
  them.
- **AF83-7 — no, rejected class.** Fixed vendor/operator settings; a version bump
  fires none of AF-9/AF-14/AF-17/AF82-7.

Unlike the 8.2 and 09-05 passes, no installed-text gap exists: those adopted because
a specific skill line carried a loophole (AF-2's "without a reason") or lacked a
consumer-side rule (EP-1); 8.3.0's methodology content was already adopted or is
lens-held, and the release is otherwise host implementation. Direction outcome
recorded so it is not re-litigated; the reopen triggers stand as written.

## Recent-Inspiration Reflection (2026-09-22)

User direction: "any inspired you recently? update if you think worthy".
This pass considers lessons from the recent surveys; it does not supply the
specific runtime-learner use case required by TB-1 or reopen unrelated holds.

The useful local lesson is coverage attribution. The Direction Addendum above
records a real error: the reviewer cited its own host's Escalation rule as
TeaPrompt coverage. The repository counterargument lens was the correct source.
That correction establishes repository coverage, not automatic availability in
a standalone skill: `Prompt Sources` lists explicitly describe provenance, and
the installation helpers copy/link skill directories, not the source library.

| ID | Candidate | Status | Evidence / smaller alternative / falsifier |
| --- | --- | --- | --- |
| CA-1 | Bind an already-covered verdict to the checked artifact and delivery scope | Adopted 2026-09-22 | Extend the existing Local Gap Test in [external-adoption-review](../04-agent/external-adoption-review.md#4-local-gap-test). A record-only correction fixes the past citation but leaves the review question ambiguous about whose coverage counts. No new skill or duplicated research-skill clause. Reconsider if this distinction is already supplied by the review's artifact contract or fails to prevent host/repository/install conflation. |
| CA-2 | Expand the governance pack from teaBrain/EMBER convergence | No change | [teaBrain TB-1](teabrain-concepts-experiments-survey-2026-09-21.md) and [EMBER EM-4](ember-snn-llm-survey-2026-09-22.md) remain evidence about a runtime-learner risk class, not local usage recurrence or enforcement proof; their recorded triggers remain unchanged. |
| CA-3 | Promote Agentflow preserve-before-destroy into another rule | No change | [8.3.2 survey](agentflow-8.3.2-delta-survey-2026-09-22.md) already records it as corroboration of existing recovery/risk guidance; no additional local gap established. |

Scope: one in-place prompt-lens clarification, not an external feature adoption,
new operating authority, or change to AF83-* dispositions. The one observed
citation failure justifies this narrow repair; it is not claimed as three
cross-session recurrences.

Consumer map: direct consumer is the adoption-review lens; standalone skill
bodies remain unchanged, with no claim that this lens edit changes their
installed behavior. The Decision Index points here; `index.json` is regenerated.
No router, registry, runtime, or schema changes. Existing prompt, cross-link,
record, and index checks cover structural compatibility; a disposable prompt
exercise checks host-only, repository-only, and standalone-skill coverage
judgments. Such an exercise is not a general efficacy benchmark.

Verification observed: a single stateless model invocation using the revised
lens as its system prompt classified four synthetic coverage claims correctly:
host-only instruction → not covered; checked repository lens in a full-repo
review → covered; provenance-only link to an uninstalled lens → not covered;
explicit instruction in the installed skill body → covered (4/4). No
before/after efficacy improvement is claimed. The exercise ran in memory and
left no script or new permanent test. The citation-twin search over the plan
archive found only the historical correction above, not another live claim.
