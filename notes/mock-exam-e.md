---
title: "模拟卷 E：按题目清单定制"
source: "generated from user topic list"
order: 104
---

# 模拟卷 E：按题目清单定制

## 0. 使用说明

本卷按你给出的题目清单生成：选择题 20 题，每题 3 分；大题 4 题，每题 10 分。题目覆盖 QAM、扩频、Fast Fading、Channel interleaving、SigOver Attack、WEP/WPA/WPA2、IoT Security、RFID、Bluetooth 和智能家居摄像头场景。

## 一、选择题（20 题，每题 3 分）

### 选择题 1

题干：QAM（Quadrature Amplitude Modulation）主要是在调制载波的哪些属性？

选项：

- A. 幅度和相位
- B. 只调频率
- C. 只调天线方向
- D. 只调加密密钥长度

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：QAM 是正交幅度调制，用 I/Q 两路同时承载信息，本质上同时改变载波的幅度和相位。考试看到 QAM，不要答成只调频率。

</details>

### 选择题 2

题干：扩频（Spread Spectrum）的好处最准确的是哪一项？

选项：

- A. 把信号扩展到更宽频带，提高抗窄带干扰和抗频率选择性衰落能力
- B. 让 WEP 自动升级为 WPA2
- C. 取消所有功率控制需求
- D. 让 RFID tag 不需要 reader 供能

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：扩频可把干扰影响分散，提升抗干扰、抗多径/频率选择性衰落能力，也可支持码分多址等设计。但它不等于加密，也不代表不需要功率控制。

</details>

### 选择题 3

题干：Fast Fading 通常与下列哪项关系最密切？

选项：

- A. 多径传播和移动导致的信号快速起伏
- B. WEP 的 CRC-32 线性
- C. RFID tag 的 kill command
- D. WPA2 的 PMK 派生

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Fast Fading 是小尺度、快速变化的衰落，常由 multipath propagation、Doppler effect 和相位叠加变化造成。Slow fading 更常由 shadowing effect 等大尺度遮挡造成。

</details>

### 选择题 4

题干：Channel interleaving 的主要作用是什么？

选项：

- A. 将连续突发错误打散，便于纠错码修复
- B. 直接完成用户认证
- C. 替代所有加密算法
- D. 固定 BLE 地址方便连接

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：无线衰落常造成 burst error。交织把连续比特分散到不同时间或位置，使纠错码看到更随机的错误分布。

</details>

### 选择题 5

题干：SigOver Attack 相比普通干扰攻击的优势更接近哪一项？

选项：

- A. 利用 capture effect/overshadowing，让接收端解出攻击者构造的同步或控制信号
- B. 不需要任何发射设备
- C. 可以直接破解所有 LTE 密钥
- D. 只能在有线以太网中发生

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：SigOver Attack 的优势不是“纯噪声阻塞”，而是用更强、更同步的恶意信号 overshadow 合法信号，使接收端把攻击者信号当成有效信号处理，隐蔽性和定向性强于简单 jamming。

</details>

### 选择题 6

题干：Wireless 更容易受攻击的原因不包括哪项？

选项：

- A. 无线信号广播传播，范围内攻击者容易监听
- B. 攻击者可伪造、注入或重放无线帧
- C. Jamming 可直接破坏可用性
- D. 无线天然具有物理线缆隔离，外人完全收不到信号

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：无线比有线更难保护，正是因为没有线缆边界：监听、注入、重放、rogue AP、deauth、jamming 都更容易发生。

</details>

### 选择题 7

题干：WEP IV 多少位？

选项：

- A. 24 bit
- B. 48 bit
- C. 96 bit
- D. 128 bit

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WEP 使用 24-bit IV，明文发送且空间太小，容易重复，从而造成 RC4 keystream reuse。

</details>

### 选择题 8

题干：WEP 使用哪种 Cipher 生成密钥流？

选项：

