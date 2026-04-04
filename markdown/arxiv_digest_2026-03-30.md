# arXiv Daily Digest — 2026-03-30

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 8

---

## 1. VLAgeBench: Benchmarking Large Vision-Language Models for Zero-Shot Human Age Estimation

**Authors:** Rakib Hossain Sajib, Md Kishor Morol, Rajan Das Gupta, Mohammad Sakib Mahmood, Shuvra Smaran Das
**arXiv:** [2603.26015](https://arxiv.org/abs/2603.26015)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Human age estimation from facial images represents a challenging computer vision task with significant applications in biometrics, healthcare, and human-computer interaction. While traditional deep learning approaches require extensive labeled datasets and domain-specific training, recent advances in large vision-language models (LVLMs) offer the potential for zero-shot age estimation. This study presents a comprehensive zero-shot evaluation of state-of-the-art Large Vision-Language Models (LVLMs) for facial age estimation, a task traditionally dominated by domain-specific convolutional networks and supervised learning. We assess the performance of GPT-4o, Claude 3.5 Sonnet, and LLaMA 3.2 Vision on two benchmark datasets, UTKFace and FG-NET, without any fine-tuning or task-specific adaptation. Using eight evaluation metrics, including MAE, MSE, RMSE, MAPE, MBE, $R^2$, CCC, and $\pm$5-year accuracy, we demonstrate that general-purpose LVLMs can deliver competitive performance in zero-shot settings. Our findings highlight the emergent capabilities of LVLMs for accurate biometric age estimation and position these models as promising tools for real-world applications. Additionally, we highlight performance disparities linked to image quality and demographic subgroups, underscoring the need for fairness-aware multimodal inference. This work introduces a reproducible benchmark and positions LVLMs as promising tools for real-world applications in forensic science, healthcare monitoring, and human-computer interaction. The benchmark focuses on strict zero-shot inference without fine-tuning and highlights remaining challenges related to prompt sensitivity, interpretability, computational cost, and demographic fairness.

---

## 2. Policy-Guided World Model Planning for Language-Conditioned Visual Navigation

**Authors:** Amirhosein Chahe, Lifeng Zhou
**arXiv:** [2603.25981](https://arxiv.org/abs/2603.25981)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Navigating to a visually specified goal given natural language instructions remains a fundamental challenge in embodied AI. Existing approaches either rely on reactive policies that struggle with long-horizon planning, or employ world models that suffer from poor action initialization in high-dimensional spaces. We present PiJEPA, a two-stage framework that combines the strengths of learned navigation policies with latent world model planning for instruction-conditioned visual navigation. In the first stage, we finetune an Octo-based generalist policy, augmented with a frozen pretrained vision encoder (DINOv2 or V-JEPA-2), on the CAST navigation dataset to produce an informed action distribution conditioned on the current observation and language instruction. In the second stage, we use this policy-derived distribution to warm-start Model Predictive Path Integral (MPPI) planning over a separately trained JEPA world model, which predicts future latent states in the embedding space of the same frozen encoder. By initializing the MPPI sampling distribution from the policy prior rather than from an uninformed Gaussian, our planner converges faster to high-quality action sequences that reach the goal. We systematically study the effect of the vision encoder backbone, comparing DINOv2 and V-JEPA-2, across both the policy and world model components. Experiments on real-world navigation tasks demonstrate that PiJEPA significantly outperforms both standalone policy execution and uninformed world model planning, achieving improved goal-reaching accuracy and instruction-following fidelity.

---

## 3. ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models

**Authors:** Yiru Wang, Anqing Jiang, Shuo Wang, ..., Zichong Gu, Hao Sun
**arXiv:** [2603.25766](https://arxiv.org/abs/2603.25766)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

The integration of Vision-Language-Action (VLA) models into autonomous driving systems offers a unified framework for interpreting complex scenes and executing control commands. However, the necessity to incorporate historical multi-view frames for accurate temporal reasoning imposes a severe computational burden, primarily driven by the quadratic complexity of self-attention mechanisms in Large Language Models (LLMs). To alleviate this bottleneck, we propose ETA-VLA, an Efficient Token Adaptation framework for VLA models. ETA-VLA processes the past $n$ frames of multi-view images and introduces a novel Intra-LLM Sparse Aggregator (ILSA). Drawing inspiration from human driver attention allocation, ILSA dynamically identifies and prunes redundant visual tokens guided by textual queries and temporal consistency. Specifically, we utilize a text-guided scoring mechanism alongside a diversity-preserving sparsification strategy to select a sparse subset of critical tokens, ensuring comprehensive awareness of the driving scene. Extensive experiments on the NAVSIM v2 demonstrate that ETA-VLA achieves driving performance comparable to state-of-the-art baselines while reducing computational FLOPs by approximately 32\%. Notably, our method prunes 85% of visual tokens and reduces inference FLOPs by 61\%, but still retaining 94% of the original accuracy on the NAVSIM v2 benchmark.

---

## 4. VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation

**Authors:** Zhide Zhong, Haodong Yan, Junfeng Li, ..., Tianran Zhang, Haoang Li
**arXiv:** [2603.26666](https://arxiv.org/abs/2603.26666)
**Categories:** Robotics (cs.RO)

Although pre-trained Vision-Language-Action (VLA) models exhibit impressive generalization in robotic manipulation, post-training remains crucial to ensure reliable performance during deployment. However, standard offline Supervised Fine-Tuning (SFT) suffers from distribution shifts and catastrophic forgetting of pre-trained capabilities, while online Reinforcement Learning (RL) struggles with sparse rewards and poor sample efficiency. In this paper, we propose On-Policy VLA Distillation (VLA-OPD), a framework bridging the efficiency of SFT with the robustness of RL. Instead of relying on sparse environmental rewards, VLA-OPD leverages an expert teacher to provide dense, token-level supervision on the student's self-generated trajectories. This enables active error correction on policy-induced states while preserving pre-trained general capabilities through gentle alignment. Crucially, we formulate VLA-OPD via a Reverse-KL objective. Unlike standard Forward-KL that induces mode-covering entropy explosion, or Hard-CE that causes premature entropy collapse, our bounded mode-seeking objective ensures stable policy learning by filtering out the teacher's epistemic uncertainty while maintaining action diversity. Experiments on LIBERO and RoboTwin2.0 benchmarks demonstrate that VLA-OPD significantly improves sample efficiency over RL and robustness over SFT, while effectively mitigating catastrophic forgetting during post-training.

---

## 5. Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate

**Authors:** Chen Yang, Yucheng Hu, Yunchao Ma, ..., Jing Tan, Haoqiang Fan
**arXiv:** [2603.26360](https://arxiv.org/abs/2603.26360)
**Categories:** Robotics (cs.RO)

In deployment of the VLA models to real-world robotic tasks, execution speed matters. In previous work arXiv:2510.26742 we analyze how to make neural computation of VLAs on GPU fast. However, we leave the question of how to actually deploy the VLA system on the real robots open. In this report we describe a set of practical techniques to achieve the end-to-end result of running a VLA-driven robot at an impressive speed in real world tasks that require both accuracy and dexterity. The stack of technology ranges across calibration, planning & control, and learning based method to identify optimal execution speed. In the tasks we show, the robot even executes in a speed on par with casual human operation and approaching the hardware limit of our lightweight arm. The unaccelerated videos and inference traces are provided in this https URL.

---

## 6. DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching

**Authors:** Jiayi Chen, Wenxuan Song, Shuai Chen, ..., Zhijun Li, Haoang Li
**arXiv:** [2603.26320](https://arxiv.org/abs/2603.26320)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision--Language--Action (VLA) models that encode actions using a discrete tokenization scheme are increasingly adopted for robotic manipulation, but existing decoding paradigms remain fundamentally limited. Whether actions are decoded sequentially by autoregressive VLAs or in parallel by discrete diffusion VLAs, once a token is generated, it is typically fixed and cannot be revised in subsequent iterations, so early token errors cannot be effectively corrected later. We propose DFM-VLA, a discrete flow matching VLA for iterative refinement of action tokens. DFM-VLA~models a token-level probability velocity field that dynamically updates the full action sequence across refinement iterations. We investigate two ways to construct the velocity field: an auxiliary velocity-head formulation and an action-embedding-guided formulation. Our framework further adopts a two-stage decoding strategy with an iterative refinement stage followed by deterministic validation for stable convergence. Extensive experiments on CALVIN, LIBERO, and real-world manipulation tasks show that DFM-VLA consistently outperforms strong autoregressive, discrete diffusion, and continuous diffusion baselines in manipulation performance while retaining high inference efficiency. In particular, DFM-VLA achieves an average success length of 4.44 on CALVIN and an average success rate of 95.7\% on LIBERO, highlighting the value of action refinement via discrete flow matching for robotic manipulation. Our project is available this https URL

---

## 7. DiffusionAnything: End-to-End In-context Diffusion Learning for Unified Navigation and Pre-Grasp Motion

**Authors:** Iana Zhura, Yara Mahmoud, Jeffrin Sam, ..., Miguel Altamirano Cabrera, Dzmitry Tsetserukou
**arXiv:** [2603.26322](https://arxiv.org/abs/2603.26322)
**Categories:** Robotics (cs.RO)

Efficiently predicting motion plans directly from vision remains a fundamental challenge in robotics, where planning typically requires explicit goal specification and task-specific design. Recent vision-language-action (VLA) models infer actions directly from visual input but demand massive computational resources, extensive training data, and fail zero-shot in novel scenes. We present a unified image-space diffusion policy handling both meter-scale navigation and centimeter-scale manipulation via multi-scale feature modulation, with only 5 minutes of self-supervised data per task. Three key innovations drive the framework: (1) Multi-scale FiLM conditioning on task mode, depth scale, and spatial attention enables task-appropriate behavior in a single model; (2) trajectory-aligned depth prediction focuses metric 3D reasoning along generated waypoints; (3) self-supervised attention from AnyTraverse enables goal-directed inference without vision-language models and depth sensors. Operating purely from RGB input (2.0 GB memory, 10 Hz), the model achieves robust zero-shot generalization to novel scenes while remaining suitable for onboard deployment.

---

## 8. World Reasoning Arena

**Authors:** PAN Team Institute of Foundation Models, Qiyue Gao, Kun Zhou, ..., Zhengzhong Liu, Eric Xing
**arXiv:** [2603.25887](https://arxiv.org/abs/2603.25887)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

World models (WMs) are intended to serve as internal simulators of the real world that enable agents to understand, anticipate, and act upon complex environments. Existing WM benchmarks remain narrowly focused on next-state prediction and visual fidelity, overlooking the richer simulation capabilities required for intelligent behavior. To address this gap, we introduce WR-Arena, a comprehensive benchmark for evaluating WMs along three fundamental dimensions of next world simulation: (i) Action Simulation Fidelity, the ability to interpret and follow semantically meaningful, multi-step instructions and generate diverse counterfactual rollouts; (ii) Long-horizon Forecast, the ability to sustain accurate, coherent, and physically plausible simulations across extended interactions; and (iii) Simulative Reasoning and Planning, the ability to support goal-directed reasoning by simulating, comparing, and selecting among alternative futures in both structured and open-ended environments. We build a task taxonomy and curate diverse datasets designed to probe these capabilities, moving beyond single-turn and perceptual evaluations. Through extensive experiments with state-of-the-art WMs, our results expose a substantial gap between current models and human-level hypothetical reasoning, and establish WR-Arena as both a diagnostic tool and a guideline for advancing next-generation world models capable of robust understanding, forecasting, and purposeful action. The code is available at this https URL.

---
