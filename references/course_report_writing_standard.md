# Course Report Writing Standard

[English](course_report_writing_standard.md) | [中文](course_report_writing_standard.zh-CN.md)

This file is the English companion to `course_report_writing_standard.zh-CN.md`, which was transcribed from the user-provided `课程报告撰写规范.docx`. For exact Chinese typography terms such as `小二`, `小三`, `四号`, `小四`, `五号`, `小五`, `宋体`, and `黑体`, the Chinese file is authoritative.

## Priority

- The Chinese standard is the highest-priority formatting authority for generated Word reports.
- The Word template provides structure only: cover fields, table-of-contents region, header/footer regions, appendix heading, and review forms.
- If template styles conflict with the school standard, correct them to the school standard.
- Do not invent blue, colorful, gradient, or arbitrary custom heading styles.
- Leave optional cover fields blank when the user does not provide them.
- By default, create only the appendix heading and leave appendix body empty.

## Required Structure

The report consists of front matter and body matter.

Front matter:

- cover
- table of contents

Body matter:

- introduction
- body / project work
- conclusion and discussion according to the course implementation requirements

The cover should include the Chinese or foreign title, college, department, major, class, name, student ID, instructor, and submission date. The title should accurately reflect the report content, normally no longer than 35 Chinese characters, and remain identical wherever it appears.

The table of contents must be independent and include chapter, section, item numbering, titles, and page numbers.

## Writing Requirements

The introduction should briefly describe the purpose, significance, scope, research plan, methods, experiment design, and topic basis. It should be concise, avoid repeating the abstract, and avoid restating basic textbook knowledge.

The body is the core and main length of the report. It may include objects of investigation, experiment or observation methods and results, instrument principles, material selection, calculation methods, programming principles, data processing, design rationale, figures, tables, arguments, and conclusions. Body content must be factual, objective, accurate, complete, logical, rigorous, well-structured, fluent, and appropriate for the discipline.

Figures and tables must be numbered by chapter. Figure captions go below figures; table captions go above tables. Axes must include quantities and units. Use computer-drawn figures and tables. If a long table continues to another page, repeat the header and mark the continuation using the Chinese continuation-table notation described in the Chinese standard.

Symbols and abbreviations should follow authoritative disciplinary conventions. Custom symbols or abbreviations must be defined at first use. Citations to external materials, including figures, tables, data, claims, and evidence, must use superscript citation markers in order of first appearance.

The conclusion should be accurate, complete, clear, and concise. It may include suggestions, future ideas, and unresolved issues.

## Page Setup

- Paper: standard A4, 210mm x 297mm.
- Margins: top, bottom, left, and right are all 25mm.
- Header distance: 1.5cm.
- Footer distance: 1.75cm.
- Printing and binding: single-sided printing, left binding.
- Cover: use the customized-class standard cover.

## Front Matter Formatting

Headers and footers start from the abstract page:

- Header font: SimSun, Chinese `五号`, centered.
- Header text: `{report_header_text}`. Default to `课程报告` unless the user or template provides a required school header.
- Abstract and TOC page numbers: uppercase Roman numerals, SimSun `小五`, centered footer.

Chinese abstract:

- Title `摘  要`: SimHei `小二`, centered, two spaces between the two characters, single line spacing.
- Body and keywords: SimSun `小四`, first-line indent 2 Chinese characters, 1.5 line spacing.
- `关键词`: SimHei `小四`, bold.
- Keywords: SimSun `小四`, separated by Chinese comma, no punctuation after the last keyword.

English abstract:

- Title: Times New Roman `小二`, centered, single line spacing.
- Body and keywords: Times New Roman `小四`, first-line indent 2 characters, 1.5 line spacing.
- `Key Words`: SimHei `小四`, bold.
- Keywords: Times New Roman `小四`, separated by half-width comma, no punctuation after the last keyword.

Table of contents:

- Title `目  录`: SimHei `小二`, centered, two spaces between characters.
- Level-1 entries: SimHei `小四`.
- Other entries: SimSun `小四`.
- TOC line spacing: 1.5.
- Level-3 entries: left indent 2 characters.
- Page numbers right-aligned; title and page number connected with dot leaders.
- Numbers, page numbers, and dot leaders use Times New Roman `小四`.

## Main Body Formatting

Heading hierarchy:

| Level | Font and Size | Format | Example |
| --- | --- | --- | --- |
| Chapter | Chinese: SimHei `小二`; numbers/English: Times New Roman `小二` | Centered, 1 line before, 1 line after, single spacing | 第1章 XXX |
| Section | Chinese: SimHei `小三`; numbers/English: Times New Roman `小三` | Left aligned, 1 line before, 1 line after, single spacing | 1.1 XXXXXX |
| Subsection | Chinese: SimHei `四号`; numbers/English: Times New Roman `四号` | Left aligned, 1 line before, 1 line after, single spacing | 1.1.1 XXXXXX |
| Item | Chinese: SimSun `小四`; numbers/English: Times New Roman `小四` | First-line indent 2 characters, 1 line before, 1 line after, 1.5 spacing | （a）（b）（c） / （1）（2）（3） |

Other heading rules:

- Each chapter starts on a new page.
- Chapter title should normally be no longer than 25 Chinese characters.
- Use half-width dots between Arabic numbering levels.
- Do not place any heading as the last line of a page.

Body text:

- Chinese: SimSun `小四`.
- Numbers and English: Times New Roman `小四`.
- First-line indent: 2 Chinese characters.
- Line spacing: 1.5.
- Main-body header: single line, centered `{report_header_text}`, SimSun `五号`. Default to `课程报告` unless the user or template provides a required school header.
- Main-body page numbers: restart from body, Arabic numerals, Times New Roman `小五`, centered footer.

Figures:

- Figure number uses chapter number, such as `图4.1`.
- Figure number and title are separated by one Chinese character space.
- Caption goes directly below the figure; figure and caption stay on the same page.
- Caption font: SimSun `五号`.
- In-figure labels should not be larger than the caption; recommended `五号`.

Tables:

- Table number uses chapter number, such as `表5.1`.
- Caption goes above the table, centered.
- Caption font: SimSun `五号`.
- Table text: SimSun `五号`; content size should not exceed caption size.

Formulas:

- Number formulas by chapter, such as `式（3-1）`.
- Formula is usually centered on a separate line.
- Formula number appears on the same line, right aligned.

Code:

- First code line: 0.5 line before.
- Other code lines: 0 before and 0 after.
- Multiple line spacing: 1.25.
- English/numbers: Times New Roman `五号`.
- Chinese: SimSun `五号`.
- Not bold; keep layout clean and readable.

## Implementation Gates

- Remove old body text, stale TOC entries, old captions, old headings, and old sample data from templates.
- Validate headings, body text, TOC, headers/footers, captions, tables, formulas, code blocks, and appendix after generation.
- If automation cannot update Word fields, page numbers, or headers/footers precisely, keep the document structurally refreshable and explicitly tell the user what to refresh in Word.
