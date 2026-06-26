---
title: "Lecture 14: NFC Application Security"
source: "materials/Lecture 14 NFC Application Security(1).pptx"
order: 14
---

# Lecture 14: NFC Application Security

## 零基础导读

NFC 是 13.56 MHz 的近距离通信，但短距离不是认证。一次 NFC 读卡可以按 ISO 14443 流程理解：PCD/reader 产生电磁场，PICC/card 从场中取能；reader 发 REQA，card 回 ATQA；防冲突阶段选出 UID，返回 SAK；如果需要更高层通信，reader 发 RATS，card 回 ATS，之后双方用 APDU 命令/响应交换应用数据。FWT/FWI/SFGI 这些参数决定 reader 等待响应的时间窗口，relay attack 就会利用过宽的等待和网络转发把远处的卡“接到”本地 reader。

NFC Forum Type 1/2/3/4 标签在容量、UID、访问控制和底层标准上不同，但 NFC 规范本身不会自动替你完成所有安全工作。普通标签可能被 cloning、modification、swapping/replacing；NDEF Signature RTD 能证明内容完整性和来源，但如果不绑定 UID、计数器、业务上下文或后端状态，签名内容仍可复制到另一张标签。真正的门禁、票务、支付要额外做 MAC、签名、密钥认证、后端校验和风控。

手机 NFC 安全还要区分 SE 和 HCE。SE/UICC/eSE 是隔离硬件或安全域，适合存支付 applet 和密钥，由 card manager、security domain、TSM、MNO、SP 等角色管理；HCE 由普通主机模拟卡，部署灵活但更依赖 OS、TEE、云端 tokenization 和风控。Google Wallet PIN 漏洞说明，把 4 位 PIN 的 hash 放在 `/data` 里，root 后可以离线枚举 10000 个 PIN；更合理的是把 PIN 验证和尝试计数放入 SE/TEE。

手机侧威胁还包括恶意或格式错误标签。malformed tag 可能触发 NFC 解析器、NDEF handler 或文件选择逻辑的崩溃，造成 DoS；NDEF URL、恶意文件、USSD 链接或深链可能诱导用户打开钓鱼站点、下载恶意应用或触发危险拨号指令。SE 侧如果 card manager 被错误锁定，用户可能无法安装、删除或更新 applet。安全执行要靠 sandbox/permission boundaries、隔离执行、secure storage、remote attestation、secure provisioning、迁移和 trusted path，确保密钥、PIN、applet 和交易确认不被普通 App 篡改。

## 本章知识地图

1. **一次读卡流程**：PCD 产生场 -> PICC 取能 -> REQA/ATQA -> anti-collision -> UID/SAK -> RATS/ATS -> APDU。
2. **NFC 三模式**：Reader/Writer 读写标签，Card Emulation 模拟卡，Peer-to-Peer 交换数据。
3. **Type 1/2/3/4**：容量、访问控制、底层协议不同；Type 2 常见简单标签，Type 4 更适合复杂安全应用。
4. **应用层安全**：NFC spec 不自动提供加密、reader 认证或后端校验；NDEF 签名也不等于绑定物理标签。
5. **移动支付风险**：SE/UICC/eSE、TSM/MNO/SP、HCE/TEE、APDU relay、FWT 超时、PIN 存储、malformed tag 和 USSD 链接都影响安全。
6. **票务/门禁设计**：不能只信 UID；应使用 Hash(UID + Master key)、OTP counter、MAC、lock bytes、后端数据库和 open payment 风控绑定真实业务状态。

## 初学者常见疑问

问：为什么 NFC 短距离仍会被 relay attack？

答：短距离只限制 PCD 和 PICC 的射频场距离。Relay attack 用一个设备靠近受害者卡/手机，另一个设备靠近 POS/门禁，中间通过网络转发 APDU。POS 以为卡就在旁边，卡也以为在和本地 reader 交互。只要 FWT 等待时间允许，短距离假设就被协议转发绕过。

问：NDEF 签名为什么不能完全防克隆？

答：NDEF 签名保护的是 NDEF 内容的完整性和来源。如果签名没有覆盖 UID、计数器、位置、时间或后端状态，攻击者可以把同一份签名内容复制到另一张可克隆标签上。验证者看到内容签名正确，但无法证明这就是原来的物理标签。

问：SE 和 HCE 怎么取舍？

答：SE 把密钥和 applet 放在隔离环境里，普通 App 不能随便读，适合支付、交通卡等高安全场景；缺点是部署涉及运营商、银行、TSM、设备厂商等角色。HCE 部署更灵活，可快速上线，但密钥保护更多依赖 TEE、云端 token、交易限额、风控和锁屏状态。

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

