# Prose Quality And AI Trace Control

[English](prose_quality.md) | [中文](prose_quality.zh-CN.md)

## Goal

The report should read like a completed student course report, not a draft with prompt traces, placeholder notes, encyclopedia-style terminology piles, or excessive parenthetical explanations.

## Parentheses

Allowed:

- A small number of first occurrences of essential technical terms with English full name or abbreviation, such as `潜在语义分析（Latent Semantic Analysis, LSA）`.
- Formula numbers, figure/table numbers, and citation markers.

Limit:

- Explain a term in parentheses only at first use.
- Avoid consecutive English parenthetical glosses.
- Do not use parentheses for writing instructions or self-notes.
- Keep Chinese-English terminology glosses sparse. A full report should normally use no more than 10-15 English term parentheticals unless the course explicitly requires bilingual terminology.
- After a term is defined once, use the Chinese term or abbreviation directly.

Forbidden:

- "to be filled", "TODO", "placeholder"
- "for example" or "note" style parentheticals repeated throughout the body
- parentheticals that explain what the writer should do instead of reporting completed work
- obvious prompt residue
- encyclopedia-style term piles such as `Hidden Markov Model, HMM`, `Conditional Random Fields, CRF`, `Large Language Model, LLM` repeated across one section without direct project use

Rewrite examples:

- Bad: `隐马尔可夫模型（Hidden Markov Model, HMM）、最大熵模型和条件随机场（Conditional Random Fields, CRF）在序列标注中被广泛使用。`
- Better: `早期序列标注通常依赖隐马尔可夫模型、最大熵模型和条件随机场等统计方法，它们共同推动了词性标注、命名实体识别等任务的发展。`
- Better when abbreviation is needed: `条件随机场（CRF）常用于序列标注。后文直接使用 CRF。`

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
- dense bilingual terminology piles that make the prose look AI-generated
- placeholder words
- template-like repeated paragraphs
- repeated long paragraphs
