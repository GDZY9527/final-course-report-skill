from __future__ import annotations

import argparse
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    from PIL import Image
except Exception:
    Image = None

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

TEXT_EXTENSIONS = {".md", ".txt", ".py", ".html", ".css", ".js", ".json", ".yaml", ".yml"}
MOJIBAKE_RE = re.compile(r"(鑷|鍩|鏈|璇|鈥|鈺|锛|銆|馃|�|Ã|Â)")
PLACEHOLDER_RE = re.compile(
    r"(To be filled|TODO|PLACEHOLDER|placeholder|待补充|此处|自行填写|按需填写|可替换|说明：|注：)"
)
HEADING_RE = re.compile(r"^(第\s*\d+\s*章|附录$|\d+(?:\.\d+){1,3}\s+|[一二三四五六七八九十]+、)")
PROMPTLIKE_PAREN_RE = re.compile(
    r"([（(][^）)]{2,80}(?:建议|可选|此处|说明|补充|TODO|placeholder|"
    r"[A-Za-z]{3,}[^）)]{0,60})[）)])"
)
ENGLISH_TERM_PAREN_RE = re.compile(r"[（(][^）)]*[A-Za-z]{3,}[^）)]*[）)]")
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "dist", "build", ".venv", "venv"}


def paragraph_text(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.findall(".//w:t", NS)).strip()


def paragraph_style(p: ET.Element) -> str:
    style = p.find("./w:pPr/w:pStyle", NS)
    if style is None:
        return ""
    return style.attrib.get(f"{{{NS['w']}}}val", "")


def is_template_docx(path: Path) -> bool:
    lowered = path.name.lower()
    return "template" in lowered or "模板" in path.name or path.name.startswith("~$")


