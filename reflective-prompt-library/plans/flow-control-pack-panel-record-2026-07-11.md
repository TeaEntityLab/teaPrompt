# Flow-Control Pack Panel Record — 2026-07-11

## Purpose

Record the parallel-lens discussion and decision for the request: **"according all surveys inside reflective-prompt-library/plans/, rethink about [the newly created flow-control skill pack]"** — an adversarial review of `skills/flow-control-generator/`, `skills/flow-loop-harness/`, and `plans/agent-flow-control-research-2026-07-11.md` before finalizing.

This record is governance / methodology evidence, not an agent operating rule. Its adopted candidates are tracked in the Candidate Adoption Ledger inside [agent-flow-control-research-2026-07-11.md](agent-flow-control-research-2026-07-11.md#panel-review-and-candidate-adoption-ledger-2026-07-11).

## Panel Packet

The review used the `parallel-lens-review-packet` protocol. A temporary shared packet was written to the repo root (`review-packet-flow-control-pack-2026-07-11.md`, deleted after synthesis) separating observed evidence, author-claimed evidence, and `[INFERENCE]`. State at review time: branch `main`, HEAD `d3a5ec7`, the three pack files staged and uncommitted.

Key observed evidence in the packet:

- `make all` FAILED with the pack in place: 5 failed / 745 passed — five guard tests assert the `skills/*/SKILL.md` disk count is exactly nine (`test_readme_governance`, `test_quality_gates_summary` ×2, `test_validate_governance`), so the frozen-nine surface is mechanically enforced, not prose-only.
- Same-day governance rethink (D1) had already flagged those count/phrase pins for replacement with registry-based contract checks.
- Prior panels repeatedly rejected new skills (reflective-panel; runtime-trust-boundary as ninth skill; STORM as method-not-skill); the promotion gate requires recurrence evidence plus explicit human approval; external interest is not local evidence.
- The pack's templates were author-claimed correct but unexecuted at packet time.

## Panel Lenses

Six reviewer lenses ran as parallel same-host subagent workers (no claim of distinct provider personas). All six returned `AGREE WITH CHANGES`; none returned `AGREE` or `DISAGREE`:

- Governance / promotion-gate auditor
- External-adoption methodology / evidence-tier auditor
- Runtime trust-boundary / security reviewer
- Minimality challenger
- Script correctness reviewer (executed /tmp reproductions)
- Routing fairness / discoverability reviewer

The host session independently executed all seven templates against stub agents on macOS bash 3.2.57 before and after fixes (rig transcript summarized under Evidence Actually Checked).

## Panel Consensus

**Decision:** `AGREE WITH CHANGES`

**Core finding:** The pack's mechanism is sound and the local gap is real but was over-labeled: it is a **user-directed Acquisition L2 exception** (explicit instruction supplies human approval; recurrence evidence is `unknown`, not zero), not a STORM-grade "verified" gap. The shipped-as placement violated the mechanically enforced nine-skill guard; the honest path is the Option B registry split the same-day governance rethink (D1) already pointed at — CORE_SKILLS (nine, frozen) vs registered DOMAIN_PACK_SKILLS — never a nested-directory evasion of the glob. The templates contained nine real bugs, one critical (parallel fan-in failed on its own happy path), proving the packet's honesty rule: an unexecuted script is author-claimed, not verified.

**Use-case recommendation:**

| Use case | Recommendation |
| --- | --- |
| `study` | Research record stands as reference for 2026-07 platform flow vocabulary (advisory tier; `[search-derived]` items must be re-verified before reliance). |
| `reproduce` | Templates are stub-dry-run verified on bash 3.2; reproduce via the rig procedure in each skill's Verification section before real runs. |
| `adopt` | Adopted as two registered domain-pack skills under the Option B guards, with demotion triggers; not core routing surface. |
| `deploy` | Unattended or side-effectful loop runs remain human-gated; host permission modes are a precondition the scripts cannot enforce. |

## Required Changes (all adopted 2026-07-11 unless marked deferred)

1. **Placement (Option B).** Register `DOMAIN_PACK_SKILLS` in `validate_skill_examples.py`; enforce in `validate_governance.py` (unregistered-directory error, domain-pack self-label, no core context-load row); amend the five count-pin tests to registry parity (`on_disk == CORE ∪ PACKS`, `len(CORE) == 9`); add `test_skill_map_lists_domain_packs` and `test_unregistered_skill_directory_fails_validation` guards. Rejected alternatives: `skills/packs/` nesting (evades `glob('*/SKILL.md')` in bad faith), repo-root placement (cohesion), lens-only demotion (conflicts with the explicit user instruction).
2. **Template bugs B1–B9.** B1 parallel wave double-wait (critical, happy-path failure) → per-pid `wave_wait`; B2 router label mangling → first-line + lowercase + truncate normalization; B3 fix-loop crash outside git repos → guarded `snapshot()`; B4 untracked-only progress missed → tracked-diff + untracked-count signal, verifier-output checksum fallback (documented limitation: a silent verifier disables non-git progress detection, so stuck loops exit via the cap); B5 backlog retire-line mismatch (duplicate task execution) → `grep -n` dispatch + `sed` exact-line retirement; B6 unenforced "agent must not edit backlog" → canonical copy under `state/`; B7 orchestrator crash on fenced JSON → `parse_plan()`; B8 plan-gate exit code → stderr + exit 2; B9 exit 4 (broken verifier) unimplemented → `[ -x "$VERIFY" ]` preflight. Rig follow-up during adoption: bash 3.2 did not deliver the exec-failure status (126) through `|| ec=$?` inside an `if fn;` condition (observed `ec=1`), so the wrapper-capture design was replaced by the deterministic preflight.
3. **Runtime-boundary wording C1–C6.** Ledger described as resume *convention* the host must honor (frontmatter + Methods); Acquisition claim corrected to "L2 exception with L3-style verifier artifact; full L3 requires `artifact-promotion.md` §4 fail-closed gates + replay evidence"; generator Escalation extended to privacy/permissions; permission boundary added to the generator Script Contract; verifier non-writability labeled a host-runtime precondition; §4 gates cross-referenced from both Verification sections.
4. **Evidence relabels.** "Verified gap" → "user-directed, structurally plausible, recurrence evidence unknown"; "all five vendors" / "every platform" absolutism scoped to the six surveyed sources; platform tables labeled advisory-tier reference vocabulary.
5. **Discoverability.** `skill-map.md` "Registered domain packs (not core routing)" table and an EN cheatsheet "Domain packs" section appended (test-safe: pinned gloss lines and boundary quick-cue block untouched); no `reflective-dispatch` route row; PROJECT_KNOWLEDGE Decision Index line added.
6. **Deferred / resolved items.** P6 merge-to-one-skill (Minimality dissent) — re-litigate if either skill sees zero solo invocations by 2026-10-11. P7 router/quick-cue integration — **resolved 2026-07-11 as no core-router integration** after three ROUTE-002/003 collision groups (9/9 phrases) passed pre-tune; see [decision record](p7-pack-routing-decision-2026-07-11.md). zh-TW cheatsheet parity — when the EN appendix is stable.

## Shared Findings

1. Every lens independently converged on Option B as the only honest placement; nested-glob evasion was unanimously rejected.
2. The strongest cross-lens agreement: deterministic guards, not prose, are what made this reviewable — the failing `make all` was the packet's most load-bearing evidence.
3. Execution evidence flips conclusions: two lenses' priors ("templates unverified = maintenance debt" vs "templates fine") were both replaced by the rig's nine concrete bugs and subsequent green runs.
4. The user-directed exception path (explicit instruction + demotion triggers + ledger) is now a precedented pattern for future externally-motivated additions.

## Disagreements / Residual Risks

- **Granularity:** Minimality lens holds one merged skill is sufficient and two directories duplicate contract boilerplate; Governance and Routing lenses hold the machine-readable `human_review_required` split (false for one-pass generation, true for loops) is load-bearing for host gating. Ruled: two skills, dissent preserved, deferred re-litigation trigger P6 recorded.
- **Evaluator-optimizer template:** Minimality wanted it cut (model critic contradicts the external-truth-layer principle); ruled: kept with an explicit advisory-tier caution, since bounded writer-critic rounds are a real user ask and `workflow-recipes.md` already carries the shared-error warning.
- **Resolved residual — trigger-phrase collisions:** `pipeline` / `orchestrate` / flow-script vocabulary is now covered by three P7 collision groups (9/9 pre-tune, no router defect); packs remain host-invoked and outside core routing. Re-open only on the successor trigger in the [P7 decision](p7-pack-routing-decision-2026-07-11.md).
- No fresh operator-usage data exists for the pack (it is new); every utility claim above template correctness is `[INFERENCE]` until the 2026-10-11 review.

## Evidence Actually Checked

- Executed (this session): `make all` before fixes (5 failed / 745 passed, failure text in packet) and after fixes (green — see research-record ledger); seven-template stub rig on bash 3.2.57 (`/tmp/flowpack-rig`): pipeline exit 0; parallel happy-path exit 127 pre-fix; router `Bug\n` → `ug` → fail-closed exit 2 pre-fix; fix-loop exit 129 in non-git dir and false exit 3 on untracked-only progress pre-fix; writer-critic ACCEPT round-2 exit 0; backlog duplicate-dispatch on leading blank line pre-fix; orchestrator exit 0; post-fix re-runs of all failure and success paths (0/2/3/4 reachability for loops).
- Read (lenses, targeted): the three pack files; governance-rules-rethink, workflow-possibilities-constraints, skills-runtime-legitimacy, external-adoption case studies, skills/memory/agent-tooling surveys, STORM and vLLM records, five-layer record, ponytail/project-adjustment reflections, multi-agent panel consensus (targeted sections), ROUTING_CONTRACT, QUALITY_GATES_SUMMARY, cheatsheet/skill-map, dispatch skill, runtime-trust-boundary, workflow-acquisition, artifact-promotion.
- Author-claimed, not reproduced: the research record's platform findings beyond the listed primary URLs; `[search-derived]` items (AgentKit wind-down date, native `/goal` loop) remain unverified.

## Falsifiability

This record is wrong if the pack's guards pass while an unregistered skill directory ships, if the adopted wording is absent from its named surfaces (ledger P1–P5), if P6 is never re-litigated when its trigger fires, or if P7's successor trigger fires without a new decision record. Any of those signals means the adoption ledger mechanism failed and the 2026-07-11 governance-rethink A1/A3 discipline must be re-applied here.
