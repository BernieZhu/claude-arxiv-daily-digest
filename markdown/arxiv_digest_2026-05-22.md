# arXiv Daily Digest — 2026-05-22

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 10

---

## 1. Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts

**Authors:** Zhen Sun, Yongjian Guo, Haoran Sun, ..., Junwu Xiong, Zhijun Meng
**arXiv:** [2605.22446](https://arxiv.org/abs/2605.22446)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. Low-quality actions may cause physical failures during execution or lead to misleading world-model rollouts with redundant rendering costs. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity assessment before physical execution or world-model imagination. Pre-VLA leverages an efficient multimodal backbone with modality-aware pooling and a lightweight dual-branch head to predict both safety confidence and critic-derived advantage scores for candidate action chunks. To handle severe class imbalance and unstable boundary decisions, we train Pre-VLA with a multi-task objective combining Focal classification, advantage regression, and soft-threshold calibration. During deployment, a dual-mode preemptive resampling scheduler filters low-quality actions and triggers adaptive resampling under a limited computation budget. Experiments on the LIBERO benchmark show that Pre-VLA improves the average closed-loop success rate across four suites from 30.79\% to 37.62\% over RynnVLA-002, reduces task execution steps, achieves 183.9 ms average forward verification time per action chunk, and mitigates error accumulation in world-model rollouts.

---

## 2. LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model

**Authors:** Xiaodong Mei, Diankun Zhang, Hongwei Xie, ..., Hangjun Ye, Dan Xu
**arXiv:** [2605.22089](https://arxiv.org/abs/2605.22089)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have emerged as a promising framework for end-to-end autonomous driving. However, existing VLAs typically rely on sparse action supervision, which underutilizes their powerful scene understanding and reasoning capabilities. Recent attempts to incorporate dense visual supervision via world modeling often overemphasize pixel-level image reconstruction, neglecting semantically meaningful scene representation learning. In this work, we propose LVDrive, a Latent Visual representation enhanced VLA framework for autonomous driving. LVDrive introduces a future scene prediction task into the VLA paradigm, where future representations are learned entirely in a high-level latent space under auxiliary supervision from a pretrained vision backbone. Departing from inefficient autoregressive generation, we jointly model future scene and motion prediction within a unified embedding space, processed in a single forward pass to conduct the future-aware reasoning. We further design a two-stage trajectory decoding strategy that explicitly leverages the learned latent future representations to refine trajectory generation. Extensive experiments on the challenging Bench2Drive benchmark demonstrate that LVDrive achieves significant improvements in closed-loop driving performance, outperforming both action supervised methods and image-reconstruction-based world model approaches.

---

## 3. ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data

**Authors:** Jiangyuan Wang, Xuyong Chen, Junwei He, ..., Shasha Xie, Fuman Han
**arXiv:** [2605.21963](https://arxiv.org/abs/2605.21963)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Long-horizon clinical simulation -- predicting how a patient's physiology evolves over years under specified interventions -- is central to chronic-disease care, yet existing electronic health record (EHR) models are predominantly discriminative, and general-purpose large language models drift under repeated interventions. We propose the \textbf{ChronoMedicalWorld Model (CMWM)}, an action-conditioned latent world-model framework for learning patient trajectories from longitudinal care data. CMWM couples a joint-embedding state encoder with a wide action encoder that admits both structured intervention indicators and free-text communication embeddings, and trains a recurrent latent transition module under a six-term objective: next-observation supervision, next-latent prediction, SIGReg latent regularisation, and three physiology-aware shape priors (slope, continuity, large-jump penalty). A closed-loop rollout-prefix protocol matches training to deployment, so the model is optimised against the same multi-step error it exhibits at inference. As a concrete case study, we instantiate CMWM for annual estimated glomerular filtration rate (eGFR) trajectory forecasting in chronic kidney disease (CKD). On a 2{,}232-patient nephrology cohort, the CKD instantiation achieves a dynamic-50\% history rollout test mean absolute error (MAE) of 7.384 and root-mean-square error (RMSE) of 10.256, against 7.964 and 11.069 for a tuned GPT-5.5 structured-prompting baseline ($-7.28\%$ MAE, $-7.35\%$ RMSE), with the gain dominated by the dialogue portion of patient--health-coach communication. The framework is not CKD-specific: its architecture, loss design, and training protocol apply to any chronic condition that can be cast as periodic clinical state interleaved with structured and conversational interventions.

---

## 4. EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control

**Authors:** Chushan Zhang, Ruihan Lu, Jinguang Tong, ..., Yikai Wang, Hongdong Li
**arXiv:** [2605.21862](https://arxiv.org/abs/2605.21862)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Chunked vision-language-action (VLA) policies predict multi-step robot controls, conditioning each update on the current visual observation alone. Yet robot actions cause contact, occlusion, and object motion, and the geometry that later decisions depend on can change before the next visual update arrives. Spatial VLAs improve current-frame geometry. Temporal VLAs aggregate past frames. Neither maintains an action-updated scene prior across chunks. We argue for a persistent action-updated scene state across control calls, and introduce EvoScene-VLA. Its recurrent scene prefix carries a geometry-aware scene state across chunks. At each vision-language model (VLM) call, the VLM combines scene information from the current observation with the action-updated prior from the previous chunk; the action decoder outputs both the next action chunk and a compact scene update. This update becomes the next prior, which the VLM corrects against the new observation when the next call arrives. Each control call therefore starts from a scene prior that reflects both recent actions and fresh visual evidence. During training, \textbf{Scene Predictor} supplies future scene-token targets, and Geometric Anchor aligns scene slots with frozen depth and 3D teachers. We discard both modules at deployment. On 31 RoboTwin tasks, EvoScene-VLA raises average success from 87.2% to 89.1% in fixed evaluation and from 86.1% to 88.5% in randomized evaluation. On the Galaxea R1-Lite real robot, EvoScene-VLA outperforms all baselines.

---

## 5. CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models

**Authors:** Zhi Liu
**arXiv:** [2605.21854](https://arxiv.org/abs/2605.21854)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have rapidly converged on a small set of architectural patterns: discrete-token autoregression (e.g. OpenVLA) and continuous-action flow-matching (e.g. pi-0.5). Yet preference alignment via Direct Preference Optimisation (DPO) -- the de-facto post-training step in language models -- has been studied almost exclusively on autoregressive VLAs. We present CrossVLA, an empirical study of cross-paradigm VLA post-training. Three contributions: (i) a surrogate flow-matching log-probability estimator that lets DPO operate on continuous-action backbones without probability-flow ODE integration; (ii) a head-to-head comparison of LoRA and DoRA as the parameter-efficient layer for VLA DPO, finding DoRA improves over OpenVLA SFT by a mean +10.4 pp across LIBERO 4-suite (600 trials, 3 seeds) -- per-suite +20.0 Object, +11.0 Long-horizon, +8.0 Goal, +2.7 Spatial -- with zero seed variance on Object (38/50 on each of 3 seeds); (iii) an inference-time anatomy showing the denoise loop dominates 78.6% of sample_actions latency and prefix-K/V caching a la VLA-Cache caps at a 21% acceleration ceiling -- both chunk-level and token-level cache strategies degrade success rate to 0-80% in our benchmarks. We further pretrain a multi-view + temporal projection head on 6000 LIBERO frames, achieving 99.5% k-NN recall@1 for same-task retrieval (36x over random), available as a downstream initialisation. All code, ckpts, training logs, and reproduction scripts are open at this https URL.

---

## 6. Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics

**Authors:** Liangyu Li, Shengzhi Wang, Qingwen Liu
**arXiv:** [2605.22164](https://arxiv.org/abs/2605.22164)
**Categories:** Machine Learning (cs.LG); Robotics (cs.RO)

Latent world models can contain the state needed for control, yet their terminal-cost interface can expose the planner to the wrong decision-relevant information. In common latent MPC, candidate sequences are ranked by Euclidean distance between predicted terminal and goal latent states; this assumes that raw latent distance weights reachability-relevant variables correctly. We propose trajectory reachability metrics (TRM), a post-hoc terminal-ranking method for fixed latent world models. TRM trains a small pairwise head from logged trajectory structure and uses it as a replacement or hybrid cost; the encoder, dynamics, sampler, optimizer, and evaluation manifests remain fixed. The key design choice is horizon-aware supervision: the metric is trained on broad, balanced temporal separations to match the long-horizon terminal candidate ranking problem. On a hard TwoRoom benchmark, raw latent planning with LeWorldModel (LeWM) reaches 7.0% success, while full-horizon TRM reaches 97.0%; shuffled temporal-label controls stay at 0.0%. The same recipe improves a PLDM baseline from 32.7% to 84.0% across three seeds, and a short-horizon TRM variant reaches only 35.0% with the 100,000 pair budget. In TwoRoom, we provide mechanistic evidence for why TRM works: XY position is linearly decodable (R^2=0.998), yet raw latent MSE misranks candidates; the XY-probe rowspace accounts for less than 1% of terminal-goal latent MSE but carries most candidate-quality signal; and SCSA audits show that TRM improves the ordering and selected endpoint seen by the planner. On PushT go50/go75, TRM-style task-state metrics improve SCSA ranking and selected final distance more cleanly than closed-loop success, motivating auxiliary hybrid costs in continuous manipulation. TRM is the planner-facing repair, and audits explain when terminal reachability metrics should replace or augment raw latent proximity.

---

## 7. stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation

**Authors:** Lucas Maes, Quentin Le Lidec, Luiz Facury, ..., Yann LeCun, Randall Balestriero
**arXiv:** [2605.21800](https://arxiv.org/abs/2605.21800)
**Categories:** Machine Learning (cs.LG); Robotics (cs.RO)

World models are central to building agents that can reason, plan, and generalize beyond their training data. However, research on world models is currently fragmented, with disparate codebases, data pipelines, and evaluation protocols hindering reproducibility and fair comparison. Current practice is further limited by three key bottlenecks: fragile one-off codebases, slow video data loading, and the lack of standardized generalization benchmarks. We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation. It delivers (1) a high-performance Lance-based data layer with native support and conversion tools for MP4, HDF5, and LeRobot datasets, (2) clean, well-tested implementations of modern world model baselines and planning solvers, and (3) a broad suite of environments and tasks extended with controllable visual, geometric, and physical factors of variation for systematic in-silico evaluation of dynamics understanding, control performance, representation quality, and out-of-distribution generalization. By unifying the full pipeline under a single, scalable framework, \texttt{swm} dramatically reduces research overhead and accelerates trustworthy progress toward reliable world models.

---

## 8. GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations

**Authors:** Wenxuan Guo, Ziyuan Li, Meng Zhang, ..., Erjin Zhou, Jianjiang Feng
**arXiv:** [2605.22812](https://arxiv.org/abs/2605.22812)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have shown strong potential for general-purpose robot manipulation by unifying perception and action. However, existing VLA systems primarily rely on textual instructions and struggle to resolve spatial ambiguity in complex scenes with multiple similar objects. To address this limitation, we introduce gesture as a parallel instruction modality and propose a Gesture-aware Vision-Language-Action model (GesVLA). Our approach encodes gesture features directly into the latent space, enabling them to participate in both high-level reasoning and low-level action generation, and adopts a dual-VLM architecture to achieve tight coupling between gesture representations and action policies. At the data level, we construct a scalable gesture data generation pipeline by rendering hand models onto real-world scene images. This reduces the sim-to-real visual gap while producing rich data with diverse motion patterns and corresponding pointing annotations. In addition, we employ a two-stage training strategy to equip the model with both gesture perception and action prediction capabilities. We evaluate our approach on multiple real-world robotic tasks, including a controlled block manipulation task for validation and more practical scenarios such as product and produce selection. Experimental results show that incorporating gesture consistently improves target grounding accuracy and human-robot interaction efficiency, especially in complex and cluttered environments. Project page: this https URL.

---

## 9. Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

**Authors:** Pengteng Li, Weiyu Guo, He Zhang, ..., Yandong Guo, Hui Xiong
**arXiv:** [2605.22283](https://arxiv.org/abs/2605.22283)
**Categories:** Robotics (cs.RO)

We introduce SOMA, the Spatial Memory framework for Out-of-Vision Manipulation in Vision-Language-Action (VLA) models. Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera's field of view. SOMA addresses this limitation by equipping VLAs with a persistent spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond the current visual frustum. The framework consists of three components: Spatial Memory Construction, which aggregates angular-wise observations into a unified spatial-semantic representation through scanning; Dynamic Memory Refinement, which maintains global consistency over time; and Contextual Memory Retrieval, which activates instruction-relevant spatial cues during manipulation. We evaluate SOMA on five challenging real-world out-of-vision manipulation tasks, including multi-step and dual-arm scenarios where target objects are initially invisible. Experimental results show that SOMA not only improves task success rates, but also induces qualitatively different manipulation behaviors, with faster target localization, reduced viewpoint search, and near one-shot grasping under partial observability. Additional experiments on RoboCasa GR1 and SimplerEnv further validate the effectiveness of SOMA's memory design under conventional fully observable settings. Code will be released soon.

---

## 10. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

**Authors:** Bing Hu, Zaijing Li, Rui Shao, ..., Wei-Shi Zheng, Liqiang Nie
**arXiv:** [2605.22671](https://arxiv.org/abs/2605.22671)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components: (1) the \textbf{Visuomotor Behavior Encoder (VBE)}, which utilizes a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation; and (2) the \textbf{Phase-conditioned Behavior Decoder (PBD)}, which decodes this representation into precise actions by dynamically aligning task-level priors with real-time execution progress. Experiments on RoboTwin 2.0, LIBERO, and CALVIN demonstrate state-of-the-art success rates of 58\%, 98\%, and 4.36 (this http URL), respectively. Notably, in real-world sim-to-real transfer, BehaviorVLA matches the performance of OpenVLA-OFT using only 50\% of the demonstration data, showcasing its superior data efficiency and generalization.

---
