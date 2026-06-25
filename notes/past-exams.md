---
title: "历年卷回忆题与参考答案"
source: "student recollection"
order: 99
---

# 历年卷回忆题与参考答案

## 0. 使用说明

这页是根据考后回忆整理的复习版，不是原卷逐字复刻。题干和选项中缺失的部分按课件内容做了模拟补全，适合考前背诵和查漏补缺。若题目只要求单选，优先按“最贴近课件表述”的答案作答；若老师按简答给分，把后面的关键词写全更稳。

## 1. 回忆卷 A：选择/填空题

### 1. WiFi 标准频段

题干：IEEE 802.11 无线局域网常用的公共频段包括哪些？

选项：

- A. 900 MHz 和 1.8 GHz
- B. 2.4 GHz 和 5 GHz
- C. 13.56 MHz 和 125 kHz
- D. 60 GHz 和 77 GHz

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：课件中 802.11 WLAN 工作在 2.4 GHz 和 5 GHz 公共频段。802.11b/g 常见于 2.4 GHz，802.11a/ac 常见于 5 GHz，802.11n/ax 可覆盖 2.4/5 GHz；WiFi 7 还可涉及 6 GHz，但本题按课件回忆选 2.4/5 GHz。

</details>

### 2. DSSS 的优点

题干：关于直接序列扩频 DSSS，下列哪项是其优点？

选项：

- A. 完全不需要功率控制
- B. 减少频率选择性衰落，并支持软切换
- C. 只能用于有线以太网
- D. 比 FHSS 更容易避开任意窄带干扰

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：DSSS 使用扩展码把信号扩展到更宽频带，可减少频率选择性衰落；在蜂窝场景中多个基站可使用相同频率范围，支持软切换。缺点是需要较精确的功率控制。

</details>

### 3. 单工、半双工、全双工

题干：将下列系统与通信方式匹配。

选项：

- A. 广播
- B. 蓝牙
- C. 移动手机通话
- D. 现代交换式以太网

<details class="self-test-answer">
<summary>参考答案</summary>


- 广播：单工 Simplex，只从广播站到接收者。
- 蓝牙：半双工 Half-duplex，典型物理信道使用 TDMA-TDD，master/slave 交替发送。
- 移动手机通话：全双工 Full-duplex，用户体验上可同时说和听；底层可用 FDD 或 TDD 实现。
- 现代交换式以太网：全双工 Full-duplex。若题目特指早期共享介质/Hub Ethernet 或 CSMA/CD 以太网，则是半双工。

</details>

### 4. Channel Interleave 的作用

题干：信道交织 Channel Interleaving 的主要作用是什么？

选项：

- A. 让相邻比特在传输中分散到不同时间/位置，减轻突发错误对同一码字的集中破坏
- B. 直接完成用户身份认证
- C. 把 2.4 GHz 信号转换成 5 GHz 信号
- D. 替代所有加密算法

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：无线衰落常造成 burst error。交织把连续错误打散，使纠错码看到更随机的错误，提高信道编码纠错效果。

</details>

### 5. IoT 面临的 Contradictions

题干：下列哪组矛盾最符合 IoT 系统设计中的典型 contradictions？

选项：

- A. High performance vs. Low energy
- B. Strong security/privacy vs. Limited computation/storage
- C. Massive connectivity/heterogeneity vs. Manageability
- D. 以上都是

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

可背答案：IoT 常见矛盾包括高性能与低能耗、强安全与资源受限、大规模异构连接与可管理性、开放互联与隔离控制、数据共享/智能化与隐私保护、实时可用性与网络拥塞/低带宽。

</details>

### 6. 现有 WiFi 标准缺少什么

题干：现有 WiFi 标准在密集 AP 部署中主要缺少什么？

选项：

- A. 良好的机制来减轻干扰
- B. 任何物理层调制方式
- C. 任何 MAC 层协议
- D. 对 2.4 GHz 频段的支持

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：课件原意是 WiFi 标准缺少良好的机制来缓解干扰，尤其是密集 AP 部署中；静态信道、功率、载波侦听阈值等会造成低频谱复用和严重竞争。

