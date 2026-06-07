# Project Uniqueness

[English](project_uniqueness.md) | [中文](project_uniqueness.zh-CN.md)

## No Reuse Rule

Every new report must use a new practice project. This applies even when the course name is the same as a previous report.

Do not reuse, lightly rename, or slightly modify:

- example projects in this repository
- projects from prior test runs
- projects already present in the target course directory
- common fallback examples from this skill
- generic management systems, generic RAG QA systems, generic sentiment classifiers, or generic dashboards

Historical examples are negative examples for reuse. They may teach quality expectations, not project topics.

## Banned Default Patterns

Do not select these as default projects unless the user explicitly asks and accepts the reuse risk:

- C++ OOP: library/book management, student score management, generic inventory management.
- NLP: generic sentiment analysis, BERT/TF-IDF text classification, simple news classifier.
- LLM application: generic RAG knowledge-base QA, generic prompt evaluator, generic chatbot.
- Database/software engineering: generic CRUD management system without a domain-specific process.

If the course naturally points to one of these patterns, redesign it into a different domain workflow with different data, roles, interactions, and evaluation evidence.

## Required Project Brief

Before coding, create `results/project_brief.md` and include:

- course name and chosen project title
- three candidate project ideas and why two were rejected
- explicit statement that prior examples and current directory projects were checked
- 5-7 course-specific requirements
- domain-specific data schema or input/output format
- unique workflow that cannot be pasted into another course unchanged
- expected evidence files in `results/`
- similarity risk notes and how the project avoids reuse

Do not start implementation before this brief exists.

## Similarity Check

Before final delivery, compare the chosen project against known examples and current directory files. If the project title, domain entities, data schema, main workflow, and figures overlap heavily with an old project, choose a new project.

Record the decision in `results/project_brief.md` and `results/report_notes.md`.
