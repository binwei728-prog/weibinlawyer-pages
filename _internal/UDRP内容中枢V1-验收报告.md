# UDRP 域名争议内容中枢 V1 · 验收报告

- **站点**：weibinlawyer.com（GitHub Pages，分支根目录 + Jekyll 构建）
- **仓库**：`C:\Users\weibi\weibinlawyer-pages`
- **本轮提交**：`7e9c4fc`
- **报告日期**：2026-09-12
- **本轮范围**：把已有的 `/udrp/` 升级为 Knowledge Hub，建立长期可扩展的 UDRP 内容体系骨架；不新增第二个支柱页，不改 URL，不改设计语言

---

## 一、修改文件清单

### 1.1 新增（发布范围内）

| 文件 | 说明 |
|---|---|
| `udrp/cases/index.html` | 案例库列表页框架。已设 `noindex,follow`，未加入 sitemap，暂未在任何页面链接 |
| `udrp/cases/_templates/case.html` | 单案例页模板。位于下划线目录，Jekyll 构建时整目录排除，不会发布 |

### 1.2 新增（不发布，位于 `_internal/`）

| 文件 | 说明 |
|---|---|
| `_internal/udrp-cases/schema.json` | 案例条目的机器可读数据模型（JSON Schema） |
| `_internal/udrp-cases/待采集清单.md` | 采集铁律、官方来源入口、采集优先级、录入步骤、发布前合规自查 |
| `_internal/udrp-annual-report-2026/结构规划.md` | 《2026 中国相关 UDRP 案件年度观察》结构规划（本轮只出架构） |
| `_internal/udrp-en-plan.md` | 英文内容体系 7 页实施计划 |

### 1.3 修改（10 个文件）

| 文件 | 改动要点 |
|---|---|
| `udrp/index.html` | 枢纽页升级：H1、首屏三入口、新增 4 张结构化表格、答辩清单 7→10 项、.ai 模块升级、A–J 专题导航、Service 节点、2 条新 FAQ、移除单向 hreflang（+172 / −57 行） |
| `articles/udrp-can-brand-owner-recover-domain.html` | 补面包屑（可见 + schema）、改写 description、补 dateModified |
| `articles/udrp-trademark-similarity-not-conclusion.html` | 同上 |
| `articles/udrp-legitimate-rights-evidence.html` | 同上 |
| `articles/udrp-bad-faith-timeline-analysis.html` | 同上 |
| `articles/udrp-response-deadline-and-remedy.html` | 同上 |
| `services/ai-domain-disputes.html` | 补 `Service` 结构化数据（该页是枢纽 06 节对应的服务页，原先只有 WebPage + BreadcrumbList） |
| `en/udrp-counsel.html` | title 73→60 字符；description 212→156 字符 |
| `llms.txt` | 枢纽页新定位、A–J 覆盖说明、UDRP 与商标侵权诉讼关系的一般性说明 |
| `sitemap.xml` | `/udrp/` lastmod → 2026-09-12；首页 lastmod 修正为 2026-09-11（原为 2026-08-30，与实际修改时间不符） |

### 1.4 仓库外的工具（不随站点发布）

| 文件 | 说明 |
|---|---|
| `site-tools/audit_udrp_assets.py` | 新增。UDRP 资产清点（元数据 / 结构化数据 / 全库内链引用统计） |
| `site-tools/audit_udrp_cluster.py` | 新增。UDRP 集群 SEO/GEO/结构化数据终检 |
| `site-tools/fix_udrp_articles.py` | 新增。5 篇文章面包屑与描述的批量补齐（可复用） |
| `site-tools/verify_site.py` | 修改。改为**只校验会被发布的文件**（按 Jekyll 的 `_`/`.` 前缀排除规则），避免把模板中的相对路径误报为断链 |
| `site-tools/prep_viewport_probe.py` | 修改。探针页清单扩至 9 页，新增目录 `en/`、`udrp/cases/` |
| `_probe/viewport/frame.html` | 重建。新增 `h` 参数（iframe 高度），并记录 `file://` 跨域限制的规避方式 |

---

## 二、新增 / 修改 URL

