---
name: verification-map-generator
description: Use when a product repository needs an agent-drivable verification surface — a VERIFY.md control doc, a features/ map routing feature areas to drive commands, and optionally a locked acceptance spec — so a fresh agent can verify the product, classify failures (product regression / doc drift / spec-oracle error / harness failure), and keep the map event-driven. Proven on HTTP servers (curl surface) and libraries (test-suite surface) across JS, Go, and Rust.
license: MIT
compatibility: Requires a product repo with an executable check surface (test suite, HTTP routes, CLI). Generated docs live in the product repo, not TeaPrompt.
metadata:
  risk_level: low
  human_review_required: false
  external_io: false
  context_load: medium
---

# Verification Map Generator

**Type:** Domain-pack skill (artifact generation) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Generate the smallest durable verification surface for a product repo so that a *fresh* agent — no conversation history — can launch, doctor, drive, and classify failures without operator-supplied navigation. Evidence: `PROJECT_KNOWLEDGE.md` verification-map durable lesson (four products — HTTP server plus Go/JS/Rust libraries; unlabeled seeded bugs caught, spec-oracle errors classified, doc drift detected including in the generator's own output).

## Module Contract

Trigger:

- The user names a product repo and asks for verification assets, a control surface, a feature map, or "do experiments on" a repo.
- A product needs repeated agent-driven verification where transcript memory cannot carry the procedure.

Methods:

- Control-surface identification: server → launch + HTTP routes; library → test runner + scratch-driver recipe; environment quirks recorded verbatim.
- Feature partitioning: one map file per feature area with `source_commit` / `last_verified_at` / `verification_status` metadata.
- Four-way failure classification: product regression / doc drift / spec-oracle error / harness failure.
- Fresh-agent proof: the map is verified by a fresh agent completing the sweep, plus correct classification under an unlabeled seeded bug.

Output:

- `VERIFY.md`, `features/README.md` + per-feature files, optional locked `acceptance.yaml` — all inside the product repo.

Escalation:

- Route products with no executable check surface (no tests, no routes, no CLI) to `reflective-spec-plan` for a test-design pass first — the map routes to checks that exist; it does not invent them.
- Route auth, permissions, security-sensitive, or destructive verification steps to `reflective-risk` before generating drive commands that exercise them.

Inputs:

- The product repo (read-only during generation).
- Its existing check surface: test suite, HTTP routes, CLI commands — the map routes to what exists; it does not invent a runner.

Failure signals:

- A fresh agent cannot complete the sweep without asking for navigation help.
- A seeded unlabeled bug is not classified product regression.
- A stale map is not classified doc drift; a wrong spec is not classified spec-oracle error.

Verification: run a fresh agent against the generated docs on the healthy product (must pass clean), then on a copy with an **unlabeled** seeded bug (must classify product regression). Never label seeded bugs — a `// SEEDED BUG` comment lets the no-docs arm detect it from source and weakens the measurement.

## Generation Procedure

1. **Identify the control surface.** Server → launch command + curl/HTTP routes. Library → test runner (`go test`, `npm test`, `cargo test`) + scratch-driver recipe for uncovered behavior. Record environment quirks verbatim (e.g. `-mod=mod` for stale vendor trees) — a quirk documented is a harness failure prevented.
2. **Write VERIFY.md.** Launch, doctor (fast smoke), drive, evidence, the four-way failure classification table, cleanup. Every command must be copy-paste runnable; verify each one yourself before writing it — a wrong command in VERIFY.md is doc drift the first agent will find.
3. **Partition features.** One file per feature area, 3–6 files total. Each carries `source_commit` + `last_verified_at` + `verification_status` metadata, entry points, drive commands (per-area test regexes or route lists), observable outcomes, failure paths, evidence.
4. **Optionally write acceptance.yaml.** Locked, small (3–6 checks), covering the highest-value invariants. Every check expression must use API names verified against the source — a check that does not compile or run is a harness failure, not a spec-oracle error, and teaches the verifier nothing. Mark the file read-only; a spec-vs-product mismatch must be classifiable as spec-oracle error.
5. **Verify the map before handing off.** Run every drive command; confirm outcomes match what you wrote. API names, casing, and flags are the top drift sources — check them against source, not memory.

## Failure Classification (canonical table — copy into VERIFY.md)

| Class | Meaning | Repair |
| --- | --- | --- |
| Product regression | Product behavior changed for the worse | Report; never edit map/spec/tests to match |
| Doc drift | Docs no longer match a healthy product | Update the doc |
| Spec/oracle error | The acceptance spec or test expectation is wrong | Oracles read-only; propose change for review |
| Harness failure | Toolchain, launch, environment, external dep broke | Fix the harness |

## Maintenance Rule

Event-driven, not calendar-driven: re-verify a feature file when its covered source changes; update `source_commit`/`last_verified_at`. A `verification_status: failed` means the product changed — classify before editing the map.

## Never

- Do not write the map from memory of the API — verify every command and name against the source first.
- Do not label seeded bugs used to test the map.
- Do not let the map describe behavior the product does not have; a map that matches a broken product hides the regression.
- Do not add driver/test files inside the product repo during verification — scratch drivers live outside with a path/replace reference.
- Do not treat a green run as proof the map is right — the map is proven by a fresh agent completing the sweep and by correct failure classification under seeded faults.

## Examples

Companion examples live at `<skills-root>/examples/verification-map-generator.examples.md` when co-installed. They show generated-surface shapes and expected fresh-agent verdicts, not proof that code was executed.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `PROJECT_KNOWLEDGE.md` (verification-map durable lesson and evidence pointer)
- `04-agent/artifact-promotion.md` (promotion gates this skill passed)
