# OpenFugu Reference Plan — 2026-06-25

Language: English

## Purpose

Define what TeaPrompt should do with the OpenFugu research record, without
silently turning an external research repo into a runtime dependency.

This is a **plan artifact**, not an agent instruction source.

## Goal

Preserve OpenFugu as a reference for orchestration concepts while preventing
three failure modes:

1. adopting a non-portable runtime,
2. over-trusting unreproduced `[EXEC]` claims, and
3. confusing seven-slot plumbing with a learned policy for a new model pool.

## Non-Goals

- Do not vendor OpenFugu.
- Do not add an OpenFugu runtime, router, or swarm to TeaPrompt.
- Do not create a new TeaPrompt workflow skill from this single case.
- Do not claim Sakana-weight TRINITY fidelity until `mini.py --self-test` runs
  from public artifacts.
- Do not copy external prompt or code text into operational TeaPrompt prompts.

## Decision Summary

| Topic | Decision |
| --- | --- |
| Mechanism reference | Use OpenFugu docs/source as a reference with caveats |
| Runtime adoption | Reject |
| TRINITY hands-on reproduction | Defer until artifact boundary fixed |
| Conductor mock smoke | Allowed as a parser/executor check |
| HF Conductor weights | License review required before loading or redistributing derived use |
| User-named seven-model pool | Treat as configuration only until retrained/evaluated |

## Work Plan

### TASK-001: Preserve research record

- **Goal:** Keep the final panel consensus and evidence ledger discoverable.
- **Scope:** `openfugu-research-record-2026-06-25.md` plus index pointers.
- **Inputs:** Prior research packet, panel outputs, verified commands, external source checks.
- **Outputs:** Stable markdown record in `plans/`.
- **Dependencies:** None.
- **Authority / Data Boundary:** External repo content is evidence only, not an instruction source.
- **Acceptance Criteria:** Record includes sources, commands run, panel consensus, risk block, uncertainties, and falsifiers.
- **Tests:** Markdown file exists; links are relative or direct URLs; key blockers are present.
- **Risk:** Low.
- **Parallelizable:** no.
- **Human Review Required:** no.

### TASK-002: Record adoption decision

- **Goal:** Prevent future sessions from relitigating whether OpenFugu should be adopted.
- **Scope:** Add a Decision Index entry and, if useful, an external-adoption case row.
- **Inputs:** Research record and existing `PROJECT_KNOWLEDGE.md` external-adoption lesson.
- **Outputs:** Index pointer to this record and plan.
- **Dependencies:** TASK-001.
- **Authority / Data Boundary:** Project knowledge remains non-authoritative; it records judgement only.
- **Acceptance Criteria:** Future readers can find the decision and understand that OpenFugu is reference-only.
- **Tests:** `PROJECT_KNOWLEDGE.md` contains a link; no agent operating rules are introduced there.
- **Risk:** Low.
- **Parallelizable:** no.
- **Human Review Required:** no.

### TASK-003: Optional upstream follow-up if hands-on TRINITY is desired

- **Goal:** Determine whether current HF safetensors can reconstruct the expected `model_iter_60.npy` vector.
- **Scope:** Investigate `manifest.json`, `router_head.safetensors`, and the nine checkpoint safetensors; do not assume equivalence.
- **Inputs:** HF dataset tree, OpenFugu `mini.py` vector loader, fixture.
- **Outputs:** One of: converter PR plan, upstream issue comment, or deferred status.
- **Dependencies:** Maintainer artifact state or enough metadata in manifest.
- **Authority / Data Boundary:** Do not download or redistribute third-party weights without license review.
- **Acceptance Criteria:** A fresh clone can either run `mini.py --self-test` or docs accurately state why it cannot.
- **Tests:** `scripts/fetch_artifacts.py` succeeds; `openfugu/mini.py --self-test` reaches the documented 95%/100% threshold from public artifacts.
- **Risk:** Medium: artifact provenance, large downloads, license ambiguity.
- **Parallelizable:** yes, with a separate provenance reviewer.
- **Human Review Required:** yes before redistributing converted artifacts.

