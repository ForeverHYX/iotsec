---
title: "第四周：WEP 安全机制与漏洞"
source: "materials/第四周Wired Equivalent Privacy (WEP).pptx"
order: 4.1
---

# 第四周：WEP 安全机制与漏洞

## 零基础导读

WEP 解决的是 802.11 WLAN 早期最直接的问题：无线信号会从 AP 和 STA 的天线向外广播，楼外的人也可能收到，所以需要 link-layer encryption，让无线链路尽量像插网线一样不容易被旁人读懂。AP 是接入点，STA 是客户端，frame 是 802.11 发送的一帧数据，payload 是里面真正要保护的数据，IV 是每帧携带的初始化向量，ICV 是 WEP 用 CRC-32 算出的完整性检查值。WEP 把 `message || ICV` 和 RC4 生成的 keystream 做 XOR 得到密文，再把 IV 明文放在帧头附近一起发出。

WEP 的核心漏洞来自“流密码不能重用密钥流”。RC4 是 stream cipher，同一个 seed 会生成同一个 keystream。WEP 的 seed 是 `IV || shared key`，shared key 长期不变，IV 又只有 24 bit，而且必须明文发给接收方。24-bit 看起来有 1677 万种，但在 11 Mbps 高流量环境中约数小时就会耗尽；如果 IV 随机选，大约 5000 个包就会有明显碰撞概率。相同 IV 加相同 key 意味着相同 keystream，于是攻击者能用 `C1 XOR C2 = P1 XOR P2` 做分析。

WEP 的完整性也不安全。CRC-32 适合发现随机传输错误，但它没有密钥，而且线性；攻击者翻转密文的一位，就会翻转明文对应位，还能同步修正 ICV。已知明文也很多：LLC/SNAP 头、IP/ARP 格式、ARP replay 中可预测的字段都能帮助恢复 keystream。共享密钥认证四步更糟：AP 发明文 challenge，STA 用 WEP 加密后回传，旁观者把明文和密文异或，就得到该 IV 下的 keystream，可伪造认证但不一定知道长期 key。

## 本章知识地图

1. **从一帧看 WEP**：message -> CRC-32 得 ICV -> `IV || key` 输入 RC4 -> keystream -> XOR -> ciphertext，IV 明文随帧发送。
2. **IV 的矛盾**：接收方需要 IV 生成同一 keystream，所以 IV 必须公开；但 IV 短且可重复，公开后攻击者能找出 keystream reuse。
3. **CRC 与 MAC 的区别**：CRC-32 无密钥、线性，只防随机错误；HMAC/MAC 有密钥，目标是防恶意篡改。
4. **典型攻击直觉**：known plaintext、LLC/SNAP、ARP replay、weak IV/FMS、Chopchop、Fragmentation 都在利用 IV、RC4 或 ICV 的弱点。
5. **管理帧问题**：beacon、reassociation、deauthentication 等早期 802.11 管理帧缺少强认证，rogue AP 和断连攻击更容易发生。

## 初学者常见疑问

问：IV 公开为什么不是单独的问题？

答：IV 本身不是秘密。很多安全协议都会公开 nonce/IV，因为接收方需要它来解密。真正的问题是 WEP 的 IV 太短、可重复，又和长期 shared key 简单拼接成 RC4 seed。公开 IV 让攻击者能快速识别“这两帧用了同一个 IV”，从而推断它们用了同一 keystream。

问：共享密钥认证四步为什么会泄露 keystream？

答：流程是 AP 发明文 challenge，STA 用 WEP 把 challenge 加密后发回，AP 解密验证。旁观者同时看到明文 challenge 和密文 challenge；两者 XOR 就是对应 IV 下的 RC4 keystream。攻击者之后可以用这段 keystream 加密自己的 challenge 响应，从而伪造认证。它泄露的是一段 keystream，不是直接泄露长期 WEP key。

问：为什么加长 WEP key 仍然不够？

答：104-bit key 比 40-bit key 更难暴力猜，但没有修复 24-bit IV、CRC-32 非 MAC、IV 明文且可重用、共享密钥人工配置、RC4 weak IV、管理帧缺少认证等协议设计问题。WEP 的漏洞不是单个参数太小，而是多个层面的设计都错了。

## 1. 本章速览

