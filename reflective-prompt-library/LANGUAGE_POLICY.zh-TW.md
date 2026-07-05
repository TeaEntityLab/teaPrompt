Language: [English](LANGUAGE_POLICY.md) | 繁體中文

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

## 本地化邊界 (2026-06-25)

- `skills/*/SKILL.md` 契約與 governance plans 以英文為 canonical。
- 繁體中文支援 navigation（`README.zh-TW.md`）、分流速查（`SKILL_TRIGGER_CHEATSHEET.zh-TW.md`）與 glossary routing lines，不取代完整 skill contract。
- Prompt source files under `00-core/`–`05-domain/` 可保留本地化內容，前提是語言版本與相對連結清楚。
- Operational test：TW adopter 可透過 cheatsheet + glossary 分流 L1–L2 任務；更深的 skill contract 載入英文。
- ROUTE-002 的繁中 holdout phrases 測試 intent-normalization fairness，不代表 full `SKILL.md` 翻譯。
