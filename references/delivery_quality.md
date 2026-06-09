# Delivery Quality

[English](delivery_quality.md) | [中文](delivery_quality.zh-CN.md)

## Strict Quality Gates

Before final delivery, verify:

- project can run or limitations are truthfully documented
- backend/core logic produces real outputs
- frontend opens and shows real project data or deterministic result data
- screenshots are complete and readable
- figures follow academic technical style
- metrics or tests come from real files
- Word report opens and renders
- PDF export is readable when generated
- table of contents, headers/footers, captions, tables, and appendices are checked
- no unresolved placeholders remain

## Delivery Package

Default package contents:

- final `.docx`
- final `.pdf` when available
- project source
- `results/`
- `README.md`
- `requirements.txt`
- run scripts or command notes
- generated figure/table inventory
- verification summary

Before packaging, show an exclusion list for confirmation.

Recommended exclusions:

- `__pycache__/`
- `.pytest_cache/`
- `node_modules/`
- build caches
- `.obj`, `.exe`, `.pdb`, `.ilk`
- old screenshots
- temporary logs
- secrets and `.env`
- large draft docx/pdf versions

Do not delete user files unless explicitly requested.

## Automated Audit

Run `scripts/audit_generated_report.py {course_dir}` when Python and Pillow are available. Treat failures as blockers unless the user explicitly accepts the limitation.

Recommended strict command:

```powershell
python scripts/audit_generated_report.py {course_dir} `
  --require-project-brief `
  --require-frontend-brief `
  --require-heading-styles `
  --require-fresh-toc `
  --require-single-final-docx `
  --require-django-frontend `
  --require-frontend-screenshots `
  --forbid-placeholders
```

Default hard blockers:

- DOCX text density below the configured threshold.
- DOCX embedded media below the configured threshold.
- Dark/print-risk PNG figures.
- Old template keywords remain in a new report.
- Generated project figures exist but are not embedded in the report.
- Chapter/section headings are only formatted text in `Normal` style instead of real Word heading styles.
- The generated table of contents still contains template content or stale chapter names.
- Appendix body contains generated filler; by default only the appendix title should remain.
- More than one final report DOCX remains in the delivery root.
- Excessive English terminology parentheticals make the prose look AI-generated.
- Generated Markdown/Python/HTML/JSON/log files contain mojibake, encoding damage, or unresolved placeholders.
- Python web projects use Flask/single-file Jinja demo structure when Django was required.
- Fewer than three real frontend/browser screenshots are recorded.
- Runtime logs contain `To be filled`, `TODO`, or other non-executed placeholders.
- Temporary Word/cache/stray files such as `~$*.docx`, `__pycache__/`, `.pyc`, or accidental zero-byte junk files enter the delivery package.

Directory delivery is acceptable when the user did not ask for a zip. Only create a zip after showing the exclusion list.
