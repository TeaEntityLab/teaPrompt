Language: [English](README.md) | 繁體中文

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

## 推薦入口

- 分流先用 `reflective-dispatch`
- 任務定義用 `reflective-brief`
- 寫規格用 `reflective-spec-plan`
- 實作用 `reflective-implement`
- 審查用 `reflective-review`
- 高風險先走 `reflective-risk`

## License

MIT，見 [LICENSE](LICENSE)。
