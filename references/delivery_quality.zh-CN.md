# 交付质量

[English](delivery_quality.md) | [中文](delivery_quality.zh-CN.md)

## 严格质量门槛

最终交付前验证：

- 项目可运行，或限制被如实记录
- 后端/核心逻辑产生真实输出
- 前端能打开，并展示真实项目数据或确定性结果数据
- 截图完整清晰
- 配图符合学术技术图风格
- 指标或测试来自真实文件
- Word 报告可打开和渲染
- 生成 PDF 时 PDF 可读
- 目录、页眉页脚、图题表题、表格和附录已检查
- 没有未处理占位符

## 交付包

默认交付包包含：

- 最终 `.docx`
- 可用时包含最终 `.pdf`
- 项目源码
- `results/`
- `README.md`
- `requirements.txt`
- 运行脚本或命令说明
- 图表清单
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

除非用户明确要求，不要删除用户文件。

## 自动审计

如果 Python 和 Pillow 可用，运行 `scripts/audit_generated_report.py {course_dir}`。除非用户明确接受限制，否则审计失败项应视为阻塞。

默认硬性阻塞项：

- DOCX 正文密度低于配置门槛。
- DOCX 嵌入媒体数低于配置门槛。
- PNG 存在暗色/打印风险。
- 新报告中残留旧模板关键词。
- 项目图片已生成但没有嵌入报告。

用户未要求压缩包时，可以交付目录形态。只有在展示排除清单后才创建 zip。
