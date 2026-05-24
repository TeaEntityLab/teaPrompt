# Counterargument Architect Prompt

Use this to prevent excessive optimism, overengineering, or AI flattery.

```markdown
請扮演最嚴格但公平的反方架構師，攻擊我的方案。

## 我的方案
{貼上方案}

請從以下角度反駁：

1. 這是不是解錯問題？
2. 是否把症狀誤認為根因？
3. 是否有更低成本解？
4. 是否過度工程？
5. 是否低估維護成本？
6. 是否低估人類審查成本？
7. 是否依賴不可靠假設？
8. 是否忽略安全、隱私、權限、資料遺失？
9. 是否會造成未來技術債？
10. 哪些地方只是聽起來先進？

請輸出：

- Fatal flaws：致命缺陷
- Major concerns：重大疑慮
- Minor concerns：次要疑慮
- Better alternatives：更好替代方案
- Minimum viable version：最小可行版本
- Kill criteria：什麼情況應該停止
```

