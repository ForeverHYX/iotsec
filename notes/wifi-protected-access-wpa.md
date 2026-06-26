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

PPT 对 IV sequence enforcement 的细节是：WPA 使用 `16-bit monotonically incrementing counter` 抑制重放，规则包括取旧 IV 的 `1st and 3rd bytes of the old IV`，rekey 时 `reset packet sequence to 0`，每包 `increment by 1 per packet`，并 `drop out-of-sequence packets`。

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

## 公式与术语速查

| 英文/缩写 | 中文含义 | 初学者要会的解释 |
|---|---|---|
| WPA | Wi-Fi Protected Access | WEP 到 WPA2 之间的过渡安全方案，核心是 TKIP。 |
| TKIP | Temporal Key Integrity Protocol | 临时密钥完整性协议，用 48-bit TSC、per-packet key mixing、Michael MIC 修补 WEP。 |
| TSC | TKIP Sequence Counter | TKIP 序列计数器，防止重放；QoS 可有多个 TSC 通道。 |
| Michael MIC | Michael Message Integrity Code | TKIP 的轻量完整性保护，8 bytes/64-bit，强度有限。 |
| PMK | Pairwise Master Key | 主密钥；PSK 模式由 passphrase 和 SSID 经 PBKDF2 得到。 |
| PTK | Pairwise Transient Key | 临时会话密钥，由 PMK、ANonce、SNonce、双方 MAC 派生。 |
| EAPOL | EAP over LAN | 客户端和 AP 之间承载 EAP/握手消息。 |
| RADIUS | Remote Authentication Dial-In User Service | AP 和认证服务器之间传递认证结果和密钥材料。 |
| brute force | 暴力穷举 | 枚举所有可能密码，随机长密码很难被穷举。 |
| dictionary attack | 字典攻击 | 只试常见词和变形，现实中常比完全暴力更有效。 |
| rainbow table | 彩虹表 | 预计算常见 SSID 和口令的结果，加速离线破解。 |

关键公式/流程：

- PSK 到 PMK：`PMK = PBKDF2(passphrase, SSID, 4096 iterations, 256 bits)`。
- PTK 派生输入：`PTK = PRF(PMK, ANonce, SNonce, AP MAC, STA MAC)`。
- TKIP 加密一帧：payload -> Michael MIC -> ICV -> per-packet key mixing -> RC4 -> ciphertext。
- 4-way handshake：Msg1 发 ANonce；Msg2 回 SNonce+MIC；Msg3 下发 GTK/Key Data；Msg4 确认。

PPT 细节补充：

- TKIP 有 `active countermeasures`：如果短时间内检测到 Michael MIC 失败，会触发断开/暂停通信/重新密钥等反制，目的是限制攻击者在线试错速度。
- `EAPOL-Start` 是客户端发起 802.1X/EAP 认证的常见起始消息。`AS` 是 Authentication Server，通常是 RADIUS 服务器；AP 在 802.1X 中是 Authenticator，客户端是 Supplicant。
- WPA-PSK 的精确派生式可写 `PSK = PBKDF2(Password, SSID, SSIDlength, 4096, 256)`，输出 256-bit PSK/PMK。SSID 作为盐，所以同一密码在不同 SSID 下结果不同。
- PTK 的精确输入可写 `PTK = HASH(PMK, ANonce, SNonce, STA MAC Address, AP MAC Address)`；实际标准还会排序 MAC/nonce 并使用 PRF，但考试写出这些输入即可。
- 暴力破解量级例子：8 位大小写字母数字密码空间 `62^8 = 218,340,105,584,896`。PPT 假设 `280GTX` 每秒 `11000 keys/sec`，8 位随机口令约需 `630 years`；`12-char passphrase` 才对应约 `9,309,091,680 years`。结论是随机长密码难以穷举，但弱口令仍会被 dictionary attack 优先击中。
- TKIP key mixing 分 `Phase 1` 和 `Phase 2`：Phase 1 把 temporal key、发射端地址和 TSC 高位混合，降低每包计算成本；Phase 2 加入 TSC 低位，生成实际 RC4 per-packet key。
- 离线口令攻击只需要抓到 4-way handshake；攻击者不需要继续和 AP 交互，因此弱口令的风险主要来自字典和泄露密码库。

## 历年卷风格练习

1. WPA 为什么说是过渡方案？它保留了 WEP 的哪个加密基础，又修补了哪些问题？
2. 抓到 WPA-PSK 的 4-way handshake 后，为什么可以离线 dictionary attack？
3. brute force、dictionary attack、rainbow table 的区别是什么？
4. Beck-Tews 攻击利用了 TKIP/QoS 的什么特性？

<details class="self-test-answer">
<summary>参考答案</summary>

1. WPA 需要兼容旧硬件，所以保留 RC4，但用 TKIP 增加 48-bit TSC、每包密钥混合、Michael MIC、序列检查和重新密钥机制，修补 WEP 的短 IV、弱完整性和密钥管理问题。
2. 握手中有 ANonce、SNonce、双方 MAC 和 MIC。攻击者本地猜 passphrase，经 PBKDF2 得 PMK，再派生 PTK 并计算 MIC；若和抓包 MIC 相同，密码正确，不需要在线询问 AP。
3. brute force 枚举所有字符串；dictionary attack 只试常见词和变形；rainbow table 提前预计算常见 SSID/密码组合，抓到握手后查表更快。
4. 802.11e QoS 有 8 QoS channels，各自维护 TSC/序列空间。攻击者可利用计数器较小的通道绕过部分反重放限制；Michael 失败反制约 2 MIC failures/min 限制了试错速度。

</details>
