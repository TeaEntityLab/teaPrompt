# Agent Selection Prompt

Use this to decide whether a task should use prompting, artifacts, coding agents, workflow engines, or a full agent system.

```markdown
請判斷以下任務應該用 Prompting、文件 workflow、Agentic Coding、Workflow Engine，還是完整 Agent System。

## 任務
{貼上任務}

請根據以下因素評估：

1. 任務複雜度
2. 是否需要工具
3. 是否需要讀寫檔案
4. 是否需要測試
5. 是否需要多輪執行
6. 是否需要狀態保存
7. 是否需要 resume
8. 是否涉及風險
9. Token 成本
10. 人類時間成本
11. 失敗代價
12. 是否高頻重複

請輸出：

| 層級 | 是否適合 | 理由 |
|---|---|---|

層級：
- Prompt-only
- Prompt + Artifact
- Agentic Coding
- Workflow Engine
- Full Agent System

最後給：
- 建議層級
- 最小可行做法
- 不應該過度工程的部分
```

