# arXiv Daily Digest — 2026-04-30

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 4

---

## 1. Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising

**Authors:** Jun Guo, Qiwei Li, Peiyan Li, ..., Xinghang Li, Huaping Liu
**arXiv:** [2604.26694](https://arxiv.org/abs/2604.26694)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

We propose X-WAM, a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, addressing the critical limitations of prior unified world models (e.g., UWM) that only model 2D pixel-space and fail to balance action efficiency and world modeling quality. To leverage the strong visual priors of pretrained video diffusion models, X-WAM imagines the future world by predicting multi-view RGB-D videos, and obtains spatial information efficiently through a lightweight structural adaptation: replicating the final few blocks of the pretrained Diffusion Transformer into a dedicated depth prediction branch for the reconstruction of future spatial information. Moreover, we propose Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency. ANS applies a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video. Rather than entirely decoupling the timesteps during training, ANS samples from their joint distribution to align with the inference distribution. Pretrained on over 5,800 hours of robotic data, X-WAM achieves 79.2% and 90.7% average success rate on RoboCasa and RoboTwin 2.0 benchmarks, while producing high-fidelity 4D reconstruction and generation surpassing existing methods in both visual and geometric metrics.

---

## 2. Lifting Embodied World Models for Planning and Control

**Authors:** Alex N. Wang, Trevor Darrell, Pavel Izmailov, Yutong Bai, Amir Bar
**arXiv:** [2604.26182](https://arxiv.org/abs/2604.26182)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

World models of embodied agents predict future observations conditioned on an action taken by the agent. For complex embodiments, action spaces are high-dimensional and difficult to specify: for example, precisely controlling a human agent requires specifying the motion of each joint. This makes the world model hard to control and expensive to plan with as search-based methods like CEM scale poorly with action dimensionality. To address this issue, we train a lightweight policy that maps high-level actions to sequences of low-level joint actions. Composing this policy with the frozen world model produces a lifted world model that predicts a sequence of future observations from a single high-level action. We instantiate this framework for a human-like embodiment, defining the high-level action space as a small set of 2D waypoints annotated on the current observation frame, each specifying a near-term goal position for a leaf joint (pelvis, head, hands). Waypoints are low-dimensional, visually interpretable, and easy to specify manually or to search over. We show that the lifted world model substantially outperforms searching directly in low-level joint space ($3.8\times$ lower mean joint error to the goal pose), while remaining more compute-efficient and generalizing to environments unseen by the policy.

---

## 3. STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation

**Authors:** Yuxuan Tian, Yurun Jin, Bin Yu, ..., Kai Chen, Cong Huang
**arXiv:** [2604.26848](https://arxiv.org/abs/2604.26848)
**Categories:** Robotics (cs.RO)

Robotic manipulation critically requires reasoning about future spatial-temporal interactions, yet existing VLA policies and world-model-enhanced policies do not fully model action-relevant spatial-temporal interaction structure. We propose STARRY, a world-model-enhanced action-generation policy that aligns spatial-temporal prediction with action generation. STARRY jointly denoises future spatial-temporal latents and action sequences, and introduces Geometry-Aware Selective Attention Modulation to convert predicted depth and end-effector geometry into token-aligned weights for selective action-attention modulation. On RoboTwin 2.0, STARRY achieves 93.82% / 93.30% average success under Clean and Randomized settings. Real-world experiments further improve average success from 42.5% to 70.8% over $\pi_{0.5}$, demonstrating the effectiveness of action-centric spatial-temporal world modeling for spatial-temporally demanding robotic action generation.

---

## 4. World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning

**Authors:** Wanyue Zhang, Wenxiang Wu, Wang Xu, ..., Zitao Liu, Jiajun Zhang
**arXiv:** [2604.26934](https://arxiv.org/abs/2604.26934)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. Recent efforts address this limitation either by scaling spatial supervision with synthetic data or by coupling VLMs with world models at inference time. However, the former often lacks explicit modeling of motion-conditioned state transitions, while the latter incurs substantial computational overhead. In this work, we propose World2VLM, a training framework that distills spatial imagination from a generative world model into a vision-language model. Given an initial observation and a parameterized camera trajectory, we use a view-consistent world model to synthesize geometrically aligned future views and derive structured supervision for both forward (action-to-outcome) and inverse (outcome-to-action) spatial reasoning. We post-train the VLM with a two-stage recipe on a compact dataset generated by this pipeline and evaluate it on multiple spatial reasoning benchmarks. World2VLM delivers consistent improvements over the base model across diverse benchmarks, including SAT-Real, SAT-Synthesized, VSI-Bench, and MindCube. It also outperforms the test-time world-model-coupled methods while eliminating the need for expensive inference-time generation. Our results suggest that world models can serve not only as inference-time tools, but also as effective training-time teachers, enabling VLMs to internalize spatial imagination in a scalable and efficient manner.

---
