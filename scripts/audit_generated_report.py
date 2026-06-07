from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    from PIL import Image
except Exception:
    Image = None

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def inspect_docx(path: Path, root: Path) -> dict:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
        media = [n for n in zf.namelist() if n.startswith("word/media/")]
    doc = ET.fromstring(xml)
    paragraphs = []
    for p in doc.findall(".//w:p", NS):
        text = "".join(t.text or "" for t in p.findall(".//w:t", NS)).strip()
        if text:
            paragraphs.append(text)
    full = "\n".join(paragraphs)
    return {
        "file": str(path.relative_to(root)),
        "bytes": path.stat().st_size,
        "paragraphs": len(paragraphs),
        "chars_no_space": len(re.sub(r"\s+", "", full)),
        "chinese_chars": len(re.findall(r"[\u4e00-\u9fff]", full)),
        "embedded_media": len(media),
        "tables": len(doc.findall(".//w:tbl", NS)),
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
        if hasattr(sample, "get_flattened_data"):
            pixels = list(sample.get_flattened_data())
        else:
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit generated final-course-report outputs.")
    parser.add_argument("root", help="Course output directory to inspect.")
    parser.add_argument("--min-chars", type=int, default=18000)
    parser.add_argument("--min-media", type=int, default=8)
    parser.add_argument("--json-out", default="")
    parser.add_argument("--forbidden-keyword", action="append", default=[], help="Keyword that must not remain in generated DOCX text. Repeatable.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    docx = [inspect_docx(p, root) for p in root.rglob("*.docx") if "模板" not in p.name]
    png = [inspect_png(p, root) for p in root.rglob("*.png")]

    failures = []
    for item in docx:
        body_text = item.pop("text")
        if item["chars_no_space"] < args.min_chars:
            failures.append(f"{item['file']}: text density below {args.min_chars}")
        if item["embedded_media"] < args.min_media:
            failures.append(f"{item['file']}: embedded media below {args.min_media}")
        if item["tables"] < 5:
            failures.append(f"{item['file']}: table count below 5")
        for keyword in args.forbidden_keyword:
            if keyword and keyword in body_text:
                failures.append(f"{item['file']}: forbidden keyword remains: {keyword}")
    for item in png:
        if item.get("print_risk"):
            failures.append(f"{item['file']}: dark/print-risk image")

    report = {"docx": docx, "png": png, "failures": failures}
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(text, encoding="utf-8")
    print(text)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
