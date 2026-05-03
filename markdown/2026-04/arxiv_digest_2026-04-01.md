# arXiv Daily Digest — 2026-04-01

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 6

---

## 1. Enhancing Policy Learning with World-Action Model

**Authors:** Yuci Han, Alper Yilmaz
**arXiv:** [2603.28955](https://arxiv.org/abs/2603.28955)
**Categories:** Artificial Intelligence (cs.AI)

This paper presents the World-Action Model (WAM), an action-regularized world model that jointly reasons over future visual observations and the actions that drive state transitions. Unlike conventional world models trained solely via image prediction, WAM incorporates an inverse dynamics objective into DreamerV2 that predicts actions from latent state transitions, encouraging the learned representations to capture action-relevant structure critical for downstream control. We evaluate WAM on enhancing policy learning across eight manipulation tasks from the CALVIN benchmark. We first pretrain a diffusion policy via behavioral cloning on world model latents, then refine it with model-based PPO inside the frozen world model. Without modifying the policy architecture or training procedure, WAM improves average behavioral cloning success from 59.4% to 71.2% over DreamerV2 and DiWA baselines. After PPO fine-tuning, WAM achieves 92.8% average success versus 79.8% for the baseline, with two tasks reaching 100%, using 8.7x fewer training steps.

---

## 2. DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA

**Authors:** Yi Chen, Yuying Ge, Hui Zhou, ..., Yixiao Ge, Xihui Liu
**arXiv:** [2603.29844](https://arxiv.org/abs/2603.29844)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

The development of Vision-Language-Action (VLA) models has been significantly accelerated by pre-trained Vision-Language Models (VLMs). However, most existing end-to-end VLAs treat the VLM primarily as a multimodal encoder, directly mapping vision-language features to low-level actions. This paradigm underutilizes the VLM's potential in high-level decision making and introduces training instability, frequently degrading its rich semantic representations. To address these limitations, we introduce DIAL, a framework bridging high-level decision making and low-level motor execution through a differentiable latent intent bottleneck. Specifically, a VLM-based System-2 performs latent world modeling by synthesizing latent visual foresight within the VLM's native feature space; this foresight explicitly encodes intent and serves as the structural bottleneck. A lightweight System-1 policy then decodes this predicted intent together with the current observation into precise robot actions via latent inverse dynamics. To ensure optimization stability, we employ a two-stage training paradigm: a decoupled warmup phase where System-2 learns to predict latent futures while System-1 learns motor control under ground-truth future guidance within a unified feature space, followed by seamless end-to-end joint optimization. This enables action-aware gradients to refine the VLM backbone in a controlled manner, preserving pre-trained knowledge. Extensive experiments on the RoboCasa GR1 Tabletop benchmark show that DIAL establishes a new state-of-the-art, achieving superior performance with 10x fewer demonstrations than prior methods. Furthermore, by leveraging heterogeneous human demonstrations, DIAL learns physically grounded manipulation priors and exhibits robust zero-shot generalization to unseen objects and novel configurations during real-world deployment on a humanoid robot.

---

## 3. Learn2Fold: Structured Origami Generation with World Model Planning

**Authors:** Yanjia Huang, Yunuo Chen, Ying Jiang, ..., Yin Yang, Chenfanfu Jiang
**arXiv:** [2603.29585](https://arxiv.org/abs/2603.29585)
**Categories:** Graphics (cs.GR); Artificial Intelligence (cs.AI)

The ability to transform a flat sheet into a complex three-dimensional structure is a fundamental test of physical intelligence. Unlike cloth manipulation, origami is governed by strict geometric axioms and hard kinematic constraints, where a single invalid crease or collision can invalidate the entire folding sequence. As a result, origami demands long-horizon constructive reasoning that jointly satisfies precise physical laws and high-level semantic intent. Existing approaches fall into two disjoint paradigms: optimization-based methods enforce physical validity but require dense, precisely specified inputs, making them unsuitable for sparse natural language descriptions, while generative foundation models excel at semantic and perceptual synthesis yet fail to produce long-horizon, physics-consistent folding processes. Consequently, generating valid origami folding sequences directly from text remains an open challenge. To address this gap, we introduce Learn2Fold, a neuro-symbolic framework that formulates origami folding as conditional program induction over a crease-pattern graph. Our key insight is to decouple semantic proposal from physical verification. A large language model generates candidate folding programs from abstract text prompts, while a learned graph-structured world model serves as a differentiable surrogate simulator that predicts physical feasibility and failure modes before execution. Integrated within a lookahead planning loop, Learn2Fold enables robust generation of physically valid folding sequences for complex and out-of-distribution patterns, demonstrating that effective spatial intelligence arises from the synergy between symbolic reasoning and grounded physical simulation.

---

## 4. AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models

**Authors:** Mozhgan Pourkeshavatz, Tianran Liu, Nicholas Rhinehart
**arXiv:** [2603.28963](https://arxiv.org/abs/2603.28963)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Multi-agent traffic simulation is central to developing and testing autonomous driving systems. Recent data-driven simulators have achieved promising results, but rely heavily on supervised learning from labeled trajectories or semantic annotations, making it costly to scale their performance. Meanwhile, large amounts of unlabeled sensor data can be collected at scale but remain largely unused by existing traffic simulation frameworks. This raises a key question: How can a method harness unlabeled data to improve traffic simulation performance? In this work, we propose AutoWorld, a traffic simulation framework that employs a world model learned from unlabeled occupancy representations of LiDAR data. Given world model samples, AutoWorld constructs a coarse-to-fine predictive scene context as input to a multi-agent motion generation model. To promote sample diversity, AutoWorld uses a cascaded Determinantal Point Process framework to guide the sampling processes of both the world model and the motion model. Furthermore, we designed a motion-aware latent supervision objective that enhances AutoWorld's representation of scene dynamics. Experiments on the WOSAC benchmark show that AutoWorld ranks first on the leaderboard according to the primary Realism Meta Metric (RMM). We further show that simulation performance consistently improves with the inclusion of unlabeled LiDAR data, and study the efficacy of each component with ablations. Our method paves the way for scaling traffic simulation realism without additional labeling. Our project page contains additional visualizations and released code.

---

## 5. OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models

**Authors:** Tianran Liu, Shengwen Zhao, Mozhgan Pourkeshavarz, Weican Li, Nicholas Rhinehart
**arXiv:** [2603.28887](https://arxiv.org/abs/2603.28887)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Data-driven autonomous driving simulation has long been constrained by its heavy reliance on pre-recorded driving logs or spatial priors, such as HD maps. This fundamental dependency severely limits scalability, restricting open-ended generation capabilities to the finite scale of existing collected datasets. To break this bottleneck, we present OccSim, the first occupancy world model-driven 3D simulator. OccSim obviates the requirement for continuous logs or HD maps; conditioned only on a single initial frame and a sequence of future ego-actions, it can stably generate over 3,000 continuous frames, enabling the continuous construction of large-scale 3D occupancy maps spanning over 4 kilometers for simulation. This represents an >80x improvement in stable generation length over previous state-of-the-art occupancy world models. OccSim is powered by two modules: W-DiT based static occupancy world model and the Layout Generator. W-DiT handles the ultra-long-horizon generation of static environments by explicitly introducing known rigid transformations in architecture design, while the Layout Generator populates the dynamic foreground with reactive agents based on the synthesized road topology. With these designs, OccSim can synthesize massive, diverse simulation streams. Extensive experiments demonstrate its downstream utility: data collected directly from OccSim can pre-train 4D semantic occupancy forecasting models to achieve up to 67% zero-shot performance on unseen data, outperforming previous asset-based simulator by 11%. When scaling the OccSim dataset to 5x the size, the zero-shot performance increases to about 74%, while the improvement over asset-based simulators expands to 22.1%.

---

## 6. HCLSM: Hierarchical Causal Latent State Machines for Object-Centric World Modeling

**Authors:** Jaber Jaber, Osama Jaber
**arXiv:** [2603.29090](https://arxiv.org/abs/2603.29090)
**Categories:** Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

World models that predict future states from video remain limited by flat latent representations that entangle objects, ignore causal structure, and collapse temporal dynamics into a single scale. We present HCLSM, a world model architecture that operates on three interconnected principles: object-centric decomposition via slot attention with spatial broadcast decoding, hierarchical temporal dynamics through a three-level engine combining selective state space models for continuous physics, sparse transformers for discrete events, and compressed transformers for abstract goals, and causal structure learning through graph neural network interaction patterns. HCLSM introduces a two-stage training protocol where spatial reconstruction forces slot specialization before dynamics prediction begins. We train a 68M-parameter model on the PushT robotic manipulation benchmark from the Open X-Embodiment dataset, achieving 0.008 MSE next-state prediction loss with emerging spatial decomposition (SBD loss: 0.0075) and learned event boundaries. A custom Triton kernel for the SSM scan delivers 38x speedup over sequential PyTorch. The full system spans 8,478 lines of Python across 51 modules with 171 unit tests. Code: this https URL

---
