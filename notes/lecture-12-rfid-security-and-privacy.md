---
title: "Lecture 12: RFID Security and Privacy"
source: "materials/Lecture 12 RFID Security and Privacy.pptx"
order: 12
---

# Lecture 12: RFID Security and Privacy

## 零基础导读

RFID 一次读取可以这样想：reader 先产生射频场，无源 tag 从场中取能；tag 不主动发强信号，而是通过负载调制或反向散射 backscatter 改变天线反射特性，把自己的 ID 或数据“映回去”。低频/高频系统常用电感耦合，UHF 系统更像雷达式反向散射。Reader/Interrogator 负责供能、发命令、收响应、防冲突和连接后台数据库；tag/transponder 负责存储少量 ID/数据并按协议响应。

多个 tag 同时响应会冲突，所以需要防冲突协议。FSA 的直觉是把一轮分成多个 slot，每个 tag 随机选一个 slot 回答；slot 可能为空、单个 tag 成功、多个 tag 冲突。Q algorithm 根据空 slot 和冲突 slot 调整帧长：tag 多就加大 Q，tag 少就减小。二进制树协议则按 ID 前缀分裂集合，比如 4 个标签 ID 分别以 0、10、110、111 开头，reader 先问前缀 0，再问 1，再继续把 11 分成 110 和 111，直到每次只剩一个 tag。

RFID 安全有两个方向：隐私是防坏 reader 偷偷读好 tag，认证是防坏 tag 骗好 reader。HB/HB+ 是给低成本 tag 的轻量认证。HB 用 secret vector 和随机 challenge 做 dot product，再 XOR 一个 noise bit；LPN 难题说，带噪声的线性方程很难解。主动攻击者如果反复发特殊查询，可用多数投票恢复秘密位；HB+ 加 blinding value 和额外秘密来抵抗这种主动攻击。物理层研究如 GenePrint、Hu-Fu、RF-Mehndi、RF-Cloak 则利用硬件指纹、耦合、用户触摸或 reader 随机波形来增强安全。

从 reader 侧看，RFID 系统不是一根天线那么简单。射频模块负责载波产生、功率放大、收发切换、调制/解调和信号检测；基带控制模块负责协议时序、编码/解码、防冲突、命令状态机、认证、加密/解密和与上位机通信。后台应用再把 EPC/UID 映射到库存、门禁、票务或审计记录。考试问“RFID 系统功能”时，可以按 reader 供能与查询、tag 存储与响应、antenna 耦合与辐射、middleware/database 解释业务含义来答。

## 本章知识地图

1. **一次读取流程**：reader 供能 -> tag 被激活 -> 负载调制/反向散射 -> reader 解调 -> 后台数据库解释 ID。
2. **硬件和频段**：LF/HF 常见 inductive coupling，UHF 常见 backscatter；AM/FSK/PSK 是可能的调制方式。
3. **防冲突**：ALOHA/FSA/Q algorithm 用 slot 解决随机碰撞；二进制树用 ID 前缀逐步分裂。
4. **隐私 vs 认证**：隐私防非法 reader 读 tag，认证防伪 tag 骗 reader，攻击方向相反。
5. **Reader 架构**：射频模块负责空中信号，基带控制模块负责编码/解码、防冲突、认证和加密/解密，后台数据库负责业务解释。
6. **HB/LPN**：parity、XOR、dot product、noise 让低成本 tag 不用公钥也能认证；HB+ 修补主动攻击。

## 初学者常见疑问

问：为什么 RFID tag 难以直接使用传统公钥密码？

答：很多 RFID tag 是廉价无源标签，没有电池，只靠 reader 的场取能；芯片面积、门数、存储、时钟和通信时间都很有限。公钥密码需要较大计算和存储，成本和能耗都不适合低端 tag，所以课件才会讲 HB/HB+、物理层指纹和 RF-Cloak 这类轻量或 reader 侧方案。

问：用 4 个标签如何理解 FSA 和二进制树？

答：FSA 中 4 个标签各自随机选 slot，可能出现两个标签选同一 slot 导致冲突，下一帧再试；Q algorithm 会根据冲突多不多调 slot 数。二进制树则不随机选 slot，而是 reader 问“ID 以 0 开头的回应”，再问“以 1 开头的回应”，如果 1 下面仍冲突，就继续问 10、11，直到每个前缀只匹配一个标签。

问：RF-Cloak 为什么像 one-time pad？

