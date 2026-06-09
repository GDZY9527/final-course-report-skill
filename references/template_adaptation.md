# Word Template Adaptation

[English](template_adaptation.md) | [中文](template_adaptation.zh-CN.md)

## Template Role

The Word template provides structure, not the highest authority for fonts, sizes, and styling. Report formatting must follow `course_report_writing_standard.zh-CN.md` first.

Keep useful template structure such as:

- cover layout and cover field positions
- table-of-contents region or placeholder
- header/footer regions
- appendix heading position
- teacher review form, grading form, or fixed school-required tables

Remove or replace old course body text, old project text, stale TOC entries, old captions, old heading colors, and sample data.

## Template Type

Before writing, classify the Word template:

- Blank template: only cover, TOC, and review form.
- Old report template: body content comes from another course or previous project.
- Mixed template: cover and review form are useful, but old chapters remain.

For old or mixed templates, keep only useful structure. Do not let old report content drive the new course report.

## Boundary Detection

Identify and record:

- cover table and cover fields
- TOC region
- first body chapter start
- appendix region
- teacher review form

Prefer structural position and heading level over exact string matching. Use fuzzy matching for Chinese punctuation, whitespace, and full-width/half-width variants.

## Formatting Order

1. Read the template and identify structure.
2. Remove old body content and stale TOC entries.
3. Read `course_report_writing_standard.zh-CN.md`.
4. Apply the school writing standard to page setup, margins, headers/footers, TOC, headings, body text, captions, formulas, and code blocks.
5. Write the new report content.
6. Render or open-check the result to confirm no old template content remains and no old template styling polluted the report.

## Cleanup Checks

After generation, check that:

- old course keywords do not exist unless explicitly used as historical background
- old project names do not exist
- old captions do not exist
- cover fields match current input or approved blank placeholders
- TOC and heading structure belong to the new report
- fonts, sizes, headings, margins, headers/footers, captions, formulas, and code blocks follow `course_report_writing_standard.zh-CN.md`

If Word fields cannot be updated automatically, state that the user should refresh the table of contents in Word.
