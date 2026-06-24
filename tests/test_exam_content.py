import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExamContentTests(unittest.TestCase):
    def test_past_exams_page_is_in_site_manifest(self):
        notes = json.loads((ROOT / "content" / "notes.json").read_text(encoding="utf-8"))
        slugs = {note["slug"] for note in notes}
        self.assertIn("past-exams", slugs)

    def test_past_exams_page_covers_recalled_major_questions(self):
        text = (ROOT / "notes" / "past-exams.md").read_text(encoding="utf-8")
        required_terms = [
            "Hidden Terminal",
            "WEP 加密过程",
            "WPA2 四次握手",
            "智能家居监控系统",
            "Security Demands",
            "Security Architecture",
            "RFID tag 和 reader 之间传递敏感信息",
        ]
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
