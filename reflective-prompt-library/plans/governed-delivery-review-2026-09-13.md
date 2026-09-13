# Governed Delivery — Independent Review Record — 2026-09-13

> **Status: decided (non-authoritative); review record.** The deferred GD-18 independent post-land panel for the [governed-delivery adoption](governed-delivery-adoption-2026-09-03.md). Five read-only scout lenses reviewed the pack, the adoption record, the guard, and the admission surfaces against a shared packet (`review-packet-governed-delivery-2026-09-13.md`, deleted after synthesis). Authority chain unchanged: `06-repo/AGENTS.md` and invoked `SKILL.md` contracts govern; this record is evidence, not an operating rule.

## Panel Consensus

- **Decision:** AGREE WITH CHANGES — 5/5 lenses. The adoption's architecture (Option C layering, clean-room restatement, off-dispatch registration, host-precondition honesty, disclosed composite self-acceptance) is sound; every required change landed in this commit.
- **Use-case recommendation:** adopt (as already landed); the pack stays a host-invoked domain pack.

## Required Wording Changes (all applied)

| # | Change | Lens | Surface |
| --- | --- | --- | --- |
| R1 | Stale-propagation covers every spec_version-keyed artifact (plan items, ledger entries, oracle manifest, task packet, acceptance record), not just plan items + ledger entries | Contract | pack gate-table footer, GDR-6, `reflective-spec-plan` anchor B2, guard `ANCHORS` |
| R2 | Execution auto-release restricted to deterministic packet-binding/ledger-currency checks; self-report adherence never auto-releases | Contract | pack gate table `execution` row |
| R3 | Auto-release keys off condition determinism, not evidence tier | Contract | pack gate-table footer |
| R4 | "Nine core skills / 42 lines" corrected to eight skills / 41 insertions (git `1e4f960` numstat; reflective-dispatch untouched); stale char counts refreshed | Evidence | adoption record lines 11, 102–103 |
| R5 | Recurrence demotion trigger made falsifiable: named host-supplied channel; unmeasured recurrence stays `unknown`, and a skipped/unrecorded checkpoint triggers demotion as a policy consequence of missing evidence, not as an observed zero | Minimality + Evidence | adoption record + pack Demotion Triggers; Falsifiability item 5 restated to the demotion *decision* |
| R6 | Redundancy-in-use trigger added for GD↔agent-governance-scaffold boilerplate divergence | Minimality | adoption record + pack Demotion Triggers |
| R7 | Guard pins pack absence from all three ROUTE yamls + ROUTING_CONTRACT.md (structural isolation; not a fixture edit — GD-19 respected) | Registry | `test_gd17_absent_from_route_fixtures` |
| R8 | Clean-room scan broadened from `skills/*/SKILL.md` to all installed surfaces (examples, skill-map, both cheatsheets, both install guides); regex extended with I1–I9 inequality strings and corpus figures | Clean-room | `test_clean_room_tokens_absent_from_all_installed_surfaces`, `CLEAN_ROOM_FORBIDDEN` |
| R9 | skill-map trigger-fairness line now names the pack's collision words (deliver/autonomous/unattended) | Registry | `skills/skill-map.md` |

## Shared Findings

- No enforcement overclaim anywhere: sealing, isolation, budgets, ledgers, and the human channel are correctly attributed to the host on every surface (observed, all lenses).
- All nine contract-template invariants match their Methods/Never text; no template field contradicts its invariant (observed, Contract).
- Clean-room is intact today: zero corpus-vocabulary hits across every installed surface (observed, Clean-room).
- 12/14 core-skill anchors are load-bearing; A1 (brief) and E1 (research) lean decorative — kept as adopted; tightening is optional and was declined this pass (Minimality).
- The pack's non-core routing boundary was prose-only; R7 now pins it structurally (Registry).

## Disagreements / Residual Risks

- **GD↔AGS duplication is unmanaged debt, not a defect.** ~40% shared epistemic boilerplate (host preconditions, `artifact-complete` status, constitutional paths, self-report Nevers, overlapping refuters). The lifecycle object is genuinely distinct; R6 gives the divergence a trigger instead of forcing a merge now.
- **Description-level collision risk is unmeasured** (deliberately): a host could auto-invoke the pack on bare "autonomous"/"deliver"; GD-19's ≥3-holdout-group rule still gates any fixture work.
- **Anchor tests pin verbatim prose** — defensible drift detection (the sentence is the adopted feature), acknowledged as prose-pinning, not behavior assertion (Clean-room).
- **"Unlicensed corpus" is author-assumed** (no license inspectable on pasted text); the clean-room stance is the correct conservative default regardless (Clean-room).

## M5 Managed-Skill Re-Audit (event: this panel)

Per `dormant-work-specs-2026-07-11.md` M5 — a governance panel fires the managed-skill re-audit. Audited the four TeaPrompt-referencing managed skills against governed surfaces:

| Skill | Disposition |
| --- | --- |
| `teaprompt-project-primer` | **actively-wrong → corrected host-side**: claimed two domain packs; `DOMAIN_PACK_SKILLS` has four since 2026-09-03. All other claims verified (authority chain, layer map, read-first surfaces, promotion rules). |
| `teaprompt-artifact-promotion` | no drift — registry path, §4 memory-write gate, destination classifier all current. |
| `parallel-lens-review-packet` | no drift — repo-owned contract pointer (`workflow-recipes.md` §Packet and verdict contract) and all cited test files exist. |
| `redacted-external-review-panel` | no drift — TeaPrompt scope banner and M7 deferral citation still accurate. |

Zero repo-should-adopt items; no repo surface was edited from managed-skill content.

## Evidence Actually Checked

- **Observed:** five complete lens reviews (hub-delivered); git `1e4f960` numstat (41 ins / 0 del / 8 files); guard suite 16 tests green post-change; `make all` green (see Completion Ledger); index consumers (`prompt_composer`, `eval_harness`, `site/index.html` field usage) verified against the regenerated `index.json`.
- **Author-claimed:** the original adoption's composite self-acceptance narrative; recurrence remains `unknown` (no observation channel exists — now stated in the trigger).
- **[INFERENCE]:** the two contract fixes (R1–R3) remove real incoherence; no host has run the contract set, so behavioral benefit is unproven.
- **Not done:** GDR-1–GDR-6 refuters (all `unknown`); GD-19 collision measurement (deferred); A1/E1 anchor tightening (declined, optional).

## Falsifiability

This record is wrong if: any R1–R9 change is absent from its named surface while the guard passes; the pack appears in a ROUTE fixture; a corpus token lands on any installed surface; or the M5 dispositions misreport a managed skill's content.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Five-lens independent review | done | GDEvidenceAuditor, GDContractCorrectness, GDRegistryRouting, GDMinimalityOverlap, GDCleanRoom — all AGREE WITH CHANGES |
| Required changes R1–R9 | done | named surfaces above; guard 16/16 |
| M5 re-audit | done | four skills audited; one correction applied host-side |
| Index repair + consumer coverage | done | `index.json` regenerated (148 files); composer/harness/site verified |
| Plan snapshot refresh | done | `QUALITY_GATES_SUMMARY.md` counts re-dated 2026-09-13 |
| Full repository gate | verified | `make all` from repository root |
