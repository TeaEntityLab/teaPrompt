Language: [English](SKILL_INSTALLATION.md) | 繁體中文

> **⚠️ 範圍說明**：本文件是繁體中文**精簡版安裝指引**，不是英文版的逐句翻譯。**可執行的安裝作法只有一種**：先載入[英文版](SKILL_INSTALLATION.md#install-helpers)的 helper 定義，再依本文件各平台的目的地呼叫 helper。本文件不維護第二套複製作法；**完整的安全性注意事項、疑難排解檢查清單及平台對應細節請務必參閱英文版**，以確保安全安裝。翻譯管理見 [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md)。

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

**Harness policy：** 九個凍結 workflow skills，採嚴謹度優先分流。見 [06-repo/AGENTS.md](06-repo/AGENTS.md#harness-policy-nine-skills) 與 [skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md](skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md)。

**Domain packs 與觸發模式：** 十個 domain packs（`flow-control-generator`、`flow-loop-harness`、`agent-governance-scaffold`、`governed-delivery`、`verification-map-generator`、`headless-agent-cli-contract`、`arm-blinded-eval-harness`、`acceptance-join-validator`、`golden-benchmark-runner`、`router-trace-linter`）是 host 直接呼叫的選配 contracts，不屬於九技能核心分流。若 host 支援使用者手動觸發模式（例如 Claude Code 的 `disable-model-invocation: true`），可將 domain packs 以該模式安裝，減少常駐 context 負擔；請在安裝副本上設定，倉庫內的 `SKILL.md` frontmatter 保持跨平台通用。九個核心 skills 維持可被模型自動觸發，以保留 `reflective-dispatch` 的分流語意。

每個平台都需要：

```text
<skills-root>/<skill-name>/SKILL.md
```

請安裝整個 skill 目錄，不要只複製 `SKILL.md`。兩個 flow packs、
`arm-blinded-eval-harness`、`router-trace-linter` 與 `governed-delivery` 的
`TEMPLATES.md`，以及 `agent-governance-scaffold` 與 `governed-delivery` 的
`ARTIFACTS.md`，都是套件的一部分；主合約會說明何時載入。
英文版 copy／symlink helpers 已保留整個目錄，複製後不需要 TeaPrompt 原始碼
目錄即可讀取或實例化參考內容。若 host 不支援 skills 自動探索，除了貼上主合約，
也須依選用分支貼上相應的範本或物件內容。

範例檔屬於輔助說明面，建議一併放在：

```text
<skills-root>/examples/<skill-name>.examples.md
```

## 開始之前

前置需求：POSIX `sh`，以及 `cp` 與 `ln`。以下每個 shell 都要做一次：

1. 切到 TeaPrompt 倉庫根目錄。
2. 從[英文版 Install helpers](SKILL_INSTALLATION.md#install-helpers) 複製六個 helper 定義，貼到目前的 shell 執行。
3. 再執行下方各平台的 helper 呼叫。Helper 只會安裝含有 `SKILL.md` 的目錄。

> 不要用手寫的 `mkdir -p <目的地>` 加 `cp -R reflective-prompt-library/skills/reflective-* <目的地>/` 取代 helper。那組指令在來源不完整（例如 `reflective-*` 目錄存在但沒有 `SKILL.md`）時仍會回傳 0，讓你誤以為安裝成功；helper 會在建立目的地之前先檢查，來源不合要求就回傳非零並拒絕安裝。

失敗時一律是非零結束碼且不算安裝成功：來源目錄缺失、來源內沒有預期的核心 skills、缺少 pack skill，或缺少範例目錄，都會在視為安裝完成之前失敗。核心 helper 會先檢查預期的 skills，才建立目的地，因此錯誤的來源不會留下空的安裝結果。`cp -R` 與 `ln -sfn` 的失敗也會向外傳遞，不受呼叫端 `errexit` 設定影響。Symlink helper 若遇到已存在的非連結 skill 目錄會拒絕覆寫並保留原檔；如需從手動複製改為連結安裝，請由擁有者自行備份本地修改並搬移該目錄後再重跑 helper（helper 不會刪除非連結目的地）。

## Claude Code

- 專案層：`.claude/skills/<skill-name>/SKILL.md`
- 個人層：`~/.claude/skills/<skill-name>/SKILL.md`

專案安裝（複製）：

```bash
install_core_skills_copy .claude/skills
```

專案安裝（連結）：

```bash
install_core_skills_symlink .claude/skills
```

個人安裝（複製）：

```bash
install_core_skills_copy "$HOME/.claude/skills"
```

個人安裝（連結）：

```bash
install_core_skills_symlink "$HOME/.claude/skills"
```

驗證：

```bash
find .claude/skills -maxdepth 2 -name SKILL.md -print
```

若在 session 開始後才建立 `.claude/skills`，請重啟 Claude Code。

## Codex

- 個人層（預設）：`~/.codex/skills/<skill-name>/SKILL.md`
- 共享專案層（兼容路徑）：`.agents/skills/<skill-name>/SKILL.md`

個人安裝（複製）：

```bash
install_core_skills_copy "${CODEX_HOME:-$HOME/.codex}/skills"
```

個人安裝（連結）：

```bash
install_core_skills_symlink "${CODEX_HOME:-$HOME/.codex}/skills"
```

驗證：

```bash
find "${CODEX_HOME:-$HOME/.codex}/skills" -maxdepth 2 -name SKILL.md -print
```

安裝後請重啟 Codex，讓它讀到新的 skills。

共享專案安裝（複製）：

```bash
install_core_skills_copy .agents/skills
```

共享專案安裝（連結）：

```bash
install_core_skills_symlink .agents/skills
```

全域共享安裝（所有支援 `.agents/skills` 的 host 通用）：

```bash
install_core_skills_copy "$HOME/.agents/skills"
# 或
install_core_skills_symlink "$HOME/.agents/skills"
```

## Cursor

建議優先使用：

- `.agents/skills/`（若你的 Cursor 版本支援 Agent Skills）

共享專案安裝（複製）：

```bash
install_core_skills_copy .agents/skills
```

共享專案安裝（連結）：

```bash
install_core_skills_symlink .agents/skills
```

Cursor 專用專案路徑（若你的版本支援）：

```bash
install_core_skills_copy .cursor/skills
# 或
install_core_skills_symlink .cursor/skills
```

驗證：

```bash
find .agents/skills .cursor/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null
```

然後重新開啟專案或重啟 Cursor，並在可用的 Agent／skills UI 確認。

若未支援 SKILL 自動載入，請用 Cursor Rules fallback（參考英文版完整模板）。

## Antigravity CLI / IDE

本指南於 2026-09-05 移除 Gemini CLI 章節。[Google 官方公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)確認，免費與 Google AI Pro／Ultra 使用者改用 Antigravity CLI；企業授權與付費 API 的 Gemini CLI 存取仍受支援，不能解讀成所有 Gemini CLI 都已退役。

依 [Antigravity 技能文件](https://antigravity.google/docs/skills)於 2026-10-01 核對的路徑：

- Workspace（CLI／Antigravity 2.0／IDE）：`.agents/skills/<skill-name>/SKILL.md`
- Global（CLI）：`~/.gemini/antigravity-cli/skills/<skill-name>/SKILL.md`
- Global（Antigravity 2.0／IDE）：`~/.gemini/config/skills/<skill-name>/SKILL.md`
- 舊版 global（僅 IDE 支援）：`~/.gemini/antigravity/skills/<skill-name>/SKILL.md`

Workspace 安裝（複製）：

```bash
install_core_skills_copy .agents/skills
```

Workspace 安裝（連結）：

```bash
install_core_skills_symlink .agents/skills
```

CLI 的 global 安裝：

```bash
install_core_skills_copy "$HOME/.gemini/antigravity-cli/skills"
# 或
install_core_skills_symlink "$HOME/.gemini/antigravity-cli/skills"
```

Antigravity 2.0／IDE 的 global 安裝：

```bash
install_core_skills_copy "$HOME/.gemini/config/skills"
# 或
install_core_skills_symlink "$HOME/.gemini/config/skills"
```

驗證：

```bash
find .agents/skills "$HOME/.gemini/antigravity-cli/skills" "$HOME/.gemini/config/skills" "$HOME/.gemini/antigravity/skills" -maxdepth 2 -name SKILL.md -print 2>/dev/null
```

CLI 可用自動產生的 `/<skill-name>` 指令呼叫技能；獨立 IDE 可在 agent 側邊面板的 **Customizations** 檢視技能。以上是官方文件核對，不是本輪新的 host 載入驗證；2026-09-05 的 `agy` 1.1.27 與舊路徑觀察仍屬歷史證據。

## OpenCode

可用路徑：

- `.opencode/skills/`
- `~/.config/opencode/skills/`
- `.agents/skills/`（共享）
- `.claude/skills/`（兼容）

專案安裝（複製）：

```bash
install_core_skills_copy .opencode/skills
```

專案安裝（連結）：

```bash
install_core_skills_symlink .opencode/skills
```

全域安裝（複製）：

```bash
install_core_skills_copy "$HOME/.config/opencode/skills"
```

全域安裝（連結）：

```bash
install_core_skills_symlink "$HOME/.config/opencode/skills"
```

共享專案安裝：

```bash
install_core_skills_copy .agents/skills
# 或
install_core_skills_symlink .agents/skills
```

OpenCode 也讀取 Claude 兼容路徑。若依賴該探索模式：

```bash
install_core_skills_symlink .claude/skills
```

驗證：

```bash
find .opencode/skills ~/.config/opencode/skills .agents/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null
```

## 選配：domain packs 與範例檔

預設只安裝九個核心 skills。需要 host 直接呼叫的產生器 packs（flow scripts、loop harnesses、governance scaffolding、verification maps）時，才用同一個目的地加裝：

```bash
install_domain_packs_copy <目的地>
# 或
install_domain_packs_symlink <目的地>
```

需要範例檔時：

```bash
install_skill_examples_copy <目的地>
# 或
install_skill_examples_symlink <目的地>
```

安裝後的範例檔位於 `<目的地>/examples/<skill-name>.examples.md`。

## 快速驗證

已安裝的目的地應符合 `<skills-root>/<skill-name>/SKILL.md` 的形狀。列出實際安裝的 skills：

```bash
find <目的地> -maxdepth 2 -name SKILL.md -print
```

例如專案層 `.agents/skills`：

```bash
find .agents/skills -maxdepth 2 -name SKILL.md -print
```

若有安裝範例檔，可另外檢查：

```bash
find <目的地> -maxdepth 2 -path '*/examples/*.examples.md' -print
```

## 安全性注意事項

- 第三方 skills 應視為可執行的操作指令，而非被動文件。
- 安裝前請務必閱讀 `SKILL.md` 內容。
- 避免大規模全域安裝，建議使用專案層級的少量 skill 集合。
- 除非 skill 確實需要，否則不要授予工具權限或 hook。
- 高風險工作流程請保留在 `reflective-risk` 之後再執行。
- `reflective-risk`、`flow-loop-harness`、`agent-governance-scaffold`、`governed-delivery`、`headless-agent-cli-contract`、`arm-blinded-eval-harness` 與 `golden-benchmark-runner` 的
  metadata 都設為 `human_review_required: true`；這只是意圖宣告，不會自行建立
  host 的核准關卡。限制 Skill 自動呼叫只控制觸發方式，不等於逐次動作授權或
  結果驗收；手動呼叫 Skill 也不代表核准其中所有動作。仍須另外設定 host 的
  動作權限與必要的人工檢查點，並檢視證據後才驗收。TeaPrompt 本身不會強制執行。
- `examples/*.examples.md` 只示範輸入/輸出形狀與證據層級，不代表已實際執行、已核准，或 host 已完成強制執行。

## 注意事項

- 高風險任務先走 `reflective-risk`
- 不要一次全域安裝大量第三方 skills
- 若新建 skills 根目錄後看不到，重啟對應工具

完整來源、平台差異與疑難排解請看英文完整版：
[SKILL_INSTALLATION.md](SKILL_INSTALLATION.md)
