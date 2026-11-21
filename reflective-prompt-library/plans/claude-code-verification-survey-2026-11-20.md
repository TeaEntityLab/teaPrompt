# Claude Code Verification Survey — Team Practice and Contract Map (2026-11-20)

Language: English

> **Status:** source-qualified reference record (`VER-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner supplied the Anthropic-published article "How the Claude Code team thinks about verification" (Addy Osmani, claude.dev, 2026-11-16). This record checks its mechanisms against TeaPrompt's existing contracts; it is a single-team practitioner account on a vendor blog, not a measured benchmark. No install, model call, Skill change, commit, or push is authorized.

## Research Question

Which mechanisms in the article are already held by named TeaPrompt surfaces, which are practitioner practice worth recording as reference, and does anything expose a verified local gap?

## Direct Recommendation

**Adopt the record only.** The article describes verification practices for a hosted agent product; some match TeaPrompt methods, others are team-specific. Its most useful example is how the team selects checks: each of its reported 39 checklist items links a pattern visible in a diff to a check and an incident. This is a candidate worked reference, not evidence that TeaPrompt needs or runs that checklist.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| [claude.dev verification post](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/) | **Primary** — full article text (markdown alternate), published 2026-11-16, authored Addy Osmani | Verbatim basis for every claim below |
| [Solving code review at Anthropic](https://claude.dev/blog/solving-code-review-at-anthropic/) (linked) | Companion primary (not separately fetched; cited only as linked context) | Prior review-system post this article deepens |
| Prior TeaPrompt records | `agent-ecosystem-harness-survey-2026-10-11.md` (AE-05 inert candidate), `addy-osmani-agent-management-survey-2026-11-09.md` (AOM), `agentflow-8.4.1-delta-survey` v9.1.12 adaptive-verification | Baseline for the contract map and the "second recurrence" gate |

**Qualifications on the source:** vendor blog authored by a team member describing his own team's internal pipeline; the "~90% of code written/reviewed by Claude" figure, the "up to 10 points" internal-test gain, the 39-item checklist size, the three-round threshold and the revert/reject metrics are all **self-reported**, not independently measured. The linked internal-test claim (`claude-managed-agents`) is not reproduced here.

## Claim Fidelity and Contract Map

| # | Article mechanism | Transcript check | TeaPrompt surface | Disposition |
| --- | --- | --- | --- | --- |
| 1 | E2E tests first: real user flows, definitive done criteria, screenshots/traces; unit tests can pass while the feature breaks | Verbatim | [reflective-review](../skills/reflective-review/SKILL.md) evidence tiers ("a green run proves its tested assertions, not operational behavior"), browser verification duty | Already present — same claim, stronger oracle statement |
| 2 | Property tests (round-trip, invariants, idempotence, equivalence); edge cases the authoring agent didn't bias toward | Verbatim | `test-designer`, anti-cheating oracle separation | Already present at method level |
| 3 | Differential tests for migrations: old system = oracle, sampled traffic, normalization | Verbatim | Old-bytes differential driver (2026-10-01 advisory pass); golden-benchmark paired runs | Already present — direct local precedent |
| 4 | `verify` skill in `.claude/skills/`, per-repo, iterated to reliability | Verbatim | Skill-as-procedure convention; smoke-test harness pattern | Already present — skill packaging, no contract gap |
| 5 | Failing tests escalate to human after **three** rounds | Verbatim | Stop-conditions in flow-loop-harness; Human Review Required | Adjacent — a numeric threshold is a tuning choice, not a rule TeaPrompt must adopt |
| 6 | Code owners write their own checks; check explains why it pulled a reviewer | Verbatim | Owner-defined acceptance, oracle authorship | Already present |
| 7 | **Diff-trigger reliability checklist**: 39 items, each `trigger (readable from diff) → check → linked incidents/PRs`; only matching items run (3–10 typical) | Verbatim | [verification-map-generator](../skills/verification-map-generator) VERIFY.md control docs; incident-ledger pattern | **Closest candidate** — a worked, source-attested instantiation; reference material, not a new rule |
| 8 | `REVIEW.md` per-repo reviewer attention; rounds build on prior context/failures | Verbatim | reflect-review scope packets; context-handoff | Already present — same idea at record level |
| 9 | Changes can't modify their own checks: `REVIEW.md` read from base branch, never the PR | Verbatim | AGENTS "oracles are read-only during a run… host write protection or CI ownership must" | Already present and stronger — TeaPrompt pins the boundary as invariant |
| 10 | Cheap checks before shared review/CI; commit gate off/observe/enforce; verification stamp (incl. `"none"`) on each commit; blocked-twice → allow so agent isn't stuck | Verbatim | flow-loop gate sequences; evidence ledgers | Adjacent — product-workflow detail; observe-before-enforce is a good rollout pattern already implicit in gates |
| 11 | Reviewer-of-reviewers: track merged-reverts, maintainer rejects, size-matched clean subset; formal eval on recreated repo state + one-sentence answer key; separate raw/post-verification/final recall; tuning/stopping at overfitting | Verbatim | `golden-benchmark` methodology; test-designer failure-signal design; incident→regression-test duty | Already present at methodology level; the separate-stage recall decomposition is a practitioner detail worth noting |
| 12 | Turn misses into rules: pattern needs ≥2 PRs + diff-identifiable; 3 agents try to disprove; human PR approval; replay 3 finders vs known-incident PR, ≥2 detections = detectable; flaky-test rule (can't skip/sleep/retry; if unfixable, delete and record why); prune rule sets | Verbatim | incident→rule admission gates; durable-lesson review; flow-control fail-closed | Already present — the ≥2-incident threshold and adversarial-disprove step match local adoption gates |
| 13 | Verification loops enable delegation at scale ("one or two" → "dozens or hundreds" of Claudes) | Verbatim | Parallel dispatch governance; review capacity as constraint (AOM S1) | Already present — restates the same capacity argument |
| 14 | "~90% of code written/reviewed by Claude"; "up to 10 points" internal gain | Verbatim | — | **Self-reported vendor figure** — record as claim, not measurement |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| VER-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected article, a linked companion source with divergent claims, or a new digest version |
| VER-DOC2 | Optional worked reference: a `REVIEW.md`-style checklist in `verification-map-generator`, citing this article | **Deferred** | A second independent source must show a diff pattern selecting a specific check linked to a past incident, or a local review must show a need for that selection rule. A mutation test alone does neither. |
| VER-SK1 | Skill or prompt-body change encoding the article's mechanisms | **No change** | A reproduced defect in a named local review or verification procedure that the proposed change would address |
| VER-RULE1 | Numeric thresholds (3 strikes, 39 items, ≥2 incidents, ≥2/3 finders, 90%/10-point figures) as operating rules | **Rejected** | Practitioner tuning values and self-reported vendor metrics; not invariant rules and not locally verified |
| VER-RUN1 | Reproducing the internal verify/commit-gate pipeline | **Not adopted** | Separate scoped host evaluation; the article is descriptive, not a shipped artifact |

## Evidence vs Inference

- **Verified (article text):** every mechanism in the table; publication date and author.
- **Verified as self-report only:** ~90% code-authored figure, 10-point internal gain, 39-item checklist count, three-round threshold, revert/reject/eval metrics — single-team account, no reproducible data.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; the VER-DOC2 deferral call; classifying the diff-trigger checklist as the closest candidate.
- **Unknown:** whether the 39-item checklist, commit stamps and observe/enforce gate exist in publicly inspectable form; whether the linked internal-test gain survives independent reproduction; whether the mechanisms described match actual Claude Code release behavior (the article describes team practice, not a shipped config).

## Falsifiability, Risks, and Handoff

- This is vendor-published practitioner advocacy for its own product; treat efficacy figures as marketing-adjacent, not measured. The mechanisms themselves are conventional and independently defensible.
- AE-05 asks whether a check catches an injected fault. VER-DOC2 asks which check a change should trigger and which past incident justifies it. A mutation test could be the selected check; that does not make a second mutation example evidence of the selection rule.
- No Skill/runtime/prompt-body changes; catalogued via the external-adoption case file and `index.json`.
