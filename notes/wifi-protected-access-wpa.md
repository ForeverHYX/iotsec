---
title: "第四周：WPA 与 TKIP"
source: "materials/第四周WiFi Protected Access (WPA).pptx"
order: 4.2
---

# 第四周：WPA 与 TKIP

## 零基础导读

WPA 是一个过渡方案：它要修补 WEP，但又不能要求所有旧 AP 和网卡立即换硬件，所以保留 RC4，外面套上 TKIP。理解 WPA 时要把它看成“逐项修补 WEP”：WEP 的 IV 太短，TKIP 改成 48-bit TSC；WEP 简单 `IV || key`，TKIP 做 per-packet key mixing；WEP 的 CRC-32 不是 MAC，TKIP 加 Michael MIC；WEP 没有可靠重放保护，TKIP 用序列规则丢弃旧包；WEP 长期共享一个 key，WPA 引入 4-way handshake 和 rekey。

TKIP 加密一帧的顺序可以这样想：先拿到 payload 和部分头部信息，用 Michael 算 MIC；把 payload、MIC 和 ICV 组合；用 TSC、发送方地址和临时密钥做两阶段 key mixing，得到本包 RC4 key；RC4 生成 keystream 后 XOR；最后把必要的 IV/TSC 信息随帧发送。Michael 是为了旧硬件设计的折中，强度有限，所以 WPA 还设置 MIC failure countermeasures，避免攻击者无限试错。

WPA 的密钥来自 PMK 和 PTK。PSK 模式中，passphrase、SSID、SSID length 经 4096 次 PBKDF2 得到 PMK；Enterprise 模式中，Supplicant 和 Authentication Server 通过 802.1X/EAP 认证后得到 PMK，AP 通过 RADIUS 拿到密钥材料。4-way handshake 用 ANonce、SNonce、AP MAC、STA MAC 和 PMK 派生 PTK，并用 EAPOL-Key MIC 证明双方知道 PMK。WPA/TKIP 典型 key size 是 128 bits，Michael 8 bytes。攻击者抓到握手后能离线猜 passphrase：本地枚举候选密码，派生 PTK，验证 MIC 是否匹配。Beck-Tews 则说明 TKIP 仍有结构性弱点，QoS 的多个 TSC 通道可被利用来绕过部分反重放限制。

## 本章知识地图

1. **WPA 修 WEP**：48-bit TSC、per-packet key mixing、Michael MIC、sequence check、4-way handshake、rekey。
2. **TKIP 加密一帧**：payload/头部 -> Michael MIC -> payload+MIC+ICV -> key mixing -> RC4 -> ciphertext。
3. **4-Way Handshake**：Msg1 给 ANonce，Msg2 给 SNonce+MIC，Msg3 发 GTK/Key Data，Msg4 确认安装。
4. **PSK 攻击路径**：抓 EAPOL 握手 -> dictionary/brute force/rainbow table 枚举 passphrase -> PBKDF2 得 PMK -> 验证 MIC。
5. **Enterprise 消息路径**：EAPOL 在客户端和 AP 之间，RADIUS 在 AP 和认证服务器之间；AP 多数时候代理 EAP，认证成功后拿 PMK。

## 初学者常见疑问

问：MIC、MAC、CRC 为什么容易混？

答：CRC 是无密钥错误检测码，主要防随机传输错误。MAC 是 Message Authentication Code，依赖秘密密钥，目标是防恶意篡改和伪造。Michael MIC 是 WPA/TKIP 中的一种轻量消息完整性机制，名字里有 MIC，但强度不如现代 HMAC/CBC-MAC；它是旧硬件限制下的折中。

问：为什么 WPA-PSK 是离线攻击？

答：攻击者只要抓到一次 4-way handshake，就有 ANonce、SNonce、双方 MAC 和 EAPOL-Key MIC。之后不需要再问 AP，可以在本地试密码：候选 passphrase + SSID 经 PBKDF2 得 PMK，再派生 PTK，再算 MIC，看是否等于抓到的 MIC。弱密码、常见 SSID 和预计算 rainbow table 都会降低安全性。

问：Beck-Tews 攻击说明了什么？

答：它不是把 WPA 完全打回 WEP，而是说明 TKIP 是补丁式过渡协议。PPT 中关键点是 QoS 有多个独立 TSC 通道，攻击者可利用较小计数器通道绕过部分反重放，并受 Michael 失败反制限速。结论是：TKIP 仍基于 RC4 和弱 MIC，不应作为长期安全方案。

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
- **PTK 派生为什么要放入双方 nonce 和 MAC**：nonce 提供新鲜性，MAC 地址把密钥绑定到这对 AP/STA，避免不同会话或不同设备组合意外得到相同临时密钥。
- **握手被抓包为什么足够离线攻击 PSK**：攻击者有 ANonce、SNonce、双方 MAC 和 MIC 后，可以在本地枚举 passphrase 派生 PMK/PTK，再验证 MIC 是否匹配，不需要继续和 AP 交互。

## 6. WPA-PSK

- 不需要 RADIUS 服务器，使用共享口令。
- 适合家庭和小型网络。
- 安全性高度依赖 passphrase 强度。
- 攻击者抓到 4-way handshake 后，可以离线字典攻击；SSID 也参与 PBKDF2，因此常见 SSID 可被预计算彩虹表利用。
- 防护建议：使用长、随机、非字典口令；避免常见 SSID；更高安全场景使用 Enterprise。
- **brute force、dictionary、rainbow table 区别**：brute force 是枚举所有可能字符串，8 字符随机口令按 PPT 估计可能需要约 630 年，12 字符会更久；dictionary attack 只试常见词、姓名、手机号和变形，现实中更有效；rainbow table 是提前为常见 SSID 和常见口令预计算 PMK，抓到握手后查表更快。结论是强随机长口令能抵抗离线攻击，弱口令会被快速筛出。

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
- **Beck-Tews 补充**：802.11e QoS 可有 8 QoS channels，每个通道维护自己的 TSC/序列空间。攻击者可尝试把短包转到计数器较小的通道绕过部分反重放限制；Michael countermeasures 通常限制为约 2 MIC failures/min，降低了试错速度，但也说明 TKIP 需要额外反制来弥补 MIC 强度不足。

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

<details class="self-test-answer">
<summary>参考答案</summary>

1. WPA 是过渡方案，需要兼容大量只能硬件加速 RC4 的旧 AP 和网卡，因此用 TKIP 在 RC4 基础上修补 IV、完整性和密钥管理。
2. 它避免像 WEP 那样简单使用 `IV || key`，而是为每个包混合出不同 key，降低 IV 与长期密钥关系泄露和密钥流重用风险。
3. 在 PSK 模式中，passphrase、SSID、SSID 长度经过 4096 次 PBKDF2 派生出 256-bit PMK。
4. 输入包括 PMK、ANonce、SNonce、AP MAC 地址和 STA MAC 地址，由此派生 PTK。
5. 抓到 4-way handshake 后，攻击者可本地尝试候选口令并计算 MIC 验证是否正确，不需要在线登录，因此弱口令会被字典攻击。

</details>
