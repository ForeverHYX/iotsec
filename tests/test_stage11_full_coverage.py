import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "notes"
COURSE_NOTE_EXCLUDES = {"index.md", "past-exams.md"}
ORDERED_ITEM = re.compile(r"^\d+\.\s+", re.MULTILINE)

REQUIRED_TERMS = {
    "2023-pdf.md": [
        "Slow fading",
        "Shadowing Effect",
        "Doppler Effect",
        "Multi-path Propagation",
        "Breathing Effect",
        "major cause of slow fading",
        "Fast fading",
        "Rayleigh fading",
        "Rician fading",
        "Free-space path loss",
        "Nyquist formula",
        "Shannon capacity",
        "C = B log2(1 + S/N)",
        "Channel Interleave",
        "f = 1/T",
        "s(t)=A sin(2πft+φ)",
        "SNR_dB=10log10(P_signal/P_noise)",
        "f_d ≈ (v/λ)cosθ",
        "log-normal distribution",
        "inter-symbol interference (ISI)",
        "Barker code",
        "CCK",
        "Radio Access Network (RAN)",
        "CSMA/CA",
        "RTS/CTS",
        "near-far effect",
        "hidden terminal problem",
    ],
    "week-1-2026.md": [
        "NIST Computer Security Handbook",
        "System Resource",
        "Adversary",
        "Non-repudiability",
        "SDN/NFV/SDWN",
        "spectral efficiency = data rate / bandwidth",
        "Underlay / Interweave / Overlay",
        "D2D",
        "Massive MIMO",
        "OFDMA",
        "MLO",
        "FCC",
        "OSM",
        "ITU-R",
        "C = B log2(1 + SNR)",
    ],
    "part1-mac.md": [
        "hidden terminal problem",
        "exposed terminal problem",
        "RTS/CTS",
        "DIFS",
        "SIFS",
        "NAV",
        "Use illustration",
        "Polling",
        "Token passing",
        "Taking-turns MAC protocols",
        "maximum propagation delay",
        ">= 2 * maximum propagation delay",
        "hears RTS but does not hear CTS",
        "may still transmit",
    ],
    "part2.md": [
        "Signal Overshadowing Attack",
        "Capture Effect",
        "What principle does signal Overshadowing utilize",
        "How is the attack implemented",
        "malicious subframe",
        "PSS/SSS",
        "GPSDO",
        "LTE - Long Term Evolution",
        "LOS/NLOS",
        "10 us",
        "+-90 Hz @ 1.8 GHz",
        "+-45 Hz @ 1.8 GHz",
        "m = c XOR c' XOR m'",
        "3/15",
        "12/15",
    ],
    "wired-equivalent-privacy-wep.md": [
        "Wi-Fi Alliance",
        "2.4 GHz and 5 GHz public spectrum bands",
        "Authenticity",
        "Replay detection",
        "Protection against jamming",
        "256 bit = 232-bit key + 24-bit IV",
        "first byte 3..7",
        "second byte 255",
        "third byte anything",
        "9000 weak IVs",
        "5% of IVs",
        "AirSnort",
        "AA AA 03 00 00 00 08",
    ],
    "wifi-protected-access-wpa.md": [
        "active countermeasures",
        "EAPOL-Start",
        "AS",
        "PSK = PBKDF2(Password, SSID, SSIDlength, 4096, 256)",
        "PTK = HASH(PMK, ANonce, SNonce, STA MAC Address, AP MAC Address)",
        "62^8 = 218,340,105,584,896",
        "280GTX",
        "11000 keys/sec",
        "630 years",
        "12-char passphrase",
        "9,309,091,680 years",
        "Phase 1",
        "Phase 2",
        "16-bit monotonically incrementing counter",
        "1st and 3rd bytes of the old IV",
        "reset packet sequence to 0",
        "increment by 1 per packet",
        "drop out-of-sequence packets",
    ],
    "protected-access-2-wpa2.md": [
        "MSK",
        "MK",
        "Supplicant",
        "Authenticator",
        "EAPOL-start",
        "Radius-access-accept",
        "WEP RC4/40-bit/24-bit IV",
        "Nonce reuse implies keystream reuse",
        "Abstract model != real code",
    ],
    "week-7-iot-and-its-security-1.md": [
        "Auto-ID Center",
        "EPC system",
        "Object equalization",
        "ad-hoc terminal interconnection",
        "δ = sign(∇x J(θ, x, y))",
        "MCD",
        "RTF",
        "PhoneyTalker",
        "PhyTalker",
        "Privacy-Utility Dilemma",
        "trust management",
        "malicious-node access",
        "monitoring/destruction of transmitted data",
        "poor data consistency",
        "congestion-driven DoS",
        "outsourced-data privacy",
        "ciphertext retrieval/operation",
        "anti-detection",
        "anti-radiation",
        "physical secrecy",
        "digital signatures",
        "security protocols",
        "pervasive service intellectualization",
    ],
    "lecture-12-rfid-security-and-privacy.md": [
        "Transceiver",
        "middleware",
        "SHF",
        "125kHz",
        "high-frequency interface module",
        "local oscillator",
        "mixer",
        "circulator",
        "I-Q output",
        "Pure ALOHA utilization 18.4%",
        "(a · x) ⊕ v",
        "(a · x) ⊕ (b · y) ⊕ v",
        "Qfp",
        "C=0.1-0.5",
        "self-organizing networking ability",
        "multi-antenna management",
        "middleware interface",
        "peripheral connection",
        "reader/application-layer communication security",
        "v=1 with probability η",
        "repeat r times",
        "fewer than ηr",
        "repeated non-random challenges",
        "majority vote",
        "ALOHA starvation",
        "random binary tree counter",
        "FSA/random tree/query tree",
        "t × s + tag-estimation time",
        "n × s",
        "8/16-bit",
        "O(n)",
        "θ(nlogn)",
        "θ(n)",
        "n × (k + 2 - log n)",
        "k × (2.21 log n + 4.19)",
        "n = number of tags",
        "k = tag ID length",
        "N = estimate of n",
    ],
    "lecture-13-bluetooth-security-and-privacy.md": [
        "Harald \"Bluetooth\" Gormsson",
        "SIG",
        "PAN",
        "RS-232",
        "EDR",
        "HS",
        "TDMA-TDD-Slow Frequency Hopping",
        "GFSK",
        "Wibree",
        "SSP",
        "E0",
        "RNG",
        "RAND",
        "1 Mbit/s",
        "3 Mbit/s",
        "24 Mbit/s",
        "ADV_DIRECT_IND 3.75ms for 1.28s",
        "adv' = E(t_i) - 5",
        "10 m",
        "100 m",
        "1600 hops/sec over 79 frequencies",
        "37x2MHz",
        "79x1MHz",
        "increased GMSK modulation index",
        "3ms",
        ">100ms",
        "FEC/fast ACK",
        "Lazy Acknowledgement",
        "24-bit CRC",
        "32-bit Message Integrity Check",
        "Blue snarfing",
    ],
    "lecture-14-nfc-application-security-1.md": [
        "Initiator/Target",
        "FWI/SFGI/FWT/fc",
        "BCC/INT/LOCK0/LOCK1/BL",
        "Secure MicroSD",
        "ObC",
        "OTA",
        "FWT = (256 × 16 / fc) × 2^FWI",
        "FWI=8 ≈77ms",
        "SHA-256(salt || PIN)",
        "FWI=0 ≈303μs",
        "FWI=4 ≈4833μs",
        "FWI=14 ≈4949ms",
        "MIFARE DESFire default FWI=0x8",
        "430ms",
        "readers often ignore FWT configuration",
        "contactless EMV relay",
        "proxy token requires card emulation",
        "UID spoofing is not needed",
        "travel account in SP cloud",
        "ticket identity/travel info",
        "Transport Authority",
        "six PIN tries",
        "offline guessing outside that counter",
    ],
}


