# arXiv Daily Digest — 2026-05-07

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 6

---

## 1. Executable World Models for ARC-AGI-3 in the Era of Coding Agents

**Authors:** Sergey Rodionov
**arXiv:** [2605.05138](https://arxiv.org/abs/2605.05138)
**Categories:** Artificial Intelligence (cs.AI)

We evaluate an initial coding-agent system for ARC-AGI-3 in which the agent maintains an executable Python world model, verifies it against previous observations, refactors it toward simpler abstractions as a practical proxy for an MDL-like simplicity bias, and plans through the model before acting. The system is intentionally direct: it uses a scripted controller, predefined world-model interfaces, verifier programs, and a plan executor, but no hand-coded game-specific logic. We report results on the 25 public ARC-AGI-3 games. Each recorded playthrough uses a fresh agent instance with no access to previous playthrough-specific files or conversation state. Most games have a single recorded playthrough; for a few games, we report multiple independent fresh-agent playthroughs to expose run-to-run variability. The agent fully solved 7 games, achieved a Relative Human Action Efficiency greater than 75%, on 6 games, and obtained a mean per-game RHAE of 32.58%. Because the system uses no game-specific code, it can serve as a game-general baseline for ARC-AGI-3. Performance on the private validation set remains to be tested. Overall, the results provide preliminary evidence that verifier-driven executable world models are a promising approach for ARC-AGI-3 agents.

---

## 2. Driver-WM: A Driver-Centric Traffic-Conditioned Latent World Model for In-Cabin Dynamics Rollout

**Authors:** Haozhuang Chi, Daosheng Qiu, Hao Su, ..., Haoruo Zhang, Chen Lv
**arXiv:** [2605.05092](https://arxiv.org/abs/2605.05092)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Safe L2/L3 driving automation requires anticipating human-in-the-loop reactions during shared-control transitions. While most driving world models forecast the external environment, in-cabin intelligence remains strictly recognition-oriented and lacks multi-step rollout capabilities for driver dynamics. We introduce Driver-WM, a driver-centric latent world model that rolls out in-cabin dynamics causally conditioned on out-cabin traffic context. This formulation unifies physical kinematics forecasting with auxiliary behavioral and emotional semantic recognition. Operating in a compact latent space constructed from frozen vision-language features, Driver-WM adopts a dual-stream architecture to separately encode external traffic and internal driver states. These streams are directionally coupled via a gated causal injection mechanism, which uses a learned vector gate to modulate external contextual perturbations while strictly enforcing temporal causality. Evaluations on a multi-task assistive driving benchmark demonstrate that Driver-WM yields robust long-horizon geometric forecasting for reactive high-motion maneuvers and improves semantic alignment for both driver and traffic states. Finally, the explicit external-to-internal conditioning allows for controlled test-time interventions to systematically analyze mechanism responses.

---

## 3. ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation

**Authors:** Wei Li, Jizhihui Liu, Li Yixing, ..., Rui Shao, Liqiang Nie
**arXiv:** [2605.05126](https://arxiv.org/abs/2605.05126)
**Categories:** Robotics (cs.RO)

Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions, but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often rely on additional sensors, introducing substantial computational overhead; 2) visual reasoning is typically limited to future-frame prediction, lacking alignment with the instruction-grounded scene and thus compromising spatiotemporal consistency. To address these challenges, we propose ConsisVLA-4D, a unified and efficient framework that enhances spatiotemporal consistency in 3D perception and 4D reasoning. Specifically, we design: 1) CV-Aligner, which ensures cross-view object semantic consistency by filtering instruction-relevant regions and aligning object identities across multiple viewpoints; 2) CO-Fuser, which guarantees cross-object spatial geometric consistency by eliminating spatial relation ambiguities between objects across views using compact latent representations. Building upon these, we introduce 3) CS-Thinker to achieve cross-scene spatiotemporal consistency as actions unfold. It learns implicit knowledge of local dynamics from object-semantic tokens of CV-Aligner and global depth from geometric tokens of CO-Fuser, thereby enhancing efficient visual reasoning under scene variations. Extensive experiments demonstrate that, benefiting from its efficient spatiotemporal consistency design, ConsisVLA-4D achieves 21.6% and 41.5% performance improvements, along with 2.3-fold and 2.4-fold inference speedups compared to OpenVLA on the LIBERO benchmark and real-world platforms, this http URL-4D is open-sourced and publicly available at

