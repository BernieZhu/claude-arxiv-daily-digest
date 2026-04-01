# arXiv Daily Digest — 2026-03-31

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 10

---

## 1. ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation

**Authors:** Hongyu Yan, Qiwei Li, Jiaolong Yang, Yadong Mu
**arXiv:** [2603.27670](https://arxiv.org/abs/2603.27670)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Most existing vision-language-action (VLA) models for robotic manipulation lack progress awareness, typically relying on hand-crafted heuristics for task termination. This limitation is particularly severe in long-horizon tasks involving cascaded sub-goals. In this work, we investigate the estimation and integration of task progress, proposing a novel model named {\textbf \vla}. Our technical contributions are twofold: (1) \emph{robust progress estimation}: We pre-train a progress estimator on large-scale, unsupervised video-text robotic datasets. This estimator achieves a low prediction residual (0.07 on a scale of $[0, 1]$) in simulation and demonstrates zero-shot generalization to unseen real-world samples, and (2) \emph{differentiable progress guidance}: We introduce an inverse dynamics world model that maps predicted action tokens into future latent visual states. These latents are then processed by the progress estimator; by applying a maximal progress regularization, we establish a differentiable pipeline that provides progress-piloted guidance to refine action tokens. Extensive experiments on the CALVIN and LIBERO benchmarks, alongside real-world robot deployment, consistently demonstrate substantial improvements in success rates and generalization over strong baselines.

---

## 2. Language-Conditioned World Modeling for Visual Navigation

**Authors:** Yifei Dong, Fengyi Wu, Yilong Dai, ..., Qi Dai, Zhi-Qi Cheng
**arXiv:** [2603.26741](https://arxiv.org/abs/2603.26741)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

We study language-conditioned visual navigation (LCVN), in which an embodied agent is asked to follow a natural language instruction based only on an initial egocentric observation. Without access to goal images, the agent must rely on language to shape its perception and continuous control, making the grounding problem particularly challenging. We formulate this problem as open-loop trajectory prediction conditioned on linguistic instructions and introduce the LCVN Dataset, a benchmark of 39,016 trajectories and 117,048 human-verified instructions that supports reproducible research across a range of environments and instruction styles. Using this dataset, we develop LCVN frameworks that link language grounding, future-state prediction, and action generation through two complementary model families. The first family combines LCVN-WM, a diffusion-based world model, with LCVN-AC, an actor-critic agent trained in the latent space of the world model. The second family, LCVN-Uni, adopts an autoregressive multimodal architecture that predicts both actions and future observations. Experiments show that these families offer different advantages: the former provides more temporally coherent rollouts, whereas the latter generalizes better to unseen environments. Taken together, these observations point to the value of jointly studying language grounding, imagination, and policy learning in a unified task setting, and LCVN provides a concrete basis for further investigation of language-conditioned world models. The code is available at this https URL.

---

## 3. Lingshu-Cell: A generative cellular world model for transcriptome modeling toward virtual cells

**Authors:** Han Zhang, Guo-Hua Yuan, Chaohao Yuan, ..., Deli Zhao, Yu Rong
**arXiv:** [2603.25240](https://arxiv.org/abs/2603.25240)
**Categories:** Quantitative Methods (q-bio.QM); Artificial Intelligence (cs.AI); Genomics (q-bio.GN)

Modeling cellular states and predicting their responses to perturbations are central challenges in computational biology and the development of virtual cells. Existing foundation models for single-cell transcriptomics provide powerful static representations, but they do not explicitly model the distribution of cellular states for generative simulation. Here, we introduce Lingshu-Cell, a masked discrete diffusion model that learns transcriptomic state distributions and supports conditional simulation under perturbation. By operating directly in a discrete token space that is compatible with the sparse, non-sequential nature of single-cell transcriptomic data, Lingshu-Cell captures complex transcriptome-wide expression dependencies across approximately 18,000 genes without relying on prior gene selection, such as filtering by high variability or ranking by expression level. Across diverse tissues and species, Lingshu-Cell accurately reproduces transcriptomic distributions, marker-gene expression patterns and cell-subtype proportions, demonstrating its ability to capture complex cellular heterogeneity. Moreover, by jointly embedding cell type or donor identity with perturbation, Lingshu-Cell can predict whole-transcriptome expression changes for novel combinations of identity and perturbation. It achieves leading performance on the Virtual Cell Challenge H1 genetic perturbation benchmark and in predicting cytokine-induced responses in human PBMCs. Together, these results establish Lingshu-Cell as a flexible cellular world model for in silico simulation of cell states and perturbation responses, laying the foundation for a new paradigm in biological discovery and perturbation screening.

---

## 4. LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models

**Authors:** Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, Dahuin Jung
**arXiv:** [2603.28301](https://arxiv.org/abs/2603.28301)
**Categories:** Machine Learning (cs.LG)

Vision-Language-Action (VLA) models achieve strong performance in robotic manipulation by leveraging pre-trained vision-language backbones. However, in downstream robotic settings, they are typically fine-tuned with limited data, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored. To study this gap, we introduce LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization. Across seven VLA configurations (0.6B-7.5B), we observe consistent performance degradation of 22-52 pp under paraphrasing. This degradation is primarily driven by object-level lexical variation: even simple synonym substitutions cause large drops, indicating reliance on surface-level matching rather than semantic grounding. Moreover, 80-96% of failures arise from planning-level trajectory divergence rather than execution errors, showing that paraphrasing disrupts task identification. Binary success rate treats all paraphrases equally, obscuring whether models perform consistently across difficulty levels or rely on easier cases. To address this, we propose PRIDE, a metric that quantifies paraphrase difficulty using semantic and syntactic factors. Our benchmark and corresponding code are available at: this https URL

---

## 5. FocusVLA: Focused Visual Utilization for Vision-Language-Action Models

**Authors:** Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan
**arXiv:** [2603.28740](https://arxiv.org/abs/2603.28740)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models improve action generation by conditioning policies on rich vision-language information. However, current auto-regressive policies are constrained by three bottlenecks: (1) architectural bias drives models to overlook visual details, (2) an excessive number of visual tokens makes attention difficult to focus on the correct regions, and (3) task-irrelevant visual information introduces substantial noise - together severely impairing the quality of action. In this paper, we investigate how to effectively utilize different visual representations for action generation. To this end, we first empirically validate the above issues and show that VLA performance is primarily limited by how visual information is utilized, rather than by the quality of visual representations. Based on these insights, we introduce FocusVLA, a novel paradigm that directs the model's attention to task-relevant visual regions to effectively bridge vision to action. Specifically, we first propose Modality Cascaded Attention to eliminate shortcut pathways, thereby compelling VLA models to rely on task-relevant visual details for action generation. Furthermore, we propose Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that FocusVLA not only effectively leverages visual details to perform dexterous manipulations, but also substantially improves performance and accelerates convergence across a variety of tasks.

---

## 6. StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation

**Authors:** Yiran Shi, Dongqi Guo, Tianchen Zhao, ..., Qingmin Liao, Yu Wang
**arXiv:** [2603.28565](https://arxiv.org/abs/2603.28565)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action (VLA) models have demonstrated exceptional performance in natural language-driven perception and control. However, the high computational cost of VLA models poses significant efficiency challenges, particularly for resource-constrained edge platforms in real-world deployments. However, since different stages of VLA (observation, action generation and execution) must proceed sequentially, and wait for the completion of the preceding stage, the system suffers from frequent halting and high latency. To address this, We conduct a systematic analysis to identify the challenges for fast and fluent generation, and propose enabling VLAs with the ability to asynchronously parallelize across VLA stages in a "streaming" manner. First, we eliminate the reliance on action chunking and adopt action flow matching, which learns the trajectory of action flows rather than denoising chunk-wise actions. It overlaps the latency of action generation and execution. Second, we design an action saliency-aware adaptive observation mechanism, thereby overlapping the latency of execution and observation. Without sacrificing performance, StreamingVLA achieves substantial speedup and improves the fluency of execution. It achieves a 2.4 $\times$ latency speedup and reduces execution halting by 6.5 $\times$.

---

## 7. Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving

**Authors:** Qiqi Liu, Huan Xu, Jingyu Li, ..., Xiatian Zhu, Li Zhang
**arXiv:** [2603.27287](https://arxiv.org/abs/2603.27287)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Autonomous driving requires reasoning about how the environment evolves and planning actions accordingly. Existing world-model-based approaches typically predict future scenes first and plan afterwards, resulting in open-loop imagination that may drift from the actual decision process. In this paper, we present Uni-World VLA, a unified vision-language-action (VLA) model that tightly interleaves future frame prediction and trajectory planning. Instead of generating a full world rollout before planning, our model alternates between predicting future frames and ego actions step by step, allowing planning decisions to be continuously conditioned on the imagined future observations. This interleaved generation forms a closed-loop interaction between world modeling and control, enabling more adaptive decision-making in dynamic traffic scenarios. In addition, we incorporate monocular depth information into frames to provide stronger geometric cues for world modeling, improving long-horizon scene prediction. Experiments on the NAVSIM benchmark show that our approach achieves competitive closed-loop planning performance while producing high-fidelity future frame predictions. These results demonstrate that tightly coupling world prediction and planning is a promising direction for scalable VLA driving systems.

---

## 8. LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model

**Authors:** Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang
**arXiv:** [2603.27449](https://arxiv.org/abs/2603.27449)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Learning human-object manipulation presents significant challenges due to its fine-grained and contact-rich nature of the motions involved. Traditional physics-based animation requires extensive modeling and manual setup, and more importantly, it neither generalizes well across diverse object morphologies nor scales effectively to real-world environment. To address these limitations, we introduce LOME, an egocentric world model that can generate realistic human-object interactions as videos conditioned on an input image, a text prompt, and per-frame human actions, including both body poses and hand gestures. LOME injects strong and precise action guidance into object manipulation by jointly estimating spatial human actions and the environment contexts during training. After finetuning a pretrained video generative model on videos of diverse egocentric human-object interactions, LOME demonstrates not only high action-following accuracy and strong generalization to unseen scenarios, but also realistic physical consequences of hand-object interactions, e.g., liquid flowing from a bottle into a mug after executing a ``pouring'' action. Extensive experiments demonstrate that our video-based framework significantly outperforms state-of-the-art image based and video-based action-conditioned methods and Image/Text-to-Video (I/T2V) generative model in terms of both temporal consistency and motion control. LOME paves the way for photorealistic AR/VR experiences and scalable robotic training, without being limited to simulated environments or relying on explicit 3D/4D modeling.

---

## 9. CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence

**Authors:** Tianle Zeng, Hanxuan Chen, Yanci Wen, Hong Zhang
**arXiv:** [2603.28032](https://arxiv.org/abs/2603.28032)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Human-Computer Interaction (cs.HC)

The convergence of low-altitude economies, embodied intelligence, and air-ground cooperative systems creates growing demand for simulation infrastructure capable of jointly modeling aerial and ground agents within a single physically coherent environment. Existing open-source platforms remain domain-segregated: driving simulators lack aerial dynamics, while multirotor simulators lack realistic ground scenes. Bridge-based co-simulation introduces synchronization overhead and cannot guarantee strict spatial-temporal consistency.
We present CARLA-Air, an open-source infrastructure that unifies high-fidelity urban driving and physics-accurate multirotor flight within a single Unreal Engine process. The platform preserves both CARLA and AirSim native Python APIs and ROS 2 interfaces, enabling zero-modification code reuse. Within a shared physics tick and rendering pipeline, CARLA-Air delivers photorealistic environments with rule-compliant traffic, socially-aware pedestrians, and aerodynamically consistent UAV dynamics, synchronously capturing up to 18 sensor modalities across all platforms at each tick. The platform supports representative air-ground embodied intelligence workloads spanning cooperation, embodied navigation and vision-language action, multi-modal perception and dataset construction, and reinforcement-learning-based policy training. An extensible asset pipeline allows integration of custom robot platforms into the shared world. By inheriting AirSim's aerial capabilities -- whose upstream development has been archived -- CARLA-Air ensures this widely adopted flight stack continues to evolve within a modern infrastructure.
Released with prebuilt binaries and full source: this https URL

---

## 10. ManipArena: Comprehensive Real-world Evaluation of Reasoning-Oriented Generalist Robot Manipulation

**Authors:** Yu Sun, Meng Cao, Ping Yang, ..., Ian D Reid, Xiaodan Liang
**arXiv:** [2603.28545](https://arxiv.org/abs/2603.28545)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models and world models have recently emerged as promising paradigms for general-purpose robotic intelligence, yet their progress is hindered by the lack of reliable evaluation protocols that reflect real-world deployment. Existing benchmarks are largely simulator-centric, which provide controllability but fail to capture the reality gap caused by perception noise, complex contact dynamics, hardware constraints, and system latency. Moreover, fragmented real-world evaluations across different robot platforms prevent fair and reproducible comparison. To address these challenges, we introduce ManipArena, a standardized evaluation framework designed to bridge simulation and real-world execution. ManipArena comprises 20 diverse tasks across 10,812 expert trajectories emphasizing reasoning-oriented manipulation tasks requiring semantic and spatial reasoning, supports multi-level generalization through controlled out-of-distribution settings, and incorporates long-horizon mobile manipulation beyond tabletop scenarios. The framework further provides rich sensory diagnostics, including low-level motor signals, and synchronized real-to-sim environments constructed via high-quality 3D scanning. Together, these features enable fair, realistic, and reproducible evaluation for both VLA and world model approaches, providing a scalable foundation for diagnosing and advancing embodied intelligence systems.

---
