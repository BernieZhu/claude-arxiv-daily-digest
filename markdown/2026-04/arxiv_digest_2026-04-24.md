# arXiv Daily Digest — 2026-04-24

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 7

---

## 1. From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges

**Authors:** Yiming Zhong, Yaoyu He, Zemin Yang, ..., Xinge Zhu, Yuexin Ma
**arXiv:** [2604.21391](https://arxiv.org/abs/2604.21391)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Bridging high-level semantic understanding with low-level physical control remains a persistent challenge in embodied intelligence, stemming from the fundamental spatiotemporal scale mismatch between cognition and action. Existing generative VLA policies typically adopt a "Generation-from-Noise" paradigm, which disregards this disparity, leading to representation inefficiency and weak condition alignment during optimization. In this work, we propose ResVLA, an architecture that shifts the paradigm to "Refinement-from-Intent." Recognizing that robotic motion naturally decomposes into global intent and local dynamics, ResVLA utilizes spectral analysis to decouple control into a deterministic low-frequency anchor and a stochastic high-frequency residual. By anchoring the generative process on the predicted intent, our model focuses strictly on refining local dynamics via a residual diffusion bridge. Extensive simulation experiments show that ResVLA achieves competitive performance, strong robustness to language and robot embodiment perturbations, and faster convergence than standard generative baselines. It also demonstrates strong performance in real-world robot experiments.

---

## 2. VLAA-GUI: Knowing When to Stop, Recover, and Search, A Modular Framework for GUI Automation

**Authors:** Qijun Han, Haoqin Tu, Zijun Wang, ..., Yuyin Zhou, Cihang Xie
**arXiv:** [2604.21375](https://arxiv.org/abs/2604.21375)
**Categories:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Software Engineering (cs.SE)

Autonomous GUI agents face two fundamental challenges: early stopping, where agents prematurely declare success without verifiable evidence, and repetitive loops, where agents cycle through the same failing actions without recovery. We present VLAA-GUI, a modular GUI agentic framework built around three integrated components that guide the system on when to Stop, Recover, and Search. First, a mandatory Completeness Verifier enforces UI-observable success criteria and verification at every finish step -- with an agent-level verifier that cross-examines completion claims with decision rules, rejecting those lacking direct visual evidence. Second, a mandatory Loop Breaker provides multi-tier filtering: switching interaction mode after repeated failures, forcing strategy changes after persistent screen-state recurrence, and binding reflection signals to strategy shifts. Third, an on-demand Search Agent searches online for unfamiliar workflows by directly querying a capable LLM with search ability, returning results as plain text. We additionally integrate a Coding Agent for code-intensive actions and a Grounding Agent for precise action grounding, both invoked on demand when required. We evaluate VLAA-GUI across five top-tier backbones, including Opus 4.5, 4.6 and Gemini 3.1 Pro, on two benchmarks with Linux and Windows tasks, achieving top performance on both (77.5% on OSWorld and 61.0% on WindowsAgentArena). Notably, three of the five backbones surpass human performance (72.4%) on OSWorld in a single pass. Ablation studies show that all three proposed components consistently improve a strong backbone, while a weaker backbone benefits more from these tools when the step budget is sufficient. Further analysis also shows that the Loop Breaker nearly halves wasted steps for loop-prone models.

---

## 3. CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors

**Authors:** Dachong Li, ZhuangZhuang Chen, Jin Zhang, Jianqiang Li
**arXiv:** [2604.21241](https://arxiv.org/abs/2604.21241)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose $CorridorVLA$, which predicts sparse spatial anchors as incremental physical changes (e.g., $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside it receive corrective gradients, while minor deviations from contacts and execution noise are permitted. On the more challenging LIBERO-Plus benchmark, CorridorVLA yields consistent gains across both SmolVLA and GR00T, improving success rate by $3.4\%$--$12.4\%$ over the corresponding baselines; notably, our GR00T-Corr variant reaches a success rate of $83.21\%$. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code is available at this https URL.

---

## 4. How VLAs (Really) Work In Open-World Environments

**Authors:** Amir Rasouli, Yangzheng Wu, Zhiyuan Li, ..., Charles Eret, Sajjad Pakdamansavoji
**arXiv:** [2604.21192](https://arxiv.org/abs/2604.21192)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-language-action models (VLAs) have been extensively used in robotics applications, achieving great success in various manipulation problems. More recently, VLAs have been used in long-horizon tasks and evaluated on benchmarks, such as BEHAVIOR1K (B1K), for solving complex household chores. The common metric for measuring progress in such benchmarks is success rate or partial score based on satisfaction of progress-agnostic criteria, meaning only the final states of the objects are considered, regardless of the events that lead to such states. In this paper, we argue that using such evaluation protocols say little about safety aspects of operation and can potentially exaggerate reported performance, undermining core challenges for future real-world deployment. To this end, we conduct a thorough analysis of state-of-the-art models on the B1K Challenge and evaluate policies in terms of robustness via reproducibility and consistency of performance, safety aspects of policies operations, task awareness, and key elements leading to the incompletion of tasks. We then propose evaluation protocols to capture safety violations to better measure the true performance of the policies in more complex and interactive scenarios. At the end, we discuss the limitations of the existing VLAs and motivate future research.

---

## 5. Long-Horizon Manipulation via Trace-Conditioned VLA Planning

**Authors:** Isabella Liu, An-Chieh Cheng, Rui Yan, ..., Xiaolong Wang, Sifei Liu
**arXiv:** [2604.21924](https://arxiv.org/abs/2604.21924)
**Categories:** Robotics (cs.RO)

Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: this https URL

---

## 6. Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training

**Authors:** Yaxuan Li, Zhongyi Zhou, Yefei Chen, ..., Jianyu Chen, Yichen Zhu
**arXiv:** [2604.21741](https://arxiv.org/abs/2604.21741)
**Categories:** Robotics (cs.RO)

Post-training is essential for turning pretrained generalist robot policies into reliable task-specific controllers, but existing human-in-the-loop pipelines remain tied to physical execution: each correction requires robot time, scene setup, resets, and operator supervision in the real world. Meanwhile, action-conditioned world models have been studied mainly for imagination, synthetic data generation, and policy evaluation. We propose \textbf{Human-in-the-World-Model (Hi-WM)}, a post-training framework that uses a learned world model as a reusable corrective substrate for failure-targeted policy improvement. A policy is first rolled out in closed loop inside the world model; when the rollout becomes incorrect or failure-prone, a human intervenes directly in the model to provide short corrective actions. Hi-WM caches intermediate states and supports rollback and branching, allowing a single failure state to be reused for multiple corrective continuations and yielding dense supervision around behaviors that the base policy handles poorly. The resulting corrective trajectories are then added back to the training set for post-training. We evaluate Hi-WM on three real-world manipulation tasks spanning both rigid and deformable object interaction, and on two policy backbones. Hi-WM improves real-world success by 37.9 points on average over the base policy and by 19.0 points over a world-model closed-loop baseline, while world-model evaluation correlates strongly with real-world performance (r = 0.953). These results suggest that world models can serve not only as generators or evaluators, but also as effective corrective substrates for scalable robot post-training.

---

## 7. WorldMark: A Unified Benchmark Suite for Interactive Video World Models

**Authors:** Xiaojie Xu, Zhengyuan Lin, Kang He, ..., Kaipeng Zhang, Yongtao Ge
**arXiv:** [2604.21686](https://arxiv.org/abs/2604.21686)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Interactive video generation models such as Genie, YUME, HY-World, and Matrix-Game are advancing rapidly, yet every model is evaluated on its own benchmark with private scenes and trajectories, making fair cross-model comparison impossible. Existing public benchmarks offer useful metrics such as trajectory error, aesthetic scores, and VLM-based judgments, but none supplies the standardized test conditions -- identical scenes, identical action sequences, and a unified control interface -- needed to make those metrics comparable across models with heterogeneous inputs. We introduce WorldMark, the first benchmark that provides such a common playing field for interactive Image-to-Video world models. WorldMark contributes: (1) a unified action-mapping layer that translates a shared WASD-style action vocabulary into each model's native control format, enabling apples-to-apples comparison across six major models on identical scenes and trajectories; (2) a hierarchical test suite of 500 evaluation cases covering first- and third-person viewpoints, photorealistic and stylized scenes, and three difficulty tiers from Easy to Hard spanning 20-60s; and (3) a modular evaluation toolkit for Visual Quality, Control Alignment, and World Consistency, designed so that researchers can reuse our standardized inputs while plugging in their own metrics as the field evolves. We will release all data, evaluation code, and model outputs to facilitate future research. Beyond offline metrics, we launch World Model Arena (this http URL), an online platform where anyone can pit leading world models against each other in side-by-side battles and watch the live leaderboard.

---