WEP 是 Wi-Fi 早期安全协议，目标是为无线提供“等同有线”的隐私保护，但它在密钥管理、IV 设计、完整性校验和认证协议上都有根本缺陷。本章考试重点不是记攻击工具名字，而是能从 WEP 加密流程推导出为什么会出现密钥流重用、消息篡改、重放和认证绕过。

## 2. 无线环境中的威胁

- 无线没有天然物理边界，范围内都能监听。
- 攻击者可以轻易窃听、注入伪造消息、重放旧消息。
- 伪造 disassociation/deauthentication 消息可诱导终端重新连接，配合 rogue AP 实现中间人攻击。
- jamming、MAC 层伪造和高层协议攻击都能破坏可用性。

## 3. WEP 目标与组成

- **目标**：机密性、访问控制、数据完整性。
- **加密算法**：RC4 流密码。
- **密钥结构**：早期 64-bit WEP = 40-bit 长期共享密钥 + 24-bit IV；后续 128-bit WEP = 104-bit 共享密钥 + 24-bit IV。
- **完整性字段**：ICV，基于 CRC-32。
- **发送内容**：明文消息 + CRC 形成 plaintext，再与 RC4 密钥流 XOR，最后把 IV 明文放在帧中。

## 4. WEP 加密与解密流程

- 加密：
  1. 对消息计算 CRC-32，得到 ICV。
  2. 把 IV 与共享密钥拼接，作为 RC4 seed。
  3. RC4 生成密钥流。
  4. `(message || ICV) XOR keystream` 得到密文。
  5. 明文携带 IV。
- 解密：
  1. 接收方取出 IV。
  2. 用 `IV || key` 生成同一密钥流。
  3. 密文 XOR 密钥流恢复消息和 ICV。
  4. 检查 CRC。

## 5. WEP 的根本缺陷

- **IV 太短**：24-bit 只有约 1677 万种。高流量下很快耗尽；随机 IV 根据生日悖论更早碰撞；网卡重启从 0 开始会重复。
- **IV 明文传输且可重用**：攻击者能观察 IV，识别相同密钥流。
- **流密码密钥流重用灾难**：若 `C1=P1 XOR K`、`C2=P2 XOR K`，则 `C1 XOR C2 = P1 XOR P2`，已知或可猜部分明文即可恢复信息。
- **RC4 弱 IV/弱密钥问题**：部分 IV 模式会泄露 RC4 内部状态与密钥关系。
- **CRC-32 不是密码学 MAC**：CRC 是线性校验，攻击者可修改密文并同步修改 ICV。
- **缺少密钥管理**：共享主密钥手工配置，长期不变，一个泄露影响全网。
- **共享密钥认证反而泄露密钥流**：挑战明文和加密挑战都可被观察，攻击者可恢复对应密钥流并伪造认证。
- **位翻转攻击直觉**：流密码中翻转密文某一位会翻转明文对应位；CRC-32 又是线性的，攻击者可以计算需要同步修改的 ICV 差分，因此 WEP 的“完整性”不能抵抗恶意修改。
- **IV 重用为什么很快出现**：24-bit IV 看似有 1677 万种，但忙碌 AP 每天可发送大量帧；若 IV 随机选择，生日悖论会让碰撞远早于空间耗尽；若网卡重启从初值开始，重复更直接。

## 6. 常见攻击

- **暴力/字典攻击**：尝试候选密钥，用抓到的包和 ICV 检查验证。
- **FMS 攻击**：利用 RC4 弱 IV 与已知 SNAP/SAP 头部，收集足够包后恢复 WEP 密钥。
- **Chopchop 攻击**：不恢复密钥，而是利用 ICV 和 AP 响应逐字节恢复明文。
- **Fragmentation 攻击**：802.11 碎片使用相同 IV 时，可利用已知 LLC/SNAP 头推导密钥流，构造可被接受的加密片段。
- **重放/注入攻击**：ICV 弱且缺少可靠重放保护，使攻击者能重放或修改数据帧。
- **FMS 细节**：PPT 中 weak IV 模式大约有 9000 个，FMS 会利用 RC4 key scheduling 的偏差和已知 LLC/SNAP/SAP 头部。早期实验常以约 20,000 packets 作为能观察到恢复趋势的量级，实际需要包数取决于流量和实现。
- **Fragmentation 细节**：802.11 允许分片，PPT 强调最多 16 fragments、总共可构造约 64 bytes 任意数据。计算直觉是：每个 fragment 可从 8-byte LLC/SNAP 已知明文推出 8 bytes keystream，其中 4 bytes 要用于 CRC/ICV，因此每片约剩 4 bytes 可控数据，`(8 - 4) * 16 = 64`。攻击者可构造短加密片段让 AP 接受并产生更多可分析流量。
- **废弃状态**：WEP 在 2005 年左右已被明确弃用。即使出现 256-bit/232-bit key variant，短 IV、CRC-32、RC4 weak IV 和密钥管理问题仍然存在。