def toc_entries_from_docx(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as zf:
        doc = ET.fromstring(zf.read("word/document.xml"))
    entries = []
    for p in doc.findall(".//w:p", NS):
        text = paragraph_text(p)
        style = paragraph_style(p)
        if text and (style.startswith("TOC") or text == "目录" or text.lower() == "contents"):
            entries.append(re.sub(r"\s+", "", text))
    return entries


def inspect_docx(path: Path, root: Path) -> dict:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
        media = [n for n in zf.namelist() if n.startswith("word/media/")]
    doc = ET.fromstring(xml)

    paragraphs: list[dict] = []
    for p in doc.findall(".//w:p", NS):
        text = paragraph_text(p)
        if text:
            paragraphs.append({"text": text, "style": paragraph_style(p)})

    plain = [item["text"] for item in paragraphs]
    full = "\n".join(plain)
    appendix_index = next(
        (i for i, value in enumerate(plain) if value.strip() == "附录" or value.strip().lower() == "appendix" or value.startswith("附录")),
        None,
    )
    appendix_text = "\n".join(plain[appendix_index + 1 :]) if appendix_index is not None else ""
    normalized = [re.sub(r"\s+", "", p) for p in plain if len(re.sub(r"\s+", "", p)) >= 80]
    repeated = sorted({p for p in normalized if normalized.count(p) >= 2}, key=len, reverse=True)
    heading_candidates = [item for item in paragraphs if HEADING_RE.match(item["text"])]
    normal_headings = [item["text"] for item in heading_candidates if not item["style"]]
    style_counts = Counter(item["style"] or "NO_PARAGRAPH_STYLE" for item in heading_candidates)
    parenthetical_hints = PROMPTLIKE_PAREN_RE.findall(full)
    english_term_parentheticals = ENGLISH_TERM_PAREN_RE.findall(full)
    placeholders = PLACEHOLDER_RE.findall(full)

    return {
        "file": str(path.relative_to(root)),
        "bytes": path.stat().st_size,
        "paragraphs": len(paragraphs),
        "chars_no_space": len(re.sub(r"\s+", "", full)),
        "chinese_chars": len(re.findall(r"[\u4e00-\u9fff]", full)),
        "embedded_media": len(media),
        "tables": len(doc.findall(".//w:tbl", NS)),
        "appendix_chars": len(re.sub(r"\s+", "", appendix_text)),
        "repeated_long_paragraphs": len(repeated),
        "heading_count": len(heading_candidates),
        "normal_heading_count": len(normal_headings),
        "heading_style_counts": dict(style_counts),
        "parenthetical_hint_count": len(parenthetical_hints),
        "english_term_parenthetical_count": len(english_term_parentheticals),
        "placeholder_count": len(placeholders),
        "normal_heading_samples": normal_headings[:12],
        "parenthetical_hint_samples": parenthetical_hints[:12],
        "english_term_parenthetical_samples": english_term_parentheticals[:12],
        "placeholder_samples": sorted(set(placeholders))[:12],
        "text": full,
    }


def inspect_png(path: Path, root: Path) -> dict:
    result = {"file": str(path.relative_to(root)), "bytes": path.stat().st_size}
    if Image is None:
        result["error"] = "Pillow is not installed; cannot inspect pixels."
        return result
    with Image.open(path) as img:
        img = img.convert("RGB")
        w, h = img.size
        sample = img.resize((max(1, min(300, w)), max(1, min(300, h))))
        pixels = list(sample.getdata())
        lum = [0.2126 * r + 0.7152 * g + 0.0722 * b for r, g, b in pixels]
    avg = sum(lum) / len(lum)
    dark_ratio = sum(1 for value in lum if value < 60) / len(lum)
    return {
        **result,
        "size": f"{w}x{h}",
        "avg_luminance": round(avg, 1),
        "dark_ratio": round(dark_ratio, 3),
        "print_risk": bool(avg < 180 or dark_ratio > 0.18),
    }


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if re.search(r"(^|[_-])audit([_-]|\.|$)", path.stem.lower()):
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def inspect_text_files(root: Path) -> dict:
    mojibake = []
    placeholders = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            mojibake.append({"file": str(path.relative_to(root)), "issue": f"not utf-8: {exc}"})
            continue
        bad = MOJIBAKE_RE.findall(text)
        holder = PLACEHOLDER_RE.findall(text)
        if bad:
            mojibake.append({"file": str(path.relative_to(root)), "count": len(bad), "samples": sorted(set(bad))[:8]})
        if holder:
            placeholders.append({"file": str(path.relative_to(root)), "count": len(holder), "samples": sorted(set(holder))[:8]})
    return {"mojibake": mojibake, "placeholders": placeholders}


def inspect_frontend(root: Path) -> dict:
    files = [p for p in root.rglob("*") if p.is_file()]
    lowered = [str(p.relative_to(root)).replace("\\", "/").lower() for p in files]
    has_manage = any(item.endswith("manage.py") for item in lowered)
    has_django_urls = any(item.endswith("urls.py") for item in lowered)
    has_django_views = any(item.endswith("views.py") for item in lowered)
    has_templates = any("/templates/" in item or item.startswith("templates/") for item in lowered)
    has_static = any("/static/" in item or item.startswith("static/") for item in lowered)
    flask_markers = []
    for path in files:
        if path.suffix.lower() != ".py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if re.search(r"\bfrom\s+flask\b|\bimport\s+flask\b|Flask\(", text):
            flask_markers.append(str(path.relative_to(root)))
    return {
        "has_manage_py": has_manage,
        "has_django_urls": has_django_urls,
        "has_django_views": has_django_views,
        "has_templates": has_templates,
        "has_static": has_static,
        "flask_markers": flask_markers,
    }


def screenshot_files(root: Path) -> list[str]:
    keywords = ("screenshot", "frontend", "page", "browser", "首页", "页面", "截图")
    found = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            continue
        name = str(path.relative_to(root)).lower()
        if any(k.lower() in name for k in keywords):
            found.append(str(path.relative_to(root)))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit generated final-course-report outputs.")
    parser.add_argument("root", help="Course output directory to inspect.")
    parser.add_argument("--min-chars", type=int, default=18000)
    parser.add_argument("--min-media", type=int, default=8)
    parser.add_argument("--json-out", default="")
    parser.add_argument("--forbidden-keyword", action="append", default=[], help="Keyword that must not remain in generated DOCX text. Repeatable.")
    parser.add_argument("--require-project-brief", action="store_true", help="Fail if results/project_brief.md is missing.")
    parser.add_argument("--require-frontend-brief", action="store_true", help="Fail if results/frontend_design_brief.md is missing.")
    parser.add_argument("--require-heading-styles", action="store_true", help="Fail when numbered/chapter headings are plain Normal paragraphs without Word heading styles.")
    parser.add_argument("--require-fresh-toc", action="store_true", help="Fail if generated DOCX visible TOC matches a template DOCX.")
    parser.add_argument("--require-single-final-docx", action="store_true", help="Fail if multiple non-template report DOCX files remain in the delivery root.")
    parser.add_argument("--require-django-frontend", action="store_true", help="Fail if a Python web frontend is Flask/single-file style instead of Django structure.")
    parser.add_argument("--require-frontend-screenshots", action="store_true", help="Fail if fewer than three frontend/browser screenshot files are found.")
    parser.add_argument("--forbid-placeholders", action="store_true", help="Fail if generated text/code/log files contain unresolved placeholders.")
    parser.add_argument("--max-appendix-chars", type=int, default=20, help="Fail if appendix body is longer than this. Appendix body should stay empty unless requested.")
    parser.add_argument("--max-repeated-long-paragraphs", type=int, default=0, help="Fail if repeated long paragraphs exceed this count.")
    parser.add_argument("--max-parenthetical-hints", type=int, default=30, help="Fail if prompt-like parenthetical hints exceed this count.")
    parser.add_argument("--max-english-term-parentheticals", type=int, default=15, help="Fail if English terminology parentheticals exceed this count.")
    parser.add_argument("--max-mojibake-hits", type=int, default=0, help="Fail if text files with mojibake exceed this count.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report_docx_paths = [p for p in root.rglob("*.docx") if not is_template_docx(p)]
    template_docx_paths = [p for p in root.rglob("*.docx") if is_template_docx(p) and not p.name.startswith("~$")]
    docx = [inspect_docx(p, root) for p in report_docx_paths]
    png = [inspect_png(p, root) for p in root.rglob("*.png")]
    text_audit = inspect_text_files(root)
    frontend = inspect_frontend(root)
    screenshots = screenshot_files(root)

    failures = []
    for item in docx:
        body_text = item.pop("text")
        if item["chars_no_space"] < args.min_chars:
            failures.append(f"{item['file']}: text density below {args.min_chars}")
        if item["embedded_media"] < args.min_media:
            failures.append(f"{item['file']}: embedded media below {args.min_media}")
        if item["tables"] < 5:
            failures.append(f"{item['file']}: table count below 5")
        if item["appendix_chars"] > args.max_appendix_chars:
            failures.append(f"{item['file']}: appendix too long ({item['appendix_chars']} chars > {args.max_appendix_chars}); appendix body should be empty unless requested")
        if item["repeated_long_paragraphs"] > args.max_repeated_long_paragraphs:
            failures.append(f"{item['file']}: repeated long paragraphs detected ({item['repeated_long_paragraphs']})")
        if args.require_heading_styles and item["normal_heading_count"] > 0:
            failures.append(f"{item['file']}: {item['normal_heading_count']} heading-like paragraphs have no Word heading style")
        if item["parenthetical_hint_count"] > args.max_parenthetical_hints:
            failures.append(f"{item['file']}: prompt-like parenthetical hints exceed {args.max_parenthetical_hints} ({item['parenthetical_hint_count']})")
        if item["english_term_parenthetical_count"] > args.max_english_term_parentheticals:
            failures.append(f"{item['file']}: English terminology parentheticals exceed {args.max_english_term_parentheticals} ({item['english_term_parenthetical_count']}); reduce AI-looking bilingual term piles")
        if args.forbid_placeholders and item["placeholder_count"] > 0:
            failures.append(f"{item['file']}: unresolved placeholder/prompt markers remain in DOCX ({item['placeholder_count']})")
        for keyword in args.forbidden_keyword:
            if keyword and keyword in body_text:
                failures.append(f"{item['file']}: forbidden keyword remains: {keyword}")

    if args.require_project_brief and not any(root.rglob("results/project_brief.md")):
        failures.append("missing required results/project_brief.md")
    if args.require_frontend_brief and not any(root.rglob("results/frontend_design_brief.md")):
        failures.append("missing required results/frontend_design_brief.md")
    if args.require_single_final_docx:
        root_reports = [p for p in report_docx_paths if p.parent == root]
        if len(root_reports) != 1:
            failures.append(f"expected exactly one final report DOCX in delivery root, found {len(root_reports)}: {[p.name for p in root_reports]}")
    if args.require_fresh_toc and template_docx_paths:
        template_tocs = [toc_entries_from_docx(p) for p in template_docx_paths]
        for report_path in report_docx_paths:
            report_toc = toc_entries_from_docx(report_path)
            for template_path, template_toc in zip(template_docx_paths, template_tocs):
                if report_toc and template_toc and report_toc == template_toc:
                    failures.append(f"{report_path.relative_to(root)}: visible TOC matches template {template_path.relative_to(root)}; rebuild TOC from generated headings")
    if len(text_audit["mojibake"]) > args.max_mojibake_hits:
        failures.append(f"text files contain mojibake/encoding damage ({len(text_audit['mojibake'])} files)")
    if args.forbid_placeholders and text_audit["placeholders"]:
        failures.append(f"text files contain unresolved placeholders ({len(text_audit['placeholders'])} files)")
    if args.require_django_frontend:
        if frontend["flask_markers"]:
            failures.append(f"Flask markers found where Django frontend is required: {frontend['flask_markers'][:5]}")
        missing = [
            label for label, ok in [
                ("manage.py", frontend["has_manage_py"]),
                ("urls.py", frontend["has_django_urls"]),
                ("views.py", frontend["has_django_views"]),
                ("templates", frontend["has_templates"]),
                ("static", frontend["has_static"]),
            ] if not ok
        ]
        if missing:
            failures.append(f"Django frontend structure incomplete: missing {', '.join(missing)}")
    if args.require_frontend_screenshots and len(screenshots) < 3:
        failures.append(f"frontend/browser screenshots below 3 ({len(screenshots)} found): {screenshots}")
    for item in png:
        if item.get("print_risk"):
            failures.append(f"{item['file']}: dark/print-risk image")

    temp_files = [
        str(p.relative_to(root))
        for p in root.rglob("*")
        if p.is_file() and (p.name.startswith("~$") or p.suffix.lower() in {".pyc", ".pyo"} or p.name in {"「", "」"})
    ]
    if temp_files:
        failures.append(f"temporary/cache files should not enter delivery: {temp_files[:10]}")

    report = {"docx": docx, "png": png, "text": text_audit, "frontend": frontend, "screenshots": screenshots, "temp_files": temp_files, "failures": failures}
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(text, encoding="utf-8")
    print(text)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
