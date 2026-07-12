Language: [English](README.md) | 繁體中文

> **翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](README.md)存在差異。完整、權威的內容請以英文版為準。翻譯管理見 [LANGUAGE_POLICY.md](reflective-prompt-library/LANGUAGE_POLICY.md)。

# TeaPrompt

TeaPrompt 是一套給 AI 協作工程使用的反思型 Prompt 與 Workflow Library。

核心原則：

```text
Doing the right thing > doing things right.
```



## 北極星（North Star）

TeaPrompt 幫助人類與宿主 agent 為任務選擇**恰當的嚴謹度**，記錄**決策理由**，並以**證據**驗證結果 —— 透過可組合的 prompt 層與九個 workflow skills 作為自然語言 harness policy，**不**自建 agent runtime。

完整庫文件：[reflective-prompt-library/README.zh-TW.md](reflective-prompt-library/README.zh-TW.md)。

## 導覽（Orientation）

第一次接觸？建議依序閱讀：

1. `README.md` — 北極星：TeaPrompt 是什麼、不是什麼。
2. [reflective-prompt-library/README.zh-TW.md](reflective-prompt-library/README.zh-TW.md) — 各層與如何組合。
3. [reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md](reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md) — 快速選出 workflow skill。
4. [reflective-prompt-library/METHODOLOGY_MAP.md](reflective-prompt-library/METHODOLOGY_MAP.md) — 各層背後的原則。
5. [reflective-prompt-library/SKILL_INSTALLATION.md](reflective-prompt-library/SKILL_INSTALLATION.md) — 將 skills 安裝進你的 agent host。

維護者與治理操作者請改從 [reflective-prompt-library/06-repo/AGENTS.md](reflective-prompt-library/06-repo/AGENTS.md) 與 GLOSSARY 的 Governance Maintenance Playbook 開始。

## 治理與貢獻

- **貢獻指南：** [CONTRIBUTING.md](CONTRIBUTING.md)（英文）— 品質閘門、路由維護、`make all`
- **多視角共識紀錄：** [multi-agent-panel-consensus](reflective-prompt-library/plans/multi-agent-panel-consensus-2026-06-25.md)（六視角 Socratic 共識，Rounds 1–101）
- **維護手冊：** [GLOSSARY.md](reflective-prompt-library/GLOSSARY.md) — Governance Maintenance Playbook

此 repository 包含：

- `reflective-prompt-library/`：可重用的提示詞文件（思考、規劃、實作、審查、研究、風險、交接）。
- `reflective-prompt-library/skills/`：精簡的 `SKILL.md` 工作流包裝。
- `reflective-prompt-library/plans/`：決策紀錄、研究檔案、eval fixtures 與延後的自動化候選。
- `reflective-prompt-library/SKILL_INSTALLATION.md`：Claude / Codex / Cursor / Antigravity / OpenCode 安裝說明。
- `reflective-prompt-library/METHODOLOGY_MAP.md`：方法論分類與嚴格度分級地圖。
- `reflective-prompt-library/LANGUAGE_POLICY.md`：語言政策（操作層英文 + 本地化 prompt source）。
- `surveys/`：外部模型與工具的調查筆記，作為參考證據保存。

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
Workflow skill 觸發口訣請見 [Skill Trigger Cheatsheet（繁中）](reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md)。
方法論邊界請見 [Methodology Map](reflective-prompt-library/METHODOLOGY_MAP.md)。
語言規範請見 [Language Policy](reflective-prompt-library/LANGUAGE_POLICY.md)。

## 推薦入口

- 分流先用 `reflective-dispatch`
- 釐清目標、假設、範圍、驗收標準與可證偽性用 `reflective-brief`
- 寫規格用 `reflective-spec-plan`
- 實作用 `reflective-implement`
- 審查用 `reflective-review`
- 高風險先走 `reflective-risk`

## 設計理念

TeaPrompt 將 prompts 與 workflows 分離：

- **Prompts** 提供細膩的判斷框架與可重用的措辭。
- **Skills** 提供可重複的執行流程——它們是 prompt 層級的工作流程描述，由使用者的 agent runtime 解譯執行，而非多 agent 編排層。
- **Plans** 保存研究、決策紀錄與延後的自動化候選，避免把 archive notes 誤當成目前的操作規則。

工作流層刻意使用數量少、可組合的 broad skills，而不是每個 prompt 對應一個 skill。

## License

MIT，見 [LICENSE](LICENSE)。
