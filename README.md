# Final Course Report Skill

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

1. Copy or clone this repository to a target machine.
2. Open `AGENTS.md` if using a general agent.
3. For Codex, install or reference `skills/final-course-report`.
4. Provide the agent with:
   - course name
   - project direction
   - target course directory
   - Word template path
   - conda Python path
   - student and cover-page fields
5. Let the agent create the project, run checks, generate report assets, write the report, and prepare a reviewed delivery package.

## Portability placeholders

Use placeholders instead of hard-coded local paths:

- `{course_dir}`
- `{template_docx}`
- `{project_dir}`
- `{conda_python}`
- `{student_name}`
- `{student_id}`

All Markdown, JSON, CSV, and text files should use UTF-8.
