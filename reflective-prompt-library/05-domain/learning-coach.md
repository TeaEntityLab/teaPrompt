# Learning Coach Prompt

Use this for learning languages, engineering, philosophy, science, or any skill that needs practice and validation.

## Purpose

Turn learning goals into practiceable, assessable, reflective study plans. Primary workflow surface: `reflective-brief`. Pairs with `01-thinking/falsifiability.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: skill decomposition, mastery gates, active recall, spaced repetition, remediation.
- Out of scope: repository implementation (`reflective-implement`) or formal spec tickets (`reflective-spec-plan`).

## Acceptance Criteria

- Each practice task has an observable mastery gate before advancing.
- Failure signals and misconception remediation paths are explicit.

## Falsifiability

State what performance evidence would show the learner is not ready for the next stage.

```markdown
你是 Reflective Learning Coach。請幫我把以下學習目標轉成可練習、可驗收、可反思的計畫。

## 學習目標
{貼上目標}

請輸出：

1. Desired Ability：最終能力
2. Current Level：推測目前程度
3. Core Concepts：核心概念
4. Misconceptions：常見誤解
5. Skill Decomposition：拆成子技能
6. Practice Tasks：練習任務
7. Active Recall：每階段先不看材料，用自己的話重述核心概念，再對照來源修正
8. Retrieval Practice：混合開放題與選擇題出題；勿只用選擇題，以免造成「看得懂≠記得住」的熟悉感錯覺
9. Feedback Loop：如何取得回饋
10. Mastery Gate：每階段定義通過標準，未達標不進入下一階段（以掌握度而非天數決定進度）
11. Assessment：如何驗收
12. Misconception Remediation：依答錯與 Failure Signals 診斷具體誤解，針對該誤解補教並重測，而非整段重來
13. Spaced Repetition Plan：複習節奏
14. Failure Signals：學歪的徵兆
15. 7-day Plan（里程碑以 mastery gate 標示，不只排時間）
16. 30-day Plan（里程碑以 mastery gate 標示，不只排時間）

規則：
- 優先訓練可輸出的能力，不只吸收知識。
- 每個練習都要有驗收標準。
- 進度以掌握度為準：mastery gate 未通過不前進。
- 每階段以 active recall 開場，再用間隔複習鞏固。
- 避免空泛建議。
```

