# Invest Wiki → 美股日报产业链热力：接入说明

**状态**：方案已跑通本地试运行，待工程化  
**公共实现方案**：[kol-daily/daily-briefing/docs/03-执行流程/美股-InvestWiki产业链热力+驱动解读-实现与同步方案.md](https://github.com/xifengxx/kol-daily/blob/gh-pages/daily-briefing/docs/03-执行流程/美股-InvestWiki产业链热力+驱动解读-实现与同步方案.md)  
**简报仓库**：[xifengxx/kol-daily](https://github.com/xifengxx/kol-daily)

## 1. Invest Wiki 的角色

Invest Wiki 是产业链热力的**内容源**，负责维护：

- 产业段定义；
- 公司与产业段的关系；
- 美股、ADR、日韩台港、欧洲、A股映射等 ticker；
- 私有 / 未上市公司的标注。

美股日报不应该直接抓本仓库的 GitHub Pages 网页；应该使用由 L2 markdown 编译出的结构化快照，或者在 kol-daily 侧进一步生成的 `chain_universe.json`。

## 2. 推荐同步路径

```text
L2 markdown
  → L3 wiki_data.json
  → chain_universe.json
  → 美股日报热力 JSON
  → 美股日报报告
```

如果只更新了网页或 L3 产物，而不更新 L2 markdown，那么下次重建时改动会丢。**长期方案必须回写 L2。**

## 3. 版本要求

每次 L2 更新后，建议生成一个新的 universe 快照，并至少记录：

```json
{
  "version": "YYYY-MM-DD.<n>",
  "built_at": "ISO8601",
  "source_commit": "GitHub commit SHA",
  "source_sha256": "前 12-16 位 hash",
  "logic_version": "universe 编译规则版本",
  "stats": {}
}
```

美股日报侧也应该在热力 JSON 和报告中记录所用 universe 的 `version`、`source_sha256`、`logic_version` 和目标交易日。

## 4. 默认回算规则

产业链图谱更新后：

- 老报告默认不回算；
- 新报告使用最新 universe；
- 如确需回算，生成新报告文件，例如 `YYYY-MM-DD-industry-chain-invest-wiki-uv2.md`，不能覆盖老报告。