| URL | 状态 | 说明 |
|---|---|---|
| `https://weibinlawyer.com/udrp/cases/` | **新增** | 表单页框架。`noindex,follow`，**未加入 sitemap**，暂未站内链接 |
| `https://weibinlawyer.com/udrp/cases/_templates/case.html` | **不发布** | 位于 `_` 前缀目录，Jekyll 排除，线上应为 404 |
| `https://weibinlawyer.com/udrp/` | 内容升级 | URL 未变；含 `#providers`、`#series`、`#faq` 等既有锚点全部保留 |
| `https://weibinlawyer.com/services/ai-domain-disputes.html` | 结构化数据补充 | URL 未变 |
| `https://weibinlawyer.com/en/udrp-counsel.html` | 元数据优化 | URL 未变 |
| `https://weibinlawyer.com/articles/udrp-*.html`（5 篇） | 结构化数据与描述优化 | URL 未变 |

**未删除、未重定向、未新增任何其他 URL。**

---

## 三、UDRP 信息架构

```
weibinlawyer.com
│
├── / 首页
│      └─ #udrp 模块（2026-09-11 定稿）──────────────┐
│                                                    │
├── /udrp/  ★ UDRP 域名争议法律服务与实务指南（枢纽）  │
│   │        本页即本轮的升级对象                    │
│   │                                                │
│   ├─ 01 什么是 UDRP ──────────── 与商标侵权诉讼比较表
│   ├─ 02 三项要件 ─────────────→ 4 张卡片分别内链系列（一）(二)(三)(四)
│   ├─ 03 被投诉人 ── 4 节点 + 十项答辩核对清单 ──→ 系列（五）、投诉应对指引
│   ├─ 04 投诉人 ─── 四路径比较表 + 4 节点 + 证据顺序
│   ├─ 05 服务机构 ── 5 家机构比较表（含官方链接）
│   ├─ 06 .ai 域名 ── 高权重模块 = 论述 + 4 个争点卡片 ──→ .ai 专题、第一财经媒体页
│   ├─ 07 裁决后还能起诉吗 ── Mutual Jurisdiction ──→ #after
│   ├─ 08 RDNH ──────── 含「与投诉失败的区别」
│   ├─ 09 裁决的执行 ── 十（10）个工作日等待期
│   ├─ 10 中国律师做什么 ── 4 张服务卡 CTA
│   ├─ 11 A–J 实务专题导航 ★ 本轮新增（10 类，逐类映射现有内容）
│   ├─ 12 系列文章与来源 ── 5 篇文章 + 1 条媒体记录 + 规则来源清单
│   ├─ 13 常见问题 ──── 10 条（可见内容与 FAQPage 逐条一致）
│   └─ #contact 联系与咨询
│
├── /services/
│      ├─ udrp-domain-name-disputes.html ──↔ /en/udrp-counsel.html（正确双向 hreflang）
│      ├─ udrp-response-guide.html
│      └─ ai-domain-disputes.html（本轮补 Service 节点）
│
├── /tools/udrp-intake.html  首轮信息梳理器（4 处内链）
│
├── /articles/
│      ├─ udrp-can-brand-owner-recover-domain.html      系列（一）
│      ├─ udrp-trademark-similarity-not-conclusion.html 系列（二）
│      ├─ udrp-legitimate-rights-evidence.html          系列（三）
│      ├─ udrp-bad-faith-timeline-analysis.html         系列（四）
│      └─ udrp-response-deadline-and-remedy.html        系列（五）
│            └─ 5 篇均新增面包屑：首页 / UDRP 枢纽 / UDRP系列（N）
│
├── /media/yicai-ai-domain-dispute-20260903.html  第一财经采访记录
│
└── /udrp/cases/  ○ 案例库框架（noindex，未入 sitemap，未对外链接）
       └─ _templates/case.html  ○ 单案例页模板（不发布）

★ = 本轮新建或重大升级    ○ = 本轮新建但尚未启用    ──→ = 内链方向
```

### A–J 实务专题分类（枢纽 11 节）

