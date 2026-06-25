Language: [English](README.md) | 繁體中文

> **翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](README.md)存在差異。**英文版包含完整的 Recommended Defaults、Use Case Selection 表格及 Skills as Workflow 詳細說明**，請以英文版為完整參考。翻譯管理見 [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md)。

# Reflective Prompt Library

這個資料夾是 TeaPrompt 的主體，提供反思型工程提示詞與對應的 workflow skills。

核心原則：

```text
Doing the right thing > doing things right.
```

## 北極星（North Star）

TeaPrompt 幫助人類與宿主 agent 為任務選擇**恰當的嚴謹度**，記錄**決策理由**，並以**證據**驗證結果 —— 透過可組合的 prompt 層與九個 workflow skills 作為自然語言 harness policy，**不**自建 agent runtime。

## 嚴謹度優先於 Skills

先選 **Strictness L1–L6**（見 `skills/reflective-dispatch/SKILL.md`、[GLOSSARY.md](GLOSSARY.md)），再選 skill 階段。各 skill 的 frontmatter 含 `context_load: low|medium|high`，供成本敏感的宿主在 L1–L2 時延後高負載 skill。

## 目錄說明

- `00-core/`：核心人格與主控提示詞
- `01-thinking/`：蘇格拉底詰問、批判思考、可證偽
- `02-engineering/`：任務啟動、spec、task slicing、實作與測試
- `03-context/`：小中大 context 與 handoff
- `04-agent/`：agent 分級、workflow、retro、memory consolidation
- `05-domain/`：高風險、研究、商業、學習、寫作、創意
- `06-repo/`：AGENTS/Cursor/Codex/OpenCode 指令模板
- `skills/`：9 個可執行工作流 skill
- `skills/SKILL_TRIGGER_CHEATSHEET.md`：一頁式觸發口訣
- `skills/examples/`：每個 skill 的兩組 input/output 示例
- `plans/`：規劃與研究紀錄

## Skills as Workflow

提示檔是原始素材，`skills/` 目錄是操作層：一組可重複的工作流程，可複製到 `.claude/skills/`、`~/.codex/skills/`、`.agents/skills/` 或其他相容環境。

| 需求 | Skill |
| --- | --- |
| 分流任務到最小適用 workflow | `skills/reflective-dispatch/SKILL.md` |
| 釐清目標、假設、範圍、驗收、可證偽 | `skills/reflective-brief/SKILL.md` |
| 寫 spec、usage-first 設計、task slices、不寫程式碼的 Test Plan，或不寫 runtime code 的 agent workflow design | `skills/reflective-spec-plan/SKILL.md` |
| 實作程式碼，附驗證與可追蹤性 | `skills/reflective-implement/SKILL.md` |
| 實作前挑戰不必要 code、dependency、抽象層或 scope | `skills/reflective-minimality/SKILL.md` |
| 審查 code / plan / spec / AI output | `skills/reflective-review/SKILL.md` |
| 研究外部文件、DeepWiki、長篇文章 | `skills/reflective-research/SKILL.md` |
| 高風險任務執行前閘門 | `skills/reflective-risk/SKILL.md` |
| 交接、復盤、記憶沉澱 | `skills/reflective-handoff-retro/SKILL.md` |

設計上刻意避免一個 prompt 對應一個 skill。使用 prompt library 取得細膩判斷，使用 skills 取得執行框架。

> Skills 是 prompt 層級的工作流程包裝：由宿主 runtime（Claude Code、Codex、OpenCode 等）解譯執行的自然語言程序。它們不提供多 agent 執行時期、非同步訊息傳遞、或角色隔離。

## 延伸文件

- 安裝： [SKILL_INSTALLATION.zh-TW.md](SKILL_INSTALLATION.zh-TW.md)
- 方法論地圖： [METHODOLOGY_MAP.zh-TW.md](METHODOLOGY_MAP.zh-TW.md)
- 語言政策： [LANGUAGE_POLICY.zh-TW.md](LANGUAGE_POLICY.zh-TW.md)

## 使用建議

先看 [skills/skill-map.md](skills/skill-map.md) 選 workflow，再用 `skills/examples/` 找最接近的操作模板。
