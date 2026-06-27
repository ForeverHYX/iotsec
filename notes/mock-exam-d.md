---
title: "模拟卷 D：选择题与简答题"
source: "generated from past-exam style"
order: 103
---

# 模拟卷 D：选择题与简答题

## 0. 使用说明

本卷只包含选择题和简答题，题型按历年卷常见答法组织，不设置大题。重点覆盖无线基础、WEP/WPA/WPA2、IoT Security、RFID、Bluetooth/BLE 等高频点。

## 1. 选择题

### 选择题 1

题干：WiFi/Wireless LAN 主要对应哪个 IEEE 标准族？

选项：

- A. IEEE 802.11
- B. IEEE 802.3
- C. ISO 14443
- D. EPC Gen2 only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WiFi 使用 IEEE 802.11 标准族。802.3 是以太网，ISO 14443 与 NFC/近场卡流程相关。

</details>

### 选择题 2

题干：DSSS 的一个优点是？

选项：

- A. 扩展信号频带，减轻频率选择性衰落，并可支持软切换
- B. 完全不需要功率控制
- C. 只能用于有线通信
- D. 自动替代所有认证协议

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：DSSS 将信号扩展到更宽频带，增强抗窄带干扰和频率选择性衰落能力；但它通常仍需要功率控制。

</details>

### 选择题 3

题干：near-far effect 中，接收端最容易遇到什么问题？

选项：

- A. 近处强信号淹没远处弱信号
- B. WEP IV 自动不重复
- C. Bluetooth 不再跳频
- D. RFID reader 无法发射电磁场

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：near-far effect 是无线多用户接收中的功率差问题，强近端信号会让弱远端信号难以被正确解码。

</details>

### 选择题 4

题干：CSMA/CA 中 ACK 的作用最接近哪一项？

选项：

- A. 接收端确认帧已正确收到，发送端未收到 ACK 会认为可能失败并重传
- B. 提供 WEP 密钥管理
- C. 生成 RFID tag ID
- D. 计算 BLE 地址随机化

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：无线环境中发送端难以直接检测碰撞，因此 802.11 使用 ACK 和退避机制间接判断传输是否成功。

</details>

### 选择题 5

题干：RTS/CTS 缓解 Hidden Terminal 时，隐藏节点通常听到哪一帧后退避？

选项：

- A. 接收端发出的 CTS
- B. WEP 的 ICV
- C. RFID 的 RN16
- D. NFC 的 APDU response

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：隐藏节点可能听不到发送端 RTS，但能听到接收端 CTS，于是根据 CTS 中的持续时间设置 NAV 并退避。

</details>

### 选择题 6

题干：IoT 中 high connectivity vs. security and privacy 属于什么？

选项：

- A. Contradictions
- B. WEP encryption steps
- C. Bluetooth service levels
- D. RFID modulation categories only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：IoT contradictions 表示工程取舍，例如高连接性与安全隐私、高性能与低能耗、可扩展性与可靠可预测性之间的冲突。

</details>

### 选择题 7

题干：IoT data privacy security 最关注哪类内容？

选项：

- A. 位置、健康、家庭行为、设备状态等敏感数据的采集、存储、使用和共享
- B. 只关注天线极化
- C. 只关注 AP 信道号
- D. 只关注 CRC 多项式

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：IoT 数据常与真实生活和物理空间绑定，隐私保护要考虑最小采集、授权、脱敏、加密、审计和删除。

</details>

### 选择题 8

题干：WEP 的 seed 由什么组成？

选项：

- A. IV || shared key
- B. PMK || ANonce || SNonce
- C. APDU || FWT
- D. master clock || hopping sequence

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：WEP 将明文 IV 与长期共享密钥拼接后输入 RC4。IV 短且可重用导致密钥流重复风险。

</details>

### 选择题 9

题干：WEP FMS attack 主要利用什么？

选项：

- A. RC4 weak IV 与已知明文头部
- B. Bluetooth 地址随机化
- C. RFID Q 值调整
- D. IoT 云端审计

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：FMS 通过收集足够多带 weak IV 的包，结合已知 SNAP/LLC 头部等明文，利用 RC4 KSA 弱点恢复 WEP key。

