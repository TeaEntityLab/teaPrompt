Language: [English](SKILL_INSTALLATION.md) | 繁體中文

> **⚠️ 翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](SKILL_INSTALLATION.md)存在差異。**完整的安全性注意事項、疑難排解檢查清單及平台對應細節請務必參閱英文版**，以確保安全安裝。翻譯管理見 [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md)。

# Skills 安裝指南

最後確認日期：2026-07-06

本文件說明如何把 TeaPrompt 的 workflow skills 安裝到：

- Claude Code
- Codex
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

## 安全性注意事項

- 第三方 skills 應視為可執行的操作指令，而非被動文件。
- 安裝前請務必閱讀 `SKILL.md` 內容。
- 避免大規模全域安裝，建議使用專案層級的少量 skill 集合。
- 除非 skill 確實需要，否則不要授予工具權限或 hook。
- 高風險工作流程請保留在 `reflective-risk` 之後再執行。

## 注意事項

- 高風險任務先走 `reflective-risk`
- 不要一次全域安裝大量第三方 skills
- 若新建 skills 根目錄後看不到，重啟對應工具

完整來源、平台差異與疑難排解請看英文完整版：
[SKILL_INSTALLATION.md](SKILL_INSTALLATION.md)
