# Gemini Long Document Prompt

Use this when processing long documents. It is especially suited for Gemini-style large-context workflows.

```markdown
你將處理長文件。請不要直接摘要全文，而是先建立結構索引。

任務：
{任務}

文件：
{貼上長文件}

請輸出：

## 1. Document Map
列出文件主要區塊與用途。

## 2. Relevant Sections
哪些區塊與任務最相關？

## 3. Key Claims
列出主要主張。

## 4. Evidence
列出支持證據。

## 5. Contradictions
找出矛盾或張力。

## 6. Missing Information
缺少什麼？

## 7. Synthesis
根據任務整合答案。

## 8. Actionable Output
給出可直接使用的結論、表格或計畫。

請不要把長文件逐段重複。
```

