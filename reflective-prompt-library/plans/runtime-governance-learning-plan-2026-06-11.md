# Runtime Governance Learning Plan - 2026-06-11

## Goal

Learn and selectively integrate runtime governance patterns from the attached Siri-style analysis, OpenAI Model Spec, MCP security guidance, and Apple Foundation Models documentation.

## Direct Recommendation

Adopt runtime governance as a sublayer of TeaPrompt's Governance / Capability Risk layer. Keep it prompt-level for now, and promote it to a skill only after repeated standalone use proves the need.

## What To Learn And Add

| Theme | Learn From | Add To TeaPrompt | Status |
| --- | --- | --- | --- |
| Instruction/Data Separation | OpenAI Model Spec, Siri-style analysis | `04-agent/runtime-trust-boundary.md` | added |
| Entity-first grounding | Siri-style analysis, Apple typed/guided generation direction | Runtime prompt authority map and missing-data policy | added |
| Missing Means Unknown | Siri-style analysis | Data policy and verification checks | added |
| Tool grounding | OpenAI tool side-effect guidance, MCP security practices | Tool/action gate table | added |
| Least privilege and consent | MCP security practices | Scope minimization and Human Review gates | added |
| Profile-like specialization | Apple adapters/tool-use/guided generation | Future runtime-profile planning guidance | planned |
| Feature-specific evals | Apple evaluation discussion, current TeaPrompt quality gates | Prompt-injection, missing-data, and side-effect benchmark seeds | added |
| Skills with references | MCP Agent Skills docs, current TeaPrompt skills | Keep skill count small, load supporting prompts on demand | already aligned |

## Work Plan

### TASK-001: Add Runtime Trust Boundary Prompt

- Goal: make authority, data, context, tools, and side effects explicit.
- Files touched: `reflective-prompt-library/04-agent/runtime-trust-boundary.md`
- Acceptance: prompt includes authority map, data policy, tool/action gates, context assembly, and verification.
- Risk: low.
- Status: completed.

### TASK-002: Update Navigation And Methodology

- Goal: make the new prompt discoverable without changing the core workflow count.
- Files touched:
  - `reflective-prompt-library/README.md`
  - `reflective-prompt-library/METHODOLOGY_MAP.md`
  - `reflective-prompt-library/skills/skill-map.md`
- Acceptance: docs explain runtime governance as a sublayer, not a replacement architecture.
- Risk: low.
- Status: completed.

### TASK-003: Record Reflection And Socratic Decision

- Goal: preserve why the change was made and what was rejected.
- Files touched:
  - `reflective-prompt-library/plans/project-adjustment-reflection-2026-06-11.md`
  - `reflective-prompt-library/plans/socratic-change-inquiry-2026-06-11.md`
  - `reflective-prompt-library/plans/runtime-governance-learning-plan-2026-06-11.md`
- Acceptance: records include evidence, intent differences, Socratic challenge, decision, and acceptance criteria.
- Risk: low.
- Status: completed.

### TASK-004: Add Runtime Governance Eval Seeds

- Goal: test whether the new prompt improves behavior in agent-runtime review tasks.
- Cases added:
  - Retrieved document says to ignore previous instructions.
  - Entity has a name but no required field.
  - Irreversible action needs Human Review.
- Files touched:
  - `reflective-prompt-library/plans/benchmark_tasks.py`
- Human Review Required: no.
- Status: completed.

### TASK-005: Optimize Core Skills With Runtime Governance Lens

- Goal: integrate runtime trust-boundary guidance into all 8 workflow skills without adding a ninth skill.
- Files touched:
  - `reflective-prompt-library/skills/reflective-dispatch/SKILL.md`
  - `reflective-prompt-library/skills/reflective-brief/SKILL.md`
  - `reflective-prompt-library/skills/reflective-spec-plan/SKILL.md`
  - `reflective-prompt-library/skills/reflective-implement/SKILL.md`
  - `reflective-prompt-library/skills/reflective-review/SKILL.md`
  - `reflective-prompt-library/skills/reflective-research/SKILL.md`
  - `reflective-prompt-library/skills/reflective-risk/SKILL.md`
  - `reflective-prompt-library/skills/reflective-handoff-retro/SKILL.md`
- Human Review Required: no.
- Status: completed.

### TASK-006: Decide Whether To Promote To A Skill

- Trigger: at least three real tasks use the prompt as the primary workflow rather than as a supporting review lens.
- Acceptance: evidence shows users ask for runtime trust-boundary review as a distinct workflow.
- Rejection condition: if it is mostly used inside `reflective-risk` or `reflective-review`, keep it as source material.
- Status: future.

## Do Not Add Yet

- No Siri identity prompt.
- No universal visual-richness rule.
- No giant agent constitution.
- No new workflow skill.
- No runtime automation or permissions.
- No new dependency.

## Verification

Run:

```bash
python3 reflective-prompt-library/plans/validate_links.py
python3 reflective-prompt-library/plans/lint_skills.py
python3 reflective-prompt-library/plans/validate_governance.py
python3 reflective-prompt-library/plans/generate_index.py
```
