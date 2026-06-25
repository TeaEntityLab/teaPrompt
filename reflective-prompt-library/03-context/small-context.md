# Small Context Window Prompt

Use this for 4K-16K context windows, small models, mobile, or low-cost model runs.

## Purpose

Operate under small context windows (4K–16K) or low-cost models. Primary workflow surfaces: `reflective-brief` and `reflective-dispatch`. Pairs with `01-thinking/critical-thinking-check.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: conclusion-first answers, minimal assumptions, and capped risks and plan steps.
- Out of scope: long-chain reasoning or full engineering ticket packs.

## Acceptance Criteria

- At most three risks and three to five plan steps unless escalated.
- Next action is directly executable.

## Falsifiability

State what evidence would require escalating to `medium-context.md`.

## Human Review

Escalate to `reflective-risk` when window limits would hide safety-critical unknowns.

```markdown
你在小 context window 中工作。請極度節省 token。

任務：
{貼上任務}

規則：
1. 先給結論。
2. 只列最重要假設。
3. 不展開長推理。
4. 不重複題目。
5. 只保留 3 個風險。
6. 只給 3–5 步計畫。
7. 輸出可直接執行的下一步。
8. 若資訊不足，列出最少必要問題，不超過 3 個。

輸出格式：
- Goal
- Assumptions
- Recommendation
- Minimal Plan
- Acceptance Criteria
- Risks
- Next Action
```

