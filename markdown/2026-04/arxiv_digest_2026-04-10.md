# arXiv Daily Digest — 2026-04-10

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 8

---

## 1. Grounding Clinical AI Competency in Human Cognition Through the Clinical World Model and Skill-Mix Framework

**Authors:** Seyed Amir Ahmad Safavi-Naini, Elahe Meftah, Josh Mohess, ..., Ali Soroush, Isaac Shiri
**arXiv:** [2604.08226](https://arxiv.org/abs/2604.08226)
**Categories:** Artificial Intelligence (cs.AI); Human-Computer Interaction (cs.HC); Systems and Control (eess.SY)

The competency of any intelligent agent is bounded by its formal account of the world in which it operates. Clinical AI lacks such an account. Existing frameworks address evaluation, regulation, or system design in isolation, without a shared model of the clinical world to connect them. We introduce the Clinical World Model, a framework that formalizes care as a tripartite interaction among Patient, Provider, and Ecosystem. To formalize how any agent, whether human or artificial, transforms information into clinical action, we develop parallel decision-making architectures for providers, patients, and AI agents, grounded in validated principles of clinical cognition.
The Clinical AI Skill-Mix operationalizes competency through eight dimensions. Five define the clinical competency space (condition, phase, care setting, provider role, and task) and three specify how AI engages human reasoning (assigned authority, agent facing, and anchoring layer). The combinatorial product of these dimensions yields a space of billions of distinct competency coordinates. A central structural implication is that validation within one coordinate provides minimal evidence for performance in another, rendering the competency space irreducible. The framework supplies a common grammar through which clinical AI can be specified, evaluated, and bounded across stakeholders. By making this structure explicit, the Clinical World Model reframes the field's central question from whether AI works to in which competency coordinates reliability has been demonstrated, and for whom.

---

## 2. WorldMAP: Bootstrapping Vision-Language Navigation Trajectory Prediction with Generative World Models

**Authors:** Hongjin Chen, Shangyun Jiang, Tonghua Su, ..., Yong Li, Zhibo Chen
**arXiv:** [2604.07957](https://arxiv.org/abs/2604.07957)
**Categories:** Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision-language models (VLMs) and generative world models are opening new opportunities for embodied navigation. VLMs are increasingly used as direct planners or trajectory predictors, while world models support look-ahead reasoning by imagining future views. Yet predicting a reliable trajectory from a single egocentric observation remains challenging. Current VLMs often generate unstable trajectories, and world models, though able to synthesize plausible futures, do not directly provide the grounded signals needed for navigation learning. This raises a central question: how can generated futures be turned into supervision for grounded trajectory prediction? We present WorldMAP, a teacher--student framework that converts world-model-generated futures into persistent semantic-spatial structure and planning-derived supervision. Its world-model-driven teacher builds semantic-spatial memory from generated videos, grounds task-relevant targets and obstacles, and produces trajectory pseudo-labels through explicit planning. A lightweight student with a multi-hypothesis trajectory head is then trained to predict navigation trajectories directly from vision-language inputs. On Target-Bench, WorldMAP achieves the best ADE and FDE among compared methods, reducing ADE by 18.0% and FDE by 42.1% relative to the best competing baseline, while lifting a small open-source VLM to DTW performance competitive with proprietary models. More broadly, the results suggest that, in embodied navigation, the value of world models may lie less in supplying action-ready imagined evidence than in synthesizing structured supervision for navigation learning.

---

## 3. CausalVAE as a Plug-in for World Models: Towards Reliable Counterfactual Dynamics

**Authors:** Ziyi Ding, Xianxin Lai, Weiyu Chen, Xiao-Ping Zhang, Jiayu Chen
**arXiv:** [2604.07712](https://arxiv.org/abs/2604.07712)
**Categories:** Machine Learning (cs.LG)

In this work, CausalVAE is introduced as a plug-in structural module for latent world models and is attached to diverse encoder-transition backbones. Across the reported benchmarks, competitive factual prediction is preserved and intervention-aware counterfactual retrieval is improved after the plug-in is added, suggesting stronger robustness under distribution shift and interventions. The largest gains are observed on the Physics benchmark: when averaged over 8 paired baselines, CF-H@1 is improved by +102.5%. In a representative GNN-NLL setting on Physics, CF-H@1 is increased from 11.0 to 41.0 (+272.7%). Through causal analysis, learned structural dependencies are shown to recover meaningful first-order physical interaction trends, supporting the interpretability of the learned latent causal structure.

---

## 4. Event-Centric World Modeling with Memory-Augmented Retrieval for Embodied Decision-Making

**Authors:** Fan Zhaowen
**arXiv:** [2604.07392](https://arxiv.org/abs/2604.07392)
**Categories:** Machine Learning (cs.LG); Information Retrieval (cs.IR); Robotics (cs.RO)

Autonomous agents operating in dynamic and safety-critical environments require decision-making frameworks that are both computationally efficient and physically grounded. However, many existing approaches rely on end-to-end learning, which often lacks interpretability and explicit mechanisms for ensuring consistency with physical constraints. In this work, we propose an event-centric world modeling framework with memory-augmented retrieval for embodied decision-making. The framework represents the environment as a structured set of semantic events, which are encoded into a permutation-invariant latent representation. Decision-making is performed via retrieval over a knowledge bank of prior experiences, where each entry associates an event representation with a corresponding maneuver. The final action is computed as a weighted combination of retrieved solutions, providing a transparent link between decision and stored experiences. The proposed design enables structured abstraction of dynamic environments and supports interpretable decision-making through case-based reasoning. In addition, incorporating physics-informed knowledge into the retrieval process encourages the selection of maneuvers that are consistent with observed system dynamics. Experimental evaluation in UAV flight scenarios demonstrates that the framework operates within real-time control constraints while maintaining interpretable and consistent behavior.

---

## 5. MotionScape: A Large-Scale Real-World Highly Dynamic UAV Video Dataset for World Models

**Authors:** Zile Guo, Zhan Chen, Enze Zhu, ..., Xiaoxuan Liu, Lei Wang
**arXiv:** [2604.07991](https://arxiv.org/abs/2604.07991)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Multimedia (cs.MM)

Recent advances in world models have demonstrated strong capabilities in simulating physical reality, making them an increasingly important foundation for embodied intelligence. For UAV agents in particular, accurate prediction of complex 3D dynamics is essential for autonomous navigation and robust decision-making in unconstrained environments. However, under the highly dynamic camera trajectories typical of UAV views, existing world models often struggle to maintain spatiotemporal physical consistency. A key reason lies in the distribution bias of current training data: most existing datasets exhibit restricted 2.5D motion patterns, such as ground-constrained autonomous driving scenes or relatively smooth human-centric egocentric videos, and therefore lack realistic high-dynamic 6-DoF UAV motion priors. To address this gap, we present MotionScape, a large-scale real-world UAV-view video dataset with highly dynamic motion for world modeling. MotionScape contains over 30 hours of 4K UAV-view videos, totaling more than 4.5M frames. This novel dataset features semantically and geometrically aligned training samples, where diverse real-world UAV videos are tightly coupled with accurate 6-DoF camera trajectories and fine-grained natural language descriptions. To build the dataset, we develop an automated multi-stage processing pipeline that integrates CLIP-based relevance filtering, temporal segmentation, robust visual SLAM for trajectory recovery, and large-language-model-driven semantic annotation. Extensive experiments show that incorporating such semantically and geometrically aligned annotations effectively improves the ability of existing world models to simulate complex 3D dynamics and handle large viewpoint shifts, thereby benefiting decision-making and planning for UAV agents in complex environments. The dataset is publicly available at this https URL

---

## 6. ViVa: A Video-Generative Value Model for Robot Reinforcement Learning

**Authors:** Jindi Lv, Hao Li, Jie Li, ..., Jiancheng Lv, Guan Huang
**arXiv:** [2604.08168](https://arxiv.org/abs/2604.08168)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-language-action (VLA) models have advanced robot manipulation through large-scale pretraining, but real-world deployment remains challenging due to partial observability and delayed feedback. Reinforcement learning addresses this via value functions, which assess task progress and guide policy improvement. However, existing value models built on vision-language models (VLMs) struggle to capture temporal dynamics, undermining reliable value estimation in long-horizon tasks. In this paper, we propose ViVa, a video-generative value model that repurposes a pretrained video generator for value estimation. Taking the current observation and robot proprioception as input, ViVa jointly predicts future proprioception and a scalar value for the current state. By leveraging the spatiotemporal priors of a pretrained video generator, our approach grounds value estimation in anticipated embodiment dynamics, moving beyond static snapshots to intrinsically couple value with foresight. Integrated into RECAP, ViVa delivers substantial improvements on real-world box assembly. Qualitative analysis across all three tasks confirms that ViVa produces more reliable value signals, accurately reflecting task progress. By leveraging spatiotemporal priors from video corpora, ViVa also generalizes to novel objects, highlighting the promise of video-generative models for value estimation.

---

## 7. GIRL: Generative Imagination Reinforcement Learning via Information-Theoretic Hallucination Control

**Authors:** Prakul Sunil Hiremath
**arXiv:** [2604.07426](https://arxiv.org/abs/2604.07426)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Model-based reinforcement learning (MBRL) improves sample efficiency by optimizing policies inside imagined rollouts, but long-horizon planning degrades when model errors compound and imagined trajectories drift off the training manifold. We introduce GIRL (Generative Imagination Reinforcement Learning), a latent world-model framework that addresses this failure mode with two key components. First, a cross-modal grounding signal derived from a frozen foundation model (DINOv2) anchors the latent transition prior to a semantically consistent embedding space, penalizing inconsistent or implausible predictions. Second, an uncertainty-adaptive trust-region bottleneck interprets the KL regularizer as the Lagrange multiplier of a constrained optimization problem, restricting imagination drift within a learned region calibrated by Expected Information Gain and a Relative Performance Loss signal.
We re-derive a value-gap bound using the Performance Difference Lemma and Integral Probability Metrics, yielding a bound that remains informative as the discount factor approaches one and connects the objective to real-environment regret. Experiments across three benchmark suites, including DeepMind Control, Adroit Hand Manipulation, and Meta-World with visual distractors, show that GIRL reduces latent rollout drift by 38 to 61 percent across tasks relative to DreamerV3, improves asymptotic return, and requires fewer environment interactions on long-horizon tasks. GIRL also outperforms TD-MPC2 on sparse-reward and high-contact settings under standard evaluation metrics. A distilled-prior variant reduces inference overhead and improves computational efficiency relative to the full model.

---

## 8. HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents

**Authors:** Tencent Robotics X, HY Vision Team, Xumin Yu, ..., Linus, Shunyu Yao
**arXiv:** [2604.07430](https://arxiv.org/abs/2604.07430)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

We introduce HY-Embodied-0.5, a family of foundation models specifically designed for real-world embodied agents. To bridge the gap between general Vision-Language Models (VLMs) and the demands of embodied agents, our models are developed to enhance the core capabilities required by embodied intelligence: spatial and temporal visual perception, alongside advanced embodied reasoning for prediction, interaction, and planning. The HY-Embodied-0.5 suite comprises two primary variants: an efficient model with 2B activated parameters designed for edge deployment, and a powerful model with 32B activated parameters targeted for complex reasoning. To support the fine-grained visual perception essential for embodied tasks, we adopt a Mixture-of-Transformers (MoT) architecture to enable modality-specific computing. By incorporating latent tokens, this design effectively enhances the perceptual representation of the models. To improve reasoning capabilities, we introduce an iterative, self-evolving post-training paradigm. Furthermore, we employ on-policy distillation to transfer the advanced capabilities of the large model to the smaller variant, thereby maximizing the performance potential of the compact model. Extensive evaluations across 22 benchmarks, spanning visual perception, spatial reasoning, and embodied understanding, demonstrate the effectiveness of our approach. Our MoT-2B model outperforms similarly sized state-of-the-art models on 16 benchmarks, while the 32B variant achieves performance comparable to frontier models such as Gemini 3.0 Pro. In downstream robot control experiments, we leverage our robust VLM foundation to train an effective Vision-Language-Action (VLA) model, achieving compelling results in real-world physical evaluations. Code and models are open-sourced at this https URL.

---
