# UDRP 政策与程序规则 · 条文核对记录

- **核对日期**：2026-09-12
- **核对方法**：下载 ICANN 官方页面原文（`curl -L`，397,386 字节），本地去标签后逐条检索上下文比对；不使用抓取工具返回的 AI 摘要
- **原文来源**：
  - 政策：https://www.icann.org/resources/pages/policy-2024-02-21-en/
  - 程序规则：https://www.icann.org/resources/pages/udrp-rules-2015-03-11-en
  - 规则生效说明（原文载明）：ICANN 董事会 2013-09-28 批准；适用于 **2015-07-31 及之后**向服务机构提交投诉的全部 UDRP 程序
- **机构名单**：https://www.icann.org/zh/help/dndr/udrp/providers（五家：ADNDRC、CIIDRC、CAC、FORUM、WIPO）

> 本文件只记录**核对结论与关键原文片段**，不存放 ICANN 原文全本。需要复核时按上述 URL 重新抓取。

---

## 一、政策（Policy）条款

| 条款 | 内容要点 | 站点引用位置 | 结论 |
|---|---|---|---|
| 第 4(a) 条 | 投诉人须同时证明三项：域名与商标相同或混淆性近似；持有人无权利或合法利益；域名被恶意注册并被恶意使用 | 枢纽 02 节、5 篇文章、FAQ | ✓ 一致 |
| 第 4(c) 条 | 被投诉人可据以证明权利或合法利益的三种典型情形 | 枢纽 02 节、系列（三） | ✓ 一致 |
| 第 4(i) 条 | 救济限于注销域名或将域名注册转移给投诉人，不含损害赔偿 | 枢纽 01、07 节、FAQ | ✓ 一致 |
| 第 4(k) 条 | 注册商收到裁决通知后等待十（10）个工作日再执行；期间被投诉人于相互管辖范围内起诉并提交官方文书的，不执行裁决 | 枢纽 09 节、FAQ | ✓ 一致 |

## 二、程序规则（Rules）条款

| 条款 | 核对到的原文要点 | 站点引用位置 | 结论 |
|---|---|---|---|
| 第 1 条（定义） | `Mutual Jurisdiction` 定义为：(a) 注册商主要营业地所在法域（前提是域名持有人在注册协议中已就该管辖提交法院裁判域名争议）；或 (b) 投诉提交给服务机构时注册管理机构 Whois 数据库中记载的域名持有人地址所在法域。另定义 `Reverse Domain Name Hijacking` 为「以恶意方式使用该政策，试图剥夺已注册域名持有人持有的域名」 | 枢纽 07、08 节 | ✓ 一致 |
| 第 4(f) 条 | 原文：*"The date of commencement of the administrative proceeding shall be the date on which the Provider completes its responsibilities under Paragraph 2(a) in connection with sending the complaint to the Respondent."* | 枢纽 03 节、系列（五） | ✓ 一致（编号与内容均正确） |
| 第 5(a) 条 | 原文：*"Within twenty (20) days of the date of commencement of the administrative proceeding the Respondent shall submit a response to the Provider."* | 枢纽 03 节、FAQ | ✓ 内容一致；「日历日」的判定见下节 |
| 第 5(b) 条 | 原文：*"The Respondent may expressly request an additional four (4) calendar days in which to respond to the complaint, and the Provider shall automatically grant the extension and notify the Parties thereof."* | 枢纽 03 节、FAQ | ✓ 一致 |
| 第 5(d) 条 | 投诉人选择一人组而被投诉人选择三人组时，被投诉人须缴三人组适用费用的二分之一；须随答辩一并缴纳，未缴纳的由一人组审理 | 枢纽 03 节 | ✓ 一致 |
| 第 5(e) 条 | 原文：*"At the request of the Respondent, the Provider may, in exceptional cases, extend the period of time for the filing of the response. The period may also be extended by written stipulation between the Parties, provided the stipulation is approved by the Provider."* | 枢纽 03 节、FAQ | ✓ 一致 |
| 第 5(f) 条 | 原文：*"If a Respondent does not submit a response, in the absence of exceptional circumstances, the Panel shall decide the dispute based upon the complaint."* | 枢纽 03 节、FAQ | ✓ 一致 |
| 第 15(e) 条 | 原文：*"...If after considering the submissions the Panel finds that the complaint was brought in bad faith, for example in an attempt at Reverse Domain Name Hijacking or was brought primarily to harass the domain-name holder, the Panel shall declare in its decision that the complaint was brought in bad faith and constitutes an abuse of the administrative proceeding."* | 枢纽 08 节、FAQ | ✓ 一致 |

### 「Panel Decisions = 第 15 条」的定位依据

ICANN 官方页面在去标签后**不保留条款序号**，无法直接读出编号。定位依据来自公开裁决书中的引注：

- ADR Forum 裁决书明确引用「**Paragraph 12** of the Rules stipulates: In addition to the complaint and the response, the Panel may request, in its sole discretion, further statements or documents from either of the Parties.」
- 同一裁决书引用「**Paragraph 14** of the Rules stipulates: (a) In the event that a Party, in the absence of exceptional circumstances, does not comply with any of the time periods established by these Rules or the Panel, the Panel shall proceed to a decision on the complaint.」

以 12 = Further Statements、14 = Default 定位，可推出 15 = Panel Decisions，故 RDNH 声明条款为 **15(e)**，与站点引用一致。

---

## 三、「二十（20）日」是否为日历日

**结论：是日历日。站点表述「二十（20）个日历日」正确，未修改。**

规则 5(a) 原文只写 `twenty (20) days`，未写 calendar；而同一规则在 3(c)、4(b)、5(b)、6(a)、6(d) 等处对「日历日」均明确写作 `calendar days`，对「工作日」写作 `business days`。单看 5(a) 条文存在解释空间。

**决定性依据**：ADR Forum 裁决书 `Denver Newspaper Agency v. Jobing.com LLC` 中，Bernstein 专家组的附随意见明确写道：

> "This interpretation is consistent with the fact that **the 20 days provided by the Rules are calendar days, rather than business days.** Because the 20 days for submission of a response are calculated without regard to weekends and holidays, it is common for responses to be due on weekends and holidays."

另 WIPO 官方 UDRP Guide 亦表述为 "The Respondent has 20 days from the date of commencement of the proceeding to submit a Response"（未限定工作日）。

---

## 四、本轮记录到的一次 AI 摘要错误（警示）

抓取 `udrp-rules-2015-03-11-en` 页面时，抓取工具返回的 **AI 摘要**给出了系统性错误的条款编号，包括：

- 声称「第 15 条名为 Default，其下仅有 (a)(b) 两段，**不存在 15(e)**」
- 声称「编号 15(e) 处实为第 16 条 Panel Decisions 的 (e)」
- 声称「4(f) 实际对应第 3 条 The Complaint」

**经原文逐条核对，上述三条结论全部错误**，站点原有的 4(f) 与 15(e) 引用是正确的。原因推测为该页面把条款标题与正文分离渲染，AI 摘要在还原层级时发生了整体错位。

**纪律**：条文编号必须回原文或公开裁决书的引注核对，不得采信抓取工具的 AI 摘要（已写入 `DECISIONS.md` D12）。