| 分类 | 覆盖问题 | 现有内容 |
|---|---|---|
| A · 基础与适用范围 | UDRP 是什么、管哪些域名、与诉讼有何不同 | 枢纽 01 节 |
| B · 三项要件 | 三项要件的举证结构 | 枢纽 02 节；系列（一）(二) |
| C · 被投诉人答辩 | 核验顺序、期限起算、材料、延期 | 枢纽 03 节；系列（五）；投诉应对指引 |
| D · 投诉人追回域名 | 权利固定、证据、路径选择 | 枢纽 04 节；系列（一）；服务说明 |
| E · 服务机构与程序规则 | 五家机构差异与选择 | 枢纽 05 节 |
| F · .ai 与新型后缀 | 适用依据与抗辩空间 | 枢纽 06 节；.ai 专题 |
| G · 恶意判断与时间线 | 取得时间、使用方式、索售 | 系列（四） |
| H · 裁决后司法救济 | 相互管辖、起诉阻止执行 | 枢纽 07、09 节 |
| I · RDNH 与滥用风险 | 恶意投诉的认定与自查 | 枢纽 08 节 |
| J · 中国主体实务 | 送达、管辖地址、中英文往来 | 枢纽 10 节；English service page |

**十类均有对应现有内容，无死链，未预留"即将上线"式空位。**

---

## 四、已建立的内链关系

### 4.1 枢纽页出链（新增）

| 指向 | 位置 | 说明 |
|---|---|---|
| 系列（一）(二)(三)(四) | 02 节三要件卡片 | **本轮新增**，把要件与文章逐项对应 |
| 系列（五）+ 投诉应对指引 | 03 节末 | 本轮新增 |
| 5 家机构官网 | 05 节表格机构名 | **本轮新增**，全部实测 200 |
| .ai 专题 + 第一财经媒体页 | 06 节末 | 保留并强化 |
| 系列（一）(四) + 服务说明 | 11 节 A–J 表 D 行 | 本轮新增 |
| 系列（四） | 11 节 G 行 | 本轮新增 |
| English service page | 10 节、11 节 J 行 | 保留 |

### 4.2 全库内链拓扑（清点结果）

| 目标 | 被引用处数 |
|---|---|
| `/udrp/index.html` | 52（含全站主导航「UDRP 专题」） |
| `/services/udrp-domain-name-disputes.html` | 9 |
| `/services/ai-domain-disputes.html` | 8 |
| `/services/udrp-response-guide.html` | 7 |
| `/tools/udrp-intake.html` | 4 |
| 每篇 UDRP 系列文章 | 5（articles/index + 其余 4 篇，已成网状） |

**结论**：枢纽页是本站被引用最多的专题页之一，5 篇文章之间已形成完整网状互链；本轮补上了「要件 → 文章」「分类 → 内容」两层纵向内链，此前缺失。

---

## 五、已修复的现有文章问题

5 篇 UDRP 系列文章，统一处理：

| 问题 | 处理前 | 处理后 |
|---|---|---|
| 缺面包屑结构化数据 | 0/5 有 `BreadcrumbList` | 5/5 有，且与可见面包屑逐项一致 |
| 缺可见面包屑 | 5 篇均无（另有 15 篇文章已有此组件） | 5 篇均有，与站内既有组件同款 |
| description 偏短且带套话前缀 | 44 / 56 / 58 / 59 / 74 字，均以「卫斌律师UDRP系列文章：」开头 | 81 / 93 / 94 / 118 字（另 1 篇 81 字），改为实体描述 |
| `Article` 缺 `dateModified` | 无 | 5 篇均补 |
| 施工痕迹 | 无发现 | — |
| 移动端 | — | 320 / 360 / 390 / 414 / 480 五档零横向溢出 |

**核对通过、未作改动的项**：title 与 H1 对应、canonical 唯一、`Article.datePublished`、`author → #wei-bin`、作者实体框（已含作者页 / 业务领域 / 枢纽 / 文章索引四链）、每篇已有 4 篇同系列相关文章链接。

---

## 六、SEO / GEO 检查结果

### 6.1 基础要素（UDRP 集群 13 个页面）

| 项目 | 结果 |
|---|---|
| title 唯一性 | 13 个页面 **0 重复** |
| description 唯一性 | **0 重复** |
| canonical 唯一性 | **0 重复**，13/13 均存在 |
| 单一 H1 | 13/13 均为 1 个 H1 |
| title 长度 | 除英文页外全部 ≤ 49 字符；英文页本轮由 73 压至 60 |
| description 长度 | 枢纽 140、媒体 141、英文 156、文章 81–118；服务页 87/92、工具页 82 偏短（见第十一节） |

### 6.2 关键词与语义链

枢纽页建立了完整语义链并与正文自然对应：

> 卫斌律师 → UDRP 域名争议 → .ai 域名争议 → WIPO / CAC 程序 → 投诉 / 答辩 / 品牌域名保护

