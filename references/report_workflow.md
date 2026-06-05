# Report Workflow

## Purpose

Use this workflow to create a complete final course report and supporting project from a course name, a project direction, a Word template, and a target environment.

## Preflight

Collect:

- course name
- project direction or course focus
- target course directory
- template `.docx`
- conda Python path
- student name, student ID, class, teacher, and required filename
- whether the course is purely hardware-only

Inspect existing files before asking questions that can be answered locally.

## Two-Stage Generation

1. **Project stage**
   - Create a real runnable project.
   - Generate README, requirements, run scripts, source files, frontend, backend/core logic, data, tests, result files, screenshots, and report notes.
   - Run or document verification commands with `{conda_python}`.

2. **Report stage**
   - Analyze the Word template before writing.
   - Preserve cover, table of contents, headers/footers, heading hierarchy, figure captions, table captions, appendix style, and review forms from the template.
   - Write from real project outputs.
   - Render and visually inspect when document tools are available.

## Default Report Structure

- Cover page
- Table of contents
- Chapter 1: Course theory foundations
- Chapter 2: Core technologies and methods
- Chapter 3: Project practice
- Chapter 4: Learning reflection and future work
- References or sources
- Appendices

## Writing Requirements

- Use formal but natural academic Chinese.
- Each key theory section should connect concept, principle, engineering meaning, and project relevance.
- Every figure and table needs text interpretation.
- Chapter 3 must explain requirement background, architecture, data flow, frontend interaction, backend/core logic, tests, results, limitations, and optimization.
- Do not copy another course report's prose. Reuse structure and standards only.

## Final Response Checklist

Report final outputs:

- Word and PDF paths when generated
- project path
- conda environment path used
- generated figure/table list
- verification summary
- known limitations
- pending packaging confirmation or final package path
