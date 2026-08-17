---
name: AI服务器
slug: ai-server
industry: AI算力
layer: L3
tam_bn: 220.0
cagr_pct: 25.0
margin: 10-20%
cost_share_pct: 25
cost_share_context: 数据中心TCO
profit_pool_pct: 8
profit_pool_context: 数据中心利润池
value_add: medium
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: 工业富联(Foxconn)
    share: ~35%
    note: 601138 NVIDIA GB200独家代工全球#1，2026年AI服务器营收万亿台币级, Super Micro(SMCI)
  - name: 广达(Quanta)
    share: ~12%
    note: 台系ODM，Microsoft/Google AI服务器主力供应商
  - name: 纬创(Wistron)
    share: ~8%
    note: 台系ODM，NVIDIA DGX供应商
  china:
  - name: 品牌：Dell
    share: '-'
    note: 美国PowerEdge XE AI，企业级AI市场
  - name: HPE
    share: '-'
    note: 美国ProLiant Gen12 AI
  - name: Lenovo
    share: '-'
    note: 0992.HK ThinkSystem SR AI
  barriers: []
  tech_gap: []
key_trends:
- title: AI服务器2026年占全球服务器市场74%价值(TrendForce)
  detail: GB200/300机柜出货从20K(2025)增至30K+(2026)，ASP>$3M
- title: NVIDIA从芯片→整机柜压缩ODM利润
  detail: 工业富联/SMCI从组装向液冷+测试差异化转型，但ODM毛利率仍仅10-20%
- title: 液冷从选配变标配
  detail: GB200 NVL72强制液冷，风冷AI服务器退出，液冷ODM产能成为新瓶颈
- title: 中国AI服务器出口管制下国产替代
  detail: 昇腾910B在国内政府/运营商份额从10%向30%增长，但GPU算力差距仍大
- title: 云厂商自研服务器分流ODM
  detail: Google TPU pod/AWS Trainium rack绕过传统ODM，直接向台厂采购定制化组件
- title: 半导体全面涨价潮扩散至AI服务器
  detail: 涨价从GPU扩散至CPU/PCB/被动元件/高速连接器，AI服务器ASP持续上涨，ODM利润进一步承压
price_conduction:
- AI服务器ODM毛利率仅10-20%，NVIDIA GPU捆绑销售模式压缩ODM附加值。GPU涨价
- ODM利润空间进一步收窄
- ODM从组装向散热/测试/系统集成差异化转型
- 利润池从ODM向芯片端(NVIDIA)转移
wikilinks:
- GPU
- 散热液冷系统
- 云计算IaaS
- 数据中心IDC
- PCB与IC载板
- HBM高带宽内存
- AI训练集群/超算
- 服务器电源与UPS
- DPU/SmartNIC
key_inputs:
- GPU
companies:
- ticker: HUAWEI
  name: 华为
  role: 龙头
  rev: 15
- ticker: 000977
  name: 浪潮信息
  role: 龙头
  rev: 60
- ticker: '601138'
  name: 工业富联
  role: 龙头
  rev: 40
- ticker: '002261'
  name: 拓维信息
  role: 概念股
  rev: 25
- ticker: '000034'
  name: 神州数码
  role: 概念股
  rev: 15
- ticker: '9988'
  name: 阿里巴巴
  role: 二线弹性
  rev: 10
- ticker: NVDA
  name: NVIDIA
  role: 龙头
  rev: 10
- ticker: SMCI
  name: Super Micro
  role: 龙头
  rev: 30
- ticker: DELL
  name: Dell
  role: 二线弹性
  rev: 15
- ticker: HPE
  name: HPE
  role: 二线弹性
  rev: 10
- ticker: 0992
  name: 联想
  role: 二线弹性
  rev: 10
key_customers:
- 云计算IaaS
- AI训练集群/超算
sources:
- title: TrendForce AI Server Shipment Forecast Oct 2025
  summary: ''
  url: https://www.trendforce.com
- title: Goldman Sachs Asia AI Server Feb 2025
  summary: ''
  url: ''
- title: KGI Research AI Server TAM 2026
  summary: ''
  url: ''
- title: Digitimes Foxconn/Wistron/Quanta AI Revenue Jan 2026
  summary: ''
  url: https://www.digitimes.com
- title: TrendForce Server Market Bulletin Jan 2026
  summary: ''
  url: ''
---

# AI服务器

> **AI算力** · L3 · TAM **$220B** · CAGR **25%**

AI服务器是为深度学习训练和推理**专门优化**的高性能计算系统——集成多颗GPU、配备HBM高带宽内存、液冷散热、高速互联。|**GB200 NVL72是当前旗舰**——72颗B200 GPU通过NVLink全互联集成在液冷机柜中，单机柜ASP超$300万。2025年出货~20K机柜，2026年预计30K+。|**NVIDIA从芯片走向完整系统**：DGX+GB200 NVL机柜级方案定义行业标准，ODM从组装向散热/测试差异化转型。AI服务器2026年将占全球服务器市场74%价值。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $220B |
| 年复合增长率(CAGR) | 25% |
| 利润率区间 | 10-20% |
| 成本占比 | 25% (数据中心TCO) |
| 利润池占比 | 8% (数据中心利润池) |
| 附加值 | medium |

## 关联

- 上游: [[GPU]]

## 动态更新记录

### 更新 2026-07-22
> 来源: 消化笔记/2026-07-22-v1.1-中原证券电子行业中期策略, 消化笔记/2026-07-22-v1.1-德勤全球半导体趋势
> 置信度: 中

- **key_trends**: +1条 "半导体全面涨价潮扩散至AI服务器——涨价从GPU扩散至CPU/PCB/被动元件/高速连接器"
- **sources**: +1 中原证券2026中期策略
- **依据**: 中原证券——涨价已从存储蔓延至晶圆代工/封测/CPU/模拟/功率器件，AI硬件产业链通胀从半导体扩散到PCB、被动元件
