# 🔥 扣子（Coze）Skill 技能包合集

[![GitHub stars](https://img.shields.io/github/stars/bansheng-dotcom/linhuaxie?style=flat)](https://github.com/bansheng-dotcom/linhuaxie/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bansheng-dotcom/linhuaxie?style=flat)](https://github.com/bansheng-dotcom/linhuaxie/network) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> 🎯 零成本 AI 创收实践——在扣子平台上开发和上架可付费的 AI 技能包，实现日收入 100 元目标。

## 📦 已上架 Skill

| # | Skill 名称 | 类型 | 定价 | 简介 |
|:--:|------|------|:--:|------|
| 1 | [简历优化大师](./resume_optimizer（简历优化大师）/SKILL.md) | 提示词 + 工作流 | **9.9 元/次** | ATS关键词匹配 + STAR法则改写，提升面试邀约率 |
| 2 | [一句话PPT生成器](./ppt_generator（一句话PPT生成器）/SKILL.md) | 提示词型 | **19.9 元/次** | 一句话生成完整PPT大纲+逐页内容，10套行业模板 |
| 3 | [合同风险扫描仪](./contract_scanner（合同风险扫描仪）/SKILL.md) | 提示词 + 知识库 | **29.9 元/次** | 逐条扫描风险条款，红黄绿标注+法条依据+修改建议 |
| 4 | [小红书爆款文案生成器](./xiaohongshu_writer（小红书爆款文案生成器）/SKILL.md) | 提示词 + 联网搜索 | **9.9 元/次** | 5版标题+正文+标签+配图建议+发布策略 |
| 5 | [体检报告解读助手](./health_report_reader（体检报告解读助手）/SKILL.md) | 提示词 + 知识库 | **19.9 元/次** | 逐项解读指标含义，异常标注+就医/生活方式建议 |

## 🚀 快速使用

### 新手用户（直接安装使用）

1. 打开 [扣子技能商店](https://www.coze.cn/skills)
2. 搜索「简历优化大师」
3. 点击安装，即刻使用

### 开发者（导入本地 Skill 包）

```bash
# 进入对应 Skill 目录，打包为 .zip
cd resume_optimizer（简历优化大师）
zip -r resume_optimizer.skill *
```
# 在扣子编程中上传
# 打开 https://code.coze.cn → 技能 → 上传技能文件包
```

## 📁 目录结构

```
coze-skills/
├── README.md                          ← 项目说明书
├── .gitignore
├── resume_optimizer（简历优化大师）/          ← ① 简历优化大师
│   ├── SKILL.md
│   ├── references/
│   │   ├── ats_keywords.md
│   │   ├── self_eval_template.md
│   │   ├── star_examples.md
│   │   └── verb_thesaurus.md
│   ├── scripts/
│   │   └── keyword_matcher.py
│   └── assets/
│       └── store_listing.md
├── ppt_generator（一句话PPT生成器）/          ← ② 一句话PPT生成器
│   ├── SKILL.md
│   ├── references/
│   │   ├── chart_suggestions.md
│   │   ├── hook_phrases.md
│   │   └── templates.md
│   └── assets/
│       └── store_listing.md
├── contract_scanner（合同风险扫描仪）/        ← ③ 合同风险扫描仪
│   ├── SKILL.md
│   ├── references/
│   │   ├── legal_basics.md
│   │   └── risk_patterns.md
│   └── assets/
│       └── store_listing.md
├── xiaohongshu_writer（小红书爆款文案生成器）/ ← ④ 小红书爆款文案生成器
│   ├── SKILL.md
│   ├── references/
│   │   ├── niche_terms.md
│   │   └── title_formulas.md
│   └── assets/
│       └── store_listing.md
└── health_report_reader（体检报告解读助手）/   ← ⑤ 体检报告解读助手
    ├── SKILL.md
    ├── references/
    │   ├── indicator_guide.md
    │   └── normal_ranges.md
    └── assets/
        └── store_listing.md
```

## 💰 变现方式

这个仓库的所有 Skill 都可在 [扣子技能商店](https://www.coze.cn/skills) 上架收费：

- **分成比例**：你拿 70%，平台拿 30%（优质开发者可达 95%）
- **收款渠道**：支付宝 / 抖音支付
- **结算周期**：按月结算，可随时提现
- **资质要求**：个人开发者即可，无需营业执照

[查看完整变现流程指南 →](https://code.coze.cn/merchant-management)

## 🔧 部署到扣子

1. 下载对应 Skill 目录
2. 打包为 `.zip` 或 `.skill` 文件
3. 打开 [扣子编程](https://code.coze.cn) → 技能 → 上传技能文件包
4. 安装完成后点击「部署」→ 设置定价 → 提交审核

## 📊 收益预估（单 Skill）

| 日销量 | 日收入（到手） | 月收入（到手） |
|:--:|:--:|:--:|
| 3 单 | 20.8 元 | 624 元 |
| 5 单 | 34.7 元 | 1,040 元 |
| 10 单 | 69.3 元 | 2,079 元 |
| 15 单 | **104.0 元** ✅ | 3,120 元 |

> 🎯 目标：5 个 Skill × 日均 3 单 = **100+ 元/天**

## 🗺️ 路线图

- [x] 简历优化大师 v1.0 — ATS关键词匹配 + STAR法则改写
- [x] 一句话PPT生成器 v1.0 — 10套行业模板，30秒出大纲
- [x] 合同风险扫描仪 v1.0 — 红黄绿标注 + 法条依据 + 修改建议
- [x] 小红书爆款文案生成器 v1.0 — 联网热点 + 5版标题 + 发布策略
- [x] 体检报告解读助手 v1.0 — 逐项解读 + 异常分级 + 生活方式建议

## ⭐ Star History

如果这个项目对你有帮助，请给一个 Star ⭐

## 📄 License

MIT © [bansheng-dotcom](https://github.com/bansheng-dotcom)
