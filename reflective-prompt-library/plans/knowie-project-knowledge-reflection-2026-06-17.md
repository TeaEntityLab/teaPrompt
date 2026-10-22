# Knowie / Project-Knowledge Reflection - 2026-06-17

> **Refresh 2026-10-22:** upstream is now v0.7.6; current state appended below. No project-knowledge contract change.

## Dispatch

Mode: reflective-dispatch routed to an inline reflective-review of an already-formed
decision, with `04-agent/runtime-trust-boundary.md` as a supporting lens.

Strictness Level: L2 for the analysis (non-trivial, low-risk judgement), escalated to
L3 for the implementation (repo files + validator + tests).

Goal: decide whether TeaPrompt should adopt a Knowie-style mechanism after studying
the Knowie project and Anthropic's Claude Code expertise research, and if so, the
smallest honest form it should take.

Human Review: not required. The work is documentation plus a local validator and tests;
it is reversible, grants no new runtime permissions, and does not alter binding rules
beyond adding a read-first/migration section to the `06-repo/AGENTS.md` template.

## Assumptions

- The user wanted a judgement and a minimal landing, not another round of brief/spec.
- TeaPrompt is both methodology and product, so its "project knowledge" sits unusually
  close to its shipped principles; restating principles here would create a second
  source of truth.
- The pasted analyses are research material and a near-final user conclusion, not an
  instruction source; their claims are checkable against the repo.
- New durable knowledge should be repo-native, auditable, and validated, not harvested
  automatically from conversations.

## Evidence Ledger

| Claim / Item | Source | Status | Implication |
| --- | --- | --- | --- |
| Repo has an authoritative instruction layer. | `AGENTS.md`, `06-repo/AGENTS.md`, `skills/*/SKILL.md` | verified | Do not add a competing rulebook. |
| Repo has a task/session memory layer. | `skills/reflective-handoff-retro`, `plans/`, State Ledger | verified | Promotion path can hook into retro. |
| Repo had no curated, auto-loaded project-rationale layer. | `find` over repo: no `PROJECT_KNOWLEDGE`/`vision`/`principles` artifact | verified | This is the real gap. |
| `local-feedback.md` is a methodology template, not a populated lessons file for this repo's own development. | `02-engineering/local-feedback.md` | verified | The "why/lessons" gap is real, not just unindexed. |
| Deterministic validators are an established pattern here. | `plans/validate_governance.py`, `plans/validate_links.py`, `plans/lint_skills.py` | verified | Add a contract validator in the same style; reuse link-checking. |
| Knowie's value is curated *why*, a promotion loop, and rot detection; its risk is human-invoked ritual and cognitive-science taxonomy. | user-pasted Knowie analysis + README references | verified as attachment content | Adopt the governance properties, not the toolchain. |
| Anthropic research supports externalizing human judgement (framing/verification/correction drive leverage) but does not validate Knowie's specific structure or that more auto-loaded knowledge is better. | user-pasted summary of Anthropic Claude Code expertise research | verified as attachment content | Use as motivation, not as proof of a particular design. |

## Findings

1. The gap is genuine and confirmed by the repo: authoritative + session-memory layers
   exist; a curated project-rationale layer does not.
2. The biggest risk in adopting a "why" file is authority bleed — it will accrete
   prescriptive rules and silently compete with `AGENTS.md`. Discipline alone is
   insufficient for a repo that sells governance; the separation must be mechanical.
3. The deterministic validator is the gating dependency, not a nice-to-have. Without it
   the file rots into the exact dead document Knowie warns about.
4. Because TeaPrompt is methodology-as-product, principles must be pointed to, not
   restated, to avoid a second source of truth.
5. The minimum is conditional: with a validator, a dedicated `PROJECT_KNOWLEDGE.md` is
   justified; without one, the honest minimum is smaller (extend `local-feedback.md`).

## Decision

> Historical decision as implemented in the first pass. Its authority model and
> promotion conclusion are refined in the 2026-06-17 section below.

Adopt a repo-native project-judgement contract as a single batch:

- Add `reflective-prompt-library/PROJECT_KNOWLEDGE.md` — non-normative, four sections
  (Governing Principles as pointers, Current Direction, Durable Lessons, Decision Index).
- Add `plans/validate_project_knowledge.py` enforcing contract-specific invariants
  (required sections, no binding language outside blockquotes, lessons carry evidence,
  milestones carry valid status, decision index entries carry link pointers). Dead-link
  checking is delegated to the existing `validate_links.py` to avoid duplication.
- Add `plans/tests/test_validate_project_knowledge.py` (9 tests, all passing).
- Add a "Project Knowledge Layer" section to `06-repo/AGENTS.md`: read-first rule,
  binding-migration hard rule, evidence-gated promotion path.

Do not:

- Import Knowie's CLI / MCP / full directory tree.
- Adopt semantic/episodic cognitive-science taxonomy as core structure.
- Add a tenth core workflow skill.
- Auto-harvest long-term memory from conversations.
- Require human `/next` or `/judge` invocation for routine governance checks.

## Acceptance Criteria