- A. RC4
- B. AES-CCMP
- C. RSA
- D. ECDSA

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WEP 使用 RC4 stream cipher，seed 为 `IV || shared key`。同一 IV 和 key 会生成同一 keystream。

</details>

### 选择题 9

题干：谁使用了 CCMP 作为核心数据保护机制？

选项：

- A. WPA2
- B. WEP
- C. RFID Pure ALOHA
- D. Bluetooth piconet

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WPA2 使用 AES-CCMP。CCMP 中 AES-CTR 负责机密性，CBC-MAC 负责完整性，PN/nonce 防重放和密钥流重用。

</details>

### 选择题 10

题干：WPA/TKIP 的 integrity 主要如何保证？

选项：

- A. 使用 Michael MIC，并结合 TKIP 序列/计数器做重放防护
- B. 只使用无密钥 CRC-32
- C. 使用 RFID 的 kill tag
- D. 使用 NFC 的 FWT

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WPA/TKIP 用 Michael MIC 补强完整性，并用 TKIP sequence counter/TSC 防重放。它比 WEP 的 CRC-32 更强，但仍是过渡方案。

</details>

### 选择题 11

题干：下列哪项不是 Main Security Objectives（CIA）之一？

选项：

- A. Confidentiality
- B. Integrity
- C. Availability
- D. Authentication

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：CIA 三元组是 Confidentiality、Integrity、Availability。Authentication 很重要，但它不是 CIA 三元组中的一项。

</details>

### 选择题 12

题干：按当前公开标准/认证口径，最新一代 WiFi 标准通常指哪一个？

选项：

- A. Wi-Fi 7 / IEEE 802.11be
- B. Wi-Fi 4 / IEEE 802.11n
- C. WEP
- D. Bluetooth 5

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：按当前课程和公开认证口径答 Wi-Fi 7 / IEEE 802.11be。802.11bn/Wi-Fi 8 是后续演进方向，不作为本题答案。

</details>

### 选择题 13

题干：WiFi 在 IoT 四层模型中通常属于哪一层？

选项：

- A. Network Structure / 网络传输层
- B. Sensing and Recognition / 感知识别层
- C. Application only / 只属于应用层
- D. Data privacy policy / 只属于隐私政策

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WiFi 是 IoT 中常用的网络接入和传输技术，通常归入 network structure / 网络层。RFID、传感器、摄像头更接近感知识别层。

</details>

### 选择题 14

题干：下列哪项最符合 IoT Main Characteristic？

选项：

- A. 物理对象、感知设备、网络连接、管理服务和应用闭环结合
- B. 只是一台离线电脑
- C. 只是一种 WiFi 加密算法
- D. 只是一种 RFID 防冲突公式

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：IoT 的核心是把物理世界对象、sensing/recognition、网络连接、云/边缘管理服务和应用决策连接成 cyber-physical system。

</details>

### 选择题 15

题干：IoT communication security 主要关注什么？

选项：

- A. 传输中的加密、认证、完整性、抗重放、密钥管理和抗 DoS
- B. 只关注标签外壳颜色
- C. 只关注显示器亮度
- D. 只关注纸质说明书

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：communication security 是 IoT Security Demands 中的传输安全需求，不只是一种算法，而是跨链路、协议、密钥和可用性的一组要求。

</details>

### 选择题 16

题干：下列哪项属于 Bluetooth security threats？

选项：

- A. Sniffing、replay、downgrade、Blue snarfing、未授权服务访问
- B. WEP IV 重用 only
- C. RFID ALOHA starvation only
- D. Shannon capacity only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Bluetooth/BLE 威胁包括监听、重放、降级、弱 PIN、未授权 GATT/服务访问、Blue snarfing、tracking 等。

</details>

### 选择题 17

题干：Bluetooth piconet 里 master 主要负责什么？

选项：

