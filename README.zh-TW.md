Language: [English](README.md) | 繁體中文

> **翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](README.md)存在差異。完整、權威的內容請以英文版為準。翻譯管理見 [LANGUAGE_POLICY.md](reflective-prompt-library/LANGUAGE_POLICY.md)。

# TeaPrompt

TeaPrompt 是一套給 AI 協作工程使用的反思型 Prompt 與 Workflow Library。

核心原則：

```text
Doing the right thing > doing things right.
```

此 repository 包含：

- `reflective-prompt-library/`：可重用的提示詞文件（思考、規劃、實作、審查、研究、風險、交接）。
- `reflective-prompt-library/skills/`：精簡的 `SKILL.md` 工作流包裝。
- `reflective-prompt-library/plans/`：流程與工具化後續規劃文件。
- `reflective-prompt-library/SKILL_INSTALLATION.md`：Claude / Codex / Cursor / Antigravity / OpenCode 安裝說明。
- `reflective-prompt-library/METHODOLOGY_MAP.md`：方法論分類與嚴格度分級地圖。
- `reflective-prompt-library/LANGUAGE_POLICY.md`：語言政策（操作層英文 + 本地化 prompt source）。

## 快速開始

先看主庫：

```text
reflective-prompt-library/README.md
```

或直接安裝 workflow skill 到兼容目錄：

```text
.claude/skills/<skill-name>/SKILL.md
~/.codex/skills/<skill-name>/SKILL.md
.agents/skills/<skill-name>/SKILL.md
```

各平台安裝路徑請見 [Skill Installation Guide](reflective-prompt-library/SKILL_INSTALLATION.md)。
方法論邊界請見 [Methodology Map](reflective-prompt-library/METHODOLOGY_MAP.md)。
語言規範請見 [Language Policy](reflective-prompt-library/LANGUAGE_POLICY.md)。

## 推薦入口

- 分流先用 `reflective-dispatch`
- 任務定義用 `reflective-brief`
- 寫規格用 `reflective-spec-plan`
- 實作用 `reflective-implement`
- 審查用 `reflective-review`
- 高風險先走 `reflective-risk`

## 設計理念

TeaPrompt 將 prompts 與 workflows 分離：

- **Prompts** 提供細膩的判斷框架與可重用的措辭。
- **Skills** 提供可重複的執行流程——它們是 prompt 層級的工作流程描述，由使用者的 agent runtime 解譯執行，而非多 agent 編排層。
- **Plans** 記錄未來程式或工作流自動化的規劃，避免過早過度設計。

工作流層刻意使用數量少、可組合的 broad skills，而不是每個 prompt 對應一個 skill。

## License

MIT，見 [LICENSE](LICENSE)。
