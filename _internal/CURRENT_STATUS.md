# 当前状态

记忆版本：6
最后校准：2026-09-12（本地文件实查 + 无头浏览器多断点渲染实测；**线上复核未执行——推送未成功**）
变更摘要：首页精准优化已**提交到本地** `89ab1c4`（仅 `index.html`，+17/−21）——UDRP 专项模块文案定稿（第 4 关键词改「品牌域名保护」、CTA2 指向支柱页 `#series`）、媒体正文改为第一财经领起并加「执业后」、新增压缩版「专业研究与公共表达」、证券索赔模块压缩为「一句 + 单一 CTA」并删除产品使用细节、首页新增 UDRP `Service` 结构化数据节点。**推送被环境出口故障阻塞（本地代理对 POST 返回 502），远端仍为 `142b823`，故尚未上线。**

## 已验证现状
- [Confirmed] **无头浏览器窄视口实测（本轮新增方法）**：Windows 版 Chrome 无头模式存在约 512px 最小窗口宽度，直接用 `--window-size=360/390` **测不到真实窄视口**（三次不同参数均返回 `vw=512`）。改用 iframe 精确指定宽度后可测：首页在 320/360/390/414/480 五档**横向零溢出、零越界元素**；媒体证据页同样全绿；UDRP 支柱页唯一越界元素是机构对比表，位于 `overflow-x` 容器内，属预期行为。（2026-09-11 实测）
- [Confirmed] **首页工作区状态**：`index.html` 有未提交改动（+17/−21），其余文件与仓库其余部分干净；`robots.txt`、`sitemap.xml`、`llms.txt`、canonical、viewport 均未被本轮改动触及。（git 实查）
- [Confirmed] 本轮全站校验通过：65 个 HTML、JSON-LD 解析 0 错误、1042 条相对链接 0 失效、标签配平 0 异常（其中 2 条「施工痕迹」命中为 `tools/*-intake.html` 表单 JS 的「待补充」占位兜底，属正常）。（`verify_site.py` 实查）
- [Confirmed] 首页结构化数据现状：`@graph` 含 WebSite + **Service（本轮新增 `#udrp-service`）** + Person(`#wei-bin`) + FAQPage；另有一段独立的 `WebApplication`（指向 `claim.weibinlawyer.com`）。H1 唯一，H2 共 9 个，层级正常。（文件实查）
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
- 尚未发布的变更：**首页提交 `89ab1c4` 仍在本地，尚未推上 origin/main**（远端 HEAD 仍为 `142b823`）。
- **推送阻塞诊断（2026-09-12）**：本机出网流量全部经本地代理（`http_proxy=http://127.0.0.1:59473`，系统标记 transparent proxy）。`git ls-remote`（GET）正常，`git push`（POST）连续 10+ 次失败，错误在 `schannel: failed to receive handshake` / `Empty reply from server` / `CONNECT tunnel failed, response 502` / `Recv failure: Connection was reset` 之间跳动；清空代理直连更差（21 秒超时）。**属环境国际出口故障，非仓库/凭据/配置问题。** 处置：不改 git 配置、不清代理，等出口恢复后用带 `timeout` 的循环重试；**提交已在本地落盘，恢复后一条 `git push origin main` 即可，无需重做任何改动**。
- 发布纪律：本项目 `PROJECT_CONTEXT.md` 明确「不自动提交、推送或部署，除非用户针对本次变更明确授权」。**记忆文件与站点代码的提交/推送均须先取得用户对本轮变更的授权。**
- 推送注意：本机到 GitHub 的 HTTPS 连接偶发 `schannel` TLS 握手失败，首次推送常失败、重试即成功；建议推送时保留重试循环并以 `git ls-remote origin main` 与本地 `rev-parse HEAD` 比对确认。

## 当前问题
- **（范围外，仅建议）文章页结构化数据覆盖缺口**：36 篇 `articles/*.html` 中，仅 13 篇含 `Article`，**0 篇含 `BreadcrumbList`**，`articles/index.html` 无任何 JSON-LD。建议后续为文章页统一补 `Article` + `BreadcrumbList`。
- **（范围外，仅建议）Person 节点跨页属性不一致**：同一 `@id`（`#wei-bin`）在首页/UDRP 页/媒体页/关于页/研究页上的 `knowsAbout` 分别为 14/8/7/9/6 项，`image` 部分页面缺失，`worksFor` 一部分写内联对象、一部分引用 `#longan-shenzhen`。同一 `@id` 属性发散可能削弱实体一致性信号，建议统一为同一套属性（以首页 14 项为基准）。
- **（范围外，仅建议）页面级配置覆盖不全**：canonical 42/44、viewport 42/44、og:title 27/44——有若干页面缺 og 标签，需先定位再决定是否补。
- **（范围外，仅建议）sitemap 首页 `lastmod` 仍为 `2026-08-30`**，落后于实际内容更新日期。
- 360px、390px 手机端已用无头浏览器按区块实测通过（本轮方法见上），如需真机复核仍建议抽查一次。
- `claim.weibinlawyer.com` 外链可访问性建议定期复核。
- 根目录 `netlify.toml` 仍可公网读取（内容仅为构建目录与两个安全响应头，无敏感信息）。是否移入 `_internal/` 待用户决定——若将来重新启用 Netlify 需保留该文件在根目录。

## 待确认
- [Observed] 用户此前提出的四项表态项仍未回复：是否接入统计服务、是否公开费用区间、是否公开执业证号（现已公开）、媒体联系页是否并列律所邮箱（本轮已在服务页与首页并列公开两个邮箱）。
- [Observed] 另一会话与本次会话对同一份需求各做了一版首页实现；本会话版本胜出并已合并，其首页专用样式类（`.udrp-feature`/`.credibility-grid` 等）已不再使用，可在下次清理时删除。

## 最近完成的重要工作
- 首页精准优化一轮（仅 `index.html`）：UDRP 专项模块文案定稿与第 4 关键词替换、媒体正文改由第一财经领起、新增压缩版「专业研究与公共表达」、证券索赔压缩为单句 + 单一 CTA、新增 UDRP `Service` 结构化数据节点。
- 关闭内部文件公网暴露面：12 个内部文件迁入 `_internal/`，根目录 `AGENTS.md` 改为指针桩并排除发布，`robots.txt` 增加第二层 Disallow，线上实测全部 404。
- 新建 `/udrp/` 支柱页，作为全站 UDRP 内容集群中心（规则 + 程序 + 机构 + FAQ + 文章入口）。
- 首页新增方法论句、UDRP 独立专项区块、可核验事实清单、律师介绍区块；媒体证据链按证明层级重排；证券索赔模块压缩为 LegalTech 小模块。
- `media-interviews.html` 升级为第三方证据页；`llms.txt` 增补 UDRP 专项与规则依据；`sitemap.xml` 新增 `/udrp/` 并刷新 lastmod。
