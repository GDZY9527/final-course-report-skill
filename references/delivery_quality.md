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
