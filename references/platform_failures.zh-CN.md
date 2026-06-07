# 平台与依赖故障处理

[English](platform_failures.md) | [中文](platform_failures.zh-CN.md)

## Windows 与 PowerShell

- 避免通过 stdin heredoc 或管道传递包含中文路径的 Python 脚本。优先写入 UTF-8 `.py` 文件后再运行。
- 中文或含空格路径使用 `-LiteralPath`。
- 脆弱路径下避免通配符复制，优先显式枚举文件。
- 不依赖智能体 shell 中的 `conda activate`。优先使用 `{conda_python}` 绝对路径。
- 长驻本地服务必须用 HTTP 探针验证。`Start-Process` 不稳定时使用 `Start-Job`，验证后清理。

## 项目环境与文档环境分离

用户提供的 `{conda_python}` 用于项目运行、测试和指标生成。若该环境缺少 `python-docx` 等文档依赖，可使用可用的文档运行时生成报告，但必须明确记录“项目运行环境”和“文档生成环境”的分离。

## 常见课程专项检查

- C++：立即检查 `{conda_env}/Library/bin/g++.exe`、`g++`、`clang++`、`cl` 等编译器候选。若 CMake 因缺少 Make 失败，直接回退到编译器命令行。
- NLP/LLM：写代码前检查 `transformers`、`torch` 等实际版本。本地模型路径用于 HuggingFace 工具时尽量使用纯 ASCII 路径。
- 中英文混合分词：Python `str.isalpha()` 会把 CJK 字符视为字母；实现英文缩写分词时要加 ASCII 判断。

## 截图与 PDF 降级等级

截图等级：

- Level 1：真实运行页面的浏览器截图。
- Level 2：本地服务/API 已验证，但浏览器不可用；提供明确标注的确定性布局预览。
- Level 3：仅源码存在；记录运行验证不完整。

PDF 等级：

- Windows + Microsoft Word：Word COM 或 `docx2pdf`。
- LibreOffice：`soffice --headless --convert-to pdf`。
- 两者都不可用：交付 DOCX 和结构性 QA，并记录 PDF 限制。

不得把架构图、预览图、设计稿称为“截图”，除非它确实来自真实渲染页面。