答：RF-Cloak 的随机波形由 reader 产生，合法 reader 知道或能抵消这部分随机性，窃听者看到的 tag 响应被随机波形掩盖。对窃听者来说，随机波形像空中的一次性掩码；对 MIMO 窃听者，还可用天线运动和快速天线切换制造变化信道，让其难以消除随机项。

## 1. 本章速览

RFID 用无线方式给物体分配并读取身份，是“下一代条码”的基础技术。本章分两部分：前半讲 RFID 系统结构、标签能力和防冲突协议；后半讲 RFID 隐私、认证、HB/HB+、物理层指纹、Hu-Fu、RF-Mehndi、RF-Cloak 等安全研究。考试重点是理解低成本标签为什么难以直接使用传统密码学，以及 RFID 的隐私威胁为什么来自“可被偷偷扫描和长期跟踪”。

## 2. RFID 基础

- **RFID tag**：通常由芯片 IC 和天线组成。
- **Reader/Interrogator**：读取或写入标签信息，为无源标签供能，并与后台应用通信。
- **Antenna**：完成射频能量和信号收发。
- RFID 的核心用途是给物体分配 ID，并把 ID 关联到数据库中的更多信息。
- 典型应用：供应链、护照、药品防伪、图书馆、宠物、门禁、收费、行李追踪。
- **系统功能**：reader 负责发起查询、供能、调制/解调和防冲突协调；tag 负责存储 ID/数据并按协议响应；后台数据库负责把 ID 映射为业务含义、权限和审计记录。
- **Reader 内部功能**：射频模块负责产生载波、调制、接收和解调；基带控制模块负责协议控制、编码/解码、anti-collision、防冲突调度、认证、加密/解密和接口控制。
- **Reader 系统功能补充**：PPT 还强调 reader 要具备 `self-organizing networking ability`，能和其他 reader/网关组成现场网络；要有 `multi-antenna management`，在多天线间选择、切换或协调覆盖；要提供 `middleware interface`，把底层 tag 事件交给上层过滤和业务处理；还要支持 `peripheral connection`，例如连接显示器、蜂鸣器、门禁控制器、传感器或本地控制器；安全上要考虑 `reader/application-layer communication security`，防止 reader 到应用服务器之间的数据被窃听、篡改或伪造。
- **IoT 层次定位**：RFID 通常属于感知层，因为它直接完成对象识别和数据采集，再把结果交给网络层、管理层和应用层。

## 3. RFID 相对条码的特点

- 不需要严格视距，可通过无线读取。
- 可唯一标识单个物品，而条码通常只标识类型。
- 可快速、自动、批量扫描。
- 可作为数据库指针，连接更丰富的对象信息。
- 风险也更大：远距离或隐蔽读取会带来跟踪和隐私泄露。

## 4. RFID 硬件与耦合方式

- **低频/高频 RFID**：常使用磁场/电感耦合，阅读距离较短。
- **超高频 UHF RFID**：常使用电磁反向散射耦合，类似雷达，距离更远。
- 阅读器射频模块负责产生高频能量、激活无源标签、调制发送信号、接收并解调标签响应。
- 标签资源受限：内存小、计算能力弱、门数少、通常只有静态 ID 或少量可写数据。

## 5. 标签类型与数据传输

- **Read Only**：出厂写入，通常不可改。
- **Read/Write**：有板载存储，可改数据或 ID。
- 调制方式包括 AM、FSK、PSK。
- PSK 通过相位变化编码，速率较高、抗噪较好，但读写器实现更复杂。

## 6. RFID 防冲突问题

多个标签同时响应会冲突，标签又没有复杂冲突检测能力，因此主要由 reader 协调。

- **读写器冲突**：多个 reader 之间互相干扰，可用 CSMA、TDMA、频分等思路。
- **标签冲突**：多个标签同时回传，常用 ALOHA 类或二进制树类协议。

## 7. ALOHA 类防冲突协议

- **纯 ALOHA**：标签随机响应，简单但信道利用率约 18.4%。
- **时隙 ALOHA**：把时间划分为时隙，标签在时隙中响应，提高效率但需要同步。
- **帧时隙 ALOHA FSA**：一帧包含多个时隙，标签随机选择一个时隙响应。
- FSA 时隙结果分为：空时隙、单时隙、冲突时隙。
- FSA 优点是逻辑简单、电路简单、内存少；缺点是固定帧长不能适应动态标签数量。
- **动态帧长/Q 算法**：根据空时隙和冲突时隙情况调整帧长，标签多时增大帧，标签少时减小帧。
- **ALOHA starvation**：随机选择 slot 可能让某些标签长期碰撞或长期没有成功响应，出现“饿死”现象；动态帧长能缓解但不能从根本上保证每个标签立刻成功。

