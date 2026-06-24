import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.build_site_data import build_notes_manifest, parse_frontmatter


class BuildSiteDataTests(unittest.TestCase):
    def test_parse_frontmatter_reads_title_source_and_order(self):
        markdown = """---
title: "Example Note"
source: "materials/example.pptx"
order: 3.2
---

# Example
"""
        meta, body = parse_frontmatter(markdown)

        self.assertEqual(meta["title"], "Example Note")
        self.assertEqual(meta["source"], "materials/example.pptx")
        self.assertEqual(meta["order"], 3.2)
        self.assertIn("# Example", body)

    def test_build_notes_manifest_sorts_notes_and_links_materials(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            notes_dir = root / "notes"
            content_dir = root / "content"
            notes_dir.mkdir()
            content_dir.mkdir()
            (notes_dir / "b.md").write_text(
                '---\ntitle: "B"\nsource: "materials/b.pptx"\norder: 2\n---\n# B\n',
                encoding="utf-8",
            )
            (notes_dir / "a.md").write_text(
                '---\ntitle: "A"\nsource: "materials/a.pdf"\norder: 1\n---\n# A\n',
                encoding="utf-8",
            )
            (content_dir / "materials.json").write_text(
                json.dumps(
                    [
                        {"slug": "b", "filename": "b.pptx", "order": 2},
                        {"slug": "a", "filename": "a.pdf", "order": 1},
                    ]
                ),
                encoding="utf-8",
            )

            records = build_notes_manifest(notes_dir, content_dir / "materials.json", content_dir / "notes.json")
            payload = json.loads((content_dir / "notes.json").read_text())

        self.assertEqual([record["slug"] for record in records], ["a", "b"])
        self.assertEqual(payload[0]["material"]["filename"], "a.pdf")
        self.assertEqual(payload[1]["note_path"], "notes/b.md")


if __name__ == "__main__":
    unittest.main()
