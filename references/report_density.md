# Report Density And Evidence Rules

[English](report_density.md) | [中文](report_density.zh-CN.md)

## Minimum Density

Do not deliver a thin report. If page rendering is unavailable, use these proxy gates before final delivery:

- Target length: 28-35 A4 pages for a normal course final report.
- Minimum text density: 18,000 Chinese characters or 22,000 non-space mixed-language characters.
- Minimum embedded media: 8 report-relevant images or diagrams, unless the course brief explicitly requires fewer.
- Minimum tables: 5 evidence tables, including environment, data/results, tests, project modules, and limitations.
- Chapter 3 project practice should be the densest chapter and should contain at least 35% of the report body.
- Appendices must be organized by purpose: source tree, key code, run logs, dependency list, and extra screenshots. Do not dump unrelated fragments.

If a report falls below these gates, expand it before delivery rather than explaining the weakness afterward.

## Chapter Evidence Matrix

Before writing the report, create a short matrix:

| Course concept | Project module | Evidence file | Figure/table | Report section |

Every important theory section should point to a project module or verified result. Every figure and table must be referenced and interpreted in nearby text.

## Anti-Template-Reuse Gate

Before final delivery, search the report for old course names, old project names, stale model names, and old student fields from the template. If any unrelated old keyword remains, clean the report and re-check.

## Missing Student Fields

If the user asks for a formal submission-ready version, collect missing cover fields first. If the user allows placeholders, use visible placeholders such as `未提供` and record them in the final limitations.

## Body Density Planning

Plan target length by chapter before writing. Do not rely on appendix padding after generation:

- Chapters 1 and 2 cover theory and methods.
- Chapter 3 project practice must be the longest chapter, target 35%-45% of main-body text.
- Chapter 4 should be concise but concrete.
- The appendix is empty by default and should not be the main density source.

If the first draft is too short, expand Chapter 3 with design tradeoffs, real result interpretation, error analysis, testing discussion, and limitations instead of expanding appendices.