class Stage11FullCoverageTests(unittest.TestCase):
    def test_every_course_note_has_glossary_formula_and_exam_drill_sections(self):
        note_files = sorted(
            path
            for path in NOTES_DIR.glob("*.md")
            if path.name not in COURSE_NOTE_EXCLUDES
        )
        self.assertEqual(11, len(note_files))

        for path in note_files:
            text = path.read_text(encoding="utf-8")
            with self.subTest(note=path.name):
                self.assertIn("## 公式与术语速查", text)
                self.assertIn("## 历年卷风格练习", text)

                glossary = self._section(text, "## 公式与术语速查")
                self.assertGreaterEqual(
                    len(re.findall(r"^\|.+\|$|^-\s+", glossary, re.MULTILINE)),
                    8,
                    "glossary/formula section should define enough terms for beginners",
                )

                drill = self._section(text, "## 历年卷风格练习")
                self.assertIn('<details class="self-test-answer">', drill)
                self.assertIn("<summary>参考答案</summary>", drill)
                self.assertIn("</details>", drill)
                before_answers, answer_block = drill.split('<details class="self-test-answer">', 1)
                self.assertGreaterEqual(
                    len(ORDERED_ITEM.findall(before_answers)),
                    3,
                    "exam-style drill should include at least three questions",
                )
                self.assertGreaterEqual(
                    len(ORDERED_ITEM.findall(answer_block)),
                    len(ORDERED_ITEM.findall(before_answers)),
                    "folded answer block should answer every exam-style question",
                )

    def test_user_reported_exam_gaps_are_explicitly_covered(self):
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