| 类型 | 底层协议/容量直觉 | 典型能力与例子 | 安全注意点 |
|---|---|---|---|
| Type 1 | 基于 Innovision/Jewel，容量小、可读写，速率通常 106 kbit/s | 简单标签、低成本海报 | 有 UID、OTP 和 lock bits，但低端标签容易被复制内容。 |
| Type 2 | 基于 ISO 14443A，常见容量几十到几百字节 | MIFARE Ultralight、NTAG | UID、OTP counter/OTP bytes、lock bits 常用于票务和防篡改，但可克隆卡会削弱 UID 信任。 |
| Type 3 | 基于 FeliCa，容量较大，212/424 kbit/s | 日本交通/电子钱包类应用 | 依赖系统码和服务访问控制，适合较复杂应用。 |
| Type 4 | 基于 ISO 14443A/B，使用 APDU，容量和安全能力更强 | DESFire、支付/门禁应用 | 可支持文件系统、认证、加密和 MAC，更适合高安全场景。 |

常见威胁：

- **Tag cloning**：复制标签内容或 UID，伪造签到、优惠、门禁凭据。
- **Modification**：修改标签数据，如替换 URL 或业务参数。
- **Swapping/Replacing**：把合法标签替换为恶意标签，诱导用户执行错误操作。
- 防护包括 MAC 绑定 UID、锁定可写页、使用 OTP/lock bits、后端校验。
- **应用例子**：UID-based access control 只检查 UID，部署简单但容易被可写 UID 卡克隆；更安全做法是 reader 把 UID、计数器和 MAC 交给 backend DB 校验，后端决定门禁或票务是否有效。

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
- **FWT 细节**：FWT 由 FWI 控制，典型值可记为 `FWI=0 ≈303μs`、`FWI=4 ≈4833μs`、`FWI=14 ≈4949ms`；`MIFARE DESFire default FWI=0x8` 对应约 77 ms。PPT 例子里 Nexus S/Jelly Bean 响应可能约 `430ms`，已经远超部分严格 FWT；现实中 `readers often ignore FWT configuration`，也就是很多 reader 不严格按卡声明的 FWT 超时，给 relay attack 留出空间。

## 8. 手机 NFC 与 Secure Element

- 手机 NFC 可用于读写、P2P、卡模拟。
- 安全敏感应用需要隔离执行、安全存储、安全部署、可信路径和应用迁移能力。
- **Secure Element SE**：如 SIM/UICC、嵌入式 SE，用于存放支付/交通 applet 和密钥，通过 card manager 和 application firewall 隔离。
- **Trusted Service Manager TSM**：协调银行、交通机构、运营商等服务提供方，把凭据安全部署到 SE。
- **Host Card Emulation HCE**：由主机 CPU 模拟卡，部署灵活，但安全更多依赖 OS、TEE、云端风控和应用设计。
- **SE vs HCE 答题角度**：SE 的优势是密钥隔离、抗恶意 App 和可实现尝试计数；HCE 的优势是部署灵活、无需运营商或硬件 SE 协调，但必须用 tokenization、云端风控、TEE/锁屏和交易限额补足风险。
- **手机端威胁**：malformed tag 可造成 NDEF 解析 DoS；NDEF URL、恶意文件、USSD 链接和深链可引导恶意软件下载、钓鱼或危险拨号；card manager lockout 会让安全域或 applet 无法维护。
- **安全执行需求**：sandbox/permission boundaries 限制普通 App 访问 NFC 和 SE；隔离执行与 secure storage 保护 PIN、token 和密钥；remote attestation 证明设备/应用处于可信状态；secure provisioning 负责把凭据安全写入 SE/HCE；迁移流程要防止旧设备和新设备同时持有有效凭据；trusted path 要保证用户看到并确认的是未被恶意 App 篡改的交易信息。

## 9. 票务、门禁与开放支付设计

- **门禁**：只依赖 UID-based access control 风险很高，因为 UID 可被可克隆卡复制。更稳妥的设计是 reader 读取 UID 和随机挑战响应，后端 backend DB 校验密钥派生结果、权限和撤销状态。
- **事件票务**：可把票据标识设计成 `Hash(UID + Master key)`，reader 不直接存明文主密钥；每次入场使用 OTP counter 或一次性状态，防止同一标签被复制后多次入场。
- **内存标签保护**：lock bytes 用于锁定关键页，MAC 用于保护票据字段完整性，后端数据库记录已使用/已撤销/异常位置。注意 lock bytes 只能防普通改写，不能防高级克隆卡。
- **公共交通 open payment**：open payment 指乘客直接使用银行卡/手机钱包进出站。角色包括乘客设备或卡、reader/闸机、收单方、卡组织、发卡行、交通运营方和风控后台；安全重点是离线限额、联机清算、tokenization、黑名单同步和异常交易追踪。
- **open payment ticketing flow**：乘客有 `travel account in SP cloud`，卡或手机中保存身份和凭据；进出站时 reader 读取票据身份并把 `ticket identity/travel info` 发给后端；后端计算行程和票价，再转给 SP 收款。`Transport Authority` 负责交通规则、票价、证据和争议处理，SP 负责账户、凭据和支付扣款；二者要能提供乘车证据、支付证据和凭据生命周期管理。

