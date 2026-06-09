# DOCX Formatting Contract

[English](docx_formatting.md) | [中文](docx_formatting.zh-CN.md)

## Highest Formatting Authority

All Word report formatting must follow `references/chengdu_neusoft_report_standard.zh-CN.md` as the highest-priority authority. It is derived from the user-provided `成都东软学院定制班课程报告撰写规范.docx`.

Previous skill rules about inheriting template fonts, font sizes, heading colors, line spacing, captions, or code formatting are replaced by that writing standard.

## Template Boundary

The Word template is still used for:

- cover structure and cover field positions
- table-of-contents region
- header/footer placement
- review or grading forms
- fixed school-required tables or pages

If template fonts, sizes, heading colors, line spacing, captions, or code formatting conflict with `chengdu_neusoft_report_standard.zh-CN.md`, correct them to the writing standard.

## Required Gates

Before writing DOCX:

1. Read `chengdu_neusoft_report_standard.zh-CN.md`.
2. Configure page setup, margins, headers/footers, headings, body text, TOC, figure captions, table captions, formulas, and code styles from that standard.
3. Remove old template body text, stale TOC entries, old headings, old captions, and old sample data.

After writing DOCX, check:

- A4 page size and 25mm margins on all sides.
- Header text is `成都东软学院定制班课程报告`.
- Chinese body text uses SimSun `小四`; English and numbers use Times New Roman `小四`.
- Body text has first-line indent of 2 Chinese characters and 1.5 line spacing.
- Chapter/section/subsection/item headings follow the standard heading table.
- Figure captions are below figures; table captions are above tables; both use SimSun `五号`.
- Code uses Times New Roman `五号` / SimSun `五号`, 1.25 multiple line spacing, and no bold.
- TOC matches actual headings and has no stale template entries.
- Appendix keeps only the heading by default and leaves body empty.

Any obvious violation of the writing standard is a delivery blocker.
