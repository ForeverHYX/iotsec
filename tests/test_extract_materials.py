import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.extract_materials import parse_pptx, slugify, write_extraction


def make_pptx(path: Path, slides: dict[int, list[str]]) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        for number, lines in slides.items():
            text_nodes = "".join(f"<a:t>{line}</a:t>" for line in lines)
            archive.writestr(
                f"ppt/slides/slide{number}.xml",
                (
                    '<?xml version="1.0" encoding="UTF-8"?>'
                    '<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
                    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                    f"{text_nodes}"
                    "</p:sld>"
                ),
            )


class ExtractMaterialsTests(unittest.TestCase):
    def test_parse_pptx_sorts_slides_and_extracts_titles(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "deck.pptx"
            make_pptx(
                path,
                {
                    10: ["Late Slide", "appears after slide 2"],
                    1: ["Opening", "first concept"],
                    2: ["Second", "second concept"],
                },
            )

            result = parse_pptx(path)

        self.assertEqual([slide["number"] for slide in result["slides"]], [1, 2, 10])
        self.assertEqual(result["slides"][0]["title"], "Opening")
        self.assertIn("first concept", result["slides"][0]["text"])

    def test_slugify_removes_extension_and_normalizes_ascii(self):
        self.assertEqual(
            slugify("Lecture 12 RFID Security and Privacy.pptx"),
            "lecture-12-rfid-security-and-privacy",
        )

    def test_write_extraction_writes_json_with_summary_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "Lecture 12 RFID Security and Privacy.pptx"
            output_dir = Path(tmp) / "out"
            make_pptx(source, {1: ["RFID Security", "Tag tracking"], 2: ["Privacy", "Kill command"]})

            record = write_extraction(source, output_dir)
            payload = json.loads((output_dir / "lecture-12-rfid-security-and-privacy.json").read_text())

        self.assertEqual(record["slug"], "lecture-12-rfid-security-and-privacy")
        self.assertEqual(payload["slide_count"], 2)
        self.assertEqual(payload["slides"][1]["title"], "Privacy")


if __name__ == "__main__":
    unittest.main()
