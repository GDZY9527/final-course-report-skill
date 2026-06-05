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
