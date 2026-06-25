# Retro Prompt

Use this after a task completes. The goal is process improvement, not self-congratulation.

## Purpose

Extract reusable process improvements from a completed task. Primary workflow surface: `reflective-handoff-retro`. Pairs with `01-thinking/socratic-reviewer.md`.

## Scope

- In scope: what went well/wrong, weak gates, reusable rules, skill/script/test candidates.
- Out of scope: active implementation (`reflective-implement`).

## Acceptance Criteria

- Root causes separated from symptoms.
- At least one reusable rule or anti-regression candidate.
- One-off accidents not promoted to permanent bureaucracy without recurrence evidence.

## Falsifiability

Name one proposed rule that would be rejected if the failure cannot recur.

## Human Review

Escalate promotion candidates that would change agent operating rules to explicit human approval.


```markdown
請做 Retrospective。目標是改進下次流程，而不是自我稱讚。

## 任務結果
{貼上結果}

請回答：

1. What went well?
2. What went wrong?
3. What was misunderstood?
4. Which assumptions were wrong?
5. Where did we waste tokens or time?
6. Which step should have had a stronger gate?
7. Did tests actually verify the important behavior?
8. Did we over-engineer?
9. Did we under-specify?
10. What should become a reusable rule, skill, script, or checklist?
11. What anti-regression rule should be added?

最後輸出：
- Lessons learned
- Rule updates
- Skill candidates
- Test candidates
- Next process improvement
```

