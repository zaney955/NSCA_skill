# NSCA Strength & Conditioning Skills

这是一组面向力量与体能训练实践的 Codex skills，基于 NSCA 体系与《Essentials of Strength Training and Conditioning》的核心思想整理而成。它的目的不是复述教材，而是把一本厚重的专业书浓缩成可执行的工作流：帮助你做训练计划、测试评估、动作教学、体能训练、恢复管理和运动表现营养框架。

## 为什么选择 NSCA

NSCA，全称 National Strength and Conditioning Association，是力量与体能训练领域最具影响力的专业组织之一。它长期服务于运动表现提升、体能训练教育、认证体系和实践标准建设。许多教练熟悉的 CSCS，也就是 Certified Strength and Conditioning Specialist，正是 NSCA 的代表性认证之一。

《Essentials of Strength Training and Conditioning》是 CSCS 备考和力量体能专业学习中的核心教材。它覆盖人体系统、运动生物力学、能量系统、训练适应、测试评估、动作技术、抗阻训练设计、增强式训练、速度敏捷、有氧耐力、周期化、康复再训练、恢复、营养、设施管理等内容。原著的价值在于它不是单纯讲训练动作，而是把运动科学、测试逻辑、计划设计和安全边界连接在一起。

这套 skills 的设计思路，就是把原著中最有操作价值的部分拆成多个可触发的专业任务模块。

## 这套 Skills 如何浓缩原著精华

原著很完整，但也很厚。日常使用时，你通常并不需要重新阅读整章内容，而是需要解决具体问题：

- 这个运动员现在应该练力量、爆发力，还是维持？
- 这套测试 battery 是否合理？
- 深蹲技术问题该怎么 cue？
- 增强式训练怎么进阶才安全？
- 运动员最近疲劳堆积，训练该怎么调整？
- 比赛日前后应该如何安排一般性补给和补水？

因此，这套 skills 没有把书做成“资料摘抄库”，而是拆成三层：

1. `SKILL.md`：告诉 agent 何时触发、如何工作、边界在哪里。
2. `references/`：保存决策规则、分类框架、判断逻辑，而不是普通读书笔记。
3. `assets/templates/` 和 `scripts/`：提供可直接复用的输出结构和确定性计算工具。

换句话说，它不是让 agent 背书，而是让 agent 像一个受过 NSCA 体系训练的助理一样工作。

## 适合谁使用

这套 skills 适合多类使用者。

**体能教练和运动队教练**  
可以用它做 needs analysis、训练周期设计、测试 battery、动作 cue、恢复监控和训练调整。

**个人教练和健身教练**  
可以用它把训练计划写得更有逻辑，尤其是在动作教学、负荷安排、训练进阶和风险边界上。

**运动员**  
可以用它理解自己的训练目标、测试结果、恢复状态和训练阶段。不过涉及疼痛、伤病、营养治疗或补剂合规时，应咨询合格专业人士。

**健身爱好者**  
可以用它学习如何更系统地训练，而不是只堆动作。比如如何安排力量、爆发力、有氧和恢复。

**健身房老板、训练中心负责人**  
可以扩展使用 `nsca-facility-admin` 方向的思路，用于设施布局、安全流程、场馆规则和应急预案。不过本当前目录主要包含训练和表现相关 skills。

**学习 CSCS 或体能训练理论的人**  
可以用它把教材知识转化成案例练习，尤其适合用“给定运动员背景，输出训练方案/测试方案/技术检查”的方式学习。

## 当前包含的 Skills

### 1. `nsca-program-design`

用于抗阻训练设计、needs analysis、训练变量配置和周期化计划。

适合任务：

- 设计力量训练计划
- 制作 offseason、preseason、in-season 或 postseason 方案
- 根据 1RM、RPE 或训练状态安排负荷
- 设计 microcycle、mesocycle、annual plan
- 分析运动项目需求和运动员训练重点

高质量使用方式：

```text
使用 nsca-program-design。

运动员：20 岁女性，大学篮球中锋，训练年龄 3 年
赛季：in-season，每周 2 场比赛，2 次力量训练
目标：维持最大力量和爆发力，同时减少疲劳
数据：深蹲 1RM 120kg，卧推 1RM 70kg
限制：每次 45 分钟，无伤病，设备完整

请输出：
1. 简短 needs analysis
2. 4 周 microcycle 计划
3. 每次训练的动作、组数、次数、负荷、休息
4. 进阶和降阶规则
5. 监控指标
```

