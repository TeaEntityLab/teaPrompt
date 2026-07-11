# STORM Perspective-Discovery Reflection — 2026-06-18

> **Status: historical record (retired from active guidance, 2026-07-11).** Kept for provenance and as Decision Index / Durable Lesson evidence. Wording may predate the nine-skill surface and current governance; do not cite as current policy — see `PROJECT_KNOWLEDGE.md` Decision Index for live decisions.


## Dispatch

Decide, from intent, whether TeaPrompt should learn anything from Stanford
OVAL's STORM / Co-STORM, and if so make the minimal change.

## Assumptions

- One-hand sources: the STORM GitHub README, the NAACL 2024 paper, the EMNLP
  2024 Co-STORM paper. The circulating "4 prompts = STORM" article is a
  second-hand re-telling and is treated as such.
- The question is about TeaPrompt's *research method*, not about importing a
  product (runtime, CLI, retrievers, citation pipeline, mind map).

## Evidence Ledger

| Claim / Item | Source | Status | Note |
| --- | --- | --- | --- |
| STORM's core move is perspective-guided question asking + grounded simulated conversation, derived from related articles rather than fixed roles | STORM README; NAACL 2024 | verified | This is the transferable idea |
| STORM reports ~25% more organized, ~10% broader coverage vs. baseline, judged by 10 Wikipedia editors | NAACL 2024 | verified | Relative to a specific baseline; not proof of "PhD-level" output |
| STORM itself flags source-bias transfer and over-association of unrelated facts | NAACL 2024 | verified | Citations are not verification |
| `reflective-research` workflow assumes a well-formed question and has no question-space-expansion step | reflective-research/SKILL.md | verified | The real local gap |
| `research.md` has `Competing Views`/`Unknowns` but no blind-spot (gap no view touched) output | 05-domain/research.md | verified | STORM's highest-value output was missing |
| "4 prompts = STORM", fixed 5-perspective/3-question quotas, "always ask before answering" | circulating article | refuted | Over-simplification; quotas optimize count over evidence; not a general agent rule |

## Findings

- Genuine gap: TeaPrompt could research a broad/unfamiliar topic without ever
  expanding the question space or naming blind spots, because the question is
  assumed well-formed.
- Not a gap: evidence ledger, source hierarchy, evidence/inference split,
  falsifiability, and review are already present and are stronger than the
  article's "self peer-review" prompt.

## Decision

Adopt STORM's mechanism, reject its product form. Fold *source-grounded
perspective expansion* into `reflective-research` as an **optional** method,
triggered only for broad or unfamiliar scopes, with two faithful constraints:

1. Perspectives are derived from observed sources, not assigned role-play.
2. No fixed quota of perspectives or questions.

A blind-spot output is added to `research.md`, and the Sufficiency Gate now
requires that, when expansion was used, the synthesis names the competing
perspectives and the blind spot (or states none were found) — making the
mechanism auditable and falsifiable.

## Rejected Alternatives

- A new `R-STORM` skill: rejected — surface-area inflation; the promotion gate
  (three cross-session recurrences) is not met and an existing skill already
  owns research. See [[PROJECT_KNOWLEDGE]] Durable Lessons.
- Importing STORM/Co-STORM runtime, retrievers, or citation pipeline: rejected —
  conflicts with the project's standing non-goals (no runtime engine, no RAG
  store).
- Mandatory perspective expansion on every research task: rejected — imposes
  cost on narrow, well-formed questions where the question space is already clear.
- Fixed quotas (5 perspectives × 3 questions × 2–3 sources): rejected —
  optimizes count, not evidence sufficiency.

## Falsifiability

This change is wrong if, in practice, the optional step fires on narrow
questions where it adds nothing, or if perspectives are produced as role-play
detached from sources. Either signal means tighten the trigger or remove the
method. There is not yet a local controlled case proving TeaPrompt's prior flow
missed an important perspective; the change rests on the verified structural gap
plus external (NAACL) evidence, and remains optional pending such a case.

## State Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Optional method added to reflective-research | done | SKILL.md Methods + Workflow step 3 |
| Sufficiency gate made auditable for expansion | done | SKILL.md Sufficiency Gate |
| Blind-spot output added | done | 05-domain/research.md |
| Decision recorded and indexed | done | this file + PROJECT_KNOWLEDGE.md Decision Index |
