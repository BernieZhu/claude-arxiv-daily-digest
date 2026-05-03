# arXiv Daily Digest — 2026-04-14

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 16

---

## 1. From Topology to Trajectory: LLM-Driven World Models For Supply Chain Resilience

**Authors:** Jia Luo
**arXiv:** [2604.11041](https://arxiv.org/abs/2604.11041)
**Categories:** Artificial Intelligence (cs.AI)

Semiconductor supply chains face unprecedented resilience challenges amidst global geopolitical turbulence. Conventional Large Language Model (LLM) planners, when confronting such non-stationary "Policy Black Swan" events, frequently suffer from Decision Paralysis or a severe Grounding Gap due to the absence of physical environmental modeling. This paper introduces ReflectiChain, a cognitive agentic framework tailored for resilient macroeconomic supply chain planning. The core innovation lies in the integration of Latent Trajectory Rehearsal powered by a generative world model, which couples reflection-in-action (System 2 deliberation) with delayed reflection-on-action. Furthermore, we leverage a Retrospective Agentic RL mechanism to enable autonomous policy evolution during the deployment phase (test-time). Evaluations conducted on our high-fidelity benchmark, Semi-Sim, demonstrate that under extreme scenarios such as export bans and material shortages, ReflectiChain achieves a 250% improvement in average step rewards over the strongest LLM baselines. It successfully restores the Operability Ratio (OR) from a deficient 13.3% to over 88.5% while ensuring robust gradient convergence. Ablation studies further underscore that the synergy between physical grounding constraints and double-loop learning is fundamental to bridging the gap between semantic reasoning and physical reality for long-horizon strategic planning.

---

## 2. Do LLMs Build Spatial World Models? Evidence from Grid-World Maze Tasks

**Authors:** Weijiang Li, Yilin Zhu, Rajarshi Das, Parijat Dube
**arXiv:** [2604.10690](https://arxiv.org/abs/2604.10690)
**Categories:** Artificial Intelligence (cs.AI)

Foundation models have shown remarkable performance across diverse tasks, yet their ability to construct internal spatial world models for reasoning and planning remains unclear. We systematically evaluate the spatial understanding of large language models through maze tasks, a controlled testing context requiring multi-step planning and spatial abstraction. Across comprehensive experiments with Gemini-2.5-Flash, GPT-5-mini, Claude-Haiku-4.5, and DeepSeek-Chat, we uncover significant discrepancies in spatial reasoning that challenge assumptions about LLM planning capabilities. Using chain-of-thought prompting, Gemini achieves 80-86% accuracy on smaller mazes (5x5 to 7x7 grids) with tokenized adjacency representations, but performance collapses to 16-34% with visual grid formats, which is a 2-5x difference, suggesting representation-dependent rather than format-invariant spatial reasoning. We further probe spatial understanding through sequential proximity questions and compositional distance comparisons. Despite achieving 96-99% semantic coverage in reasoning traces, models fail to leverage this understanding for consistent spatial computations, indicating that they treat each question independently rather than building cumulative spatial knowledge. Our findings based on the maze-solving tasks suggest that LLMs do not develop robust spatial world models, but rather exhibit representation-specific and prompting-dependent reasoning that succeeds only under narrow conditions. These results have critical implications for deploying foundation models in applications requiring spatial abstraction.

---

## 3. Zero-shot World Models Are Developmentally Efficient Learners

**Authors:** Khai Loong Aw, Klemen Kotar, Wanhee Lee, ..., Michael C. Frank, Daniel L.K. Yamins
**arXiv:** [2604.10333](https://arxiv.org/abs/2604.10333)
**Categories:** Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Young children demonstrate early abilities to understand their physical world, estimating depth, motion, object coherence, interactions, and many other aspects of physical scene understanding. Children are both data-efficient and flexible cognitive systems, creating competence despite extremely limited training data, while generalizing to myriad untrained tasks -- a major challenge even for today's best AI systems. Here we introduce a novel computational hypothesis for these abilities, the Zero-shot Visual World Model (ZWM). ZWM is based on three principles: a sparse temporally-factored predictor that decouples appearance from dynamics; zero-shot estimation through approximate causal inference; and composition of inferences to build more complex abilities. We show that ZWM can be learned from the first-person experience of a single child, rapidly generating competence across multiple physical understanding benchmarks. It also broadly recapitulates behavioral signatures of child development and builds brain-like internal representations. Our work presents a blueprint for efficient and flexible learning from human-scale data, advancing both a computational account for children's early physical understanding and a path toward data-efficient AI systems.

---

## 4. OOWM: Structuring Embodied Reasoning and Planning via Object-Oriented Programmatic World Modeling

**Authors:** Hongyu Chen, Liang Lin, Guangrun Wang
**arXiv:** [2604.09580](https://arxiv.org/abs/2604.09580)
**Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Standard Chain-of-Thought (CoT) prompting empowers Large Language Models (LLMs) with reasoning capabilities, yet its reliance on linear natural language is inherently insufficient for effective world modeling in embodied tasks. While text offers flexibility, it fails to explicitly represent the state-space, object hierarchies, and causal dependencies required for robust robotic planning. To address these limitations, we propose Object-Oriented World Modeling (OOWM), a novel framework that structures embodied reasoning through the lens of software engineering formalisms. We redefine the world model not as a latent vector space, but as an explicit symbolic tuple $W = \langle S, T \rangle$: a State Abstraction ($G_\text{state}$) instantiating the environmental state $S$, coupled with a Control Policy ($G_\text{control}$) representing the transition logic $T: S \times A \rightarrow S'$. OOWM leverages the Unified Modeling Language (UML) to materialize this definition: it employs Class Diagrams to ground visual perception into rigorous object hierarchies, and Activity Diagrams to operationalize planning into executable control flows. Furthermore, we introduce a three-stage training pipeline combining Supervised Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO). Crucially, this method utilizes outcome-based rewards from the final plan to implicitly optimize the underlying object-oriented reasoning structure, enabling effective learning even with sparse annotations. Extensive evaluations on the MRoom-30k benchmark demonstrate that OOWM significantly outperforms unstructured textual baselines in planning coherence, execution success, and structural fidelity, establishing a new paradigm for structured embodied reasoning.

---

## 5. StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems

**Authors:** Jinhui Ye, Ning Gao, Senqiao Yang, ..., Shu Liu, Jiaya Jia
**arXiv:** [2604.11757](https://arxiv.org/abs/2604.11757)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for building general-purpose robotic agents. However, the VLA landscape remains highly fragmented and complex: as existing approaches vary substantially in architectures, training data, embodiment configurations, and benchmark-specific engineering. In this work, we introduce StarVLA-$\alpha$, a simple yet strong baseline designed to study VLA design choices under controlled conditions. StarVLA-$\alpha$ deliberately minimizes architectural and pipeline complexity to reduce experimental confounders and enable systematic analysis. Specifically, we re-evaluate several key design axes, including action modeling strategies, robot-specific pretraining, and interface engineering. Across unified multi-benchmark training on LIBERO, SimplerEnv, RoboTwin, and RoboCasa, the same simple baseline remains highly competitive, indicating that a strong VLM backbone combined with minimal design is already sufficient to achieve strong performance without relying on additional architectural complexity or engineering tricks. Notably, our single generalist model outperforms $\pi_{0.5}$ by 20\% on the public real-world RoboChallenge benchmark. We expect StarVLA-$\alpha$ to serve as a solid starting point for future research in the VLA regime. Code will be released at this https URL.

---

## 6. Grounded World Model for Semantically Generalizable Planning

**Authors:** Quanyi Li, Lan Feng, Haonan Zhang, ..., Alexandre Alahi, Harold Soh
**arXiv:** [2604.11751](https://arxiv.org/abs/2604.11751)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

In Model Predictive Control (MPC), world models predict the future outcomes of various action proposals, which are then scored to guide the selection of the optimal action. For visuomotor MPC, the score function is a distance metric between a predicted image and a goal image, measured in the latent space of a pretrained vision encoder like DINO and JEPA. However, it is challenging to obtain the goal image in advance of the task execution, particularly in new environments. Additionally, conveying the goal through an image offers limited interactivity compared with natural language. In this work, we propose to learn a Grounded World Model (GWM) in a vision-language-aligned latent space. As a result, each proposed action is scored based on how close its future outcome is to the task instruction, reflected by the similarity of embeddings. This approach transforms the visuomotor MPC to a VLA that surpasses VLM-based VLAs in semantic generalization. On the proposed WISER benchmark, GWM-MPC achieves a 87% success rate on the test set comprising 288 tasks that feature unseen visual signals and referring expressions, yet remain solvable with motions demonstrated during training. In contrast, traditional VLAs achieve an average success rate of 22%, even though they overfit the training set with a 90% success rate.

---

## 7. 3D-Anchored Lookahead Planning for Persistent Robotic Scene Memory via World-Model-Based MCTS

**Authors:** Bronislav Sidik, Dror Mizrahi
**arXiv:** [2604.11302](https://arxiv.org/abs/2604.11302)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

We present 3D-Anchored Lookahead Planning (3D-ALP), a System 2 reasoning engine for robotic manipulation that combines Monte Carlo Tree Search (MCTS) with a 3D-consistent world model as the rollout oracle. Unlike reactive policies that evaluate actions from the current camera frame only, 3D-ALP maintains a persistent camera-to-world (c2w) anchor that survives occlusion, enabling accurate replanning to object positions that are no longer directly observable. On a 5-step sequential reach task requiring spatial memory (Experiment E3), 3D-ALP achieves 0.650 0.109 success rate on memory-required steps versus 0.006 0.008 for a greedy reactive baseline ({\Delta}=+0.645), while step 5 success reaches 0.822 against 0.000 for greedy. An ablation study (30 episodes, 3 seeds) isolates tree search spatial memory as the primary driver (+0.533, 82% of gain) with additional benefit from deeper lookahead (+0.111, 17%). We also identify and resolve four structural failure modes in applying UCT-MCTS (Upper Confidence Bounds applied to Trees [10]) to continuous robotic manipulation.

---

## 8. AIM: Intent-Aware Unified world action Modeling with Spatial Value Maps

**Authors:** Liaoyuan Fan, Zetian Xu, Chen Cao, ..., Mingqi Yuan, Jiayu Chen
**arXiv:** [2604.11135](https://arxiv.org/abs/2604.11135)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Pretrained video generation models provide strong priors for robot control, but existing unified world action models still struggle to decode reliable actions without substantial robot-specific training. We attribute this limitation to a structural mismatch: while video models capture how scenes evolve, action generation requires explicit reasoning about where to interact and the underlying manipulation intent. We introduce AIM, an intent-aware unified world action model that bridges this gap via an explicit spatial interface. Instead of decoding actions directly from future visual representations, AIM predicts an aligned spatial value map that encodes task-relevant interaction structure, enabling a control-oriented abstraction of future dynamics. Built on a pretrained video generation model, AIM jointly models future observations and value maps within a shared mixture-of-transformers architecture. It employs intent-causal attention to route future information to the action branch exclusively through the value representation. We further propose a self-distillation reinforcement learning stage that freezes the video and value branches and optimizes only the action head using dense rewards derived from projected value-map responses together with sparse task-level signals. To support training and evaluation, we construct a simulation dataset of 30K manipulation trajectories with synchronized multi-view observations, actions, and value-map annotations. Experiments on RoboTwin 2.0 benchmark show that AIM achieves a 94.0% average success rate, significantly outperforming prior unified world action baselines. Notably, the improvement is more pronounced in long-horizon and contact-sensitive manipulation tasks, demonstrating the effectiveness of explicit spatial-intent modeling as a bridge between visual world modeling and robot control.

---

## 9. FlowHijack: A Dynamics-Aware Backdoor Attack on Flow-Matching Vision-Language-Action Models

**Authors:** Xinyuan An, Tao Luo, Gengyun Peng, ..., Kui Ren, Dongxia Wang
**arXiv:** [2604.09651](https://arxiv.org/abs/2604.09651)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG); Robotics (cs.RO)

Vision-Language-Action (VLA) models are emerging as a cornerstone for robotics, with flow-matching policies like $\pi_0$ showing great promise in generating smooth, continuous actions. As these models advance, their unique action generation mechanism - the vector field dynamics - presents a critical yet unexplored security vulnerability, particularly backdoor vulnerabilities. Existing backdoor attacks designed for autoregressive discretization VLAs cannot be directly applied to this new continuous dynamics. We introduce FlowHijack, the first backdoor attack framework to systematically target the underlying vector-field dynamics of flow-matching VLAs. Our method combines a novel $\tau$-conditioned injection strategy, which manipulates the initial phase of the action generation, with a dynamics mimicry regularizer. Experiments demonstrate that FlowHijack achieves high attack success rates using stealthy, context-aware triggers where prior works failed. Crucially, it preserves benign task performance and, by enforcing kinematic similarity, generates malicious actions that are behaviorally indistinguishable from normal actions. Our findings reveal a significant vulnerability in continuous embodied models, highlighting the urgent need for defenses targeting the model's internal generative dynamics.

---

## 10. DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models

**Authors:** Siyuan Xu, Tianshi Wang, Fengling Li, Lei Zhu, Heng Tao Shen
**arXiv:** [2604.11572](https://arxiv.org/abs/2604.11572)
**Categories:** Robotics (cs.RO); Multimedia (cs.MM)

Vision-Language-Action models (VLAs) have demonstrated strong potential for embodied AI, yet their deployment on resource-limited robots remains challenging due to high memory and computational demands. While Post-Training Quantization (PTQ) provides an efficient solution, directly applying PTQ to VLAs often results in severe performance degradation during sequential control. We identify temporal error accumulation as a key factor, where quantization perturbations at the vision-language-to-action interface are progressively amplified, leading to kinematic drift in executed trajectories. To address this issue, we propose Drift-Aware Post-Training Quantization (DA-PTQ), which formulates quantization as a drift-aware optimization problem over sequential decision processes. DA-PTQ consists of two components: (1) Cross-Space Representation Compensation, which mitigates structured distortions between multimodal representations and action space to improve action consistency, and (2) Motion-Driven Mixed-Precision Allocation, which assigns bit-widths by minimizing trajectory-level motion errors. Extensive experiments show that DA-PTQ significantly reduces kinematic drift and achieves comparable performance to full-precision models under low-bit settings, enabling practical deployment of VLAs on resource-limited robotic platforms.

---

## 11. WM-DAgger: Enabling Efficient Data Aggregation for Imitation Learning with World Models

**Authors:** Anlan Yu, Zaishu Chen, Peili Song, ..., Yi Ding, Daqing Zhang
**arXiv:** [2604.11351](https://arxiv.org/abs/2604.11351)
**Categories:** Robotics (cs.RO)

Imitation learning is a powerful paradigm for training robotic policies, yet its performance is limited by compounding errors: minor policy inaccuracies could drive robots into unseen out-of-distribution (OOD) states in the training set, where the policy could generate even bigger errors, leading to eventual failures. While the Data Aggregation (DAgger) framework tries to address this issue, its reliance on continuous human involvement severely limits scalability. In this paper, we propose WM-DAgger, an efficient data aggregation framework that leverages World Models to synthesize OOD recovery data without requiring human involvement. Specifically, we focus on manipulation tasks with an eye-in-hand robotic arm and only few-shot demonstrations. To avoid synthesizing misleading data and overcome the hallucination issues inherent to World Models, our framework introduces two key mechanisms: (1) a Corrective Action Synthesis Module that generates task-oriented recovery actions to prevent misleading supervision, and (2) a Consistency-Guided Filtering Module that discards physically implausible trajectories by anchoring terminal synthesized frames to corresponding real frames in expert demonstrations. We extensively validate WM-DAgger on multiple real-world robotic tasks. Results that our method significantly improves success rates, achieving a 93.3\% success rate in soft bag pushing with only five demonstrations. The source code is publicly available at this https URL.

---

## 12. AnySlot: Goal-Conditioned Vision-Language-Action Policies for Zero-Shot Slot-Level Placement

**Authors:** Zhaofeng Hu, Sifan Zhou, Qinbo Zhang, ..., Qi Su, Ci-Jyun Liang
**arXiv:** [2604.10432](https://arxiv.org/abs/2604.10432)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) policies have emerged as a versatile paradigm for generalist robotic manipulation. However, precise object placement under compositional language instructions remains a major challenge for modern monolithic VLA policies. Slot-level tasks require both reliable slot grounding and sub-centimeter execution accuracy. To this end, we propose AnySlot, a framework that reduces compositional complexity by introducing an explicit spatial visual goal as an intermediate representation between language grounding and control. AnySlot turns language into an explicit visual goal by generating a scene marker, then executes this goal with a goal-conditioned VLA policy. This hierarchical design effectively decouples high-level slot selection from low-level execution, ensuring both semantic accuracy and spatial robustness. Furthermore, recognizing the lack of existing benchmarks for such precision-demanding tasks, we introduce SlotBench, a comprehensive simulation benchmark featuring nine task categories tailored to evaluate structured spatial reasoning in slot-level placement. Extensive experiments show that AnySlot significantly outperforms flat VLA baselines and previous modular grounding methods in zero-shot slot-level placement.

---

## 13. STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations

**Authors:** Yuhan Xie, Yuping Yan, Yunqi Zhao, Handing Wang, Yaochu Jin
**arXiv:** [2604.10055](https://arxiv.org/abs/2604.10055)
**Categories:** Robotics (cs.RO)

Despite their strong performance in embodied tasks, recent Vision-Language-Action (VLA) models remain highly fragile under multimodal perturbations, where visual corruption and linguistic noise jointly induce distribution shifts that degrade task-level execution. Existing robustness approaches typically rely on joint training with perturbed data, treating robustness as a static objective, which leads to conflicting optimization between robustness and task fidelity. In this work, we propose STRONG-VLA, a decoupled fine-tuning framework that explicitly separates robustness acquisition from task-aligned refinement. In Stage I, the model is exposed to a curriculum of multimodal perturbations with increasing difficulty, enabling progressive robustness learning under controlled distribution shifts. In Stage II, the model is re-aligned with clean task distributions to recover execution fidelity while preserving robustness. We further establish a comprehensive benchmark with 28 perturbation types spanning both textual and visual modalities, grounded in realistic sources of sensor noise, occlusion, and instruction corruption. Extensive experiments on the LIBERO benchmark show that STRONG-VLA consistently improves task success rates across multiple VLA architectures. On OpenVLA, our method achieves gains of up to 12.60% under seen perturbations and 7.77% under unseen perturbations. Notably, similar or larger improvements are observed on OpenVLA-OFT (+14.48% / +13.81%) and pi0 (+16.49% / +5.58%), demonstrating strong cross-architecture generalization. Real-world experiments on an AIRBOT robotic platform further validate its practical effectiveness. These results highlight the importance of decoupled optimization for multimodal robustness and establish STRONG-VLA as a simple yet principled framework for robust embodied control.

---

## 14. ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models

**Authors:** Nastaran Darabi, Amit Ranjan Trivedi
**arXiv:** [2604.09824](https://arxiv.org/abs/2604.09824)
**Categories:** Robotics (cs.RO); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Vision language action (VLA) models enable generalist robotic agents but often exhibit language ignorance, relying on visual shortcuts and remaining insensitive to instruction changes. We present Prospective Grounding and Alignment VLA (ProGAL-VLA), which constructs a 3D entity-centric graph (GSM), uses a slow planner to produce symbolic sub-goals, and aligns them with grounded entities via a Grounding Alignment Contrastive (GAC) loss. All actions are conditioned on a verified goal embedding $g_t$, whose attention entropy provides an intrinsic ambiguity signal. On LIBERO-Plus, ProGAL-VLA increases robustness under robot perturbations from 30.3 to 71.5 percent, reduces language ignorance by 3x-4x, and improves entity retrieval from 0.41 to 0.71 Recall@1. On the Custom Ambiguity Benchmark, it reaches AUROC 0.81 (vs. 0.52), AUPR 0.79, and raises clarification on ambiguous inputs from 0.09 to 0.81 without harming unambiguous success. The verification bottleneck increases mutual information of language-actions, the GAC loss imposes an entity-level InfoNCE bound, and attention entropy yields calibrated selective prediction, indicating that explicit verified grounding is an effective path toward instruction-sensitive, ambiguity-aware agents.

---

## 15. ComSim: Building Scalable Real-World Robot Data Generation via Compositional Simulation

**Authors:** Yiran Qin, Jiahua Ma, Li Kang, ..., Yilun Du, Ruimao Zhang
**arXiv:** [2604.11386](https://arxiv.org/abs/2604.11386)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Recent advancements in foundational models, such as large language models and world models, have greatly enhanced the capabilities of robotics, enabling robots to autonomously perform complex tasks. However, acquiring large-scale, high-quality training data for robotics remains a challenge, as it often requires substantial manual effort and is limited in its coverage of diverse real-world environments. To address this, we propose a novel hybrid approach called Compositional Simulation, which combines classical simulation and neural simulation to generate accurate action-video pairs while maintaining real-world consistency. Our approach utilizes a closed-loop real-sim-real data augmentation pipeline, leveraging a small amount of real-world data to generate diverse, large-scale training datasets that cover a broader spectrum of real-world scenarios. We train a neural simulator to transform classical simulation videos into real-world representations, improving the accuracy of policy models trained in real-world environments. Through extensive experiments, we demonstrate that our method significantly reduces the sim2real domain gap, resulting in higher success rates in real-world policy model training. Our approach offers a scalable solution for generating robust training data and bridging the gap between simulated and real-world robotics.

---

## 16. LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment

**Authors:** Dujun Nie, Fengjiao Chen, Qi Lv, ..., Xuezhi Cao, Xunliang Cai
**arXiv:** [2604.11689](https://arxiv.org/abs/2604.11689)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

While the shortage of explicit action data limits Vision-Language-Action (VLA) models, human action videos offer a scalable yet unlabeled data source. A critical challenge in utilizing large-scale human video datasets lies in transforming visual signals into ontology-independent representations, known as latent actions. However, the capacity of latent action representation to derive robust control from visual observations has yet to be rigorously evaluated. We introduce the Latent Action Representation Yielding (LARY) Benchmark, a unified framework for evaluating latent action representations on both high-level semantic actions (what to do) and low-level robotic control (how to do). The comprehensively curated dataset encompasses over one million videos (1,000 hours) spanning 151 action categories, alongside 620K image pairs and 595K motion trajectories across diverse embodiments and environments. Our experiments reveal two crucial insights: (i) General visual foundation models, trained without any action supervision, consistently outperform specialized embodied latent action models. (ii) Latent-based visual space is fundamentally better aligned to physical action space than pixel-based space. These results suggest that general visual representations inherently encode action-relevant knowledge for physical control, and that semantic-level abstraction serves as a fundamentally more effective pathway from vision to action than pixel-level reconstruction.

---
