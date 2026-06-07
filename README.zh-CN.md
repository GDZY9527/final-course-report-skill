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

最小提示词：

```text
使用这个 skill 为《{course_name}》生成期末结课报告。
项目方向：{project_direction}  # 或填写：暂无明确项目目标，请智能体自行设计唯一性项目。
模板：{template_docx}
Conda Python：{conda_python}
学生字段：可选；未提供时封面字段留空，最后由用户在 Word 中自行填写。
```

可选补充：

```text
目标课程目录：……
学生字段：{student_name}、{student_id}、{class}、{teacher}
```

1. 将本仓库复制或克隆到目标主机。
2. 使用通用智能体时，先读取 `AGENTS.md`。
3. 使用 Codex 时，安装或引用 `skills/final-course-report`。
4. 向智能体提供最小必需输入：
   - 课程名称
   - 项目方向；如果你没有明确目标，应明确写“暂无明确项目目标，请智能体自行设计唯一性项目”
   - Word 模板路径
   - conda Python 路径
5. 可选提供覆盖项：
   - 目标课程目录：如果不希望智能体根据课程名称自动创建目录
   - 学生和封面字段：如果希望现在填入；否则封面字段留空，最后由用户在 Word 中自行填写
6. 只有当项目方向中明确表示“暂无明确项目目标”或“请智能体自行设计”时，智能体才应根据课程核心知识自行设计一个新的、未复用的、可交付项目。如果没有提供目标目录，智能体应在当前工作区或你批准的基础目录下，根据课程名称提出或创建目录。
7. 让智能体创建项目、运行检查、生成报告素材、撰写报告并准备经过检查的交付包。

如果没有提供目标目录，智能体应自行推断合理默认值，而不是停下来等待。如果项目方向完全缺失，智能体应先询问项目方向，或询问是否允许其自行设计唯一性项目。

## 跨主机安装建议

推荐用 `git clone` 克隆整个仓库，或下载 GitHub Release 中的 zip 包后完整解压。不要只复制 `skills/final-course-report` 子目录；该子目录依赖仓库根目录的 `references/`、`scripts/` 和通用入口文档。

如果某个智能体只能安装单个 skill 子目录，必须同时复制：

- `skills/final-course-report/SKILL.md`
- `skills/final-course-report/agents/`
- 仓库根目录 `references/`
- `scripts/audit_generated_report.py`

并把 `SKILL.md` 中的 `../../references/` 改为安装后实际可访问的 `references/`。安装完成后先检查 `AGENTS.zh-CN.md`、`SKILL.md`、`references/` 和审计脚本是否都能被智能体读取。

## 可迁移路径占位符

不要在可复用文件中写死本机路径，统一使用：

- `{course_dir}`
- `{template_docx}`
- `{project_dir}`
- `{conda_python}`
- `{student_name}`
- `{student_id}`

所有 Markdown、JSON、CSV 和文本文件建议使用 UTF-8。

## 质量审计

生成报告后，可运行：

```powershell
python scripts/audit_generated_report.py "{course_dir}"
```

该脚本会检查 DOCX 正文密度、嵌入图片数量和 PNG 打印风险。报告过短、图片未嵌入或存在暗色图片时，应先修复再交付。
