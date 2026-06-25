# arXiv Daily Digest — 2026-06-24

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 12

---

## 1. World Models in Pieces: Structural Certification for General Agents

**Authors:** Yikai Lu, Yifei Wu, Xinyu Lu, Tongxin Li
**arXiv:** [2606.24842](https://arxiv.org/abs/2606.24842)
**Categories:** Artificial Intelligence (cs.AI)

In the big-world regime, agents cannot be universally capable and their ability is inevitably specialized across a world model in pieces. Consequently, standard uniform guarantees fail to distinguish between the understanding of critical bottlenecks and irrelevant failures. We first formalize this limitation by proving that general agents are not universal, rendering standard worst-case analysis uninformative. To overcome this, we introduce structural certification, a transition-local framework that maps bounded goal-conditioned performance to entry-wise guarantees on the agent's internal world model. Our main contribution is constructive. We provide algorithms that filter specific transitions using deep compositional goals and prove that a general agent on these goals has a structural world model with a $\mathcal{O}(1/n) + \mathcal{O}(\delta)$ error bound. Conversely, this bound is tight in the small-$\delta$ regime, whose existence is explicitly guaranteed by our certification. These results enable the certifiable deployment of general agents by localizing the specific transitions where long-horizon planning is reliable.

---

## 2. Neuro-Symbolic Drive: Rule-Grounded Faithful Reasoning for Driving VLAs

**Authors:** Xiangbo Gao, Xiukun Huang, Boyu Lu, ..., Wei Xiong, Zhengzhong Tu
**arXiv:** [2606.23938](https://arxiv.org/abs/2606.23938)
**Categories:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Driving VLA models incorporating Chain-of-Thought (CoT) reasoning are attractive because they leverage pretrained VLM representations and expose intermediate decisions in natural language, yet current rationales often lack the step-by-step decision semantics needed to keep the rationale causally connected to the planned motion. We introduce Neuro-Symbolic Drive, a neuro-symbolic driving framework that supervises a driving VLA with rule-grounded reasoning traces extracted directly from classical rule-based planners. Our key observation is that rule-based planners are symbolic AI systems that already function as executable reasoning engines: they reason about active safety constraints, search over candidate maneuvers, and select a final trajectory. We instrument these planners in simulation to capture both the executed trajectory and the internal decision trace at each rule-evaluation step. Each trace is serialized into structured rule-grounded reasoning and paired with the trajectory to fine-tune Qwen3.5-4B as a driving VLA. Because these traces are derived directly from the planner states that determine the action, they ensure reasoning is structurally coupled to motion generation by construction, rather than by post-hoc alignment. On our simulator-generated benchmark, detailed rule-grounded reasoning reduces ADE@3s from 0.47 to 0.26 and miss rate from 8.30% to 6.40% under three-camera perception, and from 0.54 to 0.26 and 10.13% to 5.99% under eight-camera perception. Neuro-Symbolic Drive thus converts neuro-symbolic planning logic into structured supervision. Code base: this https URL.

---

## 3. InSight: Self-Guided Skill Acquisition via Steerable VLAs

**Authors:** Maggie Wang, Lars Osterberg, Stephen Tian, ..., Jiajun Wu, Mac Schwager
**arXiv:** [2606.24884](https://arxiv.org/abs/2606.24884)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Vision-language-action (VLA) models can learn manipulation skills from demonstrations, but their capabilities are bounded by the skills in the training data. We present InSight, a framework that unlocks autonomous skill acquisition by rendering VLAs steerable at the primitive-action level (e.g., "move gripper to the bowl", "lift upward", "pour the bottle"). InSight consists of two primary stages: (1) an automated segmentation pipeline that partitions demonstrations into labeled primitives via VLM plan decomposition and end-effector poses to enable VLA primitive steerability, and (2) a VLM-guided data flywheel that identifies missing primitives required to accomplish a novel task, autonomously attempts demonstrations of the missing primitives with VLM-proposed low-level control, and automatically labels, stores, and integrates successful demonstrations into the VLA training set. We evaluate InSight across simulation and real-world manipulation tasks, including block flipping, drawer closing, sweeping, twisting, and pouring, without any human demonstrations of these target skills. Once learned, these primitives can be composed to execute novel, long-horizon tasks without additional human demonstrations. Our findings demonstrate that primitive steerability provides a practical foundation for continual skill acquisition in VLA policies. Project website: this https URL.

---

## 4. G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models

**Authors:** Yue Peng, Yongzhe Zhao, Artur Habuda, ..., Fares Abu-Dakka, Li Guo
**arXiv:** [2606.24472](https://arxiv.org/abs/2606.24472)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-language-action (VLA) models have made rapid progress in generalist robot manipulation by harnessing semantic knowledge from pretrained vision-language backbones, but their visual tokens remain grounded in 2D image coordinates rather than the calibrated geometry of the robot's cameras -- a mismatch especially pronounced in multi-camera setups, where views are coupled by known intrinsics and extrinsics yet processed as independent images. We propose G$^3$VLA, a camera-aware geometric module that injects calibrated structure into the visual-token stream of a pretrained VLA without altering its action space or imitation objective, combining intrinsic-conditioned ray embeddings, projective positional encoding (PRoPE), and bidirectional cross-view fusion. Geometric supervision is provided either from ground-truth point maps when available, or from confidence-gated $\pi^3$X teacher predictions, requiring no depth sensors or manual annotations. Instantiated on $\pi_0$, G$^3$VLA yields consistent gains across the LIBERO suites, RoboCasa24, RoboTwin2.0, and real-robot settings, with the largest improvements on spatially and object-sensitive tasks. We further validate on $\pi_{0.5}$ and GR00T 1.5, with results suggesting that geometric transfer is most effective when geometry-aware tokens have direct access to the action generation pathway. Our project page is at this https URL

---

## 5. DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs

**Authors:** Haidong Hou, Zhangguo Yu, Hengbo Qi, Jianlin Zhang
**arXiv:** [2606.24089](https://arxiv.org/abs/2606.24089)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Recent advances in control have enabled bipedal-wheeled robots to traverse slopes and single-step obstacles, yet long staircase traversal remains challenging as current teacher-student frameworks suffer from weakened dynamics-aware representations and incomplete terrain geometry encoding. To bridge this gap, we propose DynaWM, a dynamics-aware representation learning framework. To enhance terrain encoding capability and enable transparent assessment, we introduce a world model as a regularizer to enforce forward-dynamics awareness, preserving comprehensive terrain geometry while facilitating hierarchical encoding visualization. To stabilize knowledge transfer, we employ a momentum target encoder to provide consistent distillation targets, preventing dimensional collapse from non-stationary teacher updates. Evaluation of the learned representations through Principal Component Analysis (PCA) visualization and quantitative metrics reveals that our encoder hierarchically captures terrain geometry with higher terrain encoding capability, leading to enhanced terrain adaptability and motion smoothness. Experimental results in simulation and real hardware demonstrate that our method achieves superior terrain adaptability and motion smoothness, enabling bipedal-wheeled robots to overcome diverse continuous stairs, as shown in Fig. 1.

---

## 6. Beyond the Autoregressive Horizon: A Comprehensive Survey of Diffusion Models, World Modelling, and State Space Models for Code

**Authors:** Kishan Maharaj, Ashita Saxena, Srikanth Tamilselvam
**arXiv:** [2606.23690](https://arxiv.org/abs/2606.23690)
**Categories:** Software Engineering (cs.SE); Artificial Intelligence (cs.AI)

Autoregressive (AR) language models have driven significant progress in automated software engineering, enabling powerful code generation and assistance systems. However, the next-token prediction paradigm introduces structural limitations for code reasoning, including restricted global planning, challenges in maintaining long-range dependencies, and limited grounding in program execution semantics. Noting the heavy skewness of existing literature towards AR models, we discuss emerging paradigms that could potentially overcome the logic and scaling bottlenecks of next-token prediction by unlocking next-generation architectural capabilities for code intelligence. Specifically, we discuss the potential of Diffusion Models, which generate code via holistic denoising that captures long-range syntactic constraints often missed by AR models. We also discuss Code World Models (CWMs), which simulate execution states to support reasoning, and State Space Models (SSMs), which provide linear-time efficiency for massive contexts. By connecting these developments with findings from cognitive neuroscience, we outline directions for developing "System 2" code generation agents.

---

## 7. Autonomous Video Generation with Counterfactual Controllability for Self-Evolving World Models

**Authors:** Xin Wang, Wenxuan Liu, Tongtong Feng, Wenwu Zhu
**arXiv:** [2606.24152](https://arxiv.org/abs/2606.24152)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Existing literature claims that video generation essentially is world modelling. On the one hand, the claim is productive because it pushes generative AI beyond static images and toward temporally extended physical scenes. On the other hand, this claim dangerously relies on the belief that scaling visual prediction alone will automatically yield physical agents. We prefer a more accurate statement: video generation models learn a partial, implicit spatiotemporal world model, but not a fully grounded or controllable one. The reason is as follows: a model may generate a plausible video of a drone crossing a forest or a robot arm manipulating a cup, yet still fail to know which variables are controllable, which constraints belong to a particular body and which futures remain valid under intervention. The frontier in essence is not predictive realism alone, instead it emphasizes a self-evolving generative nature that requires the decisive criterion to be counterfactual controllability: the capability of asking what would happen under an action, to test whether the generated future can survive embodiment constraints and to feed the resulting action knowledge back into future imagination (generation). Therefore, in this paper we present a new perspective, i.e., autonomous video generation with counterfactual controllability is one promising way to realize self-evolving world models.

---

## 8. Supervise What Survives: Geometry-Guided VLA Adaptation from Synthetic Robot Videos

**Authors:** Danze Chen, Yanzhe Chen, Qiming Huang, ..., Chen Gao, Mike Zheng Shou
**arXiv:** [2606.24448](https://arxiv.org/abs/2606.24448)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models require large-scale video-action pairs, yet real teleoperation remains scarce. While generated robot videos offer a scalable alternative, existing methods treat them as real robot data by recovering pseudo-actions from synthesized pixels. We argue that deriving low-level control from generated visuals is a mismatched abstraction. A video captures only \emph{geometry}: the spatial trajectory representing the \emph{where} of a task. A real demonstration captures \emph{control}: the exact motor commands representing the \emph{how}. Human-to-robot video generation preserves these unequally: the visible geometry survives the generation process, while the underlying control signals are lost. This \textbf{Asymmetric Preservation Principle} dictates a clean rule: this surviving geometry should solely supervise visual perception, leaving control to real demonstrations. Following this principle, we propose \textbf{GRA} (\textbf{G}eometry-guided \textbf{R}epresentation \textbf{A}lignment), which extracts the geometric content as future 2D end-effector waypoints, computed from the source human video through pose estimation, retargeting, simulation, and calibrated projection, and routes them to the VLA vision backbone via an auxiliary 2D head. The action head is trained on real demonstrations only. During fine-tuning, the waypoint loss persists as a \textbf{spatial representation anchor} that prevents the backbone from losing its geometric grounding. On real-robot tasks, GRA outperforms pseudo-action baselines under matched data budgets and narrows the gap to policies trained with substantially more real demonstrations, suggesting that correctly routed geometry bridges generated videos to robot policies more reliably than recovered actions.

---

## 9. NavWM: A Unified Navigation World Model for Foresight-Driven Planning

**Authors:** Yanghong Mei, Longteng Guo, Ming-Ming Yu, ..., Xingjian He, Jing Liu
**arXiv:** [2606.24101](https://arxiv.org/abs/2606.24101)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Conventional visual navigation policies often struggle with myopic decision-making and mode collapse in complex environments. While world models offer a promising alternative, existing paradigms typically isolate perception, generation, and control, failing to capture their shared spatio-temporal dynamics. In this paper, we propose NavWM, a unified navigation world model that seamlessly integrates latent world reasoning, multimodal action prediction, and controllable visual generation. At its core, NavWM leverages latent world tokens to distill geometric and semantic priors, endowing the agent with robust structural understanding. To overcome the limitations of deterministic policies, we introduce an anchor-based multimodal trajectory forecasting framework that generates a diverse action space. This inherent diversity explicitly empowers the generative world model to act as a robust closed-loop planner, utilizing visual foresight to evaluate and select the optimal path. Extensive experiments across diverse robotics datasets demonstrate that NavWM significantly advances the state-of-the-art, delivering remarkable improvements in both high-fidelity future state generation and zero-shot navigation success.

---

## 10. Trimming the Long-Tail of Visual World Modeling Evaluation

**Authors:** Bingxuan Li, Yining Hong, Cheng Qian, ..., Yunzhu Li, Heng Ji
**arXiv:** [2606.24256](https://arxiv.org/abs/2606.24256)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Physical interactions follow a long-tailed distribution: a set of common and regular interactions dominates human experience and visual data, while a broad spectrum of rare and irregular interactions remains underrepresented. Although recent visual world models, including image and video generation models, achieve impressive realism on existing benchmarks, they primarily focus on simulating common physical interactions. This raises a central question: Do current visual world models internalize and generalize physical principles? In this work, we introduce Tailor-Bench, a benchmark that challenges world models to simulate irregular physical interactions. To enable systematic evaluation, we design three scenario modes that progressively challenge model reasoning: Regular scenarios reflect common tool-task pairs, Unconventional scenarios replace conventional tools with attribute-compatible substitutes to test affordance generalization, and Impossible scenarios introduce attribute-violating tools to probe constraint awareness. Additionally, we design two complementary settings under a unified evaluation protocol: predictive generation requires inferring outcomes without guidance, while descriptive generation specifies the target outcome for faithful realization. Our experimental results reveal a clear long-tail gap in physical world modeling: performance degrades from Regular to Unconventional and Impossible scenarios, indicating limited generalization beyond common interactions. Failure analysis further shows that models rely on superficial visual patterns: image models fail to realize correct state changes, while video models further suffer from temporal inconsistencies.

---

## 11. DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model

**Authors:** Jingke Wang, Zhenru Zhao, Shuangming Lei, ..., Yukai Ma, Yong Liu
**arXiv:** [2606.24051](https://arxiv.org/abs/2606.24051)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action driving models convert a pretrained Vision-Language Model into a driving policy, allowing them to use world knowledge and follow language guidances. However, existing VLA driving models still lack driving-oriented spatial intelligence: their policies are mainly grounded on perspective image tokens and language priors, while precise motion planning requires metric geometry, top-down scene structure, and attention to safety-critical perceptual cues. This limitation makes current models vulnerable to weak visual geometry modeling and perceptual coverage in expert demonstrations. In this paper, we present DriveStack-VLA, a framework built upon a large VLM backbone. To strengthen the spatial grounding of VLA driving, we develop dual visual modeling components. We inject a Bird-Eye-View representation into the Large Language Model decoder through a DeepStack-style connection, and propose Render-Teacher Alignment to align the perceptual focus of real images with that of rasterized images. Furthermore, to bridge the gap in multimodal trajectory selection, we introduce a head-based self-critique module that ranks sampled trajectories and conditionally refines the best one. DriveStack-VLA achieves 91.6 PDMS on NAVSIMv1, 91.0 EPDMS on NAVSIMv2 (with the human penalty filter enabled), and a driving score of 79.49 with a success rate of 56.36\% on the closed-loop Bench2Drive. More visualizations are available on our project page: this https URL.

---

## 12. World Value Models for Robotic Manipulation

**Authors:** Zhihao Wang, Jianxiong Li, Yu Cui, ..., Junzhi Yu, Xiao Ma
**arXiv:** [2606.24742](https://arxiv.org/abs/2606.24742)
**Categories:** Robotics (cs.RO)

Generalist value models play a pivotal role in scaling robotic policy learning from large-scale, mixed-quality data. Mathematically, accurate value estimation demands deep temporal understanding, requiring models to both ground the current belief using historical context and plan over future outcomes. However, most existing robotic value models are built on Vision-Language Model (VLM) backbones that are pretrained primarily on static or temporally sparse visual observations, lacking the requisite temporal modeling capabilities for value estimation. Unlike VLMs, world models naturally excel at temporal modeling and future planning, making them ideal foundations for learning generalizable value functions. Driven by this insight, we marry world models with value estimation to construct a new generalist robotic value model, World Value Model (WVM), that offers accurate task progressions to assess data quality. On standard benchmarks, WVM delivers state-of-the-art (SOTA) Value-Order Correlation (VOC) results. Complementing standard evaluation suites that contains only expert data, we further introduce Suboptimal-Value-Bench, a multi-embodiment benchmark consisting of 800 suboptimal trajectories with high-fidelity, human-labeled frame annotations. Our evaluations show that WVM maintains its SOTA performance on Suboptimal-Value-Bench, establishing its robustness in handling both expert and suboptimal data. When deployed for policy learning, WVM improves manipulation performance across various policy extraction approaches in both simulated and real-world deployment, providing robust guidance for learning from mixed-quality data.

---
