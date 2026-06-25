Language: [English](SKILL_TRIGGER_CHEATSHEET.md) | 繁體中文

> **翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](SKILL_TRIGGER_CHEATSHEET.md)存在差異。完整、權威的內容請以英文版為準。翻譯管理見 [LANGUAGE_POLICY.md](../LANGUAGE_POLICY.md)。

# Skill 觸發口訣（速查版）

這份是 9 個 workflow skills 的一頁式選用指南。

> **輸出慣例**：精簡的交付規格應放在 Module Contract 的 `Output:` 欄位。僅當 skill 產生實質的輸出範本（例如 markdown 區塊、多欄位結構）時，才額外加入獨立的 `## Output` 區段。具有程序步驟（before/during/after）的 skill 通常不需要獨立的 Output 區段。

Skill 契約語言：
- 九個 `skills/*/SKILL.md` 以**英文**為權威；本繁中 cheatsheet 與 [GLOSSARY.md](../GLOSSARY.md) 供 L1–L2 分流與成本決策，不取代完整 skill 契約。

分流公平性說明：
- 各 skill frontmatter 含 `context_load: low|medium|high`，供成本敏感分流。
- 下面的觸發提示只是範例，不是必要措辭。
- 相近意圖即使措辭不同，也應該獲得相近的分流結果。
- 允許快速關鍵字分流，但不能因此對相近意圖靜默降低品質。
- ROUTE-002 含繁中 holdout 片語，驗證分流公平性；完整 skill 契約仍以英文 `SKILL.md` 為準。
- Strictness L1–L2 時可延後 `context_load: high` 的 skill（除非風險或明確需求）；延後項須寫入 route trace。

若任務包含外部內容、工具輸出、entity-like records 或有副作用的行動，請把 `04-agent/runtime-trust-boundary.md` 作為所選 skill 的輔助檢查鏡頭。


邊界速查（ROUTE-002 holdout）：
- **僅規劃不寫程式** → `reflective-spec-plan` — 工單、驗收標準或 rollout 計畫且明確不要改程式。
- **非正式環境審查** → `reflective-review` — 審查 PR/diff 可讀性或 regression，且明確排除正式環境風險評估。
- **已核准規格落地** → `reflective-implement` — 在 repository 實作或落地已核准 spec；不是僅規劃。

## `reflective-dispatch`

何時用：

- 先分流，不確定用 prompt 還是 workflow
- 任務混合規劃、實作、風險
- 任務包含外部資料、工具結果或行動權限問題

不要用在：

- 任務已明確只需單一 skill
- 只需最終執行，無需分流決策

L1 快速路徑：

- Strictness 為 L1 且任務瑣碎時，直接回答並附最小路由軌跡，不必另走 `reflective-brief`。

## `reflective-brief`

何時用：

- 需求模糊，需要先定義 goal/scope/acceptance

不要用在：

- 已有完整 spec 且可直接執行
- 任務僅為快速事實查詢

## `reflective-spec-plan`

何時用：

- 需要 spec、usage-first、task slicing
- 要從 spec 設計嚴謹 Test Plan，但不寫實作程式碼
- 需要規劃工具 gate、權限邊界或副作用
- 只設計可恢復 workflow、state model 或 orchestration plan，不寫 runtime code

不要用在：

- DoR 不足（先回 `reflective-brief`）
- 僅是批判現有 plan → 用 `reflective-review`
- 要新增可執行測試或修改程式碼 → 該階段用 `reflective-implement`

## `reflective-implement`

觸發提示：

- 「在 repo 實作這個變更。」
- 「在 repository 實作已核准 spec。」
- 「implement 已核准 spec in the repository。」
- 「用驗收標準與測試重構或除錯。」
- 「交付最小安全修補並附驗證。」

何時用：

- 要實作、除錯、重構並驗證

Minimality 訊號掃描（skill 內建）：

- 出現膨脹訊號（新 dependency、多餘檔案、新抽象層）時，編輯前先跑 skill 內 Minimality Signal Scan；爭議時升級到 `reflective-minimality`。

不要用在：

- 高風險尚未過 gate（先 `reflective-risk`）
- 需求仍然不明確 → 先走 `reflective-brief` 或 `reflective-spec-plan`

## `reflective-minimality`

何時用：

- 要避免過度設計、膨脹、樣板碼或不必要 dependency
- 要判斷是否可刪除、縮小、延後，或用 stdlib / native capability 解決
- 實作前需要 YAGNI / minimality / Ponytail-style gate
- 只想從 diff 裡找可刪的複雜度

不要用在：

- 需求仍不清楚（先 `reflective-brief` 或 `reflective-spec-plan`）
- 簡化可能移除 security / privacy / auth / data-loss prevention / accessibility / compatibility / explicit requirements
- 需要完整 correctness review（應搭配 `reflective-review`）

## `reflective-review`

何時用：

- 要 review code / plan / spec / AI output
- 要檢查外部內容是否被當成資料而不是指令
- 要判斷 prompt leak / mirror 是否可信、是否可移植

不要用在：

- 只是要產生第一版草稿
- 純實作且無審查要求

## `reflective-research`

何時用：

- 要做來源查證、DeepWiki 檢視、方法論盤點
- 要比較官方文件、第三方鏡像與社群分析
- 要研究目前 workflow framework 或 orchestration pattern
- 多視角戰略重思（使用 skill 內 Optional Method: Multi-Voice Panel）

不要用在：

- 完全 repo-local、不需要外部證據
- 僅為 dependency selection（應視為獨立評估流程）

## `reflective-risk`

何時用：

- auth / privacy / money / deletion / prod 等高風險
- 工具行動可能受到不可信或不完整資料影響

不要用在：

- 低風險可逆任務
- 試圖以此取代正常的實作規劃

## `reflective-handoff-retro`

何時用：

- 要交接、復盤、沉澱規則

不要用在：

- 還在進行中的實作主線
- 只需要程式碼審查結論

## 快速順序

1. `reflective-dispatch`
2. `reflective-risk`（若有高風險或副作用權限訊號）
3. `reflective-brief` / `reflective-spec-plan`
4. `reflective-minimality`（若有膨脹、dependency、抽象層或 scope creep 風險）
5. `reflective-implement`
6. `reflective-review`
7. `reflective-handoff-retro`

不確定且低風險時：
- 優先選擇可見的向上分流（default-up），而不是靜默降級。
- 主動提示可加入的強化環節，例如測試、安全審查、效能檢查。
