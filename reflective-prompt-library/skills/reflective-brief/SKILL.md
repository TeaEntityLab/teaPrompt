---
name: reflective-brief
description: Use this to start non-trivial tasks, clarify real goals, define assumptions, scope, acceptance criteria, falsifiability, and the minimal next step before planning or implementation. Especially useful when a request is broad but safe to proceed with explicit assumptions.
license: MIT
metadata:
  risk_level: low
  human_review_required: false
  external_io: false
  context_load: low
---

# Reflective Brief

**Type:** Prompt-level workflow

## Purpose

Turn a request into a small, testable task brief before deeper work.

## Module Contract

Trigger:
- Use when a non-trivial request is broad, fuzzy, assumption-heavy, or needs goal, scope, assumptions, stakeholder alignment, acceptance criteria, failure conditions, and falsifiability before planning, PRD/ticket work, or execution.

Methods:
- Why / What / How / Done
- Job-to-be-done clarification
- Assumption audit
- Authority and missing-data audit
- Scope split
- Failure conditions and falsifiability

Output:
- Output a brief with `Goal`, `Why`, `Intended Outcome`, `Assumptions`, `Authority / Missing Data Notes`, `Scope`, `Inputs / Outputs`, `Failure Conditions`, `Acceptance Criteria`, `Falsifiability`, `Minimal Plan`, `Human Review Triggers`, and `Next Action`.

Never:
- Do not plan implementation details before the goal, scope, and acceptance criteria are usable.
- Do not hide unknowns in vague wording.
- Do not dump raw, unfiltered reasoning tokens. Structured reasoning sections (Goal/Assumptions/Socratic audit/etc.) are the required output format and are not hidden chain-of-thought.

Escalation:
- Route high-risk branches to `reflective-risk`.
- Route ready specs or ticket slicing to `reflective-spec-plan`.

## Workflow

1. Identify the real goal.
2. Clarify the intended user outcome (job-to-be-done).
3. Separate problem, symptom, and proposed solution.
4. State assumptions and unknowns; an unresolved high-impact, irreversible assumption is a Human Review trigger, not a default. Before an unknown becomes a question to the user, classify it: answerable from the repository or tools (look), safe to assume (state it with its status), or the owner's decision (ask); only the last kind is asked.
5. Classify inputs as user intent, project instruction, retrieved data, tool result, or unknown.
6. Define scope in / scope out.
7. Define inputs and outputs.
8. Define failure conditions.
9. Define acceptance criteria.
10. Define falsifiability: what evidence would prove this direction wrong.
11. Write the Minimal Plan: the smallest How that could satisfy the acceptance criteria.
12. Choose the Next Action.

Spike / exploration framing: when acceptance criteria can only emerge from building (prototype, spike, throwaway experiment), do not force full criteria up front. Set the acceptance criterion to the question the prototype must answer plus a timebox, state that the artifact is disposable, and route promotion of any surviving code through `reflective-review` (and `reflective-risk` when high-risk) before it becomes production work. The spike ends only with observed run output, a measurement, or an explicit could-not-run bound, and names the decision that evidence unblocks; a designed but unrun experiment is not an answer.

### Intent Fidelity

Name what the spec will not capture — tacit constraints, unknown unknowns, and non-functional expectations — as unknowns with an owner, so intent loss is visible before planning starts.
Each assumption carries a status — `open`, `confirmed`, `refuted`, or `stale` — and a change to the goal marks dependent assumptions `stale`.

## Output

```markdown
## Goal

## Why

## Intended Outcome (JTBD)

## Assumptions

## Authority / Missing Data Notes

## Scope
- In:
- Out:

## Inputs / Outputs

## Failure Conditions

## Acceptance Criteria

## Falsifiability

## Minimal Plan

## Human Review Triggers

## Next Action
```

## Operating Rules

- Ask only when missing information changes safety, architecture, cost, privacy, data loss, or irreversibility.
- Before asking for clarification, make a brief, targeted check of available repository files, documentation, and durable memory. Ask only about a material fork the evidence cannot resolve; stop investigating once the question is specific.
- Missing information is unknown, not negative evidence or permission to infer sensitive facts.
- If ambiguity is safe, proceed with explicit assumptions.
- Provide concise reasoning summaries and clean artifacts; the raw-reasoning-token rule is defined once under `Never`.
- If outcome is unclear, ask one direct question or state one reversible assumption and continue.

## Examples

Companion examples live in the installed `<skills-root>/examples/reflective-brief.examples.md` tree when examples are co-installed. They show expected input/output shapes, not a separate runtime contract.

## Prompt Sources

Use these library prompts for exact wording when needed:

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `00-core/core-short.md`
- `02-engineering/task-start.md`
- `01-thinking/why-what-how-done.md`
- `01-thinking/falsifiability.md`
- `04-agent/runtime-trust-boundary.md`
