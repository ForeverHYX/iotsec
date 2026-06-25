---
title: "Lecture 13: Bluetooth Security and Privacy"
source: "materials/Lecture 13 Bluetooth Security and Privacy.pptx"
order: 13
---

# Lecture 13: Bluetooth Security and Privacy

## 零基础导读

Classic Bluetooth 可以先从 piconet 理解：一个 master 和最多 7 个 active slave 组成小网络，master 的 BD_ADDR 和 clock 决定跳频序列，所有 slave 跟着 master 的节奏走。物理信道按 625 微秒时隙组织，使用 TDD 交替发送，所以常被看成半双工。FHSS/AFH 能减少固定频点干扰，但跳频不是加密；真正的安全还要靠配对、link key、encryption key 和访问授权。

Classic 和 BLE 的目标不同。Classic 适合耳机音频、持续连接和较高吞吐；BLE 更重视低功耗、短包、低延迟和低占空比传感。BLE 使用广播信道让设备先被发现，广播包如 ADV_IND、ADV_DIRECT_IND 会暴露地址、设备名、服务 UUID、manufacturer data、RSSI 和时间模式。即使地址随机化，payload 和行为模式仍可能让攻击者 tracking、profiling、harming。

Bluetooth 安全的入门链条是：配对 pairing 让两个设备建立信任，bonding 把密钥保存下来以后复用。旧模式中 PIN、BD_ADDR、RAND 等输入生成 link key/encryption key；短 PIN、弱 RNG、可协商短密钥长度都会让攻击变容易。BLE 常用 AES-CCM 提供加密和 MIC，但前提是配对和密钥管理正确。BLE-Guardian 的思路是先学习目标设备广告序列，在目标广告时隙定向干扰隐藏设备，再通过 OOB 或连接参数放行授权客户端。

做 BLE 安全题时，还要能把“攻击能力”说具体。TI sniffer、Ubertooth、libbtbb、Wireshark、kismet、crackle、LightBlue 这类工具分别覆盖抓包、解码、扫描、服务枚举和弱配对分析。攻击者可被动收集 ADV_IND 广播做 tracking，也可主动连接 GATT 枚举服务，或诱导设备使用 Just Works、短密钥、旧配对方式形成 downgrade attack。工具名本身不是答案重点，重点是说明它们把“短距离蓝牙”变成可批量扫描、记录和分析的无线攻击面。

## 本章知识地图

1. **Classic Bluetooth**：piconet、master/slave、scatternet、parked slave、625 微秒 slot、TDD、FHSS/AFH。
2. **Classic vs BLE**：Classic 更适合连续音频和较高吞吐，BLE 更适合低功耗传感；BLE 使用 advertising/scanning/initiating/connection 状态。
3. **安全目标**：Authentication、Confidentiality、Authorization；短距离和跳频都不能替代这些目标。
4. **配对和密钥**：PIN/BD_ADDR/RAND -> link key/encryption key；短 PIN、downgrade attack、弱随机数和短密钥协商是风险。
5. **BLE 隐私和攻击工具**：ADV_IND、RSSI、payload、GATT 服务、设备名和广播间隔可被 TI sniffer、Ubertooth、LightBlue 等设备或 App 收集；BLE-Guardian 用 hiding + access control 缓解。

## 初学者常见疑问

问：为什么 slave 不能直接和 slave 通信？

答：piconet 的时间、跳频序列和调度由 master 控制。slave 同步到 master 的 clock 和 hopping sequence，在被分配的时隙里和 master 交换数据。两个 slave 没有共同的直接调度关系，因此经典 piconet 中不能绕过 master 直接通信。

问：短 PIN 为什么危险？

答：短 PIN 的搜索空间很小。旧配对中 PIN 参与生成 link key，如果攻击者抓到配对过程，可能离线枚举 PIN，恢复 link key 或 encryption key。可协商密钥长度也可能被降级，弱 RNG 会让 RAND 不够随机。这些问题说明“能配对”不等于“配对强”。

问：BLE-Guardian 为什么要学习广告序列？

答：BLE 广播不是连续发送，而是在 37/38/39 信道上按间隔和随机延迟出现。BLE-Guardian 要在目标广告出现时定向隐藏，必须预测设备什么时候在哪个信道发包；否则会干扰不准，既挡不住远处扫描者，也可能影响合法连接。

## 1. 本章速览

