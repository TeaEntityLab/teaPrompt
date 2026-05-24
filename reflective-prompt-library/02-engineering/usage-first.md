# Usage-first Prompt

Use this to avoid specs that look good but are awkward in practice.

```markdown
請假設這個系統已經完成，先不要寫實作，請先寫使用手冊。

## 系統 / 功能
{貼上功能描述}

請輸出：

1. 這個功能給誰用？
2. 使用者最常見的 5 個場景
3. CLI / API / UI 使用方式
4. Input examples
5. Output examples
6. Error examples
7. 成功案例
8. 失敗案例
9. 常見誤用
10. 使用者會覺得困惑的地方
11. 這份使用手冊反推出來的設計問題
12. 建議修改的 spec

請特別檢查：
- 參數是否太難懂
- 操作是否太多步
- 錯誤訊息是否可行動
- 是否有不必要功能
- 是否能成為 test cases
```

