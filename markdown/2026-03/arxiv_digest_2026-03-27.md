# arXiv Daily Digest — 2026-03-27

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 14

---

## 1. Drive My Way: Preference Alignment of Vision-Language-Action Model for Personalized Driving

**Authors:** Zehao Wang, Huaide Jiang, Shuaiwu Dong, ..., Hang Qiu, Jiachen Li
**arXiv:** [2603.25740](https://arxiv.org/abs/2603.25740)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG); Multiagent Systems (cs.MA)

Human driving behavior is inherently personal, which is shaped by long-term habits and influenced by short-term intentions. Individuals differ in how they accelerate, brake, merge, yield, and overtake across diverse situations. However, existing end-to-end autonomous driving systems either optimize for generic objectives or rely on fixed driving modes, lacking the ability to adapt to individual preferences or interpret natural language intent. To address this gap, we propose Drive My Way (DMW), a personalized Vision-Language-Action (VLA) driving framework that aligns with users' long-term driving habits and adapts to real-time user instructions. DMW learns a user embedding from our personalized driving dataset collected across multiple real drivers and conditions the policy on this embedding during planning, while natural language instructions provide additional short-term guidance. Closed-loop evaluation on the Bench2Drive benchmark demonstrates that DMW improves style instruction adaptation, and user studies show that its generated behaviors are recognizable as each driver's own style, highlighting personalization as a key capability for human-centered autonomous driving. Our data and code are available at this https URL.

---

## 2. Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models

**Authors:** Kaijin Chen, Dingkang Liang, Xin Zhou, ..., Pengfei Wan, Xiang Bai
**arXiv:** [2603.25716](https://arxiv.org/abs/2603.25716)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Video world models have shown immense potential in simulating the physical world, yet existing memory mechanisms primarily treat environments as static canvases. When dynamic subjects hide out of sight and later re-emerge, current methods often struggle, leading to frozen, distorted, or vanishing subjects. To address this, we introduce Hybrid Memory, a novel paradigm requiring models to simultaneously act as precise archivists for static backgrounds and vigilant trackers for dynamic subjects, ensuring motion continuity during out-of-view intervals. To facilitate research in this direction, we construct HM-World, the first large-scale video dataset dedicated to hybrid memory. It features 59K high-fidelity clips with decoupled camera and subject trajectories, encompassing 17 diverse scenes, 49 distinct subjects, and meticulously designed exit-entry events to rigorously evaluate hybrid coherence. Furthermore, we propose HyDRA, a specialized memory architecture that compresses memory into tokens and utilizes a spatiotemporal relevance-driven retrieval mechanism. By selectively attending to relevant motion cues, HyDRA effectively preserves the identity and motion of hidden subjects. Extensive experiments on HM-World demonstrate that our method significantly outperforms state-of-the-art approaches in both dynamic subject consistency and overall generation quality.

---

## 3. A Wireless World Model for AI-Native 6G Networks

**Authors:** Ziqi Chen, Yi Ren, Yixuan Huang, ..., Yifan Li, Liang Xia
**arXiv:** [2603.25216](https://arxiv.org/abs/2603.25216)
**Categories:** Networking and Internet Architecture (cs.NI); Artificial Intelligence (cs.AI); Signal Processing (eess.SP)

Integrating AI into the physical layer is a cornerstone of 6G networks. However, current data-driven approaches struggle to generalize across dynamic environments because they lack an intrinsic understanding of electromagnetic wave propagation. We introduce the Wireless World Model (WWM), a multi-modal foundation framework predicting the spatiotemporal evolution of wireless channels by internalizing the causal relationship between 3D geometry and signal dynamics. Pre-trained on a massive ray-traced multi-modal dataset, WWM overcomes the data authenticity gap, further validated under real-world measurement data. Using a joint-embedding predictive architecture with a multi-modal mixture-of-experts Transformer, WWM fuses channel state information, 3D point clouds, and user trajectories into a unified representation. Across the five key downstream tasks supported by WWM, it achieves remarkable performance in seen environments, unseen generalization scenarios, and real-world measurements, consistently outperforming SOTA uni-modal foundation models and task-specific models. This paves the way for physics-aware 6G intelligence that adapts to the physical world.

---

## 4. Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning

**Authors:** Jai Bardhan, Patrik Drozdik, Josef Sivic, Vladimir Petrik
**arXiv:** [2603.25685](https://arxiv.org/abs/2603.25685)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Action-conditioned robot world models generate future video frames of the manipulated scene given a robot action sequence, offering a promising alternative for simulating tasks that are difficult to model with traditional physics engines. However, these models are optimized for short-term prediction and break down when deployed autoregressively: each predicted clip feeds back as context for the next, causing errors to compound and visual quality to rapidly degrade. We address this through the following contributions. First, we introduce a reinforcement learning (RL) post-training scheme that trains the world model on its own autoregressive rollouts rather than on ground-truth histories. We achieve this by adapting a recent contrastive RL objective for diffusion models to our setting and show that its convergence guarantees carry over exactly. Second, we design a training protocol that generates and compares multiple candidate variable-length futures from the same rollout state, reinforcing higher-fidelity predictions over lower-fidelity ones. Third, we develop efficient, multi-view visual fidelity rewards that combine complementary perceptual metrics across camera views and are aggregated at the clip level for dense, low-variance training signal. Fourth, we show that our approach establishes a new state-of-the-art for rollout fidelity on the DROID dataset, outperforming the strongest baseline on all metrics (e.g., LPIPS reduced by 14% on external cameras, SSIM improved by 9.1% on the wrist camera), winning 98% of paired comparisons, and achieving an 80% preference rate in a blind human study.

---

## 5. Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance

**Authors:** Wenxuan Song, Jiayi Chen, Shuai Chen, ..., Yan Wang, Haoang Li
**arXiv:** [2603.25661](https://arxiv.org/abs/2603.25661)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary tasks. To simultaneously achieve the enhanced capabilities of auxiliary training with the simplicity of standard SFT, we decouple the two objectives of auxiliary task training within the parameter space, namely, enhancing general capabilities and fitting task-specific action distributions. To deliver this goal, we only need to train the model to converge on a small-scale task set using two distinct training strategies. The difference between the resulting model parameters can then be interpreted as capability vectors provided by auxiliary tasks. These vectors are then merged with pretrained parameters to form a capability-enhanced meta model. Moreover, when standard SFT is augmented with a lightweight orthogonal regularization loss, the merged model attains performance comparable to auxiliary finetuned baselines with reduced computational overhead. Experimental results demonstrate that this approach is highly effective across diverse robot tasks. Project page: this https URL

---

## 6. MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation

**Authors:** Yang Liu, Pengxiang Ding, Tengyue Jiang, ..., Jinkui Shi, Donglin Wang
**arXiv:** [2603.25406](https://arxiv.org/abs/2603.25406)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models aim to control robots for manipulation from visual observations and natural-language instructions. However, existing hierarchical and autoregressive paradigms often introduce architectural overhead, suffer from temporal inconsistency and long-horizon error accumulation, and lack a mechanism to capture environment dynamics without extra modules. To this end, we present MMaDA-VLA, a fully native pre-trained large diffusion VLA model that unifies multi-modal understanding and generation in a single framework. Our key idea is a native discrete diffusion formulation that embeds language, images, and continuous robot controls into one discrete token space and trains a single backbone with masked token denoising to jointly generate a future goal observation and an action chunk in parallel. Iterative denoising enables global, order-free refinement, improving long-horizon consistency while grounding actions in predicted future visual outcomes without auxiliary world models. Experiments across simulation benchmarks and real-world tasks show state-of-the-art performance, achieving 98.0% average success on LIBERO and 4.78 average length on CALVIN.

---

## 7. ThermoAct:Thermal-Aware Vision-Language-Action Models for Robotic Perception and Decision-Making

**Authors:** Young-Chae Son, Dae-Kwan Ko, Yoon-Ji Choi, Soo-Chul Lim
**arXiv:** [2603.25044](https://arxiv.org/abs/2603.25044)
**Categories:** Robotics (cs.RO)

In recent human-robot collaboration environments, there is a growing focus on integrating diverse sensor data beyond visual information to enable safer and more intelligent task execution. Although thermal data can be crucial for enhancing robot safety and operational efficiency, its integration has been relatively overlooked in prior research. This paper proposes a novel Vision-Language-Action (VLA) framework that incorporates thermal information for robot task execution. The proposed system leverages a Vision-Language Model (VLM) as a high-level planner to interpret complex natural language commands and decompose them into simpler sub-tasks. This approach facilitates efficient data collection and robust reasoning for complex operations. Unlike conventional methods that rely solely on visual data, our approach integrates thermal information, enabling the robot to perceive physical properties and proactively ensure environmental safety. Experimental results from real-world task scenarios validate the feasibility of our proposed framework, suggesting its potential to enhance task success rates and safety compared to existing vision-based systems.

---

## 8. $π$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation

**Authors:** Johnathan Tucker, Denis Liu, Aiden Swann, ..., Quan Vuong, Mac Schwager
**arXiv:** [2603.25038](https://arxiv.org/abs/2603.25038)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models such as $\pi_0$ have demonstrated remarkable generalization across diverse fixed-base manipulators. However, transferring these foundation models to aerial platforms remains an open challenge due to the fundamental mismatch between the quasi-static dynamics of fixed-base arms and the underactuated, highly dynamic nature of flight. In this work, we introduce AirVLA, a system that investigates the transferability of manipulation-pretrained VLAs to aerial pick-and-place tasks. We find that while visual representations transfer effectively, the specific control dynamics required for flight do not. To bridge this "dynamics gap" without retraining the foundation model, we introduce a Payload-Aware Guidance mechanism that injects payload constraints directly into the policy's flow-matching sampling process. To overcome data scarcity, we further utilize a Gaussian Splatting pipeline to synthesize navigation training data. We evaluate our method through a cumulative 460 real-world experiments which demonstrate that this synthetic data is a key enabler of performance, unlocking 100% success in navigation tasks where directly fine-tuning on teleoperation data alone attains 81% success. Our inference-time intervention, Payload-Aware Guidance, increases real-world pick-and-place task success from 23% to 50%. Finally, we evaluate the model on a long-horizon compositional task, achieving a 62% overall success rate. These results suggest that pre-trained manipulation VLAs, with appropriate data augmentation and physics-informed guidance, can transfer to aerial manipulation and navigation, as well as the composition of these tasks.

---

## 9. SABER: A Stealthy Agentic Black-Box Attack Framework for Vision-Language-Action Models

**Authors:** Xiyang Wu, Guangyao Shi, Qingzi Wang, ..., Amrit Singh Bedi, Dinesh Manocha
**arXiv:** [2603.24935](https://arxiv.org/abs/2603.24935)
**Categories:** Robotics (cs.RO)

Vision-language-action (VLA) models enable robots to follow natural-language instructions grounded in visual observations, but the instruction channel also introduces a critical vulnerability: small textual perturbations can alter downstream robot behavior. Systematic robustness evaluation therefore requires a black-box attacker that can generate minimal yet effective instruction edits across diverse VLA models. To this end, we present SABER, an agent-centric approach for automatically generating instruction-based adversarial attacks on VLA models under bounded edit budgets. SABER uses a GRPO-trained ReAct attacker to generate small, plausible adversarial instruction edits using character-, token-, and prompt-level tools under a bounded edit budget that induces targeted behavioral degradation, including task failure, unnecessarily long execution, and increased constraint violations. On the LIBERO benchmark across six state-of-the-art VLA models, SABER reduces task success by 20.6%, increases action-sequence length by 55%, and raises constraint violations by 33%, while requiring 21.1% fewer tool calls and 54.7% fewer character edits than strong GPT-based baselines. These results show that small, plausible instruction edits are sufficient to substantially degrade robot execution, and that an agentic black-box pipeline offers a practical, scalable, and adaptive approach for red-teaming robotic foundation models.

---

## 10. LaMP: Learning Vision-Language-Action Policies with 3D Scene Flow as Latent Motion Prior

**Authors:** Xinkai Wang, Chenyi Wang, Yifu Xu, ..., Cewu Lu, Lixin Yang
**arXiv:** [2603.25399](https://arxiv.org/abs/2603.25399)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation. Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly. This implicit learning strategy degrades under unfamiliar spatial dynamics. LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention. Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction. We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments. LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7% gain over the strongest prior baseline. Our project page is available at this https URL.

---

## 11. Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models

**Authors:** Peiju Liu, Jinming Liu, Xipeng Qiu, Xuanjing Huang
**arXiv:** [2603.24941](https://arxiv.org/abs/2603.24941)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Computation and Language (cs.CL)

Vision-Language-Action (VLA) models excel in robotic manipulation but suffer from significant inference latency due to processing dense visual tokens. Existing token reduction methods predominantly rely on attention magnitude as a static selection. In this work, we challenge this assumption, revealing that high-attention tokens are task-dependent and can even degrade policy performance. To address this, we introduce \textbf{TIES} (\textbf{T}au-guided \textbf{I}nter-layer \textbf{E}fficient \textbf{S}election), a dynamic framework guided by inter-layer token ranking consistency. By adaptively balancing attention magnitude with ranking consistency, TIES ensures robust token selection without requiring additional training. On the CogACT + SIMPLER benchmark, TIES improves average success rates by 6\% while reducing token usage by 78\%, and demonstrate strong generalization across diverse decoders and benchmarks.

---

## 12. Modernising Reinforcement Learning-Based Navigation for Embodied Semantic Scene Graph Generation

**Authors:** Roman Kueble, Marco Hueller, Mrunmai Phatak, Rainer Lienhart, Joerg Haehner
**arXiv:** [2603.25415](https://arxiv.org/abs/2603.25415)
**Categories:** Artificial Intelligence (cs.AI); Robotics (cs.RO)

Semantic world models enable embodied agents to reason about objects, relations, and spatial context beyond purely geometric representations. In Organic Computing, such models are a key enabler for objective-driven self-adaptation under uncertainty and resource constraints. The core challenge is to acquire observations maximising model quality and downstream usefulness within a limited action budget.
Semantic scene graphs (SSGs) provide a structured and compact representation for this purpose. However, constructing them within a finite action horizon requires exploration strategies that trade off information gain against navigation cost and decide when additional actions yield diminishing returns.
This work presents a modular navigation component for Embodied Semantic Scene Graph Generation and modernises its decision-making by replacing the policy-optimisation method and revisiting the discrete action formulation. We study compact and finer-grained, larger discrete motion sets and compare a single-head policy over atomic actions with a factorised multi-head policy over action components. We evaluate curriculum learning and optional depth-based collision supervision, and assess SSG completeness, execution safety, and navigation behaviour.
Results show that replacing the optimisation algorithm alone improves SSG completeness by 21\% relative to the baseline under identical reward shaping. Depth mainly affects execution safety (collision-free motion), while completeness remains largely unchanged. Combining modern optimisation with a finer-grained, factorised action representation yields the strongest overall completeness--efficiency trade-off.

---

## 13. Vega: Learning to Drive with Natural Language Instructions

**Authors:** Sicheng Zuo, Yuxuan Li, Wenzhao Zheng, ..., Jie Zhou, Jiwen Lu
**arXiv:** [2603.25741](https://arxiv.org/abs/2603.25741)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

Vision-language-action models have reshaped autonomous driving to incorporate languages into the decision-making process. However, most existing pipelines only utilize the language modality for scene descriptions or reasoning and lack the flexibility to follow diverse user instructions for personalized driving. To address this, we first construct a large-scale driving dataset (InstructScene) containing around 100,000 scenes annotated with diverse driving instructions with the corresponding trajectories. We then propose a unified Vision-Language-World-Action model, Vega, for instruction-based generation and planning. We employ the autoregressive paradigm to process visual inputs (vision) and language instructions (language) and the diffusion paradigm to generate future predictions (world modeling) and trajectories (action). We perform joint attention to enable interactions between the modalities and use individual projection layers for different modalities for more capabilities. Extensive experiments demonstrate that our method not only achieves superior planning performance but also exhibits strong instruction-following abilities, paving the way for more intelligent and personalized driving systems.

---

## 14. LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation

**Authors:** Motonari Kambara, Koki Seno, Tomoya Kaichi, Yanan Wang, Komei Sugiura
**arXiv:** [2603.25481](https://arxiv.org/abs/2603.25481)
**Categories:** Robotics (cs.RO)

We address language-conditioned robotic manipulation using flow-based trajectory generation, which enables training on human and web videos of object manipulation and requires only minimal embodiment-specific data. This task is challenging, as object trajectory generation from pre-manipulation images and natural language instructions requires appropriate instruction-flow alignment. To tackle this challenge, we propose the flow-based Language Instruction-guided open-Loop ACtion generator (LILAC). This flow-based Vision-Language-Action model (VLA) generates object-centric 2D optical flow from an RGB image and a natural language instruction, and converts the flow into a 6-DoF manipulator trajectory. LILAC incorporates two key components: Semantic Alignment Loss, which strengthens language conditioning to generate instruction-aligned optical flow, and Prompt-Conditioned Cross-Modal Adapter, which aligns learned visual prompts with image and text features to provide rich cues for flow generation. Experimentally, our method outperformed existing approaches in generated flow quality across multiple benchmarks. Furthermore, in physical object manipulation experiments using free-form instructions, LILAC demonstrated a superior task success rate compared to existing methods. The project page is available at this https URL.

---
