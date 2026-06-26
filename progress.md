# 进度日志

## 会话：2026-06-24

### 阶段 1：需求与发现
- **状态：** complete
- **开始时间：** 2026-06-24 Asia/Shanghai
- 执行的操作：
  - 读取规划技能说明。
  - 盘点当前目录，发现 11 份课程资料。
  - 检查 git 状态，确认当前目录不是 git 仓库。
  - 创建项目规划文件。
  - 检查可用工具和 GitHub CLI 登录状态。
- 创建/修改的文件：
  - `task_plan.md`
  - `findings.md`
  - `progress.md`

### 阶段 2：资料抽取与内容规划
- **状态：** complete
- 执行的操作：
  - 发现缺少 LibreOffice/pandoc/poppler 等转换工具，决定用 Python 抽取文本。
  - 编写 `tools/extract_materials.py`，用标准库解析 PPTX、用 PyPDF2 解析 PDF。
  - 编写并运行 `tests/test_extract_materials.py`，验证 PPTX 排序、slug、JSON 输出。
  - 将 11 份课件移动到 `materials/` 并运行抽取脚本。
  - 用户要求 GitHub 仓库默认设为 public，已记录为部署约束。
- 创建/修改的文件：
  - `tools/extract_materials.py`
  - `tests/test_extract_materials.py`
  - `materials/*`
  - `content/extracted/*.json`
  - `content/materials.json`

### 阶段 3：复习笔记生成
- **状态：** complete
- 执行的操作：
  - 为 11 份课件分别生成中文复习笔记。
  - 生成 `notes/index.md` 总复习索引。
  - 每篇笔记包含速览、核心概念、考试重点、易混点和自测题。
- 创建/修改的文件：
  - `notes/*.md`

### 阶段 4：静态阅读网站
- **状态：** complete
- 执行的操作：
  - 编写 `tools/build_site_data.py` 和测试，生成 `content/notes.json`。
  - 创建 `index.html`、`assets/styles.css`、`assets/app.js`。
  - 实现章节目录、搜索、笔记渲染、课件下载和 PDF/PPTX 预览入口。
  - 运行完整测试套件，确认通过。
  - 启动本地 HTTP 服务 `http://localhost:4173/`。
  - 用 agent-browser 验证章节列表、搜索过滤、章节切换、课件面板、hash 路由。
  - 发现 hash 路由在旧模块中不响应，补充 `hashchange` 监听后验证通过。
  - 截图检查桌面和移动布局；PPTX 本地 Office viewer 预览因 localhost 不可公开访问而报错，已在页面提示，部署到公开 Pages 后会使用公开 URL。
  - 添加 `.gitignore` 和 `.nojekyll`。
- 创建/修改的文件：
  - `tools/build_site_data.py`
  - `tests/test_build_site_data.py`
  - `tests/test_app_utils.mjs`
  - `content/notes.json`
  - `package.json`
  - `index.html`
  - `assets/styles.css`
  - `assets/app.js`
  - `.gitignore`
  - `.nojekyll`

### 阶段 5：GitHub 与 Pages 部署
- **状态：** complete
- 执行的操作：
  - 初始化 git 仓库，设置分支 `main`。
  - 创建初始提交 `ac5cc81`。
  - 使用 `gh repo create iotsec --public --source=. --remote=origin --push` 创建 public 仓库并推送。
  - 通过 GitHub API 启用 Pages；legacy build 失败。
  - 添加 `.github/workflows/pages.yml`，使用 Actions 上传 `_site` artifact 并部署 Pages。
  - 提交 `108d117` 并推送 workflow。
  - 使用 API 将 Pages 切换到 `build_type=workflow`。
  - 验证 Actions run `28114202023` 成功，Pages 状态为 `built`。
- 创建/修改的文件：
  - `.github/workflows/pages.yml`

### 阶段 6：交付验证
- **状态：** complete
- 执行的操作：
  - 验证线上首页 `https://foreverhyx.github.io/iotsec/` 返回 HTTP 200。
  - 使用 agent-browser 验证线上首页、章节目录、总复习笔记加载。
  - 验证线上 PDF 课件、PPTX 课件、`content/notes.json` 均返回 HTTP 200。
  - 使用 agent-browser 验证 Week 1 PDF 课件 iframe 面板和 RFID PPTX 课件面板。
  - 确认 GitHub 仓库为 public，默认分支 `main`。
