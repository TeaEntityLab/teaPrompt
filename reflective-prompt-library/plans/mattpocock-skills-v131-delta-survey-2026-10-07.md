# mattpocock/skills v1.3.1 Delta Survey (2026-10-07)

> **Status:** Reference-only record. Upstream pinned at `6fd947921b935b7e1e69293a200400f0fdd5c15f` (`main`, checked 2026-10-07) and release tag `v1.3.1` @ `24fe0ef7737efae15c87225755e9f6f5965e4888` (checked 2026-10-07). Evaluated against TeaPrompt's nine-core freeze and standing non-goals; PML-DELTA-1 reference-only, no skill, runtime, schema, or gate change. `06-repo/AGENTS.md` and the invoked skill contracts remain authoritative.

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
