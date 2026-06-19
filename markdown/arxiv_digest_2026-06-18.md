# arXiv Daily Digest — 2026-06-18

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 15

---

## 1. Dual-Channel Grounded World Modeling (DCGWM): Structural Prevention of Objective Interference Collapse via Heterogeneous External Grounding with Inward-Only Gradient Flow

**Authors:** Akshay Hazare
**arXiv:** [2606.18688](https://arxiv.org/abs/2606.18688)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Joint Embedding Predictive Architectures (JEPAs) are a leading approach to world model representation learning. We identify a failure mode in JEPA-based world models grounded against two qualitatively distinct external signals: physical dynamics (sparse, high-magnitude, constraint-satisfying gradient corrections) and social-behavioral dynamics (diffuse, distribution-matching corrections). We term this Objective Interference Collapse (OIC): we argue that joint learning in a shared latent space causes the dominant channel to systematically collapse the subordinate channel's representational subspace, in a manner not resolvable by loss weighting alone. We propose Dual-Channel Grounded World Modeling (DCGWM), designed to structurally prevent OIC through a partitioned latent space (physical subspace Z_p, behavioral subspace Z_b) with inward-only gradient flow. A Physical Grounding Channel updates only Z_p via VICReg-style alignment to physical measurements; a Social-Behavioral Grounding Channel updates only Z_b via alignment to trajectories from an emergent multi-agent simulation. An Inter-Channel Interface Module couples the subspaces at the task level without cross-subspace gradients. An Asymmetric Grounding Adherence Loss penalizes rollout drift with a hard hinge for physical violations and a soft KL for behavioral divergence. A Generative Rendering Layer is architecturally isolated from the latent world model. We present three theoretical results: the partition removes the gradient-interference pathway implicated in OIC; each grounded subspace inherits anti-collapse guarantees from its alignment objective; and generative isolation is necessary under a stated assumption on the generative objective's geometry. This manuscript establishes the problem formulation and architecture; experimental validation is ongoing and will be reported in a future revision.

---

## 2. Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models

**Authors:** Nikita Kachaev, Andrey Moskalenko, Matvey Skripkin, ..., Alexey K. Kovalev, Vlad Shakhuro
**arXiv:** [2606.19297](https://arxiv.org/abs/2606.19297)
**Categories:** Machine Learning (cs.LG); Robotics (cs.RO)

Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning powerful pretrained VLMs on robotics data, yet it is unclear how much commonsense and factual knowledge they retain after adaptation. Failures on knowledge-sensitive tasks are ambiguous, conflating missing knowledge with poor generalization of low-level control. We introduce Act2Answer, a lightweight protocol that adapts VLM knowledge benchmarks to VLA evaluation by requiring agents to answer through action. Each question becomes a short tabletop episode where the agent performs a single object-placement action to select among candidate answers, yielding an action-grounded success rate with reduced control confounds. We curate a test suite of such environments across diverse commonsense and world-knowledge categories and introduce layerwise intent probing to localize answer-relevant information across the VLM backbone and action head. In a large-scale study of 7 VLA models and 9 VLM baselines, we systematically rank models across categories, finding that VLAs show solid performance on simple concepts while exhibiting larger gaps on richer semantic categories relative to their source VLMs, that VQA co-training is associated with better knowledge retention, and that answer-relevant signals peak in middle VLA layers but attenuate in upper layers. Act2Answer is available at this https URL.

---

## 3. Stealthy World Model Manipulation via Data Poisoning

**Authors:** Yibin Hu, Xiaolin Sun, Zizhan Zheng
**arXiv:** [2606.18697](https://arxiv.org/abs/2606.18697)
**Categories:** Machine Learning (cs.LG); Cryptography and Security (cs.CR); Robotics (cs.RO)

Model-based learning agents use learned world models to predict future states, plan actions, and adapt to new environments. However, the process of updating world models from collected experience creates a training-time attack surface: adversarially poisoned fine-tuning trajectories can manipulate the learned dynamics and thereby corrupt downstream planning. In this paper, we propose SWAAP, the first two-stage data poisoning framework for learned world models. In the first stage, SWAAP identifies a harmful target world model that induces low-return behavior under planning while remaining close to clean dynamics, using first-order bilevel optimization enabled by a transition-gradient theorem. In the second stage, SWAAP realizes this target through stealth-constrained gradient matching, modifying only a limited fraction of fine-tuning transition targets so that the induced training gradients steer the victim model toward the adversarial target, while a prediction-error regularizer encourages the poisoned targets to remain close to the world model's natural approximation error. To assess attack stealthiness, we evaluate defenses and detectability across three stages of the poisoning pipeline: pre-training detection of poisoned transitions, robust training during fine-tuning, and test-time monitoring of the resulting world model. Across diverse continuous-control tasks, SWAAP causes substantial performance degradation while keeping poisoned transitions close to clean data and evading the evaluated non-adaptive residual/CUSUM/TRIM-style defenses. These results reveal a practical vulnerability in world-model adaptation pipelines and highlight the need for robustness methods that protect both world-model training data and learned dynamics.

---

## 4. Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

**Authors:** Kinam Kim, Namiko Saito, Heecheol Kim, ..., Jaegul Choo, Yasuyuki Matsushita
**arXiv:** [2606.18953](https://arxiv.org/abs/2606.18953)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models can generalize across diverse manipulation tasks, but their imitation-learning-based policies remain brittle in precise physical interactions due to compounding execution errors; Can a reinforcement learning policy trained purely in simulation improve the robustness of real-world VLAs zero-shot? Residual RL, which learns a corrective policy on top of a frozen VLA, offers a natural framework, but existing approaches face a fundamental sim-to-real dilemma: privileged-state methods require lossy distillation for deployment; image-based methods suffer from the visual domain gap; and real-world RL is costly and unsafe. We propose an object-centric residual RL framework that refines VLA actions using object poses, enabling a compact observation space that transfers consistently between simulation and reality. To align the two domains, we additionally replay the same teleoperation demonstrations in simulation to train a sim counterpart of the real-world VLA. The residual RL policy is trained only in simulation with pose noise injection and dropout, and transfers zero-shot to the real robot. Across five manipulation tasks on a real Franka Research 3 (FR3) robot, our method improves the success rate from 42% to 76% zero-shot, and the improved rollouts can be further reused to retrain the base VLA for self-improvement without additional teleoperation. Project page: this https URL

---

## 5. DREAM-Chunk: Reactive Action Chunking with Latent World Model

**Authors:** Wenxi Chen, Kaidi Zhang, Chi Lin, ..., Shaoshuai Mou, Yan Gu
**arXiv:** [2606.18589](https://arxiv.org/abs/2606.18589)
**Categories:** Robotics (cs.RO)

Action chunking has become a common interface for vision-language-action (VLA) models, enabling low-frequency policy inference to drive high-frequency robot execution. However, once an action chunk is committed, its open-loop execution can be brittle under stochastic dynamics, hardware execution errors, and partial observability. We propose DREAM-Chunk, a test-time scaling method that augments chunking-based policies with a lightweight latent world model, without requiring additional policy fine-tuning. At test time, DREAM-Chunk samples multiple candidate action chunks, rolls out their predicted latent futures, and selects actions from the chunk whose predicted state best matches the observed rollout. In this way, DREAM-Chunk uses additional test-time computation to cover multiple plausible stochastic futures and improve reactivity during long-horizon chunk execution. On the Kinetix benchmark, DREAM-Chunk improves robustness under increasing action noise and benefits from larger candidate sample sizes, especially when demonstrations contain corrective behaviors. We further validate DREAM-Chunk on four manipulation tasks across two robot platforms and two VLA policies under various sources of stochasticity. Across simulation and hardware experiments, DREAM-Chunk improves the robustness of action-chunking policies in stochastic dynamics.

---

## 6. VEGA: Learning Navigation VLAs from In-the-Wild Egocentric Video with Geometric Trajectory Supervision

**Authors:** Gershom Seneviratne, Yohan Abeysinghe, Jianyu An, Vaibhav Shende, Dinesh Manocha
**arXiv:** [2606.18426](https://arxiv.org/abs/2606.18426)
**Categories:** Robotics (cs.RO)

We introduce VEGA, an approach for training navigation VisionLanguage-Action (VLA) models from unlabeled egocentric navigation videos. Internet-scale egocentric videos provide a scalable source of navigation-relevant visual observations, capturing cluttered scenes, close-range obstacles, and natural human motion through real-world spaces. However, these videos are not directly usable for policy learning because they do not provide obstacle-aware trajectories conditioned on explicit navigation goals in the robot's coordinate frame. VEGA addresses this gap by reconstructing local scene geometry from monocular video, sampling navigation goals (represented as text, image, or spatial waypoints) and generating obstacle-aware trajectories using the constructed geometry. The resulting trajectory distribution is then used to train a flow-matching VLA navigation policy. By using geometry exclusively during training, VEGA distills obstacle-aware planning directly into a vision-based policy. Furthermore, we introduce VEGA-Bench, a benchmark containing 250k scenes and approximately 5 million navigation goals paired with scene geometry, designed to evaluate goal progress, collision avoidance, and obstacle clearance of VLAs. Our evaluation shows that VEGA achieves competitive goal progress while reducing collisions by 33.0% and improving obstacle clearance by 17.9% over the strongest baseline on VEGABench, while improving success by at least 150.0%, reducing collisions by at least 66.7%, and improving obstacle clearance by at least 60.0% in real-world trials. Ultimately, we demonstrate that video-derived geometric supervision provides a scalable and effective signal for training obstacle-aware navigation VLAs. The code and benchmark will be released at the time of publication.

---

## 7. Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation

**Authors:** Zirui Zheng, Jiaqian Yu, Xiongfeng Peng, ..., Huchuan Lu, Xu Jia
**arXiv:** [2606.18960](https://arxiv.org/abs/2606.18960)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Action-conditioned world models have emerged as a promising paradigm for robot learning, offering a scalable alternative to costly real-world experimentation by generating action-consistent video rollouts. However, persistent world modeling remains challenging in manipulation: frequent end-effector occlusions and rapid wrist-camera motion make the current observation insufficient for predicting future views, causing models to forget or hallucinate scene details seen in earlier frames. Existing memory retrieval strategies often fail to identify informative history in dynamic manipulation scenarios. To address this limitation, we propose Mem-World, a memory-augmented multi-view action-conditioned world model. At its core, we present W-VMem, a 4D wrist-view-centered surfel-indexed memory that anchors historical observations to temporally evolving surface elements. By explicitly modeling when and where scene elements are observed, W-VMem enables geometry-aware retrieval of relevant history frames conditioned on future actions. During generation, relevant history frames are selected via surfel-based rendering and scoring, providing informative and non-redundant context for prediction. Extensive experiments show that Mem-World generates persistent rollouts in complex manipulation scenarios, enables more reliable policy evaluation than Ctrl-World, improving the Pearson correlation with real-world performance by 14.5\%, and supports effective policy improvement through synthetic data generation, increasing success rates from 58\% to 72\% on long-horizon tasks.

---

## 8. Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos

**Authors:** Runze Xu, Yiluo Zhang, Jian Wang, Yu Wang, Jincheng Yu
**arXiv:** [2606.18955](https://arxiv.org/abs/2606.18955)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Training generalist Vision-Language-Action(VLA) models typically requires massive, diverse robotic datasets with high-fidelity action annotations. While egocentric human manipulation videos are abundant and capture significant environmental diversity, the absence of action labels makes them difficult to use in conventional training paradigms. To address this, we propose a latent-action-based framework designed to extract general action priors from unlabeled human videos. The architecture features a Hybrid Disentangled VQ-VAE that decouples motion dynamics from environmental backgrounds through physical masks, enabling the construction of a cross-embodiment action codebook. By pre-training on human videos with the codebook, the VLM backbone learns deep representations of action intent. For adaptation to specific embodiments, we introduce an intent-perception decoupling strategy where the VLM predicts the action intent while a separate frozen visual encoder provides state-specific features to the action expert, thereby reducing action hallucinations. Results in simulation and real-world environments show that our method, pre-trained exclusively on unlabeled human videos, performs competitively with state-of-the-art VLA models trained on massive annotated datasets, requiring only 50 trajectories for downstream adaptation.

---

## 9. DreamReg: Belief-Driven World Model for 2D-3D Ultrasound Registration

**Authors:** Luoyao Kang, Yuelin Zhang, Jiwei Shan, ..., Qingpeng Ding, Shing Shin Cheng
**arXiv:** [2606.18825](https://arxiv.org/abs/2606.18825)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Ultrasound (US) is widely used for surgical navigation, yet real-time registration between intraoperative 2D slices and preoperative 3D volumes remains challenging due to partial observability, speckle noise, and the action-dependent US acquisition. Existing methods are one-shot or short-horizon, making it hard for them to gather evidence over time or capture how surgeons adjust probe motion based on on-screen feedback. We propose DreamReg, a belief-driven world-model framework that formulates 2D-3D registration as belief updating over rigid transformations. DreamReg maintains a latent belief state that summarizes past observations and poses information, and continuously refines the transformation through learned dynamics as new slices arrive. During training, DreamReg is exposed to probe-motion trajectories that mimic clinical scanning behavior and learns to update its belief by conditioning pose refinement on the current US observation. During inference, DreamReg refines registration via internal imagination: it rolls out the learned world model to simulate candidate probe motions and their predicted observations, and integrates these imagined outcomes to converge to an accurate rigid transformation. Experiments on CAMUS and u-RegPro datasets demonstrate improved robustness and competitive registration accuracy for real-time guidance compared with state-of-the-art methods.

---

## 10. Guava: An Effective and Universal Harness for Embodied Manipulation

**Authors:** Haowen Liu, Xirui Li, Shaoxiong Yao, ..., Furong Huang, Jiayuan Mao
**arXiv:** [2606.18363](https://arxiv.org/abs/2606.18363)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Language models trained on large-scale vision-language data have demonstrated strong potential for embodied agents. Harnessing models through embodied tools use offers a promising alternative to end-to-end vision-language-action systems by combining high-level reasoning with external modules for perception, planning, and control. However, it remains unclear what makes an effective harness for embodied manipulation, and to what extent such a harness can unlock embodied capabilities in a wide range of reasoning models. In this work, we present Guava, a harness framework for embodied tool use developed through systematic exploration of the design space of agent workflows, action spaces, and observation spaces. Our study identifies three key ingredients for effective embodied agents: iterative perception-reasoning-action loops, semantic action abstractions, and multimodal observations. To understand whether these design principles are universal even to small models, we develop an end-to-end training pipeline that distills embodied manipulation capabilities into a 4B open-source model using fewer than 2K trajectories collected entirely in simulation. Experimental results in both simulation and real-world environments show performance comparable to frontier proprietary models while exhibiting strong generalization to unseen objects, novel instructions, and long-horizon tasks. Results suggest that a well-designed harness can serve as a scalable, model-agnostic interface for embodied manipulation, enabling strong emergent embodied capabilities in compact open-source models with minimal training data.

---

## 11. Zero-Shot Long-Horizon Dexterous Manipulation via Multi-View 3D-Grounded VLM Reasoning

**Authors:** Jisoo Kim, Sangwon Baik, Taeksoo Kim, ..., Mingi Choi, Hanbyul Joo
**arXiv:** [2606.19340](https://arxiv.org/abs/2606.19340)
**Categories:** Robotics (cs.RO)

We present a zero-shot framework for long-horizon dexterous manipulation that grounds language instructions into executable 3D task plans from calibrated multi-view RGB images. Rather than training an end-to-end policy, our system uses a vision-language model (VLM) to produce reference-frame task grounding and primitive-level 2D keypoints, then lifts them into 3D via multi-view fusion. This lifting combines triangulation of view-wise VLM groundings with reference-view ray voting, which searches along a semantic camera ray for geometrically consistent candidates across neighboring views. The resulting 3D keypoints support both pick-and-place and tool-use: for tool-use, we retrieve an object-centric atomic action corresponding to the inferred skill category and align its stored 6D tool trajectory to the scene; for dexterous execution, we expand the lifted grasp keypoint into a task-conditioned grasp affordance region and generate feasible grasp-motion pairs with an arm-hand motion generator. Real-world experiments show improved 3D grounding accuracy and execution reliability over single-view RGB-D grounding and fine-tuned VLA baselines. We further demonstrate long-horizon manipulation through closed-loop status verification and replan, enabling zero-shot execution on unseen objects and tool-use tasks in novel scenes.

---

## 12. Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation

**Authors:** Yu Zhang, Kangyi Ji, Yongxiang Zou, ..., Feng Zheng, Long Cheng
**arXiv:** [2606.19194](https://arxiv.org/abs/2606.19194)
**Categories:** Robotics (cs.RO)

This paper presents an invertible neural network adapter for general robotic manipulation, designed to generate precise high-dimensional actions conditioned on multimodal observations, including visual, linguistic, and proprioceptive inputs, through a one-step denoising process. Built upon a flow-matching formulation, the proposed adapter effectively constrains the action generation trajectory within an invertible latent space, thereby enabling efficient and high-quality dexterous action synthesis with only a single inference step. Compared with conventional iterative flow-matching policies, the proposed framework substantially reduces inference complexity while maintaining strong action prediction accuracy and stability. Extensive experiments are conducted across a diverse set of simulation benchmarks and real-world robotic platforms to evaluate the effectiveness of the proposed method. Across simulation benchmarks, the proposed adapter consistently demonstrates superior or near state-of-the-art performance on a wide range of manipulation tasks. Furthermore, real-world experiments reveal a significant improvement in inference efficiency for vision-language-action (VLA) models, reducing the average inference latency from 110 ms to 61 ms while maintaining strong task performance.

---

## 13. SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation

**Authors:** Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, ..., Ming-Yu Liu, Quan Vuong
**arXiv:** [2606.18610](https://arxiv.org/abs/2606.18610)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Evaluating generalist robot manipulation policies in the real world is expensive, slow, and difficult to scale. Action-conditioned video world models offer a scalable alternative by simulating policy rollouts. Autoregressive rollouts accumulate compounding errors, observations across multiple camera views must remain mutually consistent, and the evaluator must generalize to policies whose behaviors lie outside the training distribution. We address these challenges with SC3-Eval, a self-consistent video generation recipe that adapts a pre-trained video foundation model into an accurate policy evaluator by enforcing three complementary forms of consistency. First, forward-inverse dynamics consistency jointly trains the model to predict frames from actions and to recover actions from frames, anchoring generated rollouts to a physically plausible action manifold and counteracting the drift a forward-only model cannot penalize. Second, cross-view consistency trains the model to inpaint each camera view from the other, keeping the multi-camera observation coherent over long rollouts without any explicit memory mechanism. Third, test-time consistency reuses the inverse dynamics mode at inference as a per-action-chunk uncertainty signal that terminates rollouts whose generated frames drift away from the requested actions. We also demonstrate SC3-Eval rollouts reproduce the failure modes that policies exhibit in real-world rollouts, supporting fine-grained diagnostic comparison rather than aggregate ranking alone. Across seven real-world vision-language-action policies, SC3-Eval attains a closed-loop Pearson correlation of $0.929$ and MMRV of $0.119$, outperforming three strong prior video-model-based baselines, and generalizes to new tasks.

---

## 14. PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation

**Authors:** Yuhang Huang, Xuan Lv, Junyan Xu, ..., Haibin Yu, Kai Xu
**arXiv:** [2606.18375](https://arxiv.org/abs/2606.18375)
**Categories:** Robotics (cs.RO)

World foundation models (WFMs) are powerful simulators, yet they predominantly operate in a single-view setting and lack the multi-view 3D consistency required for robotic manipulation. While robotic systems rely on multiple cameras (egocentric, eye-to-hand, and wrist-mounted) for policy learning, current multi-view world models simply concatenate view tokens without explicit geometric reasoning. This causes cross-view object drift, depth inconsistency, and texture misalignment. We trace these failures to two deficiencies: the absence of an explicit inter-view communication mechanism and the lack of a 3D geometric prior. We argue that resolving both simultaneously is necessary and sufficient. To address this, we present PAIWorld, a framework that augments diffusion-transformer world models via three core components: (1) Geometry-Aware Cross-View Attention blocks that establish an explicit pathway across views, (2) Geometric Rotary Position Embedding that encodes camera ray directions and extrinsic poses into the attention mechanism, and (3) Latent 3D-REPA, which distills 3D-aware features from frozen 3D foundation models to ensure 3D consistency. Built upon a DiT-based world foundation model, PAIWorld achieves state-of-the-art multi-view 3D consistency on robotic manipulation benchmarks, ranking 1st on the WorldArena leaderboard and 2nd on the AgiBot-Challenge2026 leaderboard, while enabling downstream applications such as model-based planning, world action models, and multi-view policy post-training.

---

## 15. Physics-IQ Verified

**Authors:** Tim Rädsch, Yuki M Asano, Hilde Kuehne, ..., Robert Geirhos, Carsten T. Lüth
**arXiv:** [2606.18943](https://arxiv.org/abs/2606.18943)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video generative models ( VGMs) have become a new frontier that can be used not just for video generation but for a multitude of downstream tasks, including world modeling. To advance these tasks, a good video model must understand the physical reality of the world. Evaluating this understanding is an emerging field and has led to the Physics-IQ benchmark, which quantifies this explicitly by comparing model-generated videos to real-world videos of physical experiments. In this work, we present a systematic audit of the Physics-IQ benchmark, expose shortcomings and propose three solutions that sharpen how we can measure physical understanding of VGMs. Specifically, we improve prompt and ground-truth quality to reduce the influence of confounding factors and further introduce a sample-level scoring system that weights each sample and metric equally. Our resulting benchmark, Physics-IQ Verified, refines 57.6\% of all samples and improves over 34.8\% of prompts. In a comparison study using six image-to-video generative models, we observe moderate but meaningful ranking changes (Kendall's $\tau = 0.46$). We hope Physics-IQ Verified advances the community by providing a more reliable signal toward physically accurate VGMs. The code for the benchmark can be accessed at this https URL

---