- 创建/修改的文件：
  - `task_plan.md`
  - `findings.md`
  - `progress.md`

## 测试结果
| 测试 | 输入 | 预期结果 | 实际结果 | 状态 |
|------|------|---------|---------|------|
| git 仓库检查 | `git status --short --branch` | 了解仓库状态 | `fatal: not a git repository` | 已记录 |
| GitHub CLI 登录检查 | `gh auth status` | 确认可推送/创建仓库 | 已登录 `ForeverHYX`，有 `repo` 权限 | 通过 |
| 文档转换工具检查 | `command -v ...` | 了解可用抽取工具 | Python/Node/npm/gh/git 可用，LibreOffice/pandoc/poppler 不可用 | 已记录 |
| Python 包检查 | `importlib.util.find_spec(...)` | 了解可用 Python 解析库 | `PyPDF2` 可用，PPTX 需标准库解析 | 已记录 |
| 抽取脚本单元测试 | `python3 -m unittest tests/test_extract_materials.py -v` | 3 个测试通过 | 3 个测试通过 | 通过 |
| 课件文本抽取 | `python3 tools/extract_materials.py ...` | 生成 11 份抽取 JSON | `Extracted 11 materials to content/extracted` | 通过 |
| 网站数据脚本测试 | `python3 -m unittest tests/test_build_site_data.py -v` | 2 个测试通过 | 2 个测试通过 | 通过 |
| 前端工具测试 | `node --test tests/test_app_utils.mjs` | 2 个测试通过 | 2 个测试通过 | 通过 |
| 完整测试套件 | `npm test` | Python 和 Node 测试全部通过 | 5 个 Python 测试、2 个 Node 测试通过 | 通过 |
| 课件-笔记覆盖检查 | 对比 `content/materials.json` 与 `content/notes.json` | 11 份课件均有笔记 | `missing_notes []` | 通过 |
| 本地页面加载 | `agent-browser open http://localhost:4173/` | 章节列表和笔记显示 | 总复习索引、12 个笔记入口显示 | 通过 |
| 搜索与章节切换 | 搜索 WEP 并打开章节 | 只显示 WEP 条目且笔记更新 | WEP 笔记标题和 10 个小节显示 | 通过 |
| 课件面板 | 点击 WEP 的课件 Tab | 显示课件标题、打开链接、iframe | 显示 PPTX 课件面板；本地 Office viewer 因 localhost 限制报错 | 部分通过 |
| Hash 路由 | 打开 `#lecture-14-nfc-application-security-1` | 显示 NFC 笔记 | NFC 笔记标题和 13 个小节显示 | 通过 |
| GitHub 仓库可见性 | `gh repo view ForeverHYX/iotsec ...` | 仓库为 public | `visibility: PUBLIC`, defaultBranch `main` | 通过 |
| Pages workflow | `gh run view 28114202023 ...` | 部署成功 | `status: completed`, `conclusion: success` | 通过 |
| Pages 状态 | `gh api repos/ForeverHYX/iotsec/pages` | built/workflow/public | `status: built`, `build_type: workflow`, `public: true` | 通过 |
| 线上首页 | `curl -I -L https://foreverhyx.github.io/iotsec/` | HTTP 200 | HTTP/2 200 | 通过 |
| 线上 PDF 课件 | `curl -I -L .../materials/Week%201-2026.pdf` | HTTP 200 | HTTP/2 200, `application/pdf` | 通过 |
| 线上 PPTX 课件 | `curl -I -L .../materials/Lecture%2012...pptx` | HTTP 200 | HTTP/2 200, PPTX content type | 通过 |
| 线上数据清单 | `curl -I -L .../content/notes.json` | HTTP 200 | HTTP/2 200, `application/json` | 通过 |
| 线上页面浏览器检查 | `agent-browser open https://foreverhyx.github.io/iotsec/` | 章节和笔记显示 | 总复习索引、12 个入口显示 | 通过 |

## 错误日志
| 时间戳 | 错误 | 尝试次数 | 解决方案 |
|--------|------|---------|---------|
| 2026-06-24 | 当前目录不是 git 仓库 | 1 | 后续初始化仓库 |
| 2026-06-24 | `gh api ... -f source[branch]=main` 被 zsh glob 拦截 | 1 | 使用引号：`-f 'source[branch]=main'` |
| 2026-06-24 | legacy GitHub Pages build failed | 1 | 添加 GitHub Actions Pages workflow 并切换 `build_type=workflow` |

