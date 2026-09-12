# UDRP 英文内容体系 · 实施计划

> 本文件不对外发布（位于 `_internal/`，Jekyll 构建时排除）。
> 本轮只优化现有 `en/udrp-counsel.html`，不新增英文页面。以下为后续实施的架构规划。

## 一、定位：英文页不是中文页的翻译

英文页的读者是**境外品牌权利人、境外域名持有人、以及正在寻找中国境内协作律师的境外代理机构**。他们关心的问题与中文读者不同：

| 读者 | 真实需求 | 对应内容重点 |
|---|---|---|
| 境外品牌权利人 | 被投诉人或其资产在中国境内，如何推进程序与后续执行 | 中文送达路径、中国境内主体的应对习惯、境内诉讼衔接 |
| 境外域名持有人 | 收到投诉后如何组织中文证据、如何选择程序语言 | 中文材料的时间戳与公证、翻译安排、答辩节奏 |
| 境外代理机构 | 需要一个能同时处理英文书面往来与中国境内事务的协作方 | 工作语言、协作方式、可承接的工作范围 |

**写作要求：** 每页必须回答一个英文读者才会问的问题。不得把中文页逐句直译后发布，也不得使用机器翻译文本。

## 二、页面规划（7 页）

| # | 路径 | 页面主题 | 与中文页的对应关系 | 状态 |
|---|---|---|---|---|
| 1 | `/en/udrp.html` | English hub：UDRP 内容总入口与主题索引 | ↔ `/udrp/` | 待建 |
| 2 | `/en/udrp-counsel.html` | UDRP counsel in China（现有页面） | ↔ `/services/udrp-domain-name-disputes.html` | **本轮优化** |
| 3 | `/en/udrp-response.html` | Responding to a UDRP complaint（应诉指引） | ↔ `/services/udrp-response-guide.html` | 待建 |
| 4 | `/en/udrp-complainant.html` | Recovering a domain name（投诉人指引） | ↔ `/services/udrp-domain-name-disputes.html` + 枢纽 04 节 | 待建 |
| 5 | `/en/ai-domain-disputes.html` | `.ai` domain name disputes | ↔ `/services/ai-domain-disputes.html` | 待建 |
| 6 | `/en/udrp-providers.html` | Choosing a UDRP provider | ↔ 枢纽 05 节 | 待建 |
| 7 | `/en/udrp-after-decision.html` | After the decision: mutual jurisdiction and court options | ↔ 枢纽 07、09 节 | 待建 |

**命名约定：** 沿用现有 `/en/*.html` 平铺命名，不再新建子目录，避免与 `/udrp/` 的目录式结构冲突。

## 三、hreflang 配对规则

每一对中英文页面必须**互相**声明 hreflang，且 `x-default` 指向中文页：

```html
<link rel="alternate" hreflang="zh-CN" href="https://weibinlawyer.com/udrp/">
<link rel="alternate" hreflang="en" href="https://weibinlawyer.com/en/udrp.html">
<link rel="alternate" hreflang="x-default" href="https://weibinlawyer.com/udrp/">
```

**现有配对情况（2026-09-12 核对并修正）：**

| 中文页 | 英文页 | 配对状态 |
|---|---|---|
| `/services/udrp-domain-name-disputes.html` | `/en/udrp-counsel.html` | 双向声明，互为对应版本，**正确** |
| `/udrp/` | （无英文版） | 原误将 `/en/udrp-counsel.html` 声明为本页英文版，2026-09-12 已删除该行 |

**说明：** hreflang 必须双向对应。`/udrp/` 原先声明 `hreflang="en"` 指向 `/en/udrp-counsel.html`，但英文页声明的中文对应版本是服务页而非枢纽页，构成单向声明，搜索引擎会忽略。枢纽页本轮已删除该行，仅保留 `zh-CN` 与 `x-default`（均指向自身）。待 `/en/udrp.html` 建成后，再补回 `/udrp/` 的 `hreflang="en"`，指向 `/en/udrp.html`。

## 四、每页必须包含的要素

1. **单一 H1**，英文表述自然，不堆砌关键词
2. `canonical` 指向自身英文 URL
3. hreflang 三行（zh-CN / en / x-default）
4. 结构化数据：`LegalService` 或 `WebPage` + `BreadcrumbList`；作者实体引用 `https://weibinlawyer.com/#wei-bin`
5. 作者实体框（英文版），说明律所全称、执业地、工作语言
6. 明确的"不构成法律意见、不承诺结果"英文说明
7. 与中文对应页的交叉链接（供需要中文细节的读者跳转）

## 五、实体一致性要求（跨语言）

以下信息中英文必须完全一致，不得因翻译而变形：

| 项目 | 统一值 |
|---|---|
| 姓名 | Wei Bin（卫斌） |
| 律所全称 | Beijing Long'an (Shenzhen) Law Firm / 北京市隆安（深圳）律师事务所 |
| 执业地 | Shenzhen, mainland China |
| 工作语言 | Chinese and English |
| 执业证号 | 是否公开待定（与中文站保持同一决定） |
| 邮箱 | weibin@longanlaw.com（英文正式往来）、weibin_328@126.com |

**注意：** 英文页不得出现 "top lawyer""leading firm""best" 等自我评价性表述，与中文站的口径保持一致。

## 六、实施前置条件

- [ ] 英文页面数量达到 3 页以上时，再建立 `/en/udrp.html` 枢纽，避免空枢纽
- [ ] 每页完成后再更新 hreflang 配对，不提前改
- [ ] 英文页完成后同步更新 `llms.txt` 的英文入口
- [ ] 英文页与中文页的结构化数据中，`@id` 引用保持同一实体（`#wei-bin`）
- [ ] 不新增 `.nojekyll` 文件（见 `_internal/README.md` 的发布边界说明）

## 七、本轮范围

**只做一件事：** 优化现有 `/en/udrp-counsel.html`，检查并修正——

- title / description 长度与表述（现有 description 为 212 字符，偏长）
- H1 与 H2 层级
- canonical 与 hreflang
- 结构化数据（现为 `LegalService` + `BreadcrumbList`）
- 与中文枢纽页的交叉链接指向是否已更新为新的枢纽定位
- 移动端显示

**不做：** 新增英文页面、改动英文 URL、重写英文正文。
