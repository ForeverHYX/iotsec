import assert from "node:assert/strict";
import test from "node:test";
import { markdownToHtml, viewerForMaterial } from "../assets/app.js";

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