- **无关键词堆砌**：`keywords` meta 保留但未在正文重复堆叠；每个关键词在正文中都有实质性段落承载
- **无「顶级 / 领先 / 第一 / 知名」类自我评价表述**：全页检索确认为 0
- **无结果承诺**：全页检索「胜诉 / 必然获赔 / 100% / 一定能」确认为 0；页脚与来源说明保留了免责表述

### 6.3 hreflang

| 页面 | 处理 |
|---|---|
| `/services/udrp-domain-name-disputes.html` ↔ `/en/udrp-counsel.html` | 校验为**正确双向配对**，保持不动 |
| `/udrp/` | **修正**：原先声明 `hreflang="en"` 指向 `/en/udrp-counsel.html`，但该英文页声明的中文对应版本是服务页而非枢纽页 → 构成单向声明（搜索引擎会忽略）。本轮删除该行，仅保留 `zh-CN` 与 `x-default` |

### 6.4 canonical / sitemap / robots

| 项目 | 结果 |
|---|---|
| canonical | 13/13 存在且自指 |
| sitemap 收录 | UDRP 相关 10 条；**案例库框架页未收录**（符合设计） |
| robots.txt | 未新增规则。案例库用 `noindex` 而非 robots 屏蔽 —— 这是正确做法：若用 robots 屏蔽，爬虫将看不到 noindex，页面反而可能被索引 |
| 内链可达性 | 全站相对链接 1080 条，**0 失效** |

### 6.5 移动端

以 iframe 精确限定宽度检测（无头 Chrome 在 Windows 下有 512px 窗口下限，`--window-size=360` 实测仍返回 512px，**不能用它测窄视口**）：

| 页面 | 320 | 360 | 390 | 414 | 480 |
|---|---|---|---|---|---|
| 首页 | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |
| `/udrp/` 枢纽 | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |
| `/udrp/cases/` | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |
| 投诉应对指引 | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |
| .ai 域名专题 | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |
| 首轮信息梳理器 | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |
| 英文页 | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |
| UDRP 系列文章 | 无溢出 | 无溢出 | 无溢出 | 无溢出 | 无溢出 |

**唯一越界元素**是 `table.compare-table`（`min-width: 640px`），位于 `.table-wrap`（`overflow-x: auto`）容器内，在容器内横向滚动，属预期行为，不产生页面级横向滚动。

---

## 七、Structured Data 检查结果

| 页面 | 节点类型 | 本轮变化 |
|---|---|---|
| `/udrp/` | WebPage, **Service**, Person, BreadcrumbList, ItemList, FAQPage | 新增 Service；FAQ 8→10 条 |
| `/udrp/cases/` | CollectionPage, BreadcrumbList | 新增 |
| `/services/udrp-domain-name-disputes.html` | LegalService, FAQPage, BreadcrumbList | 未变 |
| `/services/udrp-response-guide.html` | HowTo, BreadcrumbList | 未变 |
| `/services/ai-domain-disputes.html` | WebPage, **Service**, BreadcrumbList | 新增 Service |
| `/tools/udrp-intake.html` | WebApplication | 未变 |
| `/en/udrp-counsel.html` | LegalService, BreadcrumbList | 未变 |
| `/media/yicai-...html` | WebPage, NewsArticle, Person | 未变 |
| 5 篇系列文章 | WebPage, Article, **BreadcrumbList** | 新增 BreadcrumbList；Article 补 dateModified |

**一致性校验**：

- 枢纽页 `Service` 节点使用 `@id: https://weibinlawyer.com/#udrp-service`，**与首页定义的同名实体完全一致**，属同一实体的跨页引用，不产生实体分裂
- 枢纽页 FAQ：可见 10 条 ↔ schema 10 条，**逐条字符级一致**
- 5 篇文章面包屑：可见项 ↔ schema `itemListElement` 名称，**逐项一致**
- 全站 66 个页面 JSON-LD **解析错误 0**

---

## 八、案例库数据模型

文件：`_internal/udrp-cases/schema.json`（JSON Schema draft 2020-12，190 行）

**必填字段（12 项）**：`id`、`caseNumber`、`provider`、`decisionDate`、`disputedDomains`、`complainant`、`respondent`、`result`、`threeElements`、`sourceUrl`、`sourceVerified`、`sourceVerifiedDate`

**关键设计**：

