Language: [English](SKILL_INSTALLATION.md) | 繁體中文

> **⚠️ 翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](SKILL_INSTALLATION.md)存在差異。**完整的安全性注意事項、疑難排解檢查清單及平台對應細節請務必參閱英文版**，以確保安全安裝。翻譯管理見 [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md)。

# Skills 安裝指南

最後確認日期：2026-09-16

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

**Domain packs 與觸發模式：** 十個 domain packs（`flow-control-generator`、`flow-loop-harness`、`agent-governance-scaffold`、`governed-delivery`、`verification-map-generator`、`headless-agent-cli-contract`、`arm-blinded-eval-harness`、`acceptance-join-validator`、`golden-benchmark-runner`、`router-trace-linter`）是 host 直接呼叫的選配 contracts，不屬於九技能核心分流。若 host 支援使用者手動觸發模式（例如 Claude Code 的 `disable-model-invocation: true`），可將 domain packs 以該模式安裝，減少常駐 context 負擔；請在安裝副本上設定，倉庫內的 `SKILL.md` frontmatter 保持跨平台通用。九個核心 skills 維持可被模型自動觸發，以保留 `reflective-dispatch` 的分流語意。

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

## Cursor

建議優先使用：

- `.agents/skills/`（若你的 Cursor 版本支援 Agent Skills）

若未支援 SKILL 自動載入，請用 Cursor Rules fallback（參考英文版完整模板）。

## Antigravity CLI / IDE

本指南於 2026-09-05 移除 Gemini CLI 章節。[Google 官方公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)確認，免費與 Google AI Pro／Ultra 使用者改用 Antigravity CLI；企業授權與付費 API 的 Gemini CLI 存取仍受支援，不能解讀成所有 Gemini CLI 都已退役。

依 [Antigravity 技能文件](https://antigravity.google/docs/skills)於 2026-10-01 核對的路徑：

- Workspace（CLI／Antigravity 2.0／IDE）：`.agents/skills/<skill-name>/SKILL.md`
- Global（CLI）：`~/.gemini/antigravity-cli/skills/<skill-name>/SKILL.md`
- Global（Antigravity 2.0／IDE）：`~/.gemini/config/skills/<skill-name>/SKILL.md`
- 舊版 global（僅 IDE 支援）：`~/.gemini/antigravity/skills/<skill-name>/SKILL.md`

```bash
mkdir -p .agents/skills
cp -R reflective-prompt-library/skills/reflective-* .agents/skills/
```

CLI 的 global 安裝：

```bash
mkdir -p "$HOME/.gemini/antigravity-cli/skills"
cp -R reflective-prompt-library/skills/reflective-* "$HOME/.gemini/antigravity-cli/skills/"
```

Antigravity 2.0／IDE 的 global 安裝：

```bash
mkdir -p "$HOME/.gemini/config/skills"
cp -R reflective-prompt-library/skills/reflective-* "$HOME/.gemini/config/skills/"
```

CLI 可用自動產生的 `/<skill-name>` 指令呼叫技能；獨立 IDE 可在 agent 側邊面板的 **Customizations** 檢視技能。以上是官方文件核對，不是本輪新的 host 載入驗證；2026-09-05 的 `agy` 1.1.27 與舊路徑觀察仍屬歷史證據。

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
- `reflective-risk`、`flow-loop-harness`、`agent-governance-scaffold`、`governed-delivery`、`headless-agent-cli-contract`、`arm-blinded-eval-harness` 與 `golden-benchmark-runner` 的
  metadata 都設為 `human_review_required: true`；這只是意圖宣告，安裝後仍須由
  host 的呼叫控制實際執行 Human Review，TeaPrompt 本身不會強制執行。
- `examples/*.examples.md` 只示範輸入/輸出形狀與證據層級，不代表已實際執行、已核准，或 host 已完成強制執行。

## 注意事項

- 高風險任務先走 `reflective-risk`
- 不要一次全域安裝大量第三方 skills
- 若新建 skills 根目錄後看不到，重啟對應工具
- 英文版 helper 的失敗處理：來源解析、目的地建立或複製／連結任一步驟失敗時，helper 會回傳非零結束碼，不會回報安裝成功；來源缺失、來源內沒有預期的核心 skills、缺少 pack skill 或缺少範例目錄時，會在視為安裝完成之前失敗。核心 helper 會先檢查預期的 skills，才建立目的地，因此錯誤的來源不會留下空的安裝結果。`cp -R` 與 `ln -sfn` 的失敗也會向外傳遞，不受呼叫端 `errexit` 設定影響。
- 英文版 symlink helper 若遇到已存在的非連結 skill 目錄會拒絕覆寫並保留原檔；如需從手動複製改為連結安裝，請由擁有者自行備份本地修改並搬移該目錄後再重跑 helper（helper 不會刪除非連結目的地）

完整來源、平台差異與疑難排解請看英文完整版：
[SKILL_INSTALLATION.md](SKILL_INSTALLATION.md)
