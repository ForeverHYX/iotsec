---
title: "第三周 Part 1：无线通信 MAC 层"
source: "materials/第三周-part1-无线通信MAC层.pptx"
order: 3.1
---

# 第三周 Part 1：无线通信 MAC 层

## 零基础导读

MAC 层要解决的是“大家共用同一条空气信道时，谁先说话”。如果只有一个节点，它可以用完整速率 `R bps`；如果有 `M` 个节点，理想 MAC 希望每个活跃用户平均能拿到接近 `R/M` 的能力，同时低延迟、公平、去中心化、不依赖复杂同步。问题在于无线是 broadcast channel：两个节点同时发，接收端可能只听到混在一起的信号，这叫 collision 或干扰。

三类 MAC 方案可以按“避免碰撞的方式”理解。信道分割把时间、频率、码片或空间提前分好，如 TDMA、FDMA、CDMA；它适合稳定负载，但空闲槽和空闲频段会浪费。随机访问不提前分配，节点有包就竞争，如 ALOHA、Slotted ALOHA、CSMA/CA；它适合突发流量，但要处理碰撞和重传。轮询和令牌让节点按顺序获得发送权，公平可控，但需要控制信道、中心协调或 token passing，控制开销和故障点更明显。

无线比有线更难做碰撞检测。以太网 CSMA/CD 可以边发边听，检测碰撞后立刻停；无线发射功率远强于接收信号，节点很难一边发一边可靠听别人。更重要的是，发送端的 carrier sensing 不代表接收端安全：隐藏节点听不到彼此但会在同一接收端碰撞，暴露节点听到了别人却其实可以安全发给另一个接收端。802.11 因此使用 CCA、DIFS、随机 backoff、SIFS/ACK、RTS/CTS 和 NAV 来降低碰撞概率。

## 本章知识地图

1. **理想 MAC**：单用户 `R bps`，`M` 个用户平均 `R/M`，低延迟、公平、去中心化、少同步。
2. **信道分割**：FDMA/TDMA/CDMA/SDMA 解决碰撞，但需要控制方式；中心协调、控制信道、ad-hoc/MANET 协商各有代价。
3. **随机访问演进**：ALOHA 不监听，Slotted ALOHA 缩短碰撞窗口，CSMA 先听再发，CSMA/CA 再用退避和 ACK 避免无线碰撞。
4. **802.11 细节**：CCA 判断信道忙闲，DIFS 后竞争，contention window 里随机 backoff，SIFS 后 ACK 优先返回。
5. **拓扑问题**：hidden terminal、exposed terminal、RTS、CTS、NAV 解释为什么“我听到/没听到”不能直接等于“接收端会不会被干扰”。

## 初学者常见疑问

问：为什么 ALOHA 到 CSMA/CA 是一步步改进？

答：ALOHA 有包就发，所以简单但碰撞多。Slotted ALOHA 要求节点只在时隙开头发，把碰撞窗口缩短，但需要同步。CSMA 先监听，空闲才发，降低碰撞概率，但传播延迟和隐藏节点仍会出错。CSMA/CA 进一步加入 CCA、DIFS、随机 backoff、SIFS/ACK；它不是检测碰撞，而是尽量在发送前避开碰撞，发送后用 ACK 判断是否成功。

问：CDMA 里的 chip sequence 和 inner product 是什么直觉？

答：CDMA 让多个用户同时同频发送，但每个用户把一个比特扩展成一串码片 chip sequence。接收端用目标用户的码片序列做 inner product，如果码片近似正交，目标用户的信号会被相关出来，其他用户的信号会平均掉。这需要同步和功率控制，否则 near-far effect 会让强用户淹没弱用户。

问：RTS/CTS 和 NAV 到底谁听谁？

答：发送方先发 RTS，接收方回 CTS。听到 RTS 的节点知道发送方附近要忙，听到 CTS 的节点知道接收方附近要忙。隐藏节点可能听不到 RTS，但通常能听到接收方 CTS，于是设置 NAV，在预约时间内不发。暴露节点问题则提醒我们：有些听到忙的节点其实对另一个方向发送不会干扰，但保守退避会降低空间复用。

## 1. 本章速览

MAC 层要解决的问题是：多个节点共享同一个无线信道时，谁在什么时候发送。考试重点是信道分割、随机访问、轮流访问三类方案，以及 ALOHA、CSMA、CSMA/CD、CSMA/CA、RTS/CTS、隐藏节点和暴露节点。

