Language: [English](METHODOLOGY_MAP.md) | 繁體中文

# 方法論地圖

## 核心結論

TeaPrompt 不應將所有方法整合為單一的 Master Prompt。核心架構應為 **反饋閘門工程工作流 (Feedback-Gated Engineering Workflow)**，而非單一龐大的「反思型工程智能體 (Reflective Engineering Agent)」。

正確的模式是：

```text
分類任務
-> 選擇嚴格度層次
-> 組合最小可用的 Prompt 或工作流
-> 透過品質閘門 (Quality Gates) 用證據進行驗收
```

本專案是一個結構化的方法、上下文組件和可組合工作流技能的基底 (substrate)，而非單一的超大指令集。

## 定位：技能即自然語言 Harness 政策

2026 年的智能體（Agent）文獻為本函式庫提供了精確的外部定位框架。依當前用法（術語仍有爭議——參見 ICLR 2026 後的術語論辯）：

- **Harness（執行框架）** — 圍繞模型的執行層：呼叫模型、執行工具、決定何時停止。*Agent = Model + Harness。*
- **Scaffold（鷹架）** — Harness 內部定義行為的層：提示詞、工具描述、上下文管理。
- **Skills（技能）** — 外部化的程序性專業知識，按需載入。

依此詞彙，`skills/` 層即為**自然語言 Harness 政策**：以可編輯文件描述執行期行為，由執行環境（Claude Code、Codex 等）解讀，而非硬編碼於程式中——此模式已被正式化為 Natural-Language Agent Harnesses（arXiv [2603.25723](https://arxiv.org/abs/2603.25723)）。本函式庫更廣泛的押注——能力外移至記憶、技能與 Harness，而非模型權重——符合外部化綜述（arXiv [2604.08224](https://arxiv.org/abs/2604.08224)）所描述的 Weights → Context → Harness 演進；另見 [HuggingFace agent glossary](https://huggingface.co/blog/agent-glossary)。長時程技能中的 State Ledger / Sufficiency Gate / Budget Rule 章節，應用了 Harness-1（arXiv [2606.02373](https://arxiv.org/abs/2606.02373)）的狀態外部化 Harness 設計；理由詳見 `plans/harness-1-state-ledger-research.md`。

NLAH 論文（明確引用 `SKILL.md` 類型檔案作為直接靈感來源）提煉出五項撰寫 Harness 政策文件的設計原則，本函式庫的技能契約應持續遵循：

1. **先寫任務契約（task contract）** — 輸入、輸出、允許的工具，以及任務完成的判定條件。
2. **將階段與機制分離** — 為各階段命名；確切操作交由腳本或工具執行。
3. **讓狀態與證據顯式化** — 明確說明狀態存放位置，以及後續步驟必須重新開啟哪些工件。
4. **為可消融性劃定模組邊界** — 為每個模組命名，使其可被乾淨地移除或測試。
5. **使用簡單且可執行的語言** — *「『小心一點』、『深入思考』、『像專家一樣』這類措辭是薄弱的 Harness 政策，因為它們沒有定義可觀察的行為。」*

外部化綜述補充了任何記憶／帳本（ledger）工件的成功判準：不是「我們存了多少？」，而是**「我們是否讓當前的決策變得清晰可判？」**

## 十層方法論分類法 (10-Layer Taxonomy)

本方法論正式劃分為以下十個層級：

1. **核心指令層 (Core Instruction Layer)** (`00-core/`): 全域自定義指令、系統行為與基礎設定。
2. **推理與思考層 (Reasoning / Thinking Layer)** (`01-thinking/`): 核心認知框架，包含蘇格拉底式引導、批判性分析與假設審計。
3. **工程與執行層 (Engineering / Execution Layer)** (`02-engineering/`): 特定領域的工程程序 (TDD、規格撰寫、實作策略)。
4. **上下文窗口層 (Context Window Layer)** (`03-context/`): 上下文窗口大小、Token 管理與上下文交接提示詞。
5. **工作流與智能體層 (Workflow & Agentic Layer)** (`04-agent/`): 工作流引擎、配方 (Review-Rating-Fix) 與記憶/知識整合提示詞。
6. **領域套件層 (Domain Pack Layer)** (`05-domain/`): 專用策略與執行覆蓋層 (例如商業策略、教育與認知教練)。
7. **專案模板層 (Repository Template Layer)** (`06-repo/`): 本地專案指令與規則模板 (例如 `AGENTS.md`, `cursor-rules.md`)。
8. **技能與動作層 (Skill / Action Layer)** (`skills/`): 模組化、隨需載入的 `SKILL.md` 程序，在觸發時執行。
9. **品質閘門與驗證層 (Quality Gate / Verification Layer)** (Evals/Review): 健全的反饋循環、驗收清單以及評分/回歸防禦機制。
10. **治理與能力風險層 (Governance / Capability Risk Layer)** (Risk/Compliance): 安全邊界、非公開政策、高風險審查閘門以及憑證與工具保護。

## 嚴格度分級

| 等級 | 適用場景 | 主要表面 (Main Surface) |
| --- | --- | --- |
| 1. 日常低風險 prompt | 低風險、簡短回答、無狀態 | `00-core/daily-minimal.md` |
| 2. 反思型分析 | 複雜推理或決策 | `reflective-brief` |
| 3. 工程任務 | 代碼、系統設計、數據流、測試 | `reflective-spec-plan` -> `reflective-implement` |
| 4. 高風險審查 | 安全、隱私、金流、刪除、生產環境 | `reflective-risk` |
| 5. 智能體工作流 | 長時間運行、多工具、可恢復的工作 | `reflective-dispatch` + 工作流計畫 |
| 6. 策略覆蓋層 | 商業、教育、組織、長期系統 | `05-domain/` prompts 作為覆蓋層 |

## 該合併與不該合併

### 工程反思 + Why / What / How / Done

這些在執行流程中屬於同一個部分。

- **Why**: 目標、用戶價值、選錯問題的代價。
- **What**: 範疇、輸入、輸出、驗收標準。
- **How**: 選項、風險、測試、回滾。
- **Done**: 證據、驗收、殘留風險。

### 蘇格拉底審查 + 高風險審查

僅在風險足夠高時，才啟用較重的批判性思考。

- 假設審計
- 證據檢查
- 反方論點
- 謬誤掃描
- 可證偽性
- 人工審查閘門

### 純 Prompt + 評分規準 / 檢查清單

這是日常使用的最佳模式。

- 目標
- 假設
- 分類
- 策略
- 風險
- 驗收標準

## 不該強行合併的模組

### 學習科學不等於工程工作流

教育與認知概念可以啟發 Prompt 設計，但不應成為工程智能體的預設流程。將它們保留於學習系統、語言練習、反饋循環和認知負載控制中。

### 商業策略不是 Prompt 核心

商業框架有助於定義 Why，但不應注入到每個任務中。僅在任務涉及產品、市場、組織或轉型策略時使用。

### 多智能體工作流不是單一 Prompt

多智能體任務需要狀態、工具、日誌、驗證和交接產出。Prompt 可以描述模式，但無法取代運行時 (runtime)。

## Repo 整合檢查

| 分類 / 層級 | 目前 Repo 整合度 | 狀態 | 待辦動作 |
| --- | --- | --- | --- |
| 核心指令層 | 契合 | 完成 | 維持最小化基礎腳印。 |
| 推理與思考層 | 契合 | 完成 | 保留 `01-thinking/` 底下的 prompt。 |
| 工程與執行層 | 契合 | 完成 | 保留 `02-engineering/` 底下的 prompt。 |
| 上下文窗口層 | 契合 | 完成 | 管理窗口大小與 Token 配置 (`03-context/`)。 |
| 工作流與智能體層 | 契合 | 完成 | 工作流引擎、計畫與記憶整合 (`04-agent/`)。 |
| 領域套件層 | 契合 | 完成 | 保留策略提示詞於 `05-domain/`。 |
| 專案模板層 | 契合 | 完成 | 維持 `AGENTS.md` 和 `cursor-rules.md` 模板於 `06-repo/`。 |
| 技能與動作層 | 契合 | 擴充 | 維持 9 個凍結 workflow skills（含 reflective-minimality gate）以處理反膨脹決策。 |
| 品質閘門與驗證 | 契合 | 完成 | 標準化技能層級的品質檢查。 |
| 治理與能力風險 | 契合 | 完成 | 使用 `reflective-risk` 處理高風險邊界。 |
