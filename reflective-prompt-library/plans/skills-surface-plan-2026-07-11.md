# Skills-Surface Plan — 2026-07-11

> **Status: active planning artifact (non-authoritative).** Domain plan for the
> skills workstream (WS3/WS6 of the [whole-project plan](whole-project-plan-2026-07-11.md)),
> driven by the [agent-skills/flow-control survey](../../surveys/agent-skills-flow-control-survey-2026-07-11.md).
> It proposes verification tasks and gated candidates; it adopts nothing. Authority
> stays with [`06-repo/AGENTS.md`](../06-repo/AGENTS.md) and skill contracts; every
> adoption below requires its own ledger row and, where marked, human approval.

## Why

The SKILL.md format TeaPrompt standardized on is now a cross-vendor open
standard (30+ hosts) with a formal spec, reference validator, context budgets,
and distribution channels. That changes nothing about TeaPrompt's rules and
everything about the environment they run in: conformance can now be *verified
mechanically* against an external spec, and distribution has host-native paths
beyond copy/symlink. This plan turns those environment changes into bounded
tasks with evidence gates — the survey is interest evidence, not demand.

## Scope

- In scope: spec-conformance verification, structural guard candidates,
  distribution-channel evaluation, documentation parity checks.
- Out of scope / unchanged: nine frozen core skills, pack admission rule, full
  SKILL.md i18n (non-goal), any router change (owned by the
  [routing-holdout plan](routing-holdout-plan-2026-07-11.md)), operating a
  registry/marketplace of our own (no-runtime non-goal family).

## Tasks

### S1 — skills-ref conformance verification (unblocked; do first)

- Goal: establish whether TeaPrompt's 11 skills validate under the reference
  tool, and specifically how unknown top-level frontmatter fields
  (`risk_level`, `human_review_required`, `external_io`, `context_load`) are
  treated.
- Method: run `skills-ref validate` (github.com/agentskills/agentskills,
  skills-ref) against all 11 skill directories; record per-skill results
  verbatim in this file or a follow-up note.
- Decision rule: PASS with no unknown-field complaint → record "conformant,
  no change"; WARN/FAIL on governance fields → open a **gated candidate** to
  move the four fields under the spec's `metadata:` map (touches 11 skills,
  `validate_links.py`, `validate_governance.py`, QUALITY_GATES §5 — human
  approval + full `make all` + guard updates required; not to be done casually).
- Known today: name/directory match 11/11; description lengths 195–450 chars
  (≤1024) — measured 2026-07-11.
- Acceptance: an evidence-backed conformance statement exists; `unknown`
  replaced by observed validator output.

### S2 — spec-constraint guard candidate (small, deterministic)

- Goal: keep future skills within spec constraints without relying on memory.
- Proposal: extend the existing frontmatter validation in
  [`validate_links.py`](validate_links.py) with the spec's mechanical rules —
  name regex (lowercase/digits/hyphens, no leading/trailing/double hyphen),
  name==directory, description ≤1024 chars. This is a verifier-over-new-surface
  move (preferred route per the L3 skill-plus-deterministic-verifier pattern).
- Gate: human approval; lands with focused negative tests and a `make all` run.
- Non-goal: enforcing the 500-line body guidance — `lint_skills.py` already
  warns on length; do not double-guard.

### S3 — distribution channels (trigger-gated)

- Goal: decide whether TeaPrompt ships as a host-native package in addition to
  copy/symlink instructions.
- Channels observed: Claude Code plugins + marketplaces; Codex plugins
  (workspace distribution) and `$skill-installer`; Gemini
  `gemini skills install <git-url>` (works against a plain git repo **today** —
  TeaPrompt is already installable this way; worth documenting once verified).
- Trigger: an adoption signal (a user/report asking for packaged install), or
  the cheap subset — documenting the `gemini skills install` path — can ride
  the next SKILL_INSTALLATION edit after a smoke verification.
- Evidence rule: no telemetry exists; demand stays `unknown` until reported.
  Do not build marketplace packaging on interest alone.

### S4 — installation-doc parity check (small, unblocked)

- Goal: verify [SKILL_INSTALLATION.md](../SKILL_INSTALLATION.md) reflects the
  cross-host state: `.agents/skills/` as the interoperable path (Codex repo
  scan up to root, user `~/.agents/skills`, Gemini alias precedence), Claude
  nested-skill discovery, and the Gemini→Antigravity CLI churn banner for
  free-tier users.
- Acceptance: either "already accurate" recorded, or a minimal doc diff with
  registry-parity tests green (N4 guards).

### S5 — `compatibility` frontmatter for the packs (gated candidate)

- Goal: the two domain packs declare host preconditions in prose (bash 3.2,
  git, host CLI); the spec's `compatibility` field is the standard slot.
- Gate: pack surfaces are ledger-guarded — this is a pack-contract edit
  requiring the pack record's amendment discipline (ledger row + `make all`).
  Value is discoverability for spec-aware hosts; cost is one field ×2 skills.

### S6 — invocation-control mapping note (gated candidate)

- Goal: one short note (skill-map or SKILL_INSTALLATION) mapping TeaPrompt's
  `human_review_required` to host mechanisms: Claude `disable-model-invocation`,
  Codex `allow_implicit_invocation: false`, Gemini consent prompts — so
  installers of `reflective-risk`/`flow-loop-harness` know how to enforce the
  intent host-side.
- Gate: human approval for governed-doc edits; keep it a pointer table, not new
  policy. TeaPrompt declares, hosts enforce (runtime-trust-boundary).

## Sequencing

S1 → (S2 candidate informed by S1's validator experience) → S4 → S5/S6 as one
batched doc-and-contract pass if approved. S3 waits for its trigger except the
`gemini skills install` smoke note. Nothing here blocks the flow-control or
routing plans.

## Risks

- **Spec drift:** agentskills.io is young; `metadata`/`allowed-tools` are
  evolving (allowed-tools explicitly experimental). Mitigation: S1 records the
  spec version/date; re-verify before migration work.
- **Guard duplication:** S2 must not re-implement what `lint_skills.py` or N10
  license checks already own — extend, don't fork.
- **Churn temptation:** migrating governance fields under `metadata:` without a
  failing validator would be restructuring on aesthetics; the decision rule in
  S1 exists to prevent exactly that.

## Falsifiability

This plan is stale if: S1 remains unrun by the 2026-10-11 checkpoint; the spec
changes its frontmatter table; a host drops or forks the standard (adoption
table is dated 2026-07-11); or any task is executed without its recorded gate.