</details>

### 选择题 10

题干：WPA-PSK 离线字典攻击通常依赖什么材料？

选项：

- A. 捕获到的一次 4-way handshake
- B. RFID 标签颜色
- C. NFC 卡片厚度
- D. Shannon 公式

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：攻击者捕获握手后可离线尝试口令，派生 PMK/PTK 并检查 MIC。弱口令是核心风险。

</details>

### 选择题 11

题干：WPA2/CCMP 中负责机密性的是？

选项：

- A. AES-CTR
- B. CRC-32
- C. Kill tag
- D. GATT

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：CCMP 中 AES-CTR 负责加密，CBC-MAC 负责完整性，PN/nonce 防重放和密钥流重用。

</details>

### 选择题 12

题干：KRACK 不属于哪一类攻击？

选项：

- A. 暴力破解 WiFi 密码或 AES
- B. 利用密钥重安装
- C. 利用握手消息重传处理问题
- D. 造成 nonce 重用风险

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：KRACK 的核心是 key reinstallation，不是破解 PMK、PSK 或 AES 算法。

</details>

### 选择题 13

题干：RFID 系统中 reader 的基本功能不包括哪项？

选项：

- A. 天然保证所有标签不可克隆且不可跟踪
- B. 与 tag 通信并读取/写入信息
- C. 为无源 tag 提供能量
- D. 连接后台应用或中间件

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：不可克隆、不可跟踪是安全目标或防护结果，不是 RFID 系统天然功能。

</details>

### 选择题 14

题干：RFID 隐私保护方法中，Kill tag 的主要代价是什么？

选项：

- A. 保护售后隐私但牺牲标签后续功能
- B. 自动提升标签计算能力
- C. 自动生成 WPA2 密钥
- D. 让 Bluetooth 变成全双工

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Kill tag 可以阻止售后读取和跟踪，但标签被杀死后也无法继续支持售后服务、退换货或生命周期管理。

</details>

### 选择题 15

题干：HB/HB+ 适合低成本 RFID 的原因是？

选项：

- A. 主要使用点积、异或和噪声等轻量操作
- B. 必须运行 RSA-4096
- C. 必须连接云服务器
- D. 不需要任何随机性

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：HB/HB+ 基于 LPN 思路，计算轻量，适合资源受限 tag；HB+ 还通过 blinding 改进对主动攻击的防护。

</details>

### 选择题 16

题干：Bluetooth Classic 物理层/拓扑特征最准确的是？

选项：

- A. 2.4 GHz、TDMA-TDD slow frequency hopping、piconet
- B. 13.56 MHz、APDU、FWT
- C. 24-bit IV、RC4、CRC-32
- D. EPC、backscatter、Q Algorithm only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Classic Bluetooth 是短距 2.4 GHz PAN 技术，使用 TDMA-TDD slow frequency hopping，并组织为 piconet/scatternet。

</details>

### 选择题 17

题干：Bluetooth Mode 2 的安全控制位置更接近哪一层？

选项：

- A. Service level
- B. Physical tag kill command
- C. WEP ICV
- D. Shannon capacity

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Mode 2 是 service level security，连接建立后按服务做认证、授权或加密；Mode 3 更偏 link level，在连接建立前控制。

</details>

### 选择题 18

题干：Blue snarfing 指什么？

选项：

- A. 未授权读取 Bluetooth 设备中的联系人、短信、文件等数据
- B. 正常连接蓝牙耳机
- C. RFID 防冲突中的成功时隙
- D. WEP 的 IV 拼接

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Blue snarfing 是蓝牙攻击名，重点是未授权获取设备数据。

</details>

### 选择题 19

题干：BLE-Guardian 的思路最接近哪项？

选项：

- A. 隐藏 BLE advertising，并控制授权连接
- B. 使用 CRC-32 加密 WiFi
- C. 永久公开固定 BLE 地址
- D. 让 RFID tag 不再需要 reader

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：BLE-Guardian 关注 BLE 设备被扫描和未授权连接的问题，通过隐藏广告、代理或授权机制降低暴露面。

</details>

### 选择题 20

