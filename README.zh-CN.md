# 期末结课报告 Skill

[English](README.md) | [中文](README.zh-CN.md)

这是一个可迁移的智能体能力包，用于生成完整期末结课报告和配套可交付实践项目，适配 Codex、Claude Code、OpenCode、OpenClaw 等主流编码智能体。

## 仓库提供什么

- Codex 原生 skill：`skills/final-course-report/SKILL.md`。
- 通用智能体入口：`AGENTS.md`，供 Claude Code、OpenCode、OpenClaw、Codex 等读取。
- 聚焦的参考规范：报告写作、项目交付、前端质量、配图质量、环境处理、打包交付和迁移规范。
- 轻量示例和模板，不包含私人课程成品。

## 推荐分发方式

使用 Git 仓库作为长期维护渠道，稳定版本导出 zip 用于离线迁移。

- 在示例和模板完全脱敏前，建议保持仓库私有。
- 稳定版本使用 tag，例如 `v0.1.0`。
- 从 tag 导出 zip release。
- 不提交真实学生信息、报告 `.docx`/`.pdf`、项目压缩包、API Key、conda 环境或生成后的课程作业成品。

## 快速开始

1. 将本仓库复制或克隆到目标主机。
2. 使用通用智能体时，先读取 `AGENTS.md`。
3. 使用 Codex 时，安装或引用 `skills/final-course-report`。
4. 向智能体提供：
   - 课程名称
   - 项目方向
   - 目标课程目录
   - Word 模板路径
   - conda Python 路径
   - 学生和封面字段
5. 让智能体创建项目、运行检查、生成报告素材、撰写报告并准备经过检查的交付包。

## 可迁移路径占位符

不要在可复用文件中写死本机路径，统一使用：

- `{course_dir}`
- `{template_docx}`
- `{project_dir}`
- `{conda_python}`
- `{student_name}`
- `{student_id}`

所有 Markdown、JSON、CSV 和文本文件建议使用 UTF-8。
