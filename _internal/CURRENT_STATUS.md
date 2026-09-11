# 当前状态

记忆版本：4
最后校准：2026-09-11（本地仓库、远端分支与线上实测三查）
变更摘要：修复内部文件公网可读问题——项目记忆四件套、运维文档与两个脚本共 12 个文件迁入 `_internal/`（Jekyll 默认忽略下划线前缀目录），根目录 `AGENTS.md` 降级为指针桩并以 front matter 排除发布；线上实测 12 个文件全部 404，站点主体全部 200。提交 `ac61bfe` 已推送 origin/main。

## 已验证现状
- [Confirmed] **托管链已核实**：`weibinlawyer.com` 解析至 GitHub Pages IP（185.199.108.153 / 185.199.109.153），响应头 `Server: GitHub.com`（Fastly 边缘缓存）。仓库既无 `.nojekyll` 也无 `.github/workflows`，故 GitHub Pages 采用**分支根目录 + Jekyll 构建**方式发布——这是 `_internal/` 被排除的机制前提。根目录 `netlify.toml` 为遗留配置，Netlify 已非托管方。（DNS + 响应头 + 仓库实查，2026-09-11）
- [Confirmed] **迁移前**实测：`AGENTS.md`、四份记忆文件、五份中运维文档、`replace-domain.ps1`、`tools/update_structured_data.py` 共 12 个文件均可经公网 200 直接读取。（curl 实测，2026-09-11）
- [Confirmed] **迁移后**实测：上述 12 个文件全部返回 404（含 `_internal/` 内文件，`AGENTS.md` 连续 6 次探测均 404，`/AGENTS`、`/AGENTS.html` 旁路同为 404）；同时 `/`、`/udrp/`、`/practices.html`、`/sitemap.xml`、`/media-interviews.html`、`/llms.txt`、`/en/udrp-counsel.html`、`/articles/index.html`、`tools/udrp-intake.html`、`tools/enterprise-risk-intake.html` 全部 200。**排除机制经线上实证生效，站点功能无损。**（curl 实测，2026-09-11）
- [Confirmed] 项目记忆四件套与运维文档现位于 `_internal/`；根目录 `AGENTS.md` 仅保留「记忆位置指针 + 长期记忆规则 + 发布边界」三类内容，不再承载项目状态，并用 YAML front matter `published: false` 排除发布。Codex 对根目录 `AGENTS.md` 的自动加载入口保持不变。（文件实查）
- [Confirmed] `tools/` 目录下的 `udrp-intake.html`、`enterprise-risk-intake.html` 是线上正式页面（均 200），迁移时原地保留；`tools/update_structured_data.py` 已单独移出至 `_internal/`。（线上实测）
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
- 最近提交：`ac61bfe`（内部文件迁入 `_internal/`），已推送 origin/main，远端 HEAD 与本地一致。
- 前序提交：`388fb93`（UDRP 支柱页与首页改造）+ `e0492cf`（记忆同步）+ `0a6f90a`（合并并行会话）。
- 尚未发布的变更：`_internal/` 下记忆文件的版本与内容更新（提交后将再次推送）。
- 推送注意：本机到 GitHub 的 HTTPS 连接偶发 `schannel` TLS 握手失败，首次推送常失败、重试即成功；建议推送时保留重试循环并以 `git ls-remote origin main` 与本地 `rev-parse HEAD` 比对确认。

## 当前问题
- 360px、390px 手机端真实 viewport 仍需人工复核（本轮已抽查 1280px 桌面与 390px 移动首屏）。
- `claim.weibinlawyer.com` 外链可访问性建议定期复核。
- 根目录 `netlify.toml` 仍可公网读取（内容仅为构建目录与两个安全响应头，无敏感信息）。是否移入 `_internal/` 待用户决定——若将来重新启用 Netlify 需保留该文件在根目录。

## 待确认
- [Observed] 用户此前提出的四项表态项仍未回复：是否接入统计服务、是否公开费用区间、是否公开执业证号（现已公开）、媒体联系页是否并列律所邮箱（本轮已在服务页与首页并列公开两个邮箱）。
- [Observed] 另一会话与本次会话对同一份需求各做了一版首页实现；本会话版本胜出并已合并，其首页专用样式类（`.udrp-feature`/`.credibility-grid` 等）已不再使用，可在下次清理时删除。

## 最近完成的重要工作
- 关闭内部文件公网暴露面：12 个内部文件迁入 `_internal/`，根目录 `AGENTS.md` 改为指针桩并排除发布，`robots.txt` 增加第二层 Disallow，线上实测全部 404。
- 新建 `/udrp/` 支柱页，作为全站 UDRP 内容集群中心（规则 + 程序 + 机构 + FAQ + 文章入口）。
- 首页新增方法论句、UDRP 独立专项区块、可核验事实清单、律师介绍区块；媒体证据链按证明层级重排；证券索赔模块压缩为 LegalTech 小模块。
- `media-interviews.html` 升级为第三方证据页；`llms.txt` 增补 UDRP 专项与规则依据；`sitemap.xml` 新增 `/udrp/` 并刷新 lastmod。
