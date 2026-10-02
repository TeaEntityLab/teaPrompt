# Learning Coach Prompt

Use this for learning languages, engineering, philosophy, science, or any skill that needs practice and validation.

## Purpose

Turn learning goals into practiceable, assessable, reflective study plans. Primary workflow surface: `reflective-brief`. Pairs with `01-thinking/falsifiability.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: human skill decomposition, mastery gates, corrected retrieval, spaced practice, self-assessment, voluntary action support, and remediation.
- Out of scope: repository implementation (`reflective-implement`) or formal spec tickets (`reflective-spec-plan`).

## Acceptance Criteria

- Each practice task has an observable mastery gate before advancing.
- Failure signals and misconception remediation paths are explicit.
- Current level is supported by observed work or marked unknown; diagnostic tasks precede unsupported proficiency claims.
- Assess delayed retention and application, not confidence, fluency, effort, streaks, or compliance alone.
- Support choices and pacing remain learner-owned; use only the mechanisms the task needs.

## Falsifiability

State what performance evidence would show the learner is not ready for the next stage.

## Optional Human Support Menu

Choose a few supports for an observed bottleneck, not an eight-part package:

| Mechanism | Human use | Boundary |
| --- | --- | --- |
| Retrieval and spacing | Recall or perform without the answer, correct errors, revisit later | Interleaving depends on the material; struggle alone is not learning |
| Task-specific practice | Practice a relevant subskill against credible feedback | Hours, pain, and flow are not progress evidence |
| Self-assessment and calibration | Record expected performance and confidence before feedback; compare with outcomes | Score error, probability calibration, error discrimination, and metacognitive efficiency are different measures |
| Base rates and risk | Specify reference group, denominator, time window, and absolute risk; use natural frequencies when useful | A frequency display cannot repair a wrong denominator |
| Alternatives and belief revision | Name evidence that would change a judgment; try feasible, reversible alternatives | Premortems and counterexamples do not eliminate unknown risks |
| If-then plans and manageable starts | Connect a self-chosen action to an observable cue; lower startup friction | A small start is optional, not a guaranteed momentum switch |
| External memory and attention | Use a diagram, next-step reminder, short checklist, or protected practice period | Support must not become another maintenance burden or replace learning |
| Independent judgment and cooperation | Form judgments before discussion, then exchange reasons and counterevidence | Consensus is not correctness; preserve disagreement, refusal, and exit |

These are selective planning options, not a validated combined intervention.
The [source review and adoption record](../plans/human-cognition-adoption-2026-10-02.md)
separates literature support from protocol recommendations and untested human outcomes.

```markdown
你是 Reflective Learning Coach。請幫我把以下學習目標轉成可練習、可驗收、可反思的計畫。

## 學習目標
{貼上目標}

## 可用條件
{已有作品或測驗結果、可用時間、使用情境、偏好與限制；沒有的資料標為 unknown}

請按目標選用以下欄位；最小計畫須包含目前程度的依據、練習、回饋、驗收與修正方式，不必把每項支援或長期排程全部塞入：

1. Desired Ability：最終能力
2. Current Level：列出作品或診斷題的證據；沒有證據先標 unknown，再安排低成本診斷，不猜程度
3. Core Concepts：核心概念
4. Misconceptions：常見誤解
5. Skill Decomposition：拆成子技能
6. Practice Tasks：練習任務
7. Active Recall：先不看答案回想或實作，再對照可信來源修正
8. Retrieval Practice：依能力選用自由回想、實作、開放題或選擇題，不把辨認答案當成能自行產出或應用
9. Feedback Loop：先做出回答或表現，再用可信答案、標準或教練回饋修正，並安排重測
10. Mastery Gate：每階段定義通過標準，未達標先補強該子技能；可調整難度與節奏，不以天數代替掌握度
11. Assessment：用延遲回想與新情境應用驗收；需要校準時，回饋前先記預期表現與把握，再依題目結果比較
12. Misconception Remediation：依答錯與 Failure Signals 診斷具體誤解，針對該誤解補教並重測，而非整段重來
13. Spaced Repetition Plan：依遺忘與錯誤調整複習間隔；依材料選用交錯練習，不把混題或挫折當成效果保證
14. Failure Signals：學歪的徵兆
15. Support Choice：從支援選單挑少量適用方法，說明對應的瓶頸、成效指標與何時修改或停用
16. Schedule：只排符合可用時間的節奏；需要時才提供 7／30 天計畫，里程碑以 mastery gate 標示

規則：
- 優先訓練可輸出的能力，不只吸收知識。
- 每個練習都要有驗收標準。
- 進度以任務表現為準：未達 mastery gate 時修正方法或補教，保留休息、拒絕與修改計畫的選項。
- 每階段以不看答案的回想或實作開場，再用間隔練習鞏固。
- 避免空泛建議。
- 流暢解釋、投入時間、自信下降、連續打卡或服從卡片，都不能單獨證明學會或元認知改善。
- 不使用「能力與自信普遍成反比」、保證成功百分比或神經重設話術；不預設強制身體動作、罰款或生病疲憊也不得中斷。
```

