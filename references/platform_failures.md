# Platform And Dependency Failure Playbook

[English](platform_failures.md) | [中文](platform_failures.zh-CN.md)

## Windows And PowerShell

- Avoid stdin heredocs or pipelines for Python scripts containing Chinese paths. Write a UTF-8 `.py` file and run it.
- Use `-LiteralPath` for paths with Chinese characters or spaces.
- Avoid wildcard copying with fragile paths; enumerate files explicitly.
- Do not rely on `conda activate` inside agent shells. Prefer `{conda_python}` absolute paths.
- For long-running local services, validate with an HTTP probe. If `Start-Process` is unstable, use `Start-Job` and clean it up.

## Project Environment Versus Document Environment

Use the user-provided `{conda_python}` for project running, tests, and metrics. If it lacks document packages such as `python-docx`, use an available document runtime only for report generation and clearly record the separation.

## Common Course-Specific Checks

- C++: immediately check compiler candidates such as `{conda_env}/Library/bin/g++.exe`, `g++`, `clang++`, and `cl`. If CMake fails because Make is missing, fall back to direct compiler commands.
- NLP/LLM: inspect actual versions of `transformers`, `torch`, and related packages before writing code. Local model paths used by HuggingFace tools should be ASCII-only when possible.
- Mixed Chinese-English tokenization: Python `str.isalpha()` treats CJK characters as letters; use ASCII checks when implementing simple English acronym tokenizers.

## Screenshot And PDF Fallbacks

Screenshot levels:

- Level 1: real browser screenshot from the running app.
- Level 2: local service/API verified, but browser unavailable; provide a clearly labeled deterministic layout preview.
- Level 3: source files only; record that runtime verification is incomplete.

PDF levels:

- Word COM or `docx2pdf` on Windows with Microsoft Word.
- LibreOffice `soffice --headless --convert-to pdf`.
- If neither exists, deliver DOCX with structural QA and record the PDF limitation.

Never label a diagram or preview as a screenshot unless it came from a real rendered page.
