# Routing Holdout Expansion Plan — 2026-07-11

> **Status: active planning artifact plus execution ledger (non-authoritative).**
> H1/H2/H5/H6 and the P7 collision groups are adopted; H3/H4 remain deferred.
> The work began as design pre-work motivated by the
> [2026-07-11 survey](../../surveys/agent-skills-flow-control-survey-2026-07-11.md)
> and follows [ROUTING_CONTRACT](ROUTING_CONTRACT.md) R8 plus the observed
> pre-tune procedure from
> [Adoption Update 3, P1](governance-rules-rethink-review-2026-07-11.md#adoption-update-3-2026-07-11).
> P7/N12 consumed the evidence and resolved no core-router integration in the
> [successor decision](p7-pack-routing-decision-2026-07-11.md).

## Rules this plan operates under (pointers)

- **R8 holdout-before-tune:** candidate phrases are routed against the *untuned*
  router first; observations recorded; the fixture group is added; only then may
  a router rule change, and only if a meaningful boundary actually fails.
- **Floors ratchet:** `validate_route_fixture.py` minimums only go up
  (currently ROUTE-002 ≥44 groups/124 phrases; ROUTE-003 ≥22 groups/76 phrases).
- **P7 is decided by its successor record:** these fixtures test that
  pack-adjacent vocabulary does not destabilize the nine core routes. Nine fresh
  collision phrases passed pre-tune, so `reflective-dispatch` does not route to
  packs; the packs remain host-invoked.
- **Parity mechanics:** any adopted group follows the
  [playbook](../GLOSSARY.md#governance-maintenance-playbook--治理維護手冊) items
  6–8 (probe tuples, EN/zh-TW cheatsheet cues, CONTRIBUTING R8–R12 sync).

## Candidate ROUTE-003 groups (adversarial traps)

Every "expected" below is a **hypothesis** until the pre-tune observation run;
`unknown` means the plan deliberately refuses to guess.

### H1 `goal_mode_not_plan_trap`
- Risk being probed: continue-until-done phrasing drifting to `reflective-spec-plan`
  or `reflective-dispatch` instead of execution.
- Candidate phrases: "keep working until every test in test/auth passes";
  "don't stop until lint is clean and the build exits 0"; "finish the migration
  — completion means zero deprecated imports left"; zh-TW variant: 「持續修到整個
  測試套件全綠為止」.
- Expected (hypothesis): `reflective-implement` — these are delivery asks with a
  verifiable end state, the R11 approved-spec family's nearest neighbor.

### H2 `loop_script_authoring_trap`
- Risk being probed: explicit script/runner loop requests — the packs' home
  turf — misrouting to workflow-design planning when the user wants code.
- Candidate phrases: "write a bash loop that reruns the agent until the
  verifier passes"; "generate a fix-until-green script with an iteration cap";
  "script a writer-critic round harness".
- Expected (hypothesis): `reflective-implement` (executable-artifact authoring),
  with the pack reachable via the host, not via a dispatch route row. This
  group's observations are direct P7 evidence.

### H3 `scheduled_check_boundary_trap`
- Risk being probed: recurring/scheduled phrasing ("every morning", "nightly")
  splitting inconsistently across brief/spec-plan/implement.
- Candidate phrases: "run the dependency audit every morning and report
  drift"; "set up a nightly loop that checks the deploy finished".
- Expected: **unknown** — genuinely ambiguous between workflow design
  (`reflective-spec-plan`) and implementation; the observation run decides
  whether a boundary rule is even needed.

## Candidate ROUTE-002 groups (holdout)

### H4 `skill_authoring_holdout`
- Phrases: "write a SKILL.md for our deploy process"; "turn this checklist into
  an agent skill"; zh-TW: 「把這份 SOP 做成一個 skill」.
- Expected (hypothesis): `reflective-spec-plan` when the procedure itself needs
  design (SOP-compiler framing), `reflective-implement` for verbatim
  transcription — the observation run must show which signal dominates; if the
  split is unstable, that is a real boundary finding, not a tuning license.

### H5 `skill_install_holdout`
- Phrases: "install these skills into .agents/skills for the whole team";
  "symlink the skill pack into my user skills directory".
- Expected (hypothesis): `reflective-implement` (mechanical, low strictness).

### H6 `goal_condition_design_holdout`
- Phrases: "help me write a completion condition the evaluator can actually
  judge"; "what's a falsifiable end state for this refactor goal?".
- Expected (hypothesis): `reflective-brief` (acceptance-criteria/falsifiability
  shaping) — a useful probe that brief does not collapse into implement when
  "goal"/"refactor" vocabulary appears.

## Execution checklist (for the change that adopts any of H1–H6)

1. Pre-tune observation: route every candidate phrase against the current
   router; record actual route + confidence per phrase (the P1 procedure).
2. Select groups where observations are stable or reveal a meaningful boundary;
   drop or rewrite the rest — fixture quality over count.
3. Add fixture groups; bump `validate_route_fixture.py` floors to the new
   counts; mirror probe tuples and EN/zh-TW cheatsheet cues (playbook 6–8);
   sync CONTRIBUTING routing-maintenance wording if boundaries changed.
4. Tune router rules **only** for boundaries that failed with recorded
   observations; re-run `make all` from the repository root.
5. Record the outcome (including "no tune needed") in this file's ledger below
   and a PROJECT_KNOWLEDGE Decision Index entry.
6. Hand the observation set to the P7/N12 re-litigation as its holdout
   evidence.

## Ledger

Executed 2026-07-11 (user-approved survey implementation). Pre-tune observation
run against the untuned router, then adoption per the checklist; post-tune all
adopted phrases route as canonized; `make all` green (790 pytest, ROUTE-001/002/003
at 100% with floors raised to 42/118 and 21/73).

| Group | Status | Observation evidence (pre-tune → post-tune) | Fixture change |
| --- | --- | --- | --- |
| H1 `goal_mode_not_plan_trap` | **Adopted (ROUTE-003)** | scattered risk/implement/dispatch (conf 0.30–0.50) → implement 0.80–0.90; the `test/auth` path fragment falsely triggering the risk guard was the observed defect (guard keyword `auth` dropped) | +4 phrases; router `goal_delivery` boundary (+4 implement, risk-context guarded) |
| H2 `loop_script_authoring_trap` | **Adopted (ROUTE-003)** | implement/dispatch fallback (0.30–0.50) → implement 0.80–0.90 | +3 phrases; router `loop_script` boundary |
| H3 scheduled-check | **Deferred** | minimality + review scatter; canonical route genuinely ambiguous (design vs implement) — forcing a route would be fixture-fitting | none; revisit on real scheduled-check misroute reports |
| H4 skill-authoring | **Deferred** | dispatch/review scatter; spec-plan vs implement contested (sop-compiler framing vs transcription) | none; revisit with real skill-authoring demand |
| H5 `skill_install_holdout` | **Adopted (ROUTE-002)** | dispatch fallback ×2 (0.30) → implement 0.80 | +2 phrases; router `skill_install` boundary |
| H6 `goal_condition_design_holdout` | **Adopted (ROUTE-002)** | brief/dispatch split → brief 0.80–0.90 | +2 phrases; router `completion_condition` boundary |

Parity executed per playbook: two new ROUTE-003 canonical probes in
`tests/test_validate_route_fixture.py` (flowing into EN/zh-TW cheatsheet parity
tests); implement-section trigger cues added to both cheatsheets; quick-cue
summary untouched (Round 66 expansion rejection honored); floors bumped in
`validate_route_fixture.py`; QUALITY_GATES counts synced. These observations
fed the P7/N12 re-litigation below.

## P7/N12 execution update (2026-07-11)

User-authorized re-litigation added three fresh groups after a pre-tune
observation against the unchanged router:

| Group | Fixture | Pre-tune observation | Change |
| --- | --- | --- | --- |
| `pack_vocab_plan_holdout` | ROUTE-002 | 3/3 → `reflective-spec-plan` (100%) | +3 phrases |
| `pack_vocab_route_holdout` | ROUTE-002 | 3/3 → `reflective-dispatch` (100%) | +3 phrases |
| `pack_vocab_implement_not_plan_trap` | ROUTE-003 | 3/3 → `reflective-implement` (100%) | +3 phrases |

No boundary failed, so no router rule, `VALID_WORKFLOWS`, dispatch row, or
quick-cue changed. Floors rose to 44/124 and 22/76. P7/N12 resolved as
**no core-router integration**; see the
[decision record](p7-pack-routing-decision-2026-07-11.md).

## Falsifiability

This plan fails its purpose if any router rule lands before its observation run
(R8 violation); if the P7 successor decision is cited without the initial H1–H6
and later 9-phrase observations; or if H3/H4 land before their genuinely
ambiguous boundaries are decided from real evidence.
