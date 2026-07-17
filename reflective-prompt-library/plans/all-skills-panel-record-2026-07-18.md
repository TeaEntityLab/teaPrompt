# All-Skill Layer Panel Record — 2026-07-18

> **Status: decided (non-authoritative); panel record.** Seven-lens Parallel Lens
> Review of all 12 TeaPrompt repo skill contracts under
> `reflective-prompt-library/skills/*/SKILL.md`. Authority chain unchanged:
> `06-repo/AGENTS.md` and invoked `SKILL.md` contracts govern; this record is
> evidence, not an operating rule. If it and a governed surface disagree, the
> governed surface wins.

## Purpose

User instruction: *"Review all skill"* under the Parallel Lens Review
packet-and-verdict contract (`04-agent/workflow-recipes.md` §Parallel Lens
Review). Scope: the nine frozen core workflow skills plus three registered
host-invoked domain packs in the current working tree on `main` at `cc0c781`
with uncommitted governance-pack remediation changes.

## Panel Packet

A temporary shared packet was written to the repo root as
`review-packet-all-skills-2026-07-18.md` and deleted after synthesis. It separated
observed, author-claimed, and `[INFERENCE]` evidence.

Observed packet evidence:

- Branch `main`, HEAD `cc0c781`, dirty/staged tree.
- Skill inventory: 12 `SKILL.md` files; 9 core workflow skills and 3 registered
  domain packs.
- `validate_governance.py`: 12 valid skills, 0 invalid.
- `validate_skill_examples.py`: all 9 core + 3 domain-pack skills had examples.
- `lint_skills.py`: 157 files, 0 errors, 1 warning before packet write — known
  `agent-governance-scaffold` length warning.
- `make all` was not rerun for the packet before fan-out; any full-gate result is
  post-adoption evidence only.

## Panel Lenses

Scout fan-out failed 7/7 with provider quota 429; the identical batch ran on
strictly read-only default workers under the protocol fallback. Same-host review
roles only; no claim of provider/persona independence.

Lenses:

- Metadata / registry / classification
- Routing boundary
- Evidence-tier honesty
- Minimality / context budget
- Safety / trust boundary
- Install / examples / portability
- Adoption readiness

## Panel Consensus

**Decision:** `AGREE WITH CHANGES` (7/7; no `AGREE`, no `DISAGREE`).

The all-skill layer is structurally sound: metadata validates, examples exist,
the nine-core / three-domain-pack split is enforced, and domain packs remain
outside `reflective-dispatch` route rows. Required changes were portability and
evidence-tier repairs, not a routing or skill-count reversal.

**Use-case recommendation:**

| Use case | Recommendation |
| --- | --- |
| `study` | Yes. The skill layer is coherent source material; panel records carry the caveats. |
| `reproduce` | Reproduce structural checks: lint/governance/examples/tests. Do not treat examples as e2e proof. |
| `adopt` | Adopt after AS1–AS7 are landed and guarded; domain packs remain explicit opt-in. |
| `deploy` | Not directly. Generated scripts/scaffolds require host review, approval, and runtime wiring before unattended use. |

## Required Wording Changes

1. Co-installable examples: every shipped `SKILL.md` now points to
   `<skills-root>/examples/<skill>.examples.md`; installation helpers can copy or
   symlink `skills/examples/`.
2. Portable dispatch cues: `reflective-dispatch` now inlines the boundary quick
   cues instead of relying only on repo-local cheatsheet/ROUTING_CONTRACT paths.
3. Flow-control safety parity: `flow-control-generator` now has a Human Review
   Boundary matching its side-effectful script risk, plus a deployment-pipeline
   example with an approval pause.
4. Evidence-tier labels: flow-pack examples label stub runs as rig-tier only;
   governance `conformance_suite` and `checker_profile` mark host-run and
   illustrative-placeholder status.
5. Metadata docs: `CONTRIBUTING.md` now shows governance metadata nested under
   `metadata:`; `QUALITY_GATES_SUMMARY.md` lists all 12 applied metadata rows.
6. Governance field-use closure: `agent-governance-scaffold` Example 3 documents
   the canonical field-emit shape, literal HANDOVER status, five-column invariant
   map, named unwired bypass, and generic host matrix.
7. R17 reconciliation: `agent-governance-scaffold` R17 is no longer plain
   deferred; it is **fired-partial** for the lite-ad schema track, with the live
   runtime rig still deferred.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| AS1 | Add installed example pointers to all 12 skills and install helpers for `skills/examples/` | Adopted 2026-07-18 | `SKILL.md` Examples sections; `SKILL_INSTALLATION.md`; `validate_skill_examples.py`; `test_port1_shipped_skills_point_to_installed_examples_tree` | none |