- A. 提供 clock 和 hopping sequence，让 slave 同步到同一 piconet
- B. 计算 WEP 的 CRC-32
- C. 发送 NFC APDU
- D. 执行 RFID kill tag

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Classic Bluetooth piconet 中一个 master 管理多个 slave，slave 同步到 master clock 和跳频序列。

</details>

### 选择题 18

题干：如何解决 RFID 的隐私问题，下列哪组最完整？

选项：

- A. Kill tag、renaming、访问控制、距离限制、屏蔽、轻量级认证、后台校验
- B. 永久公开固定 ID
- C. 禁止所有 reader 供能
- D. 只把标签刷成不同颜色

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：RFID 隐私保护常见方案包括 kill、重命名、访问控制、距离策略、屏蔽、轻量认证和后台校验。不同方案有功能、成本和可用性取舍。

</details>

### 选择题 19

题干：RFID Components 通常包括哪些？

选项：

- A. Tag、Reader、Antenna、中间件/后台系统
- B. PMK、PTK、GTK、KCK
- C. PCD、PICC、APDU、FWT only
- D. Master、slave、piconet、scatternet only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：RFID 系统通常由 tag、reader、antenna 和后台应用/中间件组成。无源 tag 还依赖 reader 电磁场供能和 backscatter。

</details>

### 选择题 20

题干：下列哪项最可能导致用户隐私泄露？

选项：

- A. BLE 广播中长期稳定的地址、设备名、服务 UUID 和 manufacturer data
- B. 使用强随机 PSK
- C. 对固件更新做签名校验
- D. 最小化 IoT 数据采集

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：稳定广播标识和 payload 可被扫描者用来 tracking/profiling，推断用户设备、位置、作息和行为模式。

</details>

## 二、大题（4 题，每题 10 分）

### 大题 1

题干：比较 CSMA/CD 和 CSMA/CA 的异同。

<details class="self-test-answer">
<summary>参考答案</summary>

参考要点：

- 相同点：
  - 都属于共享介质访问控制思想，都先感知信道再决定是否发送。
  - 都希望减少多个节点同时发送造成的冲突。
  - 都使用退避思想处理竞争。
- 不同点：
  - CSMA/CD 是 Collision Detection，典型用于早期共享有线以太网。发送时可以边发边检测碰撞，检测到碰撞后停止发送并退避重传。
  - CSMA/CA 是 Collision Avoidance，典型用于 802.11 WiFi。无线中发送端很难边发边可靠检测碰撞，所以通过 DIFS/SIFS、随机退避、ACK、RTS/CTS、NAV 等机制尽量避免碰撞。
  - CSMA/CD 假设有线信号传播和碰撞检测更可控；CSMA/CA 必须处理 hidden terminal、exposed terminal、无线衰落和接收端碰撞。
- 可补充：
  - Hidden Terminal 中，A/C 互相听不到但都能干扰 B，普通 carrier sensing 不够。
  - RTS/CTS 可让接收端 B 发 CTS，隐藏节点听到后设置 NAV 退避。

</details>

### 大题 2

题干：比较 WPA Pre-Shared Key Mode 和 Enterprise Mode 的区别。

<details class="self-test-answer">
<summary>参考答案</summary>

参考要点：

- WPA Pre-Shared Key Mode：
  - 所有合法用户共享一个 passphrase/PSK，适合家庭或小型网络。
  - PMK 通常由 passphrase 和 SSID 通过 PBKDF2 派生。
  - 部署简单，不需要认证服务器。
  - 风险是口令弱时可被离线字典攻击；多人共享同一口令，离职或泄露后难以按用户撤销。
- WPA Enterprise Mode：
  - 使用 802.1X、EAP 和 RADIUS/Authentication Server。
  - 支持按用户或设备认证，便于账号管理、审计和撤销权限。
  - 安全性和可管理性更好，适合企业/校园。
  - 部署复杂，需要认证服务器、证书或 EAP 配置。
- 共同点：
  - 后续都可进入 4-way handshake，基于 PMK、ANonce、SNonce、AP MAC、STA MAC 派生 PTK。
  - PTK 可拆为 KCK、KEK、TK，分别用于 MIC、加密 key data 和单播数据保护。

