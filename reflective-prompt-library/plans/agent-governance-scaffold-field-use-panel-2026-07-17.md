# Agent-Governance-Scaffold Field-Use Panel Record — 2026-07-17

> **Status: decided (non-authoritative); field-use panel record.** Six-lens Parallel
> Lens Review of the `agent-governance-scaffold` domain pack after its **first
> observed host emit** (`lite-ad/.agent/`). This is not a re-admission of Option B.
> Authority chain unchanged: `06-repo/AGENTS.md` and the invoked `SKILL.md`
> contracts govern; this record is evidence, not an operating rule. If it and a
> governed surface disagree, the governed surface wins.
>
> **Authority caveat:** TeaPrompt `main` still has the 2026-07-18 panel remediations
> (R1–R17) and that panel record as **uncommitted/index changes** atop `cc0c781`.
> This field-use review treats the working-tree skill SHA
> `1c744fd47c8f2fb4c9718e3fabd3319922b405fff7713e1bb8ded074de3a828a` as the
> operative contract, and treats R1–R16 as **panel-decided, unlanded** until
> committed.

## Purpose

User instruction: *"Review agent-governance-scaffold skill"* under the Parallel
Lens Review packet-and-verdict contract
(`04-agent/workflow-recipes.md` §Parallel Lens Review), after a completed
`agent-governance-scaffold` emit into `lite-ad`. Prior admission panel
(2026-07-18) left residual: *"usage evidence: none"*; R17 deferred until first
concrete host integration or any `*.schema.json`.

## Panel Packet

Shared packet (temporary, deleted after synthesis):
`/Users/teee/dev/lite-ad/review-packet-agent-governance-scaffold-field-use-2026-07-17.md`.

Key observed evidence:

- Skill 24,994 chars / 25,131 bytes; `context_load: medium`; `human_review_required: true`.
- `pytest plans/tests/test_agent_governance_scaffold_adoption_state.py -q` → **49 passed**.
- lite-ad emit: 9 files under `.agent/` including Draft 2020-12
  `governance-objects.schema.json`.
- Emit mismatches: five-column invariant map absent; literal
  `artifact-complete` / `enforcement-proven` absent; formal schema present without
  R17 ledger update.
- Re-executed this session: YAML/JSON parse PASS; `bash -n` PASS; fake-backend
  smoke PASS (exit 64 on noargs / `danger-full-access` / bad effort; modes fence
  `--cd` + stdin); **real Codex invocations: 0**.

## Panel Lenses

Six same-host roles (not named provider personas). Scout fan-out failed 6/6 with
provider quota 429; identical batch re-fanned on default task workers with
STRICTLY READ-ONLY constraint (protocol backend-quota fallback). Five lenses
initially returned JSON summaries; full Markdown deliverables were recovered over
IRC before synthesis (Usability, EvidenceTier, Minimality, AdoptionGov,
ContractCorrect, TrustBoundary).

- Evidence-tier / honesty auditor
- Contract-correctness reviewer
- Runtime trust-boundary / security / R17 reviewer
- Minimality / information-architecture challenger
- Implementer usability / actionability reviewer
- Adoption / demotion / ledger governance reviewer

## Panel Consensus

### Decision

**`AGREE WITH CHANGES` (6/6; no `AGREE`, no `DISAGREE`)**

The pack survives first field use as a domain-pack **generator**. Option B
admission is **not falsified**. The lite-ad emit is substantively strong
(four-power map, fail-closed pending/deny templates, host-honest NO-GO prose,
lease-keyed budgets, constitutional paths, wrapper three-no + prompt-defense,
parse/smoke clean) but **contract-nonconformant** on load-bearing Verification
gates the skill itself elevated after R12–R14: five-column invariant map,
literal status labels, R17 ceremony for formal schema, named unwired bypass for
`run-codex.sh → codex exec`, and task-minimal / Tier-2 traceability.

### Use-case recommendation

