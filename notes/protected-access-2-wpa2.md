---
title: "第四周：WPA2、CCMP 与 KRACK"
source: "materials/第四周Protected Access 2 (WPA2).pptx"
order: 4.3
---

# 第四周：WPA2、CCMP 与 KRACK

## 零基础导读

WPA2 是 Wi-Fi 安全从“修补旧硬件”走向“重新设计”的阶段，正式对应 IEEE 802.11i/RSN。你可以把连接过程分成四步：Discovery 阶段 AP 用 Beacon/Probe Response 发 RSN IE，告诉客户端支持哪些 AKM suite、pairwise cipher、group cipher；Association Request 中 STA 选择自己要用的组合；Authentication 阶段用 PSK 或 802.1X/EAP 得到 PMK；Key Management 阶段用 4-way handshake 派生并安装 PTK/GTK；最后 Phase 4 用 CCMP 保护数据帧。RSN IE 是 Robust Security Network Information Element，AKM 是 Authentication and Key Management。

密钥层级是理解 WPA2 的核心。PMK 不直接加密数据，它只是主材料。4-way handshake 用 PMK、ANonce、SNonce、AP MAC、STA MAC 派生 PTK。PPT 中 PTK 64 bytes，可拆出 KCK/KEK/TK 各 16 bytes 等用途密钥：KCK 验证 EAPOL-Key MIC，KEK 加密 GTK 等 Key Data，TK 加密单播数据。GTK 是组密钥，用于广播/组播数据。这样设计的好处是主密钥不直接暴露在每个数据包上，不同用途的密钥也分开。

CCMP 使用 128-bit AES-CCM，包含 CTR 和 CBC-MAC。AES 本来是 block cipher，一次处理固定大小的块；CTR 模式把 AES 变成 keystream 生成器，再和明文 XOR，提供机密性；CBC-MAC 对帧内容和相关头部计算认证标签，提供完整性。48-bit PN/nonce 防重放，也防 CTR keystream 重用。KRACK 时间线说明实现细节能破坏强算法：攻击者阻断 Msg4，AP 重传 Msg3，客户端重复安装同一 PTK，PN/nonce 归零，于是可能重用 keystream。攻击者不需要知道 Wi-Fi 密码，也不是破解 AES。

## 本章知识地图

1. **WPA2 四阶段**：Discovery/RSN IE -> Authentication/PMK -> 4-way handshake/PTK+GTK -> CCMP data protection。
2. **安全能力协商**：RSN IE 发布能力，Association Request 选择 AKM、pairwise cipher、group cipher；Open System Authentication 本身不提供安全。
3. **密钥层级图**：PMK -> PTK -> KCK/KEK/TK，同时 AP 分发 GTK；不同密钥服务不同任务。
4. **CCMP 一帧流程**：构造 nonce/PN -> CTR 加密明文 -> CBC-MAC 算标签 -> 接收端检查 PN 和 MIC。
5. **漫游优化**：PMK Caching 复用最近的 PMK，Pre-authentication 让 STA 在切换 AP 前先完成认证，减少漫游时延。

## 初学者常见疑问

问：RSN IE 和 Association Request 为什么重要？

答：安全协议必须先协商“双方都支持什么”。AP 在 RSN IE 里发布支持的认证和密码套件，STA 在 Association Request 中选择一组。如果协商结果被降级或双方理解不一致，后面的认证和加密都可能建立在错误能力上。Open System Authentication 只是旧状态机步骤，不是真安全认证。

问：CCMP 为什么比 TKIP 强？

答：TKIP 仍基于 RC4 和 Michael MIC，是给旧硬件的补丁。CCMP 使用 AES-CCM，把机密性、完整性和重放保护设计在一起。CTR 负责加密，CBC-MAC 负责认证，PN/nonce 确保每包新鲜。只要 nonce 不重复，AES-CCMP 的安全基础远强于 WEP/WPA-TKIP。

问：KRACK 时间线为什么不是“破解密码”？

