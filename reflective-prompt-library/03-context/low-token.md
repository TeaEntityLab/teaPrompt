# Low Token Mode Prompt

Use this when budget, latency, or model quota is tight.

## Purpose

Budget-aware terse output when latency or quota is tight. Primary workflow surfaces: `reflective-dispatch` (L1 fast path) and `reflective-brief`. Pairs with `01-thinking/critical-thinking-check.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: minimal decision, reason, plan, and acceptance output under strict length caps.
- Out of scope: full spec slicing (`reflective-spec-plan`) or repository implementation.

## Acceptance Criteria

- Fixed output slots are filled without narrative padding.
- Stop condition is explicit.

## Falsifiability

Name one omitted slot that would make the answer non-actionable.

## Human Review

Escalate to `reflective-risk` when compression would hide safety-critical assumptions.

```markdown
低 token 模式。請只輸出必要內容。

任務：
{貼上任務}

格式：

Decision:
Reason:
Assumptions:
Risks:
Next 3 steps:
Acceptance:
Stop condition:
```