| Use case | Recommendation |
| --- | --- |
| `study` | Concepts record remains the reference surface. |
| `reproduce` | Reproduce by parse + structural checklist; cite lite-ad as first emit with known gaps (FU2–FU6). Do not trust narrated enforcement. |
| `adopt` | **Primary.** Keep as third domain pack; apply FU1–FU7 / FU9–FU11 / FU13–FU15; land uncommitted R1–R17 before citing them as closed. |
| `deploy` | **Never unattended.** `human_review_required: true`; no `enforcement-proven` until R17 runtime rig (FU5 remainder). |

## Required Wording Changes

Highest-priority skill/example/ledger changes converging across ≥4 lenses:

1. **Example 3 — worked field emit** with canonical `.agent/` tree, five-column
   `INVARIANTS.md` excerpt, and HANDOVER status line (Usability U1; Minimality M6).
   First emit may be Codex-shaped, but Example 3 must keep `run-<cli>.sh` /
   `<cli>-bounded-worker` parameterization and must **not** harden Codex as the
   only host (FU15: agy, agent(cursor-cli), Devin, OpenCode, OMP, Claude, …).
2. **HANDOVER status gate:** require literal `**Governance status:** artifact-complete`
   (or `enforcement-proven` with evidence); prose paraphrase does not satisfy
   Verification §6.
3. **INVARIANTS.md shape:** mandate
   `emitted_object | invariant(s) | host_enforcer | evidence_now | unwired_obligation`;
   inverted invariant→objects tables fail the gate.
4. **Formal schema default:** first scaffold = typed templates only; no
   `*.schema.json` unless user requests or R17 row is opened; on emit, record
   dialect + `r17_status: partial` and update ledger.
5. **Named unwired bypass:** every handover must name
   `direct_<cli>_exec_via_hook` when a run hook is emitted; consider fail-closed
   stub that refuses direct CLI exec until broker is named.
6. **Usage / demotion annotation:** first solo invocation = lite-ad 2026-07-17;
   does not clear 2026-10-11 checkpoint.
7. **R17 row:** `Deferred` → `Fired-partial 2026-07-17 (lite-ad)`; runtime
   bypass/receipt/budget/mutation rig remains open.
8. **Output / Artifact Set clarity:** Tier-1 default set vs Tier-2 concepts
   pointers; conditional-artifact trigger table in handover.
9. **Identical-gate fallback** must appear in emitted worker contracts (TrustBoundary R17-S6 / FU13).
10. **Constitutional `deny_write`** must include `.agent/hooks/**` and `.agent/evidence-schema/**` (R17-S7 / FU14).

Exact lens wording diffs live in the synthesis session artifacts
(`agent://*Lens-2` transcripts); landing commit should quote FU rows below.

## Shared Findings

1. **First invocation falsifies "usage evidence: none"** without proving
   recurrence, minimality, or enforcement.
2. **R17 partially fired** via concrete host + Draft 2020-12 schema; leaving
   the ledger "Deferred" is itself an honesty failure.
3. **Static guards ≠ emit conformance:** 49 adoption-state tests pass while the
   field emit misses skill Verification gates — category error between author-time
   substring guards and operator-time scaffold shape.
4. **Both skill and operator defects:** skill/examples under-operationalize
   emit gates (~60–70%); operator invented formal schema and transpose invariant
   table (~30–40%).
5. **Executable `run-codex.sh` is a residual deputy path** even when HANDOVER
   says NO-GO Codex — Verification §5 requires it named (and TrustBoundary argues
   for a fail-closed stub). The same deputy-path class applies to any
   `run-<cli>.sh` for other hosts (FU15).
6. **Substance is good:** trust boundary, four-power map, pending activation,
   lease budgets, mutation/canary marked not-run, smoke tests without Codex.
7. **CLI matrix is wider than the first emit:** skill contract is already
   `<cli>`-generic (0 Codex mentions in skill/examples), but lite-ad hardened a
   Codex-only worker/hook. Host agents in scope include agy, agent(cursor-cli),
   Devin, OpenCode, OMP, and Claude — Example 3 / future emits must not treat
   Codex as the sole backend.

## Disagreements / Residual Risks