如果没有 1RM，可以这样说：

```text
使用 nsca-program-design。
没有 1RM 数据，请用 RPE/RIR 保守设计一名初级足球运动员的 6 周基础力量计划。
```

### 2. `nsca-athlete-testing`

用于运动员测试选择、测试顺序、测试执行标准、成绩解释和 athlete profile。

适合任务：

- 设计 preseason 测试 battery
- 安排测试日流程
- 解释力量、速度、跳跃、敏捷、有氧测试结果
- 生成运动员 profile
- 做队内排名、T-score、relative strength 等基础分析

高质量使用方式：

```text
使用 nsca-athlete-testing。

对象：高中男子足球队，18 人
目的：preseason baseline，帮助制定训练重点
设备：杠铃、跳箱、卷尺、电子计时门、操场
时间：90 分钟
测试方向：力量、爆发力、速度、变向、有氧能力

请输出：
1. 推荐 test battery
2. 测试顺序和理由
3. 每项测试的记录指标
4. 安全注意事项
5. 如何把结果转化成训练重点
```

解释成绩时可以这样问：

```text
使用 nsca-athlete-testing。
以下是 10 名运动员的 10m、40m、垂直跳和深蹲 1RM 数据。
请帮我生成 athlete profile，并指出每个人最优先改善的体能品质。
```

### 3. `nsca-exercise-technique`

用于动作技术教学、常见错误分析、coaching cues、spotting 和 warm-up/mobility 技术。

适合任务：

- 写深蹲、卧推、硬拉、划船、推举等动作 checklist
- 分析动作错误
- 给出 cue、回归和进阶
- 判断某动作是否需要 spotter
- 设计热身和灵活性流程

高质量使用方式：

```text
使用 nsca-exercise-technique。

动作：卧推
对象：中级训练者
目标：提高力量，同时保证安全
问题：下降时肩部不稳定，推起时左右不均
限制：无疼痛，有一名 spotter

请输出：
1. setup checklist
2. 执行步骤
3. 常见错误和修正
4. coaching cues
5. spotting 方法
6. 下次训练的技术练习安排
```

如果涉及疼痛，请这样提供信息：

```text
使用 nsca-exercise-technique。
运动员深蹲时出现膝痛。请不要给医疗诊断，只帮我列出应停止训练的情况、需要转介的问题，以及在获得医疗许可前可以如何记录动作观察。
```

### 4. `nsca-conditioning`

用于增强式训练、速度训练、变向和敏捷训练、有氧耐力与代谢训练。

适合任务：

- 设计 plyometric progression
- 设计 sprint acceleration 或 maximal velocity 训练
- 设计 COD/agility session
- 设计 aerobic endurance 或 metabolic conditioning block
- 把 conditioning 和力量训练整合到一周中

高质量使用方式：

```text
使用 nsca-conditioning。

运动员：排球运动员，训练年龄 2 年
目标：提升垂直爆发力和落地质量
周期：6 周，每周 2 次
限制：无伤病，室内木地板，可用跳箱和药球
当前训练：每周 3 次力量训练，2 次专项训练

请输出：
1. 6 周增强式训练进阶
2. 每次训练的 drills、组数、次数或 foot contacts
3. 强度进阶逻辑
4. 落地技术 cue
5. 与力量训练的周安排建议
```

速度敏捷可以这样问：

```text
使用 nsca-conditioning。
给一名足球边锋设计 4 周 speed + COD block，重点是前 10m 加速和 45-90 度变向。
请安排每周 2 次，包含 warm-up、主训练、休息时间、监控和降阶规则。
```

### 5. `nsca-recovery-reconditioning`

用于恢复监控、overreaching/overtraining 风险审查、训练调整和医疗许可后的 reconditioning。

适合任务：

- 判断训练疲劳风险
- 设计 readiness 或 recovery monitoring 表
- 给表现下降的运动员做训练调整建议
- 根据医疗团队给出的禁忌和允许活动，设计 reconditioning 框架
- 生成 rehab referral summary 或 return-to-training constraints

高质量使用方式：

```text
使用 nsca-recovery-reconditioning。

运动员：大学短跑运动员
情况：最近 2 周训练量增加，睡眠下降，RPE 升高，30m 成绩连续变慢
无急性疼痛，无伤病诊断
目标：判断是否需要 deload，并给出一周恢复调整方案

请输出：
1. 风险等级，不要做医学诊断
2. 可能原因
3. 本周训练调整
4. 恢复优先级
5. 监控指标
6. 需要转介的情况
```

