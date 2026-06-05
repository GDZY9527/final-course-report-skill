# 期末结课报告智能体指南

[English](AGENTS.md) | [中文](AGENTS.zh-CN.md)

当用户需要期末报告、结课报告、课程总结报告、配套实践项目、Word/PDF 报告、报告配图、项目截图或可复用报告生成流程时，使用本指南。

## 工作原则

- 先构建真实可运行、可复现的项目，再撰写项目实践章节。
- 除纯硬件课程外，所有新的纯软件或软硬结合项目都必须包含完整前端和后端，或等价的软件分层。
- 早期 NLP 示例没有前端只作为历史限制记录，后续新项目不得沿用该形态。
- 不得虚构实验结果、截图、代码片段、指标、构建成功、前端行为或 API 可用性。
- 当网络、API、模型下载、浏览器截图、编译器或依赖不可用时，优先提供可运行的离线降级方案，并在报告和交付说明中如实记录限制。
- 用户手动创建 conda 环境并安装依赖。智能体只负责编写 `requirements.txt` 和依赖说明，不默认静默安装包。
- 生成最终报告前，询问姓名、学号、班级、教师、课程、模板路径、目标目录和 conda Python 路径。
- 中文 Markdown、JSON、CSV 和文本文件默认使用 UTF-8。

## 必须执行的流程

1. 检查目标目录、模板文档、现有项目文件和用户约束。
2. 创建或更新规范级项目，包括清晰模块、前端、后端/核心逻辑、数据、README、requirements、运行脚本、测试和 results。
3. 使用 `{conda_python}` 运行或记录精确验证命令。
4. 生成确定性的项目素材：目录树、架构/系统流程、代码截图、前端截图、指标图、日志和结果表。
5. 基于模板和真实项目输出撰写报告。
6. 默认加入参考文献或资料来源。
7. 有文档工具时，渲染并目检报告。
8. 打包前给出排除清单并等待确认。

## 参考文件

按需读取以下文件：

- `references/report_workflow.md`：报告流程和章节结构。
- `references/project_contract.md`：项目产物与规范级交付要求。
- `references/frontend_quality.md`：强制前端要求。
- `references/visual_rules.md`：学术论文风配图要求。
- `references/environment.md`：conda 与依赖处理。
- `references/delivery_quality.md`：质量门槛和打包规范。
- `references/originality_and_sources.md`：原创表达和参考文献规则。
- `references/course_patterns.md`：已有 C++、大模型应用、NLP 报告经验。
- `references/portability.md`：跨主机、跨智能体迁移规范。

## 最终输出要求

最终答复应列出：

- 报告路径
- 项目路径
- 使用的环境路径
- 生成的图表
- 验证命令和结果
- 已知限制
- 交付包内容或待确认的打包清单
