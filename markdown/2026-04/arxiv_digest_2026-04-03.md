# arXiv Daily Digest — 2026-04-03

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 13

---

## 1. World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry

**Authors:** Yuejiang Liu, Fan Feng, Lingjing Kong, ..., Chelsea Finn, Yilun Du
**arXiv:** [2604.01985](https://arxiv.org/abs/2604.01985)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Robotics (cs.RO)

General-purpose world models promise scalable policy evaluation, optimization, and planning, yet achieving the required level of robustness remains challenging. Unlike policy learning, which primarily focuses on optimal actions, a world model must be reliable over a much broader range of suboptimal actions, which are often insufficiently covered by action-labeled interaction data. To address this challenge, we propose World Action Verifier (WAV), a framework that enables world models to identify their own prediction errors and self-improve. The key idea is to decompose action-conditioned state prediction into two factors -- state plausibility and action reachability -- and verify each separately. We show that these verification problems can be substantially easier than predicting future states due to two underlying asymmetries: the broader availability of action-free data and the lower dimensionality of action-relevant features. Leveraging these asymmetries, we augment a world model with (i) a diverse subgoal generator obtained from video corpora and (ii) a sparse inverse model that infers actions from a subset of state features. By enforcing cycle consistency among generated subgoals, inferred actions, and forward rollouts, WAV provides an effective verification mechanism in under-explored regimes, where existing methods typically fail. Across nine tasks spanning MiniGrid, RoboMimic, and ManiSkill, our method achieves 2x higher sample efficiency while improving downstream policy performance by 18%.

---

## 2. DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning

**Authors:** Yang Zhou, Xiaofeng Wang, Hao Shao, ..., Guan Huang, Steven L. Waslander
**arXiv:** [2604.01765](https://arxiv.org/abs/2604.01765)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Recently, world-action models (WAM) have emerged to bridge vision-language-action (VLA) models and world models, unifying their reasoning and instruction-following capabilities and spatio-temporal world modeling. However, existing WAM approaches often focus on modeling 2D appearance or latent representations, with limited geometric grounding-an essential element for embodied systems operating in the physical world. We present DriveDreamer-Policy, a unified driving world-action model that integrates depth generation, future video generation, and motion planning within a single modular architecture. The model employs a large language model to process language instructions, multi-view images, and actions, followed by three lightweight generators that produce depth, future video, and actions. By learning a geometry-aware world representation and using it to guide both future prediction and planning within a unified framework, the proposed model produces more coherent imagined futures and more informed driving actions, while maintaining modularity and controllable latency. Experiments on the Navsim v1 and v2 benchmarks demonstrate that DriveDreamer-Policy achieves strong performance on both closed-loop planning and world generation tasks. In particular, our model reaches 89.2 PDMS on Navsim v1 and 88.7 EPDMS on Navsim v2, outperforming existing world-model-based approaches while producing higher-quality future video and depth predictions. Ablation studies further show that explicit depth learning provides complementary benefits to video imagination and improves planning robustness.

---

## 3. Causal Scene Narration with Runtime Safety Supervision for Vision-Language-Action Driving

**Authors:** Yun Li, Yidu Zhang, Simon Thompson, Ehsan Javanmardi, Manabu Tsukada
**arXiv:** [2604.01723](https://arxiv.org/abs/2604.01723)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models for autonomous driving must integrate diverse textual inputs, including navigation commands, hazard warnings, and traffic state descriptions, yet current systems often present these as disconnected fragments, forcing the model to discover on its own which environmental constraints are relevant to the current maneuver. We introduce Causal Scene Narration (CSN), which restructures VLA text inputs through intent-constraint alignment, quantitative grounding, and structured separation, at inference time with zero GPU cost. We complement CSN with Simplex-based runtime safety supervision and training-time alignment via Plackett-Luce DPO with negative log-likelihood (NLL) regularization. A multi-town closed-loop CARLA evaluation shows that CSN improves Driving Score by +31.1% on original LMDrive and +24.5% on the preference-aligned variant. A controlled ablation reveals that causal structure accounts for 39.1% of this gain, with the remainder attributable to information content alone. A perception noise ablation confirms that CSN's benefit is robust to realistic sensing errors. Semantic safety supervision improves Infraction Score, while reactive Time-To-Collision monitoring degrades performance, demonstrating that intent-aware monitoring is needed for VLA systems.

---

## 4. Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models

**Authors:** Jiawei Chen, Simin Huang, Jiawei Du, ..., Chao Yu, Zhaoxia Yin
**arXiv:** [2604.01618](https://arxiv.org/abs/2604.01618)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-language-action (VLA) models have shown strong performance in robotic manipulation, yet their robustness to physically realizable adversarial attacks remains underexplored. Existing studies reveal vulnerabilities through language perturbations and 2D visual attacks, but these attack surfaces are either less representative of real deployment or limited in physical realism. In contrast, adversarial 3D textures pose a more physically plausible and damaging threat, as they are naturally attached to manipulated objects and are easier to deploy in physical environments. Bringing adversarial 3D textures to VLA systems is nevertheless nontrivial. A central obstacle is that standard 3D simulators do not provide a differentiable optimization path from the VLA objective function back to object appearance, making it difficult to optimize through an end-to-end manner. To address this, we introduce Foreground-Background Decoupling (FBD), which enables differentiable texture optimization through dual-renderer alignment while preserving the original simulation environment. To further ensure that the attack remains effective across long-horizon and diverse viewpoints in the physical world, we propose Trajectory-Aware Adversarial Optimization (TAAO), which prioritizes behaviorally critical frames and stabilizes optimization with a vertex-based parameterization. Built on these designs, we present Tex3D, the first framework for end-to-end optimization of 3D adversarial textures directly within the VLA simulation environment. Experiments in both simulation and real-robot settings show that Tex3D significantly degrades VLA performance across multiple manipulation tasks, achieving task failure rates of up to 96.7\%. Our empirical results expose critical vulnerabilities of VLA systems to physically grounded 3D adversarial attacks and highlight the need for robustness-aware training.

---

## 5. ModTrans: Translating Real-world Models for Distributed Training Simulator

**Authors:** Yi Lyu
**arXiv:** [2604.01607](https://arxiv.org/abs/2604.01607)
**Categories:** Distributed, Parallel, and Cluster Computing (cs.DC); Artificial Intelligence (cs.AI)

Large-scale distributed training has been a research hot spot in machine learning systems for industry and academia in recent years. However, conducting experiments without physical machines and corresponding resources is difficult. One solution is to leverage distributed training simulators, but current ones like ASTRA-sim do not support importing real-world developed models, which poses challenges for ML researchers seeking to use them. Based on this challenge, we developed ModTrans, a translator supporting format translation from any real-world model to the ASTRA-sim simulator's input, removing the barrier between machine learning experts and machine learning system researchers. The experiment results show that ModTrans's cost is negligible.

---

## 6. Safety, Security, and Cognitive Risks in World Models

**Authors:** Manoj Parmar
**arXiv:** [2604.01346](https://arxiv.org/abs/2604.01346)
**Categories:** Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI); Machine Learning (cs.LG); Robotics (cs.RO)

World models -- learned internal simulators of environment dynamics -- are rapidly becoming foundational to autonomous decision-making in robotics, autonomous vehicles, and agentic AI. Yet this predictive power introduces a distinctive set of safety, security, and cognitive risks. Adversaries can corrupt training data, poison latent representations, and exploit compounding rollout errors to cause catastrophic failures in safety-critical deployments. World model-equipped agents are more capable of goal misgeneralisation, deceptive alignment, and reward hacking precisely because they can simulate the consequences of their own actions. Authoritative world model predictions further foster automation bias and miscalibrated human trust that operators lack the tools to audit.
This paper surveys the world model landscape; introduces formal definitions of trajectory persistence and representational risk; presents a five-profile attacker capability taxonomy; and develops a unified threat model extending MITRE ATLAS and the OWASP LLM Top 10 to the world model stack. We provide an empirical proof-of-concept on trajectory-persistent adversarial attacks (GRU-RSSM: A_1 = 2.26x amplification, -59.5% reduction under adversarial fine-tuning; stochastic RSSM proxy: A_1 = 0.65x; DreamerV3 checkpoint: non-zero action drift confirmed). We illustrate risks through four deployment scenarios and propose interdisciplinary mitigations spanning adversarial hardening, alignment engineering, NIST AI RMF and EU AI Act governance, and human-factors design. We argue that world models must be treated as safety-critical infrastructure requiring the same rigour as flight-control software or medical devices.

---

## 7. Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior

**Authors:** Haochen Niu, Kanyu Zhang, Shuyu Yin, ..., Peilin Liu, Fei Wen
**arXiv:** [2604.01570](https://arxiv.org/abs/2604.01570)
**Categories:** Robotics (cs.RO)

In real-world robotic manipulation, states typically admit a neighborhood of near-equivalent actions. That is, for each state, there exist a feasible action neighborhood (FAN) rather than a single correct action, within which motions yield indistinguishable progress. However, prevalent VLA training methodologies are directly inherited from linguistic settings and do not exploit the FAN property, thus leading to poor generalization and low sample efficiency. To address this limitation, we introduce a FAN-guided regularizer that shapes the model's output distribution to align with the geometry of FAN. Concretely, we introduce a Gaussian prior that promotes locally smooth and unimodal predictions around the preferred direction and magnitude. In extensive experiments across both reinforced finetuning (RFT) and supervised finetuning (SFT), our method achieves significant improvement in sample efficiency, and success rate in both in-distribution and out-of-distribution (OOD) scenarios. By aligning with the intrinsic action tolerance of physical manipulation, FAN-guided regularization provides a principled and practical method for sample-efficient, and generalizable VLA adaptation.

---

## 8. AnchorVLA: Anchored Diffusion for Efficient End-to-End Mobile Manipulation

**Authors:** Jia Syuen Lim, Zhizhen Zhang, Peter Bohm, ..., Zi Huang, Yadan Luo
**arXiv:** [2604.01567](https://arxiv.org/abs/2604.01567)
**Categories:** Robotics (cs.RO)

A central challenge in mobile manipulation is preserving multiple plausible action models while remaining reactive during execution. A bottle in a cluttered scene can often be approached and grasped in multiple valid ways. Robust behavior depends on preserving this action diversity while remaining reactive as the scene evolves. Diffusion policies are appealing because they model multimodal action distributions rather than collapsing to one solution. But in practice, full iterative denoising is costly at control time. Action chunking helps amortize inference, yet it also creates partially open-loop behavior, allowing small mismatches to accumulate into drift. We present AnchorVLA, a diffusion-based VLA policy for mobile manipulation built on the core insight that when sampling begins near a plausible solution manifold, extensive denoising is unnecessary to recover multimodal, valid actions. AnchorVLA combines a lightweight VLA adaptation backbone with an anchored diffusion action head, which denoises locally around anchor trajectories using a truncated diffusion schedule. This retains multimodal action generation while reducing inference cost for closed-loop control. Crucially, to mitigate chunking-induced drift, we introduce a test-time self-correction mechanism via a lightweight residual correction module that makes high-frequency, per-step adjustments during rollout. Across diverse mobile manipulation tasks, AnchorVLA improves success and stability under disturbances and distribution shifts while maintaining low-latency inference. The source code is made available at this https URL.

---

## 9. UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models

**Authors:** Qiyao Zhang, Shuhua Zheng, Jianli Sun, ..., Yisheng Lv, Yonglin Tian
**arXiv:** [2604.02241](https://arxiv.org/abs/2604.02241)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Embodied visual tracking is crucial for Unmanned Aerial Vehicles (UAVs) executing complex real-world tasks. In dynamic urban scenarios with complex semantic requirements, Vision-Language-Action (VLA) models show great promise due to their cross-modal fusion and continuous action generation capabilities. To benchmark multimodal tracking in such environments, we construct a dedicated evaluation benchmark and a large-scale dataset encompassing over 890K frames, 176 tasks, and 85 diverse objects. Furthermore, to address temporal feature redundancy and the lack of spatial geometric priors in existing VLA models, we propose an improved VLA tracking model, UAV-Track VLA. Built upon the $\pi_{0.5}$ architecture, our model introduces a temporal compression net to efficiently capture inter-frame dynamics. Additionally, a parallel dual-branch decoder comprising a spatial-aware auxiliary grounding head and a flow matching action expert is designed to decouple cross-modal features and generate fine-grained continuous actions. Systematic experiments in the CARLA simulator validate the superior end-to-end performance of our method. Notably, in challenging long-distance pedestrian tracking tasks, UAV-Track VLA achieves a 61.76\% success rate and 269.65 average tracking frames, significantly outperforming existing baselines. Furthermore, it demonstrates robust zero-shot generalization in unseen environments and reduces single-step inference latency by 33.4\% (to 0.0571s) compared to the original $\pi_{0.5}$, enabling highly efficient, real-time UAV control. Data samples and demonstration videos are available at: this https URL\_VLA.

---

## 10. UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving

**Authors:** Yongkang Li, Lijun Zhou, Sixu Yan, ..., Haiyang Sun, Xinggang Wang
**arXiv:** [2604.02190](https://arxiv.org/abs/2604.02190)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision-Language-Action (VLA) models have recently emerged in autonomous driving, with the promise of leveraging rich world knowledge to improve the cognitive capabilities of driving systems. However, adapting such models for driving tasks currently faces a critical dilemma between spatial perception and semantic reasoning. Consequently, existing VLA systems are forced into suboptimal compromises: directly adopting 2D Vision-Language Models yields limited spatial perception, whereas enhancing them with 3D spatial representations often impairs the native reasoning capacity of VLMs. We argue that this dilemma largely stems from the coupled optimization of spatial perception and semantic reasoning within shared model parameters. To overcome this, we propose UniDriveVLA, a Unified Driving Vision-Language-Action model based on Mixture-of-Transformers that addresses the perception-reasoning conflict via expert decoupling. Specifically, it comprises three experts for driving understanding, scene perception, and action planning, which are coordinated through masked joint attention. In addition, we combine a sparse perception paradigm with a three-stage progressive training strategy to improve spatial perception while maintaining semantic reasoning capability. Extensive experiments show that UniDriveVLA achieves state-of-the-art performance in open-loop evaluation on nuScenes and closed-loop evaluation on Bench2Drive. Moreover, it demonstrates strong performance across a broad range of perception, prediction, and understanding tasks, including 3D detection, online mapping, motion forecasting, and driving-oriented VQA, highlighting its broad applicability as a unified model for autonomous driving. Code and model have been released at this https URL

---

## 11. F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling

**Authors:** Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, ..., Song Fu, Qing Yang
**arXiv:** [2604.01605](https://arxiv.org/abs/2604.01605)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

We present F3DGS, a federated 3D Gaussian Splatting framework for decentralized multi-agent 3D reconstruction. Existing 3DGS pipelines assume centralized access to all observations, which limits their applicability in distributed robotic settings where agents operate independently, and centralized data aggregation may be restricted. Directly extending centralized training to multi-agent systems introduces communication overhead and geometric inconsistency. F3DGS first constructs a shared geometric scaffold by registering locally merged LiDAR point clouds from multiple clients to initialize a global 3DGS model. During federated optimization, Gaussian positions are fixed to preserve geometric alignment, while each client updates only appearance-related attributes, including covariance, opacity, and spherical harmonic coefficients. The server aggregates these updates using visibility-aware aggregation, weighting each client's contribution by how frequently it observed each Gaussian, resolving the partial-observability challenge inherent to multi-agent exploration. To evaluate decentralized reconstruction, we collect a multi-sequence indoor dataset with synchronized LiDAR, RGB, and IMU measurements. Experiments show that F3DGS achieves reconstruction quality comparable to centralized training while enabling distributed optimization across agents. The dataset, development kit, and source code will be publicly released.

---

## 12. ActionParty: Multi-Subject Action Binding in Generative Video Games

**Authors:** Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, ..., Fabio Pizzati, Aliaksandr Siarohin
**arXiv:** [2604.02330](https://arxiv.org/abs/2604.02330)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Recent advances in video diffusion have enabled the development of "world models" capable of simulating interactive environments. However, these models are largely restricted to single-agent settings, failing to control multiple agents simultaneously in a scene. In this work, we tackle a fundamental issue of action binding in existing video diffusion models, which struggle to associate specific actions with their corresponding subjects. For this purpose, we propose ActionParty, an action controllable multi-subject world model for generative video games. It introduces subject state tokens, i.e. latent variables that persistently capture the state of each subject in the scene. By jointly modeling state tokens and video latents with a spatial biasing mechanism, we disentangle global video frame rendering from individual action-controlled subject updates. We evaluate ActionParty on the Melting Pot benchmark, demonstrating the first video world model capable of controlling up to seven players simultaneously across 46 diverse environments. Our results show significant improvements in action-following accuracy and identity consistency, while enabling robust autoregressive tracking of subjects through complex interactions.

---

## 13. Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying Text to 2D and 3D Generation

**Authors:** Chongjie Ye, Cheng Cao, Chuanyu Pan, ..., Yuanming Hu, Xiaoguang Han
**arXiv:** [2604.02289](https://arxiv.org/abs/2604.02289)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Recent multimodal large language models have achieved strong performance in unified text and image understanding and generation, yet extending such native capability to 3D remains challenging due to limited data. Compared to abundant 2D imagery, high-quality 3D assets are scarce, making 3D synthesis under-constrained. Existing methods often rely on indirect pipelines that edit in 2D and lift results into 3D via optimization, sacrificing geometric consistency. We present Omni123, a 3D-native foundation model that unifies text-to-2D and text-to-3D generation within a single autoregressive framework. Our key insight is that cross-modal consistency between images and 3D can serve as an implicit structural constraint. By representing text, images, and 3D as discrete tokens in a shared sequence space, the model leverages abundant 2D data as a geometric prior to improve 3D representations. We introduce an interleaved X-to-X training paradigm that coordinates diverse cross-modal tasks over heterogeneous paired datasets without requiring fully aligned text-image-3D triplets. By traversing semantic-visual-geometric cycles (e.g., text to image to 3D to image) within autoregressive sequences, the model jointly enforces semantic alignment, appearance fidelity, and multi-view geometric consistency. Experiments show that Omni123 significantly improves text-guided 3D generation and editing, demonstrating a scalable path toward multimodal 3D world models.

---
