const state = {
  notes: [],
  activeSlug: "",
  activeTab: "note",
};

function stripFrontmatter(markdown) {
  return markdown.replace(/^---\n[\s\S]*?\n---\n/, "");
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function inlineMarkdown(value) {
  return escapeHtml(value)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
}

function flushList(html, list) {
  if (!list) return null;
  html.push(`<${list.type}>${list.items.map((item) => `<li>${inlineMarkdown(item)}</li>`).join("")}</${list.type}>`);
  return null;
}

function renderAllowedHtmlBlock(line) {
  if (line === '<details class="self-test-answer">') return line;
  if (line === "</details>") return line;
  const summary = line.match(/^<summary>(.+)<\/summary>$/);
  if (summary) {
    return `<summary>${inlineMarkdown(summary[1])}</summary>`;
  }
  return null;
}

export function markdownToHtml(markdown) {
  const lines = stripFrontmatter(markdown).replace(/\r\n/g, "\n").split("\n");
  const html = [];
  let paragraph = [];
  let list = null;

  const flushParagraph = () => {
    if (!paragraph.length) return;
    html.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
    paragraph = [];
  };

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      flushParagraph();
      list = flushList(html, list);
      continue;
    }

    const htmlBlock = renderAllowedHtmlBlock(trimmed);
    if (htmlBlock) {
      flushParagraph();
      list = flushList(html, list);
      html.push(htmlBlock);
      continue;
    }

    const heading = trimmed.match(/^(#{1,3})\s+(.+)$/);
    if (heading) {
      flushParagraph();
      list = flushList(html, list);
      const level = heading[1].length;
      html.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
      continue;
    }

    const bullet = trimmed.match(/^[-*]\s+(.+)$/);
    if (bullet) {
      flushParagraph();
      if (!list || list.type !== "ul") list = flushList(html, list) || { type: "ul", items: [] };
      list.items.push(bullet[1]);
      continue;
    }

    const ordered = trimmed.match(/^\d+\.\s+(.+)$/);
    if (ordered) {
      flushParagraph();
      if (!list || list.type !== "ol") list = flushList(html, list) || { type: "ol", items: [] };
      list.items.push(ordered[1]);
      continue;
    }

    list = flushList(html, list);
    paragraph.push(trimmed);
  }

  flushParagraph();
  flushList(html, list);
  return html.join("\n");
}

function encodedMaterialUrl(filename, baseUrl) {
  const encoded = filename.split("/").map(encodeURIComponent).join("/");
  return new URL(`materials/${encoded}`, baseUrl).href;
}

export function viewerForMaterial(material, baseUrl = window.location.href) {
  if (!material) return { type: "none", url: "" };
  const directUrl = encodedMaterialUrl(material.filename, baseUrl);
  if (material.extension === "pdf") {
    return { type: "pdf", url: directUrl };
  }
  if (material.extension === "pptx") {
    const office = `https://view.officeapps.live.com/op/embed.aspx?src=${encodeURIComponent(directUrl)}`;
    return { type: "office", url: office, directUrl };
  }
  return { type: "download", url: directUrl };
}

function orderLabel(order) {
  if (Number(order) === 0) return "总";
  return String(order).replace(".0", "");
}

function noteMeta(note) {
  const material = note.material;
  if (!material) return "总复习";
  const count = material.slide_count ? `${material.slide_count} slides` : `${material.page_count} pages`;
  return `${material.extension.toUpperCase()} · ${count}`;
}

export function noteMatchesQuery(note, query) {
  const normalized = query.trim().toLowerCase();
  if (!normalized) return true;
  return `${note.title} ${note.source} ${note.slug} ${note.search_text || ""}`.toLowerCase().includes(normalized);
}

function renderChapterList(filter = "") {
  const target = document.querySelector("#chapterList");
  const notes = state.notes.filter((note) => noteMatchesQuery(note, filter));

  target.innerHTML = notes
    .map(
      (note) => `
        <button class="chapter-button ${note.slug === state.activeSlug ? "active" : ""}" type="button" data-slug="${note.slug}">
          <span class="chapter-order">${orderLabel(note.order)}</span>
          <span>
            <span class="chapter-title">${escapeHtml(note.title)}</span>
            <span class="chapter-meta">${escapeHtml(noteMeta(note))}</span>
          </span>
        </button>
      `,
    )
    .join("");

  target.querySelectorAll("[data-slug]").forEach((button) => {
    button.addEventListener("click", () => selectNote(button.dataset.slug));
  });
}

function setTab(tab) {
  state.activeTab = tab;
  document.querySelector("#noteTab").classList.toggle("active", tab === "note");
  document.querySelector("#materialTab").classList.toggle("active", tab === "material");
  document.querySelector("#noteTab").setAttribute("aria-selected", String(tab === "note"));
  document.querySelector("#materialTab").setAttribute("aria-selected", String(tab === "material"));
  document.querySelector("#notePanel").classList.toggle("active", tab === "note");
  document.querySelector("#materialPanel").classList.toggle("active", tab === "material");
}

async function selectNote(slug, options = { updateHash: true }) {
  const note = state.notes.find((item) => item.slug === slug) || state.notes[0];
  if (!note) return;

  state.activeSlug = note.slug;
  if (options.updateHash && window.location.hash !== `#${note.slug}`) {
    window.location.hash = note.slug;
  }
  renderChapterList(document.querySelector("#searchInput").value);

  document.querySelector("#chapterTitle").textContent = note.title;
  document.querySelector("#chapterKicker").textContent = `Chapter ${orderLabel(note.order)}`;
  document.querySelector("#noteDownload").href = note.note_path;

  const markdown = await fetch(note.note_path).then((response) => response.text());
  document.querySelector("#noteContent").innerHTML = markdownToHtml(markdown);
  renderMaterial(note.material);
}

async function handleHashChange() {
  const slug = window.location.hash.replace("#", "");
  if (slug && slug !== state.activeSlug) {
    await selectNote(slug, { updateHash: false });
  }
}

function renderMaterial(material) {
  const frame = document.querySelector("#materialFrame");
  const title = document.querySelector("#materialTitle");
  const hint = document.querySelector("#materialHint");
  const download = document.querySelector("#materialDownload");
  const open = document.querySelector("#openMaterial");
  const viewer = viewerForMaterial(material, window.location.href);

  if (!material) {
    title.textContent = "总复习索引";
    hint.textContent = "本页不绑定单个课件。";
    frame.removeAttribute("src");
    download.style.display = "none";
    open.style.display = "none";
    return;
  }

  const directUrl = viewer.directUrl || viewer.url;
  title.textContent = material.filename;
  download.style.display = "";
  open.style.display = "";
  download.href = directUrl;
  open.href = directUrl;

  if (viewer.type === "office") {
    hint.textContent = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1"
      ? "PPTX 在线预览需要公开 Pages 地址；本地可直接下载或打开课件。"
      : "";
    frame.src = viewer.url;
    return;
  }

  hint.textContent = "";
  frame.src = viewer.url;
}

async function init() {
  const notes = await fetch("content/notes.json").then((response) => response.json());
  state.notes = notes;

  document.querySelector("#searchInput").addEventListener("input", (event) => {
    renderChapterList(event.target.value);
  });
  document.querySelector("#noteTab").addEventListener("click", () => setTab("note"));
  document.querySelector("#materialTab").addEventListener("click", () => setTab("material"));
  window.addEventListener("hashchange", () => {
    handleHashChange().catch((error) => {
      document.querySelector("#noteContent").innerHTML = `<p>${escapeHtml(error.message)}</p>`;
    });
  });

  renderChapterList();
  const slug = window.location.hash.replace("#", "");
  await selectNote(slug || notes[0]?.slug);
}

if (typeof document !== "undefined") {
  init().catch((error) => {
    document.body.innerHTML = `<main class="empty-state">加载失败：${escapeHtml(error.message)}</main>`;
  });
}
