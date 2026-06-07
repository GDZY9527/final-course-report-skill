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
2. Infer missing project and directory defaults using `../../references/smart_defaults.md`.
3. Plan a course-specific project using `../../references/project_contract.md` and reject generic template reuse.
4. Plan report density, chapter evidence, and appendices using `../../references/report_density.md`.
5. Adapt the Word template using `../../references/template_adaptation.md` before writing body content.
6. Build or update the project according to `../../references/project_contract.md`.
7. For software and software-hardware projects, implement frontend requirements from `../../references/frontend_quality.md`.
8. Handle conda, platform, and dependency rules from `../../references/environment.md` and `../../references/platform_failures.md`.
9. Maintain an execution log using `../../references/execution_log.md`.
10. Generate and embed academic-style, print-friendly deterministic figures using `../../references/visual_rules.md`.
11. Write the report using real project outputs, originality rules, and references from `../../references/report_workflow.md` and `../../references/originality_and_sources.md`.
12. Apply strict delivery gates, run available audits, and package only after confirmation using `../../references/delivery_quality.md`.
13. If moving between machines or agents, follow `../../references/portability.md`.

## Non-Negotiable Rules

- Do not fabricate project success, test results, metrics, screenshots, API usage, frontend behavior, PDF export, page count, or code snippets.
- Prefer useful inference over asking. Ask only for facts that are required, cannot be discovered, and would be risky to assume.
- Except for purely hardware-only courses, every new project must include complete frontend and backend or equivalent software layers.
- Older NLP examples without a frontend are historical limitations only; new NLP projects must include frontend/backend delivery.
- If network, API access, model downloads, compilers, browser screenshots, or dependencies are unavailable, provide a runnable offline fallback when possible and record limitations honestly.
- The user creates conda environments and installs dependencies manually. Write `requirements.txt` and clear setup instructions; do not assume packages are installed.
- Use UTF-8 for Chinese Markdown, JSON, CSV, and text files.
- Ask before final packaging which generated files should be excluded.
- Do not deliver thin reports: satisfy the report-density gate or explicitly obtain user acceptance for a smaller report.
- All printable report figures and screenshots must use light backgrounds; dark images are blockers.
- Generated figures must be embedded into the DOCX, not merely saved in `results/`.

## Reference Selection

Required by phase:

- Start: `smart_defaults.md`, `project_contract.md`, `report_density.md`, and `template_adaptation.md`.
- Environment and tools: `environment.md` and `platform_failures.md`.
- Frontend: `frontend_quality.md` for every non-pure-hardware project.
- Figures: `visual_rules.md` before generating or inserting any figure.
- Writing: `report_workflow.md` and `originality_and_sources.md`.
- Logging: `execution_log.md` throughout long tasks.
- Final checks: `delivery_quality.md`; run `scripts/audit_generated_report.py` when available.
- Course patterns: `course_patterns.md` only when choosing or adapting project shapes.
- Portability: `portability.md` when moving between machines or agents.