</details>

### 7. WEP 保持数据完整性的算法

题干：WEP 中用于数据完整性检查的算法是什么？

选项：

- A. HMAC-SHA256
- B. CRC-32
- C. CBC-MAC
- D. RSA

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：WEP 的 ICV 来自 CRC-32。CRC-32 只能检测随机错误，不是密码学 MAC，攻击者可以修改密文并同步修正 CRC。

</details>

### 8. WEP 使用的加密算法

题干：WEP 使用哪种加密算法生成密钥流？

选项：

- A. AES
- B. RC4
- C. DES
- D. RSA

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：WEP 使用 RC4 流密码，seed 为 `IV || shared key`。IV 太短且可重用是 WEP 的核心漏洞之一。

</details>

### 9. WPA2 所用 IV/PN 长度

题干：WPA2/CCMP 用于防重放并构造 fresh nonce 的 Packet Number/IV 长度是多少？

选项：

- A. 16 bit
- B. 24 bit
- C. 32 bit
- D. 48 bit

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：课件对比表中 WPA2 key life/IV 为 48 bit；CCMP 使用 48-bit Packet Number (PN) 防重放并构造新鲜 nonce。

</details>

### 10. 三个基本 Security Objectives

题干：NIST/课程中最基本的三个安全目标是什么？

选项：

- A. Confidentiality, Integrity, Availability
- B. Authentication, Authorization, Accounting
- C. Encryption, Hashing, Signing
- D. Routing, Forwarding, Switching

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：CIA 三元组：机密性、完整性、可用性。

</details>

### 11. Wireless LAN/WiFi 标准

题干：Wireless LAN，也就是 WiFi，主要对应哪个 IEEE 标准族？

选项：

- A. IEEE 802.3
- B. IEEE 802.11
- C. IEEE 802.15.4
- D. IEEE 802.16

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：WiFi 指使用 IEEE 802.11 标准的无线局域网。802.3 是以太网，802.15 相关 Bluetooth/ZigBee，802.16 是 WiMAX。

</details>

### 12. WSN 的特点

题干：以下哪项属于 Wireless Sensor Network (WSN) 的特点？

选项：

- A. 能量是核心约束，节点速率低但数量可从几十到上千
- B. 每个节点都具有强大的服务器级计算能力
- C. 网络智能只在单个终端设备中
- D. 只用于有线骨干网

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

可背答案：WSN 节点多、低功耗、低速率、能量受限；数据通常流向中心汇聚节点；多跳、自组织、部署在物理环境中；网络智能往往在整体网络而不是单个设备中体现。

</details>

### 13. IoT computing system security

题干：IoT computing system security 主要关注什么？

选项：

- A. IoT 应用和计算系统中的认证、授权、审计、隐私、服务质量和应用安全
- B. 只关注 WiFi 的 2.4 GHz 频段
- C. 只关注 WEP 的 CRC-32
- D. 只关注 RFID 标签外观

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：课件把 IoT computing system security 作为 Security Demands 之一，强调 IoT 应用已渗透现实场景，除传统网络认证、授权、审计外，还包含 IoT 特有隐私、安全和服务质量要求。

</details>

### 14. RFID 适合的通信保护思路

题干：在“RFID tag 和 reader 通信被窃听”的课件场景中，哪种保护思路最贴近 RF-Cloak？

选项：

- A. 使用 reader 随机化信号，使随机波形在空中起到类似 one-time pad 的作用
- B. 公开固定标签 ID
- C. 永远不改变 reader 信号
- D. 只依赖标签外壳颜色

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：课件 RF-Cloak 中 “Random waveform acts like a one-time pad on the air”。注意这不是说所有廉价 RFID tag 都能直接运行传统 one-time pad，而是 reader 端随机化调制/信道来保护空中通信。

</details>

### 15. RFID 在 IoT 哪一层

题干：RFID 在 IoT 架构中通常属于哪一层？

选项：

