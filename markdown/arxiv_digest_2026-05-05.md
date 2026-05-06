# arXiv Daily Digest — 2026-05-05

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 17

---

## 1. Shadow-Loom: Causal Reasoning over Graphical World Model of Narratives

**Authors:** David Wilmot
**arXiv:** [2605.02475](https://arxiv.org/abs/2605.02475)
**Categories:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Stories hold a reader's attention because they have causes, secrets, and consequences. Shadow-Loom is an experimental open-source framework that turns a narrative into a versioned graphical world model and lets two engines act on it: a causal physics grounded in Pearl's ladder of causation and a recently proposed counterfactual calculus over Ancestral Multi-World Networks; and a narrative physics that scores the same graph against four structural reader-states -- mystery, dramatic irony, suspense, and surprise -- in the tradition of Sternberg's curiosity/suspense/surprise triad, with suspense formalised in the structural-affect line of work on story comprehension and computational suspense. Large language models are used only at the boundary: extraction, rendering, and audit; identification, intervention, and counterfactual reasoning are carried out in typed code over the graph. The system is offered as a research artefact rather than as a benchmarked NLP model; code, fixtures, and pipeline are released open source.

---

## 2. Latent State Design for World Models under Sufficiency Constraints

**Authors:** Keon Woo Kim
**arXiv:** [2605.01694](https://arxiv.org/abs/2605.01694)
**Categories:** Artificial Intelligence (cs.AI)

A world model matters to an agent only through the state it constructs. That state must preserve some information, discard other information, and support some future function: prediction, control, planning, memory, grounding, or counterfactual reasoning. This paper treats world-model research as latent state design under sufficiency constraints.
We propose a functional taxonomy that groups methods by what their latent state is for, rather than by architecture or application domain: predictive embedding, recurrent belief state, object/causal structure, latent action interface, grounded planning interface, and memory substrate. These roles expose distinctions that architecture-based groupings hide, including the gap between predictive sufficiency and control sufficiency, and the gap between passive video prediction and counterfactual action modeling.
The taxonomy supports an evaluation framework that judges a model by the sufficiency constraint its latent state was built to satisfy. We compare methods along seven axes: representation, prediction, planning, controllability, causal/counterfactual support, memory, and uncertainty. We use the resulting matrix as a diagnostic for what a latent state preserves, discards, and enables.
The conclusion that follows is that an actionable world model is the one whose state construction matches the task, not the one that preserves the most information.

---

## 3. VILAS: A VLA-Integrated Low-cost Architecture with Soft Grasping for Robotic Manipulation

**Authors:** Zijian An, Hadi Khezam, Bill Cai, ..., Zheng, Lifeng Zhou
**arXiv:** [2605.02037](https://arxiv.org/abs/2605.02037)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

We present VILAS, a fully low-cost, modular robotic manipulation platform designed to support end-to-end vision-language-action (VLA) policy learning and deployment on accessible hardware. The system integrates a Fairino FR5 collaborative arm, a Jodell RG52-50 electric gripper, and a dual-camera perception module, unified through a ZMQ-based communication architecture that seamlessly coordinates teleoperation, data collection, and policy deployment within a single framework. To enable safe manipulation of fragile objects without relying on explicit force sensing, we design a kirigami-based soft compliant gripper extension that induces predictable deformation under compressive loading, providing gentle and repeatable contact with delicate targets. We deploy and evaluate three state-of-the-art VLA models on the VILAS platform: pi_0, pi_0.5, and GR00T N1.6. All models are fine-tuned from publicly released pretrained checkpoints using an identical demonstration dataset collected via our teleoperation pipeline. Experiments on a grape grasping task validate the effectiveness of the proposed system, confirming that capable manipulation policies can be successfully trained and deployed on low-cost modular hardware. Our results further provide practical insights into the deployment characteristics of current VLA models in real-world settings.

---

## 4. TRAP: Tail-aware Ranking Attack for World-Model Planning

**Authors:** Siyuan Duan, Ke Zhang, Xizhao Luo
**arXiv:** [2605.01950](https://arxiv.org/abs/2605.01950)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

World models enable long-horizon planning by internally generating and evaluating imagined trajectories, making them a promising foundation for generalist agents. However, this imagination-driven decision process also introduces new security risks. Existing backdoor attacks typically aim to manipulate local features, one-step predictions, or instantaneous policy outputs. While such objectives may suffice for weaker reactive models, they are often ineffective against world models, where the learned dynamics prior and planning process can absorb or wash out the effects of shallow perturbations. More importantly, we find that world models exhibit a distinct backdoor vulnerability rooted in the long-tailed ranking structure of imagined trajectories, where disrupting the ordering of a few decision-critical trajectories can systematically hijack planning.
To exploit this vulnerability, we propose TRAP, a backdoor attack framework for world models that targets imagined trajectory ranking. TRAP combines a tail-aware ranking loss to focus optimization on decision-critical trajectories with dual gating mechanisms that stabilize optimization and regulate when and where the attack penalty is applied. Under trigger conditions, TRAP alters the relative ranking of imagined trajectories to redirect planning outcomes, while largely maintaining the normal ranking structure on clean inputs. Experiments on DreamerV3 and TD-MPC2 across diverse tasks show that TRAP consistently induces sustained behavioral deviations and significant performance degradation, highlighting the need for dedicated security evaluation of world-model-based agents.

---

## 5. Phone2Act: A Low-Cost, Hardware-Agnostic Teleoperation System for Scalable VLA Data Collection

**Authors:** Om Mandhane, Bipin Yadav, Sangeetha Prasanna Ram, Gopalakrishnan Narayanan
**arXiv:** [2605.01948](https://arxiv.org/abs/2605.01948)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Human-Computer Interaction (cs.HC)

Collecting diverse, high-quality manipulation data for Vision-Language-Action (VLA) model training remains prohibitively expensive for many research groups, as existing teleoperation frameworks rely on specialized hardware or are tightly coupled to specific robot platforms. We present Phone2Act, a low-cost, hardware-agnostic teleoperation framework that transforms a commodity smartphone into a 6-DoF robot controller via Google ARCore. Built on a modular ROS 2 architecture, Phone2Act decouples control logic from hardware specifics through interchangeable bridge nodes, supporting platforms from industrial cobots to low-cost bimanual arms without code modification. A Universal Recorder synchronizes multi-camera RGB streams with robot state feedback and exports demonstrations natively in the LeRobot dataset format, eliminating post-processing and enabling immediate VLA fine-tuning. We validate the framework by fine-tuning GR00T-N1.5 on 130 collected episodes, achieving a 90% success rate on a real-world multi-stage pick-and-place task deployed on a physical Dobot CR5.

---

## 6. Code World Model Preparedness Report

**Authors:** Daniel Song, Peter Ney, Cristina Menghini, ..., Shengjia Zhao, Summer Yue
**arXiv:** [2605.00932](https://arxiv.org/abs/2605.00932)
**Categories:** Software Engineering (cs.SE); Artificial Intelligence (cs.AI)

This report documents the preparedness assessment of Code World Model (CWM), a model for code generation and reasoning about code from Meta. We conducted pre-release testing across domains identified in our Frontier AI Framework as potentially presenting catastrophic risks, and also evaluated the model's misaligned propensities. Our assessment found that CWM does not pose additional frontier risks beyond those present in the current AI ecosystem. We therefore release it as an open-weight model.

---

## 7. Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation

**Authors:** Zhilong Zhang, Wenyu Luo, Haonan Wang, ..., Lei Yuan, Yang Yu
**arXiv:** [2605.01772](https://arxiv.org/abs/2605.01772)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied intelligence, enabling robots to perform tasks based on natural language instructions and current visual input. However, existing VLA models struggle with long-horizon tasks due to compounding errors. Prior methods decompose tasks into subtasks of fixed granularity, which cannot adapt to the varying complexity of execution states, limiting their robustness in long-horizon tasks. To overcome this, we introduce Anticipation Model, which adaptively and recursively generates future subgoals. This model continuously adapts as the task unfolds, adjusting future subgoals in response to evolving dynamics, facilitating more reliable planning paths. Building on this concept, we propose Anticipation-VLA, a hierarchical VLA model that leverages the anticipation model to generate actionable subgoals that guide VLA policy execution. We implement Anticipation-VLA with finetuning a Unified Multimodal Model (UMM) for high-level subgoal generation and a goal-conditioned VLA policy for low-level action execution. Experiments in both simulated and real-world robotic tasks demonstrate the effectiveness of Anticipation-VLA, highlighting the importance of adaptive and recursive subgoal generation for robust policy execution.

---

## 8. Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference

**Authors:** Yudong Liu, Yuan Li, Zijia Tang, ..., Yiran Chen, Hai Li
**arXiv:** [2605.02739](https://arxiv.org/abs/2605.02739)
**Categories:** Robotics (cs.RO)

Dual-system Vision-Language-Action (VLA) models achieve state-of-the-art robotic manipulation but are bottlenecked by the VLM backbone, which must
execute at every control step while producing temporally redundant features. We propose Latent Bridge, a lightweight model that predicts VLM output
deltas between timesteps, enabling the action head to operate on predicted outputs while the expensive VLM backbone is called only periodically. We
instantiate Latent Bridge on two architecturally distinct VLAs: GR00T-N1.6 (feature-space bridge) and {\pi}0.5 (KV-cache bridge), demonstrating that the
approach generalizes across VLA designs. Our task-agnostic DAgger training pipeline transfers across benchmarks without modification. Across four
LIBERO suites, 24 RoboCasa kitchen tasks, and the ALOHA sim transfer-cube task, Latent Bridge achieves 95-100% performance retention while reducing
VLM calls by 50-75%, yielding 1.65-1.73x net per-episode speedup.

---

## 9. VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model

**Authors:** Wenhao Li, Xiu Su, Dan Niu, ..., Shan You, Chang Xu
**arXiv:** [2605.01194](https://arxiv.org/abs/2605.01194)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have demonstrated remarkable capabilities and generalization in embodied manipulation. However, their decision-making relies on a fast, instinctive process that lacks deliberation. This strategy often leads to suboptimal or catastrophic actions when facing complex or ambiguous scenarios that require greater consideration. In this paper, we introduce \textbf{VLA-ATTC}, a framework that endows VLA models with adaptive test-time compute (TTC). VLA-ATTC employs an uncertainty-based ``cognitive clutch'' to dynamically transition from reflexive execution to a TTC deliberation phase when necessary. During TTC phase, a novel \textbf{Relative Action Critic} (RAC) model identifies the optimal action from generated candidates via pairwise comparisons. This relative mechanism replaces unstable absolute value estimation, significantly simplifying the learning objective. Furthermore, we introduce an efficient sampling strategy to amortize computational costs and an automated data pipeline that curates preference pairs without manual annotation. On the LIBERO-LONG benchmark, VLA-ATTC reduces the failure rate of the SOTA model PI0.5 by over 50\%. We will open-source all the code and weights.

---

## 10. Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery

**Authors:** Wenhao Li, Xiu Su, Yichao Cao, ..., Yi Chen, Chang Xu
**arXiv:** [2605.01191](https://arxiv.org/abs/2605.01191)
**Categories:** Robotics (cs.RO)

Vision-language-action (VLA) models have advanced the field of embodied manipulation by harnessing broad world knowledge and strong generalization. However, current VLA models still face several key challenges, including limited reasoning capability, lack of status monitoring, and difficulty in self-correction. In this paper, we introduce \textbf{Sentinel-VLA}, a metacognitive VLA model equipped with an active ``sentinel'' module to monitor real-time execution status. Only when necessary, such as during initial planning or upon detecting an error, the model triggers a dynamic reasoning or formulate error recovery solutions. This on-demand reasoning mechanism ensures robust decision-making while minimizing computational overhead. Notably, all training data (spanning 44 tasks and over 2.6 million transitions) is automatically generated and annotated through our designed pipeline. We also propose the Self-Evolving Continual Learning (SECL) algorithm, which allows Sentinel-VLA to identify its capability boundaries and automatically collect data for expansion, paired with Orthogonal Continual Adapter (OC-Adapter) to constrain parameter updates to an orthogonal space, thereby preventing catastrophic forgetting. Real-world experiments demonstrate that Sentinel-VLA boosts the task success rate by over 30\% compared to the SOTA model, PI0. We will open-source all the code, weights, and data generation pipeline.

---

## 11. Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation

**Authors:** Chenyu Hui, Xiaodi Huang, Siyu Xu, ..., Tao Huang, Chang Xu
**arXiv:** [2605.02757](https://arxiv.org/abs/2605.02757)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision-language-action (VLA) models typically rely on large-scale real-world videos, whereas simulated data, despite being inexpensive and highly parallelizable to collect, often suffers from a substantial visual domain gap and limited environmental diversity, resulting in weak real-world generalization. We present an efficient video augmentation framework that converts simulated VLA videos into realistic training videos while preserving task semantics and action trajectories. Our pipeline extracts structured conditions from simulation via video semantic segmentation and video captioning, rewrites captions to diversify environments, and uses a conditional video transfer model to synthesize realistic videos. To make augmentation practical at scale, we introduce a diffusion feature-reuse mechanism that reuses video tokens across adjacent timesteps to accelerate generation, and a coreset sampling strategy that identifies a compact, non-redundant subset for augmentation under limited computation. Extensive experiments on Robotwin 2.0, LIBERO, LIBERO-Plus, and a real robotic platform demonstrate consistent improvements. For example, our method improves RDT-1B by 8% on Robotwin 2.0, and boosts $\pi_0$ by 5.1% on the more challenging LIBERO-Plus benchmark. Code is available at: this https URL.

---

## 12. Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models

**Authors:** Junyuan Xiao, Dingkang Liang, Xin Zhou, ..., Jianlou Si, Wenming Yang
**arXiv:** [2605.01896](https://arxiv.org/abs/2605.01896)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Emerging multi-modal world models attempt to jointly generate videos across diverse modalities (e.g., RGB, depth, and mask), yet they fail to fully exploit the rich priors of existing foundation models. We propose $M^2$-REPA, the first representation alignment method tailored for multi-modal video generation. Our key insight is that foundation models trained on different modality spaces naturally capture distinct domain-specific priors, acting as complementary "experts." Specifically, we first decouple modality-specific features from the diffusion model's intermediate representations, then align each with its corresponding expert foundation model. To this end, we design two synergistic objectives: a multi-modal representation alignment loss that enforces feature-to-expert matching, and a modality-specific decoupling regularization that encourages complementarity across different modalities. This design enables joint optimization, fully exploiting priors from multiple foundation models. Extensive experiments demonstrate that our method significantly outperforms baselines in visual quality and long-term consistency.

---

## 13. Embody4D: A Generalist 4D World Model for Embodied AI

**Authors:** Peiyan Tu, Hanxin Zhu, Jingwen Sun, ..., Xiaoqian Cheng, Zhibo Chen
**arXiv:** [2605.01799](https://arxiv.org/abs/2605.01799)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

World models have made significant progress in modeling dynamic environments; however, most embodied world models are still restricted to 2D representations, lacking the comprehensive multi-view information essential for embodied spatial reasoning. Bridging this gap is non-trivial, primarily due to challenges from severe scarcity of paired multi-view data, the difficulty of maintaining spatiotemporal consistency in generated 3D geometries, and the tendency to hallucinate manipulation details. To address these challenges, we propose Embody4D, a dedicated video-to-video world model for embodied scenarios, capable of synthesizing arbitrary novel views from a monocular video. First, to tackle data scarcity, we introduce a 3D-aware compositional synthesis pipeline to curate a heterogeneous dataset compositing cross-embodiment robotic arms with diverse backgrounds, guaranteeing broad generalization. Second, to enforce geometric stability, we devise an adaptive noise injection strategy; by leveraging confidence disparities across image regions, this method selectively regularizes the diffusion process to ensure strict spatiotemporal consistency. Finally, to guarantee manipulation fidelity, we incorporate an interaction-aware attention mechanism that explicitly attends to the robotic interaction regions. Extensive experiments demonstrate that Embody4D achieves state-of-the-art performance, serving as a robust world model that synthesizes high-fidelity, view-consistent videos to empower downstream robotic planning and learning.

---

## 14. LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception

**Authors:** Justn williams, Kishor Datta Gupta, Roy George, Mrinmoy Sarkar
**arXiv:** [2605.00884](https://arxiv.org/abs/2605.00884)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action (VLA) models have shown strong semantic grounding and task generalization in manipulation, but aerial deployment remains difficult because drones require low-latency closed-loop guidance under strict onboard compute and communication constraints. We present LiteVLA-H, a compact 256M-parameter VLA system designed for dual-rate operation on an NVIDIA Jetson AGX Orin: a fast outer-loop guidance mode for short action-token outputs and a slower semantic mode for scene understanding, hazard description, and operator-facing narration. The central empirical observation is that, in this compact edge regime, end-to-end latency is dominated by multimodal pre-fill rather than by the marginal cost of decoding a few extra tokens. This motivates a scheduler that issues reactive action tokens at 50.65,ms (19.74,Hz) while still supporting sentence-level semantic outputs at 149.90--164.57\ms (6.08--6.67,Hz) on the same embedded platform. To specialize the model without collapsing its descriptive competence, we use a knowledge-preserving fine-tuning recipe that mixes reactive flight data, aerial semantic data, and generic caption/VQA supervision. Beyond reporting current latency measurements, we position the system against recent state-of-the-art architectures, including AnywhereVLA, FutureVLA, and ReMem-VLA, showing that the measured action branch reaches a higher edge inference rate under our deployment conditions while retaining periodic semantic awareness.

---

## 15. Adversarial Flow Matching for Imperceptible Attacks on End-to-End Autonomous Driving

**Authors:** Xinyu Zeng, Xiangkun He, Lei Tao, Chen Lv, Hong Cheng
**arXiv:** [2605.00880](https://arxiv.org/abs/2605.00880)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Autonomous driving (AD) is evolving towards end-to-end (E2E) frameworks through two primary paradigms: monolithic models exemplified by Vision-Language-Action (VLA), and specialized modular architectures. Despite their divergent designs, both paradigms increasingly rely on Transformer backbones for complex reasoning, potentially causing a shared vulnerability: visually imperceptible perturbations can manipulate E2E AD models into hazardous maneuvers by targeting the Transformer module. Most existing adversarial attack approaches against AD systems operate under white-box or black-box settings; yet, they typically necessitate full model transparency, or suffer from either prohibitive query latency or limited attack transferability. In this paper, we propose Adversarial Flow Matching (AFM), a novel gray-box attack framework that exploits Transformer structural vulnerabilities in E2E AD models. AFM enables efficient one-step generation of adversarial examples via a neural average velocity field. Additionally, the proposed technique yields effective and visually imperceptible attacks by synergistically perturbing the generative latent space and the neural average velocity field. Extensive experiments demonstrate that AFM achieves a superior trade-off between attack effectiveness and imperceptibility: it substantially degrades the performance of both VLA and modular AD agents across various scenarios compared to baselines, while maintaining state-of-the-art visual imperceptibility. Furthermore, adversarial examples generated by AFM exhibit robust cross-model transferability, indicating that AFM closely approximates a black-box attack setting while requiring only the prior knowledge that the target AD model incorporates a Transformer-based module.

---

## 16. MolmoAct2: Action Reasoning Models for Real-world Deployment

**Authors:** Haoquan Fang, Jiafei Duan, Donovan Clay, ..., Dieter Fox, Ranjay Krishna
**arXiv:** [2605.02881](https://arxiv.org/abs/2605.02881)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: this https URL

---

## 17. Video Generation with Predictive Latents

**Authors:** Yian Zhao, Feng Wang, Qiushan Guo, ..., Jian Zhang, Jie Chen
**arXiv:** [2605.02134](https://arxiv.org/abs/2605.02134)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video Variational Autoencoder (VAE) enables latent video generative modeling by mapping the visual world into compact spatiotemporal latent spaces, improving training efficiency and stability. While existing video VAEs achieve commendable reconstruction quality, continued optimization of reconstruction does not necessarily translate into improved generative performance. How to enhance the diffusability of video latents remains a critical and unresolved challenge. In this work, inspired by principles of predictive world modeling, we investigate the potential of predictive learning to improve the video generative modeling. To this end, we introduce a simple and effective predictive reconstruction objective that unifies predictive learning with video reconstruction. Specifically, we randomly discard future frames and encode only partial past observations, while training the decoder to reconstruct the observed frames and predict future ones simultaneously. This design encourages the latent space to encode temporally predictive structures and build a more coherent understanding of video dynamics, thereby improving generation quality. Our model, termed Predictive Video VAE (PV-VAE), achieves superior performance on video generation, with 52% faster convergence and a 34.42 FVD improvement over the Wan2.2 VAE on UCF101. Furthermore, comprehensive analyses demonstrate that PV-VAE not only exhibits favorable scalability, with generative performance improving alongside VAE training, but also yields consistent gains in downstream video understanding, underscoring a latent space that effectively captures temporal coherence and motion priors.

---
