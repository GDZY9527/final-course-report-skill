# Smart Defaults

[English](smart_defaults.md) | [中文](smart_defaults.zh-CN.md)

## Goal

Make the skill useful from a short prompt. Infer safe defaults where possible, and ask only when missing information would block or materially change the result.

## Minimum Usable Prompt

```text
Use this skill to generate a final course report for {course_name}.
Template: {template_docx}
Conda Python: {conda_python}
Student fields: {student_name}, {student_id}, {class}, {teacher}
```

Optional:

```text
Project direction: ...
Target course directory: ...
```

## Inference Policy

Infer before asking:

- If project direction is missing, choose a compact deliverable project that exercises the course's core concepts and can produce real results.
- If target course directory is missing, propose or create `{workspace}/{course_name}` after confirming the base directory is writable or user-approved.
- If output filename is missing, use `{course_name}-{student_id}-{student_name}.docx` when student fields are known.
- If the course is not obviously pure hardware, include a complete frontend.
- If the intended advanced stack is unavailable, choose a local baseline and document the intended route as future work.

Ask only when:

- the template path is missing and cannot be discovered
- conda Python path is missing and execution is required
- student/cover fields are missing before final report generation
- multiple existing course directories or templates are equally plausible
- the course may be pure hardware and frontend requirements are ambiguous

## Course-Type Project Heuristics

- Programming/OOP: management system, simulation platform, compiler/interpreter mini tool, data-structure visualization, or algorithm demo with frontend dashboard.
- Database: CRUD management system, analytics dashboard, data import/export, query visualization, SQLite fallback when server DB is unavailable.
- AI/ML/NLP/CV: model service or baseline pipeline plus web demo, metrics dashboard, prediction examples, confusion matrix or evaluation chart.
- LLM/Agent: RAG, tool-use agent, prompt evaluation system, knowledge-base QA, offline fallback plus frontend.
- Software engineering: requirements/task/defect/project management system with workflow states, charts, and tests.
- Networking/security: monitoring dashboard, packet/log analyzer, rule simulator, local dataset fallback.
- IoT/software-hardware: sensor data simulator or hardware input reader plus monitoring/configuration frontend.
- Pure hardware: provide hardware design, test plan, measurements, diagrams, and report assets; frontend is optional unless software monitoring/control exists.

## Naming Defaults

Use readable ASCII project folder names when portability matters:

- `{course_slug}_project`
- `{course_slug}_report_assets`
- `{course_slug}_delivery`

Keep the human-facing report title in Chinese when the course is Chinese.

## First-Run Output

When using inferred defaults, state them clearly before or while executing:

- chosen project direction
- target directory
- frontend/backend stack
- fallback plan
- expected result files
