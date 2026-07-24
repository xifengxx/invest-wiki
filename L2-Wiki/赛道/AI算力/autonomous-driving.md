---
name: 自动驾驶
slug: autonomous-driving
industry: AI算力
layer: L3
tam_bn: 48.0
cagr_pct: 30.0
margin: 30-50%
cost_share_pct: 40
cost_share_context: 自动驾驶系统(芯片+传感器+软件+域控)占产业链总成本比例
profit_pool_pct: 45
profit_pool_context: 自动驾驶系统供应商(芯片+软件+传感器)占产业链利润池份额
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: Waymo(Alphabet)
    share: ~35%全球Robotaxi
    note: GOOGL 6城运营,2500台车,周45万+付费行程,2025年收入$1B+,估值$100-110B
  - name: NVIDIA
    share: ~50%全球AV芯片
    note: NVDA DRIVE Orin/Thor,30+车企采用,训练GPU~90%份额,Thor达2000 TOPS
  - name: Tesla
    share: 新兴Robotaxi颠覆者
    note: TSLA FSD v13端到端,Cybercab目标2026年4月,$0.40/英里,67-100亿英里训练数据
  - name: Qualcomm
    share: ~25%全球AV芯片
    note: QCOM Snapdragon Ride Flex(1000+ TOPS),中国车企主力供应商
  - name: Mobileye
    share: ~15%全球ADAS芯片
    note: MBLY EyeQ6/SuperVision/Chauffeur,Intel子公司,面临中国替代
  - name: 禾赛Hesai
    share: ~35%全球LiDAR出货
    note: HSAI AT128大规模量产,50万+年产能,NASDAQ上市,晶圆到模组垂直整合
  - name: Luminar
    share: ~10%欧美LiDAR
    note: LAZR Iris+ 1550nm,沃尔沃/奔驰合作,财务承压
  china:
  - name: 百度Apollo Go
    share: ~30%中国Robotaxi
    note: BIDU/9888.HK 22城运营,1700万+累计行程,第6代车$28K/台(-60%成本),目标2030年100城
  - name: 地平线
    share: ~35%中国AV芯片
    note: 9660.HK Journey征程6(560 TOPS),比亚迪/理想/大众中国定点,港股上市
  - name: 速腾聚创
    share: ~25%中国LiDAR
    note: 2498.HK M平台MEMS方案,比亚迪/吉利/小鹏/丰田客户,港股上市
  - name: 小马智行Pony.ai
    share: ~15%中国Robotaxi
    note: PONY Gen-7 Robotaxi 2025年6月发布,美股上市,比亚迪合作
  - name: 文远知行WeRide
    share: ~10%中国Robotaxi
    note: WRD Robotaxi+Robobus+Robovan,Uber合作15城全球拓展,美股上市
  - name: 华为
    share: ~20%中国智驾Tier-1
    note: (未上市) ADS 3.0端到端架构,HI-XG LiDAR 905nm+1550nm双路线,MDC计算平台
  - name: 黑芝麻智能
    share: ~10%中国AV芯片
    note: 2533.HK A1000系列,港股上市,华为生态
  barriers:
  - item: AI芯片算力+能效比
    detail: NVIDIA Thor 2000 TOPS领先国产芯片35倍，CUDA生态300万+开发者锁定
  - item: 车规认证周期
    detail: 18-24月+大客户定点锁定，新进入者难以快速获客
  - item: 数据积累马太效应
    detail: Tesla 67-100亿英里训练数据远超竞品，算法迭代飞轮不可复制
  - item: 全栈能力稀缺
    detail: 仅有Waymo/Tesla/华为/百度具备传感器+感知+规控完整自研能力
  tech_gap:
  - dimension: 芯片算力
    detail: 国产黑芝麻A1000(58 TOPS) vs NVIDIA Thor(2000 TOPS)差距~35x
  - dimension: 算法数据
    detail: Tesla 100亿英里 vs 中国头部~10亿英里差距~10x
  - dimension: LiDAR技术
    detail: 中国禾赛/速腾出货量全球领先但FMCW(Aeva/Aurora)可能颠覆现有技术路线
  - dimension: L4运营
    detail: Waymo 6城45万+周行程 vs 百度22城1700万+累计行程，商业化深度vs广度存差异
key_trends:
- title: L4 Robotaxi进入规模化运营拐点(2025-2026)
  detail: Waymo 6城运营/$1B+年收入,百度22城/1700万+行程,Tesla Cybercab目标2026年量产,Robotaxi每公里成本¥2.1接近人工出租车¥2.0
- title: 端到端AI架构替代传统模块化架构
  detail: Tesla FSD v13/华为ADS 3.0/小鹏XNGP全面转向端到端单一神经网络,感知-预测-规划-控制一体化,Transformer+Occupancy Network成为标配
