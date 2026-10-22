# Oh My OpenAgent (OmO) 5.x Re-survey — Standalone Runtime Pivot (2026-10-01)

> **Status: decided — record-only; no adoption.** The 2026-06-25 tooling research
> recorded `code-yeongyu/oh-my-openagent` as a multi-agent orchestration *plugin*
> for OpenCode/Codex. Since then it has pivoted to a standalone agent runtime
> (`omo`, npm `omo-ai`, compiled Bun binary) running on `senpi`, a hard fork of
> `badlogic/pi-mono`. The user's hint ("not original depending on OpenCode, now
> an isolated agent system itself") is confirmed against the pinned source.
> All six candidate mechanisms land `record-only` / `covered`: five are prompt
> text or already owned by TeaPrompt methodology; none justifies a runtime,
> dependency, license, or router change.

## Research Question

User direction: survey `https://github.com/code-yeongyu/oh-my-openagent`
(checked 2026-10-01), honoring the hint that it is no longer an
OpenCode-dependent plugin but an isolated agent system.

What does the post-pivot architecture actually enforce in code versus prompt
text, what changed relative to the 2026-06-25 record, and does any mechanism
fill a verified gap in TeaPrompt? This survey does not reopen the standing
methodology posture: TeaPrompt stays methodology-side; host-run machinery is a
non-goal absent an owner sentence or a reproduced local failure.

## Direct Recommendation

- Correct the stale identity: OmO is now a standalone Bun-compiled agent
  runtime on its own engine fork; OpenCode/Codex plugins remain only as
  maintained adapter/migration layers (`docs/guide/migrating-from-opencode.md`,
  `omo setup` carries keys/providers/skills across).
- Do not install, depend on, or route to OmO. The SUL-1.0 license forbids
  commercial redistribution/hosting; TeaPrompt is a text-only methodology
  library and gains nothing from a source-available runtime.
- Treat every `ultrawork` verification claim (real-surface proof, per-target
  evidence reuse, two-attempt re-review, full-suite-before-final) as
  **prompt text only** — no harness enforces it. This is the same
  boundary the flow-loop-harness already draws: a verifier must be a
  deterministic external check, not a model's self-report.
- Note the one genuine runtime asset class worth citing by name only:
  fail-closed safety gating in `senpi-desktop-safety` (heartbeat <2000ms,
  screen-lock probe, OS-grant check, coordinate-frame freshness, and an
  out-of-band `UserReset` resume token unreachable by the model).

## Version / Date Context

