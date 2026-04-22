# arXiv Daily Digest — 2026-04-21

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 26

---

## 1. Can Explicit Physical Feasibility Benefit VLA Learning? An Empirical Study

**Authors:** Yubai Wei, Chen Wu, Hashem Haghbayan
**arXiv:** [2604.17896](https://arxiv.org/abs/2604.17896)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Vision-Language-Action (VLA) models map multimodal inputs directly to robot actions and are typically trained through large-scale imitation learning. While this paradigm has shown strong performance, prevailing VLA training procedures do not explicitly supervise hard physical constraints such as obstacle avoidance or kinematic feasibility. As a result, the geometric structure underlying physically feasible behavior must be inferred only implicitly from demonstrations. In this paper, we study whether introducing explicit feasibility supervision can provide effective structured guidance for VLA policies. We formulate a simple geometry-grounded feasibility objective and integrate it into the training stage of a diffusion-based VLA policy. To evaluate this idea systematically, we use obstacle-aware manipulation as a controlled probe of geometry-dependent physical feasibility. Empirical results show that augmenting VLA training with feasibility supervision improves both physical reliability and overall task performance, while also enhancing learning efficiency in the low-data regime. These findings indicate that explicit feasibility signals can effectively complement imitation-based VLA learning, highlighting their potential for developing more reliable VLA policies.

---

## 2. AnchorRefine: Synergy-Manipulation Based on Trajectory Anchor and Residual Refinement for Vision-Language-Action Models

**Authors:** Tingzheng Jia, Kan Guo, Lanping Qian, ..., Baocai Yin, Jiapu Wang
**arXiv:** [2604.17787](https://arxiv.org/abs/2604.17787)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Precision-critical manipulation requires both global trajectory organization and local execution correction, yet most vision-language-action (VLA) policies generate actions within a single unified space. This monolithic formulation forces macro-level transport and micro-level refinement to be optimized under the same objective, causing large motions to dominate learning while suppressing small but failure-critical corrective signals. In contrast, human manipulation is structured by global movement planning together with continuous local adjustment during execution. Motivated by this principle, we propose AnchorRefine, a hierarchical framework that factorizes VLA action modeling into trajectory anchor and residual refinement. The anchor planner predicts a coarse motion scaffold, while the refinement module corrects execution-level deviations to improve geometric and contact precision. We further introduce a decision-aware gripper refinement mechanism to better capture the discrete and boundary-sensitive nature of gripper control. Experiments on LIBERO, CALVIN, and real-robot tasks demonstrate that AnchorRefine consistently improves both regression-based and diffusion-based VLA backbones, yielding gains of up to 7.8% in simulation success rate and 18% in real-world success rate.

---

## 3. SafeDream: Safety World Model for Proactive Early Jailbreak Detection

**Authors:** Bo Yan, Weikai Lin, Yada Zhu, Song Wang
**arXiv:** [2604.16824](https://arxiv.org/abs/2604.16824)
**Categories:** Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)

Multi-turn jailbreak attacks progressively erode LLM safety alignment across seemingly innocuous conversation turns, achieving success rates exceeding 90% against state-of-the-art models. Existing alignment-based and guardrail methods suffer from three key limitations: they require costly weight modification, evaluate each turn independently without modeling cumulative safety erosion, and detect attacks only after harmful content has been generated. To address these limitations, we first formulate the proactive early jailbreak detection problem with a new metric, detection lead, that measures how early an attack can be detected before the LLM complies. We then propose SAFEDREAM, a lightweight world-model-based framework that operates as an external module without modifying the LLM's weights. SAFEDREAM introduces three components: (1) a safety state world model that encodes LLM hidden states into a compact safety representation and predicts how it evolves across turns, (2) CUSUM detection that accumulates weak per-turn risk signals into reliable evidence, and (3) contrastive imagination that simultaneously rolls out attack and benign futures in latent space to issue early alarms before jailbreaks occur. On three multi-turn jailbreak benchmarks (XGuard-Train, SafeDialBench, SafeMTData) against 8 baselines, SAFEDREAM achieves the best detection timeliness across all benchmarks (1.06-1.20 turns before compliance) while maintaining competitive false positive rates and outperforming baselines in detection quality.

---

## 4. ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control

**Authors:** Lingling Chen, Zongyao Lyu, William J. Beksi
**arXiv:** [2604.16677](https://arxiv.org/abs/2604.16677)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences. However, VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated. To address this problem we introduce ReconVLA, a reliable conformal model that produces uncertainty-guided and failure-aware control signals. Concretely, our approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. Furthermore, we extend conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty. We evaluate ReconVLA in both simulation and real robot experiments across diverse manipulation tasks. Our results show that conformalized action predictions consistently improve failure anticipation, reduce catastrophic errors, and provide a calibrated measure of confidence without retraining or modifying the underlying VLA.

---

## 5. Human Cognition in Machines: A Unified Perspective of World Models

**Authors:** Timothy Rupprecht, Pu Zhao, Amir Taherin, ..., Edmund Yeh, Yanzhi Wang
**arXiv:** [2604.16592](https://arxiv.org/abs/2604.16592)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Emerging Technologies (cs.ET)

This comprehensive report distinguishes prior works by the cognitive functions they innovate. Many works claim an almost "human-like" cognitive capability in their world models. To evaluate these claims requires a proper grounding in first principles in Cognitive Architecture Theory (CAT). We present a conceptual unified framework for world models that fully incorporates all the cognitive functions associated with CAT (i.e. memory, perception, language, reasoning, imagining, motivation, and meta-cognition) and identify gaps in the research as a guide for future states of the art. In particular, we find that motivation (especially intrinsic motivation) and meta-cognition remain drastically under-researched, and we propose concrete directions informed by active inference and global workspace theory to address them. We further introduce Epistemic World Models, a new category encompassing agent frameworks for scientific discovery that operate over structured knowledge. Our taxonomy, applied across video, embodied, and epistemic world models, suggests research directions where prior taxonomies have not.

---

## 6. The Global Neural World Model: Spatially Grounded Discrete Topologies for Action-Conditioned Planning

**Authors:** Noureddine Kermiche
**arXiv:** [2604.16585](https://arxiv.org/abs/2604.16585)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

We present the Global Neural World Model (GNWM), a self-stabilizing framework that achieves topological quantization through balanced continuous entropy constraints. Operating as a continuous, action-conditioned Joint-Embedding Predictive Architecture (JEPA), the GNWM maps environments onto a discrete 2D grid, enforcing translational equivariance without pixel-level reconstruction. Our results show this architecture prevents manifold drift during autoregressive rollouts by using grid ``snapping'' as a native error-correction mechanism. Furthermore, by training via maximum entropy exploration (random walks), the model learns generalized transition dynamics rather than memorizing specific expert trajectories. We validate the GNWM across passive observation, active agent control, and abstract sequence regimes, demonstrating its capacity to act not just as a spatial physics simulator, but as a causal discovery model capable of organizing continuous, predictable concepts into structured topological maps.

---

## 7. HQA-VLAttack: Towards High Quality Adversarial Attack on Vision-Language Pre-Trained Models

**Authors:** Han Liu, Jiaqi Li, Zhi Xu, ..., Yuanman Li, Hong Yu
**arXiv:** [2604.16499](https://arxiv.org/abs/2604.16499)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Black-box adversarial attack on vision-language pre-trained models is a practical and challenging task, as text and image perturbations need to be considered simultaneously, and only the predicted results are accessible. Research on this problem is in its infancy, and only a handful of methods are available. Nevertheless, existing methods either rely on a complex iterative cross-search strategy, which inevitably consumes numerous queries, or only consider reducing the similarity of positive image-text pairs but ignore that of negative ones, which will also be implicitly diminished, thus inevitably affecting the attack performance. To alleviate the above issues, we propose a simple yet effective framework to generate high-quality adversarial examples on vision-language pre-trained models, named HQA-VLAttack, which consists of text and image attack stages. For text perturbation generation, it leverages the counter-fitting word vector to generate the substitute word set, thus guaranteeing the semantic consistency between the substitute word and the original word. For image perturbation generation, it first initializes the image adversarial example via the layer-importance guided strategy, and then utilizes contrastive learning to optimize the image adversarial perturbation, which ensures that the similarity of positive image-text pairs is decreased while that of negative image-text pairs is increased. In this way, the optimized adversarial images and texts are more likely to retrieve negative examples, thereby enhancing the attack success rate. Experimental results on three benchmark datasets demonstrate that HQA-VLAttack significantly outperforms strong baselines in terms of attack success rate.

---

## 8. DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks

**Authors:** Yueci Deng, Guiliang Liu, Kui Jia
**arXiv:** [2604.16484](https://arxiv.org/abs/2604.16484)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Deploying generative World-Action Models for manipulation is severely bottlenecked by redundant pixel-level reconstruction, $\mathcal{O}(T)$ memory scaling, and sequential inference latency. We introduce the Causal Latent World Model (CLWM), which employs DINOv3 features as generative targets to disentangle interaction semantics from visual noise, yielding highly robust domain generalization. To overcome memory scaling, CLWM features a Dual-State Test-Time Training (TTT) Memory that guarantees a strict $\mathcal{O}(1)$ footprint for long-horizon tasks. To overcome deployment latency, we propose Speculative Asynchronous Inference (SAI) to mask partial diffusion denoising behind physical execution, cutting blocking latency by about $50\%$. To scale robust policies, we present EmbodiChain, an online framework that establishes the Efficiency Law by injecting an infinite flow of physics-grounded trajectories during training. Extensive experiments validate that CLWM achieves state-of-the-art performance in complex dual-arm simulation and unprecedented zero-shot sim-to-real transfer on physical robots, outperforming baselines explicitly finetuned on real-world data.

---

## 9. ICAT: Incident-Case-Grounded Adaptive Testing for Physical-Risk Prediction in Embodied World Models

**Authors:** Zhenglin Lai, Sirui Huang, Yuteng Li, ..., Jianqiang Li, Bingzhe Wu
**arXiv:** [2604.16405](https://arxiv.org/abs/2604.16405)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Video-generative world models are increasingly used as neural simulators for embodied planning and policy learning, yet their ability to predict physical risk and severe consequences is rarely this http URL find that these models often downplay or omit key danger cues and severe outcomes for hazardous actions, which can induce unsafe preferences during planning and training on imagined rollouts. We propose ICAT, which grounds testing in real incident reports and safety manuals by building structured risk memories and retrieving/composing them to constrain the generation of risk cases with causal chains and severity labels. Experiments on an ICAT-based benchmark show that mainstream world models frequently miss mechanisms and triggering conditions and miscalibrate severity, falling short of the reliability required for safety-critical embodied deployment.

---

## 10. Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity

**Authors:** Blaise Delaney, Salil Patel, Yuji Xing, Dominic Dootson, Karin Sevegnani
**arXiv:** [2604.18058](https://arxiv.org/abs/2604.18058)
**Categories:** Machine Learning (cs.LG)

We introduce Sonata, a compact latent world model for six-axis trunk IMU representation learning under clinical data scarcity. Clinical cohorts typically comprise tens to hundreds of patients, making web-scale masked-reconstruction objectives poorly matched to the problem. Sonata is a 3.77 M-parameter hybrid model, pre-trained on a harmonised corpus of nine public datasets (739 subjects, 190k windows) with a latent world-model objective that predicts future state rather than reconstructing raw sensor traces. In a controlled comparison against a matched autoregressive forecasting baseline (MAE) on the same backbone, Sonata yields consistently stronger frozen-probe clinical discrimination, prospective fall-risk prediction, and cross-cohort transfer across a 14-arm evaluation suite, while producing higher-rank, more structured latent representations. At 3.77 M parameters the model is compatible with on-device wearable inference, offering a step toward general kinematic world models for neurological assessment.

---

## 11. Unmasking the Illusion of Embodied Reasoning in Vision-Language-Action Models

**Authors:** Haiweng Xu, Sipeng Zheng, Hao Luo, ..., Ziheng Xi, Zongqing Lu
**arXiv:** [2604.18000](https://arxiv.org/abs/2604.18000)
**Categories:** Robotics (cs.RO)

Recent Vision-Language-Action (VLA) models report impressive success rates on standard robotic benchmarks, fueling optimism about general-purpose physical intelligence. However, recent evidence suggests a systematic misalignment between standard benchmark success and true embodied reasoning, raising the question of whether these high scores reflect genuine cognitive capability. To address this gap, we introduce BeTTER, a diagnostic Benchmark for Testing True Embodied Reasoning in robotic policies. BeTTER applies targeted causal interventions (e.g., spatial layout shifts, temporal extrapolation) while enforcing kinematic isolation to explicitly decouple high-level reasoning failures from low-level execution limits. Through systematic evaluation, we reveal that state-of-the-art VLAs catastrophically fail in dynamic scenarios, exhibiting severe lexical-kinematic shortcuts, behavioral inertia, and semantic feature collapse. Crucially, our mechanistic analysis traces these symptoms to fundamental architectural bottlenecks - such as capacity compression and myopic downsampling - which systematically degrade the model's foundational semantic representation. We demonstrate that highly static evaluation protocols effectively mask this degradation by allowing optimization to overfit to sensorimotor priors. Supported by real-world robotic validation, our findings confirm that this representational breakdown is not a simulation artifact, highlighting the critical need for future VLA paradigms to resolve the structural tension between high-frequency control and high-level reasoning.

---

## 12. ST-$π$: Structured SpatioTemporal VLA for Robotic Manipulation

**Authors:** Chuanhao Ma, Hanyu Zhou, Shihan Peng, ..., Tao Gu, Luxin Yan
**arXiv:** [2604.17880](https://arxiv.org/abs/2604.17880)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action (VLA) models have achieved great success on general robotic tasks, but still face challenges in fine-grained spatiotemporal manipulation. Typically, existing methods mainly embed spatiotemporal knowledge into visual and action representations, and directly perform a cross-modal mapping for step-level action prediction. However, such spatiotemporal reasoning remains largely implicit, making it difficult to handle multiple sequential behaviors with explicit spatiotemporal boundaries. In this work, we propose ST-$\pi$, a structured spatiotemporal VLA model for robotic manipulation. Our model is guided by two key designs: 1) Spatiotemporal VLM. We encode 4D observations and task instructions into latent spaces, and feed them into the LLM to generate a sequence of causally ordered chunk-level action prompts consisting of sub-tasks, spatial grounding and temporal grounding. 2) Spatiotemporal action expert. Conditioned on chunk-level action prompts, we design a structured dual-generator guidance to jointly model spatial dependencies and temporal causality, thus predicting step-level action parameters. Within this structured framework, the VLM explicitly plans global spatiotemporal behavior, and the action expert further refines local spatiotemporal control. In addition, we propose a real-world robotic dataset with structured spatiotemporal annotations for fine-tuning. Extensive experiments have been conducted to demonstrate the effectiveness of our model. Our code link: this https URL.

---

## 13. ReFineVLA: Multimodal Reasoning-Aware Generalist Robotic Policies via Teacher-Guided Fine-Tuning

**Authors:** Tuan Van Vo, Tan Q. Nguyen, Khang Nguyen, ..., Ngo Anh Vien, Minh Nhat Vu
**arXiv:** [2604.17800](https://arxiv.org/abs/2604.17800)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have gained much attention from the research community thanks to their strength in translating multimodal observations with linguistic instructions into desired robotic actions. Despite their advancements, VLAs often overlook explicit reasoning and learn the functional input-action mappings, omitting crucial logical steps, which are especially pronounced in interpretability and generalization for complex, long-horizon manipulation tasks. In this work, we propose ReFineVLA, a multimodal reasoning-aware framework that fine-tunes VLAs with teacher-guided reasons. We first augment robotic datasets with reasoning rationales generated by an expert teacher model, guiding VLA models to learn to reason about their actions. Then, we fine-tune pre-trained VLAs with the reasoning-enriched datasets with ReFineVLA, while maintaining the underlying generalization abilities and boosting reasoning capabilities. We also conduct attention map visualization to analyze the alignment among visual observation, linguistic prompts, and to-be-executed actions of ReFineVLA, reflecting the model is ability to focus on relevant tasks and actions. Through this additional step, we explore that ReFineVLA-trained models exhibit a meaningful agreement between vision-language and action domains, highlighting the enhanced multimodal understanding and generalization. Evaluated across a suite of simulated manipulation benchmarks on SimplerEnv with both WidowX and Google Robot tasks, ReFineVLA achieves state-of-the-art performance, in success rate over the second-best method on the both the WidowX benchmark and Google Robot Tasks.

---

## 14. OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL

**Authors:** Haoxiang Jie, Yaoyuan Yan, Xiangyu Wei, ..., Zhiyou Heng, Daocheng Chen
**arXiv:** [2604.17706](https://arxiv.org/abs/2604.17706)
**Categories:** Robotics (cs.RO)

Visual-Language-Action (VLA) models represent a paradigm shift in embodied AI, yet existing frameworks often struggle with imprecise spatial perception, suboptimal multimodal fusion, and instability in reinforcement learning. To bridge these gaps, we propose OmniVLA-RL, a novel architecture that leverages a Mix-of-Transformers (MoT) design to synergistically integrate reasoning, spatial, and action experts. Furthermore, we introduce Flow-GSPO, which reformulates flow matching as a Stochastic Differential Equation (SDE) process and integrates it with Group Segmented Policy Optimization (GSPO) to enhance action precision and training robustness. Extensive evaluations on the LIBERO and LIBERO-Plus benchmarks demonstrate that OmniVLA-RL significantly outperforms state-of-the-art methods, effectively overcoming the fundamental limitations of current VLA models.

---

## 15. Infrastructure-Centric World Models: Bridging Temporal Depth and Spatial Breadth for Roadside Perception

**Authors:** Siyuan Meng, Chengbo Ai
**arXiv:** [2604.17651](https://arxiv.org/abs/2604.17651)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

World models, generative AI systems that simulate how environments evolve, are transforming autonomous driving, yet all existing approaches adopt an ego-vehicle perspective, leaving the infrastructure viewpoint unexplored. We argue that infrastructure-centric world models offer a fundamentally complementary capability: the bird's-eye, multi-sensor, persistent viewpoint that roadside systems uniquely possess. Central to our thesis is a spatio-temporal complementarity: fixed roadside sensors excel at temporal depth, accumulating long-term behavioral distributions including rare safety-critical events, while vehicle-borne sensors excel at spatial breadth, sampling diverse scenes across large road networks. This paper presents a vision for Infrastructure-centric World Models (I-WM) in three phases: (I) generative scene understanding with quality-aware uncertainty propagation, (II) physics-informed predictive dynamics with multi-agent counterfactual reasoning, and (III) collaborative world models for V2X communication via latent space alignment. We propose a dual-layer architecture, annotation-free perception as a multi-modal data engine feeding end-to-end generative world models, with a phased sensor strategy from LiDAR through 4D radar and signal phase data to event cameras. We establish a taxonomy of driving world model paradigms, position I-WM relative to LeCun's JEPA, Li Fei-Fei's spatial intelligence, and VLA architectures, and introduce Infrastructure VLA (I-VLA) as a novel unification of roadside perception, language commands, and traffic control actions. Our vision builds upon existing multi-LiDAR pipelines and identifies open-source foundations for each phase, providing a path toward infrastructure that understands and anticipates traffic.

---

## 16. MultiWorld: Scalable Multi-Agent Multi-View Video World Models

**Authors:** Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu
**arXiv:** [2604.18564](https://arxiv.org/abs/2604.18564)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video world models have achieved remarkable success in simulating environmental dynamics in response to actions by users or agents. They are modeled as action-conditioned video generation models that take historical frames and current actions as input to predict future frames. Yet, most existing approaches are limited to single-agent scenarios and fail to capture the complex interactions inherent in real-world multi-agent systems. We present \textbf{MultiWorld}, a unified framework for multi-agent multi-view world modeling that enables accurate control of multiple agents while maintaining multi-view consistency. We introduce the Multi-Agent Condition Module to achieve precise multi-agent controllability, and the Global State Encoder to ensure coherent observations across different views. MultiWorld supports flexible scaling of agent and view counts, and synthesizes different views in parallel for high efficiency. Experiments on multi-player game environments and multi-robot manipulation tasks demonstrate that MultiWorld outperforms baselines in video fidelity, action-following ability, and multi-view consistency. Project page: this https URL

---

## 17. Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models

**Authors:** Zehua Zang, Xi Wang, Fuchun Sun, ..., Jiahuan Zhou, Jiangmeng Li
**arXiv:** [2604.18107](https://arxiv.org/abs/2604.18107)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose. We attribute this brittleness to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns. We propose Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model. PDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. To further improve stability, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue. Experiments on LIBERO (+7.4\% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation, establishing a practical path toward reliable test-time adaptation in multimodal decision-making agents. The code is available at \href{this https URL}{this https URL}.

---

## 18. OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models

**Authors:** Yiwei Zhang, Xuesong Chen, Jin Gao, ..., Shaoshuai Shi, Zhipeng Zhang
**arXiv:** [2604.17915](https://arxiv.org/abs/2604.17915)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language Models(VLMs) excel at autoregressive text generation, yet end-to-end autonomous driving requires multi-task learning with structured outputs and heterogeneous decoding behaviors, such as autoregressive language generation, parallel object detection and trajectory regression. To accommodate these differences, existing systems typically introduce separate or cascaded decoders, resulting in architectural fragmentation and limited backbone reuse. In this work, we present a unified autonomous driving framework built upon a pretrained VLM, where heterogeneous decoding behaviors are reconciled within a single transformer decoder. We demonstrate that pretrained VLM attention exhibits strong transferability beyond pure language modeling. By organizing visual and structured query tokens within a single causal decoder, structured queries can naturally condition on visual context through the original attention mechanism. Textual and structured outputs share a common attention backbone, enabling stable joint optimization across heterogeneous tasks. Trajectory planning is realized within the same causal LLM decoder by introducing structured trajectory queries. This unified formulation enables planning to share the pretrained attention backbone with images and perception tokens. Extensive experiments on end-to-end autonomous driving benchmarks demonstrate state-of-the-art performance, including 0.28 L2 and 0.18 collision rate on nuScenes open-loop evaluation and competitive results (86.8 PDMS) on NAVSIM closed-loop evaluation. The full model preserves multi-modal generation capability, while an efficient inference mode achieves approximately 40% lower latency. Code and models are available at this https URL

---

## 19. Active World-Model with 4D-informed Retrieval for Exploration and Awareness

**Authors:** Elaheh Vaezpour, Amirhosein Javadi, Tara Javidi
**arXiv:** [2604.16733](https://arxiv.org/abs/2604.16733)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Physical awareness, especially in a large and dynamic environment, is shaped by sensing decisions that determine observability across space, time, and scale, while observations impact the quality of sensing decisions. This loopy information structure makes physical awareness a fundamentally challenging decision problem with partial observations. While in the past decade we have witnessed the unprecedented success of reinforcement learning (RL) in problems with full observability, decision problems with partial observation, such as POMDPs, remain largely open: real-world explorations are excessively costly, while sim-to-real pipeline suffer from unobserved viewpoints. We introduce AW4RE (Active World-model with 4D-informed Retrieval for Exploration), an awareness-centric generative world model that provides a sensor-native surrogate environment for exploring sensing queries. Conditioned on a queried sensing action, AW4RE estimates the action-conditioned observation process. This is done by combining 4D-informed evidence retrieval, action-conditioned geometric support with temporal coherence, and conditional generative completion. Experiments demonstrate that AW4RE produces more grounded and consistent predictions than geometry-aware generative baselines under extreme viewpoint shifts, temporal gaps, and sparse geometric support.

---

## 20. Dual-Anchoring: Addressing State Drift in Vision-Language Navigation

**Authors:** Kangyi Wu, Pengna Li, Kailin Lyu, ..., Jinjun Wang, Jianyi Liu
**arXiv:** [2604.17473](https://arxiv.org/abs/2604.17473)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language Navigation(VLN) requires an agent to navigate through 3D environments by following natural language instructions. While recent Video Large Language Models(Video-LLMs) have largely advanced VLN, they remain highly susceptible to State Drift in long scenarios. In these cases, the agent's internal state drifts away from the true task execution state, leading to aimless wandering and failure to execute essential maneuvers in the instruction. We attribute this failure to two distinct cognitive deficits: Progress Drift, where the agent fails to distinguish completed sub-goals from remaining ones, and Memory Drift, where the agent's history representations degrade, making it lose track of visited landmarks. In this paper, we propose a Dual-Anchoring Framework that explicitly anchors the instruction progress and history representations. First, to address progress drift, we introduce Instruction Progress Anchoring, which supervises the agent to generate structured text tokens that delineate completed versus remaining sub-goals. Second, to mitigate memory drift, we propose Memory Landmark Anchoring, which utilizes a Landmark-Centric World Model to retrospectively predict object-centric embeddings extracted by the Segment Anything Model, compelling the agent to explicitly verify past observations and preserve distinct representations of visited landmarks. Facilitating this framework, we curate two extensive datasets: 3.6 million samples with explicit progress descriptions, and 937k grounded landmark data for retrospective verification. Extensive experiments in both simulation and real-world environments demonstrate the superiority of our method, achieving a 15.2% improvement in Success Rate and a remarkable 24.7% gain on long-horizon trajectories. To facilitate further research, we will release our code, data generation pipelines, and the collected datasets.

---

## 21. StableIDM: Stabilizing Inverse Dynamics Model against Manipulator Truncation via Spatio-Temporal Refinement

**Authors:** Kerui Li, Zhe Jing, Xiaofeng Wang, ..., Qingkai Yang, Huaibo Huang
**arXiv:** [2604.17887](https://arxiv.org/abs/2604.17887)
**Categories:** Robotics (cs.RO)

Inverse Dynamics Models (IDMs) map visual observations to low-level action commands, serving as central components for data labeling and policy execution in embodied AI. However, their performance degrades severely under manipulator truncation, a common failure mode that makes state recovery ill-posed and leads to unstable control. We present StableIDM, a spatio-temporal framework that refines features from visual inputs to stabilize action predictions under such partial observability. StableIDM integrates three complementary components: (1) auxiliary robot-centric masking to suppress background clutter, (2) Directional Feature Aggregation (DFA) for geometry-aware spatial reasoning, which extracts anisotropic features along directions inferred from the visible arm and (3) Temporal Dynamics Refinement (TDR) to smooth and correct predictions via motion continuity. Extensive evaluations validate our approach: StableIDM improves strict action accuracy by 12.1% under severe truncation on the AgiBot benchmark, and increases average task success by 9.7% in real-robot replay. Moreover, it boosts end-to-end grasp success by 11.5% when decoding video-generated plans, and improves downstream VLA real-robot success by 17.6% when functioning as an automatic annotator. These results demonstrate that StableIDM provides a robust and scalable backbone for both policy execution and data generation in embodied artificial intelligence.

---

## 22. OFlow: Injecting Object-Aware Temporal Flow Matching for Robust Robotic Manipulation

**Authors:** Kuanning Wang, Ke Fan, Chenhao Qiu, ..., Daniel Seita, Xiangyang Xue
**arXiv:** [2604.17876](https://arxiv.org/abs/2604.17876)
**Categories:** Robotics (cs.RO)

Robust robotic manipulation requires not only predicting how the scene evolves over time, but also recognizing task-relevant objects in complex scenes. However, existing VLA models face two limitations. They typically act only on the current frame, while future prediction and object-aware reasoning are often learned in separate latent spaces. We propose OFlow (injecting Object-Aware Temporal Flow Matching into VLAs), a framework that addresses both limitations by unifying temporal foresight and object-aware reasoning in a shared semantic latent space. Our method forecasts future latents with temporal flow matching, factorizes them into object-aware representations that emphasize physically relevant cues while filtering task-irrelevant variation, and conditions continuous action generation on these predictions. By integrating OFlow into VLA pipelines, our method enables more reliable control under distribution shifts. Extensive experiments across LIBERO, LIBERO-Plus, MetaWorld, and SimplerEnv benchmarks and real-world tasks demonstrate that object-aware foresight consistently enhances robustness and success.

---

## 23. Chain Of Interaction Benchmark (COIN): When Reasoning meets Embodied Interaction

**Authors:** Xianhao Wang, Xiaojian Ma, Haozhe Hu, ..., Bin Li, Qing Li
**arXiv:** [2604.16886](https://arxiv.org/abs/2604.16886)
**Categories:** Robotics (cs.RO)

Generalist embodied agents must perform interactive, causally-dependent reasoning, continually interacting with the environment, acquiring information, and updating plans to solve long-horizon tasks before they could be adopted in real-life scenarios. For instance, retrieving an apple from a cabinet may require opening multiple doors and drawers before the apple becomes visible and reachable, demanding sequential interaction under partial observability. However, existing benchmarks fail to systematically evaluate this essential capability. We introduce COIN, a benchmark designed to assess interactive reasoning in realistic robotic manipulation through three key contributions. First, we construct COIN-50: 50 interactive tasks in daily scenarios, and create COIN-Primitive required by causally-dependent tasks, and COIN-Composition with mid-term complexity for skill learning and generalization evaluation. Second, we develop a low-cost mobile AR teleoperation system and collect the COIN-Primitive Dataset with 50 demonstrations per primitive task (1,000 in total). Third, we develop systematic evaluation metrics about execution stability and generalization robustness to evaluate CodeAsPolicy, VLA, and language-conditioned H-VLA approaches. Our comprehensive evaluation reveals critical limitations in current methods: models struggle with interactive reasoning tasks due to significant gaps between visual understanding and motor execution. We provide fine-grained analysis of these limitations.

---

## 24. Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining

**Authors:** Wenyao Zhang, Bozhou Zhang, Zekun Qi, ..., Xin Jin, Li Zhang
**arXiv:** [2604.16391](https://arxiv.org/abs/2604.16391)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action (VLA) models have shown great potential in building generalist robots, but still face a dilemma-misalignment of 2D image forecasting and 3D action prediction. Besides, such a vision-action entangled training manner limits model learning from large-scale, action-free web video data. To address these issues, we propose DeFI, a novel framework that Decouples visual Forward and Inverse dynamics pretraining to exploit respective data sources, wherein video generation and action prediction are disentangled. We introduce the General Forward Dynamics Model (GFDM), pretrained on diverse human and robot videos for future prediction, and the General Inverse Dynamics Model (GIDM), trained via self-supervised learning to infer latent actions from unlabeled video transitions. These models are then integrated into a unified architecture for end-to-end finetuning on downstream tasks. In this manner, GFDM and GIDM first shine separately and then cooperate for mutual benefit. Extensive experiments on CALVIN ABC-D and SimplerEnv demonstrate state-of-the-art performance, with DeFI achieving an average task length of 4.51 for CALVIN, 51.2% success rate on SimplerEnv-Fractal benchmark and 81.3% success rate in real-world deployment, significantly outperforming prior methods.

---

## 25. OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation

**Authors:** Jinghui Lu, Jiayi Guan, Zhijian Huang, ..., Hangjun Ye, Long Chen
**arXiv:** [2604.18486](https://arxiv.org/abs/2604.18486)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Computation and Language (cs.CL); Robotics (cs.RO)

Chain-of-Thought (CoT) reasoning has become a powerful driver of trajectory prediction in VLA-based autonomous driving, yet its autoregressive nature imposes a latency cost that is prohibitive for real-time deployment. Latent CoT methods attempt to close this gap by compressing reasoning into continuous hidden states, but consistently fall short of their explicit counterparts. We suggest that this is due to purely linguistic latent representations compressing a symbolic abstraction of the world, rather than the causal dynamics that actually govern driving. Thus, we present OneVL (One-step latent reasoning and planning with Vision-Language explanations), a unified VLA and World Model framework that routes reasoning through compact latent tokens supervised by dual auxiliary decoders. Alongside a language decoder that reconstructs text CoT, we introduce a visual world model decoder that predicts future-frame tokens, forcing the latent space to internalize the causal dynamics of road geometry, agent motion, and environmental change. A three-stage training pipeline progressively aligns these latents with trajectory, language, and visual objectives, ensuring stable joint optimization. At inference, the auxiliary decoders are discarded and all latent tokens are prefilled in a single parallel pass, matching the speed of answer-only prediction. Across four benchmarks, OneVL becomes the first latent CoT method to surpass explicit CoT, delivering state-of-the-art accuracy at answer-only latency, and providing direct evidence that tighter compression, when guided in both language and world-model supervision, produces more generalizable representations than verbose token-by-token reasoning. Project Page: this https URL

---

## 26. XEmbodied: A Foundation Model with Enhanced Geometric and Physical Cues for Large-Scale Embodied Environments

**Authors:** Kangan Qian, ChuChu Xie, Yang Zhong, ..., Long Chen, Diange Yang
**arXiv:** [2604.18484](https://arxiv.org/abs/2604.18484)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Multimedia (cs.MM); Robotics (cs.RO)

Vision-Language-Action (VLA) models drive next-generation autonomous systems, but training them requires scalable, high-quality annotations from complex environments. Current cloud pipelines rely on generic vision-language models (VLMs) that lack geometric reasoning and domain semantics due to their 2D image-text pretraining. To address this mismatch, we propose XEmbodied, a cloud-side foundation model that endows VLMs with intrinsic 3D geometric awareness and interaction with physical cues (e.g., occupancy grids, 3D boxes). Instead of treating geometry as auxiliary input, XEmbodied integrates geometric representations via a structured 3D Adapter and distills physical signals into context tokens using an Efficient Image-Embodied Adapter. Through progressive domain curriculum and reinforcement learning post-training, XEmbodied preserves general capabilities while demonstrating robust performance across 18 public benchmarks. It significantly improves spatial reasoning, traffic semantics, embodied affordance, and out-of-distribution generalization for large-scale scenario mining and embodied VQA.

---
