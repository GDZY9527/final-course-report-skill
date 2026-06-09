# Frontend Framework And Consumer-Grade Delivery Gate

[English](frontend_framework.md) | [中文](frontend_framework.zh-CN.md)

## Conclusion

Flask is not inherently bad, but Flask + Jinja + minimal CSS is too often downgraded into a classroom demo. For Python web projects, default to Django unless the user explicitly requests another stack.

## Default Framework

For non-pure-hardware courses using Python web technology:

- Default to Django.
- Include a Django project, at least one business app, templates, static files, URL routes, views, forms or equivalent input validation, and error pages.
- If an API is needed, use Django views or Django REST Framework.
- Do not use a single-file script as a complete backend.
- Flask is allowed only when the user explicitly requests it or the project is clearly a lightweight API prototype. Even then, the frontend quality gate still applies.

## Consumer-Grade Frontend Standard

The frontend must not be only a title, cards, form, and table. It must include:

- project-specific workbench, not a generic blue dashboard
- clear information architecture: navigation, main workspace, detail area, results area, state area
- at least 3 real business pages or equivalent views
- loading, empty, success, failure, validation, and backend-error states
- real data-driven charts, tables, detail panels, and operation feedback
- responsive layout checked on desktop and mobile
- accessibility: labels, semantic buttons, focus states, and contrast
- visual design tied to the project domain

## Forbidden

- single-file Flask + Jinja + rough CSS as the complete frontend/backend
- same blue dashboard/card grid for all courses
- sparse demo pages with large blank areas and very few workflows
- unhandled JavaScript errors
- mojibake/garbled UI text
- claiming real screenshots when screenshots were not taken from a real browser run

## Verification

Before delivery, record:

- start command
- visited URL
- page list
- real browser screenshot paths
- browser console errors
- mobile viewport check

If browser screenshots cannot run, record the limitation honestly.
