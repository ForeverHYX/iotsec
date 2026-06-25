import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "notes"
SELF_TEST_HEADING = re.compile(r"^##\s+\d+\.\s+快速自测\s*$", re.MULTILINE)
ORDERED_ITEM = re.compile(r"^\d+\.\s+", re.MULTILINE)


class SelfTestAnswerTests(unittest.TestCase):
    def test_all_chapter_self_tests_have_collapsible_answers(self):
        note_files = sorted(
            path
            for path in NOTES_DIR.glob("*.md")
            if path.name not in {"index.md", "past-exams.md"}
        )
        self.assertGreater(len(note_files), 0)

        for path in note_files:
            text = path.read_text(encoding="utf-8")
            match = SELF_TEST_HEADING.search(text)
            self.assertIsNotNone(match, f"{path.name} should contain a 快速自测 section")

            section = text[match.end():]
            with self.subTest(note=path.name):
                self.assertIn('<details class="self-test-answer">', section)
                self.assertIn("<summary>参考答案</summary>", section)
                self.assertIn("</details>", section)

                before_answers, answer_block = section.split('<details class="self-test-answer">', 1)
                question_count = len(ORDERED_ITEM.findall(before_answers))
                answer_count = len(ORDERED_ITEM.findall(answer_block))

                self.assertGreater(question_count, 0, "self-test should include questions")
                self.assertEqual(
                    question_count,
                    answer_count,
                    "collapsible answer block should answer each self-test question",
                )


if __name__ == "__main__":
    unittest.main()
