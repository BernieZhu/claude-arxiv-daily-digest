# arXiv Daily Digest — 2026-04-15

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 3

---

## 1. HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models

**Authors:** Zixing Chen, Yifeng Gao, Li Wang, ..., Xingjun Ma, Yu-Gang Jiang
**arXiv:** [2604.12447](https://arxiv.org/abs/2604.12447)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models inherit rich world knowledge from vision-language backbones and acquire executable skills via action demonstrations. However, existing evaluations largely focus on action execution success, leaving action policies loosely coupled with visual-linguistic semantics. This decoupling exposes a systematic vulnerability whereby correct action execution may induce unsafe outcomes under semantic risk. To expose this vulnerability, we introduce HazardArena, a benchmark designed to evaluate semantic safety in VLAs under controlled yet risk-bearing contexts. HazardArena is constructed from safe/unsafe twin scenarios that share matched objects, layouts, and action requirements, differing only in the semantic context that determines whether an action is unsafe. We find that VLA models trained exclusively on safe scenarios often fail to behave safely when evaluated in their corresponding unsafe counterparts. HazardArena includes over 2,000 assets and 40 risk-sensitive tasks spanning 7 real-world risk categories grounded in established robotic safety standards. To mitigate this vulnerability, we propose a training-free Safety Option Layer that constrains action execution using semantic attributes or a vision-language judge, substantially reducing unsafe behaviors with minimal impact on task performance. We hope that HazardArena highlights the need to rethink how semantic safety is evaluated and enforced in VLAs as they scale toward real-world deployment.

---

## 2. Unveiling the Surprising Efficacy of Navigation Understanding in End-to-End Autonomous Driving

**Authors:** Zhihua Hua, Junli Wang, Pengfei LI, ..., Zhongxue Gan, Wenchao Ding
**arXiv:** [2604.12208](https://arxiv.org/abs/2604.12208)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Global navigation information and local scene understanding are two crucial components of autonomous driving systems. However, our experimental results indicate that many end-to-end autonomous driving systems tend to over-rely on local scene understanding while failing to utilize global navigation information. These systems exhibit weak correlation between their planning capabilities and navigation input, and struggle to perform navigation-following in complex scenarios. To overcome this limitation, we propose the Sequential Navigation Guidance (SNG) framework, an efficient representation of global navigation information based on real-world navigation patterns. The SNG encompasses both navigation paths for constraining long-term trajectories and turn-by-turn (TBT) information for real-time decision-making logic. We constructed the SNG-QA dataset, a visual question answering (VQA) dataset based on SNG that aligns global and local planning. Additionally, we introduce an efficient model SNG-VLA that fuses local planning with global planning. The SNG-VLA achieves state-of-the-art performance through precise navigation information modeling without requiring auxiliary loss functions from perception tasks. Project page: SNG-VLA

---

## 3. Robotic Manipulation is Vision-to-Geometry Mapping ($f(v) \rightarrow G$): Vision-Geometry Backbones over Language and Video Models

**Authors:** Zijian Song, Qichang Li, Jiawei Zhou, ..., Liang Lin, Guangrun Wang
**arXiv:** [2604.12908](https://arxiv.org/abs/2604.12908)
**Categories:** Robotics (cs.RO)

At its core, robotic manipulation is a problem of vision-to-geometry mapping ($f(v) \rightarrow G$). Physical actions are fundamentally defined by geometric properties like 3D positions and spatial relationships. Consequently, we argue that the foundation for generalizable robotic control should be a vision-geometry backbone, rather than the widely adopted vision-language or video models. Conventional VLA and video-predictive models rely on backbones pretrained on large-scale 2D image-text or temporal pixel data. While effective, their representations are largely shaped by semantic concepts or 2D priors, which do not intrinsically align with the precise 3D geometric nature required for physical manipulation. Driven by this insight, we propose the Vision-Geometry-Action (VGA) model, which directly conditions action generation on pretrained native 3D representations. Specifically, VGA replaces conventional language or video backbones with a pretrained 3D world model, establishing a seamless vision-to-geometry mapping that translates visual inputs directly into physical actions. To further enhance geometric consistency, we introduce a Progressive Volumetric Modulation module and adopt a joint training strategy. Extensive experiments validate the effectiveness of our approach. In simulation benchmarks, VGA outperforms top-tier VLA baselines including $\pi_{0.5}$ and GeoVLA, demonstrating its superiority in precise manipulation. More importantly, VGA exhibits remarkable zero-shot generalization to unseen viewpoints in real-world deployments, consistently outperforming $\pi_{0.5}$. These results highlight that operating on native 3D representations-rather than translating through language or 2D video priors-is a highly promising direction for achieving generalizable physical intelligence.

---
