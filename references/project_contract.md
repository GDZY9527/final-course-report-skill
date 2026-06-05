# Project Contract

## Required Project Quality

Build projects as deliverable course software, not disposable demos.

Every project must provide:

- clear directory structure
- README with setup, run, test, frontend, results, limitations, and extension notes
- `requirements.txt` for Python dependencies when Python is used
- run scripts or exact commands
- source code split by responsibility
- test or evaluation path
- logs and metrics where relevant
- reproducible result files in `results/`
- report writing notes in `results/report_notes.md`
- design summary in `results/design_summary.md`

## Frontend/Backend Requirement

Except for purely hardware-only courses, new projects must include:

- backend, service layer, algorithm layer, or core program
- frontend page or app for operation, visualization, monitoring, management, or result display
- real data exchange or stable exported data linkage between frontend and project results
- frontend screenshots from a real page or deterministic rendering

For software-hardware courses, include hardware I/O or simulated sensor/device data plus a frontend for monitoring, configuration, control, or result visualization.

## Results Contract

Use real files and real runs:

- `results/metrics.json` or equivalent test/evaluation result file
- `results/run_log.txt` or equivalent command output log
- project directory tree image
- system/architecture flow image
- key code screenshots from real source files
- frontend screenshots
- evaluation charts or test summary images

If any result cannot be produced, record why and provide a truthful fallback.

## Fallbacks

When online APIs, large models, compilers, browser automation, or external services are unavailable:

- prefer a smaller local baseline
- keep the original intended route in README and report as future extension
- make the fallback runnable and reproducible
- never write that an unavailable component succeeded

Examples:

- BERT unavailable -> TF-IDF or classical ML baseline plus frontend.
- LLM API unavailable -> offline retrieval/template answer fallback plus frontend.
- Database server unavailable -> SQLite or file-backed fallback.
- Compiler unavailable -> provide source, build instructions, and truthful limitation, then verify any runnable surrounding scripts.