| Identity | Observed value | Boundary / tracking event |
| --- | --- | --- |
| Reviewed commit | `37659a4c15cdbb5e2eb10d21109ae42829bcf2cd` (checked commit, 2026-10-01, merge of test-audit PR #9336 — corrected 2026-10-02; originally labeled "main HEAD," but the historical branch-at-HEAD attribution is unverified) | Immutable research pin; recheck on next release-line or engine change. |
| Release tag checked | `v5.1.7` → `89688165848b69121270682193b5ac2c175666de` | Tag and reviewed commit differ; no behavioral difference inferred from identity alone. |
| Package | root `package.json` name `oh-my-opencode`, version `5.1.7`; npm package `omo-ai` | Name predates the rename; artifact ≠ reviewed tree. |
| Engine | `senpi` v2026.9.30 (`@code-yeongyu/senpi`), fork of `badlogic/pi-mono` | Engine changes on senpi's own release line. |
| License | SUL-1.0 (`LICENSE.md:26-27`): internal-business/non-commercial use only; no commercial distribution or paid SaaS; patent-retaliation clause | Source-available, not OSI. |
| Prior local record | `agent-tooling-research-2026-06-25.md` rows 37/51/52/134-177; `external-adoption-case-studies-2026-06-20.md` Hyperplan row | The plugin-era characterization is now historical. |

## Method and Evidence Actually Checked

- Cloned to `/tmp/oma-survey`; pinned `37659a4`; read `README.md`,
  `CHANGELOG.md` (5.1.6/5.1.7), `ROADMAP.md`, `LICENSE.md`,
  `docs/guide/migrating-from-opencode.md`, root `package.json`.
- Three slices: (A) runtime topology/editions/license/safety via a delegated
  read-only scout; (B) orchestration/verification mechanics via a read-only
  scout; (C) memory/skills/hooks slice done directly (the third scout hit a
  usage-limit error; coordinator completed that slice inline).
- Traced (coordinator): `packages/memory-core/src/index.ts` barrel and
  `git/`, `memfs/`, `recall/`, `reflection/` subtrees;
  `packages/omo-senpi/src/components/memory/wiring.ts:13,132-155` (Kibitzer
  sidecar wiring); `packages/shared-skills/skills/` catalog (18 SKILL.md
  entries — corrected 2026-10-02; originally "16 skills" — incl.
  `ulw-plan`, `ulw-execute`);
  `packages/shared-skills/skills/ulw-execute/SKILL.md` (orchestrator-only
  rule, goal/todo discipline, Boulder state);
  `packages/omo-opencode/src/hooks/json-error-recovery/hook.ts`
  (JSON-parse-error retry list, not pre-execution repair);
  `packages/boulder-state` (state machine over `.omo/boulder.json`).
- Not run: no install, no `omo` execution, no provider calls. All behavior
  statements are source evidence, not runtime proof.
- Citation correction (2026-10-02): source paths below now use the reviewed tree's
  root-relative `packages/` locations, superseding the earlier package-relative
  shorthand for updater, DAG, memory, Boulder storage and ultrawork prompt.
  Pinned source/path checks do not add an installation or runtime receipt.

## Delta vs 2026-06-25 Record

| 2026-06 record | 2026-10-01 observed |
| --- | --- |
| Plugin for OpenCode (Ultimate) + Codex (Light) | Standalone `omo` runtime on senpi; plugins kept as adapters/migration path |
| `Team Mode`, `ultrawork`, hooks, MCPs | ultrawork persists as prompt doctrine; `mass ulw` now drives a real in-process DAG scheduler (`packages/senpi-task/src/dag`, ~14k LOC, WAL store); hooks moved into engine components |
| SUL-1.0 license badge | Unchanged: SUL-1.0 confirmed at `LICENSE.md` |
| Hyperplan runtime judged non-goal (agent swarm + runtime engine) | Same verdict at larger scale: the machinery grew; the non-goal boundary did not |

## Prompt-Text vs Enforced-Mechanism Map

| Claim (README/CHANGELOG) | Enforcement tier | Evidence |
| --- | --- | --- |
| "proves each step… checks the result on the real surface" | prompt only | `packages/prompts-core/prompts/ultrawork/*.md`; no runtime validates the surface check |
| evidence reuse per target; re-review ≤2; full suite before final | prompt only | `packages/prompts-core/prompts/ultrawork/codex.md:310-320,404-409`; one CLI helper exists for recording blockers, enforcement is self-policed |
| "mass ulw → graph of agents" | real engine + prompt glue | `packages/senpi-task/src/dag/` scheduler (dependency frontier, WAL, crash recovery); the *graph authorship* is model-written JS via `OMO_DAG_SDK_ROOT/sdk.js` |
| session resume / stale work | enforced | `packages/boulder-state` schema v2 + `packages/boulder-state/src/storage/stale-work.ts` transcript-mtime reconciliation (6h → paused) |
| Kibitzer nudge = observation only | enforced | `packages/memory-core/src/recall/gate.ts` rejects imperatives/second-person/Korean honorific request forms |
| malformed tool args "repaired before they run" | partially verified | OpenCode `json-error-recovery` hook retries parse-failed calls; no pre-execution repair found in the traced paths — treat claim as [INFERENCE] |
| install checksum verification | enforced at install, not update | `packages/get-worker/scripts/install.sh` verifies SHA256SUMS (path corrected 2026-10-02; originally `get-worker/scripts/install.sh`); `packages/omo-native/compiled-update.ts:50-61` `omo update` path emits raw curl+mv with no checksum [gap noted] |
| computer-use safety | enforced | `crates/senpi-desktop-safety/src/gate.rs` five-check fail-closed gate + `UserReset` out-of-band resume |

## Candidate Adoption Ledger

| ID | Mechanism | Disposition | Rationale |
| --- | --- | --- | --- |
| OO-1 | READ→CHANGE→RUN→CLEAN real-surface loop | Covered | `flow-loop-harness` requires an external verifier before done; OmO's version is prompt text inside a runtime we do not run |
| OO-2 | "tests alone never prove done" doctrine | Covered | Same contract already pinned (verifier must exercise the real surface; mock/echo tests explicitly rejected in consumer suites) |
| OO-3 | Bounded delta re-review (≤2) | Recorded | Prompt-level cap on reviewer respawns; TeaPrompt's loop caps already bound retries by `MAX_ITER`-class limits; a per-artifact *delta-scope* reviewer rule is noted, not adopted |
| OO-4 | Observation-only sidecar nudges (no imperatives to main agent) | Recorded | Strong guardrail pattern: a secondary advisor may inject facts, never directives. Adjacent to TeaPrompt's human-review/authority boundary; worth citing if a future host ever adds advisor lanes |
| OO-5 | Three-state plan checkboxes (`[x]/[ ]/[~]` blocked) | Recorded | `boulder-state` plan-checklist distinguishes blocked from open; TeaPrompt TASKS.md is a flat line-per-task list by design (fail-fast exit 3 covers the blocked case) |
| OO-6 | Fail-closed safety gate + out-of-band resume token | Recorded | `senpi-desktop-safety` is the genuinely hardened piece: heartbeat, lock-probe, frame-freshness, `UserReset`. Methodology analog: resumption of a halted risky path must require an authority the model cannot mint — consistent with `issued_out_of_band` in governance scaffold; no change needed |

## Falsifiability

This record is wrong or stale if: the `v5.1.7`→checked-commit pin is wrong (recheck
`git rev-list -1 v5.1.7` vs `37659a4`); senpi is replaced as engine; the
OpenCode/Codex adapters are deleted rather than maintained; license changes
from SUL-1.0; or a mechanism listed as "prompt only" gains runtime
enforcement (recheck `prompts-core` vs `senpi-task` boundary). Any adoption
requires an owner sentence plus a reproduced local failure per the standing
adoption bar.

## Source Corrections (2026-10-02)

Adjudicated repairs to source-tier facts above; all OO-* dispositions and the
record-only/no-adoption stance are unchanged.

- The reviewed commit `37659a4c` is recorded as the **checked commit** of
  2026-10-01, not "main HEAD": the historical branch-at-HEAD attribution is
  unverified, and no historical dev-HEAD inference substitutes for it. The
  tag identity (`v5.1.7` → `89688165`) remains distinct from the checked
  commit; the `v5.1.7`→commit wording in Falsifiability was updated to match.
- `packages/shared-skills/skills/` carries **18 SKILL.md catalog entries**,
  not 16.
- The install-checksum script is `packages/get-worker/scripts/install.sh`;
  the earlier `get-worker/scripts/install.sh` path omitted the package
  prefix.

## Latest-version refresh — 2026-10-22

- Prior baseline: checked commit `37659a4c15cdbb5e2eb10d21109ae42829bcf2cd`
  (2026-10-01), tag `v5.1.7` → `89688165`. Status: changed.
- Latest checked: default branch `dev` HEAD
  `e63990197933e32d6486740d1e43823db097586f` (2026-10-22, merge of
  test-audit PR #10861). Release split: `master` branch == tag `v5.1.40`
  (`eb585410`, 2026-10-20); `dev` HEAD is 2 days ahead of the latest stable
  tag. Root `package.json` still named `oh-my-opencode`, version `5.1.40`.
  Engine `@code-yeongyu/senpi` 2026.9.30 → **2026.10.19-2**. Only
  prerelease tag in range: `v5.1.34-beta.1`. License: `LICENSE.md`
  byte-identical — SUL-1.0 unchanged. Delta: 4,342 commits, 3,266 files;
  changelog 5.1.8 → 5.1.40 plus `[Unreleased]`.
- Actual meaningful changes (changelog claims + source spot-checks at `dev`
  HEAD):
  - Memory sync becomes an end-to-end encrypted multi-device engine
    (crash-safe journal, ≤8 MiB batches, compare-and-swap commits, device
    keyring verification, passkey recovery, weak/malformed Ed25519-key
    refusal). OmO accounts groundwork ships ahead of the service
    (`omo login/whoami/logout`, OS-credential-store-only keys).
  - Credential hygiene: the launcher deletes a legacy plaintext
    `~/.omo/credentials.json` on upgrade; `/feedback` reports reuse the
    `/share` redactor and never send memory.
  - New methodology-adjacent surface: standing-instruction agreements
    (`system/agreements.md`, repetition counter, human-only edits,
    `/agreements`) — a disclosure/counter pattern, noted, not adopted.
  - Computer-use hardening: foreground whole-screen input needs approval
    (`ControlRequired` otherwise); stop chord honors physical keyboards
    only; `senpi-desktop-safety` +888 lines (supervisor stop paths);
    `gate.rs` byte-identical (198 lines).
  - DAG scheduler: infra-failed `mass ulw` children retry ≤2 with backoff
    instead of failing the branch. `ulw-plan` review drops the fixed
    five-round cap for a finding-driven stop rule.
  - `omo update`: refuses package-manager-owned binaries with the manager's
    own upgrade command (#9585) — but the remaining path is still raw
    `curl+mv` with no checksum/signature verification: the 2026-10-01 gap
    persists (verified: no `sha256|checksum|sigstore|verify` in
    `packages/omo-native/compiled-update.ts` at HEAD).
  - OpenCode 2 plugin shape supported alongside 1.x, with an OmO Native
    notice; migration doc retained — standalone pivot confirmed, adapters
    maintained. Release binaries: Bun 1.4.3 (CVE-2026-48618), size budget
    160 → 182 MiB; workflow node-id path-traversal fix; locale-safe
    archive-entry validation.
- Effect on prior findings: all six OO-* dispositions stand. Anchors
  re-verified at HEAD: Kibitzer imperative/second-person rejection prose
  intact in `packages/memory-core/src/recall/gate.ts`; skills catalog
  still 18 SKILL.md entries; `boulder-state`, `json-error-recovery`,
  install-time SHA256SUMS check all present; ultrawork verification claims
  still prompt text in `packages/prompts-core/prompts/ultrawork/` (small
  per-model edits only). Record-only / no-adoption stance unchanged; the
  account-service and sync surfaces widen the credential/exfil footprint
  without changing the methodology boundary.
- Inspected (immutable): `dev@e6399019`, `v5.1.40@eb585410`,
  `v5.1.7@89688165` trees; `CHANGELOG.md`, `LICENSE.md` (zero-diff),
  `package.json`, `compiled-update.ts`, `recall/gate.ts`, `gate.rs` at
  `https://github.com/code-yeongyu/oh-my-openagent`.
- Untested limits: no install, no `omo` execution, no provider calls;
  changelog entries are author reports; sync/crypto correctness not
  audited; execution of the safety gate unverified.