## 8. 二进制树类防冲突协议

- 基本思想：递归地把冲突标签集合分成两个子集，直到每个集合只剩一个标签。
- **查询二进制树**：reader 广播前缀，匹配前缀的标签响应。标签无状态，只需比较自己的 ID 前缀。
- **随机二进制树**：标签维护计数器，冲突后随机分裂，逐步减少同时响应数量。
- 树协议通常识别确定性更强，但交互轮数和传输复杂度可能较高。
- `random binary tree counter` 的直觉：counter 为 0 的标签响应；若发生冲突，参与冲突的标签随机把 counter 设为 0 或 1，未参与的标签按协议递增/等待；reader 不断查询 counter 为 0 的集合，直到每次只剩一个标签成功。
- PPT 性能表可按 `FSA/random tree/query tree` 记忆：FSA 依赖帧长和随机 slot，random tree 依赖随机分裂和标签状态，query tree 依赖 reader 前缀查询且标签无状态。答题时可从内存需求、是否 starvation、通信轮数和是否需要同步比较。
- 性能表变量：`n = number of tags` in recognition area，`k = tag ID length`，`t` = one frame time，`s` = number of frames，`N = estimate of n`。
- FSA 复杂度：时间上界可写 `t × s + tag-estimation time`，传输上界 `n × s`；标签侧通常需要可写 `8/16-bit` slot counter。
- Random binary tree：时间复杂度 `O(n)`；传输最坏情况在 `n` 未知时为 `θ(nlogn)`，在 `n` 已知时为 `θ(n)`；标签也需要可写 `8/16-bit` counter。
- Query binary tree：平均时间 `O(n)`；最坏时间可写 `n × (k + 2 - log n)`；最坏传输可写 `k × (2.21 log n + 4.19)`；优点是 tag 无状态，不需要可写 tag memory。

## 9. RFID 隐私与安全问题

- 标签高度移动，可能携带个人信息。
- 可被暗中扫描，用户通常不知道何时被读取。
- 低成本标签缺少强密码能力，访问控制和数据隐私难实现。
- **消费者隐私问题**：购物标签与信用卡身份绑定后，可推断财产、偏好、活动位置。
- **跟踪问题**：即使 ID 本身无语义，固定 ID 也能跨地点追踪同一人。
- **企业风险**：仓库传输可被窃听，货架周转率可被竞争对手扫描，标签可被伪造或替换。

## 10. 隐私保护方案

- **Kill 标签**：售后输入密码使标签永久失效。隐私强，但失去售后服务、退换货、智能应用价值。
- **重命名标签**：标签 ID 随时间改变，减少长期跟踪；需要系统能重新关联旧信息。
- **距离测量/距离作为信任**：远距离只释放泛化信息，近距离才释放唯一 ID。
- **政策和法律**：帮助规范部署，但不能阻止任意 reader 私下读取。

## 11. HB 与 HB+ 协议

- HB 目标：低成本标签向 reader 认证。
- 安全基础：LPN Learning Parity with Noise，带噪声的线性奇偶学习问题很难。
- HB 中标签计算类似 `a · x XOR noise` 的响应。
- **HB 弱点**：主动攻击者可反复发送非随机查询，利用多数投票恢复秘密位。
- **HB+**：改进 HB，加入额外随机性和双秘密，提升对主动攻击的抵抗能力。
- **PPT 参数写法**：噪声位 `v=1 with probability η`，reader 和 tag `repeat r times`。认证判决不是要求全对，而是如果错误响应 `fewer than ηr` 就接受，因为合法 tag 也会按概率 η 故意加入噪声。
- **主动攻击细节**：攻击者使用 `repeated non-random challenges`，例如固定某些 challenge 位反复询问；由于噪声只是概率性翻转，多次采样后可用 `majority vote` 估计真实内积结果，从而逐位 recover secret bits。HB+ 用第二个随机 challenge 和 blinding secret 减少这种固定查询多数投票攻击。

## 12. 物理层认证研究

