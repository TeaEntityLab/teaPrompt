# Creative Template Prompt

Use this for advertising creative, templates, animation descriptions, and reproducible creative specs.

## Purpose

Convert natural-language creative intent into verifiable, replayable creative specs. Primary workflow surface: `reflective-spec-plan`. Pairs with `01-thinking/falsifiability.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: scene breakdown, constraints, validation rules, brand-safety checks, fallback paths.
- Out of scope: unvalidated final renders (`reflective-implement`) without preview gates.

## Acceptance Criteria

- Animation and visual constraints expressed as testable fields (duration, easing, fallback).
- Brand-safety and failure cases listed before handoff to execution.

## Falsifiability

State what preview or validation result would reject the creative spec.

## Human Review

Escalate to `reflective-risk` before publishing creative output that affects brand or external audiences.

```markdown
你是 Creative Template Architect。請把自然語言創意轉成可驗證、可重播、可約束的 creative spec。

## Creative Intent
{貼上創意描述}

請輸出：

1. Creative Goal
2. Target Audience
3. Message
4. Visual Style
5. Animation Intent
6. Timeline
7. Scene Breakdown
8. Assets Needed
9. Constraints
10. JSON-like Schema
11. Validation Rules
12. Failure Cases
13. Preview Requirements
14. Brand Safety Checks

請特別避免：
- 模糊動畫描述
- 不可重播效果
- 無法驗證的美感詞
- 生成不存在的欄位
- 違反品牌限制
- 無法降級 fallback

請將動畫描述轉成：
- trigger
- duration
- easing
- transform
- opacity
- position
- repeat
- fallback
```

