# arXiv Daily Digest — 2026-04-23

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 8

---

## 1. A Vision-Language-Action Model for Adaptive Ultrasound-Guided Needle Insertion and Needle Tracking

**Authors:** Yuelin Zhang, Qingpeng Ding, Longxiang Tang, Chengyu Fang, Shing Shin Cheng
**arXiv:** [2604.20347](https://arxiv.org/abs/2604.20347)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Ultrasound (US)-guided needle insertion is a critical yet challenging procedure due to dynamic imaging conditions and difficulties in needle visualization. Many methods have been proposed for automated needle insertion, but they often rely on hand-crafted pipelines with modular controllers, whose performance degrades in challenging cases. In this paper, a Vision-Language-Action (VLA) model is proposed for adaptive and automated US-guided needle insertion and tracking on a robotic ultrasound (RUS) system. This framework provides a unified approach to needle tracking and needle insertion control, enabling real-time, dynamically adaptive adjustment of insertion based on the obtained needle position and environment awareness. To achieve real-time and end-to-end tracking, a Cross-Depth Fusion (CDF) tracking head is proposed, integrating shallow positional and deep semantic features from the large-scale vision backbone. To adapt the pretrained vision backbone for tracking tasks, a Tracking-Conditioning (TraCon) register is introduced for parameter-efficient feature conditioning. After needle tracking, an uncertainty-aware control policy and an asynchronous VLA pipeline are presented for adaptive needle insertion control, ensuring timely decision-making for improved safety and outcomes. Extensive experiments on both needle tracking and insertion show that our method consistently outperforms state-of-the-art trackers and manual operation, achieving higher tracking accuracy, improved insertion success rates, and reduced procedure time, highlighting promising directions for RUS-based intelligent intervention.

---

## 2. Cortex 2.0: Grounding World Models in Real-World Industrial Deployment

**Authors:** Adriana Aida, Walid Amer, Katarina Bankovic, ..., Marc Tuscher, Pavan Upputuri
**arXiv:** [2604.20246](https://arxiv.org/abs/2604.20246)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Industrial robotic manipulation demands reliable long-horizon execution across embodiments, tasks, and changing object distributions. While Vision-Language-Action models have demonstrated strong generalization, they remain fundamentally reactive. By optimizing the next action given the current observation without evaluating potential futures, they are brittle to the compounding failure modes of long-horizon tasks. Cortex 2.0 shifts from reactive control to plan-and-act by generating candidate future trajectories in visual latent space, scoring them for expected success and efficiency, then committing only to the highest-scoring candidate. We evaluate Cortex 2.0 on a single-arm and dual-arm manipulation platform across four tasks of increasing complexity: pick and place, item and trash sorting, screw sorting, and shoebox unpacking. Cortex 2.0 consistently outperforms state-of-the-art Vision-Language-Action baselines, achieving the best results across all tasks. The system remains reliable in unstructured environments characterized by heavy clutter, frequent occlusions, and contact-rich manipulation, where reactive policies fail. These results demonstrate that world-model-based planning can operate reliably in complex industrial environments.

---

## 3. EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training

**Authors:** Yiyang Du, Zhanqiu Guo, Xin Ye, Liu Ren, Chenyan Xiong
**arXiv:** [2604.20012](https://arxiv.org/abs/2604.20012)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Vision-Language-Action Models (VLAs) inherit their visual and linguistic capabilities from Vision-Language Models (VLMs), yet most VLAs are built from off-the-shelf VLMs that are not adapted to the embodied domain, limiting their downstream performance. In this work, we propose EmbodiedMidtrain to bridge the gap between VLMs and VLAs. We first characterize the data distribution gap between them, showing that VLA data occupy compact regions that are largely separated from the broader VLM distribution, while the degree of alignment varies substantially both across and within VLM data sources. Then, we build a mid-training data engine that leverages a lightweight learnable proximity estimator to select the most VLA-aligned candidates from a large VLM pool, and mid-trains the VLM on this curated mixture before downstream VLA fine-tuning. Experiments on three robot manipulation benchmarks show that mid-training consistently improves performance across different VLM backbones, achieving results competitive with expert VLAs and off-the-shelf VLMs trained with larger model scale and training budgets. Further analysis reveals that mid-training provides a stronger initialization for VLA fine-tuning, with gains emerging from the earliest steps and widening throughout training. Moreover, the data engine captures both dataset-level and sample-level alignment signals, favoring spatial reasoning over text-centric tasks while preserving the diversity of the VLM data. We will release all code, data and models for future research.

---

## 4. Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models

**Authors:** Shelly Francis-Meretzki, Mirco Mutti, Yaniv Romano, Aviv Tamar
**arXiv:** [2604.20472](https://arxiv.org/abs/2604.20472)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Recent advances in vision-language-action (VLA) models for robotics have highlighted the importance of reliable uncertainty quantification in sequential tasks. However, assessing and improving calibration in such settings remains mostly unexplored, especially when only partial trajectories are observed. In this work, we formulate sequential calibration for episodic tasks, where task-success confidence is produced along an episode, while success is determined at the end of it. We introduce a sequential extension of the Brier score and show that, for binary outcomes, its risk minimizer coincides with the VLA policy's value function. This connection bridges uncertainty calibration and reinforcement learning, enabling the use of temporal-difference (TD) value estimation as a principled calibration mechanism over time. We empirically show that TD calibration improves performance relative to the state-of-the-art on simulated and real-robot data. Interestingly, we show that when calibrated using TD, the VLA's single-step action probabilities can yield competitive uncertainty estimates, in contrast to recent findings that employed different calibration techniques.

---

## 5. Toward Safe Autonomous Robotic Endovascular Interventions using World Models

**Authors:** Harry Robertshaw, Nikola Fischer, Han-Ru Wu, ..., Alejandro Granados, Thomas C Booth
**arXiv:** [2604.20151](https://arxiv.org/abs/2604.20151)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Autonomous mechanical thrombectomy (MT) presents substantial challenges due to highly variable vascular geometries and the requirements for accurate, real-time control. While reinforcement learning (RL) has emerged as a promising paradigm for the automation of endovascular navigation, existing approaches often show limited robustness when faced with diverse patient anatomies or extended navigation horizons. In this work, we investigate a world-model-based framework for autonomous endovascular navigation built on TD-MPC2, a model-based RL method that integrates planning and learned dynamics. We evaluate a TD-MPC2 agent trained on multiple navigation tasks across hold out patient-specific vasculatures and benchmark its performance against the state-of-the-art Soft Actor-Critic (SAC) algorithm agent. Both approaches are further validated in vitro using patient-specific vascular phantoms under fluoroscopic guidance. In simulation, TD-MPC2 demonstrates a significantly higher mean success rate than SAC (58% vs. 36%, p < 0.001), and mean tip contact forces of 0.15 N, well below the proposed 1.5 N vessel rupture threshold. Mean success rates for TD-MPC2 (68%) were comparable to SAC (60%) in vitro, but TD-MPC2 achieved superior path ratios (p = 0.017) at the cost of longer procedure times (p < 0.001). Together, these results provide the first demonstration of autonomous MT navigation validated across both hold out in silico data and fluoroscopy-guided in vitro experiments, highlighting the promise of world models for safe and generalizable AI-assisted endovascular interventions.

---

## 6. PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance

**Authors:** Yupeng Zheng, Xiang Li, Songen Gu, ..., Haoran Li, Wenchao Ding
**arXiv:** [2604.20834](https://arxiv.org/abs/2604.20834)
**Categories:** Robotics (cs.RO)

Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: this https URL

---

## 7. X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference

**Authors:** Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, ..., Bo Tian, Xianming Liu
**arXiv:** [2604.20289](https://arxiv.org/abs/2604.20289)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Real-time world simulation is becoming a key infrastructure for scalable evaluation and online reinforcement learning of autonomous driving systems. Recent driving world models built on autoregressive video diffusion achieve high-fidelity, controllable multi-camera generation, but their inference cost remains a bottleneck for interactive deployment. However, existing diffusion caching methods are designed for offline video generation with multiple denoising steps, and do not transfer to this scenario. Few-step distilled models have no inter-step redundancy left for these methods to reuse, and sequence-level parallelization techniques require future conditioning that closed-loop interactive generation does not provide. We present X-Cache, a training-free acceleration method that caches along a different axis: across consecutive generation chunks rather than across denoising steps. X-Cache maintains per-block residual caches that persist across chunks, and applies a dual-metric gating mechanism over a structure- and action-aware block-input fingerprint to independently decide whether each block should recompute or reuse its cached residual. To prevent approximation errors from permanently contaminating the autoregressive KV cache, X-Cache identifies KV update chunks (the forward passes that write clean keys and values into the persistent cache) and unconditionally forces full computation on these chunks, cutting off error propagation. We implement X-Cache on X-world, a production multi-camera action-conditioned driving world model built on multi-block causal DiT with few-step denoising and rolling KV cache. X-Cache achieves 71% block skip rate with 2.6x wall-clock speedup while maintaining minimum degradation.

---

## 8. JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy

**Authors:** Tianle Zhang, Zhihao Yuan, Dafeng Chi, ..., Yuzheng Zhuang, Liang Lin
**arXiv:** [2604.20100](https://arxiv.org/abs/2604.20100)
**Categories:** Robotics (cs.RO)

Robotic autonomy in open-world environments is fundamentally limited by insufficient data diversity and poor cross-embodiment generalization. Existing robotic datasets are often limited in scale and task coverage, while relatively large differences across robot embodiments impede effective behavior knowledge transfer. To address these challenges, we propose JoyAI-RA, a vision-language-action (VLA) embodied foundation model tailored for generalizable robotic manipulation. JoyAI-RA presents a multi-source multi-level pretraining framework that integrates web data, large-scale egocentric human manipulation videos, simulation-generated trajectories, and real-robot data. Through training on heterogeneous multi-source data with explicit action-space unification, JoyAI-RA effectively bridges embodiment gaps, particularly between human manipulation and robotic control, thereby enhancing cross-embodiment behavior learning. JoyAI-RA outperforms state-of-the-art methods in both simulation and real-world benchmarks, especially on diverse tasks with generalization demands.

---
