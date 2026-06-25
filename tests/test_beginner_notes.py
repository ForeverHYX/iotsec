import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "notes"
COURSE_NOTE_EXCLUDES = {"index.md", "past-exams.md"}

REQUIRED_TERMS = {
    "week-1-2026.md": [
        "Shannon limit", "频谱复用", "IoT 四层", "智能网联汽车", "IoT 历史", "CPS", "CAN", "e-cockpit",
        "licensed/unlicensed", "SD radio", "SDWN",
    ],
    "2023-pdf.md": [
        "基带", "射频", "ASK", "QAM", "Nyquist", "Shannon", "RAN", "核心网", "sampling", "quantization",
        "source coding", "channel coding", "授权频段", "免授权频段", "天线", "标准演进",
    ],
    "part1-mac.md": ["理想 MAC", "R/M", "CCA", "NAV", "轮询", "令牌", "DIFS 空闲则发送", "控制信道", "MANET"],
    "part2.md": [
        "UE", "eNodeB", "RRC", "PCFICH", "PDCCH", "PDSCH", "Bearer", "COUNT", "45 vs 21600",
        "675 vs 432000", "640 倍", "3 台 UE", "USRP B210", "89%", "加密 RTP",
    ],
    "wired-equivalent-privacy-wep.md": [
        "LLC/SNAP", "ARP replay", "共享密钥认证四步", "5000", "9000", "20,000 packets",
        "16 fragments", "64 bytes", "不能进一步正常访问网络", "2005",
    ],
    "wifi-protected-access-wpa.md": [
        "TKIP 加密一帧", "EAPOL", "RADIUS", "Beck-Tews", "QoS", "630 年", "rainbow table",
        "8 QoS channels", "2 MIC failures/min", "Michael 8 bytes", "128 bits",
    ],
    "protected-access-2-wpa2.md": [
        "RSN IE", "Association Request", "GTK", "PMK Caching", "Pre-authentication", "KRACK 时间线",
        "data flooding", "AP failure", "128-bit AES", "PTK 64 bytes", "KCK/KEK/TK 各 16 bytes",
    ],
    "week-7-iot-and-its-security-1.md": [
        "贯穿例子", "Shadow IoT", "LPWAN", "语音感知安全", "embedding", "DAS/NAS/SAN", "IaaS/PaaS/SaaS",
    ],
    "lecture-12-rfid-security-and-privacy.md": [
        "负载调制", "反向散射", "4 个标签", "LPN", "dot product", "HB+", "基带控制模块", "射频模块",
        "RN16", "协方差", "PDoT", "相位偏移",
    ],
    "lecture-13-bluetooth-security-and-privacy.md": [
        "625 微秒", "Classic vs BLE", "AES-CCM", "ADV_IND", "BLE-Guardian", "TI sniffer", "Ubertooth",
        "LightBlue", "downgrade attack",
    ],
    "lecture-14-nfc-application-security-1.md": [
        "REQA", "ATQA", "RATS", "APDU", "FWT", "Type 1/2/3/4", "malformed tag", "USSD",
        "remote attestation", "secure provisioning", "Hash(UID + Master key)", "OTP counter", "open payment",
    ],
}


class BeginnerNotesTests(unittest.TestCase):
    def test_course_notes_include_beginner_learning_sections(self):
        note_files = sorted(
            path
            for path in NOTES_DIR.glob("*.md")
            if path.name not in COURSE_NOTE_EXCLUDES
        )
        self.assertEqual(11, len(note_files))

        for path in note_files:
            text = path.read_text(encoding="utf-8")
            with self.subTest(note=path.name):
                self.assertIn("## 零基础导读", text)
                self.assertIn("## 本章知识地图", text)
                self.assertIn("## 初学者常见疑问", text)
                self.assertGreaterEqual(text.count("问："), 2)
                self.assertGreaterEqual(text.count("答："), 2)

    def test_beginner_sections_have_real_explanatory_density(self):
        note_files = sorted(
            path
            for path in NOTES_DIR.glob("*.md")
            if path.name not in COURSE_NOTE_EXCLUDES
        )

        for path in note_files:
            text = path.read_text(encoding="utf-8")
            with self.subTest(note=path.name):
                beginner_section = self._section(text, "## 零基础导读")
                map_section = self._section(text, "## 本章知识地图")
                faq_section = self._section(text, "## 初学者常见疑问")

                self.assertGreaterEqual(len(re.findall(r"[\u4e00-\u9fff]", beginner_section)), 220)
                self.assertGreaterEqual(len(re.findall(r"^\d+\.|^- ", map_section, re.MULTILINE)), 4)
                self.assertGreaterEqual(len(re.findall(r"[\u4e00-\u9fff]", faq_section)), 220)

    def test_notes_cover_subagent_identified_beginner_gaps(self):
        for filename, terms in REQUIRED_TERMS.items():
            text = (NOTES_DIR / filename).read_text(encoding="utf-8")
            for term in terms:
                with self.subTest(note=filename, term=term):
                    self.assertIn(term, text)

    def _section(self, text: str, heading: str) -> str:
        start = text.find(heading)
        self.assertNotEqual(-1, start)
        next_heading = text.find("\n## ", start + len(heading))
        if next_heading == -1:
            return text[start:]
        return text[start:next_heading]


if __name__ == "__main__":
    unittest.main()
