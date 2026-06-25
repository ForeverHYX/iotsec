# 发现与决策

## 需求
- 为当前文件夹课程资料按章节整理复习笔记。
- 笔记目标：快速理解所有应知概念和考试需要掌握的知识。
- 将原始资料和笔记上传到用户的 GitHub。
- 使用 GitHub Pages 部署在线阅读网站，可查看 PPT/PDF 和总结笔记。
- GitHub 仓库必须创建为公开仓库。
- 新增用户提供的两份历年卷回忆，补全题干选项和参考答案，并加入网站。
- 继续优化章节笔记：所有末尾快速自测要有可折叠参考答案，知识讲解要更详细，并重新 build/push 网站。

## 当前资料清单
- `Week 1-2026.pdf`
- `第二周 无线基础2023 pdf.pdf`
- `第三周-part1-无线通信MAC层.pptx`
- `第三周-part2-蜂窝网络安全.pptx`
- `第四周Wired Equivalent Privacy (WEP).pptx`
- `第四周WiFi Protected Access (WPA).pptx`
- `第四周Protected Access 2 (WPA2).pptx`
- `Week 7 IoT and Its Security(1).pptx`
- `Lecture 12 RFID Security and Privacy.pptx`
- `Lecture 13 Bluetooth Security and Privacy.pptx`
- `Lecture 14 NFC Application Security(1).pptx`

## 研究发现
- 初始检查显示当前目录不是 git 仓库。
- 目录中暂未发现已有网站源码、笔记或部署配置。
- GitHub CLI 已登录账号 `ForeverHYX`，具有 `repo` 权限，git 协议为 SSH。
- 本机可用：`python3`、`node`、`npm`、`gh`、`git`。
- 本机缺少：`pandoc`、`libreoffice/soffice`、`pdftotext`、`convert/magick`、`mutool`、`qpdf`。
- Python 包检查：`PyPDF2` 可用；`python-pptx`、`pypdf`、`PyMuPDF`、`pdfminer` 缺失。
- 已将 11 份原始课件移动到 `materials/`。
- 已生成抽取文本目录 `content/extracted/` 和清单 `content/materials.json`。
- 已生成 11 篇章节复习笔记和 1 篇总复习索引，目录为 `notes/`。
- 已生成前端笔记清单 `content/notes.json`，11 份课件均有对应笔记。
- 已创建静态阅读网站：`index.html`、`assets/styles.css`、`assets/app.js`。
- 已创建 public GitHub 仓库：`https://github.com/ForeverHYX/iotsec`
- 已部署 GitHub Pages：`https://foreverhyx.github.io/iotsec/`
- Pages 当前状态：`built`，`build_type=workflow`，HTTPS 已启用。
- 新增历年卷资料为用户回忆文本，不是原始扫描卷；需要标注“回忆版/模拟补全”。
- 已新增 `notes/past-exams.md`，包含回忆卷 A 选择/填空、简答题池，以及 2024-2025 大题回忆。
- 已扩展 `content/notes.json` 的 `search_text` 字段，支持正文关键词搜索。
- 线上历年卷页面已验证：`https://foreverhyx.github.io/iotsec/#past-exams`
- 已为 11 篇章节笔记的“快速自测”增加折叠参考答案，并补充无线基础、MAC、蜂窝、WEP/WPA/WPA2、IoT、RFID、Bluetooth、NFC 等关键机制说明。
- 历年卷页面原本直接展示 30 个参考答案；已按用户要求改为默认折叠显示。
- 新一轮 subagent 初审结论：课程笔记正确但偏考前提纲，零基础读者缺少“机制怎么一步步发生”和“术语首次出现时是什么意思”的解释桥梁。
- 已给 11 篇课程笔记增加零基础导读、知识地图和初学者常见疑问，并覆盖 subagent 指出的关键术语和流程缺口。
- 阶段 10 返修后，新一轮 subagent 复审通过；最后两个修正点是 WEP fragmentation 的 64 bytes 总量推导，以及 SigOver 定量结果必须解释为每 UE 每小时请求率而非设备数量。
- 阶段 10 已部署到 GitHub Pages，workflow `28180254014` 成功，线上原始 Markdown 和 `content/notes.json` 已验证包含新增零基础讲解内容。

## 技术决策
| 决策 | 理由 |
|------|------|
| 将原始课件保留在 `materials/` 或等价公开目录中 | 方便 GitHub Pages 直接链接查看/下载 |
| 生成 Markdown 笔记作为内容源，再渲染成静态网站 | 便于复习、维护、GitHub 阅读和 Pages 构建 |
| 优先使用无需后端的静态站点 | GitHub Pages 原生支持，部署风险低 |
| 默认 GitHub 仓库名使用 `iotsec` | 与当前目录一致，便于 Pages URL 直观 |
| 使用 Python 库/脚本抽取课件文本 | 当前环境缺少常见文档转换命令 |
| PPTX 使用 `zipfile` + XML 解析，PDF 使用 `PyPDF2` | 不引入额外安装依赖，适合直接在当前环境运行 |
| GitHub 仓库创建为 public | 用户明确要求默认 public |
| 网站直接使用原生 HTML/CSS/JS | GitHub Pages 可直接托管，不需要构建步骤 |
| 使用 GitHub Actions Pages workflow 部署 | legacy Pages build 失败，workflow artifact 部署成功 |
| 历年卷做成独立 Markdown 笔记页 | 复用现有网站目录、搜索、Markdown 渲染和 GitHub Pages 部署流程 |
| 为笔记 manifest 增加正文搜索索引 | 历年卷页面需要通过 hidden、WEP、RFID 等正文关键词被搜到 |
| 仅允许受控 self-test `<details>`/`<summary>` HTML 通过 Markdown 渲染 | 满足折叠答案需求，同时继续转义其它正文内容，避免任意 HTML 注入 |

## 遇到的问题
| 问题 | 解决方案 |
|------|---------|
| 当前目录不是 git 仓库 | 后续初始化 git 并创建/连接 GitHub 仓库 |
| 缺少文档转换命令 | 使用 Python 解析 pptx/pdf，网站直接链接原始课件 |
| 缺少 `python-pptx` | 使用标准库解析 PPTX 内部 OOXML 文本 |
| legacy Pages build failed | 切换到 GitHub Actions Pages workflow |

## 资源
- 规划文件：`task_plan.md`、`findings.md`、`progress.md`
- 原始课件目录：`materials/`
- 抽取文本目录：`content/extracted/`
- 资料清单：`content/materials.json`
- 复习笔记目录：`notes/`
- 网站入口：`index.html`
- GitHub 仓库：`https://github.com/ForeverHYX/iotsec`
- GitHub Pages：`https://foreverhyx.github.io/iotsec/`
- 历年卷页面：`https://foreverhyx.github.io/iotsec/#past-exams`

## 视觉/浏览器发现
<!-- 关键：每执行2次查看/浏览器操作后必须更新此部分 -->
<!-- 多模态内容必须立即以文本形式记录 -->
- 尚未进行视觉/浏览器检查。

---
*每执行2次查看/浏览器/搜索操作后更新此文件*
*防止视觉信息丢失*
