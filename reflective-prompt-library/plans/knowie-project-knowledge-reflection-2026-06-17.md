# Knowie / Project-Knowledge Reflection - 2026-06-17

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

## Promotion Gate (for future escalation)

Escalate to a richer directory or a dedicated skill only after: three cross-session
decision drifts, three lessons recurring across tasks, the single file becoming hard to
search, deterministic health checks outgrowing one validator, or a real cross-tool
sharing need beyond this repo.
