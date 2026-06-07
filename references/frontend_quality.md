# Frontend Quality

[English](frontend_quality.md) | [中文](frontend_quality.zh-CN.md)

## Mandatory Standard

For every non-pure-hardware project, the software portion must include a complete, real, runnable frontend. A screenshot-only mockup, blank HTML page, or minimal form is not acceptable.

## Required Frontend Capabilities

Include:

- main workspace or dashboard
- core operation area
- real project data or result display
- state feedback for loading, success, empty state, and errors
- at least one meaningful interaction loop
- metrics, logs, sources, predictions, records, or test results as appropriate
- clear startup instructions
- screenshots suitable for report insertion

## UI Quality

The frontend should be polished enough for course defense and report screenshots:

- clear information hierarchy
- responsive layout for desktop and reasonable mobile widths
- no text overflow
- no incoherent overlap
- visible interaction states
- readable Chinese text
- restrained professional visual style

Avoid decorative-only pages. The first screen should show the actual system, not a marketing landing page.

## Integration

The frontend must reflect real project behavior through one of:

- backend API calls
- local service routes
- exported JSON/CSV result files
- deterministic static preview generated from real result data

Document the integration path in README and `results/report_notes.md`.

## Screenshot Verification Levels

- Level 1: real browser screenshot from the running frontend; preferred and required for final-quality software reports when tools are available.
- Level 2: API/service verified and deterministic light-background preview generated; label it as a preview, not a screenshot.
- Level 3: frontend source only; record as incomplete verification and do not present it as fully delivered.

All screenshots used in printable reports must be light-background and must show real project data.
