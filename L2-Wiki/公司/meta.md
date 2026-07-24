---
name: Meta
slug: meta
country: US
ticker: META
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- AI Agent
- AI开发者工具
- AI推理API服务
- AI模型训练平台
- AI训练集群/超算
one_liner: 全球最大社交媒体与数字广告平台，以Facebook/Instagram/WhatsApp为核心，通过开源AI模型Llama和自研芯片转型AI算力基础设施提供商，构建从社交到AI云的新增长曲线。
chain_layer: L4
chain_role: 龙头
suppliers:
- company: NVIDIA
  ticker: NVDA
  supplies: H100/B200 GPU
  revenue_pct: 15
  note: 训练Llama大模型
- company: Broadcom
  ticker: AVGO
  supplies: MTIA ASIC设计
  note: 自研推荐系统芯片
- company: 台积电
  ticker: TSM
  supplies: MTIA晶圆代工
- company: 英伟达/NVIDIA
  supplies: 主力GPU供应商，2026年签署多年协议部署数百万Blackwell/Vera Rubin GPU
- company: AMD
  supplies: 600亿美元GPU协议，定制MI450用于推理，部署高达6GW算力
- company: 博通/Broadcom
  supplies: 自研芯片MTIA/Iris设计合作伙伴，合作至2029年
- company: 台积电/TSMC
  supplies: 自研Iris芯片制造
- company: CoreWeave
  supplies: 210亿美元算力合作扩展协议，补充云容量
customers:
- company: 全球Llama开发者
  note: 开源大模型生态
- company: Meta广告客户
  note: AI驱动广告推荐
- company: Anthropic
  note: 洽谈100亿美元两年期算力租赁协议，运行Claude模型
- company: 外部AI开发者
  note: 通过Meta Compute平台租赁GPU和调用Llama模型API
- company: 全球超1000万广告主
  note: 在Facebook、Instagram等平台投放
- company: WhatsApp Business用户
  note: 商业消息变现增长迅速
- company: 中小企业
  note: 利用Advantage+ AI工具自动优化广告投放
partners:
- company: NVIDIA
  ticker: NVDA
  area: GPU大规模采购
- company: Broadcom
  ticker: AVGO
  area: MTIA ASIC
competitors:
- company: Google
  ticker: GOOGL
  area: AI大模型+广告
  note: Gemini vs Llama
- company: TikTok
  area: 社交媒体广告
- company: 谷歌/Alphabet
  note: 数字广告+YouTube+Gemini AI+Google Cloud
- company: 亚马逊/AWS
  note: 云计算+电商广告+AI平台
- company: TikTok/字节跳动
  note: 短视频广告+社交电商，增速最快对手
- company: 微软/LinkedIn+OpenAI
  note: 云计算+AI模型+职业社交广告
core_business:
- 社交媒体广告（Facebook、Instagram、WhatsApp等，年广告收入1962亿美元）
- 开源AI模型Llama生态（HuggingFace超5亿下载，AI助手用户达10亿）
- Meta Compute云算力租赁（对外出租GPU集群，与Anthropic洽谈100亿美元合同）
- VR/AR硬件（Quest头显全球73%份额，Ray-Ban Meta智能眼镜）
- 自研AI芯片MTIA/Iris（第四代训练推理加速器，2026年9月量产）
revenue_model: 广告收入占98%，2025年达1962亿美元（同比增22%），核心驱动来自AI优化投放Advantage+、Reels短视频及WhatsApp商业消息。2025年总营收2009.7亿美元，净利润约605亿美元。2026年起开辟Meta Compute云算力租赁新收入来源，租250MW算力年收入可达100亿美元（摩根士丹利测算）。
ticker: META
description: Meta Platforms是全球最大社交媒体公司，旗下Facebook、Instagram、WhatsApp月活用户超40亿。公司全面转型AI算力巨头，FY2025资本开支超630亿美元投入AI基础设施，自研MTIA芯片与开源Llama大模型构成完整AI技术栈。通过AI赋能广告精准投放，FY2025营收突破2000亿美元(+22% YoY)，是AI商业化的全球标杆企业。
website: https://www.meta.com
industry: AI算力
founded: 2004
headquarters: 美国加州门洛帕克
employees: ~79,000
latest_revenue: Q1 2026 $56.3B（+33% YoY），Q2E $58-61B
market_cap: ~$1.6T（2026.7）
---

# Meta

从社交媒体霸主到AI算力基础设施巨头，以开源Llama+自研芯片+超大规模数据中心构建AI生态护城河

## 财务状况

| 指标 | FY2024 | FY2025 |
|------|--------|--------|
| 营收 | $1,645亿 | $2,010亿 |
| 净利润 | $624亿 | $605亿 |
| 资本开支 | $393亿 | **$630亿+** |

AI资本开支年增60%至630亿美元，主投GPU集群与数据中心。R&D支出574亿美元，核心投向Llama模型训练与AI基础设施。广告业务依托AI推荐实现22%营收增长，AI投资回报开始显现。

## 产品线详解

- **Llama开源模型**: Llama 3系列（8B/70B/405B参数），开源社区下载量数亿次，性能对标GPT-4
- **Meta AI助手**: 集成于Facebook/Instagram/WhatsApp/Messenger，覆盖40亿+全球用户
- **MTIA芯片**: 自研AI推理加速芯片v2已量产，下一代2026年9月投产，降低NVIDIA依赖
- **AI数据中心**: 全球超大规模GPU集群，定制化液冷架构，支撑万亿参数级模型训练

## 技术路线图

- **Llama 4/5**: 多模态架构（文本+图像+视频+语音），向万亿参数迈进，推理能力大幅提升
- **MTIA v3**: 2026年投产，采用先进制程，覆盖训练+推理全场景，逐步替代GPU
- **开源AGI战略**: 扎克伯格主张开源通往AGI，构建开发者生态对抗闭源阵营（OpenAI/Google）
- **AI Agent**: 企业级AI助手，自动化广告投放、客服与内容审核，2B商业化新增长极


## 融资与现金流

- 详见财务状况章节
## 研发投入与专利

R&D支出FY2025达**574亿美元**（+31% YoY），占营收28.5%，全行业最高之一。累计AI相关专利超万项，覆盖模型架构、推理优化、芯片设计。**开源生态壁垒**: Llama开源模型吸引全球百万开发者构建应用，形成事实标准。FAIR实验室持续产出Transformer架构优化等基础研究成果，开源社区锁定效应构成竞争护城河。

