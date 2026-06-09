# Prose Quality And AI Trace Control

[English](prose_quality.md) | [中文](prose_quality.zh-CN.md)

## Goal

The report should read like a completed student course report, not a draft with prompt traces, placeholder notes, or excessive parenthetical explanations.

## Parentheses

Allowed:

- First occurrence of a technical term with English full name or abbreviation, such as `潜在语义分析（Latent Semantic Analysis, LSA）`.
- Formula numbers, figure/table numbers, and citation markers.

Limit:

- Explain a term in parentheses only at first use.
- Avoid consecutive English parenthetical glosses.
- Do not use parentheses for writing instructions or self-notes.

Forbidden:

- "to be filled", "TODO", "placeholder"
- "for example" or "note" style parentheticals repeated throughout the body
- parentheticals that explain what the writer should do instead of reporting completed work
- obvious prompt residue

## Reduce Machine-Like Prose

Avoid:

- dense mechanical enumerations in every paragraph
- repeated paragraph openings
- repeated "this project implements..." sentence patterns
- using appendix, parentheses, or terminology piles to inflate length
- putting Chinese term, English translation, abbreviation, and extra explanation all in the same sentence repeatedly

Prefer:

- course concepts tied to project decisions
- real metrics, figures, debugging, and test evidence
- natural transitions between paragraphs
- concise terminology after first definition

## Pre-Delivery Checks

Check for:

- prompt-like parentheticals
- excessive English parenthetical terms
- placeholder words
- template-like repeated paragraphs
- repeated long paragraphs