| 设计点 | 做法 |
|---|---|
| 机构限定 | `provider` 用 enum 固定为 WIPO / FORUM / CAC / ADNDRC / CIIDRC 五值 |
| 结果标准化 | `result` 用 enum：转移 / 注销 / 不支持投诉 / 部分支持 / 程序终止 |
| 三项要件 | `threeElements` 逐项取 `upheld` / `failed` / `not-reached`（未认定也如实记录，不猜测） |
| **防伪造的硬约束** | `sourceVerified` 设为 `const: true` —— schema 层面强制，未核对官方全文的条目无法通过校验 |
| 来源限定 | `sourceUrl` 要求 URI，规范中明确禁止使用第三方转载或数据库镜像 |
| 内部/外部字段分离 | `notes` 标注为不对外发布 |
| 发布开关 | `published` 默认 `false`，且规则上不得在 `sourceVerified=false` 时置为 `true` |

**配套**：

- `_internal/udrp-cases/待采集清单.md`：六项采集铁律、五家机构官方入口、P0–P3 采集优先级（按「中国相关度 × 实务参考价值」而非知名度）、七步录入流程、发布前合规自查清单
- `udrp/cases/_templates/case.html`：单案例页模板，含 4 级面包屑、基本信息表、三项要件认定表、来源区块；页内所有数字均标注"照录官方裁决全文"
- `udrp/cases/index.html`：列表页框架，含字段结构说明与收录规则

**本轮未收录任何案例。** 无编造的案号、当事人、裁决结果或统计数字。

---

## 九、下一阶段建议新增的 15 篇文章（按商业意图优先级排序，未撰写）

### 第一梯队：正在遇到问题、可能立即寻求律师（高商业意图）

1. **收到 UDRP 投诉后的头 48 小时：先做哪六件事**
   - 对应分类 C；与系列（五）形成「总—分」，承接真实搜索意图
2. **UDRP 答辩书的写法：结构与常见失分点**
   - 对应分类 C；目前只有"准备什么"，缺"怎么写"
3. **域名是我的品牌，为什么还被投诉：第 4(c) 条正当权益如何举证**
   - 对应分类 B、G；系列（三）的进阶实操版
4. **.ai 域名被大厂投诉：持有人可以怎样答辩**
   - 对应分类 F；直接承接第一财经采访带来的搜索流量
5. **对方开价几十万卖我的品牌域名：协商、UDRP 还是起诉**
   - 对应分类 D、H；目前枢纽 04 节只有表格，缺展开论述
6. **中国主体收到境外域名投诉：送达、程序语言与代理安排**
   - 对应分类 J；中文读者最实际的痛点，现有内容是空白
7. **UDRP 投诉被驳回之后，还能做什么**
   - 对应分类 D、H；覆盖败诉方后续路径

### 第二梯队：正在比较方案、评估投入（中商业意图）

8. **UDRP 与 .cn 域名争议解决办法的关键区别**
   - 对应分类 A、E；枢纽 01 节已埋点「.cn 适用 CNNIC 办法」，缺专文展开
9. **起诉阻止 UDRP 裁决执行：十个工作日窗口内要做什么**
   - 对应分类 H；枢纽 07、09 节的实操延伸
10. **域名争议中的证据固定：时间戳、公证与原始记录**
    - 对应分类 C、D；跨三类读者通用
11. **三人专家组还是一人专家组：费用、周期与结果的取舍**
    - 对应分类 E；枢纽 03 节仅一句提示
12. **商标注册时间晚于域名注册时间，投诉还有希望吗**
    - 对应分类 B、G；典型的高频疑问
13. **域名卖方报价能不能作为恶意证据：完整沟通记录怎么用**
    - 对应分类 G；系列（四）的实操延伸

### 第三梯队：教育型、建立权威与引用（低商业意图、高 Citations 价值）

14. **WIPO、CAC、FORUM、ADNDRC、CIIDRC：五家机构怎么选**
    - 对应分类 E；适合被 AI 搜索直接引用为机构对比依据
15. **通用词与数字域名的 UDRP 抗辩空间**
    - 对应分类 B、F；覆盖 .ai 之外的通用场景

> 以上标题仅为建议清单，**本轮未撰写任何一篇**。建议按第一梯队顺序写作，每篇完成后同步更新枢纽页 A–J 表中对应行的「现有内容」列。

---

## 十、英文版实施计划

文件：`_internal/udrp-en-plan.md`

