---
published: false
---

# 项目工作约定（入口指针）

> 本文件是 Codex / WorkBuddy 的自动加载入口。**项目记忆实体文件已移至 `_internal/` 目录**（该目录以下划线开头，GitHub Pages 的 Jekyll 构建会默认忽略，不会发布到公网）。
>
> 本文件仅作入口指针，不承载项目状态；项目状态的唯一权威源在 `_internal/` 内。

## 项目记忆位置

| 文件 | 用途 |
|---|---|
| `_internal/CURRENT_STATUS.md` | 当前真实状态（顶部有「记忆同步信标」版本号） |
| `_internal/PROJECT_CONTEXT.md` | 项目定位 + 全局工作规则 + 文件路由表 + 合规红线 |
| `_internal/TODO.md` | 待办与优先级 |
| `_internal/DECISIONS.md` | 已定决策及原因 |

## 长期项目记忆规则

- 仅当当前工作目录和任务已唯一确定属于本项目时，才读取本项目记忆；禁止读取其他项目的记忆文件。
- 新任务先读 `_internal/CURRENT_STATUS.md`、`_internal/TODO.md` 和 `_internal/PROJECT_CONTEXT.md` 的「全局工作规则」；涉及历史取舍时再读 `_internal/DECISIONS.md`，其余内容按文件路由表读取。
- 每个与本项目有关的对话在开始新的实质工作前，都先读取 `_internal/CURRENT_STATUS.md` 顶部的「记忆同步信标」。若该对话未确认过当前版本、版本号与上次读取不同，或无法判断是否已同步，必须重新读取 HOT 层；涉及决策变化时再读取 `_internal/DECISIONS.md`。
- 任一对话修改四份记忆文件时，必须最后更新 `_internal/CURRENT_STATUS.md` 的版本号、更新时间和一行变更摘要；四文件全部写完后再提升版本号，使它成为其他对话判断失效与重载的统一信标。
- 用户最新指示和可验证现状优先于记忆文件；推测不得写成事实。
- 工作结束仅在有实质变化时更新对应记忆文件，避免流水账。

## 发布边界（重要）

- 本仓库同时是 GitHub Pages 的**发布源**（`main` 分支根目录直接对外，站点 `https://weibinlawyer.com`）。因此：**任何不打算公网可读的文件，一律放入 `_internal/`**，不要放在仓库根目录。
- 根目录除本文件外的 `.md` 均已清空；如需在根目录放说明文档，必须使用 `_internal/`。
- `tools/` 目录中的 `udrp-intake.html`、`enterprise-risk-intake.html` 是**线上正式页面**，不得移动或删除。