- A. Sensing Layer
- B. Transport Layer
- C. Management Layer
- D. Application Layer only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：RFID 是自动信息生成/对象识别技术，是感知层设备之一。

</details>

### 16. RFID 系统功能

题干：RFID 系统的基本功能不包括哪项？

选项：

- A. 识别真实物体并读取其 ID
- B. 通过 reader 为无源 tag 供能
- C. reader/tag/antenna 间进行无线通信
- D. 保证所有标签天然不可克隆且不可跟踪

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：RFID 的功能是对象识别、读取/写入标签、供能、通信、连接后台应用。不可克隆、不可跟踪是安全目标，不是天然功能。

</details>

### 17. RFID 隐私保护方法

题干：下列哪项是课件提到的 RFID 隐私保护方法？

选项：

- A. Kill tag
- B. Re-naming tags
- C. Distance measurement / policy and legislation
- D. 以上都是

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：Kill 保护售后隐私但牺牲后续功能；renaming 防长期跟踪；距离测量按距离释放不同信息；政策/法律可规范部署但不能单独阻止非法读取。

</details>

### 18. Bluetooth 系统功能/安全目标

题干：Bluetooth security 中提到的三个核心安全目标是什么？

选项：

- A. Authentication, Confidentiality, Authorization
- B. CRC, RC4, IV
- C. Routing, Switching, Forwarding
- D. Sensing, Storage, Printing

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Bluetooth 课件明确列出 Authentication、Confidentiality、Authorization。

</details>

### 19. Bluetooth 使用的关键技术

题干：Bluetooth Classic 物理层/拓扑的关键技术特征是什么？

选项：

- A. TDMA-TDD Slow Frequency Hopping，piconet 中 master 设置时钟和跳频序列
- B. 只使用有线 CSMA/CD
- C. 只使用 13.56 MHz NFC
- D. 只使用 WEP 的 RC4

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Bluetooth 工作在 2.4 GHz ISM，使用 TDMA-TDD slow frequency hopping；piconet 中一个 master、多个 slave，同步到共同 clock 和 hopping sequence。

</details>

### 20. Bluetooth 保护方法

题干：下列哪项属于 Bluetooth/BLE 的安全或隐私保护方法？

选项：

- A. 配对与 bonding、链路加密、访问授权
- B. 地址随机化、直接广播
- C. BLE-Guardian 通过隐藏广告和授权连接保护 BLE 设备
- D. 以上都是

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：Bluetooth 保护包括认证、授权、加密、强 PIN/随机数、最小密钥长度、地址随机化、BLE-Guardian 等。

</details>

## 2. 回忆卷 A：简答题池

### 1. 画图解释 Hidden Terminal 问题和解决方法

题干：如下拓扑中，A 和 C 都能与 B 通信，但 A 与 C 彼此听不到。请画图解释 Hidden Terminal 问题，并说明 802.11 中的解决方法。

<details class="self-test-answer">
<summary>参考答案</summary>


```text
A  --->  B  <---  C
A 听不到 C，C 听不到 A，但二者都能到达 B。
```

要点：

- 隐藏终端问题是发送端听不到另一个发送端，于是二者都认为信道空闲。
- A 和 C 同时向 B 发送时，B 处发生碰撞。
- 根因：无线中的 carrier sensing 发生在发送端，但碰撞影响接收端；“我听不到别人”不代表接收端不会被干扰。
- 解决方法：RTS/CTS。
- A 先给 B 发 RTS，说明要占用介质多长时间；B 回复 CTS。
- C 即使听不到 A，也能听到 B 的 CTS，于是设置 NAV 并退避，从而避免在 B 处碰撞。
- RTS/CTS 适合较大数据帧，小包使用会增加控制开销。

</details>

### 2. 阐述 WPA2 四次握手

题干：请说明 WPA2 4-way handshake 的输入、四个消息的作用，以及握手后生成/安装哪些密钥。

<details class="self-test-answer">
<summary>参考答案</summary>