</details>

### 大题 3

题干：你在自己家安装一个通过 WiFi 联网的监控摄像头。攻击者可以采取什么措施？可以获取什么隐私？如何防御？

<details class="self-test-answer">
<summary>参考答案</summary>

攻击措施：

- WiFi 侧：
  - 嗅探无线流量，抓取 WPA/WPA2 4-way handshake，对弱 PSK 做离线字典攻击。
  - 设置 rogue AP / evil twin，诱导手机或摄像头连接。
  - 发送 deauthentication/disassociation 管理帧，让设备断线或诱导重连。
  - Jamming 或流量洪泛导致摄像头不可用。
- 设备侧：
  - 利用默认口令、弱口令、开放端口、旧固件漏洞。
  - 固件逆向、未签名 OTA、后门账号。
- 云/App 侧：
  - 账号弱密码、token 泄露、云 API 越权、App 日志泄露。

可获取隐私：

- 家中视频和音频。
- 是否在家、作息规律、孩子/老人活动、访客时间。
- 室内布局、财物情况、设备清单。
- WiFi SSID、摄像头型号、手机标识、云账号 token。

防御：

- 使用强 WPA2/WPA3 口令，禁用 WEP/WPA/TKIP。
- 修改默认账号密码，启用 MFA。
- 摄像头和主设备网络隔离，关闭不必要端口。
- 固件签名更新，及时补丁。
- 云端最小权限、端到端加密、日志审计和异常登录提醒。
- 隐私设计：最小采集、本地存储/处理优先、按需开启摄像头和麦克风。

</details>

### 大题 4

题干：详细阐述 Security Demands、Security Architecture，并说明 Bluetooth Security Modes。

<details class="self-test-answer">
<summary>参考答案</summary>

Security Demands：

- Access security：
  - 保护用户、设备和节点接入过程。
  - 重点是身份认证、授权、访问控制、非法节点接入防护。
- Communication security：
  - 保护 IoT 网络传输。
  - 重点是加密、完整性、认证、抗重放、密钥管理、拥塞和 DoS 防护。
- Data privacy security：
  - 保护位置、健康、家庭行为、视频音频、工业状态等敏感数据。
  - 技术包括数据最小化、加密存储、脱敏、访问控制、审计和生命周期管理。
- Computing system security：
  - 保护 IoT 应用、云/边缘平台、固件、服务质量和可信更新。
  - 重点是应用权限、固件签名、隔离、审计、故障恢复。

Security Architecture：

- Sensing security：
  - 感知层设备，如 RFID、摄像头、传感器、麦克风。
  - 防伪造节点、物理篡改、假数据注入和非法读取。
- Transmission security：
  - 网络传输层，如 WiFi、Bluetooth、蜂窝、LPWAN。
  - 做链路或端到端加密、认证、完整性、抗重放和抗 DoS。
- Data security：
  - 数据存储、处理、共享和备份。
  - 做加密、访问控制、脱敏、备份、审计。
- Application security：
  - 智能家居、医疗、交通、工业等业务逻辑。
  - 做权限校验、输入验证、业务逻辑保护、日志和异常检测。

Bluetooth Security Modes：

- Mode 1：
  - No security，不做认证和加密，风险最高。
- Mode 2：
  - Service level security，连接建立后在服务层做认证、授权或加密。
  - 不同服务可有不同访问控制。
- Mode 3：
  - Link level security，连接建立前先做认证和加密。
  - 安全控制更早介入。
- Mode 4：
  - SSP / Secure Simple Pairing 相关，强调更强配对、链路密钥和服务安全级别。

总结：Security Demands 回答“需要保护什么”，Security Architecture 回答“在哪些层部署保护”，Bluetooth Security Modes 则是 Bluetooth 协议内部对安全控制位置和强度的划分。

</details>