---

## 4. From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models

**Authors:** Yihan Lin, Haoyang Li, Yang Li, ..., Chao Shao, Jing Zhang
**arXiv:** [2605.04678](https://arxiv.org/abs/2605.04678)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a unified VLA baseline, we instantiate and compare four representative integration strategies. Our results reveal a formulation-task correspondence: image-based latent actions benefit long-horizon reasoning and scene-level generalization, whereas action-based latent actions excel at complex motor coordination. Furthermore, we find that directly supervising the VLM with discrete latent action tokens yields the most effective performance. Finally, our experiments offer initial insights into the benefits of latent action supervision in mixed-data, suggesting a promising direction for VLA training. Code is available at this https URL.

---

## 5. LoViF 2026 The First Challenge on Holistic Quality Assessment for 4D World Model (PhyScore)

**Authors:** Wei Luo, Yiting Lu, Xin Li, ..., Tianyi Yan, Huan Zheng
**arXiv:** [2605.05187](https://arxiv.org/abs/2605.05187)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

This paper reports on the LoViF 2026 PhyScore challenge, a competition on holistic quality assessment of world-model-generated videos across both 2D and 4D generation settings. The challenge is motivated by a central gap in current evaluation practice: perceptual quality alone is insufficient to judge whether generated dynamics are physically plausible, temporally coherent, and consistent with input conditions. Participants are required to build a metric that jointly predicts four dimensions, i.e., Video Quality, Physical Realism, Condition-Video Alignment, and Temporal Consistency. Depart from that, participants also need to localize physical anomaly timestamps for fine-grained diagnosis.
The benchmark dataset contains 1,554 videos generated by seven representative world generative models, organized into three tracks (text-2D, image-to-4D, and video-to-4D) and spanning 26 categories. These categories explicitly cover physics-relevant scenarios, including dynamics, optics, and thermodynamics, together with diverse real-world and creative content. To ensure label reliability, scores and anomaly timestamps are produced through trained human annotation with an additional automated quality-control pass.
Evaluation is based on both score prediction and anomaly localization, with a composite protocol that combines TimeStamp_IOU and SRCC/PLCC. This report summarizes the challenge design and provides method-level insights from submitted solutions.

---

## 6. Dream-MPC: Gradient-Based Model Predictive Control with Latent Imagination

**Authors:** Jonathan Spieler, Sven Behnke
**arXiv:** [2605.04568](https://arxiv.org/abs/2605.04568)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Robotics (cs.RO)

State-of-the-art model-based Reinforcement Learning (RL) approaches either use gradient-free, population-based methods for planning, learned policy networks, or a combination of policy networks and planning. Hybrid approaches that combine Model Predictive Control (MPC) with a learned model and a policy prior to leverage the advantages of both paradigms have shown promising results. However, these approaches typically rely on gradient-free optimization methods, which can be computationally expensive for high-dimensional control tasks. While gradient-based methods are a promising alternative, recent works have empirically shown that gradient-based methods often perform worse than their gradient-free counterparts. We propose Dream-MPC, a novel approach that generates few candidate trajectories from a rolled-out policy and optimizes each trajectory by gradient ascent using a learned world model, uncertainty regularization and amortization of optimization iterations over time by reusing previously optimized actions. Our results on 24 continuous control tasks show that Dream-MPC can significantly improve the performance of the underlying policy and can outperform gradient-free MPC and state-of-the-art baselines. We will open source our code and more at this https URL.

---
