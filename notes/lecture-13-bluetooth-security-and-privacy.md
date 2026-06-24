---
title: "Lecture 13: Bluetooth Security and Privacy"
source: "materials/Lecture 13 Bluetooth Security and Privacy.pptx"
order: 13
---

# Lecture 13: Bluetooth Security and Privacy

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

## 9. BLE 隐私问题

- 攻击者可被动扫描 BLE 广播，收集时间戳、蓝牙地址、广告内容、RSSI。
- 很多设备使用固定地址、不充分随机化、唯一设备名或唯一服务字段。
- 广播内容可能泄露设备类型、健康状态、生活习惯、位置、偏好。
- 风险链条：
  1. Tracking User：用稳定标识追踪用户。
  2. Profiling User：根据设备和广告内容画像。
  3. Harming User：对敏感设备指纹识别、未授权访问或攻击。

## 10. BLE-Guardian

- 目标：用现成硬件、少用户干预、设备无关地保护 BLE 用户隐私。
- 硬件示例：Ubertooth One，可在 BLE 信道上收发。
- **Device Hiding**：学习目标设备广告序列，在广告时隙进行定向干扰，使远处攻击者看不到广告。
- **Access Control**：通过 OOB 信道或连接参数识别授权客户端，允许合法连接。
- 评估结果显示可把攻击者可读广告的距离限制在很短范围，并对目标设备/客户端无额外能耗。

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
