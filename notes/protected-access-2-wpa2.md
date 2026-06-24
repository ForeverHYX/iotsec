---
title: "第四周：WPA2、CCMP 与 KRACK"
source: "materials/第四周Protected Access 2 (WPA2).pptx"
order: 4.3
---

# 第四周：WPA2、CCMP 与 KRACK

## 1. 本章速览

WPA2 基于 IEEE 802.11i，正式形态是 RSN，核心提升是使用 AES-CCMP 替代 WPA/TKIP 的 RC4。考试重点是 WPA2 四个阶段、4-way handshake、PMK/PTK/KCK/KEK/TK 的层级、CCMP 如何同时提供机密性与完整性，以及 KRACK 为什么能在密码算法安全的情况下破坏实现安全。

## 2. WPA2 基本结构

- **Personal 模式**：使用 PSK，不需要单独认证服务器。
- **Enterprise 模式**：使用 802.1X/EAP 和认证服务器，对用户进行单独认证。
- **四个阶段**：
  1. 发现与协商安全能力。
  2. 认证并生成主密钥。
  3. 通过 4-way handshake 生成并安装临时密钥。
  4. 使用 CCMP 提供数据机密性、完整性和重放保护。

## 3. Phase 1：Discovery

- AP 通过 Beacon 和 Probe Response 发布 RSN IE。
- RSN IE 告诉 STA 支持的认证与密钥管理套件、pairwise cipher、group cipher 等能力。
- STA 在 Association Request 中选择匹配能力。
- Open System Authentication 只是为了兼容 802.11 状态机，本身不提供安全性。

## 4. Phase 2：Authentication

- Enterprise 模式中，STA、AP、Authentication Server 通过 EAP/802.1X 完成认证。
- 认证成功后，客户端与认证服务器获得主密钥材料。
- AS 把 PMK 分发给 AP。
- PSK 模式中，PMK 直接由预共享密钥派生。

## 5. Phase 3：Key Management 与 4-Way Handshake

4-way handshake 的目标：

- 确认客户端和 AP 都持有正确 PMK。
- 用 PMK、ANonce、SNonce、双方 MAC 地址派生 PTK。
- 安装 pairwise 加密与完整性密钥。
- 把 GTK 和 GTK 序号安全传给客户端。
- 确认协商的 cipher suite。

PTK 进一步拆分为：

- **KCK**：计算 EAPOL-Key 消息 MIC。
- **KEK**：加密 Key Data，如 GTK。
- **TK**：加密/解密单播数据帧。

## 6. Phase 4：CCMP

- **AES-CCMP** = Counter Mode + CBC-MAC Protocol。
- **CTR 模式**：用 AES 加密递增 counter 生成密钥流，再与明文 XOR，提供机密性。
- **CBC-MAC**：对数据块链式计算消息认证码，提供完整性。
- **48-bit Packet Number PN**：用于重放保护，并参与构造 nonce，保证每包新鲜性。
- CCMP 保护帧体和大部分 MAC 头，降低攻击者利用头部字段的能力。

## 7. WPA/WPA2/WEP 对比

- WEP：RC4，24-bit IV，CRC-32，缺少密钥管理，已废弃。
- WPA：RC4 + TKIP，Michael MIC，48-bit IV，4-way handshake，是过渡方案。
- WPA2：AES-CCMP，RSN，强完整性和重放保护，是长期替代方案。

## 8. WPA2 的限制

- 无法防止纯物理层攻击，如 RF jamming。
- 控制和管理帧历史上保护不足，可导致 DoS、MAC spoofing、大规模 deauthentication。
- 安全证明通常针对抽象协议或单独密码组件，真实系统组合和实现仍可能出错。

## 9. KRACK：Key Reinstallation Attack

- KRACK 利用 4-way handshake 中重传与密钥安装逻辑的漏洞。
- 当攻击者阻断 Msg4 时，AP 可能重传 Msg3；客户端收到重传 Msg3 后重新安装已经安装过的 PTK。
- **关键后果**：重新安装 PTK 会把 nonce/packet number 重置为初始值，导致 nonce 重用。
- 对 CTR 类加密来说，nonce 重用会导致密钥流重用，进而泄露明文或允许重放/注入，具体影响取决于加密协议和实现。
- KRACK 说明：即使 4-way handshake 有安全证明、AES-CCMP 本身安全，组合实现仍可能出问题。

## 10. 考试重点

- 能列出 WPA2 四个阶段并说明每阶段目的。
- 能解释 RSN IE、Association Request 在安全能力协商中的作用。
- 能说明 PMK、PTK、KCK、KEK、TK、GTK 的关系。
- 能解释 CCMP 中 CTR 和 CBC-MAC 分别提供什么。
- 能说明 PN/nonce 的安全意义。
- 能描述 KRACK 的触发条件：Msg3 重传、客户端重复安装 PTK、nonce 重置。
- 能解释“形式化证明不等于实现安全”。

## 11. 易混点

- **Open System Authentication 不提供安全**：真正认证发生在 802.1X/EAP 或 PSK/4-way handshake 阶段。
- **PMK 不是直接加密数据的密钥**：它用于派生 PTK，PTK 再拆出 TK 等实际用途密钥。
- **KRACK 不是破解 AES**：它利用 nonce/key 安装逻辑错误。
- **Enterprise 也可能受 KRACK 影响**：问题在 4-way handshake 实现，不只在 PSK 密码强度。

## 12. 快速自测

1. WPA2 的 Personal 和 Enterprise 模式差异是什么？
2. 4-way handshake 为什么需要 ANonce 和 SNonce？
3. KCK、KEK、TK 各自用途是什么？
4. CCMP 如何同时保护机密性和完整性？
5. KRACK 为什么能绕过“算法本身安全”的保证？
