---
title: "模拟卷 A：历年卷风格练习"
source: "generated from past-exam style"
order: 100
---

# 模拟卷 A：历年卷风格练习

## 0. 使用说明

本卷按现有历年卷页面的题型结构生成：20 道客观题、6 道简答题池、4 道综合大题。题型、答题方式和考点密度保持一致，题干和场景做了变化。建议先独立作答，再展开参考答案。

## 1. 模拟卷 A：选择/填空式客观题

### 客观题 1

题干：IEEE 802.11 无线局域网在课程中主要对应哪些公共频段？

选项：

- A. 125 kHz 和 13.56 MHz
- B. 2.4 GHz 和 5 GHz
- C. 433 MHz 和 868 MHz
- D. 77 GHz 和 24 GHz

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：课程按传统 WLAN 重点记 2.4 GHz 和 5 GHz。13.56 MHz 更接近 HF RFID/NFC，77 GHz 常见于车载雷达，不是本题所问 WiFi 频段。

</details>

### 客观题 2

题干：为什么课件说密集 AP 部署下 WiFi 标准缺少良好的干扰缓解机制？

选项：

- A. 因为 WiFi 没有任何 MAC 协议
- B. 因为静态信道、功率和载波侦听阈值会造成争用和低频谱复用
- C. 因为所有 AP 都只能使用有线 CSMA/CD
- D. 因为 802.11 不能在室内使用

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：历年卷常考“WiFi 标准缺少 good mechanisms to mitigate interference”。答题时写密集 AP、静态信道/功率/载波侦听阈值、争用和吞吐下降即可。

</details>

### 客观题 3

题干：无线 slow fading 的 major cause 在课程中更贴近哪一项？

选项：

- A. Shadowing effect
- B. CRC-32 线性
- C. APDU 格式错误
- D. 4-way handshake 的 MIC

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：slow fading 常由障碍物遮挡、地形和大尺度环境变化引起，即 shadowing。多径造成的快速起伏更接近 fast fading。

</details>

### 客观题 4

题干：Hidden Terminal 问题中，A 与 C 互相听不到但都能到达 B。802.11 常用哪种机制缓解？

选项：

- A. RTS/CTS 和 NAV
- B. CRC-32
- C. Kill tag
- D. HCE

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：A 先发 RTS，B 回 CTS；隐藏节点 C 若听到 B 的 CTS，会根据持续时间设置 NAV 并退避，从而减少 B 处碰撞。

</details>

### 客观题 5

题干：Channel Interleaving 的主要作用是什么？

选项：

- A. 将突发错误打散，让纠错码更容易处理
- B. 直接完成用户授权
- C. 替代所有加密
- D. 固定所有设备的蓝牙地址

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：无线衰落可能造成连续比特错误。交织把相邻比特分散到不同时间/位置，使纠错码看到更随机的错误。

</details>

### 客观题 6

题干：NIST/课程中最基本的三个 Security Objectives 是什么？

选项：

- A. Confidentiality, Integrity, Availability
- B. Authentication, Authorization, Accounting
- C. Routing, Switching, Forwarding
- D. Encryption, Hashing, Compression

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：CIA 三元组是所有安全分析的底座。认证、授权、问责也重要，但不是本题问的三个基本目标。

</details>

### 客观题 7

题干：IoT 四层模型中，RFID、传感器、摄像头主要属于哪一层？

选项：

- A. Sensing and Recognition Layer
- B. Application Layer
- C. Management and Service Layer
- D. 只属于 cloud storage

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：感知识别层负责采集、识别和连接物理世界，RFID 与传感器是典型代表。

</details>

### 客观题 8

题干：下列哪组最符合 IoT 系统中的 contradictions？

选项：

- A. High connectivity vs. Security and Privacy
- B. High performance vs. Low energy
- C. Scalability vs. Reliability and Predictability
- D. 以上都是

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：IoT 不是单一协议问题，而是资源、规模、隐私、安全、可靠性和开放性之间的工程取舍。

</details>

### 客观题 9

题干：IoT communication security 最关注下列哪类问题？

选项：

- A. 传输过程中的加密、完整性、认证、抗重放、拥塞和 DoS 防护
- B. 只关注标签外壳颜色
- C. 只关注 WEP 的 24-bit IV
- D. 只关注显示器分辨率

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Security Demands 中 communication security 对应网络传输安全，答题关键词是加密、认证、完整性、抗重放、密钥管理、拥塞和 DoS。

</details>

### 客观题 10

题干：下列哪项属于 Wireless Sensor Network 的典型特点？

