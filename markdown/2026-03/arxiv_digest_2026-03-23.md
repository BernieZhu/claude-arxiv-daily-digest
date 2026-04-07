# arXiv Daily Digest — 2026-03-23

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 10

---

## 1. X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving

**Authors:** Chaoda Zheng, Sean Li, Jinhao Deng, ..., Yu Zhang, Xianming Liu
**arXiv:** [2603.19979](https://arxiv.org/abs/2603.19979)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Scalable and reliable evaluation is increasingly critical in the end-to-end era of autonomous driving, where vision--language--action (VLA) policies directly map raw sensor streams to driving actions. Yet, current evaluation pipelines still rely heavily on real-world road testing, which is costly, biased toward limited scenario coverage, and difficult to reproduce. These challenges motivate a real-world simulator that can generate realistic future observations under proposed actions, while remaining controllable and stable over long horizons. We present X-World, an action-conditioned multi-camera generative world model that simulates future observations directly in video space. Given synchronized multi-view camera history and a future action sequence, X-World generates future multi-camera video streams that follow the commanded actions. To ensure reproducible and editable scene rollouts, X-World further supports optional controls over dynamic traffic agents and static road elements, and retains a text-prompt interface for appearance-level control (e.g., weather and time of day). Beyond world simulation, X-World also enables video style transfer by conditioning on appearance prompts while preserving the underlying action and scene dynamics. At the core of X-World is a multi-view latent video generator designed to explicitly encourage cross-view geometric consistency and temporal coherence under diverse control signals. Experiments show that X-World achieves high-quality multi-view video generation with (i) strong view consistency across cameras, (ii) stable temporal dynamics over long rollouts, and (iii) high controllability with strict action following and faithful adherence to optional scene controls. These properties make X-World a practical foundation for scalable and reproducible evaluation.

---

## 2. LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

**Authors:** Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
**arXiv:** [2603.19312](https://arxiv.org/abs/2603.19312)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Joint Embedding Predictive Architectures (JEPAs) offer a compelling framework for learning world models in compact latent spaces, yet existing methods remain fragile, relying on complex multi-term losses, exponential moving averages, pre-trained encoders, or auxiliary supervision to avoid representation collapse. In this work, we introduce LeWorldModel (LeWM), the first JEPA that trains stably end-to-end from raw pixels using only two loss terms: a next-embedding prediction loss and a regularizer enforcing Gaussian-distributed latent embeddings. This reduces tunable loss hyperparameters from six to one compared to the only existing end-to-end alternative. With ~15M parameters trainable on a single GPU in a few hours, LeWM plans up to 48x faster than foundation-model-based world models while remaining competitive across diverse 2D and 3D control tasks. Beyond control, we show that LeWM's latent space encodes meaningful physical structure through probing of physical quantities. Surprise evaluation confirms that the model reliably detects physically implausible events.

---

## 3. Structured Latent Dynamics in Wireless CSI via Homomorphic World Models

**Authors:** Salmane Naoumi, Mehdi Bennis, Marwa Chafii
**arXiv:** [2603.20048](https://arxiv.org/abs/2603.20048)
**Categories:** Signal Processing (eess.SP); Machine Learning (cs.LG)

We introduce a self-supervised framework for learning predictive and structured representations of wireless channels by modeling the temporal evolution of channel state information (CSI) in a compact latent space. Our method casts the problem as a world modeling task and leverages the Joint Embedding Predictive Architecture (JEPA) to learn action-conditioned latent dynamics from CSI trajectories. To promote geometric consistency and compositionality, we parameterize transitions using homomorphic updates derived from Lie algebra, yielding a structured latent space that reflects spatial layout and user motion. Evaluations on the DICHASUS dataset show that our approach outperforms strong baselines in preserving topology and forecasting future embeddings across unseen environments. The resulting latent space enables metrically faithful channel charts, offering a scalable foundation for downstream applications such as mobility-aware scheduling, localization, and wireless scene understanding.

---

## 4. DynFlowDrive: Flow-Based Dynamic World Modeling for Autonomous Driving

**Authors:** Xiaolu Liu, Yicong Li, Song Wang, ..., Angela Yao, Jianke Zhu
**arXiv:** [2603.19675](https://arxiv.org/abs/2603.19675)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Recently, world models have been incorporated into the autonomous driving systems to improve the planning reliability. Existing approaches typically predict future states through appearance generation or deterministic regression, which limits their ability to capture trajectory-conditioned scene evolution and leads to unreliable action planning. To address this, we propose DynFlowDrive, a latent world model that leverages flow-based dynamics to model the transition of world states under different driving actions. By adopting the rectifiedflow formulation, the model learns a velocity field that describes how the scene state changes under different driving actions, enabling progressive prediction of future latent states. Building upon this, we further introduce a stability-aware multi-mode trajectory selection strategy that evaluates candidate trajectories according to the stability of the induced scene transitions. Extensive experiments on the nuScenes and NavSim benchmarks demonstrate consistent improvements across diverse driving frameworks without introducing additional inference overhead. Source code will be abaliable at this https URL.

---

## 5. HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks

**Authors:** Jingyu Guo, Ziye Chen, Ziwen Li, ..., Tongliang Liu, Mingming Gong
**arXiv:** [2603.19822](https://arxiv.org/abs/2603.19822)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Existing UAV vision-language navigation (VLN) benchmarks have enabled language-guided flight, but they largely focus on long, step-wise route descriptions with goal-centric evaluation, making them less diagnostic for real operations where brief, high-level commands must be grounded into safe multi-stage behaviors. We present HUGE-Bench, a benchmark for High-Level UAV Vision-Language-Action (HL-VLA) tasks that tests whether an agent can interpret concise language and execute complex, process-oriented trajectories with safety awareness. HUGE-Bench comprises 4 real-world digital twin scenes, 8 high-level tasks, and 2.56M meters of trajectories, and is built on an aligned 3D Gaussian Splatting (3DGS)-Mesh representation that combines photorealistic rendering with collision-capable geometry for scalable generation and collision-aware evaluation. We introduce process-oriented and collision-aware metrics to assess process fidelity, terminal accuracy, and safety. Experiments on representative state-of-the-art VLA models reveal significant gaps in high-level semantic completion and safe execution, highlighting HUGE-Bench as a diagnostic testbed for high-level UAV autonomy.

---

## 6. WorldAgents: Can Foundation Image Models be Agents for 3D World Models?

**Authors:** Ziya Erkoç, Angela Dai, Matthias Nießner
**arXiv:** [2603.19708](https://arxiv.org/abs/2603.19708)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Given the remarkable ability of 2D foundation image models to generate high-fidelity outputs, we investigate a fundamental question: do 2D foundation image models inherently possess 3D world model capabilities? To answer this, we systematically evaluate multiple state-of-the-art image generation models and Vision-Language Models (VLMs) on the task of 3D world synthesis. To harness and benchmark their potential implicit 3D capability, we propose an agentic framing to facilitate 3D world generation. Our approach employs a multi-agent architecture: a VLM-based director that formulates prompts to guide image synthesis, a generator that synthesizes new image views, and a VLM-backed two-step verifier that evaluates and selectively curates generated frames from both 2D image and 3D reconstruction space. Crucially, we demonstrate that our agentic approach provides coherent and robust 3D reconstruction, producing output scenes that can be explored by rendering novel views. Through extensive experiments across various foundation models, we demonstrate that 2D models do indeed encapsulate a grasp of 3D worlds. By exploiting this understanding, our method successfully synthesizes expansive, realistic, and 3D-consistent worlds.

---

## 7. IndoorR2X: Indoor Robot-to-Everything Coordination with LLM-Driven Planning

**Authors:** Fan Yang, Soumya Teotia, Shaunak A. Mehta, ..., Kanji Uchino, Yonatan Bisk
**arXiv:** [2603.20182](https://arxiv.org/abs/2603.20182)
**Categories:** Robotics (cs.RO); Multiagent Systems (cs.MA)

Although robot-to-robot (R2R) communication improves indoor scene understanding beyond what a single robot can achieve, R2R alone cannot overcome partial observability without substantial exploration overhead or scaling team size. In contrast, many indoor environments already include low-cost Internet of Things (IoT) sensors (e.g., cameras) that provide persistent, building-wide context beyond onboard perception. We therefore introduce IndoorR2X, the first benchmark and simulation framework for Large Language Model (LLM)-driven multi-robot task planning with Robot-to-Everything (R2X) perception and communication in indoor environments. IndoorR2X integrates observations from mobile robots and static IoT devices to construct a global semantic state that supports scalable scene understanding, reduces redundant exploration, and enables high-level coordination through LLM-based planning. IndoorR2X provides configurable simulation environments, sensor layouts, robot teams, and task suites to systematically evaluate high-level semantic coordination strategies. Extensive experiments across diverse settings demonstrate that IoT-augmented world modeling improves multi-robot efficiency and reliability, and we highlight key insights and failure modes for advancing LLM-based collaboration between robot teams and indoor IoT sensors.

---

## 8. Speculative Policy Orchestration: A Latency-Resilient Framework for Cloud-Robotic Manipulation

**Authors:** Chanh Nguyen, Shutong Jin, Florian T. Pokorny, Erik Elmroth
**arXiv:** [2603.19418](https://arxiv.org/abs/2603.19418)
**Categories:** Robotics (cs.RO); Distributed, Parallel, and Cluster Computing (cs.DC)

Cloud robotics enables robots to offload high-dimensional motion planning and reasoning to remote servers. However, for continuous manipulation tasks requiring high-frequency control, network latency and jitter can severely destabilize the system, causing command starvation and unsafe physical execution.
To address this, we propose Speculative Policy Orchestration (SPO), a latency-resilient cloud-edge framework. SPO utilizes a cloud-hosted world model to pre-compute and stream future kinematic waypoints to a local edge buffer, decoupling execution frequency from network round-trip time. To mitigate unsafe execution caused by predictive drift, the edge node employs an $\epsilon$-tube verifier that strictly bounds kinematic execution errors. The framework is coupled with an Adaptive Horizon Scaling mechanism that dynamically expands or shrinks the speculative pre-fetch depth based on real-time tracking error.
We evaluate SPO on continuous RLBench manipulation tasks under emulated network delays. Results show that even when deployed with learned models of modest accuracy, SPO reduces network-induced idle time by over 60% compared to blocking remote inference. Furthermore, SPO discards approximately 60% fewer cloud predictions than static caching baselines. Ultimately, SPO enables fluid, real-time cloud-robotic control while maintaining bounded physical safety.

---

## 9. VAMPO: Policy Optimization for Improving Visual Dynamics in Video Action Models

**Authors:** Zirui Ge, Pengxiang Ding, Baohua Yin, ..., Yaozhi Luo, Donglin Wang
**arXiv:** [2603.19370](https://arxiv.org/abs/2603.19370)
**Categories:** Robotics (cs.RO)

Video action models are an appealing foundation for Vision--Language--Action systems because they can learn visual dynamics from large-scale video data and transfer this knowledge to downstream robot control. Yet current diffusion-based video predictors are trained with likelihood-surrogate objectives, which encourage globally plausible predictions without explicitly optimizing the precision-critical visual dynamics needed for manipulation. This objective mismatch often leads to subtle errors in object pose, spatial relations, and contact timing that can be amplified by downstream policies. We propose VAMPO, a post-training framework that directly improves visual dynamics in video action models through policy optimization. Our key idea is to formulate multi-step denoising as a sequential decision process and optimize the denoising policy with rewards defined over expert visual dynamics in latent space. To make this optimization practical, we introduce an Euler Hybrid sampler that injects stochasticity only at the first denoising step, enabling tractable low-variance policy-gradient estimation while preserving the coherence of the remaining denoising trajectory. We further combine this design with GRPO and a verifiable non-adversarial reward. Across diverse simulated and real-world manipulation tasks, VAMPO improves task-relevant visual dynamics, leading to better downstream action generation and stronger generalization. The homepage is this https URL.

---

## 10. EgoForge: Goal-Directed Egocentric World Simulator

**Authors:** Yifan Shen, Jiateng Liu, Xinzhuo Li, ..., Xu Cao, Ismini Lourentzou
**arXiv:** [2603.20169](https://arxiv.org/abs/2603.20169)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Multimedia (cs.MM)

Generative world models have shown promise for simulating dynamic environments, yet egocentric video remains challenging due to rapid viewpoint changes, frequent hand-object interactions, and goal-directed procedures whose evolution depends on latent human intent. Existing approaches either focus on hand-centric instructional synthesis with limited scene evolution, perform static view translation without modeling action dynamics, or rely on dense supervision, such as camera trajectories, long video prefixes, synchronized multicamera capture, etc. In this work, we introduce EgoForge, an egocentric goal-directed world simulator that generates coherent, first-person video rollouts from minimal static inputs: a single egocentric image, a high-level instruction, and an optional auxiliary exocentric view. To improve intent alignment and temporal consistency, we propose VideoDiffusionNFT, a trajectory-level reward-guided refinement that optimizes goal completion, temporal causality, scene consistency, and perceptual fidelity during diffusion sampling. Extensive experiments show EgoForge achieves consistent gains in semantic alignment, geometric stability, and motion fidelity over strong baselines, and robust performance in real-world smart-glasses experiments.

---
