# DOCX Generation Quality Gate

[English](docx_generation_quality.md) | [中文](docx_generation_quality.zh-CN.md)

## Regression From V3.0

The V3.0 test showed a common failure: the visible fonts and sizes were changed, but the table of contents still came from the template; chapter and section titles looked like headings but remained `Normal`/body paragraphs; heading spacing was too tight.

## Real Heading Styles Are Required

All DOCX headings must use real Word paragraph styles, not body paragraphs with manual font changes.

- Chapter: use the template `一级标题` or equivalent Heading 1 style.
- Section: use `二级标题` or equivalent Heading 2 style.
- Subsection: use `三级标题` or equivalent Heading 3 style.
- Item: use `四级标题` or an equivalent item-heading style; if unavailable, apply the writing-standard paragraph format and record the limitation.

Forbidden:

- Calling `doc.add_paragraph()` and only changing font, size, bold, or alignment.
- Using `Normal` / body style to imitate headings.
- Writing headings that the TOC and navigation pane cannot recognize.

## Rebuild the Table of Contents

The TOC must not be inherited from the template. The agent must:

1. Remove stale template TOC entries.
2. Build the TOC from the generated report's actual heading hierarchy.
3. Insert a refreshable Word TOC field when possible.
4. If a refreshable field cannot be updated, create a static TOC that exactly matches the new headings and tell the user to refresh it in Word.

Blockers:

- TOC contains old course names, old project names, BERT, stale headings, or template remnants.
- Word navigation pane does not recognize headings.
- TOC and actual headings disagree.
- The generated DOCX has the same TOC text as the template DOCX.
- The final DOCX keeps old TOC fields without clearing their paragraph text.
- Multiple report DOCX files are left in the delivery root without clearly marking exactly one final version.

When editing a template, treat the TOC as a volatile section:

- Record all template TOC paragraphs before writing.
- Delete or replace the template TOC paragraphs.
- After writing body headings, regenerate the TOC entries from the actual headings.
- Run an audit comparing template TOC text and final TOC text; any exact match means the report is not finished.
- Do not rely on "Word will update fields later" as the only solution. The visible document delivered to the user must not show stale template entries.

## Heading Spacing

Heading spacing must not be visually cramped. Follow `course_report_writing_standard.zh-CN.md`:

- Chapter/section/subsection headings: 1 line before, 1 line after, single line spacing.
- Do not use 1pt or 0pt spacing as a fake "one line".
- With `python-docx`, prefer `Pt(12)` or the template's actual heading spacing; do not confuse `space_before=1` with one line.

## Recommended `python-docx` Pattern

```python
p = doc.add_paragraph("第1章 XXX")
p.style = find_style(doc, ["一级标题", "Heading 1", "标题 1"])
apply_heading_font(p, level=1)
```

Do not only write:

```python
p = doc.add_paragraph("第1章 XXX")
run = p.add_run(...)
run.font.size = Pt(18)
```

## Pre-Delivery Checks

Before delivery, verify that:

- Word navigation pane recognizes level-1, level-2, and level-3 headings.
- TOC content comes from new headings, not the template.
- Heading spacing follows the writing standard.
- Body font, size, line spacing, and indentation follow the writing standard.
- Appendix has only the heading by default.
- Only one final report DOCX is present in the delivery root, or older draft DOCX files are moved to a clearly named draft folder that is excluded from final packaging.