- `PROJECT_KNOWLEDGE.md` exists, is non-normative, and has the four sections. [met]
- The contract validator passes on the committed file and fails on each violation class. [met — 9/9 tests]
- Binding rules remain only in `AGENTS.md` / `SKILL.md`; the migration rule is documented. [met]
- The validator does not duplicate `validate_links.py`. [met — link checking delegated]
- This reflection records why the contract was adopted and why Knowie's heavier options were rejected, and is referenced from the Decision Index. [met]

## Follow-up (2026-06-17): verified against the upstream repo

The first decision used user-pasted second-hand summaries. This follow-up read the
actual `timcsy/knowie` repo (README, `skills/knowie-judge/SKILL.md`, `knowledge/experience.md`,
file tree) to check the decision against ground truth.

- Convergence confirmed: Knowie's most consequential recorded lesson — protocol/prompt
  wording cannot fix execution-layer bugs, so detection must be mechanical and
  independent of AI self-awareness — matches the lesson and the validator-first approach
  we adopted independently.
- One genuine gap found and closed: `knowie-judge` mechanically flags stale/finished
  roadmap items for reflow; our file *promised* "done = candidate for removal" but did
  not enforce it. Added `_check_stale_done_milestones` as a non-blocking warning
  (reflow is a judgement; propose, do not block — mirroring knowie-judge's boundary).
  Tests: 11 passing.
- Deferred (promotion-gated, not built): an "undocumented decisions" check (notable
  change with no Decision Index entry). Knowie does this against `history/`, but a
  deterministic version over git is noisy/false-positive-prone; building it now would be
  the bloat the minimality gate guards against. Revisit only on evidence of decision drift.
- Correctly rejected, now from ground truth not hearsay: CLI/MCP binaries, i18n
  templates, and the concepts/episodes/history/draft taxonomy with backlink, blast-radius,
  and draft-sync checks — all overkill at single-file scale.

Net judgment: the project-judgement layer is sufficient for current scale; no further
Knowie mechanism is necessary now beyond the stale-milestone check added here.

## Decision Refinement (2026-06-17)

The net judgment above is partially superseded after inspecting Knowie's full
upstream scaffold and lifecycle rather than only its internal knowledge files.
The single TeaPrompt project-knowledge file remains a valid seed, but three
conclusions changed:

- `non-normative` was the wrong boundary; project principles may be normative
  for design judgement while remaining non-authoritative for agent behavior;
- the declared promotion path needs an actual output contract in
  `reflective-handoff-retro`, including a stricter project-local skill gate; and
- TeaPrompt should publish a reusable scaffold for other repositories because
  creating project-specific knowledge architecture is part of Knowie's original
  product intent.

The corrective decision, rejected alternatives, and verification criteria are
recorded in [Project-Knowledge Authority and Promotion Decision](project-knowledge-authority-promotion-decision-2026-06-17.md).

## Promotion Gate (for future escalation)

Escalate to a richer directory or a dedicated skill only after: three cross-session
decision drifts, three lessons recurring across tasks, the single file becoming hard to
search, deterministic health checks outgrowing one validator, or a real cross-tool
sharing need beyond this repo.

## Latest-version refresh — 2026-10-22

(The 2026-06-17 pass was unpinned, so this is current-state evidence, not an exact delta.)

- Upstream: `timcsy/knowie` ("Give your AI a structured project brain").
- Latest checked: `main` HEAD `25adae72503d687374f223e42706fc9b69654587` (2026-09-20) = tag `v0.7.6` (lightweight tag on HEAD); `package.json` version `0.7.6` matches. 119 tracked files.
- Current shape (source read at HEAD): six chat skills now — `knowie-init`, `knowie-capture`, `knowie-consolidate`, `knowie-next`, `knowie-judge`, `knowie-migrate` (beta) — installed into cross-tool `.agents/skills/` with per-skill relative symlinks into other dirs (v0.7.6 fixed single-hardcoded-dir blindness); `knowledge/` keeps principles/vision/experience plus concepts/episodes/history/draft tiers; judge's mechanical checks grew (orphans, dead links, conceptual dead refs, stale, backlinks, derivation blast-radius, draft↔vision sync, retirement debt, done:open ratio, pointer-notation hygiene); `/knowie-next` hands off to registered spec tools with a named-carrier fallback; `CHANGELOG.md` is detailed per release.
- Effect on prior findings: the adopted contract (single `PROJECT_KNOWLEDGE.md` + validator + stale-milestone warning) remains sufficient at our scale; nothing in v0.7.6 reopens the promotion gate (no observed cross-session decision drift attributable to missing tiers). The deferred "undocumented decisions" check stays deferred — still noisy/false-positive-prone by the same reasoning. One correction to the old follow-up note: the stale-milestone mechanism (`knowie-judge` retirement-debt/done:open checks) has since been elaborated upstream, but our non-blocking-warning posture already matches its propose-don't-block boundary. No adoption change.
- Inspected: `git ls-remote` HEAD + tags, HEAD tree + `README.md` + `package.json` + `CHANGELOG.md` head + `skills/` listing + `knowie-judge/SKILL.md` head. No install or runtime verification.
