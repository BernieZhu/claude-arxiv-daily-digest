# arXiv Daily Digest — 2026-04-29

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 2

---

## 1. Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System

**Authors:** Yifei Wei, Linqing Zhong, Yi Liu, ..., Maoqing Yao, Guanghui Ren
**arXiv:** [2604.24921](https://arxiv.org/abs/2604.24921)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models are a promising paradigm for generalist robotic manipulation by grounding high-level semantic instructions into executable physical actions. However, prevailing approaches typically adopt a monolithic generation paradigm, directly mapping visual-linguistic features to high-frequency motor commands in a flat, non-hierarchical fashion. This strategy overlooks the inherent hierarchy of robotic manipulation, where complex actions can be naturally modeled in a Hybrid Action Space, decomposing into discrete macro-directional reaching and continuous micro-pose alignment, severely widening the semantic-actuation gap and imposing a heavy representational burden on grounding high-level semantics to continuous actions. To address this, we introduce Libra-VLA, a novel Coarse-to-Fine Dual-System VLA architecture. We explicitly decouple the learning complexity into a coarse-to-fine hierarchy to strike a training equilibrium, while simultaneously leveraging this structural modularity to implement an asynchronous execution strategy. The Semantic Planner predicts discrete action tokens capturing macro-directional intent, while the Action Refiner conditions on coarse intent to generate high-frequency continuous actions for precise alignment. Crucially, our empirical analysis reveals that performance follows an inverted-U curve relative to action decomposition granularity, peaking exactly when the learning difficulty is balanced between the two sub-systems. With the asynchronous design, our approach offers a scalable, robust, and responsive solution for open-world manipulation.

---

## 2. Privileged Foresight Distillation: Zero-Cost Future Correction for World Action Models

**Authors:** Pengcheng Fang, Hongli Chen, Xiaohao Cai
**arXiv:** [2604.25859](https://arxiv.org/abs/2604.25859)
**Categories:** Robotics (cs.RO)

World action models jointly predict future video and action during training, raising an open question about what role the future-prediction branch actually plays. A recent finding shows that this branch can be removed at inference with little to no loss on common manipulation benchmarks, suggesting that future information may act merely as a regularizer on the shared visual backbone. We propose instead that joint training induces an action-conditioned correction that privileged future observations impose on action denoising, and that current-only policies capture this correction only partially. Making the account precise, we formulate privileged foresight as a residual in the action-denoising direction -- the difference between what a model predicts given the true future and what it predicts given only the current frame -- and introduce \emph{Privileged Foresight Distillation (PFD)}, which transfers this residual from a training-time teacher into a small adapter on a current-only student. The teacher and student share the same backbone and differ only in the attention mask over video tokens; future video is never generated at inference. Controlled experiments verify that this gain reflects a genuine future-conditioned correction rather than a side effect of capacity or regularization. Empirically, PFD achieves consistent improvements on LIBERO and RoboTwin manipulation benchmarks while preserving the current-only inference interface at negligible added latency. This view reframes the role of future information in world action models: not as a target to predict, nor as a regularizer to absorb, but as a compressible correction to be distilled.

---
