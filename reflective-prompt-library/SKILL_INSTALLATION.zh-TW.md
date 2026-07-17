Language: [English](SKILL_INSTALLATION.md) | 繁體中文

> **⚠️ 翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](SKILL_INSTALLATION.md)存在差異。**完整的安全性注意事項、疑難排解檢查清單及平台對應細節請務必參閱英文版**，以確保安全安裝。翻譯管理見 [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md)。

# Skills 安裝指南

最後確認日期：2026-07-18

本文件說明如何把 TeaPrompt 的 workflow skills 安裝到：

- Claude Code
- Codex
- Gemini CLI
- Cursor
- Antigravity CLI / IDE
- OpenCode

Skill 原始位置：

```text
reflective-prompt-library/skills/
  reflective-brief/
  reflective-dispatch/
  reflective-handoff-retro/
  reflective-implement/
  reflective-minimality/    # gate skill — anti-bloat review, not a lifecycle workflow
  reflective-research/
  reflective-review/
  reflective-risk/
  reflective-spec-plan/
```

**Harness policy:** 九個凍結 workflow skills，採嚴謹度優先分流。見 [06-repo/AGENTS.md](06-repo/AGENTS.md#harness-policy-nine-skills) 與 [skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md](skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md)。

每個平台都需要：

```text
<skills-root>/<skill-name>/SKILL.md
```

範例檔屬於輔助說明面，建議一併放在：

```text
<skills-root>/examples/<skill-name>.examples.md
```

## Claude Code

- 專案層：`.claude/skills/<skill-name>/SKILL.md`
- 個人層：`~/.claude/skills/<skill-name>/SKILL.md`

```bash
mkdir -p .claude/skills
cp -R reflective-prompt-library/skills/reflective-* .claude/skills/
```

## Codex

- 個人層（預設）：`~/.codex/skills/<skill-name>/SKILL.md`
- 共享專案層（兼容路徑）：`.agents/skills/<skill-name>/SKILL.md`

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R reflective-prompt-library/skills/reflective-* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Gemini CLI

- 工作區層：`.gemini/skills/` 或 `.agents/skills/`（`.agents/skills` 優先）
- 使用者層：`~/.gemini/skills/` 或 `~/.agents/skills/`

```bash
gemini skills link "$(pwd)/reflective-prompt-library/skills/reflective-brief" --scope user
gemini skills list --all
```

啟用 skill 時會出現安全確認提示；免費層 Gemini CLI 將由 Antigravity CLI 取代（詳見英文版）。

## Cursor

建議優先使用：

- `.agents/skills/`（若你的 Cursor 版本支援 Agent Skills）

若未支援 SKILL 自動載入，請用 Cursor Rules fallback（參考英文版完整模板）。

## Antigravity CLI / IDE

- Workspace：`.agents/skills/<skill-name>/SKILL.md`
- Global：`~/.gemini/antigravity/skills/<skill-name>/SKILL.md`

```bash
mkdir -p .agents/skills
cp -R reflective-prompt-library/skills/reflective-* .agents/skills/
```

## OpenCode

可用路徑：

- `.opencode/skills/`
- `~/.config/opencode/skills/`
- `.agents/skills/`（共享）
- `.claude/skills/`（兼容）

```bash
mkdir -p .opencode/skills
cp -R reflective-prompt-library/skills/reflective-* .opencode/skills/
```

## 快速驗證

```bash
find . -path './.git' -prune -o -name SKILL.md -print | rg 'reflective-'
```

若有安裝範例檔，可另外檢查：

```bash
find . -path './.git' -prune -o -path '*/skills/examples/*.examples.md' -print
```

## 安全性注意事項

- 第三方 skills 應視為可執行的操作指令，而非被動文件。
- 安裝前請務必閱讀 `SKILL.md` 內容。
- 避免大規模全域安裝，建議使用專案層級的少量 skill 集合。
- 除非 skill 確實需要，否則不要授予工具權限或 hook。
- 高風險工作流程請保留在 `reflective-risk` 之後再執行。
- `reflective-risk`、`flow-loop-harness` 與 `agent-governance-scaffold` 的
  metadata 都設為 `human_review_required: true`；這只是意圖宣告，安裝後仍須由
  host 的呼叫控制實際執行 Human Review，TeaPrompt 本身不會強制執行。
- `examples/*.examples.md` 只示範輸入/輸出形狀與證據層級，不代表已實際執行、已核准，或 host 已完成強制執行。


## 注意事項

- 高風險任務先走 `reflective-risk`
- 不要一次全域安裝大量第三方 skills
- 若新建 skills 根目錄後看不到，重啟對應工具

完整來源、平台差異與疑難排解請看英文完整版：
[SKILL_INSTALLATION.md](SKILL_INSTALLATION.md)
