---
name: "Chiplet与异构集成"
slug: "c-chiplet"
type: "concept"
category: "技术"
difficulty: "高级"
confidence: "高"
one_liner: "将一个大芯片拆成多个小芯粒，像拼乐高一样用先进封装组合，突破单芯片面积极限、提升良率、降低成本的芯片设计新范式"
fable_title: "乐高积木 vs 一整块木头雕刻——拆开做，再拼起来"
affected_segments: ["chiplet", "cowos-advanced-packaging", "gpu-architecture", "cpu-server", "semi-advanced-packaging"]
affected_companies: ["amd", "intel", "nvidia", "tsmc", "apple", "broadcom"]
heat: "趋势"
tags: ["Chiplet", "异构集成", "先进封装", "UCIe", "芯片设计"]
related_concepts:
  - slug: "cowos"
    relation: "CoWoS是Chiplet架构目前最成熟的高性能互联封装平台"
  - slug: "hbm"
    relation: "HBM本质上是Chiplet的「内存Tile」——通过先进封装集成到芯片系统"
  - slug: "ucie"
    relation: "UCIe是Chiplet互联的行业标准，解决不同厂商芯粒之间的「语言不通」问题"
  - slug: "asic"
    relation: "ASIC天然适合Chiplet路线——不同功能模块用不同工艺节点制造"
updated: "2026-07"
wikilinks: ["Chiplet与异构集成", "先进封装CoWoS", "GPU架构设计", "CPU(服务器级)", "先进封装(CoWoS/3D)", "ASIC/AI定制芯片", "EDA与IP核"]
---

# Chiplet · 异构集成

> **把大芯片拆成乐高积木块,每块用最合适的工艺造,再通过先进封装拼回去** | 技术 · 高级

---

## 一、生活化类比：乐高积木 vs 一整块木头雕刻

古代木匠做一张复杂的桌子,只能找一整块大木头,从头雕到尾——费料、费工、一个地方雕坏了整块木头报废。这就是传统SoC(单片系统芯片)：CPU、GPU、内存控制器、I/O全集成在一块芯片上,面积越大良率越低,一个缺陷就报废。

Chiplet就像乐高积木的做法：桌面、桌腿、抽屉、装饰条分别用不同的木材（甚至塑料、金属）做好,最后拼成一张完整的桌子。每个积木块用最合适的材料（工艺节点）,拼装靠标准化的卡扣（UCIe互联接口）。坏了只要换那一个积木块,不用扔整张桌子。

**对应关系：**

| 比喻中的元素 | 对应的技术/产业元素 |
|-------------|------------------|
| 一整块木头雕刻 | 传统SoC(单片芯片,所有功能集成在一个die) |
| 乐高积木块 | Chiplet(芯粒,每个独立die实现特定功能) |
| 不同材质(木头/塑料/金属) | 不同工艺节点(3nm计算die+7nm I/O die) |
| 乐高卡扣 | UCIe互联标准(不同厂商芯粒之间的通用接口) |
| 拼装说明书 | 先进封装(CoWoS/EMIB) |
| 坏一个换一个 | 良率提升(小die良率远高于大die) |

---

## 二、专业但通俗的定义

**全称**：Chiplet（芯粒/小芯片）+ Heterogeneous Integration（异构集成）。AMD 2017年首发Chiplet架构CPU(Epyc),Intel 2023年跟进(Meteor Lake),NVIDIA Blackwell(2024)引入Chiplet设计。

**传统SoC vs Chiplet方案：**

| 对比维度 | 传统SoC(单片) | Chiplet架构 |
|---------|------------|-----------|
| 芯片面积 | 越来越大(>800mm²),逼近光罩极限 | 每个芯粒<200mm²,总体>1000mm² |
| 良率 | 面积越大良率指数下降(800mm²良率可能<50%) | 小die良率>90%,整体成本降低30-50% |
| 工艺选择 | 全部用同一工艺节点 | 计算die用最新节点(3nm),I/O die用成熟节点(7nm) |
| 开发周期 | 整个芯片重新设计,2-3年 | 复用已有芯粒,拼装升级,6-12个月 |
| 互联标准 | 内部总线,无需标准 | UCIe/BoW等互联标准,不同厂商芯粒需兼容 |

