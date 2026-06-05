# Frontend Quality

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
