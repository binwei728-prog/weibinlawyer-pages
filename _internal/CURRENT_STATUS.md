# 当前状态

记忆版本：3
最后校准：2026-09-11（本地仓库、远端分支与文件实查）
变更摘要：完成本轮「定位强化 + GEO 强化 + 转化优化」——新建 /udrp/ 支柱页、首页结构收敛、媒体证据页升级、全站作者实体框统一；已提交并推送 origin/main。

## 已验证现状
- [Confirmed] 仓库为卫斌律师个人静态网站，远端为 `binwei728-prog/weibinlawyer-pages`。正式站点 `https://weibinlawyer.com/`（GitHub Pages，CNAME 指向自定义域名）。（Git remote 实查，2026-09-11）
- [Confirmed] 本轮新增 `udrp/index.html` UDRP 支柱页：适用范围、第 4(a) 条三项要件、第 4(c) 条抗辩、被投诉人期限与答辩、投诉人路径、五家 ICANN 认可机构比较表、.ai 域名、相互管辖、RDNH、裁决后十个工作日执行期、中国律师工作内容、系列文章入口、FAQ；含 BreadcrumbList、FAQPage、ItemList、Person 结构化数据。（文件实查，2026-09-11）
- [Confirmed] 首页结构已收敛为：首屏定位（含方法论句）→ 四个核心业务入口 → 跨境与新型争议专项（UDRP）→ 为什么选择我 → 权威媒体与第三方公开记录 → 最新专业文章 → LegalTech 项目（证券索赔，已压缩）→ 律师介绍 → 联系。（`index.html` 实查）
- [Confirmed] `media-interviews.html` 已升级为第三方证据页：每条记录含媒体名称、日期、报道标题、受访讨论的问题、原始报道链接（另附转载版链接）。（文件实查）
- [Confirmed] 39 篇 `articles/*.html` 与 4 篇 `publications/*.html` 底部已统一「作者实体信息」区块；「公众号原文链接取得后将补充至本页」施工痕迹已全部清除（仅 `tools/*intake*.html` 表单 JS 保留「待补充」占位兜底，属正常）。（文件实查）
- [Confirmed] 52 个页面的导航新增「UDRP 专题」入口；5 篇 UDRP 文章、3 个 UDRP 服务页、英文页、文章索引页、业务领域页均已回链支柱页。（文件实查）
- [Confirmed] 全站校验通过：65 个 HTML 文件，JSON-LD 解析 0 错误，1041 条相对链接 0 失效，标签配平 0 异常；sitemap 62 条 URL 全部指向存在的本地文件。（校验脚本实查，2026-09-11）
- [Confirmed] UDRP 规则引用已按 ICANN 官方英文文本逐条核对：Policy 4(a)/4(c)/4(i)/4(k)；Rules 第 1 条（相互管辖定义）、4(f)（程序开始日）、5(a)（二十个日历日）、5(b)（自动延长四日）、5(d)（改选三人组费用）、5(e)（例外延期）、5(f)（未答辩）、15(e)（反向域名劫持）。（2026-09-11 抓取 icann.org 原文核验）
- [Confirmed] 机构名单已核实：ICANN 现列五家 —— ADNDRC、CIIDRC、CAC、FORUM、WIPO；ACDR/CPR/eResolution 为前机构。（icann.org 中文机构列表页，2026-09-11）
- [Confirmed] `.ai` 已整体采纳 UDRP（非变体政策），WIPO 官方 ccTLD 说明页列明。注意：`.io` 属 UDRP **变体**政策，不得与 `.ai` 混为一类。（wipo.int .AI 页，2026-09-11）

## 本地、远端与线上
- 线上或正式环境锚点：`https://weibinlawyer.com/`。
- 本轮提交：本地 `388fb93`，已推送 origin/main；另一会话并行提交 `09c1fe2` 已合并（保留本会话实现，合入其新增的四份记忆文件与 AGENTS.md）。
- 尚未发布的变更：无。

## 当前问题
- 线上四个地址（`/`、`/practices.html`、`/udrp/`、`/sitemap.xml`）需推送后实测 200 与正文。
- 360px、390px 手机端真实 viewport 仍需人工复核（本轮已抽查 1280px 桌面与 390px 移动首屏）。
- `claim.weibinlawyer.com` 外链可访问性建议定期复核。

## 待确认
- [Observed] 用户此前提出的四项表态项仍未回复：是否接入统计服务、是否公开费用区间、是否公开执业证号（现已公开）、媒体联系页是否并列律所邮箱（本轮已在服务页与首页并列公开两个邮箱）。
- [Observed] 另一会话与本次会话对同一份需求各做了一版首页实现；本会话版本胜出并已合并，其首页专用样式类（`.udrp-feature`/`.credibility-grid` 等）已不再使用，可在下次清理时删除。

## 最近完成的重要工作
- 新建 `/udrp/` 支柱页，作为全站 UDRP 内容集群中心（规则 + 程序 + 机构 + FAQ + 文章入口）。
- 首页新增方法论句、UDRP 独立专项区块、可核验事实清单、律师介绍区块；媒体证据链按证明层级重排；证券索赔模块压缩为 LegalTech 小模块。
- `media-interviews.html` 升级为第三方证据页；`llms.txt` 增补 UDRP 专项与规则依据；`sitemap.xml` 新增 `/udrp/` 并刷新 lastmod。