- 目的：双方证明都持有 PMK，并协商新鲜的 PTK。
- 输入：PMK、AP 生成的 ANonce、STA 生成的 SNonce、AP MAC、STA MAC。
- Msg1：AP -> STA，发送 ANonce。
- STA 收到 ANonce 后生成 SNonce，并由 PMK、ANonce、SNonce、双方 MAC 派生 PTK。
- Msg2：STA -> AP，发送 SNonce 和 MIC，证明 STA 持有 PMK/已派生 PTK。
- AP 用同样输入派生 PTK，并验证 MIC。
- Msg3：AP -> STA，发送 GTK/RSN 信息等 key data，并带 MIC；通知 STA 安装密钥。
- Msg4：STA -> AP，确认密钥安装完成。
- PTK 通常拆为 KCK、KEK、TK：KCK 算 EAPOL-Key MIC，KEK 加密 key data，TK 加密单播数据。
- WPA2/CCMP 用 AES-CCMP，PN/IV 为 48 bit，用于防重放和构造 nonce。

</details>

### 3. 智能门锁/智能家居监控系统：攻击与隐私

题干：一个智能门锁产品使用屋内 WiFi 和蓝牙。另一个版本把场景换成智能家居监控系统。攻击者可采取什么措施攻击？可以获得什么隐私？

<details class="self-test-answer">
<summary>参考答案</summary>


- WiFi 侧攻击：
  - 嗅探无线流量，抓取握手，若使用弱 WPA/WPA2-PSK，可离线字典攻击。
  - 建立 rogue AP/evil twin，诱导设备或手机连接。
  - 发送 deauthentication/disassociation 管理帧造成断连或诱导重连。
  - 对弱配置、默认口令、未更新固件、开放端口进行入侵。
  - RF jamming 或流量洪泛造成不可用。
- Bluetooth/BLE 侧攻击：
  - 被动扫描 BLE advertising，追踪设备地址、RSSI、设备名、服务 UUID。
  - 利用固定 BD_ADDR 或随机化不足进行长期跟踪。
  - 弱 PIN/配对降级/MITM，重放或未授权连接。
  - 对 BLE GATT 服务做未授权读写或 fuzzing。
- 设备/云/应用侧攻击：
  - 默认账号、弱密码、token 泄露、云 API 越权。
  - App 权限过大、日志泄露、固件逆向、OTA 更新未签名。
  - 摄像头/门锁被加入 botnet 或被远程控制。
- 可获取隐私：
  - 居住规律、开关门时间、是否在家。
  - 家庭成员数量、访客记录、位置/活动轨迹。
  - 摄像头视频、音频、屏幕/报警记录。
  - WiFi SSID、设备指纹、手机蓝牙标识、账号 token。
- 防御：
  - 强 WPA2/WPA3 口令，禁用 WEP/WPA/TKIP，启用管理帧保护。
  - BLE 使用安全配对、地址随机化、最小暴露 GATT 服务。
  - 固件签名更新、关闭默认口令、最小权限、端到端加密、日志审计、异常检测。

</details>

### 4. 详细阐述 Security Demands

题干：请详细阐述 IoT 的 Security Demands。

<details class="self-test-answer">
<summary>参考答案</summary>


- **IoT access security**：
  - 感知节点、用户和系统接入前必须认证与授权。
  - 关注设备身份、节点可信管理、访问控制和非法节点接入防护。
- **IoT communication security**：
  - 大量终端接入会造成拥塞并扩大 DoS 攻击面。
  - 需要加密、完整性、认证、抗重放、密钥管理和拥塞/异常流量防护。
- **IoT data privacy security**：
  - IoT 数据包含位置、健康、行为、家庭/企业活动等敏感信息。
  - 云计算和大数据提高处理能力，也会让用户失去对数据的直接控制。
  - 需要数据最小化、访问控制、加密存储/传输、脱敏、审计和隐私保护。
- **IoT computing system security**：
  - IoT 应用场景广泛，既有传统网络应用威胁，也有物理世界联动风险。
  - 需要认证、授权、审计、应用隔离、固件安全、可信更新、服务质量和故障恢复。
