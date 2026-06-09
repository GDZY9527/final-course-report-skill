# 前端框架与消费级交付门禁

[English](frontend_framework.md) | [中文](frontend_framework.zh-CN.md)

## 结论

Flask 本身不是问题，但 Flask + Jinja + 少量 CSS 很容易退化成课堂 demo。Python Web 项目默认使用 Django，除非用户明确指定其他技术栈。

## 默认框架

非纯硬件课程使用 Python Web 技术时：

- 默认使用 Django。
- 包含 Django project、至少一个业务 app、templates、static、URL 路由、views、forms 或等价输入校验、错误页面。
- 需要 API 时使用 Django views 或 Django REST Framework。
- 不允许把单文件脚本当作完整后端。
- 只有用户明确要求，或项目确实是轻量 API 原型时，才允许 Flask；即便使用 Flask，前端质量门禁仍然适用。

## 消费级前端标准

前端不能只是标题、卡片、表单和表格。必须包含：

- 项目专属工作台，而不是通用蓝色 dashboard。
- 清晰信息架构：导航、主工作区、详情区、结果区、状态区。
- 至少 3 个真实业务页面或等价视图。
- loading、empty、success、failure、validation、backend-error 状态。
- 真实数据驱动的图表、表格、详情面板和操作反馈。
- 至少一个项目专属可视分析面，例如热力图、时间线、对比面板、关系图、流程追踪或交互式指标面板。
- 页面文案使用项目领域词汇、业务流程和结果对象，不能只写泛泛的“dashboard/card/form”。
- 真实浏览器截图：主页面、一次成功输入后的操作页、一个指标/结果页。
- 桌面端和移动端响应式检查。
- 可访问性：label、语义按钮、focus 状态和对比度。
- 视觉设计要绑定项目领域。

## 禁止

- 单文件 Flask + Jinja + 粗糙 CSS 作为完整前后端。
- 所有课程都使用同一套蓝色 dashboard/card grid。
- 页面稀疏、大片空白、工作流极少的 demo。
- 前端设计 brief 里写了某个功能，但 templates/CSS/JS 没有实现。
- 未处理的 JavaScript 错误。
- UI 文本乱码。
- 没有真实浏览器运行截图却声称已经截图。

## 验证

交付前记录：

- 启动命令。
- 访问 URL。
- 页面清单。
- 真实浏览器截图路径。
- 浏览器控制台错误。
- 移动端 viewport 检查。
- 每张截图用于报告的哪个位置；如果未使用，说明原因。

无法运行浏览器截图时，如实记录限制。