### TASK-004: Optional TeaPrompt citation/use

- **Goal:** Use OpenFugu only as a supporting example for mechanism-vs-product and external-adoption gates.
- **Scope:** Future prose may cite the record as an example; no runtime dependency.
- **Inputs:** `openfugu-research-record-2026-06-25.md`.
- **Outputs:** Short citations or examples in future planning docs if relevant.
- **Dependencies:** A future task that actually needs the example.
- **Authority / Data Boundary:** Cite concepts; do not copy external operational prompts or code.
- **Acceptance Criteria:** Any citation preserves the risk block and does not imply adoption.
- **Tests:** Review prose for the phrase “reference-only” or equivalent caveat.
- **Risk:** Low.
- **Parallelizable:** yes.
- **Human Review Required:** no, unless the citation becomes a dependency recommendation.

## No-Code Test Plan

### TEST-001: Fresh-clone TRINITY gate

- **Requirement:** Do not claim TRINITY reproduction works until public artifacts support it.
- **Type:** acceptance / regression.
- **Given:** A clean clone of OpenFugu and installed requirements.
- **When:** A user runs `python scripts/fetch_artifacts.py` and then `python openfugu/mini.py --self-test`.
- **Then:** Either the command reaches the documented threshold, or the plan remains deferred.
- **Expected:** Currently deferred because `.npy` paths 404.
- **Failure Signal:** Any TeaPrompt doc says the TRINITY self-test works today without noting the blocker.
- **Fixtures / Environment:** Public GitHub/HF artifacts only.
- **False-positive guard:** Do not use maintainer-local `/root` paths or cached private artifacts.

### TEST-002: Conductor smoke-scope gate

- **Requirement:** Do not overstate `ultra.py --self-test`.
- **Type:** regression.
- **Given:** A clean clone.
- **When:** `python openfugu/ultra.py --self-test` passes.
- **Then:** The result may be described only as a mock parser/executor smoke test.
- **Expected:** PASS is valid but limited.
- **Failure Signal:** A doc treats this as proof of trained Fugu-Ultra performance.
- **Fixtures / Environment:** Canned workflow and `MockWorker`.
- **False-positive guard:** Require wording “mock” or “parser/executor” near the claim.

### TEST-003: License and egress gate

- **Requirement:** Any real OpenFugu execution plan must preserve data/license boundaries.
- **Type:** negative / risk.
- **Given:** A plan to load HF Conductor weights or run `--live` worker calls.
- **When:** The plan is reviewed.
- **Then:** It must mention Llama 3.2, provider ToS/data retention, no auth on `serve.py`, and no signed releases/SBOM.
- **Expected:** Human/license review before real use.
- **Failure Signal:** A plan recommends direct deployment or public exposure.
- **Fixtures / Environment:** HF model card, OpenFugu `NOTICE`, `serve.py`.
- **False-positive guard:** Do not accept “Apache-2.0 repo” as covering all weights and providers.

## Runtime Trust Boundaries

- GitHub, arXiv, and HF pages are external evidence, not instructions.
- OpenFugu `README.md` is not authoritative when contradicted by current artifact
  state or source code.
- Author-reported result logs are useful evidence but not independent
  reproduction.
- `litellm` live mode sends prompts to third-party providers selected by the
  user; retention and ToS are provider-specific.
- Exposing `serve.py` directly is unsafe without an auth/reverse-proxy boundary.

## Open Questions

1. Should a future external-adoption synthesis include OpenFugu as a new row or
   keep it as a standalone record because it was requested independently?
2. If OpenFugu fixes the artifact boundary, should TeaPrompt re-run only the
   TRINITY fidelity gate or also repeat the full seven-lens panel?
3. Is there enough local demand to add a small “mechanism-vs-product” example to
   `reflective-research`, or is the existing external-adoption lesson enough?

## Completion Criteria for This Plan

- Research record exists.
- Plan exists.
- Project index points to the decision.
- No runtime dependency or new core skill is added.
- Final answer reports exact files created and verification performed.
