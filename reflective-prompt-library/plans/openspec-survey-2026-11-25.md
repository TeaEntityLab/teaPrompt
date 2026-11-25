# OpenSpec (Fission-AI) Survey — Fluid Spec-Driven Development (2026-11-25)

Language: English
> **Status:** source-qualified reference record (`OSP-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.**

The owner asked to survey `Fission-AI/OpenSpec`. This record pins the repo, reads the core docs and one live spec, and maps the transferable distinctions onto existing TeaPrompt contracts. It does not install the CLI, run a change workflow, or authorize a runtime. OpenSpec is a **spec-driven-development tool in the same genre as GitHub Spec Kit** (already surveyed 2026-06-25 and re-checked 2026-11, disposition "conceptually aligned, no install by default") — OpenSpec's differentiator is fluid/iterative over phase-gated, with a cleaner delta-to-source-of-truth merge model. No reproduced local gap was found.

## Research Question and Direct Recommendation

Which mechanisms in OpenSpec are worth borrowing, and do they expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; same genre verdict as Spec Kit — conceptually aligned, no install.** OpenSpec's transferable mechanisms: a change-folder convention (proposal + spec deltas + design + tasks) that keeps intent separate from merged truth, an explicit delta grammar (`## ADDED / ## MODIFIED / ## REMOVED / ## RENAMED Requirements`) for brownfield specs, RFC 2119 `SHALL`/`MUST`/`SHOULD`/`MAY` requirement strength, named `#### Scenario:` GIVEN/WHEN/THEN cases, a "review the plan before any code" reading order with early-exit heuristics, and a CLI that emits machine-readable contracts for agent consumption. Most restate existing TeaPrompt duties; the spec-delta grammar and review-order note are deferred documentation, not a missing contract.

## Evidence Used and Date Context

Checked 2026-11-25. `Fission-AI/OpenSpec` `main` `f1cd852`, shallow clone (769 Markdown files). Read: `README.md`, `docs/concepts.md`, `docs/agent-contract.md`, `docs/writing-specs.md`, `docs/workflows.md`, `docs/reviewing-changes.md`, `docs/explore.md`, and the in-repo `openspec/specs/cli-validate/spec.md` (self-hosted example). Also checked `plans/skills-and-spec-systems-research-2026-06-25.md` for the Spec Kit precedent (lines 212-218 carry the 2026-11 delta).

## What OpenSpec Actually Is

- A **CLI + skills bundle** (`/openspec-explore`, `/openspec-propose`, `/openspec-apply-change`, `/openspec-archive-change`, plus expanded `/opsx:*` verbs) that installs per-tool agent instructions and manages an `openspec/` directory.
- **Two areas:** `openspec/specs/` = source of truth (current behavior, organized by domain), `openspec/changes/<id>/` = proposed modifications (proposal.md, spec deltas, design.md, tasks.md). Archiving merges deltas into specs.
- **Delta grammar:** changes declare `## ADDED`, `## MODIFIED`, `## REMOVED`, or `## RENAMED Requirements` — the merge is structural, not prose diffing.
- **Spec format:** requirements use RFC 2119 keywords; each requirement carries named `#### Scenario:` blocks with `WHEN/THEN/AND` bullets; the validator warns on missing narrative text and misformatted scenarios.
- **Workflow:** explicitly "actions, not phases" — `/explore` (thinking partner, never writes code), `/propose`, `/update`, `/apply`, optional `/verify`, `/archive`. Human review has two moments: the plan before apply, the code before archive.
- **Agent contract:** `docs/agent-contract.md` documents JSON envelope shapes, root-resolution precedence, and per-command output schemas "verified against `src/`" — a machine-readable surface for agent tools.
- **Governance notes:** MIT license; anonymous telemetry (command names + version only) opt-out via `openspec config set telemetry.enabled false`, `OPENSPEC_TELEMETRY=0`, or `DO_NOT_TRACK=1`; "built with OpenSpec" (repo hosts its own specs/changes as live examples).
- **Self-described comparison:** lighter than Spec Kit (no phase gates, no Python), tool-agnostic vs. Kiro's IDE lock-in; "30+ tools" supported.

## Evidence vs Inference

- **Verified:** the pinned HEAD, docs quoted above, the in-repo `cli-validate` spec format, the telemetry opt-out mechanism, the Spec Kit prior-disposition record.
- **Supplier-summarized (unverified):** "most loved spec framework" framing, "30+ tools" count, recommended model pairings (Codex 5.5 / Opus 4.7), the capstone-audit claim on `agent-contract.md` (not re-run), and all download/star badges.
- **Inference (this record):** the contract-map dispositions; the judgment that OpenSpec's core loop is the same spec-plan→implement→archive cycle TeaPrompt already models in prompt form; that the delta grammar's real value binds to a *spec-as-source-of-truth* discipline TeaPrompt does not maintain for its own prompts.
- **Unknown:** whether the delta merge is robust under concurrent edits in practice; whether the "fluid" workflow drifts from discipline at scale; CLI correctness of the JSON contract (not executed).

## TeaPrompt Contract Map and Disposition

| Finding | Existing surface | Disposition |
| --- | --- | --- |
| Agree on specs before code; review the plan before apply | `reflective-spec-plan` (acceptance criteria first); `reflective-implement` (spec before code); Human Review gate | Restated; OpenSpec's two-moment review (plan→code) is the same shape |
| Change-folder convention keeps proposal/specs/design/tasks separate from merged truth | `plans/` records + adoption ledgers; `PROJECT_KNOWLEDGE.md` as durable truth | Same separation in prose form; OpenSpec adds file-shape enforcement via CLI |
| `## ADDED/MODIFIED/REMOVED/RENAMED` delta grammar for brownfield specs | No TeaPrompt equivalent — TeaPrompt does not maintain behavioral specs of its own prompts | **Closest real distinction**, but dormant: valuable only if TeaPrompt ever maintains mergeable spec files. Deferred doc note |
| RFC 2119 `SHALL`/`MUST`/`SHOULD`/`MAY` + named GIVEN/WHEN/THEN scenarios | `reflective-spec-plan` falsifiability + acceptance criteria (prose) | TeaPrompt uses plain-language criteria; the keyword/scenario formality is a style choice, not a missing rule — reference only |
| "Read in this order, quit earliest" review heuristic (proposal → spec → design → tasks) | `reflective-review` (findings first, file/line refs, traceability table) | Deferred doc note — a worked review-order example could join the deferred worked-reference queue |
| CLI emits machine-readable contracts (JSON envelope, exit codes, root precedence) | Host-tool surface; TeaPrompt emits prompt-layer contracts, not CLI JSON | Host feature; `agent-contract.md` is a good example of agent-facing doc design — reference only |
| `/explore` as a no-stakes thinking partner before proposing | `reflective-brief` (clarify before planning); `reflective-research` | Same trigger shape |
| Anonymous telemetry with documented opt-outs | `runtime-trust-boundary.md` data policy | Privacy note recorded; opt-out path is explicit and honored — no flag |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| OSP-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Refresh if OpenSpec's delta grammar, Stores model, or agent contract changes materially |
| OSP-DOC2 | Optional worked references: (a) the two-moment review order as a `reflective-review` example; (b) the ADDED/MODIFIED/REMOVED/RENAMED delta grammar, if TeaPrompt ever maintains spec files for its own behavior | Deferred | No reproduced local gap; joins the deferred worked-reference queue (CFT/ACL/CKB/UAS/ALV-DOC2). Reopen if a spec-merge or review-order failure is demonstrated |
| OSP-SK1 | An OpenSpec-flavored spec-authoring Skill | Not adopted | `reflective-spec-plan` covers the loop; a file-shape Skill would duplicate an existing surface |
| OSP-RUN1 | Install the OpenSpec CLI or adopt its `openspec/` directory convention | Not adopted | Host tool + directory convention; TeaPrompt's equivalent lives in `plans/` records and is human/agent-maintained, not CLI-managed |
| OSP-RULE1 | Treat adoption popularity ("most loved", star/download counts) or self-hosted dogfooding as evidence the framework works | Rejected | Popularity and self-use are not measured efficacy; mechanism transfer requires reproduced local need |

## Falsifiability

- A reproduced local case where TeaPrompt's prose spec/plan artifacts demonstrably lose deltas on merge, or where an early-exit review order catches a failure the current ordering misses, would reopen OSP-DOC2/OSP-SK1 with a concrete gap.
- If TeaPrompt ever maintains versioned behavioral spec files of its own prompts, the delta grammar becomes actionable rather than dormant.

## Standing Non-Goals

- No runtime, Skill, prompt-body, routing, or governance change.
- No CLI install, no `openspec/` scaffold in this repo, no model call, no commit or push beyond this record and its catalogue row.
- OpenSpec's model recommendations, telemetry posture, and store beta were recorded as supplied; none of it authorizes adoption here.
