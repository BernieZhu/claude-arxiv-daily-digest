# arXiv Daily Digest — 2026-04-02

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 2

---

## 1. DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving

**Authors:** Yiyao Zhu, Ying Xue, Haiming Zhang, ..., Zhen Li, Shaojie Shen
**arXiv:** [2604.00969](https://arxiv.org/abs/2604.00969)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-based autonomous driving has gained much attention due to its low costs and excellent performance. Compared with dense BEV (Bird's Eye View) or sparse query models, Gaussian-centric method is a comprehensive yet sparse representation by describing scene with 3D semantic Gaussians. In this paper, we introduce DLWM, a novel paradigm with Dual Latent World Models specifically designed to enable holistic gaussian-centric pre-training in autonomous driving using two stages. In the first stage, DLWM predicts 3D Gaussians from queries by self-supervised reconstructing multi-view semantic and depth images. Equipped with fine-grained contextual features, in the second stage, two latent world models are trained separately for temporal feature learning, including Gaussian-flow-guided latent prediction for downstream occupancy perception and forecasting tasks, and ego-planning-guided latent prediction for motion planning. Extensive experiments in SurroundOcc and nuScenes benchmarks demonstrate that DLWM shows significant performance gains across Gaussian-centric 3D occupancy perception, 4D occupancy forecasting and motion planning tasks.

---

## 2. DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale

**Authors:** Sicheng Zuo, Zixun Xie, Wenzhao Zheng, ..., Zhi-Xin Yang, Jiwen Lu
**arXiv:** [2604.00813](https://arxiv.org/abs/2604.00813)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilitate planning. In this paper, we propose an alternative Vision-Geometry-Action (VGA) paradigm that advocates dense 3D geometry as the critical cue for autonomous driving. As vehicles operate in a 3D world, we think dense 3D geometry provides the most comprehensive information for decision-making. However, most existing geometry reconstruction methods (e.g., DVGT) rely on computationally expensive batch processing of multi-frame inputs and cannot be applied to online planning. To address this, we introduce a streaming Driving Visual Geometry Transformer (DVGT-2), which processes inputs in an online manner and jointly outputs dense geometry and trajectory planning for the current frame. We employ temporal causal attention and cache historical features to support on-the-fly inference. To further enhance efficiency, we propose a sliding-window streaming strategy and use historical caches within a certain interval to avoid repetitive computations. Despite the faster speed, DVGT-2 achieves superior geometry reconstruction performance on various datasets. The same trained DVGT-2 can be directly applied to planning across diverse camera configurations without fine-tuning, including closed-loop NAVSIM and open-loop nuScenes benchmarks.

---