## 2. 多址接入问题

- 多个节点通过共享信道与 AP/BS 通信。
- 一个节点独占信道时可用全速率 `R bps`。
- 两个或多个节点同时发送会发生碰撞或干扰。
- MAC 协议目标：高吞吐、低延迟、公平、去中心化、低开销，并能处理碰撞。

## 3. 三类 MAC 思路

- **信道分割**：把时间、频率、码片分给不同节点。典型 FDMA、TDMA、CDMA。优点是碰撞少；缺点是低负载时浪费。
- **随机访问**：节点有包就竞争信道，可能碰撞，碰撞后随机重传。典型 ALOHA、CSMA、CSMA/CA。
- **轮流访问**：节点按轮询或令牌轮流发送。优点是公平、可控；缺点是控制开销和中心节点/令牌故障问题。
- **信道分割的控制方式**：FDMA/TDMA/CDMA 不只是“怎么分资源”，还要决定谁来分。可以由中心节点协调，可以用控制信道发布分配，也可以在 ad-hoc/MANET 中由节点协商。控制方式本身会消耗带宽，并可能成为故障点或攻击点。

## 4. ALOHA 与 Slotted ALOHA

- **纯 ALOHA**：节点有数据立即发送；若碰撞，在随机时间后重传。简单、去中心化，但最高吞吐约 18%。
- **时隙 ALOHA**：时间切成等长时隙，节点只在时隙开始发送；需要同步；最高吞吐比纯 ALOHA 高。
- **核心限制**：不监听信道，碰撞代价高；负载增加后吞吐会迅速下降。

## 5. CSMA 系列

- **CSMA**：发送前先监听信道，空闲才发送。减少但不能消除碰撞，因为传播时延会让两个节点误以为信道空闲。
- **CSMA/CD**：发送时检测碰撞，检测到就停止。适合有线以太网，不适合典型无线，因为无线节点很难边发边听，也难以检测接收端碰撞。
- **CSMA/CA**：碰撞避免。802.11 中发送前等待 DIFS，执行随机 backoff；接收方用 ACK 确认；发送方超时未收到 ACK 则认为失败并重传。

## 6. 802.11 CSMA/CA 要点

- 按 PPT 简化流程，若节点检测到信道 **DIFS 空闲则发送** 整个数据帧；若信道忙，则等待并进入随机 backoff。
- 更完整的 802.11 DCF 机制会在竞争场景中使用随机 backoff：节点从 contention window 选计数，空闲时递减，忙时冻结，计数到 0 才发。
- 回退计时只在信道空闲时递减，信道忙则冻结。
- 计数到 0 后发送整个数据帧。
- 成功接收后，接收方短间隔 SIFS 后发送 ACK。
- 碰撞后增大竞争窗口，降低再次碰撞概率。
- DIFS 比 SIFS 长，保证正在进行的 ACK/CTS 等短控制响应优先于新一轮竞争；这也是 802.11 用时间间隔实现优先级的方式。
- 无线站点通常不能像有线以太网那样边发边检测碰撞，因为自身发射信号远强于接收信号，且发送端听到的信道状态不等于接收端状态。

## 7. 隐藏节点与暴露节点

- **隐藏节点 Hidden Node**：A 和 C 彼此听不到，但都能到达 B。A 听不到 C 的发送，可能同时向 B 发送，导致 B 处碰撞。
- **暴露节点 Exposed Node**：B 向 A 发送时，C 听到 B 以为信道忙，但 C 向 D 发送其实不会干扰 A 的接收，导致不必要等待。
- 这两个问题说明：无线的“我听到/没听到”不等价于接收端是否会被干扰。

## 8. RTS/CTS

- 发送方先发 RTS，说明希望占用介质的时间。
- 接收方回复 CTS，周围节点根据持续时间设置 NAV，暂时避免发送。
- RTS/CTS 主要缓解隐藏节点，因为隐藏在发送方旁边但能听到接收方 CTS 的节点会退避。
- 代价是额外控制帧开销；小包通常不值得使用。
- RTS/CTS 的关键不是“让所有人都听到 RTS”，而是让接收方附近的节点听到 CTS 后设置 NAV。隐藏节点通常听不到发送方，却可能听到接收方。
- exposed terminal 的判断规则是：如果一个节点 `hears RTS but does not hear CTS`，说明它听到的是发送端附近的请求，但不在接收端保护范围内，因此它 `may still transmit`。这就是 RTS/CTS 能部分缓解暴露终端的原因。
- 它不能消除所有问题：RTS/CTS 本身也可能碰撞，暴露节点仍可能过度退避，且管理/控制帧被伪造时会造成 DoS。

