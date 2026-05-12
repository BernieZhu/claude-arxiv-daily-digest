# arXiv Daily Digest — 2026-05-11

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 14

---

## 1. Three-in-One World Model: Energy-Based Consistency, Prediction, and Counterfactual Inference for Marketing Intervention

**Authors:** Junichiro Niimi
**arXiv:** [2605.07199](https://arxiv.org/abs/2605.07199)
**Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Marketing decisions reflect the interaction of latent consumer heterogeneity, time-varying internal states, and explicit interventions, a structure that current prediction- and language-oriented models do not capture in a unified manner. We propose a Three-in-One world-model architecture in which a Deep Boltzmann Machine (DBM) learns a frozen belief representation from demographics, time, and lagged actions and outcomes, with lightweight task-specific adapters attached on top. The same belief supports three tasks within a single framework: (i) energy-based consistency evaluation through the DBM's free energy, (ii) outcome prediction through adapters, and (iii) counterfactual inference by holding the belief fixed and varying only the action input given to the adapter. Using a controlled simulation in which the latent price sensitivity, promotion responsiveness, and base preference of each consumer are known, we show that the adapters match a strong MLP baseline on visit- and purchase-AUC while recovering heterogeneous treatment effects substantially better than S-, T-, X-, and DR-learner meta-learners and a Causal Forest baseline built on the same raw features, with the largest gap on a confounded price-promotion intervention. Complementing this, free-energy clamps systematically penalize counterfactual purchase trajectories that lack prior promotional exposure, and the penalty itself depends on the latent base preference in the expected direction. These results indicate that DBM beliefs disentangle latent traits in a form that survives counterfactual queries, providing an integrated world-model substrate for marketing intervention.

---

## 2. AGWM: Affordance-Grounded World Models for Environments with Compositional Prerequisites

**Authors:** Qinshi Zhang, Weipeng Deng, Zhihan Jiang, ..., Weitao Xu, Ray LC
**arXiv:** [2605.06841](https://arxiv.org/abs/2605.06841)
**Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

In model-based learning, the agent learns behaviors by simulating trajectories based on world model predictions. Standard world models typically learn a stationary transition function that maps states and actions to next states, when an action and an outcome frequently co-occur in training data, the model tends to internalize this correlation as a general causal rule while ignoring action preconditions. In interactive environments, however, agent actions can reshape the future affordance space. At each timestep, an action may becomes executable only after its prerequisites are met, or non-executable when they are destroyed. We term such events structure-changing events (SC events). As a result, a conventional world model often fails to determine whether a given action is executable in the current state, especially in multi-step predictions. Each imagined step is conditioned on an incorrect affordance state, and therefore the prediction error compounds over the rollout horizon. In this paper, we propose AGWM (Affordance-Grounded World Model), which learns an abstract affordance structure represented as a DAG of prerequisite dependencies to explicitly track the dynamic executability of actions. Experiments on game-based simulated environments demonstrate the effectiveness of our method by achieving lower multi-step prediction error, better generalization to novel configurations, and improved interpretability.

---

## 3. One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy

**Authors:** Zuojin Tang, Shengchao Yuan, Xiaoxin Bai, ..., Gang Pan, Bin Liu
**arXiv:** [2605.07931](https://arxiv.org/abs/2605.07931)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-language-action (VLA) models increasingly rely on auxiliary world modules to plan over long horizons, yet how such modules should be parameterized on top of a pretrained VLA remains an open design question. Existing world-model-augmented VLAs typically pass the per-frame visual stream into the world module at high visual bandwidth and treat its rollout as a side product of action prediction; under a constrained adaptation budget on a frozen backbone, this leaves both the per-frame representation and the latent action coupling under-examined. We introduce OneWM-VLA, which compresses each view into a single semantic token per frame through an Adaptive Attention Pooling, and produces the resulting latent stream and the action trajectory under a single flow-matching objective rather than connecting them through a separate decoder. Empirically, we find that per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance under our setup. Trained with 14.71M LoRA parameters on a $\pi_0$ (2B) backbone, OneWM-VLA improves the average success rate from 47.9% to 61.3% on MetaWorld~MT50, reaches 95.6% on LIBERO-Long (vs.85.2% for $\pi_0$), and reaches 60.0% on the long-horizon deformable task Fold Cloth on a real Piper arm (vs.20.0% for $\pi_0$).

---

## 4. ForgeVLA: Federated Vision-Language-Action Learning without Language Annotations

**Authors:** Yuhao Zhou, Yunpeng Zhu, Yang Zhou, ..., Qing Ye, Jiancheng Lyu
**arXiv:** [2605.07474](https://arxiv.org/abs/2605.07474)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models hold great promise for general-purpose robotic intelligence, yet scaling up such models is severely bottlenecked by the high cost of acquiring annotated training data. Fortunately, vision-equipped robots deployed across various domains already produce abundant vision-action pairs that can be leveraged to scale up VLA training more efficiently. However, these raw data cannot be centrally aggregated due to various constraints and also exhibit severe heterogeneity. To address these challenges, in this paper, we propose ForgeVLA, a federated VLA training framework that learns VLA models from distributed vision-action pairs without centralizing raw data or requiring manual annotations. Specifically, each client in ForgeVLA is equipped with an embodied instruction classifier that maps vision-action pairs to a predefined instruction set, recovering the missing language modality and forming complete vision-language-action triplets. Beyond triplet construction, we also identify vision-language feature collapse as a critical challenge that has been largely overlooked in prior federated VLA research. To mitigate this issue, ForgeVLA combines a client-side contrastive planning loss with a server-side adaptive aggregation strategy to learn task-discriminative representations efficiently. Extensive experiments across multiple benchmarks show that ForgeVLA significantly outperforms other baselines, and ablation studies further validate the contribution of each component.

---

## 5. BioProVLA-Agent: An Affordable, Protocol-Driven, Vision-Enhanced VLA-Enabled Embodied Multi-Agent System with Closed-Loop-Capable Reasoning for Biological Laboratory Manipulation

**Authors:** Zhaohui Du, Zhe Wang, Hongmei Fei, ..., Quan Lu, Zhe Liu
**arXiv:** [2605.07306](https://arxiv.org/abs/2605.07306)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Biological laboratory automation can reduce repetitive manual work and improve reproducibility, but reliable embodied execution in wet-lab environments remains challenging. Protocols are often unstructured, labware is frequently transparent or reflective, and multi-step procedures require state-aware execution beyond one-shot instruction following. Existing robotic systems often rely on costly hardware, fixed workflows, dedicated instruments, or robotics-oriented interfaces. Here, we introduce BioProVLA-Agent, an affordable, protocol-driven, vision-enhanced embodied multi-agent system enabled by Vision-Language-Action (VLA) models for biological manipulation. The system uses protocols as the task interface and integrates protocol parsing, visual state verification, and embodied execution in a closed-loop workflow. A Tailored LLM Protocol Agent converts protocols into verifiable subtasks; a VLM-RAG Verification Agent assesses readiness and completion using observations, robot states, retrieved knowledge, and success/failure examples; and a VLA Embodied Agent executes verified subtasks through a lightweight policy. To improve robustness under wet-lab visual perturbations, we develop AugSmolVLA, an online augmentation strategy targeting transparent labware, reflections, illumination shifts, and overexposure. We evaluate the system on a hierarchical benchmark covering 15 atomic tasks, 6 composite workflows, and 3 bimanual tasks, including tube loading, sorting, waste disposal, cap twisting, and liquid pouring. Across normal and high-exposure settings, AugSmolVLA improves execution stability over ACT, X-VLA, and the original SmolVLA, especially for precise placement, transparent-object manipulation, composite workflows, and visually degraded scenes. These results suggest a practical route toward accessible, protocol-centered, and verification-capable embodied AI for biological manipulation.

---

## 6. Sword: Style-Robust World Models as Simulators via Dynamic Latent Bootstrapping for VLA Policy Post-Training

**Authors:** Jiaxuan Gao, Yongjian Guo, Zhong Guan, ..., Junwu Xiong, Sheng Wen
**arXiv:** [2605.07288](https://arxiv.org/abs/2605.07288)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

The integration of Vision-Language-Action (VLA) models with World Models has gained increasing attention. One representative approach treats learned World Models as generative simulators, enabling policy optimization entirely within "imagination." However, when deployed as simulators for specific environments such as the LIBERO benchmark, existing World Models often suffer from poor generalization and long-horizon error accumulation. During closed-loop rollouts, these models are highly sensitive to initial-state perturbations; minor changes in color, illumination, and other visual factors can trigger cascading hallucinations, leading to severe blurriness or overexposure. Moreover, long-horizon error accumulation further degrades the quality and fidelity of predicted future states. These issues limit the reliability of World Models as simulators. To mitigate these problems, we propose Sword, a robust World Model framework. Our method introduces Structure-Guided Style Augmentation to disentangle the visual textures of interactive environments from task-relevant dynamics, thereby improving generalization. We further propose Dynamic Latent Bootstrapping, which maintains consistency between training and inference while keeping memory consumption low. Extensive experiments on the LIBERO benchmark show that our method significantly outperforms the baseline WoVR in terms of generalization, generation quality, robustness, fidelity, and the success rate of reinforcement-learning post-training for VLA models.

---

## 7. Predictive but Not Plannable: RC-aux for Latent World Models

**Authors:** Wenyuan Li, Guang Li, Keisuke Maeda, Takahiro Ogawa, Miki Haseyama
**arXiv:** [2605.07278](https://arxiv.org/abs/2605.07278)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

A latent world model may achieve accurate short-horizon prediction while still inducing a latent space that is poorly aligned with planning. A key issue is spatiotemporal mismatch: these models are often trained with local predictive supervision, but deployed for long-horizon goal-directed search in latent spaces where Euclidean distance may not reflect what is reachable within a finite action budget. We present the Reachability-Correction auxiliary objective (RC-aux), a lightweight correction for this mismatch in reconstruction-free latent world models. RC-aux keeps the world-model backbone unchanged and adds planning-aligned supervision along two axes. Along the time axis, multi-horizon open-loop prediction trains the model beyond one-step consistency. Along the space axis, budget-conditioned reachability supervision, together with temporal hard negatives, encourages the latent space to distinguish states that are eventually reachable from those reachable within the current planning horizon. At test time, the learned reachability signal can also be used by a reachability-aware planner to favor trajectories that are both goal-directed and attainable under the available budget. We instantiate RC-aux on LeWorldModel and evaluate it under both continuation-training and matched-from-scratch settings. Across goal-conditioned pixel-control tasks and a LIBERO-Goal extension, RC-aux improves LeWM-style planning with modest additional cost. These results suggest that planning with latent world models depends not only on predictive accuracy, but also on whether the learned representation encodes the temporal and geometric structure required by downstream search. The code is available at this https URL.

---

## 8. Learning Visual Feature-Based World Models via Residual Latent Action

**Authors:** Xinyu Zhang, Zhengtong Xu, Yutian Tao, ..., Yu She, Abdeslam Boularias
**arXiv:** [2605.07079](https://arxiv.org/abs/2605.07079)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG); Robotics (cs.RO)

World models predict future transitions from observations and actions. Existing works predominantly focus on image generation only. Visual feature-based world models, on the other hand, predict future visual features instead of raw video pixels, offering a promising alternative that is more efficient and less prone to hallucination. However, current feature-based approaches rely on direct regression, which leads to blurry or collapsed predictions in complex interactions, while generative modeling in high-dimensional feature spaces still remains challenging. In this work, we discover that a new type of latent action representation, which we refer to as *Residual Latent Action* (RLA), can be easily learned from DINO residuals. We also show that RLA is predictive, generalizable, and encodes temporal progression. Building on RLA, we propose *RLA World Model* (RLA-WM), which predicts RLA values via flow matching. RLA-WM outperforms both state-of-the-art feature-based and video-diffusion world models on simulation and real-world datasets, while being orders of magnitude faster than video diffusion. Furthermore, we develop two robot learning techniques that use RLA-WM to improve policy learning. The first one is a minimalist world action model with RLA that learns from actionless demonstration videos. The second one is the first visual RL framework trained entirely inside a world model learned from offline videos only, using a video-aligned reward and no online interactions or handcrafted rewards. Project page: this https URL

---

## 9. NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models

**Authors:** Wen Huang, Haoran Sun, Yongjian Guo, ..., Shuai Di, Junwu Xiong
**arXiv:** [2605.07794](https://arxiv.org/abs/2605.07794)
**Categories:** Robotics (cs.RO)

World Action Models (WAMs) are an emerging family of policies that tie robot action generation to future-observation modeling. In this work, we focus on the joint video--action modeling paradigm, where actions and imagined future observations are co-generated along a shared denoising or flow trajectory, so that perception, prediction, and control are coupled within one generative process. Existing WAMs typically realize this paradigm with a Mixture-of-Transformers (MoT), where video and action tokens interact through shared self-attention. This architecture can in principle assign a separate timestep $t_f$ to each predicted latent frame, yet current systems collapse this degree of freedom onto a single shared scalar $t$. Under the noise-as-masking view of Diffusion Forcing, this shared schedule imposes the unjustified prior that every predicted latent is equally reliable for action generation. We instead view the per-latent schedule as a \emph{learnable information-gating policy}: by changing a latent frame's noise level, the policy modulates the reliability of its Key/Value contribution to the action tokens. We propose \textbf{NoiseGate}, which combines independent per-latent timestep sampling during backbone training, a lightweight Gating Policy Network that emits per-latent time increments during denoising, and task-reward optimization that trains the schedule policy without hand-crafted shape priors. Built on a joint video--action MoT backbone, NoiseGate delivers consistent gains on diverse RoboTwin random-scene manipulation tasks.

---

## 10. Is the Future Compatible? Diagnosing Dynamic Consistency in World Action Models

**Authors:** Bo-Kai Ruan, Teng-Fang Hsiao, Ling Lo, Hong-Han Shuai
**arXiv:** [2605.07514](https://arxiv.org/abs/2605.07514)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

World Action Models (WAMs) enable decision-making through imagined rollouts by predicting future observations and actions. However, the reliability of these imagined futures remains under-examined: is a generated future merely visually plausible, or is it dynamically compatible with the action sequence it claims to model? In this work, we identify action-state consistency, the alignment between predicted actions and induced state transitions, as a missing reliability axis for WAMs. Through a systematic study across representative joint-prediction and inverse-dynamics models, we find that action-state consistency systematically separates successful and failed rollouts across many tasks and follows similar success-failure trends as learned value estimates. These results suggest that consistency captures decision-relevant structure beyond visual realism. We further identify background collapse as an important boundary condition, where low-dynamics failed trajectories can become deceptively consistent because static futures are easier to predict. Building on these findings, we introduce a value-free consensus strategy for test-time selection, which ranks candidate rollouts by agreement among predicted futures. This strategy improves success rates on RoboCasa and RoboTwin 2.0 without additional training or reward modeling. Taken together, our findings establish action-state consistency as both a diagnostic tool for evaluating WAM reliability and a practical signal for value-free planning.

---

## 11. AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models

**Authors:** Xiaoqi Li, Muhe Cai, Jiadong Xu, ..., Guangrui Ren, Hao Dong
**arXiv:** [2605.07308](https://arxiv.org/abs/2605.07308)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have significantly advanced the capabilities of robotic agents in executing diverse tasks; however, they still face challenges in contact-rich manipulation scenarios that require precise physical interactions. To address this limitation, recent studies have attempted to incorporate tactile signals during downstream tasks, enabling pretrained VLAs to interpret tactile feedback. Nevertheless, introducing new modalities during finetuning, which are rarely present in the pretrain stage, may disrupt the pretrained capabilities of VLAs. In addition, the inherently slow inference speed of VLAs hampers real-time responsiveness and limits the effective utilization of tactile feedback for action adjustment. To overcome these challenges, we propose Adaptive Tactile Vision-Language-Action (AT-VLA), which introduces a novel Adaptive Tactile Injection mechanism. This mechanism dynamically determines the appropriate timing and locations for tactile injection, incorporating only when it significantly contributes to action generation, thereby minimizing interference with pretrained representations. Furthermore, to enable rapid and accurate tactile responses, we propose a Tactile Reaction Dual-Stream mechanism, which decouples sensory processing into a slow visual-language stream for low-frequency perceptual reasoning and a fast tactile control stream for high-frequency physical interaction understanding, achieving real-time close-loop responses within 0.04 s. Real-world experiments thoroughly validate the effectiveness of AT-VLA in contact-rich manipulation tasks. The project page is available at: this https URL.

---

## 12. ST-Gen4D: Embedding 4D Spatiotemporal Cognition into World Model for 4D Generation

**Authors:** Haonan Wang, Hanyu Zhou, Tao Gu, Luxin Yan
**arXiv:** [2605.07390](https://arxiv.org/abs/2605.07390)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Generative models have achieved success in producing apparently coherent 2D videos, but remain challenging in the physical world due to lack of 4D spatiotemporal scale. Typically, existing 4D generative models directly embed macro scale constraints to enhance overall spatiotemporal consistency. However, these methods only ensure global appearance coherence and fail to reveal the local dynamics of the physical world. Our insight is that global appearance structure and local dynamic topology empower 4D spatiotemporal cognition, thereby enabling 4D generation with spatiotemporal regularities. In this work, we propose ST-Gen4D, a 4D generation framework with 4D spatiotemporal cognition-based world model. Our model is guided by four key designs: 1) Spatiotemporal representation. We encode various modalities into multiple representations as a feature basis. 2) Spatiotemporal cognition. We sculpture these representations into global appearance graph and local dynamic graph, and fuse them via semantic-bridged spatiotemporal fusion to obtain a 4D cognition graph. 3) Spatiotemporal reasoning. We utilize a world model to derive future state based on the 4D cognition. 4) Spatiotemporal generation. We leverage the derived cognition as condition to guide latent diffusion for 4D Gaussian generation. By deeply integrating 4D intrinsic cognition with generative priors, our model guarantees the structural rationality and topological consistency of 4D generation. Moreover, we propose ST-4D datasets by aggregating public 4D datasets and self-built subset. Extensive experiments demonstrate the superiority of our ST-Gen4D across 3D and 4D generation tasks.

---

## 13. GEM: Generating LiDAR World Model via Deformable Mamba

**Authors:** Yang Wu, Zhaojiang Liu, Qiang Meng, ..., Jian Yang, Jin Xie
**arXiv:** [2605.07326](https://arxiv.org/abs/2605.07326)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

World models, which simulate environmental dynamics and generate sensor observations, are gaining increasing attention in autonomous driving. However, progress in LiDAR-based world models has lagged behind those built on camera videos or occupancy data, primarily due to two core challenges: the inherent disorder of LiDAR point clouds and the difficulty of distinguishing dynamic objects from static structures. To address these issues, we propose GEM: a Generative LiDAR world model that leverages deformable mamba architecture, significantly improving fidelity and imaginative capability. Specifically, leveraging the structural similarity between sequential laser scanning and Mamba's processing mechanism, we first tokenize LiDAR sweeps into compact representations via a custom LiDAR scene tokenizer. After unsupervised disentanglement of tokenized features via a dynamic-static separator, a tri-path deformable Mamba is introduced to perform selective scanning and adaptive gating fusion over the disentangled features, leading to enhanced spatial-temporal understanding of the world evolution. Optionally, a planner and a BEV layout controller can be integrated to explore the model's capability for autonomous rollout and its potential to generate ``what-if" scenarios. Extensive experiments show that GEM achieves state-of-the-art performances across diverse benchmarks and evaluation settings, demonstrating its superiority and effectiveness. Project page: this https URL.

---

## 14. See Tomorrow, Act Today: Foresight-Driven Autonomous Driving

**Authors:** Bozhou Zhang, Nan Song, Yuang Wang, ..., Xiatian Zhu, Li Zhang
**arXiv:** [2605.07195](https://arxiv.org/abs/2605.07195)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Current end-to-end autonomous driving planners are fundamentally reactive: they condition on historical and present observations to predict future actions. We argue that autonomous agents should instead imagine future scenes before deciding, just as human drivers mentally simulate ``what will happen next" before acting. We introduce ForeSight, a foundation world model centric planning framework that reframes autonomous driving as anticipatory decision-making. Rather than treating world models as auxiliary components, ForeSight makes future scene imagination the primary driver of action prediction. Our approach operates in two stages: (1) generating plausible future visual worlds via a pretrained world model, and (2) planning actions conditioned on these imagined futures. This paradigm shift from ``what should I do now?" to ``what will happen, and how should I respond?" enables genuinely anticipatory rather than reactive planning. By grounding decisions in anticipated contexts rather than present observations alone, ForeSight navigates dynamic, interactive scenarios more effectively. Extensive experiments on NAVSIM and nuScenes demonstrate that explicit future imagination significantly outperforms previous state-of-the-art alternatives, validating our foresight-driven approach.

---
