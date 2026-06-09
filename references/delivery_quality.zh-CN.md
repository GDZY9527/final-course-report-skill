# 交付质量

[English](delivery_quality.md) | [中文](delivery_quality.zh-CN.md)

## 严格质量门禁

最终交付前必须验证：

- 项目可以真实运行，或限制被如实记录。
- 后端/核心逻辑产生真实输出。
- 前端可以打开，并展示真实项目数据或确定性结果数据。
- 截图完整清晰，不存在浏览器错误遮挡关键功能。
- 配图符合学术技术图风格，背景适合打印。
- 指标或测试结果来自真实文件。
- Word 报告可以打开并渲染正常。
- 生成 PDF 时，PDF 必须可读。
- 目录、页眉页脚、图题表题、表格和附录已经检查。
- 没有未处理的占位符、提示词痕迹或乱码。

## 交付包

默认交付包包含：

- 最终 `.docx`
- 可用时包含最终 `.pdf`
- 项目源码
- `results/`
- `README.md`
- `requirements.txt`
- 运行脚本或命令说明
- 生成图表清单
- 验证摘要

打包前先给出排除清单并等待确认。

建议排除：

- `__pycache__/`
- `.pytest_cache/`
- `node_modules/`
- 构建缓存
- `.obj`、`.exe`、`.pdb`、`.ilk`
- 旧截图
- 临时日志
- secrets 和 `.env`
- 大型草稿 docx/pdf
- Word 临时文件 `~$*.docx`
- `.pyc`、`.pyo`

除非用户明确要求，不要删除用户文件。

## 自动审计

如果 Python 和 Pillow 可用，运行 `scripts/audit_generated_report.py {course_dir}`。除非用户明确接受限制，否则审计失败项应视为阻塞。

推荐严格命令：

```powershell
python scripts/audit_generated_report.py {course_dir} `
  --require-project-brief `
  --require-frontend-brief `
  --require-heading-styles `
  --require-fresh-toc `
  --require-single-final-docx `
  --require-django-frontend `
  --require-frontend-screenshots `
  --forbid-placeholders
```

默认硬性阻塞项：

- DOCX 正文密度低于配置门槛。
- DOCX 嵌入媒体数低于配置门槛。
- PNG 存在暗色/打印风险。
- 新报告中残留旧模板关键词。
- 项目图片已经生成但没有嵌入报告。
- 章节标题只是 `正文/Normal` 段落改字体，而不是 Word 真实标题样式。
- 目录仍包含模板内容或旧章节名称。
- 交付根目录中存在多个最终报告 DOCX。
- 附录正文包含生成填充内容；默认只保留附录标题。
- 英文术语括号解释过多，导致正文看起来像 AI 生成。
- 生成的 Markdown、Python、HTML、JSON 或日志文件存在乱码、编码损坏或未处理占位符。
- Python Web 项目在要求 Django 时仍使用 Flask 单文件/Jinja demo 结构。
- 真实前端/浏览器截图少于 3 张。
- 运行日志中残留 `To be filled`、`TODO` 等未执行占位符。
- Word 临时文件 `~$*.docx`、`__pycache__/`、`.pyc` 或误生成的零字节杂项文件进入交付包。

用户未要求压缩包时，可以交付目录形式。只有在展示排除清单后才创建 zip。
