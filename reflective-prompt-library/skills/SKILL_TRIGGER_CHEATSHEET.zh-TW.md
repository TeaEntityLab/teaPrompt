Language: [English](SKILL_TRIGGER_CHEATSHEET.md) | 繁體中文

> **翻譯一致性說明**：本文件為繁體中文翻譯，可能與[英文版](SKILL_TRIGGER_CHEATSHEET.md)存在差異。完整、權威的內容請以英文版為準。翻譯管理見 [LANGUAGE_POLICY.md](../LANGUAGE_POLICY.md)。

# Skill 觸發口訣（速查版）

這份是 8 個 workflow skills 的一頁式選用指南。

分流公平性說明：
- 下面的觸發提示只是範例，不是必要措辭。
- 相近意圖即使措辭不同，也應該獲得相近的分流結果。
- 允許快速關鍵字分流，但不能因此對相近意圖靜默降低品質。

若任務包含外部內容、工具輸出、entity-like records 或有副作用的行動，請把 `04-agent/runtime-trust-boundary.md` 作為所選 skill 的輔助檢查鏡頭。

## `reflective-dispatch`

何時用：

- 先分流，不確定用 prompt 還是 workflow
- 任務混合規劃、實作、風險
- 任務包含外部資料、工具結果或行動權限問題

不要用在：

- 任務已明確只需單一 skill
- 只需最終執行，無需分流決策

## `reflective-brief`

何時用：

- 需求模糊，需要先定義 goal/scope/acceptance

不要用在：

- 已有完整 spec 且可直接執行
- 任務僅為快速事實查詢

## `reflective-spec-plan`

何時用：

- 需要 spec、usage-first、task slicing
- 需要規劃工具 gate、權限邊界或副作用

不要用在：

- DoR 不足（先回 `reflective-brief`）
- 僅是批判現有 plan → 用 `reflective-review`

## `reflective-implement`

何時用：

- 要實作、除錯、重構並驗證

不要用在：

- 高風險尚未過 gate（先 `reflective-risk`）
- 需求仍然不明確 → 先走 `reflective-brief` 或 `reflective-spec-plan`

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
4. `reflective-implement`
5. `reflective-review`
6. `reflective-handoff-retro`

不確定且低風險時：
- 優先選擇可見的向上分流（default-up），而不是靜默降級。
- 主動提示可加入的強化環節，例如測試、安全審查、效能檢查。
