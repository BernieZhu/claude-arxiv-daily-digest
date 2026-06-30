# arXiv Daily Digest — 2026-06-29

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 18

---

## 1. Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents

**Authors:** Xinyuan Song, Zekun Cai
**arXiv:** [2606.27806](https://arxiv.org/abs/2606.27806)
**Categories:** Artificial Intelligence (cs.AI)

World models for language agents come in two useful forms. An agent-based world model calls an LLM API and reasons flexibly in language, but its errors appear as hallucinated state changes that are hard to score with ordinary regression losses. A parameterized world model is a trained transition predictor; its errors are easier to measure with quantities such as NodeMSE, delta accuracy, and validity accuracy, but it is usually weaker as a standalone planner. We compare these two families on four graph-structured planning benchmarks and introduce operational hallucination metrics for the agent-based case. The comparison motivates \textbf{Grounded Iterative Language Planning} (GILP), which trains only a small parameterized backbone and combines it with API-based agent reasoning. The backbone supplies valid actions, predicted state deltas, risk, and value; the LLM drafts an action and imagined delta; and a consistency gate asks for revision when the two disagree. On real GPT-4o-mini calls, GILP reduces hallucinated-state rate from 0.176 to 0.035. In calibrated simulator ablations, it raises success from 0.668 to 0.838 while adding only ~22% extra LLM calls.

---

## 2. Understanding Rollout Error in Graph World Models

**Authors:** Xinyuan Song, Zekun Cai
**arXiv:** [2606.27780](https://arxiv.org/abs/2606.27780)
**Categories:** Artificial Intelligence (cs.AI)

World models are often used for planning by rolling learned dynamics forward. Many planning environments, however, are not vectors or images; they are graphs of agents, tools, skills, routes, and dependencies. In these settings, a local prediction error may stay local or spread through the graph, and the failure mode changes again when edges are predicted rather than fixed. This paper studies long-horizon rollout error in Graph World Models (GWMs). We formulate a unified fixed-edge and dynamic-edge GWM framework with action nodes for node-, edge-, and graph-level decisions. We develop graph-valued rollout bounds that separate topology-induced amplification from model-induced amplification, and we introduce a joint node-edge operator for dynamic-edge rollouts. Guided by the analysis, we propose Error-Aware GWM, which combines spectral regularization, rollout consistency, and critical-node weighting. Across synthetic topologies and heterogeneous agent-graph testbeds, rollout error and planning regret grow with horizon, dynamic-edge training is needed when structure evolves, and Error-Aware GWM prevents long-horizon divergence while preserving prediction accuracy. Real-world graph benchmarks clarify the scope of GWMs: they are most useful for dynamic graph rollout and agent planning, while specialized graph models remain strong on static or sparse prediction tasks.

---

## 3. Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning

**Authors:** Xuan Zhang, Zhijian Zhou, Lingfeng Qiao, ..., Chao Qu, Yuan Qi
**arXiv:** [2606.27483](https://arxiv.org/abs/2606.27483)
**Categories:** Artificial Intelligence (cs.AI)

Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. Crucially, we identify a format-capability gap: simply fine-tuning agents on look-ahead traces during post-training leads to superficial mimicry of foresight without genuine predictive grounding. To bridge this gap, we introduce a three-stage training paradigm: (i) World Model Agentic Mid-Training (WM-AMT) to inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this injected capability; and (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine the calibration and utility of the generated simulations. Evaluated on search and mathematical reasoning tasks, our approach consistently outperforms other training baselines. Our results demonstrate that effective internal world modeling in LLM agents requires a capability-first training pipeline to achieve grounded and calibrated foresight.

---

## 4. From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond

**Authors:** Paul Dubois
**arXiv:** [2606.28127](https://arxiv.org/abs/2606.28127)
**Categories:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

The AI community has framed the relationship between large language models (LLMs) and world models as a dichotomy: LLMs predict tokens; world models simulate reality. Yann LeCun argues in 2022 that reaching general intelligence requires abandoning autoregressive token prediction in favour of latent-space architectures. This framing is unnecessarily binary. Two claims will be defended. First, LLMs are a degenerate special case of world models: the state space is the set of all token sequences, the only action is appending one token, and world models are therefore a strict generalisation of LLMs, not a replacement. Second, there is a natural continuous spectrum from NTP to JEPA, with multi-token prediction, future-summary prediction, and next-latent prediction as intermediate stations already populated by current research. Moving along this spectrum relaxes the LLM constraints one by one. It also progressively surrenders the two practical advantages that make LLMs trainable at scale: internet-scale self-supervised data, and a transformer architecture co-designed for discrete token prediction. Both are examined as open research questions: the data question (the cliff from self-supervised text to instrumented action-labelled environments) and the architecture question (whether the transformer generalises to continuous-state prediction, or whether a new primitive is needed).

---

## 5. S$^2$-VLA: State-Space Guided Vision-Language-Action Models for Long-Horizon Manipulation

**Authors:** Zhipeng Xie, Zongyi Han, Xiangyi Wei, ..., Yang Li, Jing Zhao
**arXiv:** [2606.27872](https://arxiv.org/abs/2606.27872)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation, but their performance degrades significantly in long-horizon tasks due to cumulative error propagation. This limitation largely arises from static feature fusion mechanisms that rely on fixed weights to combine visual, language, and action representations, preventing the model from adapting to different phases of task execution. To address this limitation, we propose S$^2$-VLA, a framework that introduces a State-Space Guided Adaptive Attention (SSGAA) mechanism. SSGAA maintains a belief state that tracks task progression and generates dynamic gating weights to adaptively fuse information from three complementary sources visual features for spatial perception, task intents for high-level task planning, and temporal action sequences for execution consistency. This adaptive fusion allows the model to shift its focus throughout task execution, aligning with the evolving requirements of different task stages. Despite its compact 2B parameter size, S$^2$-VLA consistently outperforms larger 7B-scale models and achieves state-of-the-art performance on long-horizon manipulation benchmarks, including LIBERO and SimplerEnv. highlighting the importance of adaptive feature fusion for long-horizon robotic manipulation.

---

## 6. Drop-Then-Recovery: How Redundant Are Vision-Language-Action Models?

**Authors:** Guoheng Sun, Kaixi Feng, Shwai He, ..., Gaowen Liu, Ang Li
**arXiv:** [2606.27755](https://arxiv.org/abs/2606.27755)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models enable instruction-driven robotic manipulation, but they inherit oversized language backbones from pretrained VLMs whose capacity far exceeds what is needed for short robotic instructions. This raises a basic question: how much of a VLA model is actually necessary for closed-loop control? In this work, we study architectural redundancy in VLA models by using transformer block removal as a controlled intervention. We introduce \textbf{Drop-Then-Recovery (DTR)}, an analysis protocol that removes selected blocks from a pretrained VLA model and then fine-tunes the resulting model to measure whether the removed capacity was necessary for downstream control. To make this intervention reliable, we propose \textbf{GateProbe}, a one-shot virtual-gate sensitivity metric that ranks blocks by their contribution to the downstream action loss. Across multiple VLA architectures, manipulation benchmarks and even real-robot industrial scenarios, we find a strong asymmetry in post-removal recoverability: \ul{\textit{language backbones are highly redundant for standard robotic manipulation tasks, whereas vision and action pathways are substantially less tolerant to removal}}. On LIBERO, removing half of the LLM blocks even improves OpenVLA-OFT from 95.0% to 98.3% under the same downstream fine-tuning budget, and retaining only two language blocks still recovers baseline-level performance. These results suggest that current VLA benchmarks may exert limited pressure on deep language grounding and compositional instruction understanding, and that future VLA architectures should allocate capacity more deliberately across language, vision, and action components. The code is available at this https URL.

---

## 7. Towards Evaluation of Implicit Software World Models in Coding LLMs

**Authors:** Egor Bogomolov, Yaroslav Zharov
**arXiv:** [2606.27406](https://arxiv.org/abs/2606.27406)
**Categories:** Software Engineering (cs.SE); Artificial Intelligence (cs.AI)

Software engineering, whether performed by humans or by AI agents, requires reasoning about how software behaves. We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow. In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. We use SWE-bench Verified as the source of data to hold the test close to real-world software engineering tasks. All tested models, frontier ones included, show modest performance and brittle behaviour, suggesting a notable lack of understanding of how software is executed, as opposed to how its source code is written.

---

## 8. Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation

**Authors:** Xiang Gao, Kaiwen Dong, Yuguang Yao, Padmaja Jonnalagedda, Kamalika Das
**arXiv:** [2606.27681](https://arxiv.org/abs/2606.27681)
**Categories:** Machine Learning (cs.LG); Computation and Language (cs.CL)

World models in partially observed environments rely on latent representations that summarize interaction history, but in many modern LLM-based architectures predictive performance fails to reflect representation quality due to history bypass, rendering the latent state unidentifiable. Strict latent state mediation, requiring predictions to depend only on the latent state and action, is a classical principle that resolves this, but enforcing it in text-based settings is an open challenge: textual latent states are discrete and non-differentiable, precluding variational training, and expressive LLM decoders readily ignore the bottleneck. We show how to make strict mediation work in the text domain. We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection. We then introduce textual latent states, which are discrete, interpretable, and variable-length, and factorized GRPO (fGRPO), a tree-structured reinforcement learning method that enforces strict mediation during training. Experiments on TextWorld and ScienceWorld show preserved one-step prediction accuracy alongside up to 57\% gains in representation quality and 98\% improvements in rollout performance, increasing with task complexity and horizon.

---

## 9. SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks

**Authors:** Ruiqi Song, Dujun Nie, Siyu Teng, ..., Hangbin Wu, Long Chen
**arXiv:** [2606.27807](https://arxiv.org/abs/2606.27807)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have become a dominant paradigm for embodied intelligence. However, most existing approaches are built on large-scale transformers, resulting in substantial inference latency and energy consumption that limit their practical deployment in low-power, real-time scenarios. We propose SpikeVLA, a spiking VLA architecture for embodied navigation with energy-efficient inference, consisting of three key components. (i) A spiking vision encoder, Spike-V, that replaces dense continuous layers with event-driven spiking layers to reduce the energy consumption of visual representation learning. (ii) A multi-modal spiking large language model, Spike-L, that reformulates cross-modal reasoning with spiking dynamics and token-level event-driven sparsity to further lower computational cost. (iii) A spiking action policy network, Spike-A employs Laplacian-kernel population coding with a multi-layer fully connected SNN, and decodes spiking activities into stable and robust continuous control with energy-efficient inference under low-power constraints. Experiments on navigation and robotic control tasks show that SpikeVLA significantly reduces energy consumption and computational cost while maintaining competitive performance, highlighting its potential for low-power, real-time embodied intelligence.

---

## 10. DIM-WAM: World-Action Modeling with Diverse Historical Event Memory

**Authors:** Kai Wang, Zhaopeng Gu, Yixiang Chen, ..., Yan Huang, Liang Wang
**arXiv:** [2606.27677](https://arxiv.org/abs/2606.27677)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

World-action models have shown promising robot-manipulation performance by jointly predicting future visual states and actions. However, existing methods mainly rely on short-term history and short-horizon future prediction, which is insufficient for long-horizon tasks whose correct execution depends on earlier observations and task progress. Such temporally dependent tasks require effective use of complementary temporal information, including recent local context, cross-stage historical events, immediate future dynamics, and global task progress. To address long-term forgetting and poor awareness of the global task state, we introduce DiM-WAM, a memory-augmented world-action model that integrates multi-scale historical context, local future dynamics, and global task progress. The memory extracts compact visual event information from real observations, updates multiple memory banks through independent similarity-based merging, and then reads the bank-identity- and time-embedded long-term context to condition video and action denoising. A progress-supervision objective further encourages memory tokens to encode not only completed historical events but also the current task stage and its implications for the remaining task. On RMBench, DiM-WAM raises average success from 28.4% with LingBot-VA to 69.8%, exceeding the explicit-memory Mem-0 baseline at 42.0%. On four real-world Franka tasks, it improves average stage success from 70.7% to 91.5% and full-task success from 52.5% to 80.0%. Project page: this https URL{\texttt{this https URL}}.

---

## 11. CascadeOcc: Rethinking 3D Occupancy World Models with Cascaded VQ Representations

**Authors:** Kyumin Hwang, Wonhyeok Choi, Jaeyeul Kim, ..., Daehee Park, Sunghoon Im
**arXiv:** [2606.27644](https://arxiv.org/abs/2606.27644)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

This letter proposes CascadeOcc, a novel occupancy world model that prioritizes intrinsic structural hierarchy over extrinsic auxiliary modalities for autonomous driving. Occupancy world models -- forecasting the future driving environment and planning the driving trajectory -- effectively bridge perception and planning, but current approaches often heavily rely on external modalities or large language models, failing to fully exploit the inherent structural potential of occupancy representations themselves. To enhance representational capacity for complex 3D scenes, we integrate a cascaded Vector Quantized (VQ) mechanism into an autoregressive framework. Following a coarse-to-fine principle, CascadeOcc progressively refines fine-grained details from global structures through a multi-scale architecture. Additionally, we incorporate a TimeMixer to capture multi-scale temporal dependencies, establishing a dual-hierarchy mechanism in both space and time. Experimental results on 4D occupancy forecasting and motion planning benchmarks demonstrate that CascadeOcc achieves superior performance among vision-centric approaches, validating that optimizing inherent representations is a powerful alternative to relying on external foundation models.

---

## 12. Perceptual 3D Simulation With Physical World Modeling

**Authors:** Wanhee Lee, Klemen Kotar, Rahul Mysore Venkatesh, Jared Watrous, Daniel L. K. Yamins
**arXiv:** [2606.27575](https://arxiv.org/abs/2606.27575)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Predicting how a scene will evolve after a desired 3D transformation from images is a central goal in vision, graphics, and robotics. Yet unlike ideal simulators with full access to 3D geometry and dynamics, real world systems must rely on perceptual inputs and local actions that are inherently partial and incomplete. In this work, we present P3Sim, a physical world modeling system that simulates future scene states under both partial observations and incomplete 3D transformation signals. P3Sim is composed of three interacting components: a learned physical world model, a geometric conditioning module, and a persistent scene memory. The world model interprets perception as probabilistic inference over multimodal scene variables, providing predictions of the distributions of any scene variable conditioned on any combination of others. The geometric conditioning module provides a partial 3D transform signal for conditioning the world model at inference time. The persistent scene memory integrates predictions over time, enabling online updates and consistency under uncertainty. By combining learned inference with explicit geometric structure, P3Sim balances data-driven flexibility with built-in inductive bias. This design yields a flexible perceptual simulator that generalizes across diverse 3D transformation tasks, such as novel view synthesis, object manipulation, and dynamic scene prediction, advancing toward general purpose 3D scene understanding and transformation.

---

## 13. MemoBench: Benchmarking World Modeling in Dynamically Changing Environments

**Authors:** Haoyu Chen, Kaichen Zhou, Hang Hua, ..., Paul Pu Liang, Yilun Du
**arXiv:** [2606.27537](https://arxiv.org/abs/2606.27537)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video generation models aspire to simulate dynamic environments, and several benchmarks now evaluate memory consistency across frames. However, most assess consistency only while the target remains in view, and the few that force objects out of view evaluate static scenes where nothing changes during occlusion. To bridge this gap, we introduce MemoBench, a diagnostic benchmark built around the disappear-and-reappear paradigm in dynamically changing environments: a target object undergoes a physical process, disappears from view, and must be correctly recovered in its updated state upon reappearance. We curate 360 ground-truth clips spanning synthetic and real-world scenes, and design an evaluation suite combining automated metrics with VQA-based assessment across four diagnostic pillars. Evaluation of eight state-of-the-art models reveals key insights and open challenges regarding memory consistency under the disappear-and-reappear paradigm.

---

## 14. ReWorld: Learning Better Representations for World Action Models

**Authors:** Tianze Xia, Lijun Zhou, Kaixin Xiong, ..., Haiyang Sun, Xinggang Wang
**arXiv:** [2606.27504](https://arxiv.org/abs/2606.27504)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

World Action Models (WAMs) model future environment evolution under action conditioning, offering a scalable paradigm for autonomous driving. However, existing approaches focus largely on model architecture design, and how a WAM can efficiently learn better world representations for planning remains underexplored. To address this gap, we propose ReWorld, the first representation learning framework specifically designed for autonomous-driving world action models. In WAMs, standard training supervises only the output ends of the generation and planning modules, leaving the intermediate representations that carry world knowledge to be shaped only indirectly, as byproducts of fitting these outputs. The core idea of ReWorld is to treat intermediate representations as direct targets of optimization, shaping them along three complementary dimensions. On the Video DiT responsible for generation, we impose future-predictive supervision on its intermediate representations. On the Action DiT responsible for planning, we first align its intermediate representations cross-modally with the video world representation, then further shape them to be discriminative around safety-critical boundaries via hard-negative supervision. In addition, we systematically analyze the effectiveness of existing representation learning methods in video generation world models, and discuss why their performance is limited on this task. Experiments on nuScenes and NAVSIM show that ReWorld improves fine-tuned video generation by 23.9% in FVD (81.3 to 61.9), raises closed-loop PDMS from 89.1 to 90.4 without any post-training such as RL or post-processing, and accelerates from-scratch convergence by approximately 2x.

---

## 15. PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation

**Authors:** Peiwen Zhang, Yufan Deng, Shangkun Sun, ..., Ming-Yu Liu, Daquan Zhou
**arXiv:** [2606.28128](https://arxiv.org/abs/2606.28128)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Video generation models have emerged as a promising paradigm for embodied world simulation. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. Through extensive experiments, we find that such physical instability mainly arises from two factors: deformation of moving objects and implausible spatio-temporal correlations among interacting entities, particularly during contact. Building on this observation, we propose PhysisForcing, a scalable training framework that strengthens physical consistency by focusing supervision on physics-informative regions through joint optimization of pixel-level and semantic-level features. The framework consists of a pixel-level trajectory alignment loss, which supervises DiT features using reference point trajectories, and a semantic-level relational alignment loss, which aligns DiT features with inter-region relations extracted from a frozen video understanding encoder. Extensive experiments on R-Bench, PAI-Bench, and EZS-Bench show that PhysisForcing consistently improves embodied video generation over strong baselines, improving the Wan2.2-I2V-A14B and Cosmos3-Nano base models on R-Bench by 22.3\% and 9.2\% (7.1\% and 3.7\% over vanilla finetuning), with the Cosmos3-Nano variant attaining the best overall score. Beyond generation, as a world model under the WorldArena action-planner protocol it raises the closed-loop success rate from 16.0\% to 24.0\% and further improves downstream policy success, indicating that physically aligned video models yield stronger representations for robotic manipulation.

---

## 16. Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection

**Authors:** Junwu Xiong, Yongjian Guo, Mingxi Luo, ..., Song Wang, Yince Gao
**arXiv:** [2606.27962](https://arxiv.org/abs/2606.27962)
**Categories:** Robotics (cs.RO)

This paper presents a cloud-native simulation infrastructure framework for embodied intelligence that supports large-scale training, standardized evaluation, and simulation-based data collection. The framework unifies simulation environment generation, task execution, trajectory collection, model evaluation, data management, and cloud services into a scalable and reproducible platform.
To address the high cost, limited scalability, and poor reproducibility of real-world robotic data collection, the framework adopts cloud-native technologies including elastic resource scheduling, containerized simulation, unified data management, and service-oriented system design, enabling efficient large-scale simulation for multi-model and multi-task workloads.
Built on a four-layer architecture, the framework provides standardized environment assets, automated task generation, trajectory collection, benchmark evaluation, and closed-loop data optimization. It further integrates representative systems including D-VLA, RL-VLA3, Sword, and Pre-VLA to support scalable simulation, dynamic scheduling, visual augmentation, and real-time data filtering.
We argue that cloud-native simulation infrastructure provides a unified foundation for data generation, model training, standardized evaluation, and real-world deployment, and will play a key role in the future development of embodied intelligence.

---

## 17. Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization

**Authors:** Shiang-Feng Tsai, Jin-Cheng Jhang, Yen-Ling Tai, ..., KangTung-Hsu, Yi-Ting Chen
**arXiv:** [2606.27663](https://arxiv.org/abs/2606.27663)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models leverage large-scale vision-language pretraining for flexible robot manipulation, yet at test time they remain brittle along two axes: spatial generalization, when object positions differ from those seen during training, and task generalization, when a familiar scene is paired with a different language instruction than the one seen in training. A growing family of methods addresses this brittleness by endowing a policy with the spatial and task-aware information such as 2D pixel-coordinate for object localization and placement. However, we find that existing representation through language prompting or visual prompting does not address the limitations; in contrast, exploiting a 3D point-based representation and feeding it directly to the action head leads to substantial improvements-revealing that how the grounding signal is represented and injected into the VLA is the true game changer. Thus, we propose a lightweight, model-agnostic module that represents the grounding signal in 3D, computes its relative displacement to the gripper, and injects the resulting spatial embedding directly into the action head through adaptive layer normalization. The entire module is a two-layer MLP that requires no changes to the VLA backbone or pretraining pipeline. On LIBERO-PRO, our method improves the average success rate of GR00T-N1.6 from 31.2 to 77.5 points under task perturbation and from 28.1 to 60.2 points under position perturbation (gains of 46.3 and 32.1 points). Comparable gains are achieved for $\pi_{0.5}$ as well, demonstrating that the mechanism is backbone-agnostic. Together, these results support our central finding: given adequate grounding lifted into 3D, injecting it directly into the action head is what unlocks both spatial and task generalization in VLAs-achievable with nothing more than a lightweight module on top of a pretrained backbone.

---

## 18. Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control

**Authors:** Haoyuan Wang, Yabo Chen, Haibin Huang, Chi Zhang, Xuelong Li
**arXiv:** [2606.27964](https://arxiv.org/abs/2606.27964)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Building interactive world models requires generating realistic videos while maintaining controllable dynamics over long horizons. Autoregressive video generation offers a scalable foundation, but suffers from error accumulation and temporal degradation during extended rollouts. This issue is further amplified under heterogeneous controls such as human motion and camera trajectories, which may interfere and destabilize a pretrained video prior, while existing methods often trade off controllability and visual quality. We propose "Directing the World", a fast autoregressive framework for controllable world-model video generation with compositional human-motion and camera-trajectory control. Our key idea is to decouple control learning while preserving a unified autoregressive video prior. We introduce a Fast-Slow Memory training strategy to stabilize long-horizon rollout learning and improve convergence. For human motion control, we design a t-guided Dynamic Projection mechanism and a refined Motion-CFG strategy, enabling temporally smooth and accurate motion alignment without degrading visual fidelity, and supporting multi-person this http URL learning a robust motion prior, we introduce a second-stage camera-trajectory control module to compose human dynamics with viewpoint changes for coherent world exploration. We further construct a large-scale dataset with synchronized video, text, human-motion, and camera-trajectory annotations, organized into motion-centric and camera-centric subsets for decoupled training. Extensive experiments show stable long-horizon generation with precise controllability and high visual quality. See more at this https URL.

---