**核心优势：**
1. **突破光罩极限**：单芯片面积无法超过光刻机光罩尺寸(~850mm²),Chiplet可以超越
2. **良率大幅提升**：小die良率>90%,相比同面积单die(良率可能<50%)成本降30-50%
3. **工艺灵活**：计算用3nm追求性能,I/O用7nm控制成本,射频用成熟工艺保证可靠性
4. **快速迭代**：只需升级计算芯粒,保留I/O芯粒,新品开发周期从2年缩至1年
5. **异构集成**：CPU+GPU+NPU+HBM可以像拼图一样集成,适应AI时代的多元化算力需求

---

## 三、为什么市场会关注它

| 维度 | 具体依据 |
|-----|---------|
| **政策驱动** | UCIe联盟(Intel/AMD/ARM/台积电/三星等160+成员)推动Chiplet互联标准化,中国Chiplet联盟(CCT)同步推进国产标准 |
| **技术突破** | NVIDIA Blackwell首次在GPU引入Chiplet(两个计算die通过NVLink互联),AMD MI300X用Chiplet集成CPU+GPU+HBM |
| **海外映射** | AMD Epyc(2017)→Intel Meteor Lake(2023)→NVIDIA Blackwell(2024)→Apple M系列UltraFusion(2022),所有顶级芯片全面转向Chiplet |
| **产业链传导** | Chiplet普及→先进封装(CoWoS/EMIB)需求爆发→EDA工具升级Chiplet设计→IP核市场(D2D接口IP)扩张 |
| **订单/业绩驱动** | AMD数据中心CPU 100% Chiplet架构,Intel 2025年所有新平台Chiplet,NVIDIA Rubin(2026)Chiplet架构升级 |

---

## 四、产业链位置

| 产业链环节 | 主要作用 | 代表公司/板块 | 小白理解 |
|-----------|---------|-------------|---------|
| 上游（EDA+IP核+UCIe接口） | Chiplet设计工具、D2D互联IP、UCIe控制器 | Synopsys、Cadence、Alphawave | 乐高的设计图和卡扣专利 |
| 中游（芯粒制造+先进封装） | 不同工艺节点的芯粒制造+CoWoS/EMIB封装 | 台积电、三星、Intel | 乐高积木生产和拼装 |
| 下游（芯片产品设计） | 用Chiplet架构设计CPU/GPU/AI芯片 | AMD、NVIDIA、Intel、苹果、博通 | 买积木搭自己想要的玩具 |

> Chiplet跨越AI算力 **L2（封装）→ L3（芯片设计）**，是从芯片设计范式到先进封装的系统性变革。

---

## 五、相关公司和板块

| 分类 | 公司/板块 | 关联度 | 关联原因 |
|-----|----------|-------|---------|
| **核心参与者** | AMD(AMD) | 核心 | Chiplet架构先驱(2017 Epyc),MI300X用Chiplet集成13个die |
| **核心参与者** | Intel(INTC) | 核心 | EMIB/Foveros先进封装,2023年全面转向Chiplet(Meteor Lake) |
| **核心参与者** | NVIDIA(NVDA) | 核心 | Blackwell首款GPU Chiplet(2024),Rubin进一步升级 |
| **直接相关** | 台积电(TSM) | 直接 | CoWoS+3D Fabric平台,Chiplet封装代工垄断 |
| **直接相关** | 苹果(AAPL) | 直接 | M系列UltraFusion Chiplet互联,消费电子Chiplet先驱 |
| **直接相关** | Synopsys(SNPS) | 直接 | EDA+Chiplet设计IP+D2D接口IP,受益Chiplet设计复杂性提升 |
| **间接相关** | 长电科技(600584.SH) | 间接 | 国内先进封装龙头,布局Chiplet封装但以传统封装为主 |
| **沾边概念** | 通富微电(002156.SZ) | 沾边 | AMD封装服务商,受益AMD Chiplet但自身无Chiplet IP |

