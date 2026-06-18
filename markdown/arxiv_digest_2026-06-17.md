# arXiv Daily Digest — 2026-06-17

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 17

---

## 1. Looped World Models

**Authors:** Hongyuan Adam Lu, Z.L. Victor Wei, Qun Zhang, ..., Zhangyu Wang, Wai Lam
**arXiv:** [2606.18208](https://arxiv.org/abs/2606.18208)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive computation that automatically scales depth to match the complexity of each prediction step. Orthogonal to scaling model size and training data, LoopWM establishes iterative latent depth as a new scaling axis for world simulation, which might significantly push the community forward.

---

## 2. PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space

**Authors:** Bochen Yang, Lianlei Shan
**arXiv:** [2606.17924](https://arxiv.org/abs/2606.17924)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation. Directly decoding actions from vision-language backbone representations enables low-latency control, whereas explicit reasoning through textual chains, pixel-level subgoals, or action search can improve planning but incurs substantial latency and computational cost. We propose PearlVLA, a VLA framework that moves deliberation into the latent space of a vision-language model (VLM). PearlVLA separates VLM meta-query representations into a fixed visual grounding branch and an iterative latent plan branch. At each refinement round, a plan-conditioned world query probes a lightweight frozen latent world model for an action-free future observation latent, which is fed back to guide plan refinement. A future-guided RefineNet then applies scheduled residual updates to progressively refine a coarse semantic draft into a fine-grained latent action plan. The refined plan after K rounds is then decoded in parallel into an action chunk for low-latency execution. We further introduce Causal Refinement-Grouped Process-Reward RL to optimize the latent refinement process with rewards from longer-horizon imagined futures induced by latent plan edits. Empirical evaluations on the LIBERO benchmark demonstrate that PearlVLA achieves state-of-the-art performance among existing methods.

---

## 3. OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation

**Authors:** Zijie Meng, Yufei Liu, Chengqian Ma, ..., Jiquan Yuan, Miao Zhang
**arXiv:** [2606.17536](https://arxiv.org/abs/2606.17536)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-choreographed multi-agent world model that recasts controllable multi-view video generation as latent choreography. Three Qwen2.5-VL agents - a Director parsing user intent into a structured WorldScript, a Cartographer grounding it into spatially-anchored layout tokens, and an Auditor feeding cross-view critiques back as auxiliary supervision - jointly author a single position-aware token sequence. This sequence is co-compressed with the multi-view video via a view-time permutation that enforces inter-camera geometry within the convolutional receptive field of a 3-D VAE. On nuScenes, DRIVE-CHOREO sets new state-of-the-art multi-view consistency and BEV mAP (21.6) with competitive FVD (45.7); a detector trained purely on our synthetic data gains +2.4 NDS on the real validation split, validating downstream utility.

---

## 4. NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama

**Authors:** Logan Mann, Abdur Rahman, Mohammad Saifullah, Taaha Kazi, Vasu Sharma
**arXiv:** [2606.17391](https://arxiv.org/abs/2606.17391)
**Categories:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Long-form serialized audio drama, with arcs that run for 200 to 800 episodes, is a major creative medium and a setting where frontier large language models (LLMs) fail. We benchmark 21 models, spanning classical, fine-tuned, open-frontier, closed-frontier, and reasoning tiers, on a uniform set of structural narrative metrics. All closed-frontier systems saturate at a plot-beat F1 in the band [0.78, 0.81] and collapse by about -0.20 F1 at horizon h=200. We introduce NarrativeWorldBench, an open benchmark of nine narrative-structure metrics evaluated across horizons h in {10, 20, 50, 100, 200}, with cross-lingual evaluation across four Indic languages (Hindi, Tamil, Telugu, Marathi). We introduce N-VSSM, a Narrative Variational State-Space Model that maintains a structured 256-dimensional latent world state over more than 200 episodes via a Mamba-2 backbone with an event-conditioned posterior and an 8B decoder. N-VSSM holds plot-beat F1 >= 0.84 across all horizons at 4x lower compute than the closed-frontier band. A learned Cultural Transfer Function lifts cross-language fidelity by +0.20 to +0.23 Likert points. In a within-subjects writer study (n = 12 professional authors, 240 trials), N-VSSM is preferred over Claude Opus 4.5 on long-arc consistency 71% of the time and rated +1.3 Likert points higher on controllability.

---

## 5. Quantum Cinema: An Interactive Cinematic Exploration of Quantum Computing Hardware via Generative World Models

**Authors:** Aoyu Zhang, Dongping Liu, Luyao Zhang
**arXiv:** [2606.17102](https://arxiv.org/abs/2606.17102)
**Categories:** Popular Physics (physics.pop-ph); Artificial Intelligence (cs.AI); Emerging Technologies (cs.ET); Human-Computer Interaction (cs.HC); Quantum Physics (quant-ph)

Quantum computing promises transformative advances across science and industry, yet the physical hardware that enables these computations remains invisible to the public: quantum processors operate inside sealed dilution refrigerators at temperatures near absolute zero, making direct observation impossible. This "imagination gap" between quantum computing's growing societal impact and the public's ability to visualize it represents a significant barrier to quantum literacy and workforce development. We present Quantum Cinema, an open-source, browser-based interactive application that closes this gap by transforming invisible quantum hardware into explorable, cinematic experiences using generative world models. Quantum Cinema guides users through a four-act narrative -- from the foundational Nobel Prize-winning science of quantum entanglement, through curated video introductions to three major quantum computing architectures (trapped-ion, neutral-atom, and superconducting systems), into immersive three-dimensional generative worlds that make invisible quantum phenomena observable, and finally to interactive radar-chart comparisons grounded in real quantum device specifications. All three-dimensional environments are generated using WorldLabs' generative world model platform and are scientifically grounded in curated metrics from Amazon Web Services (AWS) Braket quantum hardware. Quantum Cinema requires no installation, no specialized hardware, and no quantum computing background. It is designed to serve two distinct communities: scholars and developers seeking to replicate or extend the platform, and educators, researchers, and science communicators seeking an intuitive tool for explaining quantum hardware to diverse audiences. This paper describes the system architecture, the generative world model pipeline, use cases for both communities, and directions for future work.

---

## 6. Uncertainty Quantification for Flow-Based Vision-Language-Action Models

**Authors:** Ralf Römer, Maximilian Seeliger, Saida Liu, ..., Andreas Krause, Angela P. Schoellig
**arXiv:** [2606.18043](https://arxiv.org/abs/2606.18043)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Vision-language-action models (VLAs) combine vision-language backbones with expressive generative action heads trained via flow matching on large-scale robotic datasets. Despite their strong empirical performance in robotic manipulation, VLAs lack mechanisms to quantify confidence in their predictions and to detect when their actions may be unreliable. This presents a critical limitation for real-world deployment in non-stationary environments, where models inevitably encounter scenarios outside their pretraining distribution and may fail without warning. To address this, we derive an efficient method for quantifying epistemic uncertainty in flow-matching models by leveraging velocity-field disagreement (VFD) across a small ensemble. We successfully use this uncertainty estimate for failure detection during deployment and active fine-tuning of flow-based VLAs. To this end, we propose SAVE, a framework for uncertainty-guided active multitask fine-tuning that reduces the number of costly expert demonstrations required to adapt VLAs to new tasks. Through extensive experiments on the LIBERO benchmark, we demonstrate that VFD yields better-calibrated uncertainty estimates predictive of downstream performance, that VFD achieves strong performance in detecting failures, and that uncertainty-guided data acquisition with SAVE requires at least 22% fewer samples than baselines. In summary, our work shows that quantifying epistemic uncertainty in flow-based VLAs improves both failure awareness and adaptation. Project website: this http URL.

---

## 7. ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation

**Authors:** Tianyi Lu, Hui Zhang, Zijie Diao, ..., Zuxuan Wu, Yu-Gang Jiang
**arXiv:** [2606.17937](https://arxiv.org/abs/2606.17937)
**Categories:** Robotics (cs.RO)

Most Vision-Language-Action (VLA) models map observations directly to actions without explicit reasoning, limiting their capacity for reasoning-intensive long-horizon tasks. To address this, existing approaches adopt Chain-of-Thought (CoT) reasoning to enable subgoal decomposition and spatial anticipation. However, those methods lack a unified architecture for effective cross-modal reasoning and fail to explicitly include inverse reasoning ability based on the target state. We argue that manipulation planning naturally decomposes into prediction, anticipating the next visual state, and inverse dynamics, inferring the actions to reach it. Bridging both requires a unified autoregressive architecture that interleaves textual and visual reasoning in a single generation process. We propose \textbf{ThinkingVLA}, a generative model that realizes this decomposition within a unified Mixture-of-Transformers architecture. ThinkingVLA consists of a forward CoT that identifies the immediate subgoal and guides the visual forecasting; the predicted image then serves as the target state, grounding an inverse CoT that reasons about spatial relationships and action intent based on the predicted image; and the final action is generated conditioned on this full reasoning context. Extensive experiments on simulation and real-world benchmarks demonstrate that ThinkingVLA consistently outperforms state-of-the-art baselines, with particularly large gains on long-horizon manipulation tasks.

---

## 8. WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT

**Authors:** Zezhong Qian, Xiaowei Chi, Yu Qi, ..., Zhi Yang Chen, Shanghang Zhang
**arXiv:** [2606.17906](https://arxiv.org/abs/2606.17906)
**Categories:** Robotics (cs.RO)

Recent World-Action (WA) models demonstrate strong generalization ability and data efficiency, but they typically rely on expert trajectories for training. This reliance limits their ability to acquire fine-grained manipulation skills beyond the demonstration distribution and prevents them from continuously improving through real-world interaction. To address these limitations, we propose WAM-RL, a reinforcement learning framework that enables joint optimization of the world model and the action model through online interaction with the environment. By allowing the two components to co-evolve, our approach enhances fine-grained control and adaptability. Specifically, a WA model consists of a world model and an actor. We design a tailored reinforcement learning method with hierarchical optimization to coordinate their improvement. On the methodological side, we systematically investigate the effects of applying reinforcement learning to the action model, as well as online training of the world model within an RL setting. Our experiments reveal a key insight: optimizing only the actor yields improvements on short-horizon tasks, but fails to provide significant gains on long-horizon tasks. In contrast, jointly optimizing both the world model and the actor is critical for achieving strong performance in long-horizon settings. Our work is the first to introduce reinforcement learning into the World-Action paradigm, and provides insights into how online optimization of both the action head and the world model impacts overall performance.

---

## 9. MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation

**Authors:** Xingyuming Liu, Ruichun Ma, Heyu Guo, ..., Jiaolong Yang, Baining Guo
**arXiv:** [2606.17598](https://arxiv.org/abs/2606.17598)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive physical properties that are difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar response. We present MuseVLA, an adaptive multimodal sensing VLA model that integrates novel sensors as on-demand tools for robotic manipulation. Given a task instruction and visual context, MuseVLA first generates a sensor token and target description that select the sensing modality to invoke and what to attend to, analogous to a tool call with arguments. It then converts the selected sensor measurement into a grounded sensor image, a unified intermediate representation that encodes heterogeneous readings for multimodal fusion and action generation. This design decouples sensor-specific processing from the VLA backbone, enabling efficient integration of diverse modalities. To reduce the need for expensive multisensory robot datasets, we further introduce a data synthesis pipeline that augments existing RGB video datasets with grounded sensor images, enabling generalization to unseen sensor-guided tasks. We evaluate MuseVLA on a real-world robot across challenging dexterous hand manipulation tasks that require multimodal sensing inputs, including temperature-guided pick-and-place, audio-driven object search, and radar-assisted hidden object retrieval. MuseVLA achieves 80.6% success rate on average, outperforming RGB-only and multisensory VLA baselines significantly, and exhibits strong zero-shot capabilities on unseen tasks.

---

## 10. ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining

**Authors:** Hao Li, Ganlong Zhao, Yufei Liu, ..., Xiaogang Wang, Hongsheng Li
**arXiv:** [2606.17200](https://arxiv.org/abs/2606.17200)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models benefit from large-scale and diverse embodied data, yet scaling robot trajectory collection is costly and labor-intensive. Recent advances show that large-scale egocentric human videos provide complementary real-world supervision in pretraining. However, joint training on human and robot data remains challenging due to divergences in action spaces, embodiment structures, temporal dynamics, and supervision quality. We introduce ACE-EGO-0, a unified VLA pretraining framework jointly leveraging heterogeneous data sources. To extract large-scale pretraining supervision from egocentric human videos, we build a scalable egocentric video-to-action pipeline that converts raw human videos into robot-format pseudo-action trajectories. To make these labels comparable with robot demonstrations, ACE-EGO-0 uses a unified action representation based on camera-space actions, morphology conditioning, and time-aligned action chunking. To robustly leverage noisy pseudo-action supervision from egocentric human videos, we formulate a reliability-aware training objective with a human auxiliary loss that concentrates supervision on reliable signals. We instantiate ACE-EGO-0 on 4.53K hours of robot and simulation data, together with 1.48K hours of pseudo-action-labeled egocentric human data. Experiments show that incorporating large-scale human supervision under reliability-aware weighting consistently improves both unified joint pretraining and supervised fine-tuning. ACE-EGO-0 achieves state-of-the-art performance on RoboCasa GR1 TableTop and RoboTwin 2.0, while demonstrating strong transfer to real-world bimanual manipulation.

---

## 11. GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning

**Authors:** Haoyu Wang, Guoqing Ma, Zeyu Zhang, ..., Boxin Shi, Hao Tang
**arXiv:** [2606.17480](https://arxiv.org/abs/2606.17480)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: this https URL. Website: this https URL.

---

## 12. Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion

**Authors:** Nils Morbitzer, Jonathan Evers, Artem Savkin, ..., Federico Tombari, Stefano Gasperini
**arXiv:** [2606.18250](https://arxiv.org/abs/2606.18250)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. Unlike prior works that treat the world as a sequence of image-based features, FR3D explicitly decouples the 3D evolution of the scene from the agent's trajectory, treating the inferred ego-motion as a latent proxy for action. This disentanglement resolves the ambiguities between self-motion and world-motion, ensuring geometric consistency into the future. Furthermore, we introduce a teacher-student distillation strategy that leverages the spatial "common sense" of off-the-shelf foundation models, leading to robust zero-shot generalization. Extensive experiments demonstrate FR3D's strong performance for future dynamic 3D reconstruction from monocular observations across multiple datasets, even 2 seconds into the future. Project page: this https URL.

---

## 13. EgoCS-400K: An Egocentric Gameplay Dataset for World Models

**Authors:** Rongjin Guo, Dong Liang, Yuhao Liu, ..., Gerhard P. Hancke, Rynson W. H. Lau
**arXiv:** [2606.18180](https://arxiv.org/abs/2606.18180)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

The shift from video generation to interactive world modeling places new demands on data: beyond captioned videos, world models require temporally aligned video-action-language trajectories grounded in the actions, camera motion, states, and events that drive future scene changes. However, such data is difficult to obtain at scale. Web video datasets offer broad visual coverage but lack executable actions and reliable states; robotic datasets provide action and state supervision but are costly and limited in scene diversity; and existing simulators often lack large-scale human-driven interaction trajectories. In this paper, we introduce EgoCS-400K, a large-scale replay-grounded egocentric Counter-Strike dataset for world models, built from public professional CS and CS2 match demos that preserve human gameplay trajectories and enable parsing, replaying, rendering, and temporal alignment. We extract player states, view directions, movements, keyboard/button inputs, view-angle changes, weapon usage, game events, and round-level context, and render clean first-person videos from the same trajectories. EgoCS-400K contains over 400,000 first-person videos and 10,000 hours of gameplay from more than 1,000 matches and 40,000 rounds, covering 13 maps and 10 player viewpoints per round. It supports a range of interactive visual modeling tasks, including action-conditioned future prediction, state- and event-aware scene rollout, replay-grounded captioning, and agent egocentric action understanding. By connecting visual observations with human actions, camera motion, game states, and events at scale, EgoCS-400K serves as a practical bridge between passive web videos, controllable game simulation, and costly real-world embodied data.

---

## 14. MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model

**Authors:** Lichen Bai, Tianhao Zhang, Shitong Shao, ..., Shurui Yang, Zeke Xie
**arXiv:** [2606.17800](https://arxiv.org/abs/2606.17800)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

As an increasing majority of global video content is consumed on social platforms for interactive social purposes, video generation models built for social worlds are important but largely overlooked by previous studies. In this work, we define the position of social world models and build a prototype model as the first step towards this goal. While previous world models successfully simulate physical environments or gaming world exploration, they remain fundamentally detached from human-centric social dynamics. To bridge this gap as the first step to social world models, we present MaineCoon, the first real-time audio-visual autoregressive model that has 22B parameters and is capable of real-time streaming generation and sub-second interaction, with a record-breaking frame rate of up to 47.5 FPS, on a single GPU. To the best of our knowledge, MaineCoon is also the first real-time audio-visual generation model specifically optimized for social-interactive applications. To enable efficient and stable training, we introduce several novel techniques into MaineCoon, including self-resampling, cross-modal representation alignment, domain-aware preference optimization, and reinforced online-policy distillation (ROPD). We also design the first agentic streaming inference framework that supports thousand-second-scale or even longer generation while mitigating drift with agentic cache management and prompt planing. These innovations significantly accelerate training while optimizing real-time inference performance. We believe this work not only sets a new state-of-the-art (SOTA) performance benchmark for high-quality, low-latency, and long-horizon audio-visual autoregressive models, but also points out the paradigm shift desired for next-generation AI-native social platforms.

---

## 15. ActWorld: From Explorable to Interactive World Model via Action-Aware Memory

**Authors:** Zhexiao Xiong, Yizhi Song, Hao Kang, ..., Xin Lu, Nathan Jacobs
**arXiv:** [2606.17730](https://arxiv.org/abs/2606.17730)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Interactive world models aim to simulate environment dynamics under real-time user actions. However, their action vocabulary is largely confined to navigation: most actions correspond to motion (e.g., walk, turn, look around), while interaction with objects in the scene (e.g., pick up plates, open doors, or trigger physical responses) is either absent, restricted to game domains, or relegated to prompt-to-full-video scenarios. The resulting worlds are visually explorable but not truly actionable. In this work, we present ActWorld, an interactive world model that extends prior navigation-centric generators to support mid-rollout object interaction within a chunk-autoregressive framework. We argue that the navigation-interaction gap stems from two bottlenecks. First, a data bottleneck: the lack of human-object interaction data with accurate, dense labels. Second, a memory bottleneck: recency-biased history compression in existing world models discards the event-transition frames that causally determine subsequent object states, leading to an action-forgetting pathology. On the data side, we construct a 100K interaction video dataset, each annotated with per-chunk captions via chain-of-thought reasoning. On the model side, we introduce a hierarchical action-aware memory design that routes history compression by interaction importance, complemented by a persistent memory bank that maintains event-update and object-identity tokens across long rollouts. Experiments show that ActWorld supports both flexible navigation and rich object interaction within a single model, substantially improving interaction fidelity over navigation-only baselines without sacrificing viewpoint control. Project page is available at this https URL.

---

## 16. Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models

**Authors:** Haoqi Yuan, Zhixuan Liang, Anzhe Chen, ..., Chenfei Wu, Xiong-Hui Chen
**arXiv:** [2606.17846](https://arxiv.org/abs/2606.17846)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Foundation models in language and multimodality achieve strong generalization by aligning heterogeneous data under a unified formulation and training at scale. In this report, we investigate whether this scaling recipe can be applied to robotic manipulation to achieve genuine generalization. This is challenging because, unlike text, manipulation data is heterogeneous by nature, expensive to collect, and narrow in diversity, making alignment and scale simultaneously difficult. We present Qwen-RobotManip, a generalizable Vision-Language-Action foundation model built on Qwen-VL. Qwen-RobotManip introduces a unified alignment framework across the representation, motion, and behavioral dimensions of manipulation, making large-scale multi-source training coherent rather than conflicting. This alignment capability in turn enables Qwen-RobotManip to absorb manipulation data at a scale that prior training regimes could not sustain. A human-to-robot synthesis pipeline converts egocentric hand demonstrations into robot trajectories across 15 platforms, and a rigorous curation pipeline harmonizes heterogeneous datasets. Using only open-source datasets and human videos without proprietary data collection, Qwen-RobotManip constructs a ~38,100-hour pretraining corpus and exhibits emergent generalization capabilities, including zero-shot instruction following, robustness to perturbations, reactive error recovery, and cross-embodiment transfer. We find that standard benchmarks fail to capture pretraining quality and instead adopt OOD settings including RoboCasa365, LIBERO-Plus, EBench, RoboTwin-Clean2Rand, RoboTwin-IF, and RoboTwin-XE. Qwen-RobotManip substantially outperforms prior state-of-the-art models, including $\pi$0.5, across all OOD settings, ranks 1st in RoboChallenge with a 20% relative improvement, and is validated on real-robot platforms including AgileX ALOHA, Franka, UR, and ARX.

---

## 17. EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies

**Authors:** Ning Gao, Jinliang Zheng, Xing Gao, ..., Weinan Zhang, Chunhua Shen
**arXiv:** [2606.18239](https://arxiv.org/abs/2606.18239)
**Categories:** Robotics (cs.RO)

We present EBench, a simulation benchmark that diagnoses generalist mobile manipulation policies beyond a single success-rate scalar. EBench comprises 26 diverse and challenging manipulation tasks annotated along 5 capability dimensions and 4 generalization dimensions. We evaluate state-of-the-art generalist manipulation models including $\pi_0$, $\pi_{0.5}$, XVLA, and InternVLA-A1, and reveal that models with near success rates exhibit strikingly different capability profiles: $\pi_{0.5}$ achieves the highest test success rate and the best train--test retention, whereas InternVLA-A1 dominates mobile manipulation but collapses on dexterous tasks, and XVLA exhibits strengths on a disjoint set of atomic skills compared to other policies. Beyond capability profiling, EBench analyzes the generalization ability from 4 representative perspectives, identifying the impact of different distribution shift factors. The results reveal strengths and weaknesses of models behind an overall score. We hope this benchmark offers a broad set of diagnostic signals to guide iteration on generalist manipulation models.

---