## 五问重启检查
| 问题 | 答案 |
|------|------|
| 我在哪里？ | 阶段 6：交付验证完成 |
| 我要去哪里？ | 向用户交付仓库地址和 Pages 地址 |
| 目标是什么？ | 让用户能在线阅读当前课件和按章节整理的中文复习笔记 |
| 我学到了什么？ | 见 findings.md |
| 我做了什么？ | 见上方记录 |

---
*每个阶段完成后或遇到错误时更新此文件*

## 会话：2026-06-25

### 阶段 7：补充历年卷回忆题
- **状态：** complete
- **开始时间：** 2026-06-25 Asia/Shanghai
- 执行的操作：
  - 接收用户提供的两份历年卷回忆题。
  - 决定以“回忆版 + 模拟补全”的方式加入网站，避免误称为原卷逐字。
  - 编写 `tests/test_exam_content.py`，先验证历年卷页面和 manifest 缺失时失败。
  - 新增 `notes/past-exams.md`，补全选择/填空题 20 道、简答题池和 2024-2025 大题回忆答案。
  - 更新 `notes/index.md`。
  - 重新生成 `content/notes.json`，当前 13 个笔记入口。
  - 发现搜索只匹配标题/slug/source，无法按 hidden 等正文关键词找到历年卷页；添加正文 `search_text` 索引和前端 `noteMatchesQuery`。
  - 使用 agent-browser 本地验证 `#past-exams` 页面显示、`hidden` 搜索命中历年卷页。
  - 提交 `bf1757d` 并推送，等待 Pages workflow `28116738427` 完成。
  - 验证线上首页、`content/notes.json`、`notes/past-exams.md` 均返回 HTTP 200。
  - 使用 agent-browser 验证线上 `#past-exams` 页面渲染和 `hidden` 正文搜索。
- 创建/修改的文件：
  - `task_plan.md`
  - `findings.md`
  - `progress.md`
  - `notes/past-exams.md`
  - `notes/index.md`
  - `content/notes.json`
  - `tools/build_site_data.py`
  - `assets/app.js`
  - `tests/test_exam_content.py`
  - `tests/test_build_site_data.py`
  - `tests/test_app_utils.mjs`

## 2026-06-25 测试结果
| 测试 | 输入 | 预期结果 | 实际结果 | 状态 |
|------|------|---------|---------|------|
| 历年卷内容测试（红灯） | `python3 -m unittest tests/test_exam_content.py -v` | 缺失页面时失败 | `past-exams` 不在 manifest，文件不存在 | 已验证失败 |
| 历年卷内容测试（绿灯） | 新增页面并生成 manifest 后运行同一测试 | 2 个测试通过 | 2 个测试通过 | 通过 |
| 正文搜索索引测试（红灯） | `python3 -m unittest tests/test_build_site_data.py -v` / `node --test tests/test_app_utils.mjs` | 缺 `search_text`/`noteMatchesQuery` 时失败 | 按预期失败 | 已验证失败 |
| 正文搜索索引测试（绿灯） | 添加 `search_text` 和 `noteMatchesQuery` 后重跑 | 相关测试通过 | Python 3 个、Node 3 个通过 | 通过 |
| 全量测试 | `npm test` | 全部通过 | Python 8 个、Node 3 个通过 | 通过 |
| 本地历年卷页面 | `agent-browser open http://localhost:4173/#past-exams` | 显示历年卷入口与题目标题 | 显示 99 历年卷入口及所有题型标题 | 通过 |
| 本地正文搜索 | 搜索 `hidden` | 命中历年卷页 | 命中“历年卷回忆题与参考答案”和 MAC 章节 | 通过 |
| Pages workflow | `gh run view 28116738427 ...` | 部署成功 | `status: completed`, `conclusion: success` | 通过 |
| 线上历年卷文件 | `curl -L .../notes/past-exams.md` | HTTP 200 | HTTP 200 | 通过 |
| 线上 manifest | 读取 `https://foreverhyx.github.io/iotsec/content/notes.json` | 13 个入口且含 `past-exams` | `count 13`, `['past-exams']` | 通过 |
| 线上历年卷页面 | `agent-browser open https://foreverhyx.github.io/iotsec/?v=bf1757d#past-exams` | 页面渲染历年卷题目 | 显示 99 历年卷入口、20 道小题、简答题池和 2024-2025 大题 | 通过 |
| 线上正文搜索 | 搜索 `hidden` | 命中历年卷页 | 命中历年卷页和 MAC 章节 | 通过 |