| AS2 | Inline dispatch boundary quick cues in `reflective-dispatch` | Adopted 2026-07-18 | `reflective-dispatch/SKILL.md`; `test_port1_dispatch_boundary_quick_cues_are_inline` | none |
| AS3 | Add flow-control Human Review Boundary and side-effectful approval example | Adopted 2026-07-18 | `flow-control-generator/SKILL.md`; examples; `test_port1_flow_control_human_review_boundary_present` | none |
| AS4 | Label rig-tier/evidence-tier caveats in flow examples and governance YAML blocks | Adopted 2026-07-18 | flow examples; `agent-governance-scaffold/SKILL.md`; `test_port1_flow_examples_label_rig_tier_only`; `test_conformance_and_checker_profile_are_evidence_tier_labeled` | none |
| AS5 | Repair contributor metadata template and all-12 metadata summary | Adopted 2026-07-18 | `CONTRIBUTING.md`; `QUALITY_GATES_SUMMARY.md`; `test_port1_contributing_uses_nested_metadata_template` | none |
| AS6 | Add governance field-use Example 3 and mandatory HANDOVER/invariant/bypass shape | Adopted 2026-07-18 | governance examples + skill Verification; `test_runtime_boundary_and_examples_name_unwired_bypass`; `test_templates_do_not_claim_formal_schema_or_unbrokered_fallback` | none |
| AS7 | Reconcile R17 status to fired-partial schema track with runtime rig deferred | Adopted 2026-07-18 | governance panel/adoption records; `test_panel_record_shape`; `test_r6_adoption_record_provenance_and_triggers` | Complete runtime rig on first concrete host integration |
| AS8 | Fire all-skill R10 shrink now for governance pack | Deferred to 2026-10-11 | Minimality lens; existing R10 ledger; lint warning remains accepted | Re-litigate at checkpoint; shrink or demote if still oversized/low-recurrence |
| AS9 | Add governance vocabulary holdout groups immediately | Deferred under G9 | RoutingBoundary lens probes showed no pack leakage; G9 ledger already defines trigger | Fire on documented misroute/discoverability failure or 2026-10-11 review |
| AS10 | Add index `skill_class` schema and broaden examples beyond floor | Deferred/no-change | Metadata lens marked optional; validators already enforce registry split | Reopen only with install-UI need or repeated example confusion |

## Shared Findings

1. Metadata is complete and mostly honest: 12/12 governance-valid; only
   `reflective-research` is `external_io: true`; high-review skills are
   `reflective-risk`, `flow-loop-harness`, and `agent-governance-scaffold`.
2. The nine-core routing boundary holds. Domain packs are discoverable but not
   selectable by core route rows.
3. Examples were structurally present but not installed or referenced by any
   `SKILL.md`; this made them host-facing in the repo but orphaned on installed
   hosts.
4. The only remaining lint warning is the known governance-pack size warning;
   R10 remains checkpoint-bound.
5. Runtime/e2e proof remains absent for generated scripts, loops, and governance
   scaffolds. Stub dry-runs and parse checks are rig-tier evidence only.

## Disagreements / Residual Risks

- Minimality argued that `agent-governance-scaffold` still looks like a concepts
  plan wearing a skill costume. Merge ruling: do not shrink in this all-skill
  pass; preserve R10 checkpoint pressure.
- RoutingBoundary found governance-pack vocabulary has low-confidence dispatch
  probes, but no pack leakage. Merge ruling: G9 remains deferred until a real
  misroute/discoverability failure or the dated checkpoint.
- AdoptionReadiness flagged dirty-tree commit-citation risk. This record does
  not claim a clean committed release; it records working-tree remediation.
- R17 is partial only. Formal schema appeared in first field use, but no broker,
  receipt, budget, mutation, or canary runtime rig has executed.

## Evidence Actually Checked

- Read-only packet and seven fallback lens deliverables.
- Host-run packet commands: `lint_skills.py`, `validate_governance.py`,
  `validate_skill_examples.py`, `cx overview`, and all-skill inventory.
- Lens-run targeted checks: metadata/example validators, route probes, targeted
  greps, skill/example reads.
- Post-adoption focused checks are recorded in the final report; full-gate proof
  must be the latest `make all` run after this record lands.

## Falsifiability

This decision is wrong if any adopted AS1–AS7 row is absent from its named
surface while the new guards pass; examples are again omitted from install
surfaces; domain packs enter `reflective-dispatch` route rows without a new P7/G9
decision; `agent-governance-scaffold` R17 is cited as fully complete before the
runtime rig exists; or R10 is deferred past 2026-10-11 without a shrink, demotion,
or new decision record.
