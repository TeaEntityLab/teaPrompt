# Large Context Window Prompt

Use this for 200K-1M context windows while avoiding context rot.

## Purpose

Use 200K–1M windows without context rot via index-extract-synthesize. Primary workflow surfaces: `reflective-research` and `reflective-spec-plan`. Pairs with `01-thinking/falsifiability.md` and `01-thinking/critical-thinking-check.md`.

## Scope

- In scope: three-stage pipeline, selective extraction, and synthesis artifacts.
- Out of scope: assuming long context equals reliable understanding.

## Acceptance Criteria

- All three stages are completed in order.
- Pairs with `context-engineering.md` per the composition note below.

## Falsifiability

State what contradiction in source material would invalidate the synthesis.

```markdown
你在大型 context window 中工作，但不要假設長 context 等於可靠理解。

任務：
{貼上任務}

請分三階段處理：

## Stage 1: Index
先建立輸入內容索引：
- 有哪些文件 / 區塊
- 各自用途
- 哪些與任務高度相關
- 哪些可忽略

## Stage 2: Extract
只抽取與任務直接相關的資訊：
- claims
- evidence
- constraints
- requirements
- risks
- decisions

## Stage 3: Synthesize
整合成：
- Goal
- Assumptions
- Design
- Trade-offs
- Acceptance Criteria
- Implementation Plan
- Validation Plan
- Open Questions

規則：
- 不要因為 context 很大就全部使用。
- 避免被早期或中段資料帶偏。
- 主動檢查矛盾資訊。
- 對不同來源的可信度分級。
- 最後輸出「使用了哪些資訊 / 忽略了哪些資訊 / 為什麼」。
```

> **Composition note:** This prompt and `context-engineering.md` target the same large-context concern with different structures. When both are loaded, prefer one as primary or treat `context-engineering.md` as the general principle and this prompt as the 200K+ operationalization.

