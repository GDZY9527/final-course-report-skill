# Portability

[English](portability.md) | [中文](portability.zh-CN.md)

## Cross-Agent Entry Points

- Codex: `skills/final-course-report/SKILL.md`
- Claude Code, OpenCode, OpenClaw, and similar agents: root `AGENTS.md`

Keep all detailed instructions in plain Markdown so agents can read the repository without product-specific tooling.

## Path Placeholders

Do not hard-code the original author's machine paths in reusable files. Use:

- `{course_dir}`
- `{template_docx}`
- `{project_dir}`
- `{conda_python}`
- `{student_name}`
- `{student_id}`

## Migration Self-Check

After copying or cloning to another machine, check:

- repository can be read
- target course directory exists or can be created
- template docx exists
- conda Python path exists
- write permission is available
- dependencies are listed
- external tools are listed
- examples contain no private data

## Versioning

Use Git tags for stable releases:

```text
v0.1.0
v0.2.0
```

Export zip releases from tags for offline transfer.

Keep the repository private until examples, templates, and references are sanitized.
