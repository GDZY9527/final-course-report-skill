# Final Course Report Skill

[English](README.md) | [中文](README.zh-CN.md)

Portable instructions for generating complete final course reports and deliverable course projects with mainstream coding agents.

## What this repository provides

- A Codex skill at `skills/final-course-report/SKILL.md`.
- A generic agent entrypoint at `AGENTS.md` for Claude Code, OpenCode, OpenClaw, Codex, and similar agents.
- Focused references for report writing, project delivery, frontend quality, visual quality, environment handling, packaging, and portability.
- Lightweight examples and templates that do not include private course submissions.

## Recommended distribution

Use Git as the primary maintenance channel and export stable zip releases for offline transfer.

- Keep the repository private until examples and templates are fully sanitized.
- Tag stable versions such as `v0.1.0`.
- Export zip releases from tagged commits.
- Do not commit real student information, report `.docx`/`.pdf` files, project zips, API keys, conda environments, or generated course submissions.

## Quick start

Minimal prompt:

```text
Use this skill to generate a final course report for {course_name}.
Project direction: {project_direction}  # Or: no clear project goal; agent should design a unique project.
Template: {template_docx}
Conda Python: {conda_python}
Student fields: optional; leave cover fields blank if omitted.
```

Optional additions:

```text
Target course directory: ...
Student fields: {student_name}, {student_id}, {class}, {teacher}
```

1. Copy or clone this repository to a target machine.
2. Open `AGENTS.md` if using a general agent.
3. For Codex, install or reference `skills/final-course-report`.
4. Provide the minimum required inputs:
   - course name
   - project direction, or an explicit note such as "no clear project goal; agent should design a unique project"
   - Word template path
   - conda Python path
5. Optionally provide overrides:
   - target course directory, if the agent should not create one from the course name
   - student and cover-page fields, if you want them filled now; otherwise leave them for manual Word editing
6. If the project direction explicitly says there is no clear project goal, the agent should design a new, non-reused, deliverable project that matches the course's core concepts. If the target directory is omitted, the agent should propose or create one from the course name under the current workspace or user-approved base directory.
7. Let the agent create the project, run checks, generate report assets, write the report, and prepare a reviewed delivery package.

When the target directory is omitted, the agent should infer a sensible default instead of stopping. When project direction is missing entirely, the agent should ask for it or ask whether it may design a unique project.

## Cross-Machine Installation

Prefer `git clone` for the full repository, or download and extract the complete GitHub Release zip. Do not copy only `skills/final-course-report`; that subdirectory depends on root-level `references/`, `scripts/`, and generic agent entrypoint files.

If an agent can only install a single skill folder, copy these together:

- `skills/final-course-report/SKILL.md`
- `skills/final-course-report/agents/`
- root `references/`
- `scripts/audit_generated_report.py`

Then rewrite `../../references/` in `SKILL.md` to the installed path, usually `references/`. After installation, verify that the agent can read `AGENTS.md`, `SKILL.md`, `references/`, and the audit script.

## Portability placeholders

Use placeholders instead of hard-coded local paths:

- `{course_dir}`
- `{template_docx}`
- `{project_dir}`
- `{conda_python}`
- `{student_name}`
- `{student_id}`

All Markdown, JSON, CSV, and text files should use UTF-8.

## Quality Audit

After generating a report, run:

```powershell
python scripts/audit_generated_report.py "{course_dir}"
```

The script checks DOCX text density, embedded media count, and PNG print risk. Fix short reports, missing embedded images, and dark figures before delivery.
