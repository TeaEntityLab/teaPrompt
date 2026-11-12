Language: [English](LANGUAGE_POLICY.md) | 繁體中文

> **範圍說明**：本文件是繁體中文**精簡版語言政策**，不是英文版的逐句翻譯。英文版是 canonical；本文件只說明一個臺灣採用者需要知道的邊界：哪些有繁中版、哪些維持英文，以及安裝時可執行的唯一作法。翻譯管理見英文版 [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md)。

# 語言政策

## 目前狀態

本 repo 目前不是全英文，採雙層語言策略：

1. 操作層英文：
   - README、安裝說明、skills、plans、metadata
2. Prompt source 可本地化：
   - `00-core/` 到 `05-domain/` 可保留原語言內容

## 政策決策

以下內容使用英文作為 canonical：

- 導航與安裝文件
- `skills/*/SKILL.md`
- 規劃與研究說明
- 檔名與 metadata（`name`、`description`、`license`）

本地化 prompt 內容允許使用其他語言，前提是：

- 在文件中清楚標示語言版本
- 與英文操作層互相連結

## 已出貨的繁中輔助面（精簡版）

繁中版的定位是**導航與分流輔助**，不是完整契約翻譯：

| 繁中面 | 範圍 | 維護承諾 |
| --- | --- | --- |
| `README.zh-TW.md`（根目錄與函式庫） | 北極星、導覽順序、目錄說明 | 跟著英文版的結構走，省略長表格與詳細論證 |
| `SKILL_TRIGGER_CHEATSHEET.zh-TW.md` | 分流口訣與誤用提醒 | 跟著英文版的路由語意走，不翻譯完整 skill 契約 |
| `SKILL_INSTALLATION.zh-TW.md` | 各平台目的地與 helper 呼叫 | **沒有自己的複製實作**：可執行的 helper 定義只在英文版，繁中版只給呼叫方式 |
| `METHODOLOGY_MAP.zh-TW.md` | 核心結論、十層分類、嚴謹度分級 | 省略英文版後期的 runtime／provenance／SOP addenda，見下方的邊界說明 |

## 本地化邊界 (2026-06-25)

- `skills/*/SKILL.md` 契約與 governance plans 以英文為 canonical。
- 繁體中文支援 navigation（`README.zh-TW.md`）、分流速查（`SKILL_TRIGGER_CHEATSHEET.zh-TW.md`）與 glossary routing lines，不取代完整 skill contract。
- Prompt source files under `00-core/`–`05-domain/` 可保留本地化內容，前提是語言版本與相對連結清楚。
- Operational test：TW adopter 可透過 cheatsheet + glossary 分流 L1–L2 任務；更深的 skill contract 載入英文。
- ROUTE-002 的繁中 holdout phrases 測試 intent-normalization fairness，不代表 full `SKILL.md` 翻譯。

## 方法論繁中版的邊界

`METHODOLOGY_MAP.zh-TW.md` 是**精簡版**：它保留核心結論、治理面板紀錄、十層分類法、嚴謹度分級與 repo 整合檢查，但**沒有翻譯**英文版的以下 addenda：

- Runtime Trust Boundary 的外部引用論證（OpenAI Model Spec、MCP、Apple）
- Durable Agent Runtime 的三契約參考邊界
- Scaffold Provenance 的來源區分
- SOP Compiler、Artifact Promotion／Workflow Acquisition、Project-Knowledge 的規劃視角

需要這些 addenda 時請讀英文版 [METHODOLOGY_MAP.md](METHODOLOGY_MAP.md)；繁中版不會另行翻譯。

## 核心／Domain-pack 邊界

繁中導航面沿用同一條邊界：**九個 `reflective-*` workflow skills 是核心分流集合**，`reflective-dispatch` 只在其中選路；**十個已註冊 domain packs 是 host 直接呼叫的選配 contracts**，不進核心路由。安裝時預設只裝九個核心 skills；需要 packs 時才用同一個目的地加裝（見 [SKILL_INSTALLATION.zh-TW.md](SKILL_INSTALLATION.zh-TW.md)的「選配」一節）。分流時的完整路由表以英文 [skills/skill-map.md](skills/skill-map.md) 為準。

## 命名建議

- 預設英文檔名
- 多語版本加後綴：
  - `xxx.en.md`
  - `xxx.zh-TW.md`

## 未來若要全英文

1. 將本地化 prompt 移入 `locales/zh-TW/`
2. 保留英文 canonical 版本
3. 建立翻譯一致性檢查清單

## 驗收標準

- 操作層文件皆有英文版本
- 本地化版本有語言標註與相對路徑連結
- skill 層維持英文主體
- 貢獻者可快速判斷哪些是執行層、哪些是內容層
