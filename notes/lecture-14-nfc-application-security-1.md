---
title: "Lecture 14: NFC Application Security"
source: "materials/Lecture 14 NFC Application Security(1).pptx"
order: 14
---

# Lecture 14: NFC Application Security

## 1. 本章速览

NFC 是短距离高频 RFID 数据交换标准，工作在 13.56 MHz，典型距离 4-10 cm。NFC 常用于读写标签、卡模拟、点对点通信、门禁、票务和移动支付。本章重点是 NFC 模式、标签安全、NDEF 签名、Secure Element/HCE、Google Wallet PIN 漏洞和 relay attack。

## 2. NFC 基础

- 标准：ISO 14443、ISO 15693、ISO 18092 等。
- 频率：13.56 MHz。
- 距离：通常 4 cm 到 10 cm。
- 速率：106/212/424 kbit/s 等。
- 主动设备 PCD/reader 连接电源，产生电磁场。
- 被动设备 PICC/tag 从 reader 场中取能并通信。

## 3. NFC 三种模式

- **Reader/Writer Mode**：手机或读写器作为主动设备，读取/修改被动标签，如读取智能海报。
- **Card Emulation Mode**：手机模拟被动卡，与外部 reader 交互，如交通卡、支付卡。
- **Peer-to-Peer Mode**：两个主动 NFC 设备交换数据。

## 4. NFC Forum 标签与内存标签威胁

标签类型包括 Type 1/2/3/4，差异体现在 UID、容量、访问控制和兼容标准。

常见威胁：

- **Tag cloning**：复制标签内容或 UID，伪造签到、优惠、门禁凭据。
- **Modification**：修改标签数据，如替换 URL 或业务参数。
- **Swapping/Replacing**：把合法标签替换为恶意标签，诱导用户执行错误操作。
- 防护包括 MAC 绑定 UID、锁定可写页、使用 OTP/lock bits、后端校验。

## 5. MIFARE Ultralight / Ultralight C / DESFire

- **MIFARE Ultralight**：
  - 有 UID、OTP bytes、lock bytes。
  - OTP 位只能从 0 置 1，不能重置。
  - lock page/block lock 可防止修改。
  - 但存在可克隆卡，可重写 UID、OTP、lock bytes。
- **Ultralight C**：
  - 类似 Ultralight，容量更大。
  - 支持 one-way counter 和基于密钥的访问控制。
  - 使用 Triple-DES 认证。
- **DESFire**：
  - 支持 Triple-DES/AES 互认证，适合更高安全应用。

## 6. NDEF 与签名

- **NDEF NFC Data Exchange Format**：NFC 数据封装格式，一个 NDEF Message 包含多个 NDEF Record。
- NDEF Signature RTD 可提供完整性和真实性。
- 签名算法示例包括 RSA/SHA-1、ECDSA/SHA-1 等。
- 重要限制：签名保护内容，但不一定覆盖卡 UID，因此不能防止“把同一签名内容复制到另一张卡”的克隆。
- 因此高安全场景应把 UID、应用上下文、计数器或后端状态一并纳入校验。只验证 NDEF 内容签名，最多说明内容没改，不说明“这张物理卡就是原卡”。

## 7. Relay Attack

- 中继攻击把远处的合法卡/手机和 reader 通过攻击者设备连接起来。
- “Mole reader” 靠近受害者 NFC 设备，攻击者手机靠近 POS/门禁终端，APDU 通过网络转发。
- NFC 的短距离不能阻止 relay，因为攻击者延长的是协议链路，而不是让物理 NFC 信号传很远。
- FWT Frame Waiting Time 决定 reader 等待响应的时间窗口；过宽的超时让中继更容易。

## 8. 手机 NFC 与 Secure Element