## 10. Google Wallet 漏洞案例

- PIN 用于解锁交易，但曾存储在手机 `/data` 目录的 SQLite 数据库中，形式是 64-bit salt + 单轮 SHA-256 hash。
- 攻击者偷到设备并 root 后，可读取数据库。
- 系统表面上只允许 `six PIN tries`，但 root 后提取 salted hash，攻击者可在设备外做 `offline guessing outside that counter`。因四位 PIN 只有 10,000 种，工具可离线暴力破解。
- 更好的设计：PIN 存储和验证放入 Secure Element，尝试计数器也放入 SE。
- 用户侧防护：不要 root、启用锁屏、关闭 ADB、及时更新补丁，但这些不能替代系统设计修复。

## 11. 移动支付 Relay 攻击

- 攻击者让受害者支付 app 解锁后，通过恶意 reader/应用把 APDU 转发到远处 POS。
- `contactless EMV relay` 的典型场景是一个设备贴近受害者口袋里的卡/手机，另一个设备在 faraway shop 的 POS 前付款，中间转发 EMV APDU。
- 若用代理 token 做 relay，`proxy token requires card emulation`，也就是攻击端靠近 POS 的设备必须能模拟一张卡和 POS 交互。
- `UID spoofing is not needed`，因为 EMV 支付协议不依赖 NFC tag UID 作为支付凭据，真正关键的是 APDU 中的支付应用数据和密码学响应。
- 限制：目标支付 app 通常需要解锁和 PIN；某些攻击需要 root 或绕过 SE API 签名认证。
- 防护：
  - POS 强制交易超时，利用网络中继延迟。
  - 使用位置/上下文检测可疑交易。
  - 不把支付 applet 暴露给不可信接触接口。
  - 在 SE/TEE 中保护凭据和 PIN。
- 更强的 relay 防护通常需要距离绑定或时间测距，但普通 NFC/EMV 系统受兼容性和响应时间限制，很难只靠“短距离”假设解决。

## 12. 考试重点

- 能列出 NFC 三种模式，并给出例子。
- 能解释 PCD/PICC、主动/被动设备、13.56 MHz、短距离的意义。
- 能说明标签克隆、修改、替换三类威胁。
- 能比较 Ultralight、Ultralight C、DESFire 的安全能力。
- 能说明 NDEF 签名能保护什么，不能保护什么。
- 能解释 relay attack 为什么能绕过短距离假设。
- 能说明 Secure Element、UICC、HCE、TSM 各自角色。
- 能复述 Google Wallet PIN 存储漏洞的根因和防护。
- 能说明 malformed tag、USSD、card manager lockout 等手机侧威胁，以及 secure provisioning、remote attestation、trusted path 等安全执行需求。
- 能解释为什么门禁/票务不能只信 UID，并能用 Hash(UID + Master key)、OTP counter、MAC、backend DB 说明改进方案。

## 13. 易混点

- **短距离不是强认证**：NFC 近距离降低风险，但不能证明“人在现场”。
- **签名内容不等于绑定物理标签**：如果签名不覆盖 UID，内容可被复制。
- **锁定位不等于不可克隆**：可克隆卡可能连 UID/锁定位一起伪造。
- **HCE 灵活但不天然等同 SE 安全**：密钥保护和风控需要额外设计。
- **open payment 不是“闸机离线信任银行卡号”**：它依赖卡组织、收单、发卡、交通运营方和后台风控协同。

## 14. 快速自测

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

## 公式与术语速查