**核心定位**：英文页不是中文页的翻译。读者是境外品牌权利人、境外域名持有人、境外代理机构，问题域与中文读者不同（中文送达路径、中国境内主体应对、境内诉讼衔接、中文证据与翻译安排）。

**7 页规划**（本轮只优化了第 2 页）：

| # | 路径 | 主题 | 中文对应页 | 状态 |
|---|---|---|---|---|
| 1 | `/en/udrp.html` | English hub | `/udrp/` | 待建 |
| 2 | `/en/udrp-counsel.html` | UDRP counsel in China | `/services/udrp-domain-name-disputes.html` | **本轮优化** |
| 3 | `/en/udrp-response.html` | Responding to a complaint | `/services/udrp-response-guide.html` | 待建 |
| 4 | `/en/udrp-complainant.html` | Recovering a domain | 服务说明 + 枢纽 04 节 | 待建 |
| 5 | `/en/ai-domain-disputes.html` | `.ai` domain disputes | `/services/ai-domain-disputes.html` | 待建 |
| 6 | `/en/udrp-providers.html` | Choosing a provider | 枢纽 05 节 | 待建 |
| 7 | `/en/udrp-after-decision.html` | After the decision | 枢纽 07、09 节 | 待建 |

**约束**：命名沿用 `/en/*.html` 平铺；hreflang 必须双向；跨语言实体信息（姓名 / 律所全称 / 执业地 / 工作语言）必须完全一致；不得出现 "top lawyer""leading firm" 等自我评价表述。

**本轮实际动作**：`/en/udrp-counsel.html` title 由 73 压至 60 字符，description 由 212 压至 156 字符；hreflang 配对经核对确认正确，未改动。

---

## 十一、发现但未修改的问题（仅建议）

| # | 问题 | 位置 | 建议 |
|---|---|---|---|
| 1 | 无 `BreadcrumbList`，且无可见面包屑 | `tools/udrp-intake.html` | 该页已有 `WebApplication` 节点，结构化数据本身合理；若要补面包屑，需同时补可见面包屑（Google 要求两者对应） |
| 2 | description 偏短 | `services/udrp-domain-name-disputes.html`（87 字）、`udrp-response-guide.html`（92 字） | 两页是重要落地页，可扩至 110–150 字以提高摘要完整度 |
| 3 | 全站文章面包屑缺口 | `articles/` 下 36 篇中仍有 31 篇无 `BreadcrumbList`（15 篇有可见面包屑但无 schema） | 本轮只处理了 UDRP 系列 5 篇；其余可批量补齐（已有可复用脚本 `fix_udrp_articles.py`） |
| 4 | `Person` 实体跨页不一致 | 同一 `@id: /#wei-bin` 在 5 个页面 `knowsAbout` 项数不同（14/8/7/9/6），`image` 部分缺失，`worksFor` 写法不一 | 建议确定一份标准 Person 节点，全站统一引用 |
| 5 | 媒体页无 hreflang | `media/yicai-ai-domain-dispute-20260903.html` | 无英文版，属正常；若未来有英文报道页再配对 |
| 6 | 部分页面 lastmod 与实际修改时间不符 | `sitemap.xml` | 本轮修正了首页与 `/udrp/`；建议建立"改页面即更新 lastmod"的固定步骤 |
| 7 | 根目录存在两个含义不明的文件 | `88b706566d554cc9a28a22adcee1f259.txt`、`网站首页预览.png` | 均在发布范围内（可直接访问）。若非必需的验证文件 / 预览图，建议移入 `_internal/`，减少公开面 |
| 8 | 案例库框架页目前是"空页" | `udrp/cases/index.html` | 已用 `noindex` + 不入 sitemap + 不站内链接三重控制。首个案例入库后，再决定是否解除 `noindex` |

---

## 十二、校验与 Git

### 12.1 lint / build / test

本仓库是**纯静态站点**（HTML + 一个 `styles.css` + 原生 JS），根目录**无 `package.json`、无 lockfile、无 ESLint 配置、无 CI workflow**，因此不存在可执行的 lint / build / test 流程。以自建校验脚本作为等效质量门禁：

