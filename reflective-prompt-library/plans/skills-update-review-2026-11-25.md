# Skills Update Review — Three-Role Adjudication (2026-11-25)

Language: English
> **Status:** adjudication record (`SUR-DOC1`); two in-place contract repairs landed, no new Skill or surface.**

The owner asked whether the current skills need updates, evaluated by evidence-based Socratic critical thinking in multiple parallel roles. Three reviewer agents — Evidence Auditor, Gap Advocate, Minimality Advocate — independently read the nine frozen skills and the deferred-note queue accumulated across the 2026-11-13→2026-11-25 survey series (CFT/ACL/CKB/UAS/ALV/OSP/CMP-DOC2 items). This record adjudicates their disagreement, lands the two repairs that survived, and confirms the rest stay deferred.

## Verdict Summary

| Candidate | Evidence Auditor | Gap Advocate | Minimality Advocate | Adjudicated |
| --- | --- | --- | --- | --- |
| Frankenquote/misattributed verbatim-quote fidelity (CKB-DOC2) | defer (covered) | **adopt — highest** | defer (covered) | **ADOPTED** — existing check could pass stitched/misattributed quotes |
| Friction Notes handoff row (UAS-DOC2b) | adopt | adopt (weak) | defer (covered) | **ADOPTED** — papercut-style capture is the prompt-layer analog; one template row |
| Periodic skill ablation (UAS-DOC2 + ALV-DOC2) | defer | adopt (narrowed, doc surface) | defer | Defer — no eval substrate; narrowed clause lands only when retirement-trigger surface exists |
| Quit-earliest review order (OSP-DOC2a) | adopt (borderline) | defer | defer | Defer — efficiency not correctness; wrong-surface (examples not contract) |
| Supply-chain vetting checklist (CMP-DOC2) | defer | defer | defer | Defer — dormant; gates exist at artifact-promotion §4 and reflective-risk §122 |
| Spec-delta grammar (OSP-DOC2b) | reject for now | defer | defer | Reject/dormant — no spec files to merge |
| Kill-switch / domain-pack coverage check | covered | covered | covered | Confirmed — no edit |

## What Landed

1. **`reflective-review` Four Evidence Dimensions — Number/text row** now requires *verbatim and contiguous* match and names the three failure modes (fabricated / frankenquote / misattributed), with the deterministic-substring-first order. Gap: the previous text asked whether "the source's own body support[s] the exact figure and wording" — each stitched fragment of a frankenquote *does* appear in the source, so a reviewer could mark `verified` on a mechanically-decidable defect. Two of three roles missed this; Gap Advocate's steelman (MiniMax +2 anchor-drift precedent) held.
2. **`reflective-handoff-retro` Handoff template** gained `## Friction Notes — one line each: tried / expected / actual / suggested fix (or "None")` between `Blockers` and `Acceptance Criteria`. Gap: resolved-but-unrecorded mid-task friction evaporates before the retro template's `Reusable Rules`/`Weak Gates` can see it — the signal feeding the repo's own lesson pipeline (`verification-map-generator` step 1) had no slot.

## What Stayed Deferred and Why

- **Ablation**: two-source corroborated but no eval runtime exists to run it; the `skill-dogfood-test-plan` paired eval already closed inconclusive. The narrowed clause (retirement-trigger recheck on version-generation change) lands when a maintainer surface exists to satisfy it — not on a frozen skill.
- **Review order**: OpenSpec's order is an efficiency heuristic; reflective-review already front-loads requirement/acceptance, so the only plausible failure is contrived context-budget exhaustion. If ever wanted, it belongs in `skills/examples/`, not contract.
- **Supply-chain vetting**: artifact-promotion §4 + reflective-risk §122 already fail closed on provenance/license/SBOM/telemetry and prompt-injection authority. Reopens on the first actual third-party import.
- **Spec-delta grammar**: dormant by construction; TeaPrompt maintains prose artifacts, not mergeable spec files.

## Evidence vs Inference


- **Verified:** both edits applied and diffed; the three reviewer verdicts delivered independently; the MiniMax anchor-drift precedent (PROJECT_KNOWLEDGE.md:220) supports the frankenquote check; `artifact-promotion.md` §4, `runtime-trust-boundary.md`, `reflective-risk` §122, `verification-map-generator` §Maintenance Rule all read directly.
- **Supplier-summarized:** Uber ablation figures, Cherny quote (verified as quoted, still advice), `agent-skill-vet` existence (Reddit discourse, not audited), OpenSpec "30+ tools" claim.
- **Inference:** that the two landed edits are the correct narrowest repairs; that deferred items have correctly-formed reopen triggers.
- **Unknown:** whether the verbatim-check wording measurably changes reviewer behavior on real citation-heavy artifacts; whether periodic ablation would catch drift the event-driven maintenance gate misses (untestable without an eval surface).

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| SUR-DOC1 | This adjudication record | Adopted; documentation only | Refresh if a deferred item's reopen trigger fires or the three-role method changes |
| SUR-ED1 | `reflective-review` verbatim/contiguous quote fidelity (fabricated/frankenquote/misattributed) | Adopted in place | If stitched/misattributed quotes still pass `verified`, elevate to a checkable example |
| SUR-ED2 | `reflective-handoff-retro` `## Friction Notes` template row | Adopted in place | If entries collapse to boilerplate `None`, scope to friction-resolving handoffs |
| SUR-AB1 | Periodic skill ablation (two-source corroborated) | Deferred | No eval substrate; reopen on a measured regression or a retirement-trigger surface |
| SUR-RV1 | Quit-earliest review-order example | Deferred | Efficiency not correctness; would land in `skills/examples/`, not contract |
| SUR-SC1 | Third-party skill supply-chain vetting checklist | Deferred | Reopens on the first actual third-party skill import proposal |
| SUR-SD1 | Spec-delta grammar for mergeable spec files | Rejected/dormant | Requires a spec-file discipline TeaPrompt does not maintain |

## Falsifiability

- If a citation-heavy review still marks stitched/misattributed quotes `verified` under the new wording, the Number/text row needs the failure modes elevated to a checkable example (the deferred worked-reference destination).
- If the friction-notes row accumulates boilerplate `None` entries that carry no signal, scope it to handoffs that actually resolved friction.
- If a TeaPrompt skill is ever measured regressing, the ablation note promotes from deferred to the artifact-promotion retirement-trigger surface.

## Standing Non-Goals

- No new Skill, domain pack, example, route, runtime, or gate.
- Prior per-survey dispositions (CFT/ACL/CKB/UAS/ALV/OSP/CMP) unchanged; this record adjudicates the deferred queue, it does not re-litigate them.
