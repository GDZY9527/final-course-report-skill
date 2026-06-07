# 可迁移性

[English](portability.md) | [中文](portability.zh-CN.md)

## 跨智能体入口

- Codex：`skills/final-course-report/SKILL.md`
- Claude Code、OpenCode、OpenClaw 等通用智能体：仓库根目录 `AGENTS.md`

详细说明统一使用普通 Markdown，避免绑定某个产品的专有工具。

## 路径占位符

不要在可复用文件中写死原作者本机路径。统一使用：

- `{course_dir}`
- `{template_docx}`
- `{project_dir}`
- `{conda_python}`
- `{student_name}`
- `{student_id}`

## 跨主机安装方式

推荐方式：

- 长期同步：`git clone` 整个仓库。
- 离线迁移：下载 GitHub Release zip 并完整解压。

不建议只复制 `skills/final-course-report` 子目录，因为它默认引用仓库根目录的 `references/`，并依赖 `scripts/audit_generated_report.py` 进行质量审计。

如果目标智能体必须使用单目录 skill 安装方式，则安装包应包含：

- `SKILL.md`
- `agents/`
- 完整 `references/`
- `scripts/audit_generated_report.py`

并确认 `SKILL.md` 中的引用路径与安装后的实际结构一致。常见修正是把 `../../references/` 改为 `references/`。

## 迁移自检

复制或克隆到其他主机后，检查：

- 仓库可读取
- 目标课程目录存在或可创建
- 模板 docx 存在
- conda Python 路径存在
- 有写入权限
- 依赖已列出
- 外部工具已列出
- examples 不包含私人数据

## 版本管理

稳定版本使用 Git tag：

```text
v0.1.0
v0.2.0
```

从 tag 导出 zip release 用于离线迁移。

在示例、模板和 references 完成脱敏前，建议保持仓库私有。