- **R10 timing (preserved dissent):** Minimality wants field-accelerated R10
  (Tier-1/Tier-2 shrink; interim `context_load: high`). AdoptionGov and the
  synthesis majority keep R10 **deferred to 2026-10-11**, with annotation that
  the zero-use leg is falsified and the checkpoint now reviews **minimality
  compliance + recurrence**, not mere existence. **Ruled:** annotate now;
  adopt interim `context_load: high` as FU8 **partial**; do not force full R10
  shrink in this decision without a separate remediation pass.
- **R17 "full" vs "partial" fire:** ContractCorrect initially said "full fire"
  then ledgered "Adopted (partial)". TrustBoundary / EvidenceTier / AdoptionGov /
  Usability / Minimality: **partial fire**. **Ruled: partial fire** — schema
  track advanced; runtime rig open.
- **Fail-closed run stub vs annotated NO-GO:** TrustBoundary wants the hook to
  refuse direct CLI exec until broker exists; other lenses accept named bypass +
  NO-GO prose. **Ruled: FU11 adopt naming + skill guidance; stub behavior is
  recommended default for next skill revision, not a lite-ad rewrite mandate in
  this record.**
- **Unlanded remediations:** citing R1–R16 as closed while uncommitted is an
  authority hazard (AdoptionGov A6).
- **Composite-self-acceptance echo:** first field emit was again a single
  authoring session producing both scaffold and self-validation; this panel is
  the independent acceptance layer for that emit.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| FU1 | Example 3: lite-ad-shaped worked field emit + canonical `.agent/` tree | **Adopt** | Usability F1/D1; Minimality M6; 6/6 agreed examples insufficient | Land in `skills/examples/agent-governance-scaffold.examples.md`; extend example guard |
| FU2 | HANDOVER literal status gate (`artifact-complete` / `enforcement-proven`) | **Adopt** | All lenses; lite-ad HANDOVER lacks literals | Skill Verification §6 + Output; Example 1/3 |
| FU3 | Five-column `INVARIANTS.md` (no transpose table) | **Adopt** | All lenses; lite-ad shape mismatch | Skill checklist; Example 3; optional emit-shape guard |
| FU4 | First-scaffold default: no `*.schema.json` unless R17/user request | **Adopt** | Schema emitted; examples/guards forbid `.schema.json` in skill surfaces | Skill Methods/Never/Verification; Example 1 |
| FU5 | R17 → `Fired-partial 2026-07-17 (lite-ad)`; runtime rig open | **Partial** | `governance-objects.schema.json` Draft 2020-12; 0 live broker tests | Update 2026-07-18 panel R17 row + adoption record; complete on bypass/receipt/budget/mutation rig |
| FU6 | Named unwired bypass mandatory when run hook emitted | **Adopt** | `run-codex.sh` → `codex exec`; Verification §5 | Skill + lite-ad HANDOVER annotation |
| FU7 | Annotate demotion trigger + usage evidence (first emit); keep 2026-10-11 | **Adopt** | Packet §B.5; AdoptionGov A1/A9 | Adoption-record demotion bullet rewrite; panel residual update |
| FU8 | Interim `context_load: high` until R10 shrink | **Partial** | 24,994 chars; Minimality dissent vs AdoptionGov R10 hold | Relabel now **or** land R10 before next checkpoint; full Tier-1 shrink remains 2026-10-11-bound unless separately authorized |
| FU9 | Land uncommitted R1–R17 + 2026-07-18 panel record before citing as closed | **Adopt** | `git status` shows modified/added panel surfaces | Commit remediations; then amend R17 per FU5 |
| FU10 | Conditional-artifact trigger table in handover | **Adopt** | ContractCorrect C5; Verification §4 | Skill Verification + Example 3 |
| FU11 | Fail-closed run-interface stub when broker unwired (recommended skill default) | **Partial** | TrustBoundary F1/Socratic #2 | Skill Methods/run-interface wording; regenerate future emits; lite-ad may annotate rather than rewrite in this pass |
| FU12 | Operator repair list for lite-ad emit (labels, invariant map, ultra_vires, receipt fields) | **Adopt (host-side)** | ContractCorrect §8; TrustBoundary §9.8–9.10 | Host/owner edits under `lite-ad/.agent/`; not TeaPrompt pack demotion |
| G9 | Routing holdouts | **Deferred (unchanged)** | No TeaPrompt-local misroute from this emit | 2026-10-11 proceed/hold/close |
| R10 | Minimality Phase B shrink ~16–18k | **Deferred (annotated)** | Minimality wants accelerate; majority keeps checkpoint | Re-litigate 2026-10-11 with FU7/FU8 |

