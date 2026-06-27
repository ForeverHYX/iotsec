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

    def test_past_exams_answers_are_collapsible(self):
        text = (ROOT / "notes" / "past-exams.md").read_text(encoding="utf-8")
        question_sections = [
            section for section in text.split("\n### ") if section[:1].isdigit()
        ]
        self.assertGreaterEqual(len(question_sections), 30)

        for section in question_sections:
            title = section.splitlines()[0]
            with self.subTest(question=title):
                self.assertIn('<details class="self-test-answer">', section)
                self.assertIn("<summary>参考答案</summary>", section)
                self.assertIn("</details>", section)

        direct_answer_lines = [
            line for line in text.splitlines() if line.startswith("参考答案")
        ]
        self.assertEqual([], direct_answer_lines)

    def test_mock_exams_are_in_site_manifest(self):
        notes = json.loads((ROOT / "content" / "notes.json").read_text(encoding="utf-8"))
        slugs = {note["slug"] for note in notes}
        self.assertIn("mock-exam-a", slugs)
        self.assertIn("mock-exam-b", slugs)
        self.assertIn("mock-exam-c", slugs)
        self.assertIn("mock-exam-d", slugs)

    def test_mock_exams_keep_recalled_exam_question_structure(self):
        for filename in ["mock-exam-a.md", "mock-exam-b.md"]:
            text = (ROOT / "notes" / filename).read_text(encoding="utf-8")
            with self.subTest(file=filename):
                self.assertIn("## 1. 模拟卷", text)
                self.assertIn("## 2. 简答题池", text)
                self.assertIn("## 3. 综合大题", text)
                self.assertEqual(20, text.count("### 客观题 "))
                self.assertEqual(6, text.count("### 简答题 "))
                self.assertEqual(4, text.count("### 大题 "))
                self.assertGreaterEqual(text.count('<details class="self-test-answer">'), 30)
                self.assertIn("Hidden Terminal", text)
                self.assertIn("WEP", text)
                self.assertIn("IoT Security", text)
                self.assertIn("RFID", text)
                self.assertIn("Bluetooth", text)

    def test_choice_short_answer_mock_exams_do_not_include_big_questions(self):
        for filename in ["mock-exam-c.md", "mock-exam-d.md"]:
            text = (ROOT / "notes" / filename).read_text(encoding="utf-8")
            with self.subTest(file=filename):
                self.assertIn("## 1. 选择题", text)
                self.assertIn("## 2. 简答题", text)
                self.assertNotIn("## 3. 综合大题", text)
                self.assertNotIn("### 大题 ", text)
                self.assertEqual(20, text.count("### 选择题 "))
                self.assertEqual(6, text.count("### 简答题 "))
                self.assertGreaterEqual(text.count('<details class="self-test-answer">'), 26)
                for term in ["Hidden Terminal", "WEP", "IoT Security", "RFID", "Bluetooth"]:
                    self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
