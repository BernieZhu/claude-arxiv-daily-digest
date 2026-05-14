# arXiv Daily Digest — 2026-05-13

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 20

---

## 1. Reinforcing VLAs in Task-Agnostic World Models

**Authors:** Yucen Wang, Rui Yu, Fengming Zhang, ..., Kaixin Wang, Li Zhao
**arXiv:** [2605.12334](https://arxiv.org/abs/2605.12334)
**Categories:** Artificial Intelligence (cs.AI)

Post-training Vision-Language-Action (VLA) models via reinforcement learning (RL) in learned world models has emerged as an effective strategy to adapt to new tasks without costly real-world interactions. However, while using imagined trajectories reduces the sample complexity of policy training, existing methods still heavily rely on task-specific data to fine-tune both the world and reward models, fundamentally limiting their scalability to unseen tasks. To overcome this, we argue that world and reward models should capture transferable physical priors that enable zero-shot inference. We propose RAW-Dream (Reinforcing VLAs in task-Agnostic World Dreams), a new paradigm that completely disentangles world model learning from downstream task dependencies. RAW-Dream utilizes a world model pre-trained on diverse task-free behaviors for predicting future rollouts, and an off-the-shelf Vision-Language Model (VLM) for reward generation. Because both components are task-agnostic, VLAs can be readily finetuned for any new task entirely within this zero-shot imagination. Furthermore, to mitigate world model hallucinations, we introduce a dual-noise verification mechanism to filter out unreliable rollouts. Extensive experiments across simulation and real-world settings demonstrate consistent performance gains, proving that generalized physical priors can effectively substitute for costly task-dependent data, offering a highly scalable roadmap for VLA adaptation.

---

## 2. Why Conclusions Diverge from the Same Observations: Formalizing World-Model Non-Identifiability via an Inference

**Authors:** Toru Takahashi
**arXiv:** [2605.12255](https://arxiv.org/abs/2605.12255)
**Categories:** Artificial Intelligence (cs.AI); Computers and Society (cs.CY); Machine Learning (cs.LG)

When people share the same documents and observations yet reach different conclusions, the disagreement often shifts into a judgment that the other party is cognitively defective, irrational, or acting in bad faith. This paper argues that such divergence is better described as a form of non-identifiability inherent in inference and learning, rather than as a defect of the other party. We organize the phenomenon into two levels: (i) $\theta$-level non-identifiability, where conclusions diverge under the same world model $W$ because inference settings differ; and (ii) $W$-level non-identifiability, where repeated use of an inference setting $\theta$ biases data exposure and update rules, causing the learned world model $W$ itself to diverge. We introduce an inference profile $\theta = (R, E, S, D)$, consisting of Reference, Exploration, Stabilization, and Horizon, and show how outputs can split even for the same observation $o$ and the same $W$. We further explain why disagreements tend to project onto a small number of bases -- abstract versus concrete, externalizability, and order versus freedom -- as a consequence of general constraints on learning systems: computational, observational, and coordination constraints. Finally, we relate the framework to deep representation learning, including representation hierarchy, latent-state estimation, and regularization-exploration trade-offs, and illustrate the framework through a case study on AI regulation debates.

---

## 3. Do Enterprise Systems Need Learned World Models? The Importance of Context to Infer Dynamics

**Authors:** Jishnu Sethumadhavan Nair, Patrice Bechard, Rishabh Maheshwary, ..., Srinivas Sunkara, Sai Rajeswar
**arXiv:** [2605.12178](https://arxiv.org/abs/2605.12178)
**Categories:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)

World models enable agents to anticipate the effects of their actions by internalizing environment dynamics. In enterprise systems, however, these dynamics are often defined by tenant-specific business logic that varies across deployments and evolves over time, making models trained on historical transitions brittle under deployment shift. We ask a question the world-models literature has not addressed: when the rules can be read at inference time, does an agent still need to learn them? We argue, and demonstrate empirically, that in settings where transition dynamics are configurable and readable, runtime discovery complements offline training by grounding predictions in the active system instance. We propose enterprise discovery agents, which recover relevant transition dynamics at runtime by reading the system's configuration rather than relying solely on internalized representations. We introduce CascadeBench, a reasoning-focused benchmark for enterprise cascade prediction that adopts the evaluation methodology of World of Workflows on diverse synthetic environments, and use it together with deployment-shift evaluation to show that offline-trained world models can perform well in-distribution but degrade as dynamics change, whereas discovery-based agents are more robust under shift by grounding their predictions in the current instance. Our findings suggest that, in configurable enterprise environments, agents should not rely solely on fixed internalized dynamics, but should incorporate mechanisms for discovering relevant transition logic at runtime.

---

## 4. Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models

**Authors:** Huoren Yang, Jianchao Zhao, Hu Yusong, ..., Zhiheng Ma, Yihong Gong
**arXiv:** [2605.11809](https://arxiv.org/abs/2605.11809)
**Categories:** Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have advanced rapidly with stronger backbones, broader pre-training, and larger demonstration datasets, yet their action heads remain largely homogeneous: most directly predict action commands in a fixed world coordinate frame. We propose \textbf{MCF-Proto}, a lightweight action head that equips VLA policies with a Motion-Centric Action Frame (MCF) and a prototype-based action parameterization. At each step, the policy predicts a rotation $R_t \in SO(3)$, composes actions in the transformed local frame from a set of prototypes, and maps them back to the world frame for end-to-end training, using only standard demonstrations without auxiliary supervision. This simple design induces stable emergent structure. Without explicit directional labels, the learned local frames develop a stable geometric structure whose axes are strongly compatible with demonstrated end-effector motion. Meanwhile, actions in the learned representation become substantially more compact, with variation captured by fewer dominant directions and more regularly organized by shared prototypes. These structural properties translate into improved robustness, especially under geometric perturbations. Our results suggest that adding lightweight geometric and compositional structure to the action head can materially improve how VLA policies organize and generalize robotic manipulation behavior. An anonymized code repository is provided in the supplementary material.

---

## 5. OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models

**Authors:** Seungwoo Roh, Huiyeong Kim, Jong-Chan Kim
**arXiv:** [2605.11678](https://arxiv.org/abs/2605.11678)
**Categories:** Artificial Intelligence (cs.AI)

End-to-end Vision-Language-Action (VLA) models for autonomous driving unify perception, reasoning, and control in a single neural network, achieving strong driving performance but requiring 20-60GB of GPU memory-far exceeding the 12-16GB available on commodity GPUs. We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification. Our work proceeds in three stages: (1) Sequential Demand Layering reduces VRAM usage from model-level to layer-level granularity; (2) Pipelined Demand Layering hides parameter transfer time within layer execution time via transfer--compute overlap; and (3) a GPU-Resident Layer Decision Policy, informed by per-module residency benefit analysis, eliminates the residual transfer overhead that pipelining cannot hide. We further propose a performance prediction model that determines the optimal configuration-both the number and placement of resident layers-from a single profiling run with less than 1.3% prediction error across all configurations. Applied to NVIDIA's Alpamayo-R1-10B (21.52GB) on an RTX 5070Ti (16GB), our work achieves up to 3.55x speedup over Accelerate offloading while maintaining full BF16 precision.

---

## 6. PriorZero: Bridging Language Priors and World Models for Decision Making

**Authors:** Junyu Xiong, Yuan Pu, Jia Tang, Yazhe Niu
**arXiv:** [2605.12289](https://arxiv.org/abs/2605.12289)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Leveraging the rich world knowledge of Large Language Models (LLMs) to enhance Reinforcement Learning (RL) agents offers a promising path toward general intelligence. However, a fundamental prior-dynamics mismatch hinders existing approaches: static LLM knowledge cannot directly adapt to the complex transition dynamics of long-horizon tasks. Using LLM priors as fixed policies limits exploration diversity, as the prior is blind to environment-specific dynamics; while end-to-end fine-tuning suffers from optimization instability and credit assignment issues. To bridge this gap, we propose PriorZero, a unified framework that integrates LLM-derived conceptual priors into world-model-based planning through a decoupled rollout-training design. During rollout, a novel root-prior injection mechanism incorporates LLM priors exclusively at the root node of Monte Carlo Tree Search (MCTS), focusing search on semantically promising actions while preserving the world model's deep lookahead capability. During training, PriorZero decouples world-model learning from LLM adaptation: the world model is continuously refined on interaction data to jointly improve its dynamics, policy, and value predictions, its value estimates are then leveraged to provide fine-grained credit assignment signals for stable LLM fine-tuning via alternating optimization. Experiments across diverse benchmarks, including text-based adventure games in Jericho and instruction-following gridworld tasks in BabyAI, demonstrate that PriorZero consistently improves both exploration efficiency and asymptotic performance, establishing a promising framework for LLM-empowered decision-making. Our code is available at this https URL.

---

## 7. Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete

**Authors:** Joonha Park, Jiseung Jeong, Taesik Gong
**arXiv:** [2605.12160](https://arxiv.org/abs/2605.12160)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) policies are typically evaluated as if the user had finished typing or speaking before the robot begins acting. In real deployment, however, users take several seconds to enter a request, leaving the policy idle for a substantial fraction of the interaction. We introduce Premover, a lightweight module that converts this idle window into useful precomputation. Premover keeps the VLA backbone frozen and attaches two small projection heads, one for image patches, one for language tokens, that map an intermediate layer of the backbone into a shared space. The resulting focus map is supervised by simulator-rendered target-object segmentation masks and applied as a per-patch reweighting of the next step's image tokens. A single scalar readiness threshold, trained jointly from streaming prefixes, decides when the policy should begin acting. On the LIBERO benchmark suite, Premover reduces mean wall-clock time from 34.0 to 29.4 seconds, a 13.6% reduction, while matching the full-prompt baseline's success rate (95.1% vs. 95.0%); naive premoving, by contrast, collapses to 66.4%.

---

## 8. DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies

**Authors:** Xianzhe Fan, Yuxiang Lu, Shenyuan Gao, ..., Manling Li, Hengshuang Zhao
**arXiv:** [2605.11750](https://arxiv.org/abs/2605.11750)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models are often brittle in fine-grained manipulation, where minor action errors during the critical phases can rapidly escalate into irrecoverable failures. Since existing VLA models rely predominantly on successful demonstrations for training, they lack an explicit awareness of failure during these critical phases. To address this, we propose DreamAvoid, a critical-phase test-time dreaming framework that enables VLA models to anticipate and avoid failures. We also introduce an autonomous boundary learning paradigm to refine the system's understanding of the subtle boundary between success and failure. Specifically, we (1) utilize a Dream Trigger to determine whether the execution has entered a critical phase, (2) sample multiple candidate action chunks from the VLA via an Action Proposer, and (3) employ a Dream Evaluator, jointly trained on mixed data (success, failure, and boundary cases), to "dream" the short-horizon futures corresponding to the candidate actions, evaluate their values, and select the optimal action. We conduct extensive evaluations on real-world manipulation tasks and simulation benchmarks. The results demonstrate that DreamAvoid can effectively avoid failures, thereby improving the overall task success rate. Our code is available at this https URL.

---

## 9. Overcoming Dynamics-Blindness: Training-Free Pace-and-Path Correction for VLA Models

**Authors:** Yanyan Zhang, Chaoda Song, Vikash Singh, ..., Yu Yin, Vipin Chaudhary
**arXiv:** [2605.11459](https://arxiv.org/abs/2605.11459)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models achieve remarkable flexibility and generalization beyond classical control paradigms. However, most prevailing VLAs are trained under a single-frame observation paradigm, which leaves them structurally blind to temporal dynamics. Consequently, these models degrade severely in non-stationary scenarios, even when trained or finetuned on dynamic datasets. Existing approaches either require expensive retraining or suffer from latency bottlenecks and poor temporal consistency across action chunks. We propose Pace-and-Path Correction, a training-free, closed-form inference-time operator that wraps any chunked-action VLA. From a single quadratic cost, joint minimization yields a unified solution that decomposes orthogonally into two distinct channels. The pace channel compresses execution along the planned direction, while the path channel applies an orthogonal spatial offset, jointly absorbing the perceived dynamics within the chunk window. We evaluate our approach on a comprehensive diagnostic benchmark MoveBench designed to isolate motion as the sole controlled variable. Empirical results demonstrate that our framework consistently outperforms state-of-the-art training-free wrappers and dynamic-adaptive methods and improves success rates by up to 28.8% and 25.9% in absolute terms over foundational VLA models in dynamic-only and static-dynamic mixed environments, respectively.

---

## 10. SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection

**Authors:** Tianchonghui Fang, Yuan Zhuang, Fei Miao
**arXiv:** [2605.11114](https://arxiv.org/abs/2605.11114)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) and imitation-learning policies trained via community toolchains on low-cost hardware frequently fail when deployed outside the training environment. Existing evaluations, including the original ACT and SmolVLA benchmarks, demonstrate high success rates under controlled, fixed backgrounds, yet community practitioners report near-zero transfer to new environments. We present SEVO (Semantic-Enhanced Virtual Observation), a data-centric approach that improves cross-environment manipulation robustness without modifying the policy architecture. SEVO transforms the raw RGB camera stream through three mechanisms: (1) body-fixed cameras whose combined fields of view cover the full manipulation workspace, (2) active red-spectrum illumination that physically normalizes object appearance, and (3) real-time YOLO segmentation overlay that provides a background-invariant semantic cue. Critically, we show that a diversified data collection protocol (systematically varying lighting, backgrounds, and distractors during teleoperation) is the single most important factor for generalization. We target transparent water bottles, objects that visually blend with their surroundings, and select a simple pick-and-place task to enable hundreds of controlled real-robot trials across two mobile platforms. The full pipeline achieves 95% grasp success with ACT and 83% with SmolVLA in the training environment, transferring to novel environments at 85% and 75%. Without SEVO, the same policies achieve only 75%/70% in training and collapse to 30-35% in novel environments. Our results demonstrate that principled observation design and environmental diversity during data collection, not model scaling, enable low-cost robots to operate reliably in everyday household environments.

---

## 11. GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization

**Authors:** Xiaosong Jia, Bowen Yang, Zuhao Ge, ..., Junchi Yan, Yu-Gang Jiang
**arXiv:** [2605.12369](https://arxiv.org/abs/2605.12369)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models aim for general robot learning by aligning action as a modality within powerful Vision-Language Models (VLMs). Existing VLAs rely on end-to-end supervision to implicitly enable the action decoding process to learn task-relevant features. However, without explicit guidance, these models often overfit to spurious correlations, such as visual shortcuts or environmental noise, limiting their generalization. In this paper, we introduce GuidedVLA, a framework designed to manually guide the action generation to focus on task-relevant factors. Our core insight is to treat the action decoder not as a monolithic learner, but as an assembly of functional components. Individual attention heads are supervised by manually defined auxiliary signals to capture distinct factors. As an initial study, we instantiate this paradigm with three specialized heads: object grounding, spatial geometry, and temporal skill logic. Across simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines. Finally, we show that the quality of these specialized factors correlates positively with task performance and that our mechanism yields decoupled, high-quality features. Our results suggest that explicitly guiding action-decoder learning is a promising direction for building more robust and general VLA models.

---

## 12. World Action Models: The Next Frontier in Embodied AI

**Authors:** Siyin Wang, Junhao Shi, Zhaoyang Fu, ..., Xipeng Qiu, Yu-Gang Jiang
**arXiv:** [2605.12090](https://arxiv.org/abs/2605.12090)
**Categories:** Robotics (cs.RO); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have achieved strong semantic generalization for embodied policy learning, yet they learn reactive observation-to-action mappings without explicitly modeling how the physical world evolves under intervention. A growing body of work addresses this limitation by integrating world models, predictive models of environment dynamics, into the action generation pipeline. We term this emerging paradigm World Action Models (WAMs): embodied foundation models that unify predictive state modeling with action generation, targeting a joint distribution over future states and actions rather than actions alone. However, the literature remains fragmented across architectures, learning objectives, and application scenarios, lacking a unified conceptual framework. We formally define WAMs and disambiguate them from related concepts, and trace the foundations and early integration of VLA and world model research that gave rise to this paradigm. We organize existing methods into a structured taxonomy of Cascaded and Joint WAMs, with further subdivision by generation modality, conditioning mechanism, and action decoding strategy. We systematically analyze the data ecosystem fueling WAMs development, spanning robot teleoperation, portable human demonstrations, simulation, and internet-scale egocentric video, and synthesize emerging evaluation protocols organized around visual fidelity, physical commonsense, and action plausibility. Overall, this survey provides the first systematic account of the WAMs landscape, clarifies key architectural paradigms and their trade-offs, and identifies open challenges and future opportunities for this rapidly evolving field.

---

## 13. See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, ..., Yunke Wang, Chang Xu
**arXiv:** [2605.11817](https://arxiv.org/abs/2605.11817)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment. Existing token pruning methods suffer from a fundamental trade-off: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation. This forces a compromise, limiting the achievable compression rate and thus the potential speedup. We argue that breaking this trade-off requires rethinking compression as a geometry-aware, continuous token resampling in the vision encoder. To this end, we propose the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression (with fewer than 10% original visual tokens). Experiments on both LIBERO benchmark and a real robotic platform demonstrate that validating the lowest feasible visual token count reported to date, GridS achieves a 76% reduction in FLOPs with no degradation in the success rate. The code is available at this https URL.

---

## 14. ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models

**Authors:** Yanbin Hu, Jin Cui, Jiayi Lu, ..., Xuguang Lan, Pengju Ren
**arXiv:** [2605.10993](https://arxiv.org/abs/2605.10993)
**Categories:** Robotics (cs.RO)

Memory capacity is a critical factor determining the performance of Vision-Language-Action (VLA) models in long-horizon manipulation tasks. Existing memory-augmented architectures primarily rely on linear or flat storage, lacking structural priors for manipulation categories and hierarchical organization. This deficiency hinders efficient experience retrieval and limits generalization to unseen long-horizon task compositions. Inspired by the hierarchical organization of human experience, we propose ECHO (Experience Consolidation and Hierarchical Organization), a novel memory framework operating within a Continuous Hierarchical Space. By employing a hyperbolic autoencoder, ECHO maps VLA hidden states into this space. Leveraging hyperbolic metrics and entailment constraint mechanisms, experience vectors are organized into a semantic memory tree that supports efficient top-down retrieval. In parallel, a background consolidation mechanism continuously refines the memory tree through geometric interpolation and structural splitting, supporting virtual memory synthesis in the continuous space. We integrate ECHO into the $\pi_0$ foundation model. Evaluations on LIBERO and preliminary real-world experiments demonstrate the effectiveness of our approach, notably achieving a 12.8% absolute improvement in execution success rate over the $\pi_0$ baseline on LIBERO-Long, while improving compositional generalization on cross-suite unseen long-horizon tasks.

---

## 15. HorizonDrive: Self-Corrective Autoregressive World Model for Long-horizon Driving Simulation

**Authors:** Conglang Zhang, Yifan Zhan, Qingjie Wang, ..., Wei Yin, Zhengqing Chen
**arXiv:** [2605.11596](https://arxiv.org/abs/2605.11596)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Closed-loop driving simulation requires real-time interaction beyond short offline clips, pushing current driving world models toward autoregressive (AR) rollout. Existing AR distillation approaches typically rely on frame sinks or student-side degradation training. The former transfers poorly to driving due to fast ego-motion and rapid scene changes, while the latter remains bounded by the teacher's single-pass output length and thus provides only a limited supervision horizon. A natural question is: can the teacher itself be extended via AR rollout to provide unbounded-horizon supervision at bounded memory cost? The key difficulty is that a standard teacher drifts under its own predictions, contaminating the supervision it provides. Our key insight is to make the teacher rollout-capable, ensuring reliable supervision from its own AR rollouts. This is instantiated as HorizonDrive, an anti-drifting training-and-distillation framework for AR driving simulation. First, scheduled rollout recovery (SRR) trains the base model to reconstruct ground-truth future clips from prediction-corrupted histories, yielding a teacher that remains stable across long AR rollouts. Second, the rollout-capable teacher is extended via AR rollout, providing long-horizon distribution-matching supervision under bounded memory, while a short-window student aligns to it with teacher rollout DMD (TRD) for efficient real-time deployment. HorizonDrive natively supports minute-scale AR rollout under bounded memory; on nuScenes, HorizonDrive reduces FID by 52% and FVD by 37%, and lowers ARE and DTW by 21% and 9% relative to the strongest long-horizon streaming baselines, while remaining competitive with single-pass driving video generators.

---

## 16. Dynamic Execution Commitment of Vision-Language-Action Models

**Authors:** Feng Chen, Xianghui Wang, Yuxuan Chen, ..., Zeyu Zhang, Yicheng Wu
**arXiv:** [2605.11567](https://arxiv.org/abs/2605.11567)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models predominantly adopt action chunking, i.e., predicting and committing to a short horizon of consecutive low-level actions in a single forward pass, to amortize the inference cost of large-scale backbones and reduce per-step latency. However, committing these multi-step predictions to real-world execution requires balancing success rate against inference efficiency, a decision typically governed by fixed execution horizons tuned per task. Such heuristics ignore the state-dependent nature of predictive reliability, leading to brittle performance in dynamic or out-of-distribution settings. In this paper, we introduce A3, an Adaptive Action Acceptance mechanism that reframes dynamic execution commitment as a self-speculative prefix verification problem. A3 first computes a trajectory-wise consensus score of actions via group sampling, then selects a representative draft and prioritizes downstream verification. Specifically, it enforces: (1) consensus-ordered conditional invariance, which validates low-consensus actions by judging whether they remain consistent when re-decoded conditioned on high-consensus actions; and (2) prefix-closed sequential consistency, which guarantees physical rollout integrity by accepting only the longest continuous sequence of verified actions starting from the beginning. Consequently, the execution horizon emerges as the longest verifiable prefix satisfying both internal model logic and sequential execution constraints. Experiments across diverse VLA models and benchmarks demonstrate that A3 eliminates the need for manual horizon tuning while achieving a superior trade-off between execution robustness and inference throughput.

---

## 17. 3D-Belief: Embodied Belief Inference via Generative 3D World Modeling

**Authors:** Yifan Yin, Zehao Wen, Jieneng Chen, ..., Ayush Tewari, Tianmin Shu
**arXiv:** [2605.11367](https://arxiv.org/abs/2605.11367)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Recent advances in visual generative models have highlighted the promise of learning generative world models. However, most existing approaches frame world modeling as novel-view synthesis or future-frame prediction, emphasizing visual realism rather than the structured uncertainty required by embodied agents acting under partial observability. In this work, we propose a different perspective: world modeling as embodied belief inference in 3D space. From this view, a world model should not merely render what may be seen, but maintain and update an agent's belief about the unobserved 3D world as new observations are acquired. We identify several key capabilities for such models, including spatially consistent scene memory, multi-hypothesis belief sampling, sequential belief updating, and semantically informed prediction of unseen regions. We instantiate these ideas in 3D-Belief, a generative 3D world model that infers explicit, actionable 3D beliefs from partial observations and updates them online over time. Unlike prior visual prediction models, 3D-Belief represents uncertainty directly in 3D, enabling embodied agents to imagine plausible scene completions and reason over partially observed environments. We evaluate 3D-Belief on 2D visual quality for scene memory and unobserved-scene imagination, object- and scene-level 3D imagination using our proposed 3D-CORE benchmark, and challenging object navigation tasks in both simulation and the real world. Experiments show that 3D-Belief improves 2D and 3D imagination quality and downstream embodied task performance compared to state-of-the-art methods.

---

## 18. Do Vision-Language-Models show human-like logical problem-solving capability in point and click puzzle games?

**Authors:** Dominik Helfenstein, Marco Menner, Maximilian Triebel
**arXiv:** [2605.11223](https://arxiv.org/abs/2605.11223)
**Categories:** Artificial Intelligence (cs.AI)

Vision-Language(-Action) Models (VLMs) are increasingly applied to interactive environments, yet existing benchmarks often overlook the complex physical reasoning required for point-and-click puzzle games. This paper introduces Vision-Language Against The Incredible Machine (VLATIM), a benchmark designed to evaluate human-like logical problem-solving capabilities within the classic physics puzzle game The Incredible Machine 2 (TIM). Unlike existing benchmarks, VLATIM specifically targets the critical gap between high-level logical reasoning and continuous action spaces requiring precise mouse interactions. This benchmark is structured into five progressive parts, assessing capabilities that range from basic visual grounding and domain understanding to multi-step manipulation and full puzzle solving. Our results reveal a significant disparity between reasoning and execution. While large proprietary models demonstrate superior planning abilities, they struggle with precise visual grounding. Consequently, they do not yet show human-like problem-solving capabilities.

---

## 19. SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation

**Authors:** Chengyue Huang, Khang Vo Huynh, Sebastian Elbaum, Zsolt Kira, Lu Feng
**arXiv:** [2605.12386](https://arxiv.org/abs/2605.12386)
**Categories:** Robotics (cs.RO)

Robotic manipulation is typically evaluated by task success, but successful completion does not guarantee safe execution. Many safety failures are temporal: a robot may touch a clean surface after contamination or release an object before it is fully inside an enclosure. We introduce SafeManip, a property-driven benchmark to explicitly evaluate temporal safety properties in robotic manipulation, moving beyond prior evaluations that largely focus on task completion or per-state constraint violations. SafeManip defines reusable safety templates over finite executions using Linear Temporal Logic over finite traces (LTLf). It maps observed rollouts to symbolic predicate traces and evaluates them with LTLf-based monitors. Its property suite covers eight manipulation safety categories: collision and contact safety, grasp stability, release stability, cross-contamination, action onset, mechanism recovery, object containment, and enclosure access. Templates can be instantiated with task-specific objects, fixtures, regions, or skills, allowing the same safety specifications to generalize across tasks and environments. We evaluate SafeManip on six vision-language-action policies, including $\pi_0$, $\pi_{0.5}$, GR00T, and their training variants, across 50 RoboCasa365 household tasks. Results show that even strong models often behave unsafely. Task-success gains do not reliably translate into safer execution: many successful rollouts remain unsafe, while longer-horizon or more complex tasks expose more violations. SafeManip provides a reusable evaluation layer for diagnosing temporal safety failures and measuring safe success beyond task completion.

---

## 20. The DAWN of World-Action Interactive Models

**Authors:** Hongbo Lu, Liang Yao, Chenghao He, ..., Tao He, Pai Peng
**arXiv:** [2605.11550](https://arxiv.org/abs/2605.11550)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

A plausible scene evolution depends on the maneuver being considered, while a good maneuver depends on how the scene may evolve. Existing World Action Models (WAMs) largely miss this reciprocity, treating world prediction and action generation as either isolated parallel branches or rigid predict-then-plan pipelines. We formalize this perspective as World-Action Interactive Models (WAIMs), and instantiate it in autonomous driving with \textbf{DAWN} (\textbf{D}enoising \textbf{A}ctions and \textbf{W}orld i\textbf{N}teractive model), a simple yet strong latent generative baseline. DAWN operates in a compact semantic latent space and couples a \emph{World Predictor} with a \emph{World-Conditioned Action Denoiser}: the predicted world hypothesis conditions action denoising, while the denoised action hypothesis is fed back to update the world prediction, so that both are recursively refined during inference. Rather than eliminating test-time world evolution altogether or rolling out the full future in pixel space, DAWN performs a short explicit latent rollout that is sufficient to support long-horizon trajectory generation in complex interactive scenes. Experiments show that DAWN achieves strong planning performance and favorable safety-related results across multiple autonomous driving benchmarks. More broadly, our results suggest that interactive world-action generation is a principled path toward truly actionable world models.

---
