# arXiv Daily Digest — 2026-04-13

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 10

---

## 1. Learning Vision-Language-Action World Models for Autonomous Driving

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, ..., Bailan Feng, Chao Ma
**arXiv:** [2604.09059](https://arxiv.org/abs/2604.09059)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have recently achieved notable progress in end-to-end autonomous driving by integrating perception, reasoning, and control within a unified multimodal framework. However, they often lack explicit modeling of temporal dynamics and global world consistency, which limits their foresight and safety. In contrast, world models can simulate plausible future scenes but generally struggle to reason about or evaluate the imagined future they generate. In this work, we present VLA-World, a simple yet effective VLA world model that unifies predictive imagination with reflective reasoning to improve driving foresight. VLA-World first uses an action-derived feasible trajectory to guide the generation of the next-frame image, capturing rich spatial and temporal cues that describe how the surrounding environment evolves. The model then reasons over this self-generated future imagined frame to refine the predicted trajectory, achieving higher performance and better interpretability. To support this pipeline, we curate nuScenes-GR-20K, a generative reasoning dataset derived from nuScenes, and employ a three-stage training strategy that includes pretraining, supervised fine-tuning, and reinforcement learning. Extensive experiments demonstrate that VLA-World consistently surpasses state-of-the-art VLA and world-model baselines on both planning and future-generation benchmarks. Project page: this https URL

---

## 2. WOMBET: World Model-based Experience Transfer for Robust and Sample-efficient Reinforcement Learning

**Authors:** Mintae Kim, Koushil Sreenath
**arXiv:** [2604.08958](https://arxiv.org/abs/2604.08958)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Reinforcement learning (RL) in robotics is often limited by the cost and risk of data collection, motivating experience transfer from a source task to a target task. Offline-to-online RL leverages prior data but typically assumes a given fixed dataset and does not address how to generate reliable data for transfer. We propose \textit{World Model-based Experience Transfer} (WOMBET), a framework that jointly generates and utilizes prior data. WOMBET learns a world model in the source task and generates offline data via uncertainty-penalized planning, followed by filtering trajectories with high return and low epistemic uncertainty. It then performs online fine-tuning in the target task using adaptive sampling between offline and online data, enabling a stable transition from prior-driven initialization to task-specific adaptation. We show that the uncertainty-penalized objective provides a lower bound on the true return and derive a finite-sample error decomposition capturing distribution mismatch and approximation error. Empirically, WOMBET improves sample efficiency and final performance over strong baselines on continuous control benchmarks, demonstrating the benefit of jointly optimizing data generation and transfer.

---

## 3. LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving

**Authors:** Hao Shao, Letian Wang, Yang Zhou, ..., Wei Zhan, Hongsheng Li
**arXiv:** [2604.08719](https://arxiv.org/abs/2604.08719)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Recent years have seen remarkable progress in autonomous driving, yet generalization to long-tail and open-world scenarios remains a major bottleneck for large-scale deployment. To address this challenge, some works use LLMs and VLMs for vision-language understanding and reasoning, enabling vehicles to interpret rare and safety-critical situations when generating actions. Others study generative world models to capture the spatio-temporal evolution of driving scenes, allowing agents to imagine possible futures before acting. Inspired by human intelligence, which unifies understanding and imagination, we explore a unified model for autonomous driving. We present LMGenDrive, the first framework that combines LLM-based multimodal understanding with generative world models for end-to-end closed-loop driving. Given multi-view camera inputs and natural-language instructions, LMGenDrive generates both future driving videos and control signals. This design provides complementary benefits: video prediction improves spatio-temporal scene modeling, while the LLM contributes strong semantic priors and instruction grounding from large-scale pretraining. We further propose a progressive three-stage training strategy, from vision pretraining to multi-step long-horizon driving, to improve stability and performance. LMGenDrive supports both low-latency online planning and autoregressive offline video generation. Experiments show that it significantly outperforms prior methods on challenging closed-loop benchmarks, with clear gains in instruction following, spatio-temporal understanding, and robustness to rare scenarios. These results suggest that unifying multimodal understanding and generation is a promising direction for more generalizable and robust embodied decision-making systems.

---

## 4. Toward World Models for Epidemiology

**Authors:** Zeeshan Memon, Yiqi Su, Christo Kurisummoottil Thomas, ..., Liang Zhao, Naren Ramakrishnan
**arXiv:** [2604.09519](https://arxiv.org/abs/2604.09519)
**Categories:** Machine Learning (cs.LG)

World models have emerged as a unifying paradigm for learning latent dynamics, simulating counterfactual futures, and supporting planning under uncertainty. In this paper, we argue that computational epidemiology is a natural and underdeveloped setting for world models. This is because epidemic decision-making requires reasoning about latent disease burden, imperfect and policy-dependent surveillance signals, and intervention effects are mediated by adaptive human behavior. We introduce a conceptual framework for epidemiological world models, formulating epidemics as controlled, partially observed dynamical systems in which (i) the true epidemic state is latent, (ii) observations are noisy and endogenous to policy, and (iii) interventions act as sequential actions whose effects propagate through behavioral and social feedback. We present three case studies that illustrate why explicit world modeling is necessary for policy-relevant reasoning: strategic misreporting in behavioral surveillance, systematic delays in time-lagged signals such as hospitalizations and deaths, and counterfactual intervention analysis where identical histories diverge under alternative action sequences.

---

## 5. Toward Hardware-Agnostic Quadrupedal World Models via Morphology Conditioning

**Authors:** Mohamad H. Danesh, Chenhao Li, Amin Abyaneh, ..., Marco Hutter, Hsiu-Chin Lin
**arXiv:** [2604.08780](https://arxiv.org/abs/2604.08780)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

World models promise a paradigm shift in robotics, where an agent learns the underlying physics of its environment once to enable efficient planning and behavior learning. However, current world models are often hardware-locked specialists: a model trained on a Boston Dynamics Spot robot fails catastrophically on a Unitree Go1 due to the mismatch in kinematic and dynamic properties, as the model overfits to specific embodiment constraints rather than capturing the universal locomotion dynamics. Consequently, a slight change in actuator dynamics or limb length necessitates training a new model from scratch. In this work, we take a step towards a framework for training a generalizable Quadrupedal World Model (QWM) that disentangles environmental dynamics from robot morphology. We address the limitations of implicit system identification, where treating static physical properties (like mass or limb length) as latent variables to be inferred from motion history creates an adaptation lag that can compromise zero-shot safety and efficiency. Instead, we explicitly condition the generative dynamics on the robot's engineering specifications. By integrating a physical morphology encoder and a reward normalizer, we enable the model to serve as a neural simulator capable of generalizing across morphologies. This capability unlocks zero-shot control across a range of embodiments. We introduce, for the first time, a world model that enables zero-shot generalization to new morphologies for locomotion. While we carefully study the limitations of our method, QWM operates as a distribution-bounded interpolator within the quadrupedal morphology family rather than a universal physics engine, this work represents a significant step toward morphology-conditioned world models for legged locomotion.

---

## 6. 2D or 3D: Who Governs Salience in VLA Models? -- Tri-Stage Token Pruning Framework with Modality Salience Awareness

**Authors:** Zihao Zheng, Sicheng Tian, Zhihao Mao, ..., Guojie Luo, Xiang Chen
**arXiv:** [2604.09244](https://arxiv.org/abs/2604.09244)
**Categories:** Multimedia (cs.MM); Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision-Language-Action (VLA) models have emerged as the mainstream of embodied intelligence. Recent VLA models have expanded their input modalities from 2D-only to 2D+3D paradigms, forming multi-visual-modal VLA (MVLA) models. Despite achieving improved spatial perception, MVLA faces a greater acceleration demand due to the increased number of input tokens caused by modal expansion. Token pruning is an effective optimization methods tailored to MVLA models. However, existing token pruning schemes are designed for 2D-only VLA models, ignoring 2D/3D modality salience differences. In this paper, we follow the application process of multi-modal data in MVLA models and develop a tri-stage analysis to capture the discrepancy and dynamics of 2D/3D modality salience. Based on these, we propose a corresponding tri-stage token pruning framework for MVLA models to achieve optimal 2D/3D token selection and efficient pruning. Experiments show that our framework achieves up to a 2.55x inference speedup with minimal accuracy loss, while only costing 5.8% overhead. Our Code is coming soon.

---

## 7. Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory

**Authors:** Zile Wang, Zexiang Liu, Jiaxing Li, ..., Yangguang Li, Yahui Zhou
**arXiv:** [2604.08995](https://arxiv.org/abs/2604.08995)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

With the advancement of interactive video generation, diffusion models have increasingly demonstrated their potential as world models. However, existing approaches still struggle to simultaneously achieve memory-enabled long-term temporal consistency and high-resolution real-time generation, limiting their applicability in real-world scenarios. To address this, we present Matrix-Game 3.0, a memory-augmented interactive world model designed for 720p real-time longform video generation. Building upon Matrix-Game 2.0, we introduce systematic improvements across data, model, and inference. First, we develop an upgraded industrial-scale infinite data engine that integrates Unreal Engine-based synthetic data, large-scale automated collection from AAA games, and real-world video augmentation to produce high-quality Video-Pose-Action-Prompt quadruplet data at scale. Second, we propose a training framework for long-horizon consistency: by modeling prediction residuals and re-injecting imperfect generated frames during training, the base model learns self-correction; meanwhile, camera-aware memory retrieval and injection enable the base model to achieve long horizon spatiotemporal consistency. Third, we design a multi-segment autoregressive distillation strategy based on Distribution Matching Distillation (DMD), combined with model quantization and VAE decoder pruning, to achieve efficient real-time inference. Experimental results show that Matrix-Game 3.0 achieves up to 40 FPS real-time generation at 720p resolution with a 5B model, while maintaining stable memory consistency over minute-long sequences. Scaling up to a 2x14B model further improves generation quality, dynamics, and generalization. Our approach provides a practical pathway toward industrial-scale deployable world models.

---

## 8. Advantage-Guided Diffusion for Model-Based Reinforcement Learning

**Authors:** Daniele Foffano, Arvid Eriksson, David Broman, Karl H. Johansson, Alexandre Proutiere
**arXiv:** [2604.09035](https://arxiv.org/abs/2604.09035)
**Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Model-based reinforcement learning (MBRL) with autoregressive world models suffers from compounding errors, whereas diffusion world models mitigate this by generating trajectory segments jointly. However, existing diffusion guides are either policy-only, discarding value information, or reward-based, which becomes myopic when the diffusion horizon is short. We introduce Advantage-Guided Diffusion for MBRL (AGD-MBRL), which steers the reverse diffusion process using the agent's advantage estimates so that sampling concentrates on trajectories expected to yield higher long-term return beyond the generated window. We develop two guides: (i) Sigmoid Advantage Guidance (SAG) and (ii) Exponential Advantage Guidance (EAG). We prove that a diffusion model guided through SAG or EAG allows us to perform reweighted sampling of trajectories with weights increasing in state-action advantage-implying policy improvement under standard assumptions. Additionally, we show that the trajectories generated from AGD-MBRL follow an improved policy (that is, with higher value) compared to an unguided diffusion model. AGD integrates seamlessly with PolyGRAD-style architectures by guiding the state components while leaving action generation policy-conditioned, and requires no change to the diffusion training objective. On MuJoCo control tasks (HalfCheetah, Hopper, Walker2D and Reacher), AGD-MBRL improves sample efficiency and final return over PolyGRAD, an online Diffuser-style reward guide, and model-free baselines (PPO/TRPO), in some cases by a margin of 2x. These results show that advantage-aware guidance is a simple, effective remedy for short-horizon myopia in diffusion-model MBRL.

---

## 9. VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis

**Authors:** Xiaolei Lang, Yang Wang, Yukun Zhou, ..., Xiaofeng Wang, Zheng Zhu
**arXiv:** [2604.09330](https://arxiv.org/abs/2604.09330)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Recent advances in robot foundation models trained on large-scale human teleoperation data have enabled robots to perform increasingly complex real-world tasks. However, scaling these systems remains difficult because collecting task-specific demonstrations is expensive and labor-intensive. Synthetic data, especially generated videos, offer a promising direction, but existing World Models (WMs) are not directly suitable for policy learning since they do not provide paired action trajectories. World-Action (WA) models partially address this by predicting actions with visual outputs, yet often lack strong video-action alignment, while two-stage pipelines that generate video first and then infer actions introduce inefficiency and error accumulation. To address these limitations, we propose VAG, a unified flow-matching-based dual-stream framework that jointly generates video and action under visual and language conditioning. By synchronizing denoising in both branches and using an adaptive 3D pooling mechanism to transfer compact global video context to the action branch, VAG improves cross-modal consistency during generation. Across both simulated and real-world settings, VAG produces aligned video-action pairs with competitive prediction quality, supports executable trajectory replay, and provides useful synthetic pretraining data that improves downstream policy generalization, indicating its potential as a practical world-action model for embodied data synthesis.

---

## 10. V-CAGE: Vision-Closed-Loop Agentic Generation Engine for Robotic Manipulation

**Authors:** Yaru Liu, Ao-bo Wang, Nanyang Ye
**arXiv:** [2604.09036](https://arxiv.org/abs/2604.09036)
**Categories:** Robotics (cs.RO)

Scaling Vision-Language-Action (VLA) models requires massive datasets that are both semantically coherent and physically feasible. However, existing scene generation methods often lack context-awareness, making it difficult to synthesize high-fidelity environments embedded with rich semantic information, frequently resulting in unreachable target positions that cause tasks to fail prematurely. We present V-CAGE (Vision-Closed-loop Agentic Generation Engine), an agentic framework for autonomous robotic data synthesis. Unlike traditional scripted pipelines, V-CAGE operates as an embodied agentic system, leveraging foundation models to bridge high-level semantic reasoning with low-level physical interaction. Specifically, we introduce Inpainting-Guided Scene Construction to systematically arrange context-aware layouts, ensuring that the generated scenes are both semantically structured and kinematically reachable. To ensure trajectory correctness, we integrate functional metadata with a Vision-Language Model based closed-loop verification mechanism, acting as a visual critic to rigorously filter out silent failures and sever the error propagation chain. Finally, to overcome the storage bottleneck of massive video datasets, we implement a perceptually-driven compression algorithm that achieves over 90\% filesize reduction without compromising downstream VLA training efficacy. By centralizing semantic layout planning and visual self-verification, V-CAGE automates the end-to-end pipeline, enabling the highly scalable synthesis of diverse, high-quality robotic manipulation datasets.

---
