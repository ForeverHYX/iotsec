---
title: "模拟卷 B：历年卷风格练习"
source: "generated from past-exam style"
order: 101
---

# 模拟卷 B：历年卷风格练习

## 0. 使用说明

本卷与现有历年卷页面保持同一答题结构：20 道客观题、6 道简答题池、4 道综合大题。内容围绕同一批高频考点变换表述和场景，适合在模拟卷 A 之后继续自测。

## 1. 模拟卷 B：选择/填空式客观题

### 客观题 1

题干：licensed band 与 unlicensed band 的区别最准确的是哪一项？

选项：

- A. licensed band 受授权管理，unlicensed band 可被多类设备共享但更容易互相干扰
- B. unlicensed band 永远没有安全问题
- C. licensed band 不能用于蜂窝网络
- D. 两者只在纸面上存在，实际无线系统不用频谱

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：授权频段通常由运营商或机构管理，干扰更可控；免授权频段部署方便，但 WiFi、Bluetooth、ZigBee 等共享会带来拥塞和干扰。

</details>

### 客观题 2

题干：Shannon limit 在无线系统设计中说明了什么？

选项：

- A. 给定带宽和信噪比时，信道容量存在理论上限
- B. 加密后容量一定无限大
- C. CRC-32 可以提供认证
- D. 所有无线设备都不用考虑功率

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Shannon limit 是物理层上限，提醒我们不能只靠编码让速率无限提高；安全机制也必须承认带宽、噪声和能耗限制。

</details>

### 客观题 3

题干：near-far effect 指的是什么？

选项：

- A. 强近端信号可能淹没弱远端信号
- B. CRC 会自动变成 AES
- C. RFID tag 能无限远供电
- D. BLE 地址随机化一定失败

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：近端强信号和远端弱信号同时出现时，接收端可能难以解出弱信号。这是无线物理层与功率控制中的典型问题。

</details>

### 客观题 4

题干：Exposed Terminal 问题的核心后果是什么？

选项：

- A. 节点过度保守地等待，导致本可并发的传输被抑制
- B. WEP IV 太短
- C. RFID 标签被 kill
- D. 云端数据库自动备份

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Hidden Terminal 是“听不到别人导致碰撞”，Exposed Terminal 是“听到了别人却误以为不能发，降低空间复用”。

</details>

### 客观题 5

题干：Wireless LAN/WiFi 主要对应哪个 IEEE 标准族？

选项：

- A. IEEE 802.3
- B. IEEE 802.11
- C. IEEE 802.15.1 only
- D. ISO 14443 only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：B。

解析：WiFi 对应 IEEE 802.11。802.3 是以太网，802.15.1 与 Bluetooth 相关，ISO 14443 与近场卡流程相关。

</details>

### 客观题 6

题干：WEP shared key authentication 的漏洞本质是什么？

选项：

- A. 攻击者可通过明文挑战和加密挑战恢复 keystream，从而伪造认证响应
- B. 它使用了 AES-GCM
- C. 它要求每个用户使用 RADIUS
- D. 它完全阻止 rogue AP

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：共享密钥认证会暴露挑战明文和对应密文，攻击者可获得一段 keystream。知道 keystream 后不必知道 WEP key 也能应答类似挑战。

</details>

### 客观题 7

题干：FMS attack 主要利用 WEP/RC4 中的什么问题？

选项：

- A. weak IV 与 RC4 key scheduling 的相关性
- B. Bluetooth piconet 的 master 时钟
- C. IoT 四层模型
- D. NFC 的 FWT

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：FMS 利用 RC4 弱 IV/弱 key 相关性和已知明文头部，收集足够数据包后恢复 WEP key。

</details>

### 客观题 8

题干：WPA/WPA2-PSK 离线字典攻击通常需要攻击者先获得什么？

选项：

- A. 一次合法握手相关报文
- B. RFID tag 的颜色
- C. 所有 AP 的电源线
- D. NFC 手机钱包的发票

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：攻击者捕获 4-way handshake 后，可离线尝试候选口令，计算 PMK/PTK 并检查 MIC 是否匹配。弱 PSK 会被字典攻击击中。

</details>

### 客观题 9

题干：WPA/WPA2 Enterprise 与 PSK 的主要区别是什么？

选项：

- A. Enterprise 使用 802.1X/EAP/RADIUS 做按用户认证和密钥分发
- B. Enterprise 不需要认证
- C. PSK 自动给每个用户不同证书
- D. Enterprise 只能用于 RFID

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：PSK 是共享口令模式；Enterprise 借助 802.1X、EAP 和 RADIUS 做更细粒度的用户认证与密钥管理。

</details>

### 客观题 10

题干：KRACK 的直接利用点是什么？

选项：

