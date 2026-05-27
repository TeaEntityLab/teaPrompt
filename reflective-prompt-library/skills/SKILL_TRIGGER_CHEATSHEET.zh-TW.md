Language: [English](SKILL_TRIGGER_CHEATSHEET.md) | 繁體中文

# Skill 觸發口訣（速查版）

這份是 8 個 workflow skills 的一頁式選用指南。

## `reflective-dispatch`

何時用：

- 先分流，不確定用 prompt 還是 workflow
- 任務混合規劃、實作、風險

不要用在：

- 任務已明確只需單一 skill

## `reflective-brief`

何時用：

- 需求模糊，需要先定義 goal/scope/acceptance

不要用在：

- 已有完整 spec 且可直接執行

## `reflective-spec-plan`

何時用：

- 需要 spec、usage-first、task slicing

不要用在：

- DoR 不足（先回 `reflective-brief`）

## `reflective-implement`

何時用：

- 要實作、除錯、重構並驗證

不要用在：

- 高風險尚未過 gate（先 `reflective-risk`）

## `reflective-review`

何時用：

- 要 review code / plan / spec / AI output

不要用在：

- 只是要產生第一版草稿

## `reflective-research`

何時用：

- 要做來源查證、DeepWiki 檢視、方法論盤點

不要用在：

- 完全 repo-local、不需要外部證據

## `reflective-risk`

何時用：

- auth / privacy / money / deletion / prod 等高風險

不要用在：

- 低風險可逆任務

## `reflective-handoff-retro`

何時用：

- 要交接、復盤、沉澱規則

不要用在：

- 還在進行中的實作主線

## 快速順序

1. `reflective-dispatch`
2. `reflective-risk`（若有高風險訊號）
3. `reflective-brief` / `reflective-spec-plan`
4. `reflective-implement`
5. `reflective-review`
6. `reflective-handoff-retro`
