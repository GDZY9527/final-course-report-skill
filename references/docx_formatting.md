# DOCX Formatting Contract

[English](docx_formatting.md) | [中文](docx_formatting.zh-CN.md)

## Preserve Template Formatting

When a Word template is provided, the generated report must follow the template formatting. Do not invent colorful heading styles, arbitrary fonts, or unrelated body sizes.

Before writing, extract:

- body font, size, line spacing, first-line indent
- chapter heading style, font, size, color, spacing
- section heading style, font, size, color, spacing
- table style and caption style
- cover table and review form boundaries

Use those values for all generated body chapters.

## Cover Fields

Do not force the user to provide student name, ID, class, or teacher at the beginning. If the user provides them, fill them. If not, leave the cover fields blank or keep the template placeholders for the user to fill manually in Word.

Do not invent names, IDs, class names, departments, or teacher names.

## Body Scope

The agent writes only the main report body before appendices:

- chapter 1 theory
- chapter 2 methods/technology
- chapter 3 project practice
- chapter 4 summary/reflection
- references if required

The appendix content should not be authored by the skill unless the user explicitly asks.

## Table Of Contents

If the template contains an old TOC, remove or rebuild it so old entries do not remain. If automatic Word fields cannot be refreshed, create a simple static TOC that matches the actual headings, and tell the user to refresh fields in Word if needed.

## Strict Cleanup

After generation, inspect DOCX text for:

- old TOC entries
- old chapter headings
- old project names
- old sample data tables
- stale figure/table captions
- mixed heading colors or arbitrary custom colors
- body font or size inconsistent with the template

Any residue is a blocker.
