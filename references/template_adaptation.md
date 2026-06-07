# Template Adaptation

[English](template_adaptation.md) | [中文](template_adaptation.zh-CN.md)

## Identify Template Type

Before writing, classify the Word template:

- Blank template: cover, TOC, and review form only.
- Old report template: contains body text from another course or project.
- Mixed template: cover and review form plus partial old chapters.

For old or mixed templates, preserve useful structure but replace stale body content. Never let the old report steer the new course content.

## Boundary Detection

Detect and log:

- cover tables and cover fields
- table of contents area
- first body chapter
- appendices
- teacher review form

Prefer structural position and heading level over exact string matching. Use fuzzy matching for Chinese punctuation and whitespace variants.

## Cleanup Checks

After generation, check:

- old course keywords are absent unless intentionally cited as historical context
- old project names are absent
- old figure/table captions are absent
- cover fields match the current user input or approved placeholders
- TOC/heading structure belongs to the new report

If Word fields cannot be updated automatically, state that the user should refresh the table of contents in Word.
