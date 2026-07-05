# `reflective-dispatch` Examples

## Example 1

Input:

```text
We need to redesign onboarding flow, maybe new APIs, maybe policy updates. Help me choose the process first.
```

Expected output shape:

```markdown
Mode: routing
Strictness: L2
Goal: select execution lane for onboarding redesign
Assumptions: current APIs can be changed
Workflow: reflective-brief -> reflective-spec-plan
Route Confidence: medium
Enhancements Enabled: brief before planning
Enhancements Available: risk gate if policy/auth scope appears
Human Review: required if policy/auth scope expands
Next Action: produce brief with scope and acceptance criteria
```

## Example 2

Input:

```text
Patch this auth permission bug in production today.
```

Expected output shape:

```markdown
Mode: routing
Strictness: L4
Goal: fix auth bug safely
Assumptions: production impact likely
Workflow: reflective-risk -> reflective-implement -> reflective-review
Route Confidence: high
Enhancements Enabled: risk gate, rollback planning, review
Enhancements Available: security review after bounded patch
Human Review: required before production action
Next Action: create dry-run and rollback gate
```

