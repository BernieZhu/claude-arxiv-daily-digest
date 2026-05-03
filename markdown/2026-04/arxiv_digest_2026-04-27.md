# arXiv Daily Digest — 2026-04-27

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 7

---

## 1. Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond

**Authors:** Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, ..., Philip Torr, Jiaya Jia
**arXiv:** [2604.22748](https://arxiv.org/abs/2604.22748)
**Categories:** Artificial Intelligence (cs.AI)

As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.

---

## 2. GazeVLA: Learning Human Intention for Robotic Manipulation

**Authors:** Chengyang Li, Kaiyi Xiong, Yuan Xu, ..., Yizhou Wang, Wentao Zhu
**arXiv:** [2604.22615](https://arxiv.org/abs/2604.22615)
**Categories:** Robotics (cs.RO)

Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.

---

## 3. RedVLA: Physical Red Teaming for Vision-Language-Action Models

**Authors:** Yuhao Zhang, Borong Zhang, Jiaming Fan, ..., Yaodong Yang, Jiaming Ji
**arXiv:** [2604.22591](https://arxiv.org/abs/2604.22591)
**Categories:** Robotics (cs.RO)

The real-world deployment of Vision-Language-Action (VLA) models remains limited by the risk of unpredictable and irreversible physical harm. However, we currently lack effective mechanisms to proactively detect these physical safety risks before deployment. To address this gap, we propose \textbf{RedVLA}, the first red teaming framework for physical safety in VLA models. We systematically uncover unsafe behaviors through a two-stage process: (I) \textbf{Risk Scenario Synthesis} constructs a valid and task-feasible initial risk scene. Specifically, it identifies critical interaction regions from benign trajectories and positions the risk factor within these regions, aiming to entangle it with the VLA's execution flow and elicit a target unsafe behavior. (II) \textbf{Risk Amplification} ensures stable elicitation across heterogeneous models. It iteratively refines the risk factor state through gradient-free optimization guided by trajectory features. Experiments on six representative VLA models show that RedVLA uncovers diverse unsafe behaviors and achieves the ASR up to 95.5\% within 10 optimization iterations. To mitigate these risks, we further propose SimpleVLA-Guard, a lightweight safety guard built from RedVLA-generated data. Our data, assets, and code are available \href{this https URL}{here}.

---

## 4. CodeGraphVLP: Code-as-Planner Meets Semantic-Graph State for Non-Markovian Vision-Language-Action Models

**Authors:** Khoa Vo, Sieu Tran, Taisei Hanyu, ..., Anh Nguyen, Ngan Le
**arXiv:** [2604.22238](https://arxiv.org/abs/2604.22238)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models promise generalist robot manipulation, but are typically trained and deployed as short-horizon policies that assume the latest observation is sufficient for action reasoning. This assumption breaks in non-Markovian long-horizon tasks, where task-relevant evidence can be occluded or appear only earlier in the trajectory, and where clutter and distractors make fine-grained visual grounding brittle. We present CodeGraphVLP, a hierarchical framework that enables reliable long-horizon manipulation by combining a persistent semantic-graph state with an executable code-based planner and progress-guided visual-language prompting. The semantic-graph maintains task-relevant entities and relations under partial observability. The synthesized planner executes over this semantic-graph to perform efficient progress checks and outputs a subtask instruction together with subtask-relevant objects. We use these outputs to construct clutter-suppressed observations that focus the VLA executor on critical evidence. On real-world non-Markovian tasks, CodeGraphVLP improves task completion over strong VLA baselines and history-enabled variants while substantially lowering planning latency compared to VLM-in-the-loop planning. We also conduct extensive ablation studies to confirm the contributions of each component.

---

## 5. dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model

**Authors:** Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yaokai Xue, Yichen Zhu
**arXiv:** [2604.22152](https://arxiv.org/abs/2604.22152)
**Categories:** Robotics (cs.RO)

Evaluating robotics policies across thousands of environments and thousands of tasks is infeasible with existing approaches. This motivates the need for a new methodology for scalable robotics policy evaluation. In this paper, we propose dWorldEval, which uses a discrete diffusion world model as a scalable evaluation proxy for robotics policies. Specifically, dWorldEval maps all modalities - including vision, language, and robotic actions - into a unified token space, modeling them via a single transformer-based denoising network. In this paper, we propose dWorldEval, using a discrete diffusion world model as a scalable evaluation proxy for robotics policy. Specifically, it maps all modalities, including vision, language, and robotics action into a unified token space, then denoises them with a single transformer network. Building on this architecture, we employ a sparse keyframe memory to maintain spatiotemporal consistency. We also introduce a progress token that indicates the degree of task completion. At inference, the model jointly predicts future observations and progress token, allowing automatically determine success when the progress reaches 1. Extensive experiments demonstrate that dWorldEval significantly outperforms previous approaches, i.e., WorldEval, Ctrl-World, and WorldGym, on LIBERO, RoboTwin, and multiple real-robot tasks. It paves the way for a new architectural paradigm in building world simulators for robotics evaluation at scale.

---

## 6. Beyond Patient Invariance: Learning Cardiac Dynamics via Action-Conditioned JEPAs

**Authors:** Jose Geraldo Fernandes, Luiz Facury, Pedro Robles Dutenhefner, Wagner Meira Jr
**arXiv:** [2604.22618](https://arxiv.org/abs/2604.22618)
**Categories:** Machine Learning (cs.LG)

Self-supervised learning in healthcare has largely relied on invariance-based objectives, which maximize similarity between different views of the same patient. While effective for static anatomy, this paradigm is fundamentally misaligned with clinical diagnosis, as it mathematically compels the model to suppress the transient pathological changes it is intended to detect. We propose a shift towards Action-Conditioned World Models that learn to simulate the dynamics of disease progression, or Event-Conditioned. Adapting the LeJEPA framework to physiological time-series, we define pathology not as a static label, but as a transition vector acting on a patient's latent state. By predicting the future electrophysiological state of the heart given a disease onset, our model explicitly disentangles stable anatomical features from dynamic pathological forces. Evaluated on the MIMIC-IV-ECG dataset, our approach outperforms fully supervised baselines on the critical triage task. Crucially, we demonstrate superior sample efficiency: in low-resource regimes, our world model outperforms supervised learning by over 0.05 AUROC. These results suggest that modeling biological dynamics provides a dense supervision signal that is far more robust than static classification. Source code is available at this https URL

---

## 7. OccDirector: Language-Guided Behavior and Interaction Generation in 4D Occupancy Space

**Authors:** Zhuding Liang, Tianyi Yan, Dubing Chen, ..., Kun Zhan, Jianbing Shen
**arXiv:** [2604.22240](https://arxiv.org/abs/2604.22240)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Generative world models increasingly rely on 4D occupancy for realistic autonomous driving simulation. However, existing generation frameworks depend on rigid geometric conditions (e.g., explicit trajectories) or simplistic attribute-level text, failing to orchestrate complex, sequential multi-agent interactions. To address this semantic-spatiotemporal gap, we propose OccDirector, a pioneering framework that generates 4D occupancy dynamics conditioned solely on natural language. Operating as a ``scenario director'', OccDirector maps natural language scripts into physically plausible voxel dynamics without requiring geometric priors. Technically, it employs a VLM-driven Spatio-Temporal MMDiT equipped with a history-prefix anchoring strategy to ensure long-horizon interaction consistency. Furthermore, we introduce OccInteract-85k, a novel dataset uniquely annotated with multi-level language instructions: ranging from static layouts to intricate multi-agent behaviors, alongside a novel VLM-based evaluation benchmark. Extensive experiments demonstrate that OccDirector achieves state-of-the-art generation quality and unprecedented instruction-following capabilities, successfully shifting the paradigm from appearance synthesis to language-driven behavior orchestration.

---
