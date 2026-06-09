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
- Project direction. This is required as either a user-defined direction or an explicit statement such as "no clear project goal; agent should design a unique project." Only self-select a project when the user explicitly allows it this way.
- Optional target course directory: `{course_dir}`. If omitted, propose or create one from the course name under the current workspace or user-approved base directory.
- Word template path: `{template_docx}`.
- Conda Python path: `{conda_python}`.
- Optional student name, student ID, class, teacher, and required output filename. Do not force these at the beginning; leave cover fields for the user if omitted.
- Whether the course is purely hardware-only. If not purely hardware-only, require a complete frontend for the software portion.

## Workflow

1. Inspect the course directory, template document, existing project files, and user constraints.
2. Infer directory defaults using `../../references/smart_defaults.md`; infer a project only when the project direction explicitly says the user has no clear project goal and authorizes agent design.
3. Plan a new, non-reused project using the user-provided direction, `../../references/project_uniqueness.md`, and `../../references/project_contract.md`; create `results/project_brief.md` before coding.
4. Plan report density using `../../references/report_density.md`; density must come from main chapters, not appendix padding.
5. Adapt the Word template structure using `../../references/template_adaptation.md`, then apply the dedicated school writing standard from `../../references/chengdu_neusoft_report_standard.zh-CN.md` and `../../references/docx_formatting.md` before writing body content.
6. Build or update the project according to `../../references/project_contract.md`.
7. For software and software-hardware projects, design a project-specific frontend using `../../references/frontend_quality.md` and `../../references/frontend_design.md`.
8. Handle conda, platform, and dependency rules from `../../references/environment.md` and `../../references/platform_failures.md`.
9. Maintain an execution log using `../../references/execution_log.md`.
10. Generate and embed academic-style, print-friendly deterministic figures using `../../references/visual_rules.md`.
11. Write only the main report body and references using `../../references/report_workflow.md`, `../../references/originality_and_sources.md`, and `../../references/appendix_policy.md`; leave appendix body empty unless the user asks otherwise.
12. Apply strict delivery gates, run available audits, and package only after confirmation using `../../references/delivery_quality.md`.
13. If moving between machines or agents, follow `../../references/portability.md`.

## Non-Negotiable Rules

- Do not fabricate project success, test results, metrics, screenshots, API usage, frontend behavior, PDF export, page count, or code snippets.
- Prefer useful inference over asking, but do not invent a project direction when the field is missing. Ask for a direction, or ask whether the user authorizes the agent to design a unique project.
- Except for purely hardware-only courses, every new project must include complete frontend and backend or equivalent software layers.
- Older NLP examples without a frontend are historical limitations only; new NLP projects must include frontend/backend delivery.
- If network, API access, model downloads, compilers, browser screenshots, or dependencies are unavailable, provide a runnable offline fallback when possible and record limitations honestly.
- The user creates conda environments and installs dependencies manually. Write `requirements.txt` and clear setup instructions; do not assume packages are installed.
- Use UTF-8 for Chinese Markdown, JSON, CSV, and text files.
- Ask before final packaging which generated files should be excluded.
- Do not deliver thin reports: satisfy the report-density gate or explicitly obtain user acceptance for a smaller report.
- All printable report figures and screenshots must use light backgrounds; dark images are blockers.
- Generated figures must be embedded into the DOCX, not merely saved in `results/`.
- Do not reuse example or prior-test projects. Every report needs a new project and a `results/project_brief.md` uniqueness record.
- Do not author appendix body content by default; create only the appendix heading unless the user explicitly asks.
- Follow `chengdu_neusoft_report_standard.zh-CN.md` for all Word fonts, sizes, colors, headings, margins, headers/footers, captions, formulas, and code blocks. Arbitrary colorful headings or mismatched body text are blockers.

## Reference Selection

Required by phase:

- Start: `smart_defaults.md`, `project_uniqueness.md`, `project_contract.md`, `report_density.md`, `template_adaptation.md`, `chengdu_neusoft_report_standard.zh-CN.md`, `docx_formatting.md`, and `appendix_policy.md`.
- Environment and tools: `environment.md` and `platform_failures.md`.
- Frontend: `frontend_quality.md` and `frontend_design.md` for every non-pure-hardware project.
- Figures: `visual_rules.md` before generating or inserting any figure.
- Writing: `report_workflow.md` and `originality_and_sources.md`.
- Logging: `execution_log.md` throughout long tasks.
- Final checks: `delivery_quality.md`; run `scripts/audit_generated_report.py` when available.
- Course patterns: `course_patterns.md` only when choosing or adapting project shapes.
- Portability: `portability.md` when moving between machines or agents.