Bluetooth 是短距离个人区域网络技术，工作在 2.4 GHz ISM 频段，广泛用于手机、耳机、键盘、车载、工业和 IoT 设备。本章重点是 Bluetooth Classic 的 piconet、跳频、主从结构和安全模式，以及 BLE 的广播、配对、地址随机化、隐私追踪和 BLE-Guardian 防护。

## 2. Bluetooth 基础

- 工作频段：2.4-2.485 GHz ISM。
- 目标：短距离数据交换，最初用于替代 RS-232 数据线。
- 组织：Bluetooth SIG 管理；早期曾标准化为 IEEE 802.15.1。
- 应用：耳机、音箱、键盘、相机、打印机、手机、车载、工业系统、嵌入式设备。
- 经典 Bluetooth 支持较高连续数据传输；BLE 面向低功耗、短包、低占空比传感场景。

## 3. Piconet 与物理层

- **Piconet**：一组 ad hoc 连接设备，一个 master，最多 7 个 active slaves，可有更多 parked slaves。
- Master 设置时钟和跳频序列，分配 slave 速率。
- Slaves 只能与 master 通信，不能直接互相通信。
- 多个 piconet 可形成 scatternet，设备可用 TDM 参与多个 piconet；一个设备不能同时作为多个 piconet 的 master。
- 物理信道分为 625 microsecond 时隙，使用 TDD，master 和 slave 交替发送。
- 使用慢跳频扩频，跳频模式由 master 地址和时钟决定。
- **半双工理解**：Bluetooth 典型链路用 TDMA-TDD 交替占用时隙，同一物理信道上 master/slave 不同时发送，考试匹配题通常把 Bluetooth 归为半双工。
- **跳频的边界**：跳频降低固定频点干扰和简单监听风险，但跳频序列由协议参数决定，不提供等价于加密的机密性。

## 4. Bluetooth Classic 与 BLE

- Classic Bluetooth：适合音频、持续连接和较高吞吐。
- BLE：低功耗设计，不完全向下兼容 Classic；适合传感器短数据包、低延迟、低占空比场景。
- Dual Mode/Smart Ready 设备可同时支持 Classic 和 BLE。
- BLE 不适合长时间流媒体，但非常适合 IoT 外设。

## 5. Bluetooth 安全目标与模式

安全目标包括：

- **Authentication**：验证通信设备身份。
- **Confidentiality**：保护数据不被未授权读取。
- **Authorization**：控制设备或用户能访问哪些资源。

传统安全模式：

- **Mode 1: No Security**：只依赖短距离和跳频，基本没有协议层安全。
- **Mode 2: Service Level Security**：连接后按服务控制访问，设备可分 trusted/untrusted。
- **Mode 3: Link Level Security**：链路建立前进行认证和加密，基于 PIN、BD_ADDR、随机数、link key、encryption key。

## 6. Mode 2 的服务级安全

- Trusted device：已经建立固定关系，可访问所有服务。
- Untrusted device：认证过但无固定关系，只能访问有限服务。
- 服务安全级别：
  - Level 3：需要认证和授权，通常输入 PIN。
  - Level 2：只需要认证。
  - Level 1：开放访问。
- 风险：同一设备上所有服务策略粒度可能不够细，旧应用默认开放。

## 7. Bluetooth 安全问题

- RNG 强度未知，弱随机数会削弱认证。
- 允许短 PIN，导致 link key 和 encryption key 可预测。
- 加密密钥长度可协商，可能被降级。
- BD_ADDR 若和用户绑定，会造成长期位置和行为跟踪。
- 旧式挑战响应可能只有单向认证，存在中间人风险。
- DoS 可让设备不可用并消耗电池。
- Fuzzing 可利用畸形消息触发协议栈漏洞。
- Bluejacking/其他滥用利用设备标识和可发现状态进行骚扰或劫持。

## 8. BLE Primer

BLE 典型状态：

- **Standby**：低功耗，收发关闭。
- **Advertising**：低功耗设备发送广告包。
- **Scanning**：客户端监听广告信道。
- **Initiating/Connection**：客户端发起连接。

BLE 广播信道：

- 37: 2402 MHz
- 38: 2426 MHz
- 39: 2480 MHz

BLE 安全和隐私机制：

- 配对与 bonding：防止未授权访问设备或受保护服务。
- 地址随机化：降低长期跟踪。
- 直接广播：减少被无关设备扫描和画像。
- 最小暴露 GATT 服务、强配对方法、合理密钥长度、关闭可发现模式和及时补丁，是实际部署中比“短距离”更可靠的保护。

