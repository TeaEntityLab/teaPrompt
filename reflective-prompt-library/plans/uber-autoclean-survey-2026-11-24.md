# Uber AutoClean Survey — Agentic Feature-Flag Cleanup (2026-11-24)

Language: English
> **Status:** source-qualified reference record (`ACL-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.**

The owner asked to survey Uber's "Using AI to Delete Code" article and to update Docs or Skills where the survey supports it. This record preserves the primary sources, separates verified mechanics from self-reported outcomes, and maps the transferable distinctions onto existing TeaPrompt contracts. It does not install PolyglotPiranha, register a CodeCourt-like verifier, call a model, or authorize a flag-cleanup run. The useful mechanisms are already required by existing TeaPrompt contracts; no reproduced local gap was found.

## Research Question and Direct Recommendation

Which mechanisms in Uber's AutoClean pipeline are worth borrowing, and do they expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; do not adopt a runtime or add a Skill.** The transferable mechanisms are: a deterministic rewriter for the encodable part of the change (PolyglotPiranha simplifies the boolean logic; the agent handles context), a staged CI repair ladder (mechanical fixes first, a scope-limited agent second), post-CI verification because green CI does not prove semantics or test integrity, and per-concern verifier lanes instead of one generalist review. Each of these is already required by an existing TeaPrompt contract, so the outcome is a reference record, not a new deliverable.

## Evidence Used and Date Context

Checked 2026-11-24. Article: Uber engineering blog, "Using AI to Delete Code: Agentic Tech Debt Cleanup at Uber" (Daniel Ramos, Diego Marcilio, Nikhil Parasaram), published 2026-10-20, read via the `uber.com/tw/en/blog/ai-code-cleanup/` mirror. Two primary papers were read for the underlying tool's guarantees; the pinned `uber/piranha` README was read for current project status.

| Item | Identity | What this check covers |
| --- | --- | --- |
| AutoClean article | Uber blog, 2026-10-20 | Pipeline claims, Figure 2/3 mechanism split, adoption totals |
| PLDI 2024 paper | "A Lightweight Polyglot Code Transformation Language" (Ketkar, Ramos, Clapp, Barik, Ramanathan) | Transformation-correctness limits; 233 failing-PR analysis |
| ICSE-SEIP 2020 paper | "Piranha: Reducing Feature Flag Debt at Uber" | Flag lifecycle: a fully rolled-out flag can still be a kill switch |
| `uber/piranha` repo | `master` `4877ea2` | Current README, Apache 2.0, "not an official Uber product, provided as is" |

## What the Article Actually Claims

- AutoClean starts from the feature-flag system of record, identifies a stale flag, and produces a tested diff for human review. Agents rewrite the code around the flag; **PolyglotPiranha performs the boolean/conditional simplification** — the deterministic part is not delegated to the model.
- CI failures go through a repair ladder: a mechanical repair pass first, then a scope-limited agentic fixer, each bounded by attempt counts.
- After CI is green, deterministic static checks run, then **CodeCourt-style per-concern verifiers**: no new functionality, semantics preserved, no drift from the target flag, no agent artifacts left behind. Any failed verifier abandons the diff; passing diffs still go to human review.
- Self-reported cumulative totals: **16,000+ stale flags** and **1M+ lines** cleaned "over the past few years". The article gives no per-version or per-layer split, so the totals cannot be attributed to the LLM stages alone.
- "Specialized reviewers outperform a single reviewer" is stated as a practice judgment; no comparison data, error rates, cost, or latency are published.

## Evidence vs Inference

- **Verified from primary sources:** the pipeline shape and verifier lanes above; PolyglotPiranha's own limitation section (no compile/semantic-correctness guarantee; no SSA/def-use precision, no type resolution, no call-graph analysis); the 233-PR CI-failure analysis in the 2024 paper with **23 PRs (9.9%) failed by over-deletion from unsound rules**; the 2020 paper's warning that a fully rolled-out flag can remain an emergency kill switch.
- **Supplier-summarized (unverified):** the 16,000-flag/1M-line totals, the specialized-reviewer superiority claim, and the figure-level assertion that CI verification "catches" semantics/test-deletion issues — the article presents these as design intent and outcomes, not measured rates.
- **Inference (this record):** the contract-map dispositions; the judgment that existing TeaPrompt contracts already cover the transferable duties. Uber's internal flag system, SubmitQueue, and CodeCourt implementation were not inspected.
- **Unknown:** the actual verifier prompts/rubrics; AutoClean's false-positive and abandonment rates; how much of the 16k total predates the agentic stages.

## TeaPrompt Contract Map and Disposition

| Finding | Existing surface | Disposition |
| --- | --- | --- |
| A fully rolled-out flag can still be a kill switch; "value is constant" ≠ "safe to delete" | `reflective-minimality` debt/shortcut audit; `reflective-risk` for destructive ops | Existing contract covers; flag-lifecycle nuance is a deferred doc note, not a missing rule |
| Green CI does not prove tests were not wrongly deleted or semantics preserved | `reflective-review` test-integrity checks; "the finding disappearing because its subject was deleted is not a successful repair" | Already required; the AutoClean figure is a worked illustration, not a new rule |
| Deterministic rewriter for encodable transforms; model kept out of the simplification path | `runtime-trust-boundary.md` §3-4a (tool output vs authority); `reflective-implement` smallest safe change | Same division of labor already pointed to; no edit needed |
| Per-concern verifier lanes over one generalist verdict | `governed-delivery` oracle manifest + decorrelated verification; `verification-map-generator` VERIFY.md | Restates existing contract; parallel model lanes alone are not independent evidence — same-model blind spots apply |
| Bounded agentic repair after deterministic repair | `flow-loop-harness` external verifier + caps; host enforces, TeaPrompt does not run it | Reference only; TeaPrompt ships methodology, not the runner |
| Flag-cleanup as an industry workflow | `agent-ecosystem-harness-survey-2026-10-11.md` already records DoorDash's flag-cleanup report with source qualifications | Consistent precedent; this record adds the Uber primary source |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| ACL-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Refresh when a follow-up article, verifier data, or Piranha release changes the pinned facts |
| ACL-DOC2 | Optional worked reference in review examples (rolled-out flag still a kill switch; CI green while tests were wrongly deleted) | Deferred | No reproduced local gap; existing `reflective-review` wording already requires test-integrity and deletion-declining checks |
| ACL-SK1 | New flag-cleanup or agentic-deletion Skill | Not adopted | No verified local structural gap; TeaPrompt has no runner and existing contracts cover the duties |
| ACL-RUN1 | Install PolyglotPiranha or build a CodeCourt-like verifier host | Not adopted | Host/product implementation; `uber/piranha` is "not an official Uber product, provided as is"; a local consumer defect was not reproduced |
| ACL-RULE1 | Adopt "no new additions" as a literal no-`+`-lines rule, or treat "all model verifiers pass" as independent evidence | Rejected | The article's own figure narrows it to "no new functionality"; parallel model verdicts share blind spots and are not decorrelated evidence |

## Falsifiability

- A reproduced local failure — e.g., a flag-cleanup task where the existing prompts demonstrably fail to flag kill-switch semantics or wrongly-deleted tests — would reopen ACL-SK1/ACL-DOC2 with a concrete gap.
- Published Uber verifier comparisons (per-concern vs single reviewer) would upgrade the practice claim from supplier-summarized to verified; absence keeps it qualified.
- This survey ran no installs, no model calls, and no flag deletions; it cannot certify AutoClean's actual rates, only that the article and papers say what is recorded here.

## Standing Non-Goals

- No runtime, Skill, prompt-body, routing, or governance change.
- No PolyglotPiranha install, CodeCourt reimplementation, model call, commit, or push beyond this record and its catalogue row.
- The article's cost, latency, and reviewer-accuracy figures remain supplier claims; this record does not endorse them as measured facts.