### 阶段 8：自测答案与知识讲解优化
- **状态：** complete
- **开始时间：** 2026-06-25 Asia/Shanghai
- 执行的操作：
  - 新增 `tests/test_self_test_answers.py`，验证所有章节末尾“快速自测”都有 `<details class="self-test-answer">` 折叠答案，且题目数与答案数一致。
  - 扩展 `tests/test_app_utils.mjs`，验证 Markdown 渲染器保留受控折叠答案块，并继续渲染块内 Markdown。
  - 先运行新增测试确认红灯：前端 `<details>` 被转义，11 篇章节笔记缺少折叠答案。
  - 修改 `assets/app.js`，只允许 self-test `details`、`summary`、闭合标签通过渲染器。
  - 修改 `assets/styles.css`，为笔记中的折叠答案块增加边框、summary 高亮和正文间距。
  - 为 11 篇章节笔记补充更详细机制讲解，并在“快速自测”末尾加入可折叠参考答案。
  - 运行 `npm run build:data` 重新生成 `content/notes.json`。
  - 提交 `aeb2a1a Add collapsible self-test answers` 并推送到 GitHub。
  - 等待 Pages workflow `28174996973` 成功完成。
  - 验证线上首页、`content/notes.json`、Week 1 笔记和线上 `assets/app.js` 均已更新。
- 创建/修改的文件：
  - `assets/app.js`
  - `assets/styles.css`
  - `notes/*.md`
  - `content/notes.json`
  - `tests/test_app_utils.mjs`
  - `tests/test_self_test_answers.py`
  - `task_plan.md`
  - `findings.md`
  - `progress.md`

## 2026-06-25 阶段 8 测试结果
| 测试 | 输入 | 预期结果 | 实际结果 | 状态 |
|------|------|---------|---------|------|
| 折叠答案渲染测试（红灯） | `node --test tests/test_app_utils.mjs` | 当前渲染器不支持 details 时失败 | `<details>` 被转义，新增测试失败 | 已验证失败 |
| 自测答案内容测试（红灯） | `python3 -m unittest tests/test_self_test_answers.py -v` | 当前章节缺答案时失败 | 11 篇章节笔记均缺 `<details class="self-test-answer">` | 已验证失败 |
| 折叠答案渲染测试（绿灯） | `node --test tests/test_app_utils.mjs` | 4 个 Node 测试通过 | 4 个通过 | 通过 |
| 自测答案内容测试（绿灯） | `python3 -m unittest tests/test_self_test_answers.py -v` | 所有章节题目与答案数一致 | 1 个 Python 测试通过 | 通过 |
| 站点数据重建 | `npm run build:data` | 生成最新 manifest | `Extracted 11 materials`; `Built 13 note records` | 通过 |
| 全量测试 | `npm test` | Python 和 Node 全部通过 | Python 9 个、Node 4 个通过 | 通过 |
| Pages workflow | `gh run view 28174996973 ...` | 部署成功 | `status: completed`, `conclusion: success`, `headSha: aeb2a1a` | 通过 |
| Pages 状态 | `gh api repos/ForeverHYX/iotsec/pages` | built/workflow/public | `status: built`, `build_type: workflow`, `public: true` | 通过 |
| 线上首页 | `curl -L .../?v=aeb2a1a` | HTTP 200 | 200 | 通过 |
| 线上数据清单 | `curl -L .../content/notes.json?v=aeb2a1a` | HTTP 200 且 13 个入口 | 200，13 个入口 | 通过 |
| 线上折叠答案内容 | `curl -L .../notes/week-1-2026.md?v=aeb2a1a` | 包含新增讲解和 `<details>` | 匹配到“安全保证链条”、`<details class="self-test-answer">`、`<summary>参考答案</summary>` | 通过 |

