---
title: "模拟卷 C：选择题与简答题"
source: "generated from past-exam style"
order: 102
---

# 模拟卷 C：选择题与简答题

## 0. 使用说明

本卷只保留历年卷常见的选择题和简答题。建议 50 分钟内完成：选择题先快速判断，简答题按“概念、原因、流程、防御”写关键词。

## 1. 选择题

### 选择题 1

题干：Hidden Terminal 问题中，A 和 C 互相听不到但都能到达 B，主要会导致什么？

选项：

- A. A 和 C 都以为信道空闲，同时发给 B 并在 B 处碰撞
- B. B 自动获得更高信噪比
- C. WEP 的 IV 被扩展到 48 bit
- D. RFID tag 自动进入 sleep

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Hidden Terminal 的关键是发送端听不到另一个发送端，但接收端会被二者同时干扰。RTS/CTS 通过接收端 CTS 通知隐藏节点退避。

</details>

### 选择题 2

题干：Exposed Terminal 问题最准确的描述是？

选项：

- A. 节点听到附近发送后过度退避，抑制了本可并发的通信
- B. 攻击者恢复了 WEP 密钥
- C. RFID reader 随机化波形
- D. Bluetooth 进入 piconet

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Hidden Terminal 带来接收端碰撞，Exposed Terminal 带来空间复用不足。二者都说明无线发送端侦听不能完全代表接收端干扰状态。

</details>

### 选择题 3

题干：slow fading 的 major cause 在课程中最接近哪一项？

选项：

- A. Shadowing Effect
- B. CRC-32 线性
- C. Michael MIC 失败计数
- D. APDU 命令格式

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：slow fading 是大尺度、较慢变化的衰落，常由遮挡和阴影效应造成；fast fading 更常与多径和移动导致的小尺度快速变化相关。

</details>

### 选择题 4

题干：Channel Interleaving 的作用是？

选项：

- A. 把连续错误分散开，帮助纠错码处理突发错误
- B. 直接提供用户授权
- C. 替代 WPA2 的 4-way handshake
- D. 让 RFID tag 不再需要 reader

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：无线信道可能出现 burst error。交织将相邻比特分散到不同位置，使纠错码面对更随机的错误分布。

</details>

### 选择题 5

题干：IoT 四层模型中，RFID、传感器、摄像头属于哪一层？

选项：

- A. 感知识别层
- B. 管理服务层
- C. 应用层
- D. 只属于云数据库层

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：感知识别层负责从物理世界采集、识别和输入数据。RFID、传感器、摄像头、麦克风都属于典型感知设备。

</details>

### 选择题 6

题干：IoT Security Demands 中 communication security 主要关注什么？

选项：

- A. 传输过程中的加密、认证、完整性、抗重放和抗 DoS
- B. 只关注显示屏分辨率
- C. 只关注 RFID 标签颜色
- D. 只关注 WiFi 的品牌

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：communication security 是传输安全需求，常见关键词包括加密、完整性、认证、密钥管理、抗重放、拥塞和 DoS 防护。

</details>

### 选择题 7

题干：IoT Security Architecture 更像是在回答哪个问题？

选项：

- A. 安全措施分别部署在 sensing、transmission、data、application 哪些层
- B. WEP 为什么使用 RC4
- C. Bluetooth 为什么有 piconet
- D. NFC 为什么距离短

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Security Demands 是需求视角，Security Architecture 是结构视角。答题时可以把需求映射到感知、传输、数据和应用层。

</details>

### 选择题 8

题干：WEP 使用的流密码算法是？

选项：

- A. RC4
- B. AES-CCMP
- C. RSA
- D. ECDSA

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WEP 使用 RC4，seed 为 `IV || shared key`。RC4 本身是流密码，同一密钥流绝不能重复使用。

</details>

### 选择题 9

题干：WEP 中 ICV 使用的 CRC-32 最大问题是什么？

选项：

- A. 无密钥且线性，不是密码学 MAC
- B. 太慢导致无法传输
- C. 只能用于 Bluetooth
- D. 会自动加密明文

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：CRC-32 只能检测随机错误。攻击者可修改密文并同步修正 CRC，因此它不能保证密码学完整性。