- A. 重放 4-way handshake 中的特定消息，诱导客户端重装密钥并重置 nonce/PN
- B. 暴力破解 AES
- C. 让 RFID tag 进入 sleep
- D. 修改 BLE 广播名称

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：KRACK 是 key reinstallation attack。它不是破解密码，而是利用协议实现状态机对重传消息处理不当导致 nonce 重用。

</details>

### 客观题 11

题干：IoT Security Architecture 常按哪些部分组织防护？

选项：

- A. sensing security、transmission security、data security、application security
- B. only CRC、only IV、only RC4
- C. PCD、PICC、APDU、FWT
- D. master、slave、piconet、scatternet only

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Security Architecture 更像按层部署防护，区别于 Security Demands 按需求类别描述要保护的能力。

</details>

### 客观题 12

题干：Outsourced data privacy 的主要担忧是什么？

选项：

- A. 数据交给云或第三方处理后，用户对访问、使用和泄露风险的控制变弱
- B. 数据一上云就天然不可被访问
- C. 只影响 WEP 的 ICV
- D. 只影响物理天线方向

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：IoT 数据上云便于分析，也会带来访问控制、二次使用、泄露、越权和合规风险。

</details>

### 客观题 13

题干：无源 RFID tag 与 reader 通信通常依赖什么机制？

选项：

- A. Reader 供能，tag 通过 backscatter 调制反射信号
- B. Tag 自带大型基站
- C. 所有 tag 都用有线以太网
- D. Tag 直接运行 WPA2 4-way handshake

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：无源 RFID tag 没有主动电源，通常从 reader 电磁场取能，并用 backscatter 改变反射信号传回信息。

</details>

### 客观题 14

题干：RFID Q Algorithm 中 Q 值主要影响什么？

选项：

- A. 一轮防冲突帧中的时隙数量
- B. WEP 的 IV 长度
- C. Bluetooth 的 PIN 位数
- D. 云服务器的硬盘容量

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Q Algorithm 用 `2^Q` 之类的帧大小调节响应时隙，目标是在空时隙、成功时隙和碰撞时隙之间动态平衡。

</details>

### 客观题 15

题干：HB/HB+ 协议适合低成本 RFID 的关键原因是什么？

选项：

- A. 基于 LPN 思路，只需轻量级点积、异或和噪声，不依赖昂贵公钥运算
- B. 必须使用 RSA-4096
- C. 只能运行在云服务器
- D. 不需要任何随机性

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：HB/HB+ 的核心是轻量计算和学习带噪声奇偶问题。HB+ 引入 reader blinding 以抵抗主动攻击。

</details>

### 客观题 16

题干：Bluetooth Mode 3 与 Mode 2 的主要区别是什么？

选项：

- A. Mode 3 在链路建立前进行安全控制，Mode 2 在服务层做访问控制
- B. Mode 3 表示没有安全
- C. Mode 2 只能用于 WEP
- D. 二者都只描述 RFID 防冲突

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：经典蓝牙安全模式中，Mode 1 无安全，Mode 2 在 service level 实施安全，Mode 3 在 link level、连接建立前实施安全。

</details>

### 客观题 17

题干：Bluetooth/BLE downgrade attack 通常想达到什么效果？

选项：

- A. 诱导双方使用更弱的配对、安全模式或密钥参数
- B. 增加 RFID tag 的天线数量
- C. 修复所有漏洞
- D. 提高 WEP IV 到 128 bit

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：降级攻击的目标是让协议回退到较弱能力，例如弱配对、短 key、无 MITM 保护或旧安全模式。

</details>

### 客观题 18

题干：BLE-Guardian 的目标最接近哪一项？

选项：

- A. 隐藏 BLE 广播并控制连接授权，降低未授权发现和连接风险
- B. 让 WiFi 使用 CRC-32 加密
- C. 让 RFID tag 永远不响应 reader
- D. 让所有云数据公开

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：BLE-Guardian 关注 BLE 设备暴露在广告和连接阶段的隐私/安全问题，通过代理或授权机制减少未授权扫描和连接。

</details>

### 客观题 19

题干：Blue snarfing 指的是什么？

选项：

- A. 未授权从 Bluetooth 设备读取联系人、短信或文件等数据
- B. 合法用户正常播放音乐
- C. RFID 防冲突中的空时隙
- D. WEP 的 ICV 校验

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：Blue snarfing 是经典蓝牙攻击名，强调未授权获取设备数据；和 bluejacking 等概念要区分。

</details>

### 客观题 20

题干：智能家居 BLE 门锁最应避免下列哪种设计？

选项：

- A. 固定可追踪地址、弱 PIN、未授权 GATT 写入开锁特征
- B. 安全配对和访问授权
- C. 最小化广播信息
- D. 固件签名更新