## 7. “修补 WEP”为什么不够

课件提到的补救包括增大密钥长度、去掉弱 IV、频繁换密钥、EAP、IDS 等。但 WEP 的核心问题是协议设计同时错在 IV、完整性、认证、密钥管理多个层面。正确结论是：WEP 已被废弃，应迁移到 WPA/WPA2 或更新协议，而不是继续打补丁。

## 8. 考试重点

- 能画出 WEP 加密流程：`CRC -> IV||key -> RC4 -> XOR -> IV 明文附加`。
- 能解释为什么 24-bit IV 会碰撞，并说明生日悖论影响。
- 能用 XOR 公式说明密钥流重用的危害。
- 能说明 CRC-32 为什么不能替代 MAC。
- 能解释共享密钥认证为什么不安全。
- 能列出 FMS、Chopchop、Fragmentation 攻击各自利用的漏洞类型。

## 9. 易混点

- **增加密钥长度不能解决 IV 重用**：104-bit key 仍然搭配 24-bit IV，密钥流仍可能重复。
- **CRC 能发现随机错误，不代表能防恶意篡改**。
- **WEP 的“认证”不是强身份认证**：观察挑战-响应即可得到可复用信息。
- **RC4 是流密码**：重点风险是同一密钥流不能重复使用。

## 10. 快速自测

1. WEP 中 IV 为什么必须公开？公开后又造成什么风险？
2. 已知 `C1=P1 XOR K` 和 `C2=P2 XOR K`，为什么能得到 `P1 XOR P2`？
3. CRC-32 与 HMAC 的安全目标有什么差别？
4. 共享密钥认证会泄露什么？
5. 为什么说 WEP 应该被淘汰而不是修补？

<details class="self-test-answer">
<summary>参考答案</summary>

1. 接收方需要 IV 与共享密钥拼接生成同一 RC4 密钥流，所以 IV 必须随帧发送；公开且短的 IV 让攻击者能识别重复 IV，进而识别重复密钥流。
2. 两式异或得到 `C1 XOR C2 = P1 XOR K XOR P2 XOR K`，相同的 `K` 抵消，所以得到 `P1 XOR P2`，再结合已知明文可恢复内容。
3. CRC-32 主要检测随机传输错误，不依赖秘密密钥且线性；HMAC 使用秘密密钥，目标是抵抗恶意篡改并提供消息认证。
4. 攻击者能看到明文 challenge 和加密后的 challenge，两者异或可得到该 IV 下的 RC4 密钥流，从而伪造后续挑战响应。注意这不等于拿到长期 WEP key，也不能进一步正常访问网络；它只是说明共享密钥认证本身泄露了可复用信息。
5. WEP 同时存在短 IV、RC4 弱 IV、CRC 非 MAC、共享密钥长期不变、认证泄露密钥流等设计缺陷；单点补丁无法修复整体协议。

</details>

## 公式与术语速查

| 英文/缩写 | 中文含义 | 初学者要会的解释 |
|---|---|---|
| WEP | Wired Equivalent Privacy | 早期 802.11 加密协议，目标是让无线链路像有线一样私密，但设计已被淘汰。 |
| AP / STA | Access Point / Station | AP 是接入点，STA 是客户端设备。 |
| RC4 | Rivest Cipher 4 stream cipher | 流密码，输出 keystream；同一 seed 绝不能重复使用。 |
| IV | Initialization Vector | 初始化向量；WEP 中 24-bit，明文发送，与共享 key 拼接生成 RC4 seed。 |
| ICV | Integrity Check Value | WEP 用 CRC-32 生成的完整性字段，只能防随机错误，不能防恶意篡改。 |
| CRC-32 | 循环冗余校验 | 无密钥、线性，攻击者可同步修改密文和 ICV。 |
| LLC/SNAP | 链路层头部 | 常见已知明文字段，攻击者可用它推导部分 keystream。 |
| ARP replay | ARP 重放 | 重放可预测 ARP 包诱导 AP 产生更多流量，加速收集 IV/密文。 |
| FMS | Fluhrer-Mantin-Shamir attack | 利用 RC4 weak IV 和已知头部恢复 WEP key 的经典攻击。 |
| Chopchop | 逐字节明文恢复攻击 | 不直接求 key，通过 ICV 和 AP 响应逐步恢复明文。 |
| Fragmentation attack | 分片攻击 | 利用 802.11 分片和已知 keystream 构造短加密片段。 |