</details>

### 选择题 10

题干：WEP IV 长度是多少？

选项：

- A. 24 bit
- B. 48 bit
- C. 96 bit
- D. 128 bit

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WEP 的 IV 是 24 bit，空间太小，随机使用很快出现生日碰撞，顺序使用也可能在重启后重复。

</details>

### 选择题 11

题干：WPA/TKIP 的定位最准确的是？

选项：

- A. 保留 RC4 兼容旧硬件，并用 TKIP、Michael、48-bit IV 等修补 WEP
- B. 完全等同 WPA2/CCMP
- C. 只用于 RFID 防冲突
- D. 只解决 NFC relay

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WPA/TKIP 是过渡方案，修补 WEP 的密钥混合、完整性和重放保护，但安全强度仍不如 WPA2/CCMP。

</details>

### 选择题 12

题干：WPA2/CCMP 中 PN 的主要作用是？

选项：

- A. 防重放并参与构造 fresh nonce
- B. 计算 RFID 标签数量
- C. 表示 Bluetooth master 地址
- D. 表示 Shannon limit

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：CCMP 使用 48-bit Packet Number。PN 单调增加，用于防重放，也用于构造 AES-CTR/CBC-MAC 所需 nonce。

</details>

### 选择题 13

题干：WPA2 4-way handshake 派生 PTK 的输入不包括哪项？

选项：

- A. PMK
- B. ANonce 与 SNonce
- C. AP MAC 与 STA MAC
- D. RFID tag 的 EPC 编码

<details class="self-test-answer">
<summary>参考答案</summary>

答案：D。

解析：PTK 派生依赖 PMK、双方 nonce 和双方 MAC。EPC 是 RFID 对象识别相关内容，不属于 WPA2 握手。

</details>

### 选择题 14

题干：KRACK 攻击主要利用什么？

选项：

- A. 重传握手消息导致客户端重新安装已安装密钥并重置 nonce/PN
- B. 暴力破解 AES
- C. 读取 RFID tag 颜色
- D. 关闭 Bluetooth 跳频

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：KRACK 是 key reinstallation attack，不是破解 WiFi 密码或 AES。核心后果是 nonce 重用，进而可能解密、重放或注入部分流量。

</details>

### 选择题 15

题干：无源 RFID tag 常通过什么方式向 reader 回传信息？

选项：

- A. Backscatter / 反向散射
- B. WPA2 4-way handshake
- C. DNS 查询
- D. TCP 三次握手

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：无源 tag 从 reader 电磁场取能，并通过改变负载影响反射信号，也就是 backscatter。

</details>

### 选择题 16

题干：Frame Slotted ALOHA 的时隙结果通常分为哪三类？

选项：

- A. 空时隙、单标签成功、冲突时隙
- B. 明文、密文、签名
- C. KCK、KEK、TK
- D. PCD、PICC、APDU

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：RFID 防冲突算法常通过统计空时隙、成功时隙和碰撞时隙来估计标签数量并调整帧大小。

</details>

### 选择题 17

题干：RF-Cloak 的核心思想是？

选项：

- A. Reader 侧随机化发送信号，让空中随机波形类似 one-time pad
- B. 永远公开固定 tag ID
- C. 使用 WEP CRC-32 加密 RFID
- D. 关闭所有 reader

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：RF-Cloak 重点是 reader 侧随机化，尽量不改低成本 tag，使窃听者难以从空中信号区分 bit。

</details>

### 选择题 18

题干：Bluetooth security 的三个核心目标是？

选项：

- A. Authentication、Confidentiality、Authorization
- B. CRC、IV、RC4
- C. REQA、ATQA、SAK
- D. Kill、Rename、Distance

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Bluetooth 课程中列出的安全目标是认证、机密性和授权。

</details>

### 选择题 19

题干：Bluetooth Classic 的 piconet 中通常由谁设置 clock 和 hopping sequence？

选项：

- A. Master
- B. RFID tag
- C. NFC target
- D. DNS resolver

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Classic Bluetooth piconet 中一个 master 管理多个 slave，slave 同步到 master clock 和跳频序列。

</details>

### 选择题 20

