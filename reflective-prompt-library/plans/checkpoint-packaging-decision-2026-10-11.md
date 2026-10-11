# Checkpoint Packaging Decision — 2026-10-11

> **Status: adopted packaging refactors, installed-copy smoke verified; final repository receipts are in the [checkpoint outcome](checkpoint-2026-10-11-outcome.md).** Non-authoritative decision record. No new capability, pack, core route, runtime, provider call or campaign authorization.

## Goal and authority

Resolve the due AS8/R10/WGS-GOV-1 governance-pack size review and the flow-pack lint-tier decision. The maintainer explicitly selected **Adopt co-installed artifact reference** for `agent-governance-scaffold` and **Factor co-installed templates** for both flow packs in this checkpoint conversation. The [runbook](checkpoint-2026-10-11-runbook.md) supplies the review duty, not that approval.

The common whole-`SKILL.md` warning stays at 20,000 characters. Nine core skills and ten registered domain packs remain unchanged. Template factoring is disclosure of existing bodies, not evidence of host enforcement or smaller total installed packages.

## Evidence Actually Checked

Source-bound baselines were saved before mutation. The installed-copy smoke extracted the published copy helper from the installation guide, copied all ten packs into a disposable destination, parsed the copied governance objects, syntax-checked the copied shell/Python bodies, and exercised pipeline, fan-out, DAG and loop paths there.

| Package | Baseline main characters | Current main characters | Fenced bodies preserved |
| --- | --- | --- | --- |
| `flow-control-generator` | 44,932 | 14,988 | 5 |
| `flow-loop-harness` | 28,518 | 11,128 | 6 |
| `agent-governance-scaffold` | 27,769 | 18,429 | 16 |

All 27 fenced bodies match the baseline language/body sequences byte-for-byte and in order. Bash/Python/YAML/JSON checks succeeded; nine copied-package runtime cases returned their expected exits. The disposable installation was removed. These are synthetic control-flow and package-consumption checks, not model or actual-host proofs.

Full source hashes, case names/exits and disposal evidence: `local://checkpoint-package-smoke-results-2026-10-11.json`. Baseline bindings: `local://flow-slice-baselines-2026-10-11.md` and `local://ags-skill-baseline-2026-10-11.md`.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence and counterargument | Next action / falsifier |
| --- | --- | --- | --- | --- |
| PKG-1 | Governance object bodies in a co-installed `ARTIFACTS.md` | Adopted, user-directed 2026-10-11 | The WGS-GOV-1 design removes branch-only bodies from the main contract while retaining the artifact menu, Four-Power Split, Gate 2.0, safety/review boundaries and demotion rules. Counterargument: a missing sibling breaks emission; the whole-directory installer and installed-copy smoke cover that boundary. | Reopen on missing reference, changed emitted semantics or main contract exceeding 20,000 characters. |
| PKG-2 | Flow executable bodies in co-installed `TEMPLATES.md` references | Adopted, user-directed 2026-10-11 | Both main contracts were over the common warning; preserving the executable bodies and migrating extraction consumers avoids a second implementation convention. Counterargument: host agents must follow the context pointer; actual-host discovery remains unmeasured. | Reopen on copied-install extraction failure, stale consumer or changed runtime behavior. |
| PKG-3 | Raise the flow-pack lint threshold or invent a pack-specific tier | Rejected for this decision | Factoring satisfies the existing main-contract limit without hiding growth behind a larger threshold. References are discoverable documents, not routing inputs; ordinary document warnings remain visible. | A measured routing/reference-consumption problem would justify a new scoped review, not an automatic threshold increase. |
| PKG-4 | Demote `agent-governance-scaffold` | Branch not taken | Recorded host generation is present and the explicitly adopted shrink is implemented. Its owning zero-use/oversized-without-shrink condition is not met. Generation does not establish enforcement. | The original [demotion triggers](agent-governance-scaffold-adoption-2026-07-17.md#demotion-triggers) remain live. |
| PKG-5 | Shared-reference consolidation of GD/AGS boilerplate | Reviewed, held; no cutover adopted | Shared constitutional-path, `artifact-complete` and host-precondition meanings remain coherent. Independent GD use is not established by generation rows or a GD-only skill load; absence is unknown, not proof of never-independent use. The delivery lifecycle and four-power split remain distinct. | Reopen the implementation decision on documented coupled-only use or a shared-contract divergence, under [R6](governed-delivery-review-2026-09-13.md). |

## Implementation and consumer map

- Main contracts retain the rule/menu/selection surface and point to `<skills-root>/<pack>/ARTIFACTS.md` or `TEMPLATES.md`. No TeaPrompt checkout is needed to consume copied references.
- AGS `context_load` remains `medium`: R20's interim `high` premise ended when R10's size target was met. The obsolete interim wording assertion was removed rather than re-pinned.
- Both installation guides say to install the complete skill directory. Existing copy/symlink helpers already use whole directories; no new helper or fallback was added.
- All moved-source executable/object/heading consumers read the sibling directly. No inline-source fallback, alias, duplicated body or shim remains.
- Package-wide clean-room and rejected-candidate scans use `prompt_eval_helpers.skill_package_docs()`: 19 main skills plus three references. Registry/frontmatter cardinality checks still enumerate `SKILL.md`, not every Markdown document.
- `generate_index.py` discovers sibling Markdown files inside existing skill directories. The actual composer/discovery gate remains part of `make all`.
- Incidental exact-English wording assertions were removed. Existing behavioral exit, quorum, schema, default, reference-binding and state-transition checks were preserved; no copy/wiring assertions were added as permanent tests.

Covered consumer classes: main contracts and context menus; direct template/object extraction; dormant heading scans; installed-package token scans; copy installation and bilingual guidance; discovery generation. Actual commercial-host reference loading and enforcement are explicitly untested boundaries.

## Verification and limits

The standalone smoke exercised accepted pipeline execution, selected-preflight refusal before dispatch, zero-survivor fan-out reaching a rejecting merged gate, successful deterministic repair, no-progress stop, non-git cap exhaustion, missing-verifier refusal, and accepted/rejected DAG merges. It did not dispatch a model, execute the external book scripts, or run the held GDR/campaign suite.

Final gate counts and rendered-document checks belong to the checkpoint outcome and `review/final-report.md`, so this record does not preserve an in-flight test count as closure evidence.

## Falsifiability

This decision is wrong if the copied package needs repository-only paths to emit its bodies, if a consumer still reads the retired inline location, if a moved body differs from its source-bound baseline without a separately approved behavior change, if safety/review/demotion semantics were removed to meet the warning, or if the main contracts exceed the unchanged limit.

Unknown host use and model efficacy remain unknown. TEST-001 host qualification, Stage-1/TEST-002–004 campaign authority and the original H12 seven-guard branch remain separately held. No commit or push is authorized by this decision.

Later same-day [maintainer acceptance of the H12 replacement scope](skills-september-concepts-review-2026-09-16.md#h12-replacement-scope-decision-2026-10-11)
supersedes that historical seven-guard hold, without claiming its original
inventory was verified. The paragraph above records the packaging decision's
own limits; actual-host qualification and campaign authority remain held.