## 9. 考试重点

- 能分类比较 FDMA/TDMA/CDMA、ALOHA、CSMA/CA、轮询。
- 能说明纯 ALOHA 和时隙 ALOHA 的区别。
- 能解释为什么无线中使用 CSMA/CA 而不是 CSMA/CD。
- 能画出或文字描述 CSMA/CA 的 DIFS、backoff、SIFS、ACK 流程。
- 能用拓扑例子解释隐藏节点和暴露节点。
- 能说明 RTS/CTS 的作用、适用场景和开销。

## 10. 易混点

- **碰撞检测 vs 碰撞避免**：CD 是发生后检测并停止；CA 是发送前退避降低概率。
- **监听到空闲不保证接收端空闲**：隐藏节点问题的根源在接收端。
- **RTS/CTS 不能解决所有碰撞**：它减少隐藏节点碰撞，但引入控制开销，也可能受到控制帧丢失影响。

## 11. 快速自测

1. 为什么纯 ALOHA 的吞吐率低？
2. CSMA 为什么仍然可能碰撞？
3. 描述 802.11 节点从有包要发到收到 ACK 的过程。
4. 用 A、B、C 三个节点解释隐藏节点。
5. RTS/CTS 为什么对大数据帧更有价值？

<details class="self-test-answer">
<summary>参考答案</summary>

1. 纯 ALOHA 有包就发，不监听信道，任意两个帧只要时间重叠就会碰撞；负载升高后碰撞和随机重传会迅速吞掉吞吐。
2. CSMA 的监听发生在发送端，传播时延和隐藏节点会让两个节点都误以为信道空闲；即使发送端空闲，接收端也可能正在被干扰。
3. 按 PPT 简化流程：节点监听信道，DIFS 空闲则发送整个数据帧；若信道忙，则等待并进入随机 backoff。按 802.11 DCF 细节：竞争场景中从 contention window 选计数，计数只在空闲时递减，忙则冻结，计数到 0 发送；接收方成功后等待 SIFS 返回 ACK。
4. A 和 C 彼此听不到，但都能到达 B。A 听不到 C 就可能向 B 发，C 也可能同时向 B 发，两个信号在 B 处碰撞。
5. RTS/CTS 增加控制开销，小包用它不划算；大数据帧一旦碰撞损失更大，先用短 RTS/CTS 预约信道能降低大帧碰撞成本。

</details>

## 公式与术语速查

| 英文/缩写 | 中文含义 | 初学者要会的解释 |
|---|---|---|
| MAC | Medium Access Control，介质访问控制 | 决定多个节点如何共享同一无线信道，核心问题是“谁什么时候可以发”。 |
| R bps / R/M bps | 信道总速率/平均共享速率 | 理想 MAC 中，一个用户独占时可用 `R bps`；`M` 个活跃用户共享时，每人平均 `R/M bps`。 |
| ALOHA | 随机接入协议 | 有数据就发，碰撞后随机重传；简单但碰撞多，纯 ALOHA 最高吞吐约 18%。 |
| CSMA | Carrier Sense Multiple Access | 发送前先听信道；发送端听到空闲不代表接收端一定空闲。 |
| CSMA/CD | Collision Detection | 边发边检测碰撞，适合有线以太网；无线中自身发射太强，通常不能边发边听。 |
| CSMA/CA | Collision Avoidance | 碰撞避免，802.11 通过 CCA、DIFS、随机 backoff、SIFS/ACK 降低碰撞概率。 |
| DIFS | Distributed Inter-frame Spacing | 发送新数据前需等待的较长帧间间隔；PPT 简化流程是 **DIFS 空闲则发送**。 |
| SIFS | Short Inter-frame Spacing | ACK/CTS 等立即响应使用的较短间隔，短于 DIFS，因此优先级更高。 |
| RTS/CTS | Request to Send / Clear to Send | 发送方请求发送、接收方允许发送；让接收方附近节点设置 NAV，缓解 hidden terminal problem。 |
| NAV | Network Allocation Vector | 虚拟载波监听计时器，节点听到 RTS/CTS 后按持续时间暂不发送。 |
| hidden terminal problem | 隐藏终端问题 | 两个发送端彼此听不到，却都能到达同一接收端，导致在接收端碰撞。 |
| exposed terminal problem | 暴露终端问题 | 节点误以为发送会干扰别人，实际不会干扰，导致不必要等待和吞吐下降。 |