- 手机 NFC 可用于读写、P2P、卡模拟。
- 安全敏感应用需要隔离执行、安全存储、安全部署、可信路径和应用迁移能力。
- **Secure Element SE**：如 SIM/UICC、嵌入式 SE，用于存放支付/交通 applet 和密钥，通过 card manager 和 application firewall 隔离。
- **Trusted Service Manager TSM**：协调银行、交通机构、运营商等服务提供方，把凭据安全部署到 SE。
- **Host Card Emulation HCE**：由主机 CPU 模拟卡，部署灵活，但安全更多依赖 OS、TEE、云端风控和应用设计。
- **SE vs HCE 答题角度**：SE 的优势是密钥隔离、抗恶意 App 和可实现尝试计数；HCE 的优势是部署灵活、无需运营商或硬件 SE 协调，但必须用 tokenization、云端风控、TEE/锁屏和交易限额补足风险。

## 9. Google Wallet 漏洞案例

- PIN 用于解锁交易，但曾存储在手机 `/data` 目录的 SQLite 数据库中，形式是 64-bit salt + 单轮 SHA-256 hash。
- 攻击者偷到设备并 root 后，可读取数据库。
- 因四位 PIN 只有 10,000 种，工具可离线暴力破解。
- 更好的设计：PIN 存储和验证放入 Secure Element，尝试计数器也放入 SE。
- 用户侧防护：不要 root、启用锁屏、关闭 ADB、及时更新补丁，但这些不能替代系统设计修复。

## 10. 移动支付 Relay 攻击

- 攻击者让受害者支付 app 解锁后，通过恶意 reader/应用把 APDU 转发到远处 POS。
- 限制：目标支付 app 通常需要解锁和 PIN；某些攻击需要 root 或绕过 SE API 签名认证。
- 防护：
  - POS 强制交易超时，利用网络中继延迟。
  - 使用位置/上下文检测可疑交易。
  - 不把支付 applet 暴露给不可信接触接口。
  - 在 SE/TEE 中保护凭据和 PIN。
- 更强的 relay 防护通常需要距离绑定或时间测距，但普通 NFC/EMV 系统受兼容性和响应时间限制，很难只靠“短距离”假设解决。

## 11. 考试重点

- 能列出 NFC 三种模式，并给出例子。
- 能解释 PCD/PICC、主动/被动设备、13.56 MHz、短距离的意义。
- 能说明标签克隆、修改、替换三类威胁。
- 能比较 Ultralight、Ultralight C、DESFire 的安全能力。
- 能说明 NDEF 签名能保护什么，不能保护什么。
- 能解释 relay attack 为什么能绕过短距离假设。
- 能说明 Secure Element、UICC、HCE、TSM 各自角色。
- 能复述 Google Wallet PIN 存储漏洞的根因和防护。

## 12. 易混点

- **短距离不是强认证**：NFC 近距离降低风险，但不能证明“人在现场”。
- **签名内容不等于绑定物理标签**：如果签名不覆盖 UID，内容可被复制。
- **锁定位不等于不可克隆**：可克隆卡可能连 UID/锁定位一起伪造。
- **HCE 灵活但不天然等同 SE 安全**：密钥保护和风控需要额外设计。

## 13. 快速自测

1. Reader/Writer、Card Emulation、P2P 三种 NFC 模式分别适合什么应用？
2. 为什么 NDEF 签名不能完全防止标签克隆？
3. Relay attack 如何绕过 NFC 的短距离限制？
4. Google Wallet PIN 漏洞为什么四位 PIN 很快能被破解？
5. Secure Element 相比把凭据放在普通应用数据库里有什么优势？

<details class="self-test-answer">
<summary>参考答案</summary>

1. Reader/Writer 适合手机读海报或写标签；Card Emulation 适合手机模拟门禁、交通卡、支付卡；P2P 适合两个主动设备交换小数据。
2. 签名通常保护 NDEF 内容完整性和来源，但如果不绑定 UID 或物理卡特征，攻击者可把同一签名内容复制到另一张可克隆标签。
3. 攻击者把受害者附近的 NFC 设备和远处 POS/门禁通过网络转发 APDU，延长的是协议通信路径，而不是让 NFC 射频本身传远。
4. 四位 PIN 只有 10000 种；若数据库中只有 salt + 单轮 SHA-256 hash，攻击者 root 后可离线枚举所有 PIN，很快找到匹配值。
5. SE 提供隔离存储和受控执行，密钥不直接暴露给普通 App 或文件系统，还能实现 PIN 尝试计数、应用防火墙和更强的交易授权。

</details>
