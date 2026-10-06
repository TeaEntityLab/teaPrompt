# Managed-Skills Learned Procedures Survey — 2026-10-06

Language: English


> **Status:** Accepted record — procedures already minted as managed skills at `~/.omp/agent/managed-skills/`; this doc is the project-side survey of what was learned and where it lives.
## Purpose

Preserve the four reusable procedures this session produced as durable
documentation in the project — not as registered packs (procedures live in
`~/.omp/agent/managed-skills/`, not `skills/`). This is a record of what was
learned, why each is a procedure (not a fact), and where it now lives.

This is a **documentation artifact**, not an agent instruction source.

## Background

While surveying upstream `obra/superpowers` v6.4.2 and running the runtime-
skills dry run, four procedures recurred that were worth codifying beyond this
session. Project-specific packs (`headless-agent-cli-contract`,
`arm-blinded-eval-harness`, `acceptance-join-validator`,
`golden-benchmark-runner`, `router-trace-linter`) were registered in
`DOMAIN_PACK_SKILLS` — this survey covers the *cross-project* procedures that
don't belong to any one repo.

## Surveyed Managed-Skills Inventory (post-session)

The host's managed-skill library at `~/.omp/agent/managed-skills/` held 43
skills before this session, ~39 project-scoped and ~4 already-general (`parallel-lens-review-
packet`, `redacted-external-review-panel`, `external-doc-internalization`,
`go-private-module-offvpn-sideload`, `route-aware-go-coverage`,
`parallel-go-test-coverage-fanout`, `godoc-route-catalog`,
`source-map-api-audit`, `swaggo-annotation-audit`).

## Procedures Recorded

### 1. `registry-gated-admission-sweep`

**What:** When adding a member to a set whose membership is enforced by a
registry constant plus scattered pins (count assertions, doc tables, install
scripts, i18n twins), enumerate every surface before editing, update them all
in one change, and handle test-pinned literal phrases via dated supersession.

**Session evidence:** admitting the five domain packs touched
`DOMAIN_PACK_SKILLS` + pin 5→10, `skill-map.md`, both cheatsheets, both
install guides (list + `for name in` loops + human-review set), usage log
rows + two count tables, and three pytest pins. Two documents carried a
test-pinned literal ("Five registered domain packs") that required a dated
supersession note rather than an in-place edit.

**Location:** `~/.omp/agent/managed-skills/registry-gated-admission-sweep/SKILL.md`

### 2. `inert-proposal-mechanics-smoke`

**What:** When a proposal is held at a human admission gate and "continue"
doesn't authorize admission, advance by proving its core mechanics with
throwaway smoke tests — synthetic fixtures, stub CLIs, byte-level checks —
rather than stalling or shipping unverified.

**Session evidence:** all five proposals were smoked in `/tmp/proposal-smoke/`
before admission — router-linter on three fixtures, blinded-harness on label-
stripped extraction + leak assertion, join-validator on a synthetic REQ/AC
repo, benchmark-runner under `AGENT_CMD=cat`. A failure in the smoke (naive
extraction tripping on ollama spinner pollution) was itself evidence.

**Location:** `~/.omp/agent/managed-skills/inert-proposal-mechanics-smoke/SKILL.md`

### 3. `external-repo-delta-survey`

**What:** Re-surveying an already-surveyed upstream repo — pin the current
SHA/tag first, recover the prior baseline, diff only the delta, classify
covered/implementable/redundant, and treat version drift as a first-class
finding.

**Session evidence:** `obra/superpowers` re-survey pinned
`8ca22dba…` (v6.4.2) via `ls-remote` + release API, recovered the
2026-06-25 baseline, and scoped the delta to v6.4.1→v6.4.2 changes
(leaner plans, PR-not-main target, removed CLAUDE.md). Drift items (e.g.
`devin models list` output shape) were recorded as findings, not silently
re-tested.

**Location:** `~/.omp/agent/managed-skills/external-repo-delta-survey/SKILL.md`

### 4. `delayed-review-finding-triage`

**What:** When aggregated review findings arrive delayed, verify each against
current file bytes before acting — bucket as stale / valid / wrong-premise —
and never re-edit a correct file "to be safe".

**Session evidence:** multiple advisories predated later edits (frontmatter
fence claim was stale — already fixed; "ollama pollution unchanged" was
wrong — bytes showed stderr not stdout; "Five domain packs" pin was valid).
A stale-run suite count (1440 vs final 1449 after index regen) was caught and
corrected.

**Location:** `~/.omp/agent/managed-skills/delayed-review-finding-triage/SKILL.md`

## Evidence vs Inference

All four procedures above are evidenced by session receipts (commits `c454738`, `8f610df`, `dfa1789`; `/tmp/proposal-smoke/` artifacts; `/tmp/proposal-smoke/reprobe/` re-probe outputs). The managed-skill inventory count (43→45) is observed via directory listing. [INFERENCE] The 'cross-project' classification is judgment: these procedures are repo-agnostic in *mechanism* but were only exercised inside TeaPrompt today.

## Falsifiability

This survey is falsified if: (a) any of the four managed skills is absent at `~/.omp/agent/managed-skills/<name>/SKILL.md`; (b) the domain-pack registry count in `plans/validate_skill_examples.py` is not 10; (c) the cited commits do not contain the claimed pack-admission surfaces.

## Boundary Calls

- **Not recorded as managed skills:** the five TeaPrompt domain packs
  (repo skills, not managed skills — correct home is `skills/`), the
  reflective-* workflows (repo-owned), project-specific lessons already
  captured by `teaprompt-*` skills.
- **Not recorded at all:** dated-supersession notation (folded into the
  admission-sweep skill as a step), vocabulary-guard placeholder pattern
  (folded into the same skill's failure-modes section).

## Status

Recorded 2026-10-06; four managed skills minted, session committed at
`dfa1789`. No repo code changes beyond index/hygiene bookkeeping.
