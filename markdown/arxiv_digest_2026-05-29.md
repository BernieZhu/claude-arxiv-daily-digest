# arXiv Daily Digest — 2026-05-29

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 20

---

## 1. VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing

**Authors:** Haoyuan Shi, Xiancong Ren, Yingji Zhang, ..., Yong Dai, Xiaozhu Ju
**arXiv:** [2605.30117](https://arxiv.org/abs/2605.30117)
**Categories:** Artificial Intelligence (cs.AI)

Understanding how Vision-Language-Action (VLA) models transform multimodal knowledge into embodied control remains an open challenge. We present VLA-Trace, a progressive diagnostic framework that analyzes VLA models through a unified evidence chain from representation dynamics to causal control attribution and behavioral manifestation. It specifically combines cross-modal and checkpoint-drift centered kernel alignment (CKA) to trace representation evolution, attention knockout interventions to identify modality-specific control pathways, and rollout-level behavioral probes to examine grounding, shortcut dependence, and semantic following. Experiments on $\pi_{0.5}$ and OpenVLA reveal three key findings. First, the two models exhibit distinct modality-specific adaptation dynamics during VLA finetuning. Second, they rely on different multimodal routing strategies and layer-wise dependencies during action decoding. Third, although VLA policies excel at visually grounded trajectory generation, they remain limited in fine-grained semantic following. These findings highlight future directions for representation-preserving adaptation, causal VLA circuits, and compositional semantic control.

---

## 2. Toward AI Systems That Understand Self and Others: A Multi-Phase Inference Framework for Human Cognitive Diversity and World-Model Alignment

**Authors:** Toru Takahashi
**arXiv:** [2605.29930](https://arxiv.org/abs/2605.29930)
**Categories:** Artificial Intelligence (cs.AI); Computers and Society (cs.CY); Human-Computer Interaction (cs.HC)

Mutual misunderstanding in contemporary society does not arise merely because people hold different opinions or values. Even under the same observations, different subjects may form different inferential targets, state representations, prediction errors, and update priorities. This paper proposes a multi-phase inference framework and defines its core internal mechanism as the Multi-Phase Inference Mechanism (MIM). MIM formalizes how heterogeneous world models arise through a phase-formation space, a foregrounding field, subject-specific profile states, and alignment maps between state representations. On this basis, the paper reframes world-model alignment as the problem of making heterogeneous representations mutually processable, rather than forcing agreement or convergence to a single value system. It further connects this formalism to philosophical disagreements, cognitive typology, social fragmentation, and AI alignment. The aim is to provide a constructive vocabulary for AI systems that can help humans understand self and others by making differences in meaning, value, and prediction error visible, comparable, and transformable.

---

## 3. MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models

**Authors:** Tianzhuo Yang, Zihan Shen, Zirui Mi, ..., Boyuan Chen, Yaodong Yang
**arXiv:** [2605.29360](https://arxiv.org/abs/2605.29360)
**Categories:** Artificial Intelligence (cs.AI)

Action-conditioned world models are increasingly used as scalable simulators for robot learning, yet current evaluations provide limited evidence that their predictions are reliable under the actions they condition on. Existing benchmarks largely emphasize visual fidelity, leaving unclear whether predicted futures are physically plausible, faithful to commanded actions, and calibrated to failure when actions should not succeed. We introduce \textsc{MiraBench}, a hierarchical benchmark that defines \emph{action-conditioned reliability} as a core evaluation target for robotic world models. MiraBench decomposes this target into three progressively demanding levels: \emph{Physics Adherence}, which evaluates reference-free physical consistency; \emph{Action-Following Fidelity}, which measures whether predictions respect task-relevant action inputs; and \emph{Optimism Bias Detection}, which probes the tendency to predict successful outcomes under failure-inducing actions. To support this evaluation, we curate a human-annotated corpus with over 16,000 judgments across tasks, failure categories, and leading world models. We evaluate 12 representative model configurations spanning vector-conditioned robotic world models, text-conditioned generative world models, open-weight systems, closed-source systems, and multiple model scales. Across this broad model landscape, MiraBench reveals three central findings: visual fidelity is a poor proxy for action fidelity; increasing model scale does not reliably improve action following; and optimism bias is pervasive across current systems. By shifting evaluation from appearance to action-conditioned reliability, MiraBench provides a diagnostic foundation for assessing and improving robotic world models as faithful simulators.

---

## 4. Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments

**Authors:** Qiuyue Wang, Mingsheng Li, Jian Guan, ..., Tao Yu, Xionghui Chen
**arXiv:** [2605.30280](https://arxiv.org/abs/2605.30280)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Embodied intelligence is often studied through specialized models for individual tasks such as manipulation or navigation, resulting in fragmented capabilities and limited generalization across tasks, environments, and robot embodiments. In this work, we study whether heterogeneous embodied decision-making problems can be unified within a single vision-language-action model. We present Qwen-VLA, a unified embodied foundation model that extends Qwen's vision-language modeling stack from perception, understanding, and reasoning to continuous action and trajectory generation through a DiT-based action decoder. Qwen-VLA is trained with a large-scale joint pretraining recipe over diverse data sources, including robotics manipulation trajectories, human egocentric demonstrations, synthetic simulation data, vision-and-language navigation data, trajectory-centric supervision, and auxiliary vision-language data. To support multiple robot platforms, we introduce embodiment-aware prompt conditioning, where robot-specific textual descriptions specify the current embodiment and control convention. We further cast manipulation, navigation, and trajectory prediction into a unified action-and-trajectory prediction framework, enabling transferable visual grounding, spatial reasoning, and continuous action generation across robot morphologies, task families, and environments. Experiments on manipulation, navigation, and trajectory-centric benchmarks show consistent multi-task performance and out-of-distribution generalization under variations in scene layout, background, lighting, object configuration, and robot embodiment. Qwen-VLA-Instruct achieves 97.9% on LIBERO, 73.7% on Simpler-WidowX, 86.1%/87.2% on RoboTwin-Easy/Hard, 69.0% OSR on R2R, 59.6% SR on RxR, 76.9% average OOD success in real-world ALOHA experiments, and 26.6% zero-shot success on DOMINO dynamic manipulation.

---

## 5. BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models

**Authors:** Zhongxi Chen, Yifan Han, Yanming Shao, ..., Yao Mu, Wenzhao Lian
**arXiv:** [2605.30226](https://arxiv.org/abs/2605.30226)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have emerged as a promising paradigm for grounding visual-language understanding into real-world robotic manipulation. However, dexterous manipulation remains challenging for VLA policies due to high-dimensional hand control and compounding execution errors, which makes real-world RL post-training essential for bridging the gap between visually grounded action generation and physically reliable dexterous execution. However, high-dimensional dexterous exploration often triggers temporal inconsistency, sample inefficiency and hardware risks in the real world. To address these challenges, we propose BORA, an offline-to-online RL post-training framework designed for real-world dexterous VLA models. In the offline phase, BORA constructs a critic that takes both the VLM's cognition tokens and action chunks as inputs. This design enables action-conditioned value guidance, allowing the critic to evaluate dexterous hand motions beyond visual context alone. During the subsequent online phase, BORA freezes the VLA base and introduces a lightweight, Human-in-the-Loop (HiL) chunk-wise residual adaptation mechanism to mitigate real-world execution errors and further correct the offline-learned intents within the actual physical environment. By inheriting the offline critic and employing intervention-driven rewards, BORA effectively corrects execution discrepancies and adapts to real-world physical variances while preserving the pretrained policy as a stable prior. Extensive evaluations across five complex real-world dexterous tasks demonstrate that BORA significantly outperforms pure imitation learning and traditional decoupled RL baselines, achieving a 33% absolute increase in average success rate under standard settings and up to a 43% improvement in unseen object generalization.

---

## 6. VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies

**Authors:** Mingjian Gao, Wenqiao Zhang, Yuqian Yuan, ..., Siliang Tang, Yueting Zhuang
**arXiv:** [2605.30011](https://arxiv.org/abs/2605.30011)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Recent work has begun to equip vision-language-action (VLA) policies with explicit intermediate reasoning. In embodied control, however, textual chain-of-thought is a poor fit: irrelevant or weakly textual information can interfere with action prediction, while autoregressive text decoding adds too much latency for real-time closed-loop execution. We present VISUALTHINK-VLA, a visual intermediate-reasoning framework for accurate, low-latency VLA policies. Our bootstrapping philosophy is to guide action with effective visual thinking: VISUALTHINK-VLA bootstraps action prediction through a compact visual-evidence interface that preserves spatial precision while avoiding decoding overhead. Besides, to further improve performance and efficiency, VISUALTHINK-VLA adopts a tailored selective routing mechanism to learn the visual evidence tokens, enabling low-latency inference while preserving high-capacity specialization. We also introduce VisualEvidence-Kit, a supervision-and-audit resource centered on a VisualEvidence-Agent that constructs a 754.7k VLA instructions VisualEvidence-Set for route supervision and counterfactual faithfulness tests. Across multiple benchmarks and real-robot evaluation, VISUALTHINK-VLA achieves the highest success rate on most benchmarks while reducing the multi-second latency of reasoning-augmented baselines to the sub-second regime. For example, on BridgeData V2, it reduces step latency from 8.377,s with ECoT to 0.367,s, achieving a 22.8 times speedup.

---

## 7. VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models

**Authors:** Shengyu Si, Yuanzhuo Lu, Ruimeng Yang, ..., Zuxuan Wu, Yu-Gang Jiang
**arXiv:** [2605.29562](https://arxiv.org/abs/2605.29562)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action~(VLA) models have shown strong potential for general-purpose robotic manipulation, yet they still struggle to generalize to unseen tasks that necessitate transferring relevant experience across objects, scenes, and action patterns. This paper proposes VLA-Pro, a plug-and-play framework designed to enhance cross-task generalization by storing task-relevant procedural memories at training time and transferring these memories during inference. Specifically, VLA-Pro stores task-specific LoRA adapters as parameterized procedural memories during training. At inference time, VLA-Pro retrieves relevant procedural memories based on the current multi-modal context and dynamically fuses these memories for generating the current action chunk. Experiments on RoboTwin, RLBench, and real-world manipulation tasks show that VLA-Pro consistently improves cross-task generalization across multiple backbones, achieving up to a 207% relative improvement in simulation and increasing real-world success rate from 5.8% to 65.0%. These results suggest that procedural memory retrieval and adaptation provide an effective mechanism for transferring manipulation experience to novel tasks while preserving modularity and execution stability.

---

## 8. Emergent Semantic Representations in World Models through Physical Interaction without Linguistic Supervision

**Authors:** Jiayi Fang
**arXiv:** [2605.28865](https://arxiv.org/abs/2605.28865)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

What does a world model learn from physical exploration, without any linguistic supervision? We argue the answer is organized by a single principle: the geometric structure of the physical world. Training a VAE-based world model on random embodied exploration, we find that its latent space develops spatial semantic structure that mirrors physical geometry -- direction accuracy 0.677+-0.029 versus 0.547 for a randomly initialized encoder, and position RSA 0.192+-0.047 versus 0.029 for random encoders (6.6x improvement), showing that training induces genuine structural organization beyond CNN inductive bias. Across 20 temporal checkpoints, prediction performance and semantic alignment co-improve (Spearman r=-0.61, p=0.004), consistent with the shared-driver account. We confirm this through a double knockout: standard KL regularization (beta=0.1) forces the encoder away from geometric structure, and both prediction performance and semantic alignment collapse simultaneously to near-chance by step 50,000 -- exactly as the shared-driver account predicts. Reducing beta to 0.001 restores geometric access and recovers both capabilities together. These findings establish physical world geometry as the organizing principle of world model representations, with direct implications for the design of semantically grounded embodied agents.

---

## 9. Thoughts-as-Planning: Latent World Models for Chain-of-Thoughts Optimization via Reinforcement Planning

**Authors:** Dong Liu, Yanxuan Yu, Ying Nian Wu
**arXiv:** [2605.28842](https://arxiv.org/abs/2605.28842)
**Categories:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI)

The success of large language models (LLMs) across diverse NLP tasks has elevated the importance of reasoning chain optimization as a critical step in aligning model behavior with task objectives. Existing reasoning chain tuning methods often rely on black-box heuristics or gradient-free search, which lack interpretability, generalization, and sample efficiency. In this work, we introduce \textbf{Thoughts-as-Planning}, a novel framework that formalizes reasoning chain optimization as a sequential decision-making process over a latent semantic space. We model the LLM as a partially observable environment and learn a latent world model that simulates the effect of reasoning chain edits on downstream outputs. A proximity-preserving embedding space is constructed to encode reasoning chain-response dynamics, enabling planning via gradient descent or reinforcement learning. Our method supports multi-scale abstraction, allowing reasoning chain edits at token, segment, and instruction levels to be integrated into a unified planner. Through extensive experiments on language understanding and generation tasks, we demonstrate that Thoughts-as-Planning outperforms state-of-the-art reasoning chain tuning baselines in efficiency, robustness, and generalization, while offering interpretability through its structured planning trajectory. Our code is available at this https URL.

---

## 10. Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences

**Authors:** Benjamin Walker, Terry Lyons
**arXiv:** [2605.30100](https://arxiv.org/abs/2605.30100)
**Categories:** Machine Learning (cs.LG)

World models require state tracking, which is the ability to maintain a correct latent state across action sequences. Existing benchmarks are often synthetic or language-based, limiting their value as tests of structured state updates in realistic domains. We introduce Chess-World-Model, a large-scale state-tracking benchmark built from 10 million real chess games, where models predict the exact board state reached after a sequence of legal moves. Alongside a held-out real-game split, we include an out-of-distribution split from uniformly random legal play, which tests whether models learn the transition rules rather than shortcuts from common human positions. Prior theoretical and empirical work has shown that Transformers struggle to state-track, while input-dependent linear RNNs require expressive state-transition matrices to do so. We therefore benchmark a causal Transformer, block-diagonal SLiCE, Mamba-3, and Gated DeltaNet with negative eigenvalues under a matched interface and training protocol. The recurrent models strongly outperform the Transformer at 3 and 8 million parameters. Real-game performance saturates above 18 million parameters, but the random-uniform split remains discriminative up to 40 million, exposing failures otherwise hidden by scale. Additionally, ablations show that less expressive state-transition mechanisms reduce performance on the out-of-distribution split for all three recurrent models. Together, these results establish Chess-World-Model as a practical large-scale benchmark for state tracking that exposes failures model scale would otherwise conceal.

---

## 11. ReasonBreak: Probing Vulnerabilities in Reasoning-Enabled Vision-Language-Action Models for Autonomous Driving

**Authors:** Mohammadreza Teymoorianfard, Jean-Philippe Monteuuis, Jonathan Petit, Amir Houmansadr
**arXiv:** [2605.29114](https://arxiv.org/abs/2605.29114)
**Categories:** Cryptography and Security (cs.CR); Machine Learning (cs.LG); Robotics (cs.RO)

Vision-Language-Action (VLA) models with integrated reasoning have been proposed for end-to-end autonomous driving, assuming a tight coupling between reasoning and trajectory generation. However, the robustness of such systems under realistic input perturbations remains largely unexplored. We show that these models are highly vulnerable to realistic input perturbations, achieving up to 89% attack success rate (ASR) on reasoning and up to 72% on trajectory manipulation in closed-loop simulation, leading to increased collision rates and degraded safety metrics. Using NVIDIA's recent Alpamayo models as representative industry-developed VLAs, we conduct the first systematic black-box study of reasoning-enabled VLA models under realistic textual input corruptions, evaluating their impact on reasoning and driving behavior. We introduce a reasoning-aware evaluation framework capturing both semantic and structural aspects of reasoning, along with safety-centric measures. We also introduce a benchmark for evaluating attacks and defenses on reasoning-trajectory interactions in autonomous driving. Our results highlight the need for rigorous evaluation and improved defenses to ensure the safety of reasoning-enabled VLA systems in autonomous driving.

---

## 12. Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation

**Authors:** Kuangji Zuo, Gen Li, Bofan Lyu, ..., Geng Li, Jianfei Yang
**arXiv:** [2605.30282](https://arxiv.org/abs/2605.30282)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions. However, in practice, language alone is often insufficient to precisely convey human intent. It is difficult to describe which exact object to interact with among similar candidates, where to act on the object, or how the target may change during execution. To address this limitation, we propose Gaze2Act, a novel VLA framework that leverages human gaze as a dynamic and intuitive intent signal for complex interactive manipulation. Gaze2Act first bridges the ego-exo view gap by mapping first-person gaze into the robot's perspective through cross-view semantic matching, producing both an object mask and a gaze point for coarse-to-fine target specification. These cues are then integrated into the policy through perception-level prompting and action-level conditioning, allowing the robot to attend to relevant regions and execute precise interactions under dynamic intent. In a systematic evaluation across seven task categories and 16 real-robot tasks on a Unitree G1 humanoid, Gaze2Act achieves state-of-the-art performance in both intent accuracy and task success rate. It notably outperforms baselines in object disambiguation, fine-grained interaction, and dynamic intent steering. These results demonstrate that human gaze provides a natural, low-burden, and highly expressive modality for human-in-the-loop VLA control.

---

## 13. PhAIL: A Real-Robot VLA Benchmark and Distributional Methodology

**Authors:** Sergey Arkhangelskiy
**arXiv:** [2605.29710](https://arxiv.org/abs/2605.29710)
**Categories:** Robotics (cs.RO)

Real-world evaluation of vision-language-action (VLA) policies still rests on binary success rate at a fixed timeout with $N \le 25$ rollouts per condition, almost always without confidence intervals or paired statistical comparison; these cohort sizes struggle to resolve close comparisons reliably. We introduce PhAIL (Physical AI Leaderboard, this https URL), an open real-robot benchmark on a Franka FR3 (dataset, per-rollout artifacts, and end-to-end reference implementation) of a distributional evaluation methodology: the time-to-success cumulative distribution function (CDF) as the evaluation primitive, with two separated jobs. The first is scoring via Human-Relative Throughput (HRT), a dimensionless scalar with bootstrap confidence intervals, anchored to same-fixture human teleoperation. The second is a significance test (Kolmogorov-Smirnov, computed per-object and macro-averaged across objects). On four publicly-available VLAs, the macro-averaged KS test resolves two close comparisons (GR00T vs. ACT, OpenPI vs. ACT) at $N \le 30$ rollouts per (model, object) cell where binary-threshold metrics do not; the closest pair (OpenPI vs. GR00T) remains unresolved within our budget. The best evaluated VLA is $\sim 7\times$ slower per operation (RMST ratio) than the human reference.

---

## 14. VLAConf: Calibrated Task-Success Confidence for Vision-Language-Action Models

**Authors:** Dehao Huang, Aoxiang Gu, Chengjie Zhang, ..., Yue Wang, Hong Zhang
**arXiv:** [2605.29605](https://arxiv.org/abs/2605.29605)
**Categories:** Robotics (cs.RO)

Confidence estimation for Vision-Language-Action (VLA) models is essential for robots to perform manipulation tasks in the open world, providing crucial signals for risk-sensitive decision-making and failure anticipation. Existing confidence estimation methods typically rely on ensemble-based paradigms or action-token probabilities to predict the likelihood of task success. However, they still encounter challenges in computational efficiency and cross-architecture generalizability. These methods usually require repeated sampling, leading to inference inefficiency, and are restricted to VLA models with discrete action outputs, making them difficult to apply to continuous action spaces. To address this issue, we propose VLAConf, a one-class discriminative confidence framework. By leveraging frozen pretrained VLA internal representations, VLAConf directly estimates step-wise anomaly scores in a single forward pass using a lightweight confidence head, thereby eliminating the overhead of exhaustive resampling. We additionally use step-conditioned modeling to encode rollout-phase information along the manipulation trajectory. Experiments on the LIBERO benchmark demonstrate that VLAConf significantly improves the quality of the confidence signal constructed for post-hoc calibration, outperforming existing baselines by a large margin in inference efficiency. The effectiveness of VLAConf is further validated in real-robot experiments. To access the source code and supplementary videos, visit this https URL.

---

## 15. ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models

**Authors:** Ye Li, Huanan Liu, Kangye Ji, ..., Shu-Tao Xia, Zhi Wang
**arXiv:** [2605.29438](https://arxiv.org/abs/2605.29438)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models are a powerful paradigm for generalist robotic control. However, their high computational cost and limited control frequency hinder real-time robotic manipulation, especially when large vision-language backbones and iterative action heads run at every control step. Existing VLA acceleration methods often optimize individual components or rely on fixed acceleration rules, treating different control steps with largely fixed computation and overlooking the non-uniform reasoning demands of sequential embodied control. Inspired by human motor control, where cognitive and feedback resources concentrate on goal-sensitive stages, we argue that VLA models should learn when to invest full computation and when to reuse prior computation. We propose ElegantVLA, a plug-in phase-adaptive inference framework that accelerates VLA models through intra-model dynamic compute scheduling. ElegantVLA introduces a lightweight scheduler that observes temporal representation similarity, robot-motion cues, and episode progress to jointly allocate computation across the vision encoder, LLM, and action head. For perception-language reasoning, the scheduler selects a five-level Vision-LLM compute mode, from full recomputation to multi-step temporal reuse, based on visual-language representation stability. For action generation, it selects a three-level denoising mode, reusing intermediate denoising states during stable motion while preserving full refinement for goal-sensitive stages. By coordinating these decisions, ElegantVLA offers a general acceleration framework for modern VLA pipelines with explicit action-generation modules, without modifying or retraining the base model. Experiments on GR00T and CogACT achieve up to 2.55x and 3.77x speedup, and on six real-world GR00T tasks ElegantVLA cuts computation by 2.18x while raising control frequency from 13.8 Hz to 26.3 Hz.

---

## 16. 3DVLA: Enhancing Vision-Language-Action Models via 3D Spatial and Instance Understanding

**Authors:** Zhongyu Xia, Yousen Tang, Bingqing Wei, Yongtao Wang
**arXiv:** [2605.29416](https://arxiv.org/abs/2605.29416)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action models have achieved remarkable progress in robotic manipulation, yet they suffer from a critical limitation: a lack of 3D scene understanding. This deficiency manifests as three intertwined challenges: weak extraction of 3D spatial positions without enforcing multi-view consistency, inadequate 3D instance understanding, and fragile reasoning under occlusion. Although mature 3D perception methods exist, their direct integration into VLA pipelines is hindered by architectural incompatibility and by heavy reliance on costly instance-level annotations. To address the above challenges, we propose 3DVLA, a plug-and-play framework that injects robust 3D reasoning into pretrained VLAs without requiring extra manual labels or discarding VLM priors. Specifically, 3DVLA tackles the three challenges through: (1) pervasive 3D feature encoding with explicit multi-view consistency constraints across all modalities and a Spatially-Conditioned Geometry Aggregation method, (2) an instance estimation module with high-level instance tokens for 3D instance awareness, and (3) a masked self-supervised 3D encoding branch that retains its predictor for visual token completion to handle occlusions. We integrate 3DVLA with multiple VLA baselines and evaluate on LIBERO-Plus and RoboTwin 2.0. Results show consistent and significant gains in manipulation performance, validating both the effectiveness and plug-and-play compatibility of our approach.

---

## 17. YoCausal: How Far is Video Generation from World Model? A Causality Perspective

**Authors:** You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, ..., Yu-Lun Liu, Zhixiang Wang
**arXiv:** [2605.30346](https://arxiv.org/abs/2605.30346)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.

---

## 18. minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models

**Authors:** Min Zhao, Hongzhou Zhu, Bokai Yan, ..., Fan Bao, Jun Zhu
**arXiv:** [2605.30263](https://arxiv.org/abs/2605.30263)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Recent video diffusion foundation models have achieved remarkable progress in high-quality video generation, yet turning them into real-time interactive video world models remains challenging. Interactive world models require controllable, causal, and low-latency rollout, which in practice demands a full pipeline spanning data construction, controllable fine-tuning, autoregressive training, few-step distillation, and streaming inference. In this work, we present minWM, a full-stack open-source framework for building real-time interactive video world models. minWM provides an end-to-end pipeline that converts existing bidirectional T2V/TI2V video foundation models into camera-controllable few-step autoregressive world models. Specifically, minWM first fine-tunes a bidirectional video diffusion model with camera control, and then applies the Causal Forcing / Causal Forcing++ pipeline, including AR diffusion training, causal ODE or causal consistency distillation, and asymmetric DMD, to distill it into a few-step autoregressive generator for low-latency rollout. The framework is modular and architecture-extensible: we instantiate it on representative open backbones, including Wan2.1-T2V-1.3B and HY1.5-TI2V-8B, covering both cross-attention-based condition injection and MMDiT-style architectures. minWM also supports adapting existing video world models, such as HY-WorldPlay, to new data distributions, training recipes, and latency targets. Beyond releasing runnable scripts, checkpoints, documentation, and inference code, we provide practical ablations on camera trajectory quality, controllability training steps, and minimal batch-size requirements. We hope minWM serves as a reproducible and extensible recipe for building and adapting real-time interactive video world models.
Project Page: [this https URL](this https URL)

---

## 19. SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation

**Authors:** Shilin Ma, Chubin Zhang, Changyuan Wang, ..., Zheng Zhu, Yansong Tang
**arXiv:** [2605.29662](https://arxiv.org/abs/2605.29662)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Real-time inference of vision-language-action (VLA) models is essential for robotic control. While visual token pruning has shown strong potential for accelerating inference, most existing methods mainly base pruning decisions on shallow-layer cues and risk discarding visual information required by deep layers. To address this issue, we propose SAFE-Pruner, a plug-and-play pruning framework that incorporates attention cues of future layers into pruning decisions. Specifically, we identify semantic attention consistency, the tendency that VLA models concentrate their attention probability mass on the same semantic entity across execution steps. Based on this observation, we design a forward-looking strategy to forecast the token saliency in deep layers, which prevents the premature removal of critical tokens and leads to more stable acceleration. We further introduce an adaptive subtask division strategy to detect abrupt attention shifts, thereby improving forecasting accuracy and pruning reliability. Extensive experiments in simulation and real-world settings demonstrate that our method achieves up to 1.89x speedup with a minimal degradation in success rate of less than 1.7%, while outperforming state-of-the-art methods by up to 1.9%.

---

## 20. Mitigating State Aliasing in Vision-Language-Action Models via Inverse Dynamics Learning

**Authors:** Kyujin Lee, Injae Kim, Jihwan Park, ..., Minseok Joo, Hyunwoo J. Kim
**arXiv:** [2605.29577](https://arxiv.org/abs/2605.29577)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have emerged as a promising framework that unifies perception, reasoning, and control for robot manipulation by adapting pretrained vision-language models (VLMs) to action prediction. However, VLM-derived representations are often insensitive to subtle visual distinctions required for low-level control, causing state aliasing between visually similar states that require substantially different actions. Prior VLA studies improve visual understanding by generating visual or reasoning outputs, such as future frames, 2D grounding points or traces, or intermediate spatial reasoning steps, but these objectives typically shape the vision encoder only indirectly through end-to-end prediction and do not explicitly analyze state aliasing in the learned visual feature space. To mitigate state aliasing, we introduce inverse dynamics learning as an auxiliary objective that directly supervises the VLA vision encoder. By predicting the action between current and future observations, our objective encourages the encoder to capture fine-grained visual distinctions that determine low-level actions. We further use pseudo-reversed supervision to expose the encoder to a broader range of action directions and improve generalization under limited robot demonstrations. Our method applies to diverse VLA baselines, uses only standard observation-action pairs without additional annotations, and preserves the original inference pipeline at test time. Experiments on CALVIN ABC-D and SimplerEnv show consistent gains across diverse VLA baselines. Frozen-encoder probing and state-feature alignment analyses further show that our method learns state-discriminative visual representations that reduce state aliasing and better align with robot state changes.

---