拓扑图读法：

```text
Hidden terminal:
A  --->  B  <---  C
A 和 C 彼此听不到，但 B 能听到二者；A、C 同时发会在 B 处碰撞。

RTS/CTS solution:
A --RTS--> B --CTS--> 周围节点
听到 CTS 的 C 知道 B 正要接收，于是设置 NAV 并等待。
```

```text
Exposed terminal:
A  <---  B      C  --->  D
C 听到 B 在发，以为信道忙；但 C 发给 D 不会影响 A 接收 B，等待反而浪费。
```

PPT 细节补充：

- `Taking-turns MAC protocols` 是“轮流使用信道”的 MAC 思路，代表是 `Polling` 和 `Token passing`。它们比随机接入更少碰撞，但需要管理开销，节点失效时也要处理恢复。
- `Polling`：中心控制节点依次询问各从节点是否有数据。优点是不会像 ALOHA 那样乱撞，缺点是中心点可能成为单点故障，轮询消息也消耗时间。
- `Token passing`：网络中只有拿到 token 的节点能发送。优点是公平、可控，缺点是 token 丢失、节点故障和维护顺序会带来复杂性。
- ALOHA 的碰撞窗口和传播时延有关。纯 ALOHA 只要另一帧在本帧前后一个帧时内开始发送就可能碰撞，因此最大吞吐约 18%；Slotted ALOHA 把发送对齐到时隙，减少一半脆弱期，最大吞吐约 37%。
- CSMA/CD 需要在发送时还能检测碰撞，因此最短帧发送时间必须 `>= 2 * maximum propagation delay`。这里的 `maximum propagation delay` 是网络中最远两端信号单程传播最长时间；两倍是因为发送端要等碰撞信号从远端返回。
- 无线网络通常不用 CSMA/CD 的原因不是“不需要检测”，而是物理上很难：自己的发射功率远大于远端信号，边发边听会被自身信号淹没。
- QoS 是 Quality of Service，表示时延、抖动、丢包率、吞吐等服务质量要求。语音/视频比普通下载更怕时延和抖动。
- Cable Modem 场景也会考 MAC：上行多个用户共享信道，不能让所有 modem 同时乱发，需要预约、授权或轮询式调度。

## 历年卷风格练习

1. Use illustration to explain what is the hidden terminal problem in the wireless network. How can it be solved?
2. 按 PPT 简化流程说明 CSMA/CA 中发送方在 DIFS 空闲、信道繁忙、未收到 ACK 三种情况下分别做什么。
3. 比较 hidden terminal problem 和 exposed terminal problem：一个主要造成什么损失，另一个主要造成什么损失？
4. 为什么 RTS/CTS 对大帧更有价值，而对小帧不一定划算？

<details class="self-test-answer">
<summary>参考答案</summary>

1. 图示可写 `A -> B <- C`，其中 A 和 C 彼此在通信范围外，但都能到达 B。A 听不到 C，可能在 C 正向 B 发送时也向 B 发送，两个信号在 B 处碰撞。解决方法是 RTS/CTS：A 先向 B 发 RTS，B 回 CTS，听到 CTS 的 C 知道接收端 B 将忙，设置 NAV 并暂缓发送。
2. 若持续 DIFS 检测到信道空闲，按 PPT 简化流程发送整个数据帧；若信道忙，等待并进入随机 backoff，信道空闲时倒计时、忙时冻结；若发送后没有收到 ACK，则认为失败，扩大竞争窗口后重试。
3. Hidden terminal problem 的主要损失是接收端碰撞和重传；exposed terminal problem 的主要损失是不必要等待，降低空间复用和吞吐。
4. RTS/CTS 本身需要额外控制帧。小帧直接发送即使碰撞损失也小；大帧碰撞代价高，先用短 RTS/CTS 预约信道更划算。

</details>
