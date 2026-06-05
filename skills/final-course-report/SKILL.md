---
name: final-course-report
description: Generate complete final course reports and supporting deliverable projects. Use when Codex needs to create or update a final course report, course summary report, Word/PDF report, report figures, project screenshots, reproducible practice project, frontend/backend course project, or delivery package for a course assignment.
---

# Final Course Report

## Overview

Use this skill to produce a complete course final-report package: a real runnable project, complete frontend/backend when software is involved, verified result assets, academic-style figures, Word/PDF report content, references, and a cleaned delivery package.

This skill is portable. The repository root also contains `AGENTS.md` for non-Codex agents. The shared reference files live at `../../references` relative to this file.

## Required Inputs

Before final report generation, collect or infer:

- Course name.
- Optional project direction. If omitted, infer a deliverable project from the course's core concepts.
- Optional target course directory: `{course_dir}`. If omitted, propose or create one from the course name under the current workspace or user-approved base directory.
- Word template path: `{template_docx}`.
- Conda Python path: `{conda_python}`.
- Student name, student ID, class, teacher, and required output filename.
- Whether the course is purely hardware-only. If not purely hardware-only, require a complete frontend for the software portion.

## Workflow

1. Inspect the course directory, template document, existing project files, and user constraints.
2. Plan the project and report structure using `../../references/report_workflow.md`.
3. Infer missing project and directory defaults using `../../references/smart_defaults.md`.
4. Build or update the project according to `../../references/project_contract.md`.
5. For software and software-hardware projects, implement frontend requirements from `../../references/frontend_quality.md`.
6. Handle conda and dependency rules from `../../references/environment.md`.
7. Generate academic-style and deterministic figures using `../../references/visual_rules.md`.
8. Write the report using real project outputs, originality rules, and references from `../../references/originality_and_sources.md`.
9. Apply strict delivery gates and packaging rules from `../../references/delivery_quality.md`.
10. If moving between machines or agents, follow `../../references/portability.md`.

## Non-Negotiable Rules

- Do not fabricate project success, test results, metrics, screenshots, API usage, frontend behavior, or code snippets.
- Prefer useful inference over asking. Ask only for facts that are required, cannot be discovered, and would be risky to assume.
- Except for purely hardware-only courses, every new project must include complete frontend and backend or equivalent software layers.
- Older NLP examples without a frontend are historical limitations only; new NLP projects must include frontend/backend delivery.
- If network, API access, model downloads, compilers, browser screenshots, or dependencies are unavailable, provide a runnable offline fallback when possible and record limitations honestly.
- The user creates conda environments and installs dependencies manually. Write `requirements.txt` and clear setup instructions; do not assume packages are installed.
- Use UTF-8 for Chinese Markdown, JSON, CSV, and text files.
- Ask before final packaging which generated files should be excluded.

## Reference Selection

- Read `course_patterns.md` only when choosing project shapes or adapting from prior C++, LLM app, or NLP reports.
- Read `smart_defaults.md` whenever the user gives only a course name, omits a project direction, or omits a target directory.
- Read `visual_rules.md` whenever generating or inserting figures.
- Read `frontend_quality.md` for every non-pure-hardware project.
- Read `delivery_quality.md` before final checks or packaging.
