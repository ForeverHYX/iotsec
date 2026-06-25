import assert from "node:assert/strict";
import test from "node:test";
import { markdownToHtml, noteMatchesQuery, viewerForMaterial } from "../assets/app.js";

test("markdownToHtml removes frontmatter and renders headings and bullets", () => {
  const html = markdownToHtml(`---
title: "Demo"
---
# Demo

## Items

- one
- **two**
`);

  assert.match(html, /<h1>Demo<\/h1>/);
  assert.match(html, /<h2>Items<\/h2>/);
  assert.match(html, /<li>one<\/li>/);
  assert.match(html, /<strong>two<\/strong>/);
  assert.doesNotMatch(html, /title:/);
});

test("markdownToHtml preserves collapsible self-test answer blocks", () => {
  const html = markdownToHtml(`## 快速自测

1. Question?

<details class="self-test-answer">
<summary>参考答案</summary>

1. **Answer** uses \`nonce\`.

</details>
`);

  assert.match(html, /<details class="self-test-answer">/);
  assert.match(html, /<summary>参考答案<\/summary>/);
  assert.match(html, /<li><strong>Answer<\/strong> uses <code>nonce<\/code>\.<\/li>/);
  assert.match(html, /<\/details>/);
  assert.doesNotMatch(html, /&lt;details/);
});

test("viewerForMaterial uses direct PDF links and Office viewer for PPTX", () => {
  const pdf = viewerForMaterial({ filename: "Week 1-2026.pdf", extension: "pdf" }, "https://example.com/iotsec/");
  const pptx = viewerForMaterial(
    { filename: "Lecture 12 RFID Security and Privacy.pptx", extension: "pptx" },
    "https://example.com/iotsec/",
  );

  assert.equal(pdf.type, "pdf");
  assert.equal(pdf.url, "https://example.com/iotsec/materials/Week%201-2026.pdf");
  assert.equal(pptx.type, "office");
  assert.match(pptx.url, /^https:\/\/view\.officeapps\.live\.com\/op\/embed\.aspx\?src=/);
  assert.match(decodeURIComponent(pptx.url), /Lecture%2012%20RFID%20Security%20and%20Privacy\.pptx/);
});

test("noteMatchesQuery searches note body index", () => {
  const note = {
    title: "历年卷回忆题与参考答案",
    source: "student recollection",
    slug: "past-exams",
    search_text: "Hidden Terminal WEP 加密过程 Security Demands",
  };

  assert.equal(noteMatchesQuery(note, "hidden"), true);
  assert.equal(noteMatchesQuery(note, "Security Demands"), true);
  assert.equal(noteMatchesQuery(note, "not-present"), false);
});