- **GenePrint**：利用 UHF RFID 标签模拟硬件微小差异形成物理层指纹；典型流程是让 tag 回复 RN16 等短随机数，reader 从响应中提取信道和硬件特征，去除环境噪声后用协方差等统计特征判断是否来自同一标签。目标是兼容现有协议、无需定制标签、高准确率。
- **Hu-Fu**：面向重放弹性的 RFID 认证，通过双标签/相邻标签耦合和随机信号保护特征。两个 tag 靠近时会互相影响天线响应，攻击者重放单个旧响应或做补偿攻击，很难同时复现耦合关系和随机挑战对应的特征。
- **RF-Mehndi**：把设备特征与用户生物特征结合。用户手指触摸标签阵列会改变相位差，形成用户相关且独特的指纹；论文中用 PDoT 等相位差特征描述触摸造成的相位偏移。戒指、手链等 jewelry/accessory 会改变耦合和相位，因此系统需要把佩戴状态作为影响因素处理。
- **RF-Cloak**：通过随机化 reader 信号，像空中一次性掩码一样保护 RFID 通信，抵抗单天线甚至 MIMO 窃听。合法 reader 知道自己发出的随机波形，可以抵消后读出 tag 响应；窃听者不知道随机项，即使用 MIMO adversary 多天线观察，也会被天线运动、快速切换和变化信道破坏抵消条件。
- **RF-Cloak 的答题重点**：随机波形由 reader 侧产生，对合法 reader 可抵消或已知，对窃听者像一次性 pad；对 MIMO 窃听者，还可用天线运动和快速天线切换制造快速变化信道，目标是在不改廉价 tag 的情况下保护空中响应。

## 13. 考试重点

- 能说明 RFID 系统三组件：reader、tag、antenna。
- 能比较 RFID 与条码在读取方式、唯一性、自动化和隐私风险上的差异。
- 能解释标签冲突和 reader 冲突。
- 能比较 ALOHA/FSA/Q 算法与二进制树算法。
- 能说明固定标签 ID 如何导致跟踪隐私问题。
- 能评价 kill、renaming、distance、policy 四类隐私方案的优缺点。
- 能解释 HB 基于 LPN，为什么主动攻击会破坏 HB，HB+ 改进方向是什么。
- 能说出物理层指纹认证的核心思想：利用硬件不可避免的模拟差异。

## 14. 易混点

- **认证问题和隐私问题方向不同**：隐私是防止坏 reader 读取好标签；认证是防止坏标签骗过好 reader。
- **无意义 ID 仍可跟踪**：只要 ID 稳定，就能关联同一对象。
- **kill 标签不是万能方案**：保护隐私但牺牲后续功能。
- **物理层指纹不是传统密钥**：它依赖硬件特征和信号处理。

## 15. 快速自测

1. 为什么低成本 RFID 标签难以部署传统公钥密码？
2. FSA 中空时隙、单时隙、冲突时隙分别意味着什么？
3. 查询二进制树为什么说标签是无状态的？
4. 固定 RFID ID 如何导致消费者被跟踪？
5. HB 协议为什么需要加入噪声？

<details class="self-test-answer">
<summary>参考答案</summary>

1. 廉价无源标签门数、存储、能量和时钟都很有限，主要靠 reader 供能，难以承受公钥密码的大整数运算、长密钥存储和长交互延迟。
2. 空时隙表示没有标签选择该 slot；单时隙表示恰好一个标签响应，可成功识别；冲突时隙表示多个标签同时响应，reader 不能正确解码。
3. Reader 广播前缀，标签只比较自己的 ID 是否匹配并响应，不需要记住协议历史状态或维护复杂计数器，因此称为无状态。
4. 固定 ID 即使没有语义，也能在商店、街道、门禁等不同 reader 处被关联，推断同一个人携带同一物品的移动轨迹和消费习惯。
5. HB 基于带噪声线性奇偶问题 LPN；加入噪声让攻击者不能通过简单线性方程直接解出秘密，提高被动学习难度。

</details>

## 公式与术语速查