| 英文/缩写 | 中文含义 | 初学者要会的解释 |
|---|---|---|
| NFC | Near Field Communication | 13.56 MHz 近距离通信，常用于标签、门禁、票务和支付。 |
| PCD / PICC | Proximity Coupling Device / Card | PCD 是 reader，PICC 是卡或标签。 |
| REQA / ATQA | Request A / Answer To Request A | ISO 14443A 初始寻卡请求和响应。 |
| SAK | Select Acknowledge | 防冲突选择后卡返回的选择确认，说明卡类型和后续能力。 |
| RATS / ATS | Request/Answer To Select | 进入更高层通信前的参数协商，之后可交换 APDU。 |
| APDU | Application Protocol Data Unit | 卡应用命令/响应数据单元，支付和门禁常用。 |
| FWT | Frame Waiting Time | reader 等待 card 响应的时间窗口，relay attack 会利用过宽等待。 |
| NDEF / RTD | NFC Data Exchange Format / Record Type Definition | NFC 数据封装格式和记录类型，如 URL、文本、签名。 |
| SE / UICC / eSE | 安全元件/SIM/嵌入式 SE | 隔离存放支付、交通 applet 和密钥。 |
| HCE | Host Card Emulation | 由手机主机模拟卡，部署灵活但更依赖 OS、TEE、云端 token 和风控。 |
| TSM / MNO / SP | Trusted Service Manager / Mobile Network Operator / Service Provider | 移动支付生态中的凭据发行、运营商和服务提供方角色。 |
| USSD | Unstructured Supplementary Service Data | 拨号服务代码，恶意 NDEF/URL 可能诱导危险拨号或跳转。 |

票务/门禁常用计算：

- UID 派生票据：`TicketID = Hash(UID + Master key)`，reader 不直接暴露主密钥。
- 一次性计数：`OTP counter` 每次使用递增或消耗，后端拒绝重复计数。
- MAC：对 `UID || counter || ticket data` 计算消息认证码，防止离线改票据字段。

PPT 细节补充：

- NFC 主动通信角色可写 `Initiator/Target`：Initiator 发起通信并产生场，Target 响应；在被动卡模式里 PCD/PICC 也是类似主从关系。
- 超时参数常一起考：`FWI/SFGI/FWT/fc`。`fc` 是 13.56 MHz 载波频率，FWI 决定 Frame Waiting Time，SFGI 决定 Start-up Frame Guard Time。
- FWT 公式：`FWT = (256 × 16 / fc) × 2^FWI`。当 `FWI=8 ≈77ms`，reader 等待窗口足够让部分 relay attack 通过网络转发 APDU。
- Type 2/Ultralight 内存字段常见缩写：`BCC/INT/LOCK0/LOCK1/BL`。BCC 是 UID 校验字节，INT/内部字段由厂商使用，LOCK0/LOCK1 是锁定位，BL 是 block lock/锁块相关字段。
- 安全载体包括 UICC/eSE，也可能是 `Secure MicroSD`；移动支付生态里 `OTA` 是 Over-The-Air 远程下发/更新，`ObC` 是 Over-the-Bluetooth/Over-the-Cloud 这类替代或补充通道的缩写语境。
- Google Wallet PIN 案例的弱点可写成 `SHA-256(salt || PIN)`：salt 阻止直接查通用表，但四位 PIN 空间只有 10000，root 后仍可离线穷举。
- NDEF Signature 只能证明内容未被改，不能自动证明物理标签没被复制；高安全场景要把 UID、counter、后端状态、时间/位置或 reader challenge 一起绑定。

## 历年卷风格练习

1. 说明一次 NFC 读卡从 REQA 到 APDU 的基本流程。
2. 为什么 NDEF Signature 不能完全防止标签克隆？
3. Relay attack 如何绕过 NFC 短距离假设？FWT 在其中有什么作用？
4. 一个活动票务系统只使用 UID-based access control，有什么风险？如何用 Hash(UID + Master key)、OTP counter、MAC 和 backend DB 改进？

<details class="self-test-answer">
<summary>参考答案</summary>

1. PCD 产生 13.56 MHz 场，PICC 取能；PCD 发 REQA，PICC 回 ATQA；防冲突阶段选择 UID 并返回 SAK；若需要 ISO 14443-4 通信，PCD 发 RATS，PICC 回 ATS；之后双方用 APDU 命令/响应交换应用数据。
2. NDEF Signature 保护 NDEF 内容完整性和来源，但如果签名不绑定 UID、计数器、时间、位置或后端状态，攻击者可把同一签名内容复制到另一张可克隆标签。
3. 攻击者让一个设备靠近受害者卡/手机，另一个设备靠近 POS/门禁，中间通过网络转发 APDU。NFC 射频仍是短距离，但协议链路被延长；若 FWT 等待时间足够宽，远程响应仍会被接受。
4. 只信 UID 容易被可写 UID 卡克隆。改进方案是用 `Hash(UID + Master key)` 派生票据标识，用 OTP counter 防重复使用，用 MAC 保护票据字段完整性，并让 backend DB 检查票据状态、撤销、使用次数和异常位置。

</details>