<details class="self-test-answer">
<summary>参考答案</summary>

答案：A。

解析：固定地址会造成 tracking，弱 PIN 容易被猜测或降级，未授权 GATT 写入可能直接变成控制门锁的漏洞。

</details>

## 2. 简答题池

### 简答题 1

题干：解释 Exposed Terminal 与 Hidden Terminal 的区别，并说明 RTS/CTS 对二者的作用边界。

<details class="self-test-answer">
<summary>参考答案</summary>

- Hidden Terminal：两个发送端互相听不到，但都能干扰同一接收端，导致接收端碰撞。
- Exposed Terminal：发送端听到了附近传输，误以为自己不能发，但自己的接收端其实不会受干扰，导致空间复用下降。
- RTS/CTS 对 hidden terminal 有帮助，因为隐藏节点可听到接收端 CTS 并设置 NAV。
- 对 exposed terminal，RTS/CTS 有时能帮助判断是否真的会干扰，但也可能引入额外开销。
- 答题要强调：无线 carrier sensing 发生在发送端，碰撞和干扰影响往往体现在接收端。

</details>

### 简答题 2

题干：说明 WPA/WPA2-PSK 离线字典攻击的前提、步骤和防御。

<details class="self-test-answer">
<summary>参考答案</summary>

- 前提：攻击者能捕获一次 4-way handshake，用户使用弱 PSK。
- 步骤：
  1. 监听或诱导重连，获得 ANonce、SNonce、AP/STA MAC 和 MIC。
  2. 从字典中猜测 passphrase。
  3. 由 passphrase 和 SSID 派生 PMK，再派生 PTK。
  4. 计算 MIC 并与抓包中的 MIC 比对。
  5. 匹配则说明口令猜中。
- 防御：使用长且随机的 PSK，避免可猜词典；优先 WPA3/SAE；企业环境使用 802.1X/EAP/RADIUS；禁用 WEP/WPA/TKIP。

</details>

### 简答题 3

题干：阐述 IoT Security Architecture 的四类防护，并各举一个例子。

<details class="self-test-answer">
<summary>参考答案</summary>

- Sensing security：保护传感器、RFID、摄像头、麦克风等，例子是防伪造节点、物理防篡改、传感数据校验。
- Transmission security：保护网络传输，例子是加密、完整性、认证、抗重放、抗 DoS。
- Data security：保护存储和处理的数据，例子是加密存储、访问控制、脱敏、备份、审计。
- Application security：保护业务逻辑和用户操作，例子是权限校验、输入验证、日志审计、异常检测、安全更新。
- 横向能力：security control、security audit、privacy/security。

</details>

### 简答题 4

题干：为什么 HB/HB+ 适合低成本 RFID？HB+ 相比 HB 改进了什么？

<details class="self-test-answer">
<summary>参考答案</summary>

- 低成本原因：tag 只需点积、异或和简单随机/噪声操作，不需要昂贵公钥算法。
- 安全基础：Learning Parity with Noise，攻击者看到带噪声响应后难以学习秘密向量。
- HB 的风险：面对主动攻击者时，攻击者可构造挑战收集信息。
- HB+ 改进：reader 和 tag 共同参与，增加 blinding secret，使主动攻击更难。
- 局限：需要参数、噪声率和轮数设计平衡安全性、误拒率和通信开销。

</details>

### 简答题 5

题干：比较 Bluetooth Mode 1、Mode 2、Mode 3，并说明 Classic Bluetooth 的物理/拓扑特征。

<details class="self-test-answer">
<summary>参考答案</summary>

- Mode 1：无安全机制。
- Mode 2：service level security，连接建立后按服务做认证、授权或加密。
- Mode 3：link level security，连接建立前先做认证/加密等控制。
- Classic Bluetooth：2.4 GHz ISM，TDMA-TDD slow frequency hopping。
- Piconet：一个 master、多个 slave，同步到 master clock 和 hopping sequence。
- Scatternet：多个 piconet 通过节点参与多个网络形成更复杂拓扑。

</details>

### 简答题 6

题干：智能家居监控系统使用 WiFi 摄像头、BLE 传感器和云 App。攻击者能获得哪些隐私？如何防御？

<details class="self-test-answer">
<summary>参考答案</summary>

- WiFi 攻击：弱 PSK 离线字典、evil twin、deauth、jamming、默认口令和固件漏洞。
- BLE 攻击：广播追踪、固定地址、服务 UUID 指纹、弱配对、未授权 GATT 读写。
- 云/App 攻击：token 泄露、越权 API、弱密码、日志泄露、未签名 OTA。
- 隐私：视频/音频、是否在家、开关门时间、家庭成员作息、访客、设备清单、位置和账号信息。
- 防御：强 WPA2/WPA3、网络隔离、BLE 地址随机化和安全配对、最小服务暴露、端到端加密、固件签名、最小权限、日志审计和异常检测。