答：KRACK 利用的是密钥安装状态机。Msg3 可以重传，客户端如果重复安装已安装过的 PTK，就可能把 PN/nonce 重置。攻击者通过阻断/重放握手消息触发这个实现错误，并不需要知道 PMK 或 PSK。它说明“算法安全”和“实现按正确状态机使用算法”是两件事。

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

四条消息可按“给 nonce、证明、发组密钥、确认安装”记忆：

- Msg1：AP 发 ANonce 给 STA。
- Msg2：STA 发 SNonce 和 MIC，证明自己能由 PMK 派生 PTK。
- Msg3：AP 发带 MIC 的 Key Data，通常包含加密后的 GTK，并要求安装密钥。
- Msg4：STA 确认安装完成。KRACK 正是利用 Msg3 重传和重复安装逻辑出错。

## 6. Phase 4：CCMP

- **AES-CCMP** = Counter Mode + CBC-MAC Protocol。
- **CTR 模式**：用 AES 加密递增 counter 生成密钥流，再与明文 XOR，提供机密性。
- **CBC-MAC**：对数据块链式计算消息认证码，提供完整性。
- **48-bit Packet Number PN**：用于重放保护，并参与构造 nonce，保证每包新鲜性。
- CCMP 保护帧体和大部分 MAC 头，降低攻击者利用头部字段的能力。
- CTR 和 CBC-MAC 必须使用同一套明确的 nonce/PN 规则：CTR 一旦 nonce 重复会重用密钥流，CBC-MAC 若输入上下文不绑定也可能被拼接或重放，所以 CCMP 把地址、优先级、PN 等字段纳入处理。

## 7. WPA/WPA2/WEP 对比

- WEP：RC4，24-bit IV，CRC-32，缺少密钥管理，已废弃。
- WPA：RC4 + TKIP，Michael MIC，48-bit IV，4-way handshake，是过渡方案。
- WPA2：AES-CCMP，RSN，强完整性和重放保护，是长期替代方案。

## 8. WPA2 的限制

- 无法防止纯物理层攻击，如 RF jamming。
- 控制和管理帧历史上保护不足，可导致 DoS、MAC spoofing、大规模 deauthentication。
- 安全证明通常针对抽象协议或单独密码组件，真实系统组合和实现仍可能出错。
- **Pros**：相对 WEP/WPA-TKIP，WPA2 能抵抗 IV 碰撞导致的简单 keystream reuse、CRC 线性篡改、TKIP/Michael 弱完整性等攻击，并通过 RSN/CCMP 提供更强的机密性、完整性和重放保护。
- **Cons**：WPA2 仍不能防 RF jamming、data flooding、AP failure 等可用性问题；AP 被打掉、资源被洪泛或管理帧保护不足时，AES-CCMP 本身也无法保证服务持续可用。
- **快速漫游**：PMK Caching 让 STA 在短时间内回到同一 AP/网络时复用 PMK，Pre-authentication 允许 STA 在切换前先和目标 AP 完成认证，两者都减少漫游时重新认证的时延。

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

<details class="self-test-answer">
<summary>参考答案</summary>

1. Personal 使用共享 PSK，不需要认证服务器；Enterprise 使用 802.1X/EAP/RADIUS，可按用户认证并分发 PMK，更适合企业管理。
2. 两个 nonce 提供双方贡献的新鲜随机性，防止不同会话派生相同 PTK，并让双方确认对方参与了本次握手。
3. KCK 用于 EAPOL-Key MIC，KEK 用于加密 GTK 等 Key Data，TK 用于加密和解密单播数据帧。
4. CCMP 用 AES-CTR 生成密钥流保护机密性，用 CBC-MAC 计算认证码保护完整性，并用 48-bit PN/nonce 防重放和密钥流重用。
5. KRACK 不破解 AES，而是诱导客户端重复安装已安装的 PTK，导致 nonce/PN 重置；实现层破坏了算法安全所依赖的“nonce 不重复”条件。

</details>