| 英文/缩写 | 中文含义 | 初学者要会的解释 |
|---|---|---|
| RFID | Radio Frequency Identification | 射频识别，用 reader 无线读取 tag 的 ID 或数据。 |
| Reader / Interrogator | 读写器/询问器 | 产生射频场、给无源 tag 供能、发命令、收响应、防冲突并连接后台。 |
| Tag / Transponder | 标签/应答器 | 存储 ID 或少量数据，按协议响应 reader。 |
| LF/HF/UHF | 低频/高频/超高频 | 不同频段对应不同耦合方式、距离、速率和应用。 |
| Load modulation | 负载调制 | Tag 改变天线负载，让 reader 看到反射变化，常见于近场系统。 |
| Backscatter | 反向散射 | UHF tag 改变反射特性，把 reader 的射频能量“映回去”。 |
| FSA | Frame Slotted ALOHA | 一帧多个 slot，tag 随机选 slot，空/单/冲突三种结果。 |
| Q algorithm | 动态帧长算法 | 根据空 slot 和冲突 slot 调整帧长，适应 tag 数量变化。 |
| LPN | Learning Parity with Noise | 带噪声线性奇偶学习问题，HB/HB+ 的安全基础。 |
| dot product | 点积/内积 | HB 中 challenge 向量和 secret 向量逐位相乘再异或求和。 |
| RN16 | 16-bit random number | EPC/UHF 交互中的短随机数，物理层指纹研究可利用其响应。 |
| PDoT | Phase Difference of Tags | RF-Mehndi 中用于描述标签阵列相位差的特征。 |

HB/HB+ 公式直觉：

- HB 响应：`z = a · x XOR noise`，其中 `a` 是随机 challenge，`x` 是 secret，`noise` 是少量随机错误。
- 没有 noise 时，多组线性方程可解出 `x`；有 noise 后变成 LPN，低成本 tag 可用简单 XOR，但攻击者很难可靠求解。
- HB+ 增加 blinding value 和第二个 secret，防主动攻击者用固定查询多数投票恢复秘密位。

PPT 细节补充：

- Reader 硬件可拆成天线、`Transceiver`、控制器和 `middleware`。middleware 负责把底层读到的 tag 事件清洗、过滤、聚合并交给后端业务系统。
- RFID 频段：LF 常见 `125kHz`/134 kHz，HF 是 13.56 MHz，UHF 是 860-960 MHz，`SHF` 是 Super High Frequency，可用于更高频/更远或特殊场景。
- Reader 射频链路里的 `high-frequency interface module` 包含发射、接收、调制/解调等功能；`local oscillator` 提供本振；`mixer` 用于变频；`circulator` 帮助同一天线收发隔离；`I-Q output` 给出同相/正交两路基带信号，便于解调相位和幅度。
- `Pure ALOHA utilization 18.4%` 是纯 ALOHA 最大利用率约 1/(2e) 的结果；时隙 ALOHA 约 36.8%，FSA/Q algorithm 继续根据标签数量调帧长。
- HB 协议常写响应为 `(a · x) ⊕ v`，其中 `v` 是噪声位。HB+ 引入第二组 challenge/secret，可写成 `(a · x) ⊕ (b · y) ⊕ v`。
- EPC Gen2 Q algorithm 中 `Qfp` 是浮点形式的 Q 估计值，用于根据空 slot/冲突 slot 调整下一帧长度。参数 `C=0.1-0.5` 可理解为调整步长，冲突多就增大 Q，空 slot 多就减小 Q。
- RFID 保护方法按能力分层：低成本 tag 用随机化 ID、kill/sleep、访问密码、HB/HB+；较强 tag 可用 AES/3DES challenge-response；系统侧用 reader 认证、后端授权、日志审计和物理距离控制。

## 历年卷风格练习

1. RFID 在 IoT 哪一层？RFID 系统由哪些功能模块组成？
2. 用 4 个标签说明 FSA 和二进制树防冲突的区别。
3. 为什么适合低成本 RFID 的认证算法常选择 HB/HB+ 这类轻量方案，而不是传统公钥密码？
4. RFID tag 和 reader 之间传递敏感信息被窃听时，可以采取哪些保护措施？

<details class="self-test-answer">
<summary>参考答案</summary>

1. RFID 通常属于感知层。系统包括 reader/interrogator、tag/transponder、antenna 和后台数据库；reader 内部可分射频模块与基带控制模块，负责供能、调制/解调、编码/解码、防冲突、认证、加密/解密和业务接口。
2. FSA 中 4 个 tag 随机选 slot，可能空、成功或冲突，冲突后下一帧重试；二进制树按 ID 前缀递归查询，把冲突集合拆成更小集合直到每次只剩一个 tag。
3. 低成本无源 tag 能量、门数、存储和时钟都有限，难以承受 RSA/ECC 等公钥运算。HB/HB+ 主要用 XOR、点积和少量随机数，更适合廉价标签。
4. 可用距离限制、kill/renaming、随机 ID、challenge-response 认证、轻量加密/MAC、RF-Cloak 随机波形、后端访问控制和审计。若标签能力太弱，可把复杂安全逻辑放在 reader/后端。

</details>
