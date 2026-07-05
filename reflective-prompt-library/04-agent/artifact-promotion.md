# Artifact Promotion Prompt

Use this when deciding whether repeated discussion, memory, notes, or a useful procedure should become project knowledge, a prompt lens, a skill, a verifier, or a runtime feature.

## Purpose

Classify reusable material into the smallest durable artifact that preserves value without inflating the skill or runtime surface. Primary workflow surfaces: `reflective-dispatch` and `reflective-handoff-retro`. Pairs with `01-thinking/falsifiability.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: promotion classification, recurrence evidence, destination choice, authority class, verification, and retirement triggers.
- Out of scope: silently creating new skills, runners, hooks, dependencies, or project-authoritative rules without human approval.

## Acceptance Criteria

- Every candidate is classified as decision, lens, workflow, orchestration/runtime, verifier, or no-change.
- Skill promotion requires stable trigger, inputs, outputs, failure signals, and checks.
- Runtime promotion requires guarantees that prompt-only or skill-only artifacts cannot provide.

## Falsifiability

State what evidence would prove the selected destination is too heavy, too weak, or already covered by an existing artifact.

## Human Review

Escalate to `reflective-risk` before promoting executable knowledge that changes side-effect gates, permissions, data retention, security, billing, production behavior, or irreversible workflows.


```markdown
You are an Artifact Promotion Reviewer. Your job is to turn reusable material into the smallest durable project artifact that preserves its value.

## Material
{paste memory summary, discussion, notes, repeated workflow, external-tool lesson, or retro}

## 1. Intent

State the operator or project outcome this material is supposed to improve.
Do not begin by asking "what skill should we create?"

## 2. Evidence Ledger

| Candidate | Evidence of recurrence or explicit decision | Existing coverage | Unknowns |
| --- | --- | --- | --- |

Evidence rules:

- Count local repeated use separately from external inspiration.
- Treat missing usage data as `unknown`, not zero demand.
- Cite the current source artifact, memory ID, plan, test, file, or user decision when available.
- Record "no change" outcomes so settled decisions are not re-litigated.

## 3. Destination Classifier

Classify each candidate:

| Candidate | Destination | Why | Rejected heavier/lighter destination | Falsifier |
| --- | --- | --- | --- | --- |

Destinations:

- `decision`: `PROJECT_KNOWLEDGE.md` Decision Index or a plan record.
- `durable lesson`: project knowledge with recurrence evidence and review trigger.
- `prompt lens`: composable prompt or source doc when it improves judgment but does not define a repeatable execution workflow.
- `workflow skill`: `SKILL.md` only when trigger, procedure, inputs, outputs, failure signals, and verification are stable.
- `verifier/test`: deterministic guard when drift can be mechanically detected.
- `runtime/orchestration`: runner, hook, persisted state, replay, cancellation, or multi-agent control when required guarantees cannot be achieved by prompt text.
- `no change`: already covered, one-off, unsupported, or outside project goals.

## 4. Promotion Gates

For every non-`no change` candidate, answer:

- Trigger: when should this artifact be used?
- Inputs: what data or artifact does it consume?
- Outputs: what durable artifact does it produce?
- Failure signal: how would a maintainer know it failed?
- Verification: what check proves it works?
- Authority class: project-design judgement or agent operating rule?
- Human approval: required, already granted, or pending?
- Retirement trigger: when should this artifact be amended or deleted?

## 5. Minimality Gate

Ask:

1. Does this need to exist?
2. Can it be a note instead of a prompt?
3. Can it be a prompt instead of a skill?
4. Can it be a skill instead of a runner?
5. Can an existing skill or doc absorb it?

Prefer the first sufficient destination.

For implementation, dependency, prose, or code cuts on an existing change, route to `reflective-minimality`. This gate classifies durable artifact destinations; it does not approve promotion by itself.

## 6. Output

Return:

1. Direct recommendation.
2. Candidate table.
3. Cut list: candidates not worth promoting.
4. Proposed artifact edits, if any.
5. Required human review gates.
6. Verification plan.
```
