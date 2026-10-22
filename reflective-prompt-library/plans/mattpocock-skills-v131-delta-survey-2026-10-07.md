# mattpocock/skills v1.3.1 Delta Survey (2026-10-07)

> **Status:** Reference-only record. Upstream pinned at `6fd947921b935b7e1e69293a200400f0fdd5c15f` (`main`, checked 2026-10-07) and release tag `v1.3.1` @ `24fe0ef7737efae15c87225755e9f6f5965e4888` (checked 2026-10-07). Evaluated against TeaPrompt's nine-core freeze and standing non-goals; PML-DELTA-1 reference-only, no skill, runtime, schema, or gate change. `06-repo/AGENTS.md` and the invoked skill contracts remain authoritative.
>
> **Refresh pointer (2026-10-22):** the pins above are historical. Latest `main` `5beb35b040e3de97e54fa9e386d7e42d15c295c2` (2026-10-19) and the still-current `v1.3.1` release are covered in `## Latest-version refresh — 2026-10-22` below; the PML-DELTA-1 reference-only disposition is unchanged.

## Purpose

User instruction: "survey updated: https://github.com/mattpocock/skills" (checked 2026-10-07) followed by "If worthy recording then update docs".

This record evaluates the commit delta of `mattpocock/skills` since the 2026-10-03 survey pin (`d81f3a183412e71a5b1e84ca21bc1a35eea03a60` in `plans/pstack-matt-lauren-survey-2026-10-03.md`) through the inspected `main` (`6fd947921b935b7e1e69293a200400f0fdd5c15f`): **34 reachable commits**, 72 changed files, +1,028 / −637 lines. The release tag `v1.3.1` points to a distinct revision, `24fe0ef7737efae15c87225755e9f6f5965e4888`; its tag-to-inspected-main range contains **28 reachable commits**.

Counting method (checked 2026-10-07): `git rev-list --count d81f3a183412e71a5b1e84ca21bc1a35eea03a60..6fd947921b935b7e1e69293a200400f0fdd5c15f` returned 34; the same command with `24fe0ef7737efae15c87225755e9f6f5965e4888` as the left endpoint returned 28. The file/line delta belongs to the prior-pin-to-main range. This recording correction supersedes the earlier 32-commit statement; it does not relabel main-only observations as release-tag behavior.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Reopen trigger / falsifier |
|---|---|---|---|---|
| PML-DELTA-1 | `mattpocock/skills` main delta mechanisms (`chief-of-staff` dual-track, `SCOPE.md` catalog freeze, harness-owned recursion guards, temp-file handoffs); distinct v1.3.1 tag recorded | Reference-only (no change) | Pinned prior-to-main delta has 34 reachable commits; tag-to-main has 28 (checked 2026-10-07); existing TeaPrompt composition covers the conceptual patterns, not an efficacy result or verified host enforcement | Reopen if an upstream pattern demonstrates an exercised local structural gap not covered by existing core compositions or generator packs. |

## Delta Summary & Analysis

### 1. `chief-of-staff` Skill (`skills/in-progress/chief-of-staff/SKILL.md`)
- **Metadata:** `disable-model-invocation: true`, experimental.
- **Pattern:** Long-running coordinator pursuing multi-task goals via subagents.
- **Dual-Track Cognition:**
  - *Tactical:* Complete immediate work.
  - *Strategic:* Modify environment for the *next* task ("pit of success": constrained APIs, lint rules, `CODING_STANDARDS.md`, "no workarounds" rule).
- **Communication:** Sparse; via context pointers (paths, commits, notes) rather than transcript copying.
- **TeaPrompt Evaluation:** In TeaPrompt, this dual track is already handled by composing `reflective-handoff-retro` (reusable rules and memory consolidation) with `reflective-implement` (anti-regression rules, twin sweeps) and `flow-control-generator` (orchestrator-worker scripts). No new core skill is warranted; cardinality remains frozen at nine.

