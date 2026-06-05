# Visual Rules

[English](visual_rules.md) | [中文](visual_rules.zh-CN.md)

## Academic Technical Figure Style

Every report figure must fit an academic paper or course report style. Figures must not be simplistic, decorative, or empty.

Required qualities:

- information-dense but readable
- rigorous module hierarchy
- clear arrows and data/control flow
- explicit inputs, processing modules, outputs, constraints, and evaluation points when relevant
- aligned layout and consistent typography
- complete Chinese labels without truncation

## Deterministic vs Generated Images

Use deterministic or real-source methods for:

- project directory trees
- code screenshots
- terminal or run logs
- frontend screenshots
- test result charts
- metrics plots
- confusion matrices
- class diagrams derived from code

Use generated bitmap images only for conceptual theory figures, optimization roadmaps, or supplemental diagrams when deterministic methods are not appropriate. Do not use generated images to fake project execution.

## Required Checks

Before inserting figures:

- verify dimensions and readability
- check bottom and side edges are not cropped
- ensure text is complete
- ensure figure number and caption match the report
- ensure tables and figures are interpreted in surrounding text
- keep source images in a report asset directory for manual replacement

## Preferred Project Figures

Most projects should produce:

- course knowledge or technology system diagram
- project architecture/system flow
- frontend interaction flow
- key code screenshots
- evaluation/test chart
- frontend home and demo screenshots
- project directory tree
- future optimization roadmap