核心公式：

- WEP 加密：`ciphertext = (message || ICV) XOR RC4(IV || key)`。
- WEP 解密：`message || ICV = ciphertext XOR RC4(IV || key)`。
- keystream 重用：若 `C1=P1 XOR K`、`C2=P2 XOR K`，则 `C1 XOR C2 = P1 XOR P2`。
- Fragmentation 推导：每个 fragment 由 8-byte LLC/SNAP 推出 8 bytes keystream，其中 4 bytes 给 CRC/ICV，16 fragments 总共约 `(8 - 4) * 16 = 64` bytes 可控数据。

PPT 细节补充：

- `Wi-Fi Alliance` 是推动 Wi-Fi 互操作认证的产业组织；考试里 Wi-Fi 标准本身写 IEEE 802.11，认证/品牌生态常写 Wi-Fi Alliance。
- Wi-Fi 常使用 `2.4 GHz and 5 GHz public spectrum bands`，这些免授权频段易部署，但也更容易拥塞、被监听或被干扰。
- WEP 设计目标还包含 `Authenticity`、`Replay detection` 和 `Protection against jamming` 等安全期望；但实际 WEP 并没有真正提供强认证、强重放防护或抗干扰能力。
- WEP 密钥长度常见两种说法：64-bit WEP = 40-bit key + 24-bit IV；扩展 WEP 可写 `256 bit = 232-bit key + 24-bit IV`。无论长期 key 多长，24-bit IV 仍太短。
- RC4 weak IV/FMS 类攻击里会关注 IV 模式：`first byte 3..7`、`second byte 255`、`third byte anything`。PPT 给出的数量级是约 `9000 weak IVs`，大约占 `5% of IVs`；本质是 RC4 KSA 早期输出泄露 key 字节统计偏差。
- `AirSnort` 是早期自动收集 WEP 弱 IV 并恢复密钥的工具名，考到工具时写“抓大量包 -> 利用 RC4 weak IV 统计恢复 WEP key”。
- LLC/SNAP 已知明文常见字节可写 `AA AA 03 00 00 00 08`，攻击者利用这些固定头部从密文中推出 keystream。
- WEP 的 ICV 只防随机传输错误，不防恶意篡改；真正的数据完整性应使用带密钥的 MAC/HMAC，而不是无密钥 CRC-32。

## 历年卷风格练习

1. WEP 用什么算法保持数据完整性？用什么算法加密？
2. 画出或写出 WEP 加密过程，并指出 IV 为什么必须明文发送。
3. 为什么 CRC-32 不能替代 MAC？请用位翻转攻击解释。
4. 共享密钥认证四步为什么会泄露 keystream？攻击者知道 WEP key 吗？

<details class="self-test-answer">
<summary>参考答案</summary>

1. WEP 使用 CRC-32 生成 ICV 来检查数据完整性，使用 RC4 流密码加密。
2. 发送方先对 message 算 CRC-32 得 ICV，再用 `IV || key` 作为 RC4 输入生成 keystream，计算 `(message || ICV) XOR keystream` 得密文，并把 IV 明文放入帧中。IV 必须明文发送，因为接收方需要同一 IV 才能生成相同 keystream。
3. CRC-32 没有密钥且线性。攻击者翻转密文某位会翻转明文对应位，还可计算 ICV 的同步差分，因此能构造通过 CRC 检查的篡改包；MAC/HMAC 依赖密钥，攻击者不能伪造。
4. AP 发明文 challenge，STA 返回 WEP 加密 challenge。旁观者把明文和密文异或即可得到该 IV 下的 keystream，可伪造认证响应；但这不等于知道长期 WEP key，也不能进一步正常访问网络。

</details>