### 阶段 9：历年卷答案折叠
- **状态：** complete
- **开始时间：** 2026-06-25 Asia/Shanghai
- 执行的操作：
  - 用户要求历年卷界面的答案也做成可折叠，不要直接展示。
  - 扩展 `tests/test_exam_content.py`，要求历年卷 30 个题目小节都有 `<details class="self-test-answer">`，并禁止行首直接出现 `参考答案`。
  - 先运行 `python3 -m unittest tests/test_exam_content.py -v` 确认红灯：30 个答案均直接展示。
  - 机械转换 `notes/past-exams.md`，把每个 `参考答案` 到下一个题目标题之间的内容包进折叠块。
  - 运行 `npm run build:data` 重新生成 `content/notes.json`。
  - 提交 `0751c1a Collapse past exam answers` 并推送到 GitHub。
  - 等待 Pages workflow `28175871178` 成功完成。
  - 验证线上历年卷页面：30 个 `<details class="self-test-answer">`，30 个 `<summary>参考答案</summary>`，0 行直出的 `参考答案`。
- 创建/修改的文件：
  - `notes/past-exams.md`
  - `content/notes.json`
  - `tests/test_exam_content.py`
  - `task_plan.md`
  - `findings.md`
  - `progress.md`

## 2026-06-25 阶段 9 测试结果
| 测试 | 输入 | 预期结果 | 实际结果 | 状态 |
|------|------|---------|---------|------|
| 历年卷答案折叠测试（红灯） | `python3 -m unittest tests/test_exam_content.py -v` | 答案直出时失败 | 30 个题目小节缺少 `<details>`，且 30 行 `参考答案` 直出 | 已验证失败 |
| 历年卷答案折叠测试（绿灯） | `python3 -m unittest tests/test_exam_content.py -v` | 3 个测试通过 | 3 个通过 | 通过 |
| 站点数据重建 | `npm run build:data` | 生成最新 manifest | `Extracted 11 materials`; `Built 13 note records` | 通过 |
| 全量测试 | `npm test` | Python 和 Node 全部通过 | Python 10 个、Node 4 个通过 | 通过 |
| Pages workflow | `gh run view 28175871178 ...` | 部署成功 | `status: completed`, `conclusion: success`, `headSha: 0751c1a` | 通过 |
| 线上首页 | `curl -L .../?v=0751c1a#past-exams` | HTTP 200 | 200 | 通过 |
| 线上历年卷折叠答案 | `curl -L .../notes/past-exams.md?v=0751c1a` | 30 个折叠答案且无直出答案 | details 30，summary 30，行首 `参考答案` 0 | 通过 |
| 线上 manifest | `curl -L .../content/notes.json?v=0751c1a` | 13 个入口且含 `past-exams` | 13，`['past-exams']` | 通过 |

### 阶段 10：零基础可读性重写
- **状态：** in_progress
- **开始时间：** 2026-06-25 Asia/Shanghai
- 执行的操作：
  - 用户指出当前知识点更像“给看完的人检查”，要求假设读者零基础，读完复习笔记能理解所有 PPT 涵盖知识点。
  - 启动 3 个 subagent 分别审查基础/无线、Wi-Fi 安全、IoT/RFID/Bluetooth/NFC 组的现有笔记和抽取材料。
  - 检查抽取材料体量：11 份 extracted JSON 从 4009 到 54019 字符不等，现有 11 篇课程笔记约 84 到 149 行，确实偏压缩。
  - 新增 `tests/test_beginner_notes.py`，要求每篇课程笔记包含“零基础导读”“本章知识地图”“初学者常见疑问”，并具备基本解释密度。
  - 将 subagent 识别出的关键缺口加入 `tests/test_beginner_notes.py` 的关键词覆盖测试。
  - 先运行 `python3 -m unittest tests/test_beginner_notes.py -v` 确认红灯：11 篇课程笔记缺少零基础结构，多个 subagent 指定关键词缺失。
  - 为 11 篇课程笔记逐篇新增“零基础导读”“本章知识地图”“初学者常见疑问”，补充关键机制流程和术语首次解释。
  - 运行 `npm run build:data` 重新生成 `content/notes.json`。
  - 运行 `npm test`，当前 Python 13 个测试、Node 4 个测试通过。
  - 启动 3 个 subagent 复审新增内容是否达到零基础可读目标。
  - 根据复审反馈继续补齐缺口：IoT 云/存储模型，RFID reader 架构和物理层研究细节，Bluetooth BLE 攻击工具表，NFC Type 1/2/3/4、手机端威胁、secure execution、票务/门禁/open payment。
  - 修正 SigOver 定量结果写法，明确 `45 vs 21600`、`675 vs 432000` 和 640 倍放大含义。
  - 重新运行 `python3 -m unittest tests/test_beginner_notes.py -v`，确认零基础关键词门槛通过。
  - 重新运行 `npm run build:data` 和 `npm test`，确认 manifest 与完整测试通过。
  - 关闭上一轮旧 subagent 线程，启动 3 个新的只读 subagent 复审当前文件。
  - 新一轮 subagent 复审结果：IoT/RFID/Bluetooth/NFC 组 PASS；Wi-Fi 组发现 WEP fragmentation 64 bytes 表述需修正；基础/蜂窝组发现 SigOver 数字应解释为每 UE 每小时请求率而非设备数量。
  - 修正 WEP fragmentation 为“16 fragments 总共约 64 bytes”，补充 `(8 - 4) * 16 = 64` 推导。
  - 修正 SigOver 数字含义：`45 vs 21600` 为正常 location-update/service requests 与 SigOver 诱导请求率，`675 vs 432000` 为正常 all signaling 与 SigOver 诱导请求率，约 640 倍；同时将 ReVoLTE 89% 表述为目标数据包。
  - 返修后 Wi-Fi 组和基础/蜂窝组均确认 PASS。
