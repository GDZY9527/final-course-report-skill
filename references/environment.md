# Environment

[English](environment.md) | [中文](environment.zh-CN.md)

## Conda Convention

The user manually creates conda environments and installs dependencies. The agent should not silently install packages.

Use the provided Python path when running or documenting commands:

```powershell
{conda_python} src\preprocess.py
{conda_python} web_app.py
```

Examples of user-provided paths:

```text
{conda_root}\envs\{course_env}\python.exe
{conda_python}
```

## Dependency Handling

Always write:

- `requirements.txt`
- README dependency section
- final response dependency summary

If a package is missing, update `requirements.txt` and tell the user what to install. Do not work around this by pretending the run succeeded.

## External Tools

Clearly list non-Python requirements when needed:

- MSVC or g++
- CMake
- Graphviz
- browser runtime for screenshots
- database server
- model/API credentials

When tools are unavailable, use a truthful local fallback if possible and record the limitation.
