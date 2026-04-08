# arXiv Daily Digest — 2026-04-07

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 7

---

## 1. VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models

**Authors:** Ravi Ranjan, Agoritsa Polyzou
**arXiv:** [2604.03956](https://arxiv.org/abs/2604.03956)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-language-action (VLA) models are emerging as embodied foundation models for robotic manipulation, but their deployment introduces a new unlearning challenge: removing unsafe, spurious, or privacy-sensitive behaviors without degrading perception, language grounding, and action control. In OpenVLA-style policies, behavior is produced through a fused visual encoder, a cross-modal projector, and a language backbone that predicts tokenized robot actions, so undesirable knowledge can be distributed across perception, alignment, and reasoning/action layers rather than confined to a single module. Consequently, partial unlearning applied only to the vision stack or only to the language backbone is often insufficient, while conventional unlearning baselines designed for standalone vision or language models may leave residual forgetting or incur unnecessary utility loss in embodied settings. We propose VLA-Forget, a hybrid unlearning framework that combines ratio-aware selective editing for perception and cross-modal specificity with layer-selective reasoning/action unlearning for utility-preserving forgetting. VLA-Forget jointly optimizes three objectives: targeted forgetting, perceptual preservation, and reasoning retention, through staged updates over the visual encoder, projector, and upper action-generating transformer blocks. Across forget-set behavior probes and retain-task evaluations, VLA-Forget improves forgetting efficacy by 10%, preserves perceptual specificity by 22%, retains reasoning and task success by 9%, and reduces post-quantization recovery by 55% relative to strong unlearning baselines.

---

## 2. Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

**Authors:** Yuanchang Liang, Xiaobo Wang, Kai Wang, ..., David Kim Huat Chua, Prahlad Vadakkepat
**arXiv:** [2604.04161](https://arxiv.org/abs/2604.04161)
**Categories:** Robotics (cs.RO)

In Vision-Language-Action (VLA) models, action chunking (i.e., executing a sequence of actions without intermediate replanning) is a key technique to improve robotic manipulation abilities. However, a large chunk size reduces the model's responsiveness to new information, while a small one increases the likelihood of mode-jumping, jerky behavior resulting from discontinuities between chunks. Therefore, selecting the optimal chunk size is an urgent demand to balance the model's reactivity and consistency. Unfortunately, a dominant trend in current VLA models is an empirical fixed chunk length at inference-time, hindering their superiority and scalability across diverse manipulation tasks. To address this issue, we propose a novel Adaptive Action Chunking (AAC) strategy, which exploits action entropy as the cue to adaptively determine the chunk size based on current predictions. Extensive experiments on a wide range of simulated and real-world robotic manipulation tasks have demonstrated that our approach substantially improves performance over the state-of-the-art alternatives. The videos and source code are publicly available at this https URL.

---

## 3. E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes

**Authors:** Jiajun Zhai, Hao Shi, Shangwei Guo, Kailun Yang, Kaiwei Wang
**arXiv:** [2604.04834](https://arxiv.org/abs/2604.04834)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Multimedia (cs.MM); Robotics (cs.RO); Image and Video Processing (eess.IV)

Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illumination settings. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing and fusion for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and blur-heavy scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms exposure), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at this https URL.

---

## 4. A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens

**Authors:** Tommie Kerssies, Gabriele Berton, Ju He, ..., Gijs Dubbelman, Liang-Chieh Chen
**arXiv:** [2604.04913](https://arxiv.org/abs/2604.04913)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Anticipating diverse future states is a central challenge in video world modeling. Discriminative world models produce a deterministic prediction that implicitly averages over possible futures, while existing generative world models remain computationally expensive. Recent work demonstrates that predicting the future in the feature space of a vision foundation model (VFM), rather than a latent space optimized for pixel reconstruction, requires significantly fewer world model parameters. However, most such approaches remain discriminative. In this work, we introduce DeltaTok, a tokenizer that encodes the VFM feature difference between consecutive frames into a single continuous "delta" token, and DeltaWorld, a generative world model operating on these tokens to efficiently generate diverse plausible futures. Delta tokens reduce video from a three-dimensional spatio-temporal representation to a one-dimensional temporal sequence, for example yielding a 1,024x token reduction with 512x512 frames. This compact representation enables tractable multi-hypothesis training, where many futures are generated in parallel and only the best is supervised. At inference, this leads to diverse predictions in a single forward pass. Experiments on dense forecasting tasks demonstrate that DeltaWorld forecasts futures that more closely align with real-world outcomes, while having over 35x fewer parameters and using 2,000x fewer FLOPs than existing generative world models. Code and weights: this https URL.

---

## 5. OpenWorldLib: A Unified Codebase and Definition of Advanced World Models

**Authors:** DataFlow Team, Bohan Zeng, Daili Hua, ..., Mike Zheng Shou, Wentao Zhang
**arXiv:** [2604.04707](https://arxiv.org/abs/2604.04707)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

World models have garnered significant attention as a promising research direction in artificial intelligence, yet a clear and unified definition remains lacking. In this paper, we introduce OpenWorldLib, a comprehensive and standardized inference framework for Advanced World Models. Drawing on the evolution of world models, we propose a clear definition: a world model is a model or framework centered on perception, equipped with interaction and long-term memory capabilities, for understanding and predicting the complex world. We further systematically categorize the essential capabilities of world models. Based on this definition, OpenWorldLib integrates models across different tasks within a unified framework, enabling efficient reuse and collaborative inference. Finally, we present additional reflections and analyses on potential future directions for world model research. Code link: this https URL

---

## 6. Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?

**Authors:** Zhongru Zhang, Chenghan Yang, Qingzhou Lu, ..., Yucheng Hu, Jianyu Chen
**arXiv:** [2604.04502](https://arxiv.org/abs/2604.04502)
**Categories:** Robotics (cs.RO)

Video generation models have advanced rapidly and are beginning to show a strong understanding of physical dynamics. In this paper, we investigate how far an advanced video generation model such as Veo-3 can support generalizable robotic manipulation. We first study a zero-shot approach in which Veo-3 predicts future image sequences from current robot observations, while an inverse dynamics model IDM recovers the corresponding robot actions. The IDM is trained solely on random-play data, requiring neither human supervision nor expert demonstrations. The key intuition is that, if a video model can generate physically plausible future motions in image space, an IDM can translate those visual trajectories into executable robot actions. We evaluate this "Veo-3+IDM" approach in both simulation and the real world using a high-dimensional dexterous hand. We find that, owing to the strong generalization capability of frontier video models, Veo-3+IDM can consistently generate approximately correct task-level trajectories. However, its low-level control accuracy remains insufficient to solve most tasks reliably. Motivated by this observation, we develop a hierarchical framework, Veo-Act, which uses Veo-3 as a high-level motion planner and a VLA policy as the low-level executor, significantly improving the instruction-following performance of a state-of-the-art vision-language-action policy. Overall, our results suggest that, as video generation models continue to improve, video models can be a valuable component for generalizable robot learning.

---

## 7. DriveVA: Video Action Models are Zero-Shot Drivers

**Authors:** Mengmeng Liu, Diankun Zhang, Jiuming Liu, ..., Francesco Nex, Hao Cheng
**arXiv:** [2604.04198](https://arxiv.org/abs/2604.04198)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Generalization is a central challenge in autonomous driving, as real-world deployment requires robust performance under unseen scenarios, sensor domains, and environmental conditions. Recent world-model-based planning methods have shown strong capabilities in scene understanding and multi-modal future prediction, yet their generalization across datasets and sensor configurations remains limited. In addition, their loosely coupled planning paradigm often leads to poor video-trajectory consistency during visual imagination. To overcome these limitations, we propose DriveVA, a novel autonomous driving world model that jointly decodes future visual forecasts and action sequences in a shared latent generative process. DriveVA inherits rich priors on motion dynamics and physical plausibility from well-pretrained large-scale video generation models to capture continuous spatiotemporal evolution and causal interaction patterns. To this end, DriveVA employs a DiT-based decoder to jointly predict future action sequences (trajectories) and videos, enabling tighter alignment between planning and scene evolution. We also introduce a video continuation strategy to strengthen long-duration rollout consistency. DriveVA achieves an impressive closed-loop performance of 90.9 PDM score on the challenge NAVSIM. Extensive experiments also demonstrate the zero-shot capability and cross-domain generalization of DriveVA, which reduces average L2 error and collision rate by 78.9% and 83.3% on nuScenes and 52.5% and 52.4% on the Bench2drive built on CARLA v2 compared with the state-of-the-art world-model-based planner.

---
