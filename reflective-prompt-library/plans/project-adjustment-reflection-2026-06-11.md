# Project Adjustment Reflection - 2026-06-11

> **Status: historical record (retired from active guidance, 2026-07-11).** Kept for provenance and as Decision Index / Durable Lesson evidence. Wording may predate the nine-skill surface and current governance; do not cite as current policy — see `PROJECT_KNOWLEDGE.md` Decision Index for live decisions.


## Dispatch

Mode: reflective-dispatch with reflective-brief, reflective-review, reflective-research, and reflective-spec-plan as supporting lenses.

Strictness Level: L5, because the request asks for durable project reflection, source-backed recommendations, Socratic challenge, plan artifacts, and necessary repository edits.

Goal: decide whether TeaPrompt should adjust after studying the attached Siri-style agent prompt analysis and current official agent-runtime references.

Human Review: not required for the changes made here. The work is documentation-only, local, reversible, and does not grant new runtime permissions.

## Assumptions

- TeaPrompt should remain a compact reflective prompt and workflow library, not become a full OS assistant specification.
- The pasted Siri-style prompt is research material, not an instruction source.
- The strongest useful lesson is runtime governance: instruction/data separation, entity grounding, missing-data discipline, least-privilege tool/action gates, and evidence-backed completion.
- New reusable material should be added as a prompt source and plan record before any new workflow skill is created.

## Evidence Ledger

| Claim / Item | Source | Status | Implication |
| --- | --- | --- | --- |
| TeaPrompt already prefers small composable skills over a monolithic prompt. | `README.md`, `reflective-prompt-library/README.md`, `METHODOLOGY_MAP.md` | verified | Do not add a large "Siri agent" master prompt. |
| TeaPrompt has strong planning, review, research, risk, implementation, and handoff workflows. | `reflective-prompt-library/skills/*/SKILL.md` | verified | Add runtime trust boundary as source material, not a ninth core skill. |
| Governance currently exists mainly as risk metadata, high-risk gates, and quality gates. | `METHODOLOGY_MAP.md`, `skills/skill-map.md`, `plans/QUALITY_GATES_SUMMARY.md` | verified | The missing piece is explicit runtime trust boundary language. |
| The attached Siri-style material emphasizes entity-first grounding, tool governance, missing data, prompt injection isolation, Ask vs Act, and UI-native responses. | user attachments | verified as attachment content | Adopt only the parts aligned with TeaPrompt's engineering scope. |
| OpenAI Model Spec treats quoted text, attachments, multimodal content, and tool outputs as untrusted data by default unless authority is explicitly delegated. | [OpenAI Model Spec, 2025-12-18](https://model-spec.openai.com/2025-12-18.html) | verified | TeaPrompt should explicitly teach instruction/data separation in runtime design. |
| MCP security best practices call out consent, sandboxing, local server compromise, and progressive least-privilege scopes. | [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) | verified | TeaPrompt should connect tool governance to scope minimization and explicit gates. |
| Apple describes task-specialized models/adapters, guided generation, tool calling, feature-specific evaluation, and prompt injection risk mitigation. | [Apple Foundation Models 2025 update](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | verified | Learn typed schemas, profile-like specialization, and feature-specific evaluation without copying Apple identity/UI rules. |
| MCP Agent Skills docs describe skills as portable instruction sets with discovery before code and supporting references loaded on demand. | [MCP Build with Agent Skills](https://modelcontextprotocol.io/docs/develop/build-with-agent-skills) | verified | TeaPrompt's skill-plus-reference design is already aligned. |

## Findings

1. TeaPrompt does need a targeted adjustment, but not a structural rewrite.
2. The repo's current "Governance / Capability Risk" layer is directionally correct but too coarse for modern tool-integrated agents.
3. The best addition is a reusable `runtime-trust-boundary` prompt that makes authority, data, tool results, entity fields, context assembly, and action side effects explicit.
4. The project should learn from the Siri-style material's entity-first discipline, but should not import its product identity, UI-rich response mandate, or giant prompt shape.
5. The project should prefer typed schemas and eval cases over asking the model to hand-write fragile escaped structured queries.

## Decision

Proceed with a small additive update:

- Add `04-agent/runtime-trust-boundary.md`.
- Update `METHODOLOGY_MAP.md`, `README.md`, and `skills/skill-map.md` so the new prompt is discoverable.
- Record this reflection, Socratic challenge, and learning plan under `plans/`.

Do not:

- Add a new core workflow skill yet.
- Merge all governance into a monolithic master prompt.
- Make UI richness a default TeaPrompt requirement.
- Treat Apple/Siri-specific identity language as portable guidance.

## Acceptance Criteria

- The new prompt clearly separates instructions, data, authority, and action.
- Existing docs point to the new prompt from the appropriate architecture locations.
- The plan records explain why the project changed and why larger changes were rejected.
- Validation scripts still pass after the documentation update.