- 创建/修改的文件：
  - `task_plan.md`
  - `progress.md`
  - `tests/test_beginner_notes.py`
  - `notes/*.md`
  - `content/notes.json`

## 2026-06-25 阶段 10 测试结果
| 测试 | 输入 | 预期结果 | 实际结果 | 状态 |
|------|------|---------|---------|------|
| 零基础结构测试（红灯） | `python3 -m unittest tests/test_beginner_notes.py -v` | 当前笔记缺结构时失败 | 11 篇课程笔记缺“零基础导读/知识地图/常见疑问”，关键词缺失 | 已验证失败 |
| 零基础结构测试（绿灯） | `python3 -m unittest tests/test_beginner_notes.py -v` | 3 个测试通过 | 3 个通过 | 通过 |
| 站点数据重建 | `npm run build:data` | 生成最新 manifest | `Extracted 11 materials`; `Built 13 note records` | 通过 |
| 全量测试 | `npm test` | Python 和 Node 全部通过 | Python 13 个、Node 4 个通过 | 通过 |
| 零基础返修测试 | `python3 -m unittest tests/test_beginner_notes.py -v` | 新增关键词均覆盖 | 3 个测试通过 | 通过 |
| 返修后站点数据重建 | `npm run build:data` | 生成最新 manifest | `Extracted 11 materials`; `Built 13 note records` | 通过 |
| 返修后全量测试 | `npm test` | Python 和 Node 全部通过 | Python 13 个、Node 4 个通过 | 通过 |
| subagent 复审 | 3 个只读复审任务 | 无 must-fix | IoT 组 PASS；Wi-Fi/基础组返修后 PASS | 通过 |
| Pages workflow | `gh run watch 28180254014 --repo ForeverHYX/iotsec --exit-status` | 部署成功 | `deploy in 2m12s`, `conclusion: success`, `headSha: 7f88972` | 通过 |
| 线上首页 | `curl -I -L https://foreverhyx.github.io/iotsec/?v=7f88972...#past-exams` | HTTP 200 | HTTP/2 200 | 通过 |
| 线上笔记原文 | 读取 `notes/part2.md`、`notes/wired-equivalent-privacy-wep.md`、`notes/lecture-14-nfc-application-security-1.md` | 包含返修与新增内容 | 三个文件均匹配关键术语 | 通过 |
| 线上 manifest 索引 | 读取 `content/notes.json?v=7f88972...` | 13 个入口且索引含新增关键词 | 13 个入口；part2、WEP、NFC、Week7 关键词命中 | 通过 |