### 2. Scope & Governance Hardening (`SCOPE.md` + `.out-of-scope/`)
- **`new-skills.md`:** Upstream catalog is frozen: *"If you can compose the behaviour from existing skills, it doesn't get a new skill."* Proposing new skills is formally closed. This is compatible with TeaPrompt's frozen nine-core design [INFERENCE]; it does not validate TeaPrompt's particular three-recurrence threshold.
- **`subagent-recursion.md`:** Upstream assigns recursion and loop stopping to the harness rather than in-skill prose. This matches TeaPrompt's host-enforcement boundary [INFERENCE]. Generated `MAX_ITER`/`MAX_JOBS` scripts still need correct validation; the [review handoff](recent-changes-review-handoff-2026-10-07.md) records observed cap failures rather than treating the architecture agreement as enforcement proof.
- **`harness-name-collisions.md`:** Upstream rejects renaming skills when host harnesses ship colliding built-ins (e.g. Claude Code `/prototype` or `/research`), relying on namespaced invocation.

### 3. Execution Safety (`claude-handoff` #272)
- Replaced embedding a model-generated summary directly in shell source with reading a temporary file inside quoted command substitution (`claude --bg --name "<name>" -- "$(cat <file>)"`). In that shown transport, backticks and `$` in the file contents are not re-parsed as shell code; safety still depends on constructing the surrounding command and file path correctly.
- Compatible with TeaPrompt's `headless-agent-cli-contract` preference for reviewed argv transport without interpolating prompt text into shell source [INFERENCE]. This is a source-level comparison; the upstream CLI handoff was not exercised in this survey.

### 4. Tool Invocation Terminology
- Shifted from `/slash` command notation (`Use /tdd`, `use /code-review`) to programmatic tool calls (`Call the Skill tool with "tdd"`), decoupling skills from chat-UI conventions. Matches TeaPrompt's host-agnostic Module Contract design.

## Evidence vs Inference