伤后再训练必须这样提供边界：

```text
使用 nsca-recovery-reconditioning。

运动员 ACL 术后，已经获得队医许可进入后期 reconditioning。
允许活动：固定自行车、上肢力量、低负荷下肢闭链训练
禁忌：跑步、跳跃、深膝屈曲、开放链腿伸
目标：设计 4 周训练框架，不要做 return-to-play clearance。
```

### 6. `nsca-nutrition-performance`

用于一般运动表现营养教育、训练日补给、比赛日 fueling、hydration 和 supplement risk checklist。

适合任务：

- 设计比赛日前、中、后的补给框架
- 给训练日做一般碳水、蛋白、脂肪和补水建议
- 生成 hydration plan
- 做 supplement risk checklist
- 帮助识别需要注册营养师或医生介入的情况

不适合任务：

- 饮食障碍或 RED-S 治疗
- 医疗营养治疗
- 极端减重或快速降体重
- 判断补剂是否合法、是否不含禁药
- 为未成年人做减重计划

高质量使用方式：

```text
使用 nsca-nutrition-performance。

运动员：70kg 男性耐力跑者
比赛：半程马拉松，预计 1 小时 35 分
环境：温暖，湿度中等
目标：比赛日前、中、后 fueling 和 hydration 框架
限制：不要医疗建议，不讨论补剂合法性

请输出：
1. 赛前 24 小时重点
2. 赛前 3-4 小时和 30-60 分钟策略
3. 比赛中补给和补水框架
4. 赛后恢复
5. GI tolerance 和监控建议
```

补剂问题应该这样问：

```text
使用 nsca-nutrition-performance。
运动员想使用某款 pre-workout。请不要判断它是否合法或绝对安全，只帮我做 supplement risk checklist，并列出需要问营养师、医生和赛事管理机构的问题。
```

## 如何让 Skills 发挥最大价值

最好的提示词通常包含以下信息：

```text
使用 [skill 名称]。

背景：
- 运动员：
- 项目/位置：
- 年龄和训练年龄：
- 当前赛季：
- 当前目标：
- 每周训练/比赛安排：
- 已有测试数据：
- 设备和时间限制：
- 伤病、疼痛、医疗禁忌：

请输出：
- 主要判断
- 具体计划或表格
- 进阶和降阶规则
- 监控指标
- 风险边界和需要转介的情况
```

更简单地说：不要只问“帮我做个训练计划”，而要告诉 agent “给谁、为什么、现在什么阶段、有什么数据、有什么限制、你希望输出什么格式”。

## 推荐工作流

如果你在做完整的运动员训练管理，可以按这个顺序使用：

1. `nsca-athlete-testing`：设计测试 battery，获得 baseline。
2. `nsca-program-design`：根据测试和项目需求设计力量训练计划。
3. `nsca-conditioning`：补充速度、增强式、有氧或代谢训练。
4. `nsca-exercise-technique`：为关键动作建立教学和纠错标准。
5. `nsca-recovery-reconditioning`：监控疲劳、恢复和训练调整。
6. `nsca-nutrition-performance`：提供一般表现营养和补水框架。

一个完整对话可以这样开始：

```text
我想为一支高中篮球队建立 preseason 体能训练系统。
请先使用 nsca-athlete-testing，帮我设计 baseline testing battery。
等测试方案完成后，再使用 nsca-program-design 和 nsca-conditioning 生成 8 周训练计划。
```

## 安全和专业边界

这套 skills 是训练决策辅助工具，不是医生、物理治疗师、注册营养师、律师或认证教练本人的替代品。

遇到以下情况，应优先咨询合格专业人士：

- 疼痛、急性伤病、术后训练、神经症状
- return-to-play 或医疗 clearance
- 热病、横纹肌溶解风险、胸痛、晕厥、异常呼吸困难
- 饮食障碍、RED-S、快速减重、未成年人减重
- 补剂安全性、禁药合规、药物相互作用
- 法律责任、设施合规或紧急预案的正式法律审查

正确的使用方式，是让 skills 帮你整理问题、生成计划、建立检查表、提醒风险边界，再由合格专业人员在现实环境中做最终判断。

## 一句话总结

这套 NSCA skills 的价值在于：把《Essentials of Strength Training and Conditioning》中最重要的训练科学、测试逻辑、动作安全、周期化、恢复和表现营养原则，转化成可对话、可复用、可执行的专业工作流。