选项：

- A. 节点能量受限、数量多、低速率，数据通常汇聚到中心
- B. 所有节点都必须是服务器级计算机
- C. 只用于有线核心网
- D. 不需要任何无线通信

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WSN 重点是低功耗、低速率、多节点、能量约束、多跳或汇聚式数据收集。

</details>

### 客观题 11

题干：WEP 的 Initialization Vector 长度是多少？

选项：

- A. 16 bit
- B. 24 bit
- C. 48 bit
- D. 128 bit

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：WEP 使用 24-bit IV，并将 `IV || shared key` 输入 RC4。IV 空间太小且明文发送，是 WEP 失败的重要原因。

</details>

### 客观题 12

题干：WEP 的 ICV 使用什么算法？

选项：

- A. CRC-32
- B. CBC-MAC
- C. HMAC-SHA256
- D. ECDSA

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：CRC-32 适合检测随机错误，但它无密钥且线性，不是密码学 MAC，攻击者可以改密文并同步修正校验。

</details>

### 客观题 13

题干：WPA/TKIP 中 Michael MIC 的定位是什么？

选项：

- A. 在兼容旧硬件的前提下补强消息完整性，但强度有限
- B. 完全替代 AES-CCMP
- C. 用于 NFC 的 APDU 路由
- D. 用于 RFID 防冲突

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WPA/TKIP 是对 WEP 的过渡性修补。Michael MIC 比 CRC-32 更像完整性保护，但受旧硬件限制，安全强度仍有限。

</details>

### 客观题 14

题干：WPA2/CCMP 中 CTR、CBC-MAC、PN 分别主要负责什么？

选项：

- A. 机密性、完整性、防重放/构造 nonce
- B. 供电、调制、天线极化
- C. 标签销毁、重命名、立法
- D. 语音克隆、降噪、识别

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：CCMP 用 AES-CTR 加密，用 CBC-MAC 做完整性/来源保护，用 48-bit PN 防重放并保证 nonce 新鲜。

</details>

### 客观题 15

题干：WPA2 4-way handshake 派生 PTK 的关键输入不包括哪一项？

选项：

- A. PMK
- B. ANonce 和 SNonce
- C. AP MAC 和 STA MAC
- D. RFID tag EPC 编码

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：PTK 由 PMK、双方 nonce 和双方 MAC 派生。RFID tag EPC 不属于 WiFi 4-way handshake。

</details>

### 客观题 16

题干：Frame Slotted ALOHA 中，一个时隙可能出现哪几种状态？

选项：

- A. 空时隙、单标签成功、冲突时隙
- B. 明文、密文、签名
- C. KCK、KEK、TK
- D. PCD、PICC、APDU

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：RFID 防冲突题常按 slot 结果分析：没有 tag 响应是空时隙，一个 tag 响应是成功，多个 tag 同时响应是碰撞。

</details>

### 客观题 17

题干：下列哪项是 RFID 隐私保护方法？

选项：

- A. Kill tag
- B. Re-naming tags
- C. Distance measurement
- D. 以上都是

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：Kill、重命名、距离策略和政策/法律都在课件中作为 RFID 隐私保护思路出现，各自有功能牺牲或部署条件。

</details>

### 客观题 18

题干：RF-Cloak 的核心思想最接近哪一项？

选项：

- A. Reader 侧随机化信号，让空中随机波形起到类似 one-time pad 的效果
- B. 固定 tag ID 便于长期跟踪
- C. 关闭所有 reader 天线
- D. 使用 WEP 的 CRC-32 保护 RFID

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：RF-Cloak 强调 reader 侧随机化波形，尽量不修改低成本 tag，使窃听者难以从空中信号判断 0/1。

</details>

### 客观题 19

题干：Bluetooth Classic piconet 中，谁通常设置时钟和跳频序列？

选项：

- A. Master
- B. 任意被动窃听者
- C. RFID tag
- D. DNS 服务器

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Classic Bluetooth piconet 中一个 master 管理多个 slave，节点同步到 master clock 和 hopping sequence。

</details>

### 客观题 20

题干：BLE 广播中哪些信息可能造成 tracking/profiling？

选项：

- A. 地址、设备名、服务 UUID、manufacturer data、RSSI 和广播时间模式
- B. 只有纸质发票号码
- C. 只有 WEP 的 ICV
- D. 只有蜂窝基站的电费

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：即使使用地址随机化，payload、服务 UUID、manufacturer data、RSSI 和时序模式也可能组合成设备指纹。

</details>

