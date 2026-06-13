# Context Engineering Prompt

Use this before long tasks where context discipline matters.

```markdown
請以 Context Engineering 模式處理任務。

規則：

1. 只讀取與目前決策直接相關的內容。
2. 不要把大型原始資料完整塞入主回答。
3. 先建立資料索引，再分批處理。
4. 中間結果應摘要成 artifact。
5. 若有工具，將中間資料寫入檔案。
6. 主線程只保留：
   - goal
   - assumptions
   - current state
   - decisions
   - open risks
   - next action
7. 遇到大文件，先輸出：
   - 文件用途
   - 必讀區塊
   - 可略過區塊
   - 需要深入讀取的區塊
8. 不要依賴長 context 記憶專案狀態，請建立明確 artifact。

請在回答最後輸出：
- Context used
- Context ignored
- Information still missing
- Recommended next read
```

> **Composition note:** This prompt and `large-context.md` target the same large-context concern with different structures. When both are loaded, treat this prompt as the general principle and `large-context.md` as the 200K+ operationalization, or choose one as primary.