题干：智能家居监控系统中，攻击者通过 WiFi/BLE/云 App 可能获取什么隐私？

选项：

- A. 是否在家、开门时间、视频音频、设备清单、账号 token
- B. 只有天气预报
- C. 只有随机噪声
- D. 只有纸张厚度

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：IoT 安全题要把技术攻击和现实隐私联系起来，尤其是作息、位置、家庭成员、视频音频和账号凭据。

</details>

## 2. 简答题

### 简答题 1

题干：比较 Hidden Terminal 和 Exposed Terminal，并说明 RTS/CTS 的作用边界。

<details class="self-test-answer">
<summary>参考答案</summary>

Hidden Terminal 是互相听不到的两个发送端同时干扰同一接收端，导致接收端碰撞；Exposed Terminal 是发送端听到了附近发送而过度退避，导致本可并发的通信被抑制。RTS/CTS 对 Hidden Terminal 更直接有效，因为隐藏节点可能听到接收端 CTS 并设置 NAV；但它有控制开销，对小包或低负载不一定划算。

</details>

### 简答题 2

题干：说明 WPA-PSK 离线字典攻击的步骤和防御。

<details class="self-test-answer">
<summary>参考答案</summary>

步骤：攻击者监听或诱导重连，捕获 4-way handshake；从字典猜测 passphrase；由 passphrase 和 SSID 派生 PMK，再由 nonce 和 MAC 派生 PTK；计算 MIC 与抓包比对，匹配则猜中。防御：使用长随机 PSK，避免常见词典；优先 WPA3/SAE；企业环境使用 802.1X/EAP/RADIUS；禁用 WEP、WPA/TKIP。

</details>

### 简答题 3

题干：解释 KRACK 为什么不是破解 AES 或 WiFi 密码。

<details class="self-test-answer">
<summary>参考答案</summary>

KRACK 利用的是 4-way handshake 中密钥安装状态处理问题。攻击者重放特定握手消息，诱导客户端重新安装已安装的密钥，并重置 nonce、PN 或 replay counter。它没有求出 PSK/PMK，也没有破解 AES 算法；风险来自 nonce 重用，可能导致部分流量被解密、重放或注入。修复重点是补丁和状态机：重复安装同一密钥时不能重置 nonce。

</details>

### 简答题 4

题干：按 IoT Security Demands 分析智能家居监控系统的攻击与防御。

<details class="self-test-answer">
<summary>参考答案</summary>

Access security：防默认口令、弱账号、非法设备接入，使用强认证、MFA、最小权限。Communication security：防 WiFi 嗅探、弱 PSK、BLE tracking、重放和 DoS，使用强 WPA2/WPA3、安全配对、加密、完整性和抗重放。Data privacy security：视频、音频、作息、设备清单和位置要最小采集、加密存储、脱敏和审计。Computing system security：云 API、App token、固件和 OTA 要做权限校验、签名更新、日志和异常检测。

</details>

### 简答题 5

题干：说明 RFID 防冲突为什么需要 ALOHA/FSA/Q Algorithm 这类机制。

<details class="self-test-answer">
<summary>参考答案</summary>

一个 reader 范围内可能同时有多个 tag，如果同时响应会碰撞，reader 无法区分。ALOHA/FSA 让 tag 在随机时隙响应，时隙结果分为空、成功和冲突。Q Algorithm 根据空时隙和冲突情况调整帧大小，使标签数量与时隙数更匹配，提高识别效率。答题可写：目标是避免多 tag 同时回复、提高 throughput、降低 starvation 和识别延迟。

</details>

### 简答题 6

题干：说明 Bluetooth/BLE tracking 的来源和防御。

<details class="self-test-answer">
<summary>参考答案</summary>

来源：固定 BD_ADDR、随机化不足、设备名、服务 UUID、manufacturer data、RSSI、广播间隔和连接行为都可能形成指纹。攻击者可在商场、家居或公共空间扫描并关联设备轨迹。防御：使用地址随机化，同时减少稳定 payload；隐藏敏感服务；GATT 访问授权；安全配对和 MITM 保护；禁用降级；应用层做最小采集和用户授权；需要时采用 BLE-Guardian 类机制控制发现和连接。

</details>
