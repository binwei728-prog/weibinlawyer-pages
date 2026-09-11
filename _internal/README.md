# _internal —— 不发布目录

本目录存放**不对外公开**的项目文件：项目记忆四件套（`PROJECT_CONTEXT.md`、`CURRENT_STATUS.md`、`TODO.md`、`DECISIONS.md`）、上线运维文档与构建/运维脚本。

## 为什么放在这里

本仓库 `main` 分支根目录是 GitHub Pages 的发布源，站点为 `https://weibinlawyer.com`，**根目录下的任何文件都会对外可读**。

本网站由 GitHub Pages 的 Jekyll 构建发布，而 Jekyll 默认忽略以下划线（`_`）开头的目录，因此 `_internal/` 不会被复制到发布产物中，目录内文件不会出现在公网。

> 注意：仓库中**没有** `.nojekyll` 文件，Jekyll 构建处于启用状态，这是本排除机制生效的前提。若将来新增 `.nojekyll`，本目录会立刻变为公网可读。

## 目录内容

| 文件 | 用途 |
|---|---|
| `CURRENT_STATUS.md` / `PROJECT_CONTEXT.md` / `TODO.md` / `DECISIONS.md` | 项目记忆四件套（跨对话交接面） |
| `README-上线说明.md` / `上线前替换信息.md` / `上线完成记录.md` / `网站自动更新方案.md` / `腾讯云上线操作清单.md` | 历史上线与运维文档（部分已被 GitHub Pages 方案取代） |
| `replace-domain.ps1` | 早期域名替换脚本 |
| `update_structured_data.py` | 结构化数据生成脚本 |

## 修改规则

- 不要把本目录的文件移回仓库根目录。
- 新增任何不需要公网可读的文件，一律放入本目录。
