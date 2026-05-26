# arXiv Daily Digest — 2026-05-25

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 9

---

## 1. ChainFlow-VLA: Causal Flow Planning with Vision-Language Models

**Authors:** Xiyang Wang, Xinlin Wang, Tingguang Zhou, ..., Hangning Zhou, Mu Yang
**arXiv:** [2605.23270](https://arxiv.org/abs/2605.23270)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Current end-to-end autonomous driving systems are fundamentally limited by a mismatch between temporal causal reasoning and global trajectory consistency. Autoregressive (AR) models capture interaction-aware temporal dependencies via causal factorization, but their step-wise decoding leads to error accumulation and suboptimal global structure. In contrast, diffusion models optimize trajectories globally but lack explicit causal constraints, making them unreliable in interactive and safety-critical scenarios. This dichotomy reveals a deeper issue: existing methods treat causal modeling and global optimization as separate paradigms, without a principled way to unify them within a single trajectory distribution. To address this, we propose ChainFlow-VLA, which unifies causal generation and global refinement within a unified probabilistic framework. We formulate planning as a mixture over AR-induced modes and learn Vision-Language Model (VLM)-conditioned residual distributions over these modes. An autoregressive generator (Chain) produces a discrete set of causal trajectory modes, followed by a diffusion-based refiner (Flow) that leverages VLM hidden states as semantic priors to perform mode-conditioned correction in residual space while preserving causal structure. This straightforward conditioning seamlessly injects high-level scene understanding into fine-grained trajectory adjustments. Experiments demonstrate that ChainFlow-VLA achieves robust planning in ambiguous and long-tail scenarios, achieving a state-of-the-art score of 94.85 on the NAVSIM v1 leaderboard, matching human-level performance (94.8). Code will be available at this https URL.

---

## 2. Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models

**Authors:** Ruofan Jin, Zaixi Zhang
**arXiv:** [2605.22896](https://arxiv.org/abs/2605.22896)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models have emerged as a promising paradigm for robotic manipulation by leveraging pre-trained vision-language representations. However, current VLA training methods suffer from two critical limitations: poor generalization to novel environments and low training efficiency requiring extensive demonstrations. We introduce Agentic-VLA, an agentic training framework that enables VLAs to efficiently adapt online through three key innovations: (1) Adaptive Reward Synthesis, which dynamically generates and adjusts reward functions based on the VLA's current capabilities and task complexity, decomposing complex tasks into learnable sub-goals for curriculum learning; (2) Language-Guided Exploration, where a critic model provides structured guidance for systematic exploration rather than random sampling; and (3) Experience Memory,which stores and retrieves task-relevant policy weights for warm-starting adaptation to similar tasks. We evaluate Agentic-VLA on the LIBERO benchmark, achieving substantial improvements: +12.3% on long-horizon tasks, +28.5% in 1-shot learning, and enabling cross-task transfer from 0% to 31.2% without task-specific demonstrations. Our framework also demonstrates 2.4x faster convergence compared to existing online adaptation methods. Beyond LIBERO, Agentic-VLA retains its advantage on the dual-arm RoboTwin 2.0 benchmark, including under its randomized Hard setting. These results establish Agentic-VLA as a significant step toward truly adaptive VLA systems capable of continuous learning in deployment.

---

## 3. WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents

**Authors:** Zhixiang Guo, Siyuan Liang, Shi Fu, ..., Mark Jelasity, Dacheng Tao
**arXiv:** [2605.23220](https://arxiv.org/abs/2605.23220)
**Categories:** Machine Learning (cs.LG)

Despite the growing use of world models as decision-making agents, their adversarial robustness remains underexplored due to the lack of dedicated automated evaluation methods. A key obstacle is that attack evaluation must be both accurate and efficient: weak manually tuned attacks can overestimate robustness, while exhaustive hyperparameter search is prohibitively expensive because each candidate requires closed-loop rollouts through learned latent dynamics. We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents. WMAttack formulates robustness evaluation as a finite-budget search over attack configurations, including attack families, perturbation budgets, optimization steps, restarts, and allocation rules. To improve search accuracy, Self-Correcting Attack Search (SCAS) refines the attack proposal distribution using feedback from reward degradation, action instability, runtime cost, and rollout variability. To improve search efficiency, Representation-Guided Attack Retrieval (RGAR) retrieves effective historical configurations from representation-similar tasks, providing a warm start for unseen environments. We provide a theoretical explanation showing that proposal refinement improves finite-budget search when it shifts probability mass toward high-utility attacks. Across Atari and DeepMind Control tasks, WMAttack consistently discovers stronger attacks than the evaluated baselines, improving normalized reward drop from 0.497 to 1.034 on DreamerV3 Atari and from 0.319 to 0.682 on DMC. Ablations further show that RGAR improves initial candidate quality and SCAS improves final attack utility under fixed evaluation budgets.

---

## 4. World Machine: Towards Generative World Modeling for Time-Series

**Authors:** Elton Cardoso do Nascimento, Alexandre da Silva Simões, Esther Luna Colombini, Ricardo Ribeiro Gudwin, Paula Dornhofer Paro Costa
**arXiv:** [2605.23025](https://arxiv.org/abs/2605.23025)
**Categories:** Machine Learning (cs.LG)

World models represent a paradigm shift in generative AI, pursuing predictive understanding and controllable simulation of environments in a structured and generalizable way. We present World Machine, a generative world-modeling architecture for time series. It is a transformer-based architecture with latent states that enables adaptation to different amounts of observed data and contexts. This shows an improvement over traditional transformers, which have a computational and memory cost that scales quadratically with the context. Experiments on a proposed synthetic dataset, Toy1D, validate the approach's feasibility, demonstrate capabilities not found in conventional transformers, and highlight the contributions of each component of the training protocol.

---

## 5. Point Tracking Improves World Action Models

**Authors:** Jiarui Guan, Wenshuai Zhao, Yue Pei, ..., Arno Solin, Juho Kannala
**arXiv:** [2605.23856](https://arxiv.org/abs/2605.23856)
**Categories:** Robotics (cs.RO)

Robot policy learning benefits from world-action models that capture environment dynamics, but pixel-level prediction entangles dynamics with nuisance factors such as lighting and texture, making learned representations vulnerable to task-irrelevant visual variation. We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer. The key insight is that tracks provide an explicit representation of motion that captures long-horizon dynamics and remains robust under occlusion or partial out-of-frame motion, offering greater utility than modeling pixel appearance alone. On LIBERO and real-world LeRobot tasks, JOPAT improves over pixel-based baselines, with the largest gains on long-horizon tasks involving occlusion, object interaction, and off-screen motion.

---

## 6. $π_0$-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control

**Authors:** Huanming Liu, Congsheng Xu, Jianmin Ji, Yao Mu
**arXiv:** [2605.23128](https://arxiv.org/abs/2605.23128)
**Categories:** Robotics (cs.RO)

Currently, Vision-Language-Action (VLA) models have become the most adopted paradigm for robotic manipulation for its great potential for task generalization. While most generative flow-matching action decoders for VLA control are often deployed with fixed sampling horizons, limiting state-dependent compute and temporal reuse across control cycles. We present $\pi_0$-EqM, which replaces the flow-matching expert in $\pi_0$ with an Equilibrium Matching (EqM) decoder while leaving the upstream VLA stack unchanged. Under a matched 300-step budget, $\pi_0$-EqM improves RoboTwin average success from 40.4% to 50.2% across 19 tasks and remains competitive on LIBERO, with its clearest gain on LIBERO-10 (87.0%). Two threshold scans reveal a task-dependent non-monotonic relation between residual and success, which we term the stationarity--executability gap. The results suggest that inference depth in iterative VLA control is part of policy design and introduce an energy-based VLA perspective that may inform future work on composable action generation across tasks and embodiments.

---

## 7. GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation

**Authors:** Kaichen Zhou, Yuzhen Chen, Fangneng Zhan, ..., Paul Pu Liang, Mengyu Wang
**arXiv:** [2605.22882](https://arxiv.org/abs/2605.22882)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Video world models can generate realistic futures from a single instruction, but they often fail to preserve consistent point-level motion over time. As a result, the generated videos appear plausible, yet lack the physical grounding required for reliable action execution, such as robot manipulation. We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision, distilled from a pretrained geometry foundation model, into the video generative backbone during training. This supervision enables the model to jointly capture appearance and geometric structure while retaining a single-stream architecture with no additional inference cost. We further introduce an inverse dynamics module that converts correspondence-consistent video rollouts into executable robot trajectories, enabling direct deployment in both real-world and simulated manipulation. GEM-4D achieves state-of-the-art performance on both video prediction and geometric consistency across simulation and realistic scenarios and improves real-world manipulation success from 61% to 81%. Additional results are available at the project page: this https URL.

---

## 8. SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models

**Authors:** Zizhao Tong, Hongfeng Lai, Zeqing Wang, ..., Yeying Jin, Ling Shao
**arXiv:** [2605.23345](https://arxiv.org/abs/2605.23345)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Interactive world models for first-person shooter (FPS) games must resolve high-frequency overlapping control signals at every frame without disrupting unaffected regions. Existing methods inject actions globally and train on single titles, failing under dense FPS inputs. We observe that FPS actions are spatially selective: discrete events such as firing or reloading affect only a localized region around the weapon (the scope), while continuous camera and movement signals govern stable surroundings. We propose SCOPE, which inserts a conditioning module into each transformer block of a pretrained video diffusion model. It reshapes features into per-pixel temporal sequences so that each position computes its action response from local visual content. This separates in-scope effects from out-of-scope generation without segmentation labels. We also introduce CrossFPS, the first multi-game FPS dataset with frame-aligned action telemetry. It comprises 69K clips from 7 titles with 10-DoF controller signals, curated to remove gameplay bias. The model learns general visual-to-action mappings rather than game-specific patterns, enabling zero-shot transfer to unseen scenes. Experiments confirm strong action responsiveness, precise scope separation, and effective cross-game generalization.

---

## 9. Dreaming Smoothly and Sample Efficiently with Gradient Penalized Latent Dynamics

**Authors:** Romil V. Sonigra, P. R. Kumar
**arXiv:** [2605.23089](https://arxiv.org/abs/2605.23089)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Model-based reinforcement learning improves sample efficiency by learning a world model. However, existing latent world models such as DreamerV3 do not explicitly enforce local smoothness in their learned transition dynamics, leaving a useful inductive bias for transition dynamics learning unexploited. We propose GPLD, a gradient-penalized latent dynamics regularizer for DreamerV3 that applies a row-wise Jacobian penalty to the posterior latent distribution to encourage locally smooth transition learning. We show that this penalty can be interpreted as the continuous-latent analog of finite-difference smoothing of transition laws in discrete embedded-state MDPs, and estimate it efficiently using Hutchinson-style stochastic probes. Empirically, across DeepMind Control proprioceptive tasks, GPLD improves aggregate sample efficiency, with particularly strong gains on higher-complexity locomotion environments. On more challenging quadruped tasks, GPLD reaches high-return behavior earlier and exhibits more consistent late-stage learning over longer horizons. Explicit local smoothness regularization is a simple and effective way to improve latent world models for smooth continuous control environments. Code for GPLD is available at this http URL .

---
