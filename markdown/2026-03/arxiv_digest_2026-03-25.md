# arXiv Daily Digest — 2026-03-25

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 15

---

## 1. Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models

**Authors:** Massimiliano Pappa, Luca Romani, Valentino Sacco, ..., Xavier Alameda-Pineda, Indro Spinelli
**arXiv:** [2603.23149](https://arxiv.org/abs/2603.23149)
**Categories:** Artificial Intelligence (cs.AI)

Deploying safety-critical agents requires anticipating the consequences of actions before they are executed. While world models offer a paradigm for this proactive foresight, current approaches relying on visual simulation incur prohibitive latencies, often exceeding several seconds per step. In this work, we challenge the assumption that visual processing is necessary for failure prevention. We show that a trained policy's latent state, combined with its planned actions, already encodes sufficient information to anticipate action outcomes, making visual simulation redundant for failure prevention. To this end, we introduce DILLO (DIstiLLed Language-ActiOn World Model), a fast steering layer that shifts the paradigm from "simulate-then-act" to "describe-then-act." DILLO is trained via cross-modal distillation, where a privileged Vision Language Model teacher annotates offline trajectories and a latent-conditioned Large Language Model student learns to predict semantic outcomes. This creates a text-only inference path, bypassing heavy visual generation entirely, achieving a 14x speedup over baselines. Experiments on MetaWorld and LIBERO demonstrate that DILLO produces high-fidelity descriptions of the next state and is able to steer the policy, improving episode success rate by up to 15 pp and 9.3 pp on average across tasks.

---

## 2. CoMaTrack: Competitive Multi-Agent Game-Theoretic Tracking with Vision-Language-Action Models

**Authors:** Youzhi Liu, Li Gao, Liu Liu, Mingyang Lv, Yang Cai
**arXiv:** [2603.22846](https://arxiv.org/abs/2603.22846)
**Categories:** Artificial Intelligence (cs.AI)

Embodied Visual Tracking (EVT), a core dynamic task in embodied intelligence, requires an agent to precisely follow a language-specified target. Yet most existing methods rely on single-agent imitation learning, suffering from costly expert data and limited generalization due to static training environments. Inspired by competition-driven capability evolution, we propose CoMaTrack, a competitive game-theoretic multi-agent reinforcement learning framework that trains agents in a dynamic adversarial setting with competitive subtasks, yielding stronger adaptive planning and interference-resilient strategies. We further introduce CoMaTrack-Bench, the first benchmark for competitive EVT, featuring game scenarios between a tracker and adaptive opponents across diverse environments and instructions, enabling standardized robustness evaluation under active adversarial interactions. Experiments show that CoMaTrack achieves state-of-the-art results on both standard benchmarks and CoMaTrack-Bench. Notably, a 3B VLM trained with our framework surpasses previous single-agent imitation learning methods based on 7B models on the challenging EVT-Bench, achieving 92.1% in STT, 74.2% in DT, and 57.5% in AT. The benchmark code will be available at this https URL

---

## 3. VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs

**Authors:** Haoran Yuan, Weigang Yi, Zhenyu Zhang, ..., Katherine Driggs-Campbell, Ismini Lourentzou
**arXiv:** [2603.23481](https://arxiv.org/abs/2603.23481)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Video-Action Models (VAMs) have emerged as a promising framework for embodied intelligence, learning implicit world dynamics from raw video streams to produce temporally consistent action predictions. Although such models demonstrate strong performance on long-horizon tasks through visual reasoning, they remain limited in contact-rich scenarios where critical interaction states are only partially observable from vision alone. In particular, fine-grained force modulation and contact transitions are not reliably encoded in visual tokens, leading to unstable or imprecise behaviors. To bridge this gap, we introduce the Video-Tactile Action Model (VTAM), a multimodal world modeling framework that incorporates tactile perception as a complementary grounding signal. VTAM augments a pretrained video transformer with tactile streams via a lightweight modality transfer finetuning, enabling efficient cross-modal representation learning without tactile-language paired data or independent tactile pretraining. To stabilize multimodal fusion, we introduce a tactile regularization loss that enforces balanced cross-modal attention, preventing visual latent dominance in the action model. VTAM demonstrates superior performance in contact-rich manipulation, maintaining a robust success rate of 90 percent on average. In challenging scenarios such as potato chip pick-and-place requiring high-fidelity force awareness, VTAM outperforms the pi 0.5 baseline by 80 percent. Our findings demonstrate that integrating tactile feedback is essential for correcting visual estimation errors in world action models, providing a scalable approach to physically grounded embodied foundation models.

---

## 4. Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models

**Authors:** Ruixing Jin, Zicheng Zhu, Ruixiang Ouyang, ..., Zhizheng Wu, Guiliang Liu
**arXiv:** [2603.22876](https://arxiv.org/abs/2603.22876)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Learning a generalist control policy for dexterous manipulation typically relies on large-scale datasets. Given the high cost of real-world data collection, a practical alternative is to generate synthetic data through simulation. However, the resulting synthetic data often exhibits a significant gap from real-world distributions. While many prior studies have proposed algorithms to bridge the Sim-to-Real discrepancy, there remains a lack of principled research that grounds these methods in real-world manipulation tasks, particularly their performance on generalist policies such as Vision-Language-Action (VLA) models. In this study, we empirically examine the primary determinants of Sim-to-Real generalization across four dimensions: multi-level domain randomization, photorealistic rendering, physics-realistic modeling, and reinforcement learning updates. To support this study, we design a comprehensive evaluation protocol to quantify the real-world performance of manipulation tasks. The protocol accounts for key variations in background, lighting, distractors, object types, and spatial features. Through experiments involving over 10k real-world trials, we derive critical insights into Sim-to-Real transfer. To inform and advance future studies, we release both the robotic platforms and the evaluation protocol for public access to facilitate independent verification, thereby establishing a realistic and standardized benchmark for dexterous manipulation policies.

---

## 5. Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning

**Authors:** Rohan Deb, Stephen J. Wright, Arindam Banerjee
**arXiv:** [2603.22430](https://arxiv.org/abs/2603.22430)
**Categories:** Machine Learning (cs.LG)

Offline Reinforcement Learning (RL) aims to learn optimal policies from fixed offline datasets, without further interactions with the environment. Such methods train an offline policy (or value function), and apply it at inference time without further refinement. We introduce an inference time adaptation framework inspired by model predictive control (MPC) that utilizes a pretrained policy along with a learned world model of state transitions and rewards. While existing world model and diffusion-planning methods use learned dynamics to generate imagined trajectories during training, or to sample candidate plans at inference time, they do not use inference-time information to optimize the policy parameters on the fly. In contrast, our design is a Differentiable World Model (DWM) pipeline that enables endto-end gradient computation through imagined rollouts for policy optimization at inference time based on MPC. We evaluate our algorithm on D4RL continuous-control benchmarks (MuJoCo locomotion tasks and AntMaze), and show that exploiting inference-time information to optimize the policy parameters yields consistent gains over strong offline RL baselines.

---

## 6. Agile-VLA: Few-Shot Industrial Pose Rectification via Implicit Affordance Anchoring

**Authors:** Teng Yan, Zhengyang Pei, Chengyu Shi, ..., Peigen Tian, Bingzhuo Zhong
**arXiv:** [2603.22899](https://arxiv.org/abs/2603.22899)
**Categories:** Robotics (cs.RO)

Deploying Vision-Language-Action (VLA) models on resource-constrained edge platforms encounters a fundamental conflict between high-latency semantic inference and the high-frequency control required for dynamic manipulation. To address the challenge, this paper presents Agile-VLA, a hierarchical framework designed for industrial pose reorientation tasks on edge devices such as the NVIDIA Jetson Orin Nano. The core innovation is an Implicit Affordance Anchoring mechanism that directly maps geometric visual cues, specifically centroid and rim keypoint anchors, into structured parametric action primitives, thereby substantially reducing reliance on high-latency semantic inference during closed-loop control. By decoupling perception (10 Hz) from control (50 Hz) via an asynchronous dual-stream architecture, the system effectively mitigates the frequency mismatch inherent in edge-based robot learning. Experimental results on a standard 6-DoF manipulator demonstrate that Agile-VLA achieves robust rectification of complex, irregular workpieces using only 5-shot demonstrations through extrinsic dexterity.

---

## 7. SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation

**Authors:** Ruisen Tu, Arth Shukla, Sohyun Yoo, ..., Hao Su, Zhuowen Tu
**arXiv:** [2603.22760](https://arxiv.org/abs/2603.22760)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models show promise for robotic control, yet performance in complex household environments remains sub-optimal. Mobile manipulation requires reasoning about global scene layout, fine-grained geometry, and high-dimensional continuous actions, making standard imitation learning insufficient. We introduce a framework for learning spatially-grounded VLA models that strengthens perception and representation through auxiliary task co-training and multi-modal input enhancement. Our method addresses the challenge of controlling a 13-dimensional action space involving coordinated base motion, arm articulation, and gripper actuation. To enrich spatial understanding, the model incorporates multi-view RGB observations, depth cues, and short temporal history, providing perspectives of both global scene structure and local manipulation context. To improve representation quality, we co-train auxiliary decoders that reconstruct interpretable intermediate signals - including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks - from shared visual-language features. These objectives provide dense supervision that encourages the backbone to develop spatially grounded, manipulation-aware latent representations. Through extensive evaluation on home rearrangement tasks, our approach achieves consistent improvements across picking, placing, opening, and closing operations, substantially outperforming direct imitation learning. Our findings suggest that spatial grounding through auxiliary and multi-modal learning provides a strong direction for scaling VLA models toward general-purpose domestic robots.

---

## 8. WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG

**Authors:** Zhen Li, Zian Meng, Shuwei Shi, ..., Chuanhao Li, Kaipeng Zhang
**arXiv:** [2603.23497](https://arxiv.org/abs/2603.23497)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Dynamical systems theory and reinforcement learning view world evolution as latent-state dynamics driven by actions, with visual observations providing partial information about the state. Recent video world models attempt to learn this action-conditioned dynamics from data. However, existing datasets rarely match the requirement: they typically lack diverse and semantically meaningful action spaces, and actions are directly tied to visual observations rather than mediated by underlying states. As a result, actions are often entangled with pixel-level changes, making it difficult for models to learn structured world dynamics and maintain consistent evolution over long horizons. In this paper, we propose WildWorld, a large-scale action-conditioned world modeling dataset with explicit state annotations, automatically collected from a photorealistic AAA action role-playing game (Monster Hunter: Wilds). WildWorld contains over 108 million frames and features more than 450 actions, including movement, attacks, and skill casting, together with synchronized per-frame annotations of character skeletons, world states, camera poses, and depth maps. We further derive WildBench to evaluate models through Action Following and State Alignment. Extensive experiments reveal persistent challenges in modeling semantically rich actions and maintaining long-horizon state consistency, highlighting the need for state-aware video generation. The project page is this https URL.

---

## 9. Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

**Authors:** Anupam Pani, Yanchao Yang
**arXiv:** [2603.23202](https://arxiv.org/abs/2603.23202)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Despite advances in Vision-Language-Action (VLA) models, robotic manipulation struggles with fine-grained tasks because current models lack mechanisms for active visual attention allocation. Human gaze naturally encodes intent, planning, and execution patterns -- offering a powerful supervisory signal for guiding robot perception. We introduce a gaze-regularized training framework that aligns VLA models' internal attention with human visual patterns without architectural modifications or inference-time overhead. Our method transforms temporally aggregated gaze heatmaps into patch-level distributions and regularizes the transformer's attention through KL divergence, creating an inductive bias toward task-relevant features while preserving deployment efficiency. When integrated into existing VLA architectures, our approach yields 4-12% improvements across manipulation benchmarks. The gaze-regularized models reach equivalent performance with fewer training steps and maintain robustness under lighting variations and sensor noise. Beyond performance metrics, the learned attention patterns produce interpretable visualizations that mirror human strategies, enhancing trust in robotic systems. Moreover, our framework requires no eye-tracking equipment and applies directly to existing datasets. These results demonstrate that human perceptual priors can significantly accelerate robot learning while improving both task performance and system interpretability.

---

## 10. VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models

**Authors:** Jintao Cheng, Haozhe Wang, Weibin Li, ..., Yunhui Liu, Wei Zhang
**arXiv:** [2603.22991](https://arxiv.org/abs/2603.22991)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have rapidly advanced embodied intelligence, enabling robots to execute complex, instruction-driven tasks. However, as model capacity and visual context length grow, the inference cost of VLA systems becomes a major bottleneck for real-world deployment on resource-constrained platforms. Existing visual token pruning methods mainly rely on semantic saliency or simple temporal cues, overlooking the continuous physical interaction, a fundamental property of VLA tasks. Consequently, current approaches often prune visually sparse yet structurally critical regions that support manipulation, leading to unstable behavior during early task phases. To overcome this, we propose a shift toward an explicit Interaction-First paradigm. Our proposed \textbf{training-free} method, VLA-IAP (Interaction-Aligned Pruning), introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment. This enables a conservative-to-aggressive transition, ensuring robustness during early uncertainty and efficiency once interaction is locked. Extensive experiments show that VLA-IAP achieves a \textbf{97.8\% success rate} with a \textbf{$1.25\times$ speedup} on the LIBERO benchmark, and up to \textbf{$1.54\times$ speedup} while maintaining performance \textbf{comparable to the unpruned backbone}. Moreover, the method demonstrates superior and consistent performance across multiple model architectures and three different simulation environments, as well as a real robot platform, validating its strong generalization capability and practical applicability. Our project website is: \href{this https URL}{this http URL}.

---

## 11. AI Mental Models: Learned Intuition and Deliberation in a Bounded Neural Architecture

**Authors:** Laurence Anthony
**arXiv:** [2603.22561](https://arxiv.org/abs/2603.22561)
**Categories:** Artificial Intelligence (cs.AI)

This paper asks whether a bounded neural architecture can exhibit a meaningful division of labor between intuition and deliberation on a classic 64-item syllogistic reasoning benchmark. More broadly, the benchmark is relevant to ongoing debates about world models and multi-stage reasoning in AI. It provides a controlled setting for testing whether a learned system can develop structured internal computation rather than only one-shot associative prediction. Experiment 1 evaluates a direct neural baseline for predicting full 9-way human response distributions under 5-fold cross-validation. Experiment 2 introduces a bounded dual-path architecture with separate intuition and deliberation pathways, motivated by computational mental-model theory (Khemlani & Johnson-Laird, 2022). Under cross-validation, bounded intuition reaches an aggregate correlation of r = 0.7272, whereas bounded deliberation reaches r = 0.8152, and the deliberation advantage is significant across folds (p = 0.0101). The largest held-out gains occur for NVC, Eca, and Oca, suggesting improved handling of rejection responses and c-a conclusions. A canonical 80:20 interpretability run and a five-seed stability sweep further indicate that the deliberation pathway develops sparse, differentiated internal structure, including an Oac-leaning state, a dominant workhorse state, and several weakly used or unused states whose exact indices vary across runs. These findings are consistent with reasoning-like internal organization under bounded conditions, while stopping short of any claim that the model reproduces full sequential processes of model construction, counterexample search, and conclusion revision.

---

## 12. PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding

**Authors:** Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang
**arXiv:** [2603.22796](https://arxiv.org/abs/2603.22796)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Embodied agents for creative tasks like photography must bridge the semantic gap between high-level language commands and geometric control. We introduce PhotoAgent, an agent that achieves this by integrating Large Multimodal Models (LMMs) reasoning with a novel control paradigm. PhotoAgent first translates subjective aesthetic goals into solvable geometric constraints via LMM-driven, chain-of-thought (CoT) reasoning, allowing an analytical solver to compute a high-quality initial viewpoint. This initial pose is then iteratively refined through visual reflection within a photorealistic internal world model built with 3D Gaussian Splatting (3DGS). This ``mental simulation'' replaces costly and slow physical trial-and-error, enabling rapid convergence to aesthetically superior results. Evaluations confirm that PhotoAgent excels in spatial reasoning and achieves superior final image quality.

---

## 13. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

**Authors:** Max Fu, Justin Yu, Karim El-Refai, ..., Ken Goldberg, Linxi "Jim" Fan
**arXiv:** [2603.22435](https://arxiv.org/abs/2603.22435)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

"Code-as-Policy" considers how executable code can complement data-intensive Vision-Language-Action (VLA) methods, yet their effectiveness as autonomous controllers for embodied manipulation remains underexplored. We present CaP-X, an open-access framework for systematically studying Code-as-Policy agents in robot manipulation. At its core is CaP-Gym, an interactive environment in which agents control robots by synthesizing and executing programs that compose perception and control primitives. Building on this foundation, CaP-Bench evaluates frontier language and vision-language models across varying levels of abstraction, interaction, and perceptual grounding. Across 12 models, CaP-Bench reveals a consistent trend: performance improves with human-crafted abstractions but degrades as these priors are removed, exposing a dependence on designer scaffolding. At the same time, we observe that this gap can be mitigated through scaling agentic test-time computation--through multi-turn interaction, structured execution feedback, visual differencing, automatic skill synthesis, and ensembled reasoning--substantially improves robustness even when agents operate over low-level primitives. These findings allow us to derive CaP-Agent0, a training-free framework that recovers human-level reliability on several manipulation tasks in simulation and on real embodiments. We further introduce CaP-RL, showing reinforcement learning with verifiable rewards improves success rates and transfers from sim2real with minimal gap. Together, CaP-X provides a principled, open-access platform for advancing embodied coding agents.

---

## 14. CATNAV: Cached Vision-Language Traversability for Efficient Zero-Shot Robot Navigation

**Authors:** Aditya Potnis, Francisco Affonso, Shreya Gummadi, Naveen Kumar Uppalapati, Girish Chowdhary
**arXiv:** [2603.22800](https://arxiv.org/abs/2603.22800)
**Categories:** Robotics (cs.RO)

Navigating unstructured environments requires assessing traversal risk relative to a robot's physical capabilities, a challenge that varies across embodiments. We present CATNAV, a cost-aware traversability navigation framework that leverages multimodal LLMs for zero-shot, embodiment-aware costmap generation without task-specific training. We introduce a visuosemantic caching mechanism that detects scene novelty and reuses prior risk assessments for semantically similar frames, reducing online VLM queries by 85.7%. Furthermore, we introduce a VLM-based trajectory selection module that evaluates proposals through visual reasoning to choose the safest path given behavioral constraints. We evaluate CATNAV on a quadruped robot across indoor and outdoor unstructured environments, comparing against state-of-the-art vision-language-action baselines. Across five navigation tasks, CATNAV achieves 10 percentage point higher average goal-reaching rate and 33% fewer behavioral constraint violations.

---

## 15. ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment

**Authors:** Yuzhi Chen, Ronghan Chen, Dongjie Huo, ..., Zhiheng Ma, Mu Xu
**arXiv:** [2603.23376](https://arxiv.org/abs/2603.23376)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Video-based world models offer a powerful paradigm for embodied simulation and planning, yet state-of-the-art models often generate physically implausible manipulations - such as object penetration and anti-gravity motion - due to training on generic visual data and likelihood-based objectives that ignore physical laws. We present ABot-PhysWorld, a 14B Diffusion Transformer model that generates visually realistic, physically plausible, and action-controllable videos. Built on a curated dataset of three million manipulation clips with physics-aware annotation, it uses a novel DPO-based post-training framework with decoupled discriminators to suppress unphysical behaviors while preserving visual quality. A parallel context block enables precise spatial action injection for cross-embodiment control. To better evaluate generalization, we introduce EZSbench, the first training-independent embodied zero-shot benchmark combining real and synthetic unseen robot-task-scene combinations. It employs a decoupled protocol to separately assess physical realism and action alignment. ABot-PhysWorld achieves new state-of-the-art performance on PBench and EZSbench, surpassing Veo 3.1 and Sora v2 Pro in physical plausibility and trajectory consistency. We will release EZSbench to promote standardized evaluation in embodied video generation.

---