### Evidence Actually Checked
- Upstream Git repository [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills) (checked 2026-10-07).
- Git `ls-remote` pin `6fd947921b935b7e1e69293a200400f0fdd5c15f` (`main`) and tag `v1.3.1` @ `24fe0ef7737efae15c87225755e9f6f5965e4888` (checked 2026-10-07).
- Commit diff from prior pin `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` (checked 2026-10-03 in `plans/pstack-matt-lauren-survey-2026-10-03.md`).
- Primary file contents inspected: `skills/in-progress/chief-of-staff/SKILL.md`, `SCOPE.md`, `.out-of-scope/subagent-recursion.md`, `.out-of-scope/new-skills.md`, `.out-of-scope/harness-name-collisions.md`, `skills/in-progress/claude-handoff/SKILL.md`, and `skills/engineering/implement/SKILL.md` (checked 2026-10-07).
- Immutable source scope: [inspected main tree](https://github.com/mattpocock/skills/tree/6fd947921b935b7e1e69293a200400f0fdd5c15f) versus [distinct v1.3.1 revision](https://github.com/mattpocock/skills/tree/24fe0ef7737efae15c87225755e9f6f5965e4888) (checked 2026-10-07). The analysis above is scoped to inspected main unless explicitly stated otherwise.

### Inferences & Claims
- `chief-of-staff`'s "pit of success" and tactical/strategic dual-track mental model is already served in TeaPrompt by composing `reflective-handoff-retro` with `reflective-implement` and `flow-control-generator` [INFERENCE].
- Upstream's catalog freeze in `SCOPE.md` provides a compatible design judgment about composition and skill proliferation, not an independent measurement of maintainability cost [INFERENCE].

## Falsifiability

This assessment is wrong if:
1. `chief-of-staff` introduces a repeatable operational mechanism that cannot be expressed by composing TeaPrompt's existing nine core skills and ten domain packs, causing documented user failures in long-running goal tracking.
2. In-skill recursion guards are proven necessary despite upstream's and TeaPrompt's architectural consensus that recursion limits belong in the host execution harness.

## Latest-version refresh — 2026-10-22

Reference-only update. Prior dispositions stand: PML-DELTA-1 remains reference-only; no skill, runtime, schema, or gate change.

### Version identities (checked 2026-10-22)

- Prior baseline: `main` `6fd947921b935b7e1e69293a200400f0fdd5c15f` (checked 2026-10-07); release tag `v1.3.1` @ `24fe0ef7737efae15c87225755e9f6f5965e4888`.
- Latest `main`: `5beb35b040e3de97e54fa9e386d7e42d15c295c2`, committed 2026-10-19 (`chief-of-staff: keep memory in a dated, commit-cited wiki (#1304)`).
- Latest release: still `v1.3.1` (2026-10-04; [releases feed](https://github.com/mattpocock/skills/releases) shows no newer tag, and `refs/tags/v*` enumeration ends at `v1.3.1`). Main-only observations below are not release-tag behavior.
- Delta size: `git rev-list --count 6fd9479..5beb35b` = **19 reachable commits**; 37 changed files, +297 / −90 lines. Tag-to-latest-main range grew to **47 commits** (was 28).
- Skill inventory unchanged: `skills/*/SKILL.md` counts 38 files at both pins (two independent `git ls-tree` path filters agree).

### Material changes since the prior pin (source-read at `5beb35b`)

- `chief-of-staff`: gained a **Wiki** memory section — dated, commit-cited interlinked pages (`index.md` + one-thing-per-page) with ingest/query/lint operations and a "write history, not the present" rule (date every claim, cite the commit code claims were true at, mark superseded claims rather than rewriting). Context pointers now explicitly include wiki pages. This is the largest conceptual addition in the delta; it extends, not replaces, the previously recorded dual-track/pit-of-success pattern.
- New `.out-of-scope/lazy-load-writing-for-agents.md`: upstream formally closes requests to lazy-load `writing-for-agents` in `retro`, on the ground that the skill judges steering files before writing. Consistent with the catalog-freeze governance direction already recorded.
- `ask-matt`: router must now read a skill's `SKILL.md` before stating what it does or recommending a step be skipped (summaries are orientation-only).
- `code-review`: standards sourcing changed from named files to repo-wide search (with `CODING_STANDARDS.md`/`CONTRIBUTING.md` mandatory when present); both review sub-agents are now issued together in the foreground. Tracker-doc path reference generalized.
- `diagnosing-bugs`: forced-red rule hardened — if the red was forced by mutating code or a fixture, `diff` against a pristine copy to prove the mutation landed before trusting it.
- Smaller skill edits: `tdd` notes what each proposed seam catches and misses; `grilling` words questions so "yes" accepts the recommendation; `teach` anchors workspace paths and varies quiz answer position; `wayfinder` drops triage labels/placeholder refs/research PRs; `implement` fetches a passed ticket reference and states its title; `setup-matt-pocock-skills` fixes tracker commands and triage labels; `wizard/template.sh` readability/portability fixes; README/CLAUDE install-block and marketplace wording.
- No adapter/permission/execution-surface change: `agents/openai.yaml` Codex metadata untouched; no new or graduated skills in this range (all edits modify existing skills/docs).

### Effect on prior findings

- The recorded mechanisms (dual-track coordination, catalog freeze, harness-owned recursion guards, temp-file handoffs, tool-call terminology) are all still present and unreversed at the new pin.
- The chief-of-staff wiki is a new composable pattern candidate, but TeaPrompt composition (`reflective-handoff-retro` + `reflective-implement` + `flow-control-generator`) still covers the concern at the methodology layer; no local structural gap demonstrated. PML-DELTA-1 stays reference-only with no new ledger row warranted.

### Inspected links

- [Prior main tree](https://github.com/mattpocock/skills/tree/6fd947921b935b7e1e69293a200400f0fdd5c15f) vs [latest main tree](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2); [v1.3.1 tree](https://github.com/mattpocock/skills/tree/24fe0ef7737efae15c87225755e9f6f5965e4888); [chief-of-staff at new pin](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/in-progress/chief-of-staff/SKILL.md); [new out-of-scope record](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/.out-of-scope/lazy-load-writing-for-agents.md) (all checked 2026-10-22 via git fetch + blob diff, no checkout hooks, no code executed).

### Limits

- Source inspection only; no upstream skill, hook, or installer was executed. Release-note text is an author report. Commit count uses the prior-pin-to-main range; tag-peeled identities verified via `ls-remote`.