### TrustBoundary R17-S crosswalk (IRC full deliverable)

| TrustBoundary ID | Maps to | Status in this record |
| --- | --- | --- |
| R17 / R17-S1 | FU5 | **Partial** — Fired-partial 2026-07-17; ledger annotate on land |
| R17-S2 | FU11 (+ FU6) | **Partial** — skill default: no direct CLI exec without broker; name bypass |
| R17-S3 | FU2 + FU6 | **Adopt** — `artifact-complete`, `r17_status`, named bypass in handover header |
| R17-S4 | FU3 | **Adopt** — five-column invariant map |
| R17-S5 | FU5 remainder | **Deferred** until broker/runtime rig |
| R17-S6 | FU13 | **Adopt** — emitted worker contract must retain “identical broker/policy gates” |
| R17-S7 | FU14 | **Adopt** — skill `deny_write` must include `.agent/hooks/**` and `.agent/evidence-schema/**` |
| F1-note | FU7 | **Adopt** — annotate first field emit; keep 2026-10-11 checkpoint |

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| FU13 | Identical-gate fallback parity in emitted worker contract | **Adopt** | TrustBoundary §6 / §9.7; skill L150/L169 vs lite-ad worker L30 | Skill run-interface + worker template; lite-ad `codex-bounded-worker.md` wording under FU12 |
| FU14 | Align skill constitutional `deny_write` with emit (hooks + evidence-schema) | **Adopt** | TrustBoundary §5.4 / §9.5; skill list omits paths lite-ad correctly excludes | Patch skill constitutional block; Example 3 |
| FU15 | Multi-backend host matrix; keep skill `<cli>`-generic | **Adopt** | User note + reaffirm 2026-07-17: hosts include agy, agent(cursor-cli), Devin, OpenCode, OMP, Claude; skill/examples have 0 Codex mentions while lite-ad emit is Codex-only | When landing FU1 Example 3, keep `run-<cli>.sh` / `<cli>-bounded-worker`; name non-Codex hosts as in-scope; do not harden Codex as sole backend. Per-CLI stubs remain optional host-side (not this row). |

### Falsifiability

This record is wrong if: any FU row marked Adopt/Partial is absent from its named
surface after the landing commit while adoption guards still pass; FU5 remains
"Deferred" after `*.schema.json` stays in lite-ad without ledger update; FU7 is
removed and the demotion trigger again claims zero invocations;
`enforcement-proven` is claimed before FU5's runtime rig; or FU15 is marked Adopt
while Example 3 / skill wording hardens Codex as the only host. Any of those means
the ledger mechanism failed.

## Evidence Actually Checked

- **Executed (this panel session):** adoption-state pytest 49 passed; skill fenced
  YAML/JSON parse; lite-ad YAML/JSON parse; Draft 2020-12 meta-schema check
  (ContractCorrect lens); `bash -n` + fake-backend smoke on `run-codex.sh`
  (host + authoring session); SHA compare installed vs source skill (identical).
- **Read:** packet; skill; examples; adoption + concepts + 2026-07-18 panel;
  lite-ad `.agent/**` (HANDOVER, INVARIANTS, governance.yaml, schemas, hook,
  authorization, verification-plan, worker contract).
- **Not run:** `make all`, Wrangler, live Codex, broker/policy/verifier,
  mutation/canary runners, routing holdout measurement.
- **Honesty note:** lenses are same-host roles; scout backend was quota-exhausted;
  full deliverables recovered over IRC where previews were JSON-only.

## Next Action
Human Review before landing FU wording into the skill/examples/ledgers, and before
any lite-ad live wiring. Recommended order: **FU9 land** → **FU5/FU7 ledger
annotate** → **FU1–FU4/FU6/FU10/FU13–FU15 skill+examples** → **FU12 lite-ad emit repair** →
optional **FU8/FU11**.
