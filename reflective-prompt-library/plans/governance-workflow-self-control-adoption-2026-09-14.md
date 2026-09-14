# Governance, Workflow, and Self-Control — User-Directed Adoption Pass — 2026-09-14

> **Status: decided (non-authoritative); user-directed adoption record.** User instruction: *"Implement governance and workflow and self-control parts as possible if worth it."* Scope: the governance / workflow / self-control items left open by the [September review](september-skills-review-2026-09-14.md), the [GD-18 review](governed-delivery-review-2026-09-13.md), and the agentflow records. Bar applied per item: the installed surface must be better; name the failure defended, the smaller alternative rejected, and the gap; one surface; ≤2 sentences of prose; ledger row + guard. Date-gated items and named-trigger reserves were not preempted — a generic "if worth it" does not fire a named gate. Authority chain unchanged: `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts govern.

## Direct Answer

Seven items were worth it and landed; seven were evaluated and held, each with its reason. The largest is workflow-routing governance: the deferred GD-19 collision measurement ran, found one real derailment, and the router was tuned under holdout-before-tune with all three evals at 100%. The rest are self-control mechanisms for the repository and its agents: a guard that fails when the discovery index is stale, a "search before you add" rule on the skill that owns minimality, a status-family map for cross-phase handoffs, and evidence surfaces the 2026-10-11 checkpoint needs.

## Candidate Adoption Ledger

| # | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| GW-1 | GD-19 collision measurement for "deliver / autonomous / unattended" and the resulting R11 tune | **Adopted 2026-09-14** | Nine fresh ROUTE-002 phrases (3 groups: plan / route / risk) passed 100% pre-tune; ROUTE-003 trap `delivery_vocab_implement_not_plan_trap` held 33.3% pre-tune — "implement the approved delivery plan …" derailed to spec-plan via the planning signal `delivery plan`; narrowest fix: marker `approved delivery plan` + verification context inside the existing R11 conjunct; post-tune ROUTE-001/002/003 = 100% (16 / 47 / 23 groups); floors 47/133 and 23/79; R11 contract bullet; guard `test_gd19_*` | GD-19 row closed in the GD adoption ledger; no quick-cue added (R12: not yet frequent) |
| GW-2 | Index-currency guard: committed `index.json` must equal an in-memory generator run | **Adopted 2026-09-14** | `test_index_json_current.py`; failed on the live tree pre-regeneration for the exact files edited (observed), passes after `generate_index.py`; never writes | Failure defended: index went stale twice in one session (2026-09-13/14); smaller alternative rejected: running the generator inside `make validate` writes a committed artifact during validation |
| GW-3 | Ledger Status Families map in GLOSSARY | **Adopted 2026-09-14** | One table translating `open` / `unverified` / `pending` / `asserted` and siblings across the four ledgers; operational test names the family at handoff | Smaller alternative to vocabulary unification (C18), which stays trigger-gated |
| GW-4 | Search-before-add rule on `reflective-minimality` (prompt-text bullet) | **Adopted 2026-09-14** | One sentence appended to the OG-1 bullet: search the surface for a sentence already carrying the clause and extend it; guard: OG-1 pin unchanged (count 1) + this record's guard | Failure defended: three same-day twins on 2026-09-03 (September review C1–C3); smaller alternative rejected: the roadmap's Horizon 1 duty is invisible to an installed agent |
| GW-5 | `reflective-implement` Workflow step 4 compacted from six bullets to one self-contained sentence | **Adopted 2026-09-14** | Same clauses, one sentence; steps renumbered 4–8; no cross-reference needed, so the C16 policy question (cross-reference vs self-contained) dissolves | — |
| GW-6 | Pack examples for the four uncovered templates (writer-critic with floor, multi-wave; orchestrator-workers, DAG) | **Adopted 2026-09-14** | `flow-loop-harness.examples.md` Examples 3–4; `flow-control-generator.examples.md` Examples 4–5; each names the template's real caps, exits, gates, and rig-tier verification; `validate_skill_examples.py` green; examples live outside the 20k SKILL.md budget | C19 closed |
| GW-7 | Usage log widened to all four packs; 2026-09-05 template-maintenance note backfilled | **Adopted 2026-09-14** | `flow-pack-usage-log.md`: zero-state rows for `agent-governance-scaffold` and `governed-delivery`, `unknown`-not-zero wording, checkpoint pointer; `test_usage_log_evidence_contract` green | The 2026-10-11 GD checkpoint (runbook check 8 / Agenda 7) reads this row |
| GW-8 | Intra-skill near-duplicate guard (token-set Jaccard over sentences) | **Rejected on evidence 2026-09-14** | Prototype at threshold 0.6 over ≥10 content tokens, run on `4d90c68` (pre-merge) and HEAD: missed all three 2026-09-03 twins (semantic duplicates with different tokens) and flagged three by-design restatements (frontmatter description ≈ Trigger; GD template ≈ Methods; GDR-6 ≈ footer) | Re-open only with a detector that catches the three known twins without flagging the three known restatements |
| GW-9 | Flow-pack lint tier (25k pack tier vs template factoring) | **Held — date-gated** | Both packs ≤ 20k with < 1k headroom; Horizon 1 zero-sum rule in force | 2026-10-11 runbook Agenda 6/7 |
| GW-10 | A1 anchor tightening (`reflective-brief`) | **Held — date-gated** | E1 already merged (September review C3); A1 keeps its owner/unknown-unknowns clause until the checkpoint weighs it | 2026-10-11 runbook Agenda 7 |
| GW-11 | Ledger status vocabulary unification | **Held — trigger unfired** | GW-3 map adopted instead; each set is pinned by its skill's guard | A documented cross-skill handoff confusion |
| GW-12 | I-1 / A-5, TK-1, E-5 reserved sentences | **Held — named gates** | Each record names its own local-case trigger; I-1 carries an absence guard; AF82-8 affirms only the original triggers reopen them | Their own triggers |
| GW-13 | GD-16 refuters host run; GA-13 fault-injection suite | **Held — host-only** | No named host harness; TeaPrompt CI runs no providers | A named host harness |
| GW-14 | agentflow record-only / held rows (AF-1, AF-5, AF-8, AF-13; CX-7–CX-20; TK-2–TK-6; AF82-3/5/10/11) | **Held — panel-decided** | Each row already carries a 7/7 or coordinator disposition with reasons and a reopen trigger; no new local evidence arrived | Their recorded triggers |

## Evidence Actually Checked

- **Observed:** live router probes before and after the tune (15 phrases; 3 misses pre-tune, of which 2 were the same R11 gap and 1 a keyword-less phrase dropped from the fixture); three eval runs post-tune at 100%; `test_index_json_current.py` failing pre-regeneration with the exact edited files named; the near-duplicate prototype's output on both trees; `validate_skill_examples.py`; the full suite (1169 passed with only the two expected pre-record failures).
- **Author-claimed:** none load-bearing.
- **[INFERENCE]:** the R11 verification-context extension generalizes beyond the three trap phrases; guarded by the six GD-19 probes and the full ROUTE-002 holdout, not proven for unseen phrasing.
- **Not done:** the date-gated and host-only items above; no quick-cue bullet (R12 frequency bar not met).

## Falsifiability

This record is wrong if: a GD-19 probe or fixture group is removed while the guard passes; `index.json` goes stale without `test_index_json_current.py` failing; the search-before-add sentence or the status-family table disappears; a held item above is adopted without its named trigger firing; or a future near-duplicate detector is claimed to work without passing the GW-8 discriminating test.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| GW-1 fixtures, tune, contract, floors, probes | done | ROUTE-001/002/003 100%; `test_validate_route_fixture.py`; `test_quality_gates_summary.py` |
| GW-2 guard | done | fails stale / passes current (observed both) |
| GW-3–GW-7 surfaces | done | named files |
| GD-19 ledger row and roadmap rows updated | done | GD adoption ledger; roadmap Horizon 3 |
| Decision Index, index.json | done | `PROJECT_KNOWLEDGE.md`; regenerated |
| Full repository gate | verified | `make all` from repository root |