题干：BLE 广播隐私风险中，哪些信息可能被用于 tracking？

选项：

- A. 地址、设备名、服务 UUID、manufacturer data、RSSI 和时间模式
- B. 只有纸质准考证号
- C. 只有 WEP 的 CRC
- D. 只有 Shannon 公式

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：BLE 地址随机化只能减少一部分跟踪。payload、服务 UUID、厂商数据、RSSI 和广播间隔仍可能形成指纹。

</details>

## 2. 简答题

### 简答题 1

题干：画图解释 Hidden Terminal，并说明 RTS/CTS 如何缓解。

<details class="self-test-answer">
<summary>参考答案</summary>

可画：

```text
A  --->  B  <---  C
A 与 C 互相听不到，但都能干扰 B。
```

要点：A 和 C 在发送端听不到彼此，都判断信道空闲；同时向 B 发送时碰撞发生在 B。RTS/CTS 中，A 发 RTS，B 回 CTS，C 听到 B 的 CTS 后设置 NAV 并退避。缺点是控制帧有开销，小帧不一定划算。

</details>

### 简答题 2

题干：说明 WEP 加密流程和主要安全隐患。

<details class="self-test-answer">
<summary>参考答案</summary>

流程：message 计算 CRC-32 得到 ICV；`IV || shared key` 输入 RC4 生成 keystream；`message || ICV` 与 keystream XOR 得到 ciphertext；IV 明文发送。隐患：24-bit IV 短且可重用；RC4 keystream 重用导致 `C1 XOR C2 = P1 XOR P2`；CRC-32 无密钥且线性；缺少密钥管理；共享密钥认证会泄露 keystream；管理帧认证不足带来 rogue AP 和 deauth 风险。

</details>

### 简答题 3

题干：简述 WPA2 4-way handshake 的输入、消息作用和 PTK 子密钥。

<details class="self-test-answer">
<summary>参考答案</summary>

输入：PMK、ANonce、SNonce、AP MAC、STA MAC。Msg1 AP 发 ANonce；Msg2 STA 发 SNonce 和 MIC，证明持有 PMK；Msg3 AP 发 GTK/RSN key data 并通知安装密钥；Msg4 STA 确认。PTK 常拆为 KCK、KEK、TK：KCK 保护 EAPOL-Key MIC，KEK 加密 key data，TK 加密单播数据；GTK 用于组播/广播。

</details>

### 简答题 4

题干：阐述 IoT Security Demands 和 IoT Security Architecture 的区别。

<details class="self-test-answer">
<summary>参考答案</summary>

Security Demands 是需求视角，包括 access security、communication security、data privacy security、computing system security，回答“需要保护什么”。Security Architecture 是结构视角，包括 sensing security、transmission security、data security、application security，回答“在哪一层部署保护”。答题时可先列需求，再映射到感知、传输、数据和应用层。

</details>

### 简答题 5

题干：RFID tag 与 reader 传递敏感信息被窃听时，可采取哪些保护？重点说明 reader 侧 RF-Cloak。

<details class="self-test-answer">
<summary>参考答案</summary>

威胁包括窃听固定 ID、跟踪、重放、克隆和伪造。常规保护包括轻量级挑战响应、临时 ID/renaming、访问控制、限制距离、屏蔽和后台校验。RF-Cloak 从 reader 侧随机化波形，让空中随机信号类似 one-time pad；波形应快速变化并接近白噪声。对 MIMO 窃听者可结合天线运动和快速天线切换，使窃听者难以消除随机化。

</details>

### 简答题 6

题干：说明 Bluetooth/BLE 在智能门锁中的攻击面和防御。

<details class="self-test-answer">
<summary>参考答案</summary>

攻击面：BLE advertising 泄露地址、设备名、UUID、manufacturer data 和 RSSI；固定地址或稳定 payload 可被 tracking；弱 PIN、配对降级、MITM、未授权 GATT 写入可能导致控制风险；Classic Bluetooth 还可提 sniffing、replay、Blue snarfing。防御：地址随机化、最小化广播 payload、安全配对、MITM 保护、GATT 授权、禁用降级、固件签名更新和日志审计。

</details>