### 阶段 11：PPT 全覆盖、公式术语与历年题强化
- **状态：** in_progress
- **开始时间：** 2026-06-26 Asia/Shanghai
- 执行的操作：
  - 用户指出上一轮仍有大量 PPT 知识点、公式、英文单词和缩写被省略；举例说明第二节无线基础无法回答 slow fading 的历年选择题。
  - 本阶段目标调整为：每章必须能支撑零基础读者理解 PPT 的术语、公式、机制，并能练习历年卷风格题；答案继续折叠。
  - 新增 `tests/test_stage11_full_coverage.py`，要求 11 篇课程笔记都有“公式与术语速查”“历年卷风格练习”，且新增练习答案用 `<details class="self-test-answer">` 折叠。
  - 按 subagent 初审缺口和用户示例，为 11 篇课程笔记补充 PPT 术语、英文缩写、公式、协议步骤、攻击原理和历年卷风格练习。
  - 重点补齐：slow fading/Shadowing Effect、Doppler/multipath、Channel Interleave、hidden terminal 图示/RTS-CTS、Signal Overshadowing/Capture Effect、WEP/WPA/WPA2 细节、IoT contradictions/security architecture、RFID/Bluetooth/NFC 术语和公式。
  - 运行 `python3 -m unittest tests/test_stage11_full_coverage.py -v`，2 个测试通过。
  - 运行 `npm run build:data`，重新生成 `content/extracted` 和 `content/notes.json`。
  - 首次运行 `npm test` 失败：`tests/test_self_test_answers.py` 仍假设“快速自测”是文件最后一节，新增 Stage 11 后续章节中的编号列表被误算进自测答案数。
  - 修正 `tests/test_self_test_answers.py`，让它只检查“快速自测”到下一个二级标题之间的内容。
  - 重新运行 `npm test`，Python 15 个测试和 Node 4 个测试通过。
  - 启动 3 个只读 subagent 复审基础/无线、MAC/蜂窝/Wi-Fi、IoT/RFID/Bluetooth/NFC 三组内容覆盖。
  - 根据 subagent 复审继续补齐：第二周无线基础的 CSMA/CA、RTS/CTS、near-far effect 和 hidden terminal 练习；MAC 暴露终端 RTS/CTS 规则；ReVoLTE `3/15` 与 `12/15` Bearer ID 结果；WEP weak IV 完整模式；WPA TKIP 序列机制与暴力破解时间；IoT security demands/architecture 细项；RFID reader 功能、HB 参数、二进制树复杂度公式；Bluetooth 技术参数和 Blue snarfing；NFC FWT、EMV relay、open payment 和 Google Wallet PIN 细节。
  - 扩展 `tests/test_stage11_full_coverage.py`，把 subagent 复审给出的 must-fix 精确术语和公式纳入自动覆盖测试。
  - 重新运行 `python3 -m unittest tests/test_stage11_full_coverage.py -v`，2 个测试通过。
  - 重新运行 `npm run build:data` 和 `npm test`，Python 15 个测试和 Node 4 个测试通过。
  - 3 个 subagent 返修复审均 PASS；最后 RFID 防冲突复杂度公式单点复核也 PASS。
- 创建/修改的文件：
  - `task_plan.md`
  - `progress.md`
  - `findings.md`
  - `tests/test_stage11_full_coverage.py`
  - `tests/test_self_test_answers.py`
  - `notes/*.md`
  - `content/notes.json`

## 2026-06-26 阶段 11 测试结果
| 测试 | 输入 | 预期结果 | 实际结果 | 状态 |
|------|------|---------|---------|------|
| Stage 11 专项覆盖测试 | `python3 -m unittest tests/test_stage11_full_coverage.py -v` | 11 篇课程笔记有术语/公式/历年题结构，关键术语精确命中 | 2 个测试通过 | 通过 |
| 站点数据重建 | `npm run build:data` | 生成最新 manifest | `Extracted 11 materials`; `Built 13 note records` | 通过 |
| 完整测试首轮 | `npm test` | 全部通过 | 自测答案计数测试 11 个子项失败，原因是测试跨越到后续 Stage 11 章节 | 已记录并修复 |
| 完整测试返修后 | `npm test` | Python 和 Node 全部通过 | Python 15 个、Node 4 个通过 | 通过 |
| Stage 11 返修覆盖测试 | `python3 -m unittest tests/test_stage11_full_coverage.py -v` | subagent must-fix 项全部命中 | 2 个测试通过 | 通过 |
| 返修后站点数据重建 | `npm run build:data` | 生成最新 manifest | `Extracted 11 materials`; `Built 13 note records` | 通过 |
| 返修后完整测试 | `npm test` | Python 和 Node 全部通过 | Python 15 个、Node 4 个通过 | 通过 |
| subagent 返修复审 | 3 个只读复审任务 | 无 remaining MUST-FIX | 基础/无线 PASS；MAC/蜂窝/Wi-Fi PASS；IoT/RFID/Bluetooth/NFC PASS | 通过 |
