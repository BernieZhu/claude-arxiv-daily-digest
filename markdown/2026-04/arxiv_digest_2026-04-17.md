# arXiv Daily Digest — 2026-04-17

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 3

---

## 1. Learning Ad Hoc Network Dynamics via Graph-Structured World Models

**Authors:** Can Karacelebi, Yusuf Talha Sahin, Elif Surer, Ertan Onur
**arXiv:** [2604.14811](https://arxiv.org/abs/2604.14811)
**Categories:** Machine Learning (cs.LG); Multiagent Systems (cs.MA); Networking and Internet Architecture (cs.NI)

Ad hoc wireless networks exhibit complex, innate and coupled dynamics: node mobility, energy depletion and topology change that are difficult to model analytically. Model-free deep reinforcement learning requires sustained online interaction whereas existing model based approaches use flat state representations that lose per node structure. Therefore we propose G-RSSM, a graph structured recurrent state space model that maintains per node latent states with cross node multi head attention to learn the dynamics jointly from offline trajectories. We apply the proposed method to the downstream task clustering where a cluster head selection policy trains entirely through imagined rollouts in the learned world model. Across 27 evaluation scenarios spanning MANET, VANET, FANET, WSN and tactical networks with N=30 to 1000 nodes, the learned policy maintains high connectivity with only trained for N=50. Herein, we propose the first multi physics graph structured world model applied to combinatorial per node decision making in size agnostic wireless ad hoc networks.

---

## 2. World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems

**Authors:** Runze Li, Hongyin Zhang, Junxi Jin, ..., Shangke Lyu, Donglin Wang
**arXiv:** [2604.14732](https://arxiv.org/abs/2604.14732)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models have emerged as a promising paradigm for building embodied agents that ground perception and language into action. However, most existing approaches rely on direct action prediction, lacking the ability to reason over long-horizon trajectories and evaluate their consequences, which limits performance in complex decision-making tasks. In this work, we introduce World-Value-Action (WAV) model, a unified framework that enables implicit planning in VLA systems. Rather than performing explicit trajectory optimization, WAV model learn a structured latent representation of future trajectories conditioned on visual observations and language instructions. A learned world model predicts future states, while a trajectory value function evaluates their long-horizon utility. Action generation is then formulated as inference in this latent space, where the model progressively concentrates probability mass on high-value and dynamically feasible trajectories. We provide a theoretical perspective showing that planning directly in action space suffers from an exponential decay in the probability of feasible trajectories as the horizon increases. In contrast, latent-space inference reshapes the search distribution toward feasible regions, enabling efficient long-horizon decision making. Extensive simulations and real-world experiments demonstrate that the WAV model consistently outperforms state-of-the-art methods, achieving significant improvements in task success rate, generalization ability, and robustness, especially in long-horizon and compositional scenarios.

---

## 3. HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds

**Authors:** Team HY-World, Chenjie Cao, Xuhui Zuo, ..., Tengfei Wang, Chunchao Guo
**arXiv:** [2604.14268](https://arxiv.org/abs/2604.14268)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

We introduce HY-World 2.0, a multi-modal world model framework that advances our prior project HY-World 1.0. HY-World 2.0 accommodates diverse input modalities, including text prompts, single-view images, multi-view images, and videos, and produces 3D world representations. With text or single-view image inputs, the model performs world generation, synthesizing high-fidelity, navigable 3D Gaussian Splatting (3DGS) scenes. This is achieved through a four-stage method: a) Panorama Generation with HY-Pano 2.0, b) Trajectory Planning with WorldNav, c) World Expansion with WorldStereo 2.0, and d) World Composition with WorldMirror 2.0. Specifically, we introduce key innovations to enhance panorama fidelity, enable 3D scene understanding and planning, and upgrade WorldStereo, our keyframe-based view generation model with consistent memory. We also upgrade WorldMirror, a feed-forward model for universal 3D prediction, by refining model architecture and learning strategy, enabling world reconstruction from multi-view images or videos. Also, we introduce WorldLens, a high-performance 3DGS rendering platform featuring a flexible engine-agnostic architecture, automatic IBL lighting, efficient collision detection, and training-rendering co-design, enabling interactive exploration of 3D worlds with character support. Extensive experiments demonstrate that HY-World 2.0 achieves state-of-the-art performance on several benchmarks among open-source approaches, delivering results comparable to the closed-source model Marble. We release all model weights, code, and technical details to facilitate reproducibility and support further research on 3D world models.

---