- title: 激光雷达成本$1000→$200推动L2+渗透率突破50%
  detail: 禾赛AT128/速腾M平台固态化+规模制造降本,中国L2+渗透率>50%全球最高,LiDAR从高端选配变为中低端标配
- title: 中国智驾下沉至10万元级车型
  detail: 比亚迪天神之眼/华为ADS从30万+高端车型下沉至10万级入门车,2025年目标70%新车搭载L2/L3,单年增量数千万台
- title: Tesla x NVIDIA合作标志芯片生态重塑(2025年8月)
  detail: Tesla宣布集成NVIDIA Thor SoC,打破自研FSD芯片独占格局,Thor 2000 TOPS为L4提供算力基础
- title: GM Cruise退出Robotaxi引发行业整合(2024年12月)
  detail: GM停止对Cruise资金支持,资本向Waymo/百度/Tesla头部集中,行业进入淘汰赛阶段
- title: L3法规全球突破加速商业化
  detail: 中国发放L3测试牌照(蔚来/比亚迪/一汽),欧盟GSR2强制ADAS功能,UNECE R157允许L3高速领航,日本目标2027年100城L4部署
- title: 自动驾驶芯片算力爆发10→2000 TOPS驱动先进封装/HBM需求
  detail: L2仅需10 TOPS,L4需1000+ TOPS,NVIDIA Thor/Qualcomm Ride Flex/地平线J6均采用TSMC 4nm/CoWoS先进封装,HBM3e成为性能瓶颈
- title: FMCW激光雷达(47.46% CAGR)成下一代技术热点
  detail: 相干探测提供速度信息+抗干扰,Aeva/Aurora/华为布局,预计2027年规模上车
- title: Robotaxi服务平台化:Uber+WeRide 15城合作为范式
  detail: Uber与WeRide/Waymo/Lucid建立Robotaxi车队合作,出行平台从自营转向开放生态
price_conduction:
- AI芯片设计(NVIDIA Orin ASP$500-2000/片,毛利率60-70%)
- 晶圆代工+先进封装(TSMC 4nm/CoWoS,单芯片制造成本$50-200)
- 传感器制造(禾赛LiDAR ASP$200-1000/颗下降中,Sony车载CIS$20-50/颗,Bosch毫米波雷达$30-80/颗)
- Tier-1系统集成(Bosch/华为/德赛西威,域控制器ASP$500-2000,集成毛利率8-15%)
- OEM整车集成(L2+系统$1500-2000/车,L3$2000-5000/车,L4 Robotaxi$5000-15000/车,占整车成本8-20%)
- Robotaxi运营(百度第6代车$28K/台,每公里成本¥2.1 vs 人工¥2.0,盈亏平衡临近)
- 出行服务MaaS规模化替代(市场规模CAGR 74.5%,$2.1B→$104B)
wikilinks:
- GPU
- 边缘AI
- HBM高带宽内存
- AI服务器
- 数据中心IDC
- ASIC/AI定制芯片
- 散热液冷系统
- CIS图像传感器
- MCU与嵌入式处理器
- 功率半导体
- FPGA
key_inputs:
- GPU
- 边缘AI
- HBM高带宽内存
- AI服务器
- 数据中心IDC
- ASIC/AI定制芯片
key_customers:
- 光模块
- 散热液冷系统
- CIS图像传感器
- MCU与嵌入式处理器
- 功率半导体
- FPGA
companies:
- ticker: TSLA
  name: Tesla
  role: 龙头
  rev: 20
- ticker: BIDU
  name: 百度
  role: 龙头
  rev: 15
- ticker: '9660'
  name: 地平线
  role: 龙头
  rev: 80
- ticker: GOOGL
  name: Waymo
  role: 龙头
  rev: 10
- ticker: GM
  name: Cruise
  role: 二线弹性
  rev: 5
- ticker: MBLY
  name: Mobileye
  role: 二线弹性
  rev: 15
- ticker: NVDA
  name: NVIDIA
  role: 龙头
  rev: 10
- ticker: QCOM
  name: Qualcomm
  role: 二线弹性
  rev: 10
- ticker: PONY
  name: 小马智行
  role: 二线弹性
  rev: 15
- ticker: WRD
  name: 文远知行
  role: 二线弹性
  rev: 15
- ticker: AUR
  name: Aurora
  role: 二线弹性
  rev: 15
- ticker: ZOXX
  name: Zoox
  role: 二线弹性
  rev: 10
- ticker: NURO
  name: Nuro
  role: 二线弹性
  rev: 10
- ticker: HSAI
  name: 禾赛科技
  role: 二线弹性
  rev: 20