</details>

## 3. 综合大题

### 大题 1

题干：某办公室仍使用 WEP 保护老旧 WiFi 设备。请完整说明 WEP 加密/解密流程，并分析攻击者如何利用 IV 重用、CRC-32 和弱 IV 发起攻击。

<details class="self-test-answer">
<summary>参考答案</summary>

流程：

- 发送端对 message 算 CRC-32，得到 ICV。
- 拼接 `IV || shared key` 输入 RC4，生成 keystream。
- `message || ICV` 与 keystream XOR 得到 ciphertext。
- IV 明文附在密文前发送。
- 接收端取 IV，用同样 key 生成 keystream，XOR 解密并校验 CRC。

漏洞：

- 24-bit IV 空间太小，随机或顺序使用都容易重复。
- 同一 IV 和 key 生成同一 keystream，导致 `C1 XOR C2 = P1 XOR P2`。
- CRC-32 无密钥且线性，可被修改密文时同步修正。
- 弱 IV 与 RC4 KSA 相关，FMS 可收集数据包恢复 key。
- 共享密钥认证泄露明文挑战和密文挑战，可恢复 keystream。
- 缺少密钥管理和管理帧认证，导致长期共享密钥、rogue AP 和 deauth 风险。

</details>

### 大题 2

题干：一个智能门锁使用 BLE 门锁、手机 App、WiFi 网关和云平台。请从 BLE、WiFi、云/App 三个角度分析攻击措施、隐私泄露和防御。

<details class="self-test-answer">
<summary>参考答案</summary>

BLE：

- 攻击：固定地址 tracking、设备名/UUID 指纹、弱 PIN、配对降级、MITM、未授权 GATT 写入。
- 防御：地址随机化、安全配对、MITM 保护、最小广播 payload、GATT 授权、BLE-Guardian 类保护。

WiFi：

- 攻击：抓握手离线字典、evil twin、deauth、jamming、弱路由器口令。
- 防御：强 WPA2/WPA3、禁用 WEP/TKIP、管理帧保护、访客/IoT 网络隔离。

云/App：

- 攻击：弱密码、token 泄露、越权 API、日志泄露、未签名 OTA、固件逆向。
- 防御：多因素认证、最小权限、端到端加密、固件签名、审计和异常检测。

隐私：开门时间、住户作息、访客、手机标识、地理位置、账号 token 和家庭设备清单。

</details>

### 大题 3

题干：请比较 IoT Security Demands 和 IoT Security Architecture，并用一个智慧工厂场景说明如何把二者结合起来答题。

<details class="self-test-answer">
<summary>参考答案</summary>

比较：

- Security Demands 是需求视角：access、communication、data privacy、computing system security。
- Security Architecture 是结构视角：sensing、transmission、data、application security。
- 二者不是互斥关系，而是一个说“要保护什么”，一个说“在哪些层实现保护”。

智慧工厂例子：

- 感知层：RFID、传感器、摄像头和工业控制器，要做设备认证、防假数据注入和物理防篡改。
- 传输层：WiFi/有线/蜂窝上传生产数据，要做加密、完整性、抗重放、抗 DoS 和网络隔离。
- 数据层：生产配方、库存、设备状态和人员位置，要做访问控制、脱敏、备份和审计。
- 应用层：调度系统、告警系统和远程维护，要防越权、弱口令、日志泄露和未签名更新。
- 最后回扣 demands：这些措施分别满足 access、communication、privacy 和 computing system security。

</details>

### 大题 4

题干：某商场使用 Bluetooth beacon 和 BLE 会员设备做室内服务。请分析 Bluetooth/BLE 的安全目标、可能攻击、隐私风险和防御措施。

<details class="self-test-answer">
<summary>参考答案</summary>

安全目标：

- Authentication：确认设备或用户身份。
- Confidentiality：保护链路或业务数据不被窃听。
- Authorization：限制服务和特征访问权限。

可能攻击：

- 广播扫描、地址跟踪、RSSI 轨迹分析、设备名/UUID/manufacturer data 指纹。
- 弱配对、MITM、downgrade、replay、未授权 GATT 读写。
- Classic Bluetooth 中还可提 sniffing、blue snarfing、服务级访问控制不足。

隐私：

- 用户到店时间、路线、停留区域、会员身份、设备型号和消费偏好。

防御：

- 地址随机化但同时最小化 payload。
- 安全配对、强随机数、最小密钥长度、禁止降级。
- GATT 服务按需开放并做授权。
- 使用 BLE-Guardian 类授权连接/隐藏广播机制。
- App 和云端做最小采集、透明授权、日志审计和数据删除。

</details>
