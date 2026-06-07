# Appendix Policy

[English](appendix_policy.md) | [中文](appendix_policy.zh-CN.md)

## Default: Empty Appendix

By default, create only the appendix title `Appendix` / `附录` and leave the appendix body empty for the user to fill manually.

Do not use the appendix to pad report length. Do not dump code, logs, project trees, screenshots, or vague reflections into the appendix unless the user explicitly asks.

## Report Density Without Appendix Padding

The report density gate must be satisfied by the main chapters and references, not by appendix filler. If appendices are left empty, the main body must still satisfy the configured density threshold or the user must approve a shorter report.

## When User Requests Appendix Content

If the user explicitly asks for appendix content, organize it by purpose and keep it concise:

- source tree
- key code excerpts
- run logs
- dependency list
- extra screenshots

Every appendix item must be referenced from the main body or final delivery notes.
