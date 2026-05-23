# 🔥 扣子（Coze）Skill 技能包合集

[![GitHub stars](https://img.shields.io/github/stars/bansheng-dotcom/linhuaxie?style=flat)](https://github.com/bansheng-dotcom/linhuaxie/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bansheng-dotcom/linhuaxie?style=flat)](https://github.com/bansheng-dotcom/linhuaxie/network) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> 🎯 零成本 AI 创收实践——在扣子平台上开发和上架可付费的 AI 技能包，实现日收入 100 元目标。

## 📦 已上架 Skill

| # | Skill 名称 | 类型 | 定价 | 简介 |
|:--:|------|------|:--:|------|
| 1 | [简历优化大师](./resume_optimizer/SKILL.md) | 提示词 + 工作流 | **9.9 元/次** | ATS关键词匹配 + STAR法则改写，提升面试邀约率 |

## 🚀 快速使用

### 新手用户（直接安装使用）

1. 打开 [扣子技能商店](https://www.coze.cn/skills)
2. 搜索「简历优化大师」
3. 点击安装，即刻使用

### 开发者（导入本地 Skill 包）

```bash
# 进入对应 Skill 目录，打包为 .zip
cd resume_optimizer
zip -r resume_optimizer.skill *

# 在扣子编程中上传
# 打开 https://code.coze.cn → 技能 → 上传技能文件包
```

## 📁 目录结构

```
coze-skills/
├── resume_optimizer/              ← 简历优化大师 Skill
│   ├── SKILL.md                   ← 核心：完整 System Prompt + 工作流
│   ├── references/                ← 知识库（AI自动调用）
│   │   ├── ats_keywords.md        ← 8大行业ATS关键词库
│   │   ├── star_examples.md       ← STAR法则改写示例
│   │   ├── verb_thesaurus.md      ← 弱动词→强动词替换表
│   │   └── self_eval_template.md  ← 自我评价改写模板
│   ├── scripts/
│   │   └── keyword_matcher.py     ← 工作流代码节点
│   └── assets/
│       └── store_listing.md       ← 商店上架文案
├── .gitignore
└── README.md
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

- [x] 简历优化大师 v1.0
- [ ] 一句话PPT生成器
- [ ] 合同风险扫描仪
- [ ] 小红书爆款文案生成器
- [ ] 体检报告解读助手

## ⭐ Star History

如果这个项目对你有帮助，请给一个 Star ⭐

## 📄 License

MIT © [bansheng-dotcom](https://github.com/bansheng-dotcom)
