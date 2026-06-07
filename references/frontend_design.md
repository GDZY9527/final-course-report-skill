# Frontend Design Differentiation

[English](frontend_design.md) | [中文](frontend_design.zh-CN.md)

## Design Brief First

Before coding the frontend, create `results/frontend_design_brief.md` with:

- target users and primary workflow
- information architecture specific to the project
- visual tone and layout rationale
- data panels and interactions tied to real project outputs
- desktop and mobile layout notes
- loading, empty, success, and error states

## No Uniform Dashboard Rule

The skill may provide a frontend process, but the final UI must not look like a reused template. Do not ship the same card-grid/dashboard structure for every course.

Each frontend must have a project-specific interaction model:

- C++ systems: operations console, object relationship explorer, state transition panel, compile/run evidence.
- NLP: sample analysis workbench, token/feature explanation, prediction comparison, error analysis.
- LLM apps: prompt/evidence workspace, retrieval trace, response quality review, safety/grounding panel.
- Database: query builder, schema explorer, transaction/log view, data quality panel.
- IoT/mixed courses: live device/sensor monitor, control panel, alert timeline.

## Modern Quality Floor

The frontend should look like a polished course project, not a rushed demo:

- domain-specific navigation and section naming
- meaningful visual hierarchy, spacing, and typography
- real data cards, charts, tables, logs, and detail panels
- responsive layout with at least one mobile breakpoint
- hover/focus/active states for interactive elements
- clear loading, empty, success, and error states
- no oversized marketing hero; the first screen is the usable system

Use restrained but project-specific colors. Avoid one-size-fits-all blue dashboards.

## Verification

Record frontend evidence in `results/report_notes.md`:

- route or file opened
- data source used by the page
- screenshot level: Level 1 browser screenshot or Level 2 deterministic preview
- known limitations