- ticker: '2498'
  name: 速腾聚创
  role: 二线弹性
  rev: 20
- ticker: TSP
  name: 图森未来
  role: 概念股
  rev: 10
- ticker: AAPL
  name: Apple
  role: 概念股
  rev: 5
sources:
- title: Waymo 2025 Safety Report
  summary: ''
  url: https://www.waymo.com/safety
- title: 地平线招股书2025
  summary: ''
  url: https://www.horizon.auto
- title: CA DMV Autonomous Vehicle Disengagement Report 2025
  summary: ''
  url: https://www.dmv.ca.gov
---

# 自动驾驶

自动驾驶(Autonomous Driving)是利用AI芯片、多传感器融合(激光雷达/摄像头/毫米波雷达)与端到端神经网络实现车辆自主感知、决策与控制的系统性技术,覆盖从L2+高级辅助驾驶到L4全无人自动驾驶全栈方案,是边缘AI最大规模商用场景。2026年全球AV系统级市场规模约$48B(CAGR~30%),Robotaxi专项服务市场增速最快(CAGR 74.5%,$2.1B→$104B)。|**全球竞争格局**:NVIDIA DRIVE芯片市占率~50%+训练GPU~90%绝对主导,Waymo全球Robotaxi商业化领先(6城运营,$1B+年收入,估值$100-110B),Tesla凭FSD v13端到端+Cybercab切入2026量产。|**中国生态**:百度Apollo Go 22城运营(第6代车$28K,-60%成本),地平线征程6国产AV芯片主力,禾赛/速腾聚创全球LiDAR出货领先,华为ADS 3.0端到端Tier-1。中国L2+渗透率>50%全球最高,智驾从30万+高端下沉至10万元车型(比亚迪天神之眼)。|**技术拐点**:端到端AI架构替代传统模块化(感知→规划→控制一体化),激光雷达ASP从$1000降至$200推动L2+全价位标配,Robotaxi每公里成本¥2.1逼近人工出租车¥2.0的盈亏平衡线。芯片算力从L2的10 TOPS飙升至L4的1000-2000 TOPS(NVIDIA Thor),驱动TSMC 4nm+CoWoS先进封装+HBM3e需求,价值链向AI芯片+端到端软件集中。|2025年中国L4融资超600亿元,GM Cruise退出Robotaxi加速行业整合,Waymo/百度/Tesla三足鼎立格局形成。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $48B |
| 年复合增长率(CAGR) | 30% |
| 利润率区间 | 30-50% |
| 成本占比 | 40% (自动驾驶系统(芯片+传感器+软件+域控)占产业链总成本比例) |
| 利润池占比 | 45% (自动驾驶系统供应商(芯片+软件+传感器)占产业链利润池份额) |
| 附加值 | high |

## 关联

- 上游: [[GPU]], [[边缘AI]], [[HBM高带宽内存]], [[AI服务器]], [[数据中心IDC]], [[ASIC/AI定制芯片]]
- 下游: [[光模块]], [[散热液冷系统]], [[CIS图像传感器]], [[MCU与嵌入式处理器]], [[功率半导体]], [[FPGA]]

## 动态更新记录

### 更新 2026-07-22 (多Agent调研)
> 来源: 多Agent交叉验证调研（3搜索Agent + Judge合并，197次工具调用，9个市场研究来源）
> 置信度: 中（5项数据冲突已标注并解决）

- **全字段更新**: TAM $40B→$48B, CAGR 25%→30%，基于Precedence/Mordor/MarketsandMarkets等多来源中位数
- **key_inputs**: +10个上游类别（AI芯片/SoC、激光雷达、毫米波雷达、CIS传感器、高精地图、域控制器/MCU、自动驾驶OS、仿真验证、AI训练GPU、4D成像雷达）
- **key_customers**: +6个下游类型（Robotaxi运营商、乘用车OEM、出行平台、自动驾驶卡车、末端配送、市政交通）
- **wikilinks**: 1→12（GPU/ASIC/HBM/CIS/MCU/功率半导体/FPGA等）
- **companies**: 17→29家（含美股/港股/A股完整ticker）
- **key_trends**: 3→10条（L4拐点/端到端架构/LiDAR降本/智驾下沉/Tesla-NVIDIA/Cruise退出/L3法规/算力爆发/FMCW LiDAR/Robotaxi平台化）
- **price_conduction**: 重写为7阶段链（AI芯片→晶圆代工→传感器→Tier-1→OEM→Robotaxi→MaaS）
- **sources**: +9个市场研究URL
- **5项数据冲突**: TAM范围/CAGR定义/Cruise状态/基准年/Waymo行程量——已标注解决依据