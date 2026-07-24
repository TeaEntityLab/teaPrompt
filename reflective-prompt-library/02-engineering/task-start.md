# Task Start Prompt

Use this at the start of a new task before implementation.

## Purpose

Establish a task brief before implementation. Primary workflow surface: `reflective-brief`. Pairs with `01-thinking/why-what-how-done.md` and `01-thinking/falsifiability.md`.

## Scope

- In scope: goal, assumptions, scope boundaries, acceptance criteria, falsifiability, minimal plan before coding.
- Escalate: route to `reflective-spec-plan` when the brief is ready for ticket slicing.
- Out of scope: repository edits (`reflective-implement`), formal blast-radius gating (`reflective-risk`).

## Acceptance Criteria

- Goal and scope in/out stated.
- Acceptance criteria and falsifiability each named once.
- Minimal next step and defer list included.
- Any clarifying question names the local evidence checked and the material fork it could not resolve.

## Falsifiability

If the brief cannot name evidence that would prove the framing wrong, stop and clarify before planning.

```markdown
請先不要直接實作。請先為以下任務建立任務規格：

## 任務
{貼上任務}
若需要提問，請先簡短查閱可用的專案檔案、文件與既有記憶；只詢問查閱後仍無法判定，而且會影響方向的分歧。

## 請輸出

1. Goal：真正目標
2. Why：為什麼重要
3. Scope In：範圍內
4. Scope Out：範圍外
5. Inputs：需要哪些輸入
6. Outputs：應交付什麼
7. Assumptions：目前假設
8. Unknowns：未知問題
9. Risks：主要風險
10. Failure Conditions：什麼情況算失敗
11. Acceptance Criteria：驗收標準
12. Falsifiability：什麼證據會證明方向錯誤
13. Minimal Plan：最小可行計畫
14. Human Review Triggers：哪些情況需要人工審查

請最後給出：
- 建議採取的最小下一步
- 不建議現在做的事
```

> **Composition note:** When composed with `03-context/medium-context.md`, this prompt serves as the primary output template and `medium-context.md` provides window-size guidance for 32K-128K contexts.