| 校验 | 命令 | 结果 |
|---|---|---|
| 全站校验 | `site-tools/verify_site.py` | 66 个发布页面；JSON-LD 解析错误 **0**；相对链接 **1080 条 / 0 失效**；标签配平 **0 异常**；施工痕迹 2 处（`tools/*-intake.html` 内的合法内联 JS 字符串，误报） |
| 集群终检 | `site-tools/audit_udrp_cluster.py` | 13 个页面 title/description/canonical **0 重复**，单一 H1 13/13，结构化数据全部解析通过 |
| 视口探针 | `frame.html?p=…&w=…` | 8 页 × 5 档宽度 = 40 组，**0 页面级横向溢出** |
| 外链实测 | `curl -L -o /dev/null -w "%{http_code}"` | 5 家机构官网 + WIPO .ai 说明 + ICANN 机构列表，**7/7 返回 200** |

**校验器本身的一处修正**：`verify_site.py` 原先把 `_internal/`、`udrp/cases/_templates/` 等**不会发布**的目录也纳入检查，导致模板中按"复制后位置"书写的相对路径被误报为 13 条断链。已改为按 Jekyll 的排除规则（任一路径段以 `_` 或 `.` 开头即不发布）只校验发布范围，误报清零。

### 12.2 Git diff 摘要

```
7e9c4fc feat(udrp): UDRP 内容中枢 V1——枢纽页升级为 Knowledge Hub、案例库框架、面包屑与结构化数据补齐

 _internal/udrp-annual-report-2026/结构规划.md       | 123 +
 _internal/udrp-cases/schema.json                   | 190 +
 _internal/udrp-cases/待采集清单.md                  |  66 +
 _internal/udrp-en-plan.md                          |  95 +
 articles/udrp-bad-faith-timeline-analysis.html     |  99 +-
 articles/udrp-can-brand-owner-recover-domain.html  | 101 +-
 articles/udrp-legitimate-rights-evidence.html      |  98 +-
 articles/udrp-response-deadline-and-remedy.html    |  98 +-
 articles/udrp-trademark-similarity-not-conclusion.html | 98 +-
 en/udrp-counsel.html                               |   6 +-
 llms.txt                                           |   6 +-
 services/ai-domain-disputes.html                   |   1 +
 sitemap.xml                                        |   4 +-
 udrp/cases/_templates/case.html                    | 167 +
 udrp/cases/index.html                              | 101 +
 udrp/index.html                                    | 229 +-
 16 files changed, 1279 insertions(+), 203 deletions(-)
```

枢纽页单文件：**+172 / −57 行**（355 → 471 行）。

### 12.3 修改范围自查（对照简报第十一节）

| 禁止项 | 是否触及 |
|---|---|
| 重做首页 | 否 —— 首页本轮**零改动** |
| 改造设计语言 | 否 —— 未改 `styles.css` 一行，全部复用既有组件类 |
| 改 Logo / 主色 | 否 |
| 改四大核心业务 | 否 |
| 批量重写文章 | 否 —— 5 篇只补结构元素与描述，正文一字未改 |
| 删除媒体证据 | 否 —— 媒体页本轮零改动，枢纽仍链向它 |
| 把 UDRP 提升为第一主营 | 否 —— 首页定位未动，枢纽仍在「业务领域」之下 |
| 添加「顶级 / 领先 / 第一 / 知名」 | 否 —— 全页检索确认为 0 |
| 机械堆砌关键词 | 否 |
| 新增第二个支柱页 | 否 —— 原地升级 `/udrp/` |
| 改动或删除已有 URL | 否 —— 仅新增 `/udrp/cases/` |

---

## 结论

本轮**按要求建立了一个可长期扩展的 UDRP 树干，而不是一次性长完整片森林**：

- 枢纽页从「一篇长文」变成「有结构、有分类、有入口的知识中枢」
- 补上了此前缺失的两层纵向内链（要件 → 文章、分类 → 内容）
- 案例库具备了数据模型与采集规范，但**没有填入任何一个未经核实的案例**
- 年度报告与英文版都只出架构，未提前制造内容
- 所有规则引用（Policy 4(a)/4(c)/4(i)/4(k)、Rules 1/4(f)/5(a)–(f)/15(e)）本轮重新对照 ICANN 官方文本逐条核验，**编号与内容一致**；其中「二十（20）日」是否为日历日，另有 ADR Forum 专家组意见明确印证为日历日

**唯一需要提前知晓的取舍**：案例库列表页 `/udrp/cases/` 目前是一张空页。已用 `noindex` + 不入 sitemap + 不站内链接三重控制，搜索引擎与访客都不会遇到它；等首批案例完成官方核对后再决定是否启用。