---

## 六、投资关注点

1. **UCIe 2.0标准进度**：更高带宽、更低功耗的Chiplet互联标准能否按时落地
2. **NVIDIA Chiplet升级路线**：Blackwell→Rubin Chiplet架构复杂度提升,对先进封装需求拉动
3. **国内Chiplet联盟进展**：长电/通富/华为等能否建立国产Chiplet生态
4. **Chiplet对EDA/IP市场拉动**：Synopsys/Cadence Chiplet设计工具收入增速
5. **成本拐点**：Chiplet方案总成本低于单片方案的时机(良率+封装成本的平衡点)

---

## 七、风险提示

| 风险 | 如果发生，会怎样 |
|-----|----------------|
| 封装成本过高 | Chiplet方案总成本高于单片方案→经济性不成立,仅限高端芯片使用 |
| 互联标准碎片化 | UCIe/BoW/AIB多标准并存→兼容性差,无法形成规模化生态 |
| 热管理挑战 | 多die集成散热难度远超单die→可靠性问题,部署受限 |
| 技术壁垒过高 | Chiplet设计+验证+封装门槛远超传统SoC→只有头部厂商玩得起,中小公司出局 |
| 中国被标准排除 | UCIe联盟限制中国厂商参与→国产Chiplet生态被迫走独立路线,发展慢3-5年 |

---

## 八、如何判断是真逻辑还是炒概念

| 判断维度 | 应该看什么 | 小白容易误判的地方 |
|---------|-----------|------------------|
| 有没有Chiplet产品 | 看公司是否已出货Chiplet架构芯片(AMD/Intel/NVIDIA) | 把"多芯片封装"当Chiplet(MCM≠Chiplet) |
| 是否掌握D2D互联 | 看是否有自研或授权D2D接口IP | 以为只要做封装的就能做Chiplet |
| 先进封装能力 | 是否具备2.5D/3D封装能力(CoWoS或EMIB级别) | 把传统FCBGA封装当先进封装 |
| 客户是否顶级 | Chiplet芯片客户是否为AMD/NVIDIA/苹果级别 | 把"在研"当"导入" |
| 国产进度合理性 | 国内Chiplet比海外晚5-7年,不要用海外进度线性外推国内 | 以为海外Chiplet爆发=国内马上能跟上 |

---

## 九、后续追踪指标

- **UCIe会员数及标准更新**：当前160+成员,追踪2.0版本发布时间
- **NVIDIA Rubin Chiplet架构细节**(GTC发布)：计算die数量、互联方式
- **台积电CoWoS/3D Fabric收入增速**(季报)：Chiplet封装需求晴雨表
- **国内Chiplet产品流片公告**：华为/长电/通富Chiplet项目进展
- **Synopsys Chiplet设计工具收入**：EDA受益Chiplet的力度

---

## 十、相关概念链接

- **【CoWoS先进封装】** — Chiplet架构目前最成熟的高性能互联封装平台,AMD/NVIDIA均使用
- **【HBM高带宽内存】** — HBM是Chiplet架构中最关键的「内存Tile」
- **【UCIe】** — Chiplet互联的行业标准,解决「不同厂商芯粒之间如何通信」的问题
- **【ASIC/AI定制芯片】** — ASIC天然适合Chiplet思路——不同功能模块用不同工艺
- **【EDA与IP核】** — Chiplet设计范式改变EDA工具需求,D2D接口IP成为新品类

---

> ⚠️ **免责声明**：本内容仅作概念科普和产业认知框架搭建,不构成任何投资建议。市场有风险,投资需谨慎。
