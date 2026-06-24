#!/usr/bin/env python3
"""Extract readable text from IoT Security course materials."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree


SUPPORTED_SUFFIXES = {".pptx", ".pdf"}


def slugify(name: str) -> str:
    stem = Path(name).stem
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", stem.lower()).strip("-")
    if slug:
        return slug
    digest = hashlib.sha1(stem.encode("utf-8")).hexdigest()[:10]
    return f"material-{digest}"


def _slide_number(path: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", path)
    return int(match.group(1)) if match else 0


def _xml_text_nodes(raw_xml: bytes) -> list[str]:
    root = ElementTree.fromstring(raw_xml)
    texts: list[str] = []
    for node in root.iter():
        if node.tag.endswith("}t") or node.tag == "t":
            value = (node.text or "").strip()
            if value:
                texts.append(value)
    return texts


def _title_from_lines(lines: list[str], fallback: str) -> str:
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            return cleaned[:120]
    return fallback


def parse_pptx(path: Path) -> dict[str, Any]:
    slides: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        slide_paths = sorted(
            [name for name in archive.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", name)],
            key=_slide_number,
        )
        for slide_path in slide_paths:
            lines = _xml_text_nodes(archive.read(slide_path))
            number = _slide_number(slide_path)
            slides.append(
                {
                    "number": number,
                    "title": _title_from_lines(lines, f"Slide {number}"),
                    "lines": lines,
                    "text": "\n".join(lines),
                }
            )
    full_text = "\n\n".join(slide["text"] for slide in slides if slide["text"])
    return {
        "kind": "pptx",
        "slide_count": len(slides),
        "page_count": None,
        "slides": slides,
        "full_text": full_text,
    }


def parse_pdf(path: Path) -> dict[str, Any]:
    from PyPDF2 import PdfReader

    reader = PdfReader(str(path))
    pages: list[dict[str, Any]] = []
    for index, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        pages.append(
            {
                "number": index,
                "title": _title_from_lines(lines, f"Page {index}"),
                "lines": lines,
                "text": text,
            }
        )
    full_text = "\n\n".join(page["text"] for page in pages if page["text"])
    return {
        "kind": "pdf",
        "slide_count": None,
        "page_count": len(pages),
        "slides": pages,
        "full_text": full_text,
    }


def parse_material(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix == ".pptx":
        return parse_pptx(path)
    if suffix == ".pdf":
        return parse_pdf(path)
    raise ValueError(f"Unsupported material type: {path}")


def lecture_order(path: Path) -> float:
    name = path.name.lower()
    explicit: list[tuple[str, float]] = [
        ("week 1", 1.0),
        ("第二周", 2.0),
        ("第三周-part1", 3.1),
        ("第三周-part2", 3.2),
        ("wep", 4.1),
        ("wi-fi protected access", 4.2),
        ("wifi protected access", 4.2),
        ("wpa).pptx", 4.2),
        ("wpa2", 4.3),
        ("week 7", 7.0),
        ("lecture 12", 12.0),
        ("lecture 13", 13.0),
        ("lecture 14", 14.0),
    ]
    for marker, order in explicit:
        if marker in name:
            return order
    match = re.search(r"(?:lecture|week)\s*(\d+)", name)
    if match:
        return float(match.group(1))
    return 999.0


def write_extraction(path: Path, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(path.name)
    parsed = parse_material(path)
    payload = {
        "slug": slug,
        "title": path.stem,
        "filename": path.name,
        "extension": path.suffix.lower().lstrip("."),
        **parsed,
    }
    output_path = output_dir / f"{slug}.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "slug": slug,
        "title": path.stem,
        "filename": path.name,
        "extension": path.suffix.lower().lstrip("."),
        "order": lecture_order(path),
        "extraction": str(output_path.as_posix()),
        "slide_count": parsed["slide_count"],
        "page_count": parsed["page_count"],
        "text_chars": len(parsed["full_text"]),
    }


def discover_materials(source_dir: Path) -> list[Path]:
    paths = [
        path
        for path in source_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES and not path.name.startswith(".")
    ]
    return sorted(paths, key=lambda path: (lecture_order(path), path.name.lower()))


def extract_all(source_dir: Path, output_dir: Path, manifest_path: Path) -> list[dict[str, Any]]:
    records = [write_extraction(path, output_dir) for path in discover_materials(source_dir)]
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path("materials"))
    parser.add_argument("--output-dir", type=Path, default=Path("content/extracted"))
    parser.add_argument("--manifest", type=Path, default=Path("content/materials.json"))
    args = parser.parse_args()

    records = extract_all(args.source_dir, args.output_dir, args.manifest)
    print(f"Extracted {len(records)} materials to {args.output_dir}")


if __name__ == "__main__":
    main()