## 2. 简答题池

### 简答题 1

题干：画图解释 Hidden Terminal 问题，并说明 RTS/CTS 如何缓解。

<details class="self-test-answer">
<summary>参考答案</summary>

可画：

```text
A  --->  B  <---  C
A 和 C 互相听不到，但都能干扰 B。
```

要点：

- A 和 C 只在发送端做 carrier sensing，互相听不到时都会认为信道空闲。
- 二者同时发给 B，会在 B 处碰撞。
- A 先发 RTS，B 回复 CTS。
- C 即使听不到 A，也能听到 B 的 CTS，于是设置 NAV 并等待。
- RTS/CTS 适合较大帧，小包会增加控制开销。

</details>

### 简答题 2

题干：说明 WEP 的加密流程，并指出它为什么失败。

<details class="self-test-answer">
<summary>参考答案</summary>

流程：

1. 对 message 计算 CRC-32，得到 ICV。
2. 拼接 `IV || shared key` 作为 RC4 seed。
3. RC4 生成 keystream。
4. 将 `message || ICV` 与 keystream XOR 得到 ciphertext。
5. IV 明文随密文发送。

失败原因：

- 24-bit IV 太短，容易重复。
- IV 明文传输且没有强制禁止重用。
- 同一 keystream 重用会暴露 `P1 XOR P2`。
- CRC-32 无密钥且线性，不是 MAC。
- 缺少密钥管理，主密钥长期共享。
- 共享密钥认证和管理帧缺陷还会带来认证绕过、rogue AP、deauth 等问题。

</details>

### 简答题 3

题干：阐述 WPA2 4-way handshake 的输入、四条消息和密钥安装结果。

<details class="self-test-answer">
<summary>参考答案</summary>

- 目的：证明双方都持有 PMK，并协商新鲜 PTK。
- 输入：PMK、ANonce、SNonce、AP MAC、STA MAC。
- Msg1：AP 发 ANonce 给 STA。
- Msg2：STA 生成 SNonce 和 PTK，发 SNonce 与 MIC，证明自己持有 PMK/可生成 PTK。
- Msg3：AP 验证后发送带 MIC 的 key data，通常包含 GTK，并通知 STA 安装密钥。
- Msg4：STA 确认密钥安装。
- PTK 拆为 KCK、KEK、TK：KCK 算 EAPOL-Key MIC，KEK 加密 key data，TK 加密单播数据；GTK 用于广播/组播。

</details>

### 简答题 4

题干：详细阐述 IoT Security Demands，并说明它和 Security Architecture 的区别。

<details class="self-test-answer">
<summary>参考答案</summary>

Security Demands 是“需要保护什么能力”：

- Access security：设备、用户和节点接入前的认证、授权和访问控制。
- Communication security：传输中的加密、完整性、认证、抗重放、密钥管理和抗 DoS。
- Data privacy security：位置、健康、家庭行为等敏感数据的最小采集、加密、脱敏、访问控制和审计。
- Computing system security：IoT 应用、云/边缘、固件、服务质量、可信更新和恢复。

Security Architecture 是“按系统层次如何部署保护”：

- Sensing security、transmission security、data security、application security。
- 前者按需求分类，后者按 IoT 系统层次分配防护。

</details>

### 简答题 5

题干：一个 RFID tag 与 reader 传递敏感信息被窃听。请说明威胁和 reader 侧保护方案。

<details class="self-test-answer">
<summary>参考答案</summary>

- 威胁：窃听 tag-reader 空中通信、长期跟踪固定 ID、重放、克隆或伪造标签。
- 传统保护：轻量级加密、挑战响应、临时 ID/renaming、访问控制、屏蔽、限制读取距离和后台校验。
- Reader 侧 RF-Cloak：
  - Reader 随机化发射波形。
  - 随机波形在空中类似 one-time pad。
  - 波形应变化快、接近白噪声，并覆盖 RFID 信号变化。
  - 面对 MIMO 窃听者，可结合天线运动和快速天线切换制造快速变化信道。
  - 目标是在不改低成本 tag 的情况下让窃听者接近随机猜测。

</details>

### 简答题 6

题干：说明 Bluetooth Classic 的 piconet、跳频和安全目标，并列出 BLE tracking 的防护思路。

<details class="self-test-answer">
<summary>参考答案</summary>

