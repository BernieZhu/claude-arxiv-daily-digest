# arXiv Daily Digest — 2026-06-08

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 12

---

## 1. Bootstrap Theory of Representational Emergence: Explanatory Insufficiency as a Driver of Representation Learning and World Models

**Authors:** Jacques Raynal, Pierre Slangen, Elsa Raynal, Jacques Margerit
**arXiv:** [2606.07303](https://arxiv.org/abs/2606.07303)
**Categories:** Machine Learning (cs.LG)

Representation learning is central to modern machine learning, enabling transitions from handcrafted features to learned embeddings, latent spaces, foundation models, world models, and digital twins. Yet most research examines how representations are optimized after a representational framework has been selected, while less attention is given to when a new level of representation becomes necessary. We introduce the Bootstrap Theory of Representational Emergence (TBER), a framework describing how new representations arise when existing ones become explanatorily insufficient. In this view, representational innovation is not only driven by more data, larger models, or greater computational power, but also by persistent explanatory gaps: situations in which a representation can still describe observations but can no longer make their organization or transformations intelligible. TBER identifies explanatory insufficiency as a positive signal for representational transition. A representation becomes insufficient not because it is necessarily false, but because its explanatory domain has been exceeded. The bootstrap dynamic follows a recursive sequence: observations reveal anomalies; anomalies expose insufficiencies; insufficiencies motivate new representations; and these new representations generate further observations and possible new this http URL formalize this process through five stages: stabilized observation, anomaly detection, recognition of explanatory insufficiency, representational emergence, and provisional stabilization. We discuss applications to representation learning, latent spaces, foundation models, world models, digital twins, adaptive biological systems, and scientific discovery. TBER suggests that future AI systems may benefit from mechanisms for detecting the explanatory limits of their own internal representations.

---

## 2. Learning Explicit Behavioral Models with Adaptive Questions and World-Model Probes

**Authors:** Hikaru Shindo, Yu Deng, Teng Cao, ..., Gopika Sudhakaran, Kristian Kersting
**arXiv:** [2606.07127](https://arxiv.org/abs/2606.07127)
**Categories:** Machine Learning (cs.LG)

Interactive agents trained only against task return can achieve high scores while failing to represent the mechanisms that make their actions succeed. This makes brittle behavior difficult to diagnose and limits adaptation when environment dynamics change. Existing LLM reflection and policy-code repair can revise behavior from failed trajectories, but questions and world-understanding tests are usually used only after training. We introduce an Explicit Symbolic Behavioral Model (ESBM), a trainable behavioral model that couples task performance with evidence-grounded question answering and executable mechanism prediction. An ESBM represents behavior through typed predicates, weighted rules, bounded options and mechanism memory; the mechanism layer predicts symbolic events, object changes, rewards and terminal consequences under action interventions. After each rollout, adaptive questions and active world-model probes convert score failures, QA errors and transition-prediction errors into constraints for local ESBM edits. Candidate models are selected by a multi-criterion rule that jointly evaluates task score, answerability and active world-model consistency. Under the tested Atari-style protocols, ESBM learns high-scoring policies while producing explicit answers and executable mechanism predictions, indicating that adaptive questions can serve as both training pressure and reusable benchmarks for mechanistic policy learning in this setting.

---

## 3. RhinoVLA Technical Report

**Authors:** Huixi Intelligence, Chen Zhang, Chenyang Zhou, ..., Yijia Zhang, Yuxi Liu
**arXiv:** [2606.07383](https://arxiv.org/abs/2606.07383)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at this https URL.

---

## 4. Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models

**Authors:** Jinhao Wu, Shiduo Zhang, Yicheng Liu, ..., Xipeng Qiu, Yu-Gang Jiang
**arXiv:** [2606.07107](https://arxiv.org/abs/2606.07107)
**Categories:** Robotics (cs.RO)

Most vision-language-action (VLA) models map observations directly to actions without explicit intermediate planning, which limits performance on long-horizon tasks where early mistakes compound. We propose Coarse-to-Control, a plan-execute VLA that introduces planning natively in the action-token space. The key idea is to let the policy first predict a compact sequence of coarse action tokens that summarize the intended future trajectory, and then generate executable action tokens conditioned on this plan. Because both planning and execution share a unified discrete action vocabulary, the plan stays close to the control manifold and provides directly actionable guidance rather than an abstract hint that must be translated back to motor commands. Experiments on LIBERO, SimplerEnv-WidowX, and real-world manipulation tasks show that action-token planning consistently improves over direct action generation, with the largest gains on long-horizon multi-stage tasks.

---

## 5. Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning

**Authors:** Yinzhou Tang, Jingbo Xu, Yu Shang, ..., Wei Wu, Yong Li
**arXiv:** [2606.07089](https://arxiv.org/abs/2606.07089)
**Categories:** Robotics (cs.RO)

World Action Models (WAMs) offer a promising approach to embodied intelligence, yet existing methods rely heavily on video prediction as action priors and lack adaptive multimodal reasoning, limiting their effectiveness on long-horizon, complex tasks. We observe that WAMs require different multimodal reasoning modes under different execution contexts: textual reasoning is essential during task transitions to guide high-level action prediction, while visual reasoning is critical during fine-grained manipulation for precise control. Motivated by this observation, we propose \textbf{AdaWAM}, a world action model with adaptive multimodal reasoning abilities. AdaWAM integrates a lightweight dynamic router that autonomously triggers textual or visual reasoning as needed during task execution. Experiments on both simulated and real-world embodied tasks show that AdaWAM substantially improves inference efficiency while outperforming state-of-the-art embodied policies. Codes and demos are available at: this https URL.

---

## 6. STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images

**Authors:** Abhiroop Ajith, Constantinos Chamzas
**arXiv:** [2606.06832](https://arxiv.org/abs/2606.06832)
**Categories:** Robotics (cs.RO)

Robots performing long-horizon visual manipulation observe high-dimensional images, but successful plans depend on action-relevant facts: what can be done now and what changes afterward. A useful planning representation should discard irrelevant visual details while preserving action applicability and effects. Classical task planners exploit this structure through symbolic operators with preconditions and effects, but obtaining such representations from raw visual experience remains challenging. We study a visual task-planning setting in which a robot receives only image transitions: the current image, executed high-level action, and the resulting image. At test time, given a start image and a goal image, the robot must produce a sequence of high-level actions that reaches the goal. To address this problem, we introduce STRIPS-WM, a framework for learning image-grounded STRIPS-style world models directly from visual transitions. STRIPS-WM first induces a finite abstract transition graph from images, then learns latent binary predicates and one grounded propositional operator per action label. The learned operators form a symbolic action model with sparse preconditions and add/delete effects. Finally, the learned predicates are distilled into a visual encoder, enabling classical planning directly from novel start and goal images. Experiments on visual rearrangement tasks show that STRIPS-WM improves image-to-plan success over the tested visual rollout, latent graph-search and latent-symbolic baselines.

---

## 7. Robots Need More than VLA and World Models

**Authors:** Elis Karcini, Faisal Mehrban, Quang Nguyen, ..., Marco Hutter, Haitham Bou-Ammar
**arXiv:** [2606.06556](https://arxiv.org/abs/2606.06556)
**Categories:** Robotics (cs.RO)

Generalist robot intelligence is often framed as a policy-scaling problem: collect more robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect broader generalisation. In this position paper, we argue that this framing is incomplete. The central bottleneck is not only policy learning, but the absence of mechanisms that convert the world's abundant unstructured behavioural data into grounded robot supervision. Human motion, internet video, simulation rollouts, and interactive demonstrations contain rich information about tasks, goals, contacts, failures, and physical constraints, yet most of this information is not directly usable by robot policies because it lacks embodiment-specific action labels, task semantics, and reward structure. We identify four missing components for the next generation of robotics: data interfaces for autolabelling unstructured behaviour, embodiment interfaces for retargeting human motion to robot actions, world-model interfaces for physics-grounded 3D reasoning, and reward interfaces for inferring task progress and success from video and language. We survey recent progress in robot foundation models, cross-embodiment datasets, learning from video, world models, and reward modelling, and propose a research agenda for building robotics systems that can learn not only from robot demonstrations, but from the broader physical world.

---

## 8. LARA: Latent Action Representation Alignment for Vision-Language-Action Models

**Authors:** Mengya Liu, Baoxiong Jia, Jiangyong Huang, Jingze Zhang, Siyuan Huang
**arXiv:** [2606.07100](https://arxiv.org/abs/2606.07100)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Visual-language action (VLA) models enable robots to predict actions directly from observations and language instructions, but their performance depends on large-scale, high-quality data and is limited by the scarcity of real-world robot action datasets. To facilitate VLA model learning with abundant unlabeled human videos, Latent Action Models (LAM) learn latent action representations from visual dynamics to provide additional supervision for VLA learning. However, LAM and VLA are typically trained separately, leaving LAM ungrounded during VLA training and VLA models constrained by frozen LAM representations. To address these issues, we propose Latent Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation alignment. This enables reciprocal benefits where LAMs learn with action trajectories to avoid spurious visual changes, while VLAs are regularized by forward dynamics learned within LAMs to reduce hallucinations of functionally ineffective trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-world robotic manipulation benchmarks.

---

## 9. Robotic Policy Adaptation via Weight-Space Meta-Learning

**Authors:** Christian Bianchi, Siamak Yousefi, Alessio Sampieri, ..., Fabio Galasso, Luca Franco
**arXiv:** [2606.07217](https://arxiv.org/abs/2606.07217)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models are emerging as a promising paradigm for robotic manipulation, enabling general-purpose policies trained from large corpora of demonstrations and action labels. However, adapting these models to new tasks still typically requires task-specific demonstrations, action annotations, and additional fine-tuning, making deployment costly and difficult to scale.
We propose WIZARD, a weight-space meta-learning framework that sidesteps task-specific fine-tuning by generating task-specific LoRA parameters for a frozen VLA policy. Given only a language instruction and a short demonstration video, WIZARD predicts the corresponding adaptation weights in a single forward pass, without target-task action labels or test-time optimization. During meta-training, WIZARD learns to map task evidence directly to expert LoRA updates, capturing relationships between tasks in weight space.
Experiments on LIBERO show that WIZARD improves performance by up to ~2x on unseen dataset collections and up to ~14x on unseen tasks. On a Franka Emika Panda, WIZARD consistently improves over a real-domain adapted baseline, showing that generated adapters provide task-level specialization beyond simulation.

---

## 10. Spline Policy: A Structured Representation for Robot Policies

**Authors:** Mengze Tian, Yiming Li, Sichao Liu, Auke Ijspeert, Sylvain Calinon
**arXiv:** [2606.07386](https://arxiv.org/abs/2606.07386)
**Categories:** Robotics (cs.RO)

Modern imitation-learning policies for robot manipulation often represent actions as fixed-resolution action chunks, which are simple and effective but expose limited geometric and temporal structure before execution. This paper studies Spline Policy (SP), a structured representation that replaces action chunks with spline parameters while keeping the policy backbone unchanged. The predicted spline can be decoded as a compact continuous trajectory, queried at different temporal resolutions, constrained or edited in parameter space, and passed to downstream controllers. For quadratic spline outputs, the same representation can also be converted into a state-dependent vector field through an analytical distance-field construction. Under the regularity and projection assumptions of this construction, the induced dynamics do not increase the distance to the generated spline, yielding a principled local corrective mechanism around the predicted motion. The spline output further supports uncertainty propagation from observations to spline parameters, trajectories, and flow fields, and can be combined with classical control mechanisms such as null-space collision avoidance without retraining the policy backbone. We instantiate SP with diffusion, flow-matching, transformer-based, and vision-language-action backbones. Experiments in low-dimensional motion learning, simulated manipulation under matched backbones, dexterous manipulation, and real-robot case studies show that SP remains compatible with modern policy learners while exposing useful motion-structure properties, including compact decoding, temporal resampling, local correction around predicted motions, uncertainty evaluation, and controller compatibility.

---

## 11. ActionMap: Robot Policy Learning via Voxel Action Heatmap

**Authors:** Pei Yang, Hai Ci, Yanzhe Chen, ..., Han Cai, Mike Zheng Shou
**arXiv:** [2606.06904](https://arxiv.org/abs/2606.06904)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action (VLA) models have advanced rapidly across backbones, training recipes, and data scale, yet the action decoder, which converts the backbone's hidden state into a continuous control signal, has barely changed and remains a single-point predictor across the majority of current VLAs. Whether implemented via autoregressive token bins, L1 regression, or flow-matching denoising, the resulting decoder treats the action space as unstructured, leaving the geometric proximity of neighboring actions unexploited during training. To advance this, we introduce ActionMap, a voxel heatmap action head that drops into an existing VLA in place of its native action decoder. For each new action, the head predicts a voxel heatmap over the action space, where each voxel directly stores the probability of the corresponding action. Across LIBERO simulation and real-world Franka manipulation, our heatmap head surpasses two architecturally distinct backbones at matched training steps (e.g., +8.2% over OpenVLA-OFT's L1 regression head on the LIBERO four-suite average), converges at comparable or faster rates on both backbones, and remains markedly more data-efficient at low training data. The cross-backbone consistency indicates that action representation is a real lever for VLA performance, distinct from further backbone or recipe scaling. Project Page: this https URL.

---

## 12. AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization

**Authors:** Yu Li, Menghan Xia, Gongye Liu, ..., Kun Gai, Yujiu Yang
**arXiv:** [2606.07326](https://arxiv.org/abs/2606.07326)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Despite being a pivotal frontier, interactive world modeling remains underexplored in terms of the versatile controllability required by practical scenarios. To bridge this gap, we present AnchorWorld, a framework that advances egocentric simulation through enhanced interaction integrity and a flexible mechanism for world customization. First, we utilize 3D human motion as the primary interaction modality. To complement the out-of-view or truncated body parts in egocentric views, we introduce an auxiliary training supervision that incorporates exogenous viewpoints decoupled from the agent's first-person sensorium. It allows the model to observe the agent's full-body positioning relative to the environment, facilitating a more robust spatial grounding of human-world interactions. Furthermore, we propose a simple yet effective mechanism for customizing self-evolving worlds. This is achieved by defining anchor views within a unified world coordinate system, coupled with textual descriptions dictating the dynamic evolution of local scenes. Experimental results show that AnchorWorld significantly outperforms state-of-the-art baselines, while ablation studies validate the effectiveness of our key designs. Notably, our customization scheme exhibits promising spatio-temporal geometric consistency and adheres strictly to the prescribed evolutionary dynamics.

---
