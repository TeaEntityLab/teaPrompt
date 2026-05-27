Language: [English](METHODOLOGY_MAP.md) | 繁體中文

# 方法論地圖

## 核心結論

不要把所有方法論壓成一條超大 Prompt。

正確做法是：

```text
先分類任務
-> 選擇嚴格度
-> 套用最小可用 workflow
-> 用證據驗收
```

## 主要方法家族

1. 工程規格：TDD/Spec/驗收/回歸防護
2. 閘門治理：Why/What/How/Done
3. 批判思考：假設、證據、反方、謬誤、可證偽
4. Prompting-only：低風險、短任務
5. Agent workflow：長任務、多工具、可恢復
6. 評估治理：guardrails、approval、audit
7. 教育認知：學習與認知負荷控制（覆蓋層）
8. 商業策略：產品/組織/轉型（覆蓋層）
9. 系統工具鏈：架構、自動化、可觀測性

## 嚴格度分級

1. L1：日常低風險 prompt
2. L2：反思型分析
3. L3：工程任務（spec -> implement）
4. L4：高風險 gate
5. L5：長任務 workflow
6. L6：策略/教育/商業覆蓋層

## 該合併與不該合併

可合併：

- Reflective Engineering + Why/What/How/Done
- Socratic/Critical thinking + High-risk review

不該硬合併：

- 教育認知模型 into 核心工程 workflow
- 商業轉型框架 into 每次執行 prompt
- Multi-agent runtime into 單一提示詞

## 對 Repo 的實作建議

- 維持 8 個 skill，不新增一堆方法論 skill
- 先強化分流與 gate，再談自動化
- 把高風險與審批流程寫成明確欄位
- 以分類為核心，不做大一統

詳細矩陣與完整英文版本請看：
[METHODOLOGY_MAP.md](METHODOLOGY_MAP.md)