- Classic Bluetooth 工作在 2.4 GHz ISM，采用 TDMA-TDD slow frequency hopping。
- Piconet 中一个 master、多个 slave，slave 同步到 master 的 clock 和 hopping sequence。
- 安全目标：Authentication、Confidentiality、Authorization。
- 风险：sniffing、replay、downgrade、弱 PIN、未授权服务访问、固定地址追踪。
- BLE tracking 防护：地址随机化、最小化 advertising payload、隐藏敏感服务 UUID、限制 GATT 暴露、使用安全配对和授权、采用 BLE-Guardian 等授权连接方案。

</details>

## 3. 综合大题

### 大题 1

题干：某教学楼里 A、C 两个终端都能连接 AP B，但 A 和 C 之间隔着墙，彼此检测不到信号。请画图说明 Hidden Terminal，解释为什么普通 CSMA 仍会碰撞，并说明 RTS/CTS 的流程、优点和代价。

<details class="self-test-answer">
<summary>参考答案</summary>

答题要点：

- 图示 `A -> B <- C`，标明 A/C 互相听不到但都能到达 B。
- 普通 CSMA 在发送端监听；A 听不到 C 不代表 B 不会被 C 干扰。
- A、C 同时发送时，碰撞发生在接收端 B。
- RTS/CTS 流程：A 发 RTS，B 回 CTS，C 听到 CTS 后按 duration 设置 NAV 并退避。
- 优点：减少隐藏终端导致的大数据帧碰撞。
- 代价：控制帧增加开销，小包或低负载场景未必划算。

</details>

### 大题 2

题干：解释 WPA2 4-way handshake 和 KRACK 的关系。为什么 KRACK 不是破解密码或 AES？它利用了什么实现/协议状态问题，可能造成什么后果？

<details class="self-test-answer">
<summary>参考答案</summary>

答题要点：

- 4-way handshake 用 PMK、ANonce、SNonce、AP MAC、STA MAC 派生 PTK，证明双方持有 PMK。
- Msg3 通知 STA 安装密钥并携带 GTK 等 key data；Msg4 是确认。
- KRACK 不破解 WiFi 密码、不暴力破解 PMK，也不破解 AES。
- 它利用 Msg3 重传时客户端可能重新安装已安装密钥的实现/状态问题。
- 重新安装会重置 nonce/PN/replay counter 等状态，导致 nonce 重用。
- 后果：可能解密、重放、注入部分流量，影响具体取决于协议和实现。
- 防御：补丁禁止重复安装同一密钥时重置 nonce，严格状态机，使用更新系统和驱动。

</details>

### 大题 3

题干：一个智慧医院系统包含 RFID 药品标签、BLE 体征传感器、WiFi 摄像头、护士手机 App 和云平台。请按 IoT Security Demands 分析主要威胁、可能泄露的隐私和防御措施。

<details class="self-test-answer">
<summary>参考答案</summary>

可按四类 demands 写：

- Access security：非法设备接入、冒充护士账号、伪造传感节点。防御是设备身份认证、用户多因素认证、最小权限、访问控制和审计。
- Communication security：WiFi/BLE/RFID 空中窃听、重放、DoS、弱配对。防御是链路或端到端加密、完整性、抗重放、强配对、网络隔离、异常流量检测。
- Data privacy security：病人身份、用药记录、位置轨迹、视频和体征数据泄露。防御是最小采集、脱敏、加密存储、访问审批、日志审计和数据生命周期管理。
- Computing system security：云 API 越权、App token 泄露、固件漏洞、未签名 OTA。防御是安全更新、固件签名、密钥保护、云端权限校验、备份和恢复。
- 总结：IoT 安全是感知、通信、数据、应用跨层协同，不是只给某个链路加密。

</details>

### 大题 4

题干：一个仓库使用无源 RFID 管理高价值货物。攻击者可以在通道附近窃听 reader 与 tag 的通信。请说明攻击者能做什么，并从 RFID 隐私保护和 RF-Cloak 角度提出防御。

<details class="self-test-answer">
<summary>参考答案</summary>

答题要点：

- 攻击能力：窃听 tag ID 或业务数据，跟踪货物流动，重放响应，克隆标签，分析库存和运输规律。
- 常规隐私保护：kill tag、renaming/临时 ID、距离控制、访问控制、屏蔽、后台校验和政策限制。
- 轻量级认证：challenge-response、随机数、防重放、共享密钥或物理层指纹。
- RF-Cloak：reader 生成随机波形，让 tag 响应在空中被随机化，窃听者难以恢复 bit。
- 对抗强窃听者：天线运动、快速天线切换和快速变化信道。
- 取舍：尽量不修改低成本 tag，但 reader 复杂度和部署环境会影响效果。

</details>
