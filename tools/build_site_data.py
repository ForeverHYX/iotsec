#!/usr/bin/env python3
"""Build JSON metadata used by the static review site."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def _parse_scalar(value: str) -> str | float:
    cleaned = value.strip()
    if (cleaned.startswith('"') and cleaned.endswith('"')) or (
        cleaned.startswith("'") and cleaned.endswith("'")
    ):
        return cleaned[1:-1]
    try:
        return float(cleaned) if "." in cleaned else int(cleaned)
    except ValueError:
        return cleaned


def parse_frontmatter(markdown: str) -> tuple[dict[str, Any], str]:
    if not markdown.startswith("---\n"):
        return {}, markdown
    end = markdown.find("\n---\n", 4)
    if end == -1:
        return {}, markdown
    raw_meta = markdown[4:end]
    body = markdown[end + len("\n---\n") :]
    meta: dict[str, Any] = {}
    for line in raw_meta.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = _parse_scalar(value)
    return meta, body


def _slug_from_note(path: Path) -> str:
    return re.sub(r"[^a-zA-Z0-9.-]+", "-", path.stem.lower()).strip("-")


def build_notes_manifest(notes_dir: Path, materials_manifest: Path, output_path: Path) -> list[dict[str, Any]]:
    materials = json.loads(materials_manifest.read_text(encoding="utf-8"))
    materials_by_slug = {item["slug"]: item for item in materials}
    project_root = notes_dir.parent
    records: list[dict[str, Any]] = []
    for note_path in sorted(notes_dir.glob("*.md")):
        markdown = note_path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(markdown)
        slug = _slug_from_note(note_path)
        material = materials_by_slug.get(slug)
        order = meta.get("order", material.get("order", 999) if material else 999)
        record = {
            "slug": slug,
            "title": meta.get("title", note_path.stem),
            "source": meta.get("source", ""),
            "order": order,
            "note_path": note_path.relative_to(project_root).as_posix(),
            "word_count": len(re.findall(r"[\w\u4e00-\u9fff]+", body)),
            "material": material,
        }
        records.append(record)

    records.sort(key=lambda item: (float(item["order"]), item["title"]))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes-dir", type=Path, default=Path("notes"))
    parser.add_argument("--materials", type=Path, default=Path("content/materials.json"))
    parser.add_argument("--output", type=Path, default=Path("content/notes.json"))
    args = parser.parse_args()

    records = build_notes_manifest(args.notes_dir, args.materials, args.output)
    print(f"Built {len(records)} note records at {args.output}")


if __name__ == "__main__":
    main()
