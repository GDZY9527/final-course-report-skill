# 环境约定

[English](environment.md) | [中文](environment.zh-CN.md)

## Conda 约定

用户手动创建 conda 环境并安装依赖。智能体不应静默安装包。

运行或记录命令时使用用户提供的 Python 路径：

```powershell
{conda_python} src\preprocess.py
{conda_python} web_app.py
```

用户提供路径示例：

```text
{conda_root}\envs\{course_env}\python.exe
{conda_python}
```

## 依赖处理

始终编写：

- `requirements.txt`
- README 依赖说明
- 最终答复中的依赖摘要

如果缺少包，更新 `requirements.txt` 并告诉用户需要安装什么。不要假装运行成功。

## 外部工具

需要非 Python 工具时要明确列出：

- MSVC 或 g++
- CMake
- Graphviz
- 浏览器截图运行时
- 数据库服务
- 模型/API 凭据

工具不可用时，尽量使用真实本地兜底方案，并记录限制。
