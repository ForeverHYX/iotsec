---
title: "IoT Security 总复习索引"
source: "all materials"
order: 0
---

# IoT Security 总复习索引

## 1. 建议复习顺序

1. **安全基础**：先掌握 CIA、认证、授权、完整性、不可否认性、策略/机制、攻击者类型。
2. **无线基础**：理解衰落、干扰、复用、扩频、OFDM、双工和蜂窝网络。
3. **MAC 层**：掌握共享信道接入、碰撞、CSMA/CA、隐藏节点、RTS/CTS。
4. **蜂窝安全**：理解 LTE 空口控制面和 VoLTE 中密钥流/计数器错误带来的风险。
5. **Wi-Fi 安全三部曲**：按 WEP -> WPA -> WPA2 学，重点比较“设计目标、密钥管理、完整性、重放保护、攻击”。
6. **IoT 安全**：从四层架构和设备特性出发，分析通信、隐私、计算、感知安全。
7. **RFID/NFC/Bluetooth**：聚焦近场/短距协议的身份、隐私、低功耗和中继/克隆/追踪攻击。

## 2. 一张总图

- **安全目标**：机密性、完整性、可用性、认证、授权、隐私、不可否认、问责。
- **无线特殊性**：广播介质、共享频谱、移动性、多径、资源受限、物理干扰。
- **协议层风险**：
  - PHY：jamming、捕获效应、对抗样本、物理层指纹。
  - MAC：碰撞、隐藏节点、伪造管理帧、退避操纵。
  - Link：WEP/WPA/WPA2、Bluetooth pairing、NFC tag security。
  - Network/Core：蜂窝信令风暴、IoT botnet、云/边缘平台攻击。
  - Application：移动支付、语音助手、门禁、智能家居。

## 3. 高频考试对比题

- **认证 vs 授权 vs 访问控制**：认证确认身份；授权决定权限；访问控制执行权限。
- **加密 vs 完整性保护**：加密防窃听；MAC/签名防篡改和伪造。
- **CSMA/CD vs CSMA/CA**：有线可碰撞检测；无线更依赖退避和 ACK。
- **Hidden node vs Exposed node**：隐藏节点导致接收端碰撞；暴露节点导致不必要等待。
- **WEP vs WPA vs WPA2**：WEP/RC4/CRC/24-bit IV；WPA/RC4+TKIP/Michael/48-bit IV；WPA2/AES-CCMP/PN。
- **PSK vs Enterprise**：PSK 共享口令、易被离线字典攻击；Enterprise 使用 802.1X/RADIUS/EAP，按用户认证和分发密钥。
- **RFID vs NFC**：NFC 是短距高频 RFID 相关标准集合，更强调手机、卡模拟、P2P 和应用安全。
- **BLE 地址随机化 vs 隐私**：随机化减少跟踪，但 payload 和行为仍可能指纹化。
- **SE vs HCE**：SE 硬件隔离更强；HCE 部署灵活但依赖主机/云端保护。

## 4. 公式/机制必须会解释

- **流密码密钥流重用**：`C1=P1 XOR K`、`C2=P2 XOR K`，所以 `C1 XOR C2=P1 XOR P2`。
- **WEP seed**：`IV || shared key`，IV 明文且短，导致密钥流重用。
- **WPA/WPA2 PTK 派生输入**：PMK、ANonce、SNonce、AP MAC、STA MAC。
- **CCMP**：CTR 负责机密性，CBC-MAC 负责完整性，PN/nonce 防重放和密钥流重用。
- **ALOHA/FSA 时隙分类**：空时隙、单时隙、冲突时隙。
- **LPN/HB**：响应基于秘密向量和随机挑战的点积奇偶，并加入噪声提升学习难度。

## 5. 考前 30 分钟速刷清单

- 能否用一句话解释每种攻击的“利用点”？
- 能否区分协议设计缺陷、实现缺陷、配置缺陷和物理层限制？
- 能否给每个协议说出至少一个防御？
- 能否把一个 IoT 设备按四层架构分解并列出威胁？
- 能否解释为什么“短距离、跳频、签名、加密”都不是单独充分的安全保证？

## 6. 每章笔记

- Week 1: 安全基础与无线网络概览
- 第二周: 无线通信基础
- 第三周 Part 1: MAC 层
- 第三周 Part 2: 蜂窝网络安全
- 第四周: WEP
- 第四周: WPA
- 第四周: WPA2
- Week 7: IoT 与 IoT 安全
- Lecture 12: RFID Security and Privacy
- Lecture 13: Bluetooth Security and Privacy
- Lecture 14: NFC Application Security
- 历年卷回忆题与参考答案
- 模拟卷 A：历年卷风格练习
- 模拟卷 B：历年卷风格练习
- 模拟卷 C：选择题与简答题
- 模拟卷 D：选择题与简答题
