# 待办

维护规则：只保留当前行动项；完成且无上下文价值的条目删除。

## P0
- [ ] 案例库首批采集（结构已就位，尚未采集任何案例）。建议按 `_internal/udrp-cases/待采集清单.md` 的优先级：
  - P0a：`.ai` 域名 + 裁决结果不支持投诉的案件 2–3 件（支撑枢纽 06 节四个争点）
  - P0b：裁决中声明 RDNH 的案件 1–2 件（支撑枢纽 08 节，可与「投诉失败」明确区分）
  - 每条须完成官方来源逐字核对，`sourceVerified` 置 `true` 后方可录入
- [ ] 用户四项待表态仍未回复：是否接入统计服务、是否公开费用区间、是否公开执业证号、媒体联系页是否并列律所邮箱。

## P1
- [ ] 把 `site-tools/fix_udrp_articles.py` 改造为通用脚本，为剩余 31 篇 `articles/*.html` 补 `BreadcrumbList`（注意：其中 15 篇**已有可见面包屑但无 schema**，需按可见项生成，不能照抄 UDRP 系列的三级结构）。
- [ ] 为 `articles/*.html` 统一补 `Article`：现 36 篇中 23 篇已有、13 篇缺失。
- [ ] （建议，待用户确认）统一 `#wei-bin` Person 节点属性：`knowsAbout` 跨页为 14/8/7/9/6 项、`image` 部分缺失、`worksFor` 写法不一。建议以首页 14 项版本为基准。
- [ ] （建议，待用户确认）定位并补齐 canonical／viewport（各缺 2 页）与 og:title（缺 17 页）。
- [ ] （建议，待用户确认）UDRP 服务页与工具页 description 由 82–92 字扩至 110–150 字。
- [ ] （建议，待用户确认）把「改页面即更新 `sitemap.xml` lastmod`」固化为发布前的固定步骤（本轮已出现 `lastmod` 落后于实际修改日期的情况）。
- [ ] （建议，待用户确认）核实根目录 `88b706566d554cc9a28a22adcee1f259.txt` 与 `网站首页预览.png` 是否必需；若非必需，移入 `_internal/`。
- [ ] 观察枢纽页与 UDRP 服务页的关键词分工：枢纽页面向信息检索（UDRP 是什么／三要件／答辩期限），服务页面向商业检索（UDRP 律师／投诉应对），避免自我竞争。A–J 分类上线后需复核两者是否出现新的重叠。
- [ ] 检查首页外链 `claim.weibinlawyer.com` 的正式可访问性 — 若未上线，避免长期保留无效转化入口。
- [ ] 清理另一会话遗留的未使用首页样式类（`.udrp-feature`、`.udrp-feature-copy`、`.udrp-tags`、`.udrp-proof`、`.credibility-section`、`.credibility-grid`、`.proof-label`、`.udrp-lead`）。

## P2
- [ ] UDRP 后续选题（本轮已产出 15 篇建议清单，见 `_internal/UDRP内容中枢V1-验收报告.md` 第九节）。第一梯队 7 篇优先：
  1. 收到 UDRP 投诉后的头 48 小时：先做哪六件事
  2. UDRP 答辩书的写法：结构与常见失分点
  3. 域名是我的品牌，为什么还被投诉：第 4(c) 条正当权益如何举证
  4. .ai 域名被大厂投诉：持有人可以怎样答辩
  5. 对方开价几十万卖我的品牌域名：协商、UDRP 还是起诉
  6. 中国主体收到境外域名投诉：送达、程序语言与代理安排
  7. UDRP 投诉被驳回之后，还能做什么
  - 每篇完成后同步更新枢纽页 A–J 表对应行的「现有内容」列
- [ ] 英文内容体系：按 `_internal/udrp-en-plan.md` 建 6 个新页面（达到 3 页以上时再建 `/en/udrp.html` 英文枢纽，并同步修正 `/udrp/` 的 hreflang）。
- [ ] 年度报告：按 `_internal/udrp-annual-report-2026/结构规划.md` 推进 M1（确定口径 + 检索方案）。
- [ ] 按用户指定内容配比继续产出：UDRP/域名约 40%、金融投资及证券约 30%、公司治理与刑民交叉约 20%、媒体热点专业评论约 10%。
- [ ] 建议的公司治理选题：董事会席位与股东会决议效力攻防、实控人失去公章账册后的救济路径。

## 近期完成
- [x] **UDRP 域名争议内容中枢 V1**（2026-09-12，提交 `7e9c4fc` + `e5afa1f`，已推送并线上实测）：
  `/udrp/` 原地升级为 471 行 Knowledge Hub（新 H1、首屏三入口、4 张比较表、答辩清单 7→10 项、.ai 模块升级、A–J 十类实务专题导航、`Service` 节点、FAQ 8→10 条、移除单向 hreflang）；
  5 篇系列文章补面包屑（可见 + `BreadcrumbList`）、改写 description、补 `Article.dateModified`；
  新增 `udrp/cases/` 案例库框架（noindex，未入 sitemap）与单案例页模板（`_templates/`，线上 404 已验证）；
  新增 `_internal/udrp-cases/schema.json`（`sourceVerified` 设为 `const: true` 强制核实）、采集规范、年度报告结构规划、英文版 7 页实施计划。
- [x] 逻辑核验：Policy 4(a)/4(c)/4(i)/4(k) 与 Rules 1、4(f)、5(a)–(f)、15(e) 全部对照 ICANN 原文逐条复核通过（期间识别并排除了一次 AI 摘要给出的错误编号）。
- [x] `verify_site.py` 改为只校验发布范围（按 Jekyll `_`/`.` 前缀排除规则），误报断链由 13 条清零。
- [x] 首页精准优化一轮（仅 `index.html`，提交 `89ab1c4` 并推送）。
- [x] 内部文件公网可读问题修复：12 个内部文件迁入 `_internal/`，线上实测全部 404，站点主体全部 200（提交 `ac61bfe`）。
- [x] 手机端（320/360/390/414/480）与桌面端显示效果复核。
- [x] 新建 `/udrp/` 支柱页并接入全站导航与内链集群。
- [x] `media-interviews.html` 升级为第三方证据页（含原始报道链接）。
- [x] 全站 43 篇文章统一作者实体框，清理施工痕迹。
- [x] sitemap / llms.txt / 结构化数据同步更新并全站校验通过。