- 总结句：IoT 安全需求不是单层安全，而是接入、通信、数据、计算和应用的跨层协同。

</details>

### 5. 详细阐述 Security Architecture

题干：请详细阐述 IoT Security Architecture。

<details class="self-test-answer">
<summary>参考答案</summary>


- 按 IoT 系统结构，可把安全架构分为 sensing security、transmission security、data security、application security。
- **IoT sensing security**：
  - 保护传感器、RFID、摄像头、麦克风等感知节点。
  - 重点是身份认证、访问控制、防伪造节点、防物理篡改、防假数据注入。
- **IoT transmission security**：
  - 保护网络传输过程。
  - 重点是链路/端到端加密、完整性、认证、抗重放、抗 DoS、密钥管理和安全协议。
- **IoT data security**：
  - 保护数据的机密性、完整性和可用性。
  - 技术包括加密、访问控制、数字签名、备份、隔离、审计、隐私保护。
- **IoT application security**：
  - 保护智能家居、交通、医疗、工业等应用逻辑。
  - 重点是权限控制、业务逻辑安全、用户隐私、异常检测、日志审计和安全更新。
- 课件还提到 security control、security audit、privacy/security：不可否认、审计追踪、隐私保护是 IoT 架构中不可缺少的横向能力。

</details>

### 6. RFID tag 和 reader 之间传递敏感信息：被窃听怎么办

题干：一个 RFID tag 和一个接收者/reader 之间传递敏感信息，通信被窃听了，有何措施？如果你作为 reader，应如何解决？

<details class="self-test-answer">
<summary>参考答案</summary>


- 威胁：RFID 无线通信可被附近攻击者 eavesdrop；固定 ID 还会导致跟踪；攻击者可能重放、克隆或伪造标签。
- 传统思路：
  - 加密 tag-reader 通信，使用轻量级对称密钥或一次性随机数挑战响应。
  - 认证 reader 和 tag，防止非法 reader 扫描或伪造 tag。
  - 使用临时 ID/renaming，避免固定 ID 被长期跟踪。
  - 限制读取距离、屏蔽、kill tag、访问控制、后台校验。
- 按课件 RF-Cloak 的 reader 方案：
  - reader 随机化发送信号，使随机波形在空中类似 one-time pad。
  - 随机波形必须变化得足够快，带宽与 RFID 信号转移相当，并接近白噪声频谱。
  - 对抗 MIMO 窃听者时，可结合天线运动和快速天线切换，模拟大量快速变化信道，让攻击者难以消除随机波形。
  - 目标是不修改 RFID card/tag，也能让窃听者区分 0/1 的能力接近随机猜测。

</details>

## 3. 2024-2025 回忆卷：大题

据回忆，2024-2025 卷子与上一份基本一致，主要记住了大题。下面按 4 道 10 分题整理。

### 1. Hidden Terminal 问题和解决方法

题干补全：画图解释 hidden terminal 问题。为什么 CSMA 监听信道仍会发生碰撞？802.11 如何用 RTS/CTS 缓解？

<details class="self-test-answer">
<summary>参考答案</summary>

答案：见本页“回忆卷 A：简答题池”第 1 题。答题时一定画出 `A -> B <- C`，强调 A/C 互相听不到但都能干扰 B。

</details>

### 2. WEP 加密过程和安全隐患

题干补全：解释 WEP 加密过程，并指出其中的安全隐患。

<details class="self-test-answer">
<summary>参考答案</summary>


- 加密过程：
  1. 对 message 计算 CRC-32，得到 ICV。
  2. 拼接 24-bit IV 和共享密钥，作为 RC4 seed。
  3. RC4 生成 keystream。
  4. 将 `message || ICV` 与 keystream XOR 得到 ciphertext。
  5. IV 明文放在密文前一起发送。
- 解密过程：
  1. 接收方取出明文 IV。
  2. 用 `IV || key` 生成相同 keystream。
  3. XOR 恢复 message 和 ICV。
  4. 用 CRC 检查完整性。