## 9. BLE 隐私问题

- 攻击者可被动扫描 BLE 广播，收集时间戳、蓝牙地址、广告内容、RSSI。
- 很多设备使用固定地址、不充分随机化、唯一设备名或唯一服务字段。
- 广播内容可能泄露设备类型、健康状态、生活习惯、位置、偏好。
- 风险链条：
  1. Tracking User：用稳定标识追踪用户。
  2. Profiling User：根据设备和广告内容画像。
  3. Harming User：对敏感设备指纹识别、未授权访问或攻击。

常见 BLE 攻击和工具可以按下表记忆：

| 攻击/能力 | 常用工具或设备 | 初学者理解 |
|---|---|---|
| 广播抓包与监听 | TI sniffer、Ubertooth、kismet、Wireshark | 在 37/38/39 广播信道记录 ADV_IND、RSSI、地址和 payload，用于追踪或画像。 |
| 协议解码与弱配对分析 | Ubertooth + libbtbb、crackle | 解码 BLE/Classic 流量，分析 Just Works、短 TK、弱 PIN 或未加密连接。 |
| GATT 枚举与主动探测 | LightBlue、nRF Connect 等 App | 像客户端一样连接设备，枚举 service/characteristic，测试是否缺少授权。 |
| downgrade attack | 攻击者干预协商或诱导旧模式 | 让设备从强配对/长密钥降到 Just Works、短密钥或旧安全模式，从而绕过预期安全强度。 |

## 10. BLE-Guardian

- 目标：用现成硬件、少用户干预、设备无关地保护 BLE 用户隐私。
- 硬件示例：Ubertooth One，可在 BLE 信道上收发。
- **Device Hiding**：学习目标设备广告序列，在广告时隙进行定向干扰，使远处攻击者看不到广告。
- **Access Control**：通过 OOB 信道或连接参数识别授权客户端，允许合法连接。
- 评估结果显示可把攻击者可读广告的距离限制在很短范围，并对目标设备/客户端无额外能耗。
- 这类方案的核心是把“谁能听到广告”和“谁能建立连接”从默认公开改成可控范围，但它不能替代设备自身的认证、授权和加密。

## 11. 考试重点

- 能解释 piconet 中 master/slave、clock、frequency hopping 的作用。
- 能说明 Classic Bluetooth 与 BLE 的区别。
- 能列出 Bluetooth 安全的认证、机密性、授权目标。
- 能比较 Mode 1/2/3 的安全位置和强度。
- 能说明短 PIN、BD_ADDR、可协商密钥长度带来的风险。
- 能解释 BLE 广播为什么天然带来隐私追踪风险。
- 能描述 BLE-Guardian 的基本思路：隐藏广告 + 授权连接。

## 12. 易混点

- **短距离不等于安全**：高增益天线、被动扫描和中继都能扩大攻击能力。
- **跳频不等于加密**：跳频增加监听难度，但不能替代认证和加密。
- **地址随机化不等于完全匿名**：广告 payload、设备名、服务 UUID、RSSI 模式仍可指纹化。
- **BLE 低功耗不等于低风险**：广播机制让被动追踪更容易。

## 13. 快速自测

1. Piconet 中为什么 slave 只能和 master 通信？
2. Mode 2 和 Mode 3 的安全检查发生在连接的哪个阶段？
3. BD_ADDR 被长期收集会造成什么隐私问题？
4. BLE 广播包中哪些字段可能被用于追踪？
5. BLE-Guardian 为什么需要学习广告序列？

<details class="self-test-answer">
<summary>参考答案</summary>

1. Piconet 的时钟、跳频序列和时隙调度由 master 控制，slave 同步到 master 并按分配时隙通信；协议拓扑不支持 slave 之间直接通信。
2. Mode 2 在链路建立后按服务做访问控制；Mode 3 在链路建立前就进行认证和加密，安全检查发生得更早。
3. BD_ADDR 是稳定设备标识，长期收集可把设备与用户位置、出行规律、生活习惯和社交场景关联起来。
4. 蓝牙地址、设备名、服务 UUID、manufacturer data、广播间隔、RSSI 模式和特定 payload 都可能形成指纹。
5. 它要预测目标设备何时在哪些 BLE 广播信道发广告，才能在对应时隙做定向隐藏，同时尽量不影响合法客户端连接。

</details>
