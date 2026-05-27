Language: [English](SKILL_INSTALLATION.md) | 繁體中文

# Skills 安裝指南

最後確認日期：2026-05-27

本文件說明如何把 TeaPrompt 的 workflow skills 安裝到：

- Claude Code
- Codex
- Cursor
- Antigravity CLI / IDE
- OpenCode

Skill 原始位置：

```text
reflective-prompt-library/skills/reflective-*/
```

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

## 注意事項

- 高風險任務先走 `reflective-risk`
- 不要一次全域安裝大量第三方 skills
- 若新建 skills 根目錄後看不到，重啟對應工具

完整來源與平台差異請看英文完整版：
[SKILL_INSTALLATION.md](SKILL_INSTALLATION.md)