- 安全隐患：
  - IV 只有 24 bit，空间太小，容易碰撞。
  - IV 明文传输且不禁止重用。
  - RC4 是流密码，同一 keystream 重用会导致 `C1 XOR C2 = P1 XOR P2`。
  - CRC-32 不是密码学 MAC，攻击者可修改数据并修正 CRC。
  - 缺少密钥管理，主密钥长期共享且手动配置。
  - 共享密钥认证会泄露挑战明文和加密挑战，可恢复 keystream。
  - 管理帧缺少认证，可导致 rogue AP、deauth/DoS 等问题。

</details>

### 3. 智能家居监控系统攻击与隐私

题干补全：一个智能家居监控系统使用室内 WiFi 和蓝牙/BLE，摄像头/传感器/手机 App 与云端联动。攻击者可以采取什么措施攻击？可以获取什么隐私？如何防御？

<details class="self-test-answer">
<summary>参考答案</summary>


- 攻击措施：
  - WiFi 嗅探、弱 PSK 字典攻击、rogue AP、deauth、jamming。
  - BLE 广播扫描、固定地址跟踪、未授权 GATT 读写、弱配对/MITM。
  - 摄像头默认口令、云 API token 泄露、App 越权、固件漏洞、未签名 OTA。
  - Botnet 入侵后发起 DDoS 或作为内网跳板。
- 获取隐私：
  - 视频/音频、家庭成员作息、是否在家、访客、孩子/老人活动。
  - 室内布局、设备清单、WiFi SSID、手机和 BLE 设备标识。
  - 报警记录、门磁/运动传感器状态、云账号信息。
- 防御：
  - 强 WiFi 安全配置、禁用 WEP/TKIP、强口令、网络隔离。
  - BLE 地址随机化、安全配对、最小服务暴露、访问授权。
  - 端到端加密、固件签名、默认口令强制修改、最小权限、日志审计、异常检测。
  - 隐私设计：最小采集、本地处理优先、数据脱敏、用户授权和可删除。

</details>

### 4. RFID tag-reader 敏感通信被窃听：作为 reader 如何解决

题干补全：一个 RFID tag 和 reader 之间传递敏感信息时被攻击者窃听。请说明可采取的保护措施，重点从 reader 侧说明。

<details class="self-test-answer">
<summary>参考答案</summary>

答案：见本页“回忆卷 A：简答题池”第 6 题。重点写 RF-Cloak：reader 随机化信号，random waveform acts like one-time pad on the air；对 MIMO 窃听者结合天线运动和快速天线切换，制造快速变化信道。

</details>

## 4. 考前速背版

- WiFi/WLAN 标准：IEEE 802.11；频段：2.4 GHz、5 GHz。
- DSSS 优点：减少频率选择性衰落；蜂窝中可同频复用并支持软切换；缺点是要精确功率控制。
- 单工/半双工/全双工：广播单工；蓝牙半双工 TDD；手机通话全双工；现代交换式以太网全双工。
- Channel Interleave：把突发错误打散，帮助信道编码纠错。
- IoT contradictions：高性能 vs 低能耗；强安全 vs 资源受限；大规模异构 vs 可管理；数据共享 vs 隐私。
- WiFi 缺少：良好干扰缓解机制，尤其密集 AP。
- WEP：完整性 CRC-32，加密 RC4，IV 24 bit，漏洞是 IV/keystream reuse、CRC 非 MAC、无密钥管理。
- WPA2：AES-CCMP，48-bit PN/IV，4-way handshake 派生 PTK。
- Security Objectives：Confidentiality、Integrity、Availability。
- WSN：能量受限、节点多、低速率、多跳/自组织、数据汇聚、网络智能。
- RFID：IoT 感知层；系统由 reader、tag、antenna 组成；保护包括 kill/rename/distance/policy、认证、轻量加密、RF-Cloak。
- Bluetooth：2.4 GHz ISM，TDMA-TDD slow frequency hopping，piconet master/slave；安全目标 Authentication/Confidentiality/Authorization；BLE 隐私靠配对、地址随机化、BLE-Guardian 等。
