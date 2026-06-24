---
title: "第四周：WPA 与 TKIP"
source: "materials/第四周WiFi Protected Access (WPA).pptx"
order: 4.2
---

# 第四周：WPA 与 TKIP

## 1. 本章速览

WPA 是 WEP 到 WPA2 之间的过渡方案。它保留 RC4 以兼容旧硬件，但通过 TKIP、Michael MIC、48-bit IV、序列检查、4-way handshake、802.1X/EAP 改善 WEP 的主要缺陷。考试重点是理解 WPA 解决了什么、仍然弱在哪里，以及 PSK 与 Enterprise 两种模式的差异。

## 2. WPA 的设计目标

- 比 WEP 强，且能通过软件/固件升级部署到旧 AP 和旧网卡。
- 成本低、部署快、兼容多厂商。
- 同时支持家庭/SOHO 的 PSK 模式和企业的 802.1X/RADIUS 模式。
- 在旧 RC4 硬件限制下尽量提高机密性、完整性和密钥管理能力。

## 3. TKIP 的四个关键改进

- **Michael MIC**：每包计算 64-bit MIC，保护数据和部分头部，提升消息完整性。
- **48-bit IV/TSC**：把 WEP 的 24-bit IV 扩展到 48-bit，大幅降低重复概率。
- **IV 序列规则**：单调递增计数器，丢弃乱序或重放包。
- **每包密钥混合**：不再简单拼接 `IV || key`，而是用两阶段 mixing 生成 per-packet key，降低 IV 和密钥关系泄露。

## 4. Michael MIC 与主动反制

- Michael 是为了旧硬件性能限制设计的，强度有限。
- WPA 因此采用主动反制：检测到 MIC 失败时触发保护措施，抑制攻击者反复试探。
- 要记住：Michael 是“过渡时代的折中”，不是强 MAC 的理想方案。

## 5. PMK、PTK 与 4-Way Handshake

- **PMK Pairwise Master Key**：主密钥。
  - PSK 模式中，PMK 来自 passphrase、SSID、SSID length、4096 次 PBKDF2，输出 256-bit。
  - Enterprise 模式中，PMK 来自 802.1X/EAP 认证结果。
- **PTK Pairwise Transient Key**：会话临时密钥，由 PMK、AP nonce、STA nonce、AP MAC、STA MAC 派生。
- **4-Way Handshake 作用**：
  - 双方证明持有 PMK。
  - 协商新鲜 PTK。
  - 安装加密和完整性密钥。
  - 分发/安装 GTK 等组密钥。

## 6. WPA-PSK

- 不需要 RADIUS 服务器，使用共享口令。
- 适合家庭和小型网络。
- 安全性高度依赖 passphrase 强度。
- 攻击者抓到 4-way handshake 后，可以离线字典攻击；SSID 也参与 PBKDF2，因此常见 SSID 可被预计算彩虹表利用。
- 防护建议：使用长、随机、非字典口令；避免常见 SSID；更高安全场景使用 Enterprise。

## 7. WPA Enterprise、802.1X 与 EAP

- **802.1X**：基于端口的网络访问控制，弥补 802.11 在访问控制、认证和密钥管理上的不足。
- **三类角色**：
  - Supplicant：客户端。
  - Authenticator：AP。
  - Authentication Server：通常是 RADIUS。
- **EAP**：认证消息承载框架，不是具体认证算法。EAP Request/Response/Success/Failure 承载具体方法如 EAP-TLS。
- **EAPoL**：在 LAN 上封装 EAP，用于客户端和 AP 之间。
- **RADIUS**：AP 和认证服务器之间传递认证消息和密钥材料。

## 8. WPA 的剩余问题

- TKIP 仍基于 RC4，不是长期理想方案。
- Michael MIC 强度有限。
- WPA-PSK 仍受离线字典攻击威胁。
- 支持 QoS 等特性的实现可能被 Beck-Tews 等攻击利用，恢复部分明文或注入短包。
- 因此 WPA 是迁移方案，最终应使用 WPA2/CCMP 或更高版本。

## 9. 考试重点

- 能说出 WPA/TKIP 相对 WEP 的改进：MIC、48-bit IV、序列检查、per-packet key mixing、4-way handshake。
- 能解释 PMK 和 PTK 的来源与关系。
- 能说明 4-way handshake 的作用，不只是“认证”，也是密钥确认和安装。
- 能比较 PSK 与 Enterprise：是否需要 RADIUS、密钥是否按用户/会话分发、攻击面差异。
- 能说明 WPA-PSK 离线字典攻击为什么可行。
- 能说明为什么 TKIP 只是过渡方案。

## 10. 易混点

- **EAP 不是认证方法本身**：它是承载 TLS、密码、证书等方法的框架。
- **AP 不一定理解 EAP 内部内容**：AP 通常代理 EAP，只关心成功或失败。
- **强 PBKDF2 不拯救弱密码**：短口令、字典词仍可被离线尝试。
- **WPA 不等于 WPA2**：WPA/TKIP 仍是 RC4；WPA2/CCMP 使用 AES。

## 11. 快速自测

1. WPA 为什么没有直接抛弃 RC4？
2. TKIP 的 per-packet key mixing 解决了 WEP 的什么问题？
3. PSK 如何派生 PMK？
4. 4-way handshake 需要哪些输入来派生 PTK？
5. 为什么 WPA-PSK 的攻击可以离线进行？
