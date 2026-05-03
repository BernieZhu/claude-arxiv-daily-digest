# arXiv Daily Digest — 2026-04-08

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 10

---

## 1. Toward Consistent World Models with Multi-Token Prediction and Latent Semantic Enhancement

**Authors:** Qimin Zhong, Hao Liao, Haiming Qin, ..., Wei Chen, Naipeng Chao
**arXiv:** [2604.06155](https://arxiv.org/abs/2604.06155)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Whether Large Language Models (LLMs) develop coherent internal world models remains a core debate. While conventional Next-Token Prediction (NTP) focuses on one-step-ahead supervision, Multi-Token Prediction (MTP) has shown promise in learning more structured representations. In this work, we provide a theoretical perspective analyzing the gradient inductive bias of MTP, supported by empirical evidence, showing that MTP promotes the convergence toward internal belief states by inducing representational contractivity via gradient coupling. However, we reveal that standard MTP often suffers from structural hallucinations, where discrete token supervision encourages illegal shortcuts in latent space that violate environmental constraints. To address this, we propose a novel method Latent Semantic Enhancement MTP (LSE-MTP), which anchors predictions to ground-truth hidden state trajectories. Experiments on synthetic graphs and real-world Manhattan Taxi Ride show that LSE-MTP effectively bridges the gap between discrete tokens and continuous state representations, enhancing representation alignment, reducing structural hallucinations, and improving robustness to perturbations.

---

## 2. SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation

**Authors:** Wuyang Luan, Junhui Li, Weiguang Zhao, ..., Tieru Wu, Rui Ma
**arXiv:** [2604.05656](https://arxiv.org/abs/2604.05656)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models based on flow matching -- such as pi0, pi0.5, and SmolVLA -- achieve state-of-the-art generalist robotic manipulation, yet their iterative denoising, typically 10 ODE steps, introduces substantial latency: on a modern GPU, denoising alone accounts for 80% of end-to-end inference time. Naively reducing the step count is unreliable, degrading success on most tasks due to the velocity field being uncalibrated for single-step jumps. We present SnapFlow, a plug-and-play self-distillation method that compresses multi-step denoising into a single forward pass (1-NFE) for flow-matching VLAs. SnapFlow mixes standard flow-matching samples with consistency samples whose targets are two-step Euler shortcut velocities computed from the model's own marginal velocity predictions, avoiding the trajectory drift caused by conditional velocities, as we analyze theoretically. A zero-initialized target-time embedding lets the network switch between local velocity estimation and global one-step generation within a single architecture. SnapFlow requires no external teacher, no architecture changes, and trains in ~12h on a single GPU. We validate on two VLA architectures spanning a 6x parameter range, with identical hyperparameters: on pi0.5 (3B) across four LIBERO suites (40 tasks, 400 episodes), SnapFlow achieves 98.75% average success -- matching the 10-step teacher at 97.75% and slightly exceeding it -- with 9.6x denoising speedup and end-to-end latency reduced from 274ms to 83ms; on SmolVLA (500M), it reduces MSE by 8.3% with 3.56x end-to-end acceleration. An action-step sweep on long-horizon tasks reveals that SnapFlow maintains its advantage across execution horizons, achieving 93% at n_act=5 where the baseline reaches only 90%. SnapFlow is orthogonal to layer-distillation and token-pruning approaches, enabling compositional speedups.

---

## 3. StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing

**Authors:** StarVLA Community
**arXiv:** [2604.05014](https://arxiv.org/abs/2604.05014)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Building generalist embodied agents requires integrating perception, language understanding, and action, which are core capabilities addressed by Vision-Language-Action (VLA) approaches based on multimodal foundation models, including recent advances in vision-language models and world models. Despite rapid progress, VLA methods remain fragmented across incompatible architectures, codebases, and evaluation protocols, hindering principled comparison and reproducibility. We present StarVLA, an open-source codebase for VLA research. StarVLA addresses these challenges in three aspects. First, it provides a modular backbone--action-head architecture that supports both VLM backbones (e.g., Qwen-VL) and world-model backbones (e.g., Cosmos) alongside representative action-decoding paradigms, all under a shared abstraction in which backbone and action head can each be swapped independently. Second, it provides reusable training strategies, including cross-embodiment learning and multimodal co-training, that apply consistently across supported paradigms. Third, it integrates major benchmarks, including LIBERO, SimplerEnv, RoboTwin~2.0, RoboCasa-GR1, and BEHAVIOR-1K, through a unified evaluation interface that supports both simulation and real-robot deployment. StarVLA also ships simple, fully reproducible single-benchmark training recipes that, despite minimal data engineering, already match or surpass prior methods on multiple benchmarks with both VLM and world-model backbones. To our best knowledge, StarVLA is one of the most comprehensive open-source VLA frameworks available, and we expect it to lower the barrier for reproducing existing methods and prototyping new ones. StarVLA is being actively maintained and expanded; we will update this report as the project evolves. The code and documentation are available at this https URL.

---

## 4. A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model

**Authors:** Kaidong Zhang, Jian Zhang, Rongtao Xu, ..., Ivan Laptev, Xiaodan Liang
**arXiv:** [2604.05672](https://arxiv.org/abs/2604.05672)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for open-world robot manipulation, but their practical deployment is often constrained by cost: billion-scale VLM backbones and iterative diffusion/flow-based action heads incur high latency and compute, making real-time control expensive on commodity hardware. We present A1, a fully open-source and transparent VLA framework designed for low-cost, high-throughput inference without sacrificing manipulation success; Our approach leverages pretrained VLMs that provide implicit affordance priors for action generation. We release the full training stack (training code, data/data-processing pipeline, intermediate checkpoints, and evaluation scripts) to enable end-to-end reproducibility. Beyond optimizing the VLM alone, A1 targets the full inference pipeline by introducing a budget-aware adaptive inference scheme that jointly accelerates the backbone and the action head. Specifically, we monitor action consistency across intermediate VLM layers to trigger early termination, and propose Inter-Layer Truncated Flow Matching that warm-starts denoising across layers, enabling accurate actions with substantially fewer effective denoising iterations. Across simulation benchmarks (LIBERO, VLABench) and real robots (Franka, AgiBot), A1 achieves state-of-the-art success rates while significantly reducing inference cost (e.g., up to 72% lower per-episode latency for flow-matching inference and up to 76.6% backbone computation reduction with minor performance degradation). On RoboChallenge, A1 achieves an average success rate of 29.00%, outperforming baselines including pi0(28.33%), X-VLA (21.33%), and RDT-1B (15.00%).

---

## 5. Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment

**Authors:** Theodor Wulff, Federico Tavella, Rahul Singh Maharjan, Manith Adikari, Angelo Cangelosi
**arXiv:** [2604.05614](https://arxiv.org/abs/2604.05614)
**Categories:** Robotics (cs.RO)

Achieving robot transparency is a critical step toward effective human-robot collaboration. To be transparent, a robot's natural language communication must be consistent with its actions and explicitly grounded in the task and environment. Existing hierarchical Vision-Language-Action (VLA) models can generate language (e.g., through chain-of-thought) and low-level actions. However, current work does not consider explicit alignment between these modalities during training. To address this crucial gap, we propose a novel training framework that explicitly grounds hierarchical VLA sub-task descriptions with respect to the visual observation and action space. Our framework uses a contrastive model to assess the alignment between generated language and corresponding action trajectories. This contrastive model enables direct ranking of different language-trajectory pairs based on their alignment, allowing us to refine the grounding of our hierarchical VLA through offline preference learning. We apply our framework to the LanguageTable dataset, a benchmark dataset of human language-annotated trajectories, and provide critical insights into multimodal grounding representations, all while establishing a strong baseline that achieves performance comparable to fully supervised fine-tuning and minimizing the need for costly data annotations.

---

## 6. Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming

**Authors:** Baoshun Tong, Haoran He, Ling Pan, Yang Liu, Liang Lin
**arXiv:** [2604.05595](https://arxiv.org/abs/2604.05595)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models have achieved remarkable success in robotic manipulation. However, their robustness to linguistic nuances remains a critical, under-explored safety concern, posing a significant safety risk to real-world deployment. Red teaming, or identifying environmental scenarios that elicit catastrophic behaviors, is an important step in ensuring the safe deployment of embodied AI agents. Reinforcement learning (RL) has emerged as a promising approach in automated red teaming that aims to uncover these vulnerabilities. However, standard RL-based adversaries often suffer from severe mode collapse due to their reward-maximizing nature, which tends to converge to a narrow set of trivial or repetitive failure patterns, failing to reveal the comprehensive landscape of meaningful risks. To bridge this gap, we propose a novel \textbf{D}iversity-\textbf{A}ware \textbf{E}mbodied \textbf{R}ed \textbf{T}eaming (\textbf{DAERT}) framework, to expose the vulnerabilities of VLAs against linguistic variations. Our design is based on evaluating a uniform policy, which is able to generate a diverse set of challenging instructions while ensuring its attack effectiveness, measured by execution failures in a physical simulator. We conduct extensive experiments across different robotic benchmarks against two state-of-the-art VLAs, including $\pi_0$ and OpenVLA. Our method consistently discovers a wider range of more effective adversarial instructions that reduce the average task success rate from 93.33\% to 5.85\%, demonstrating a scalable approach to stress-testing VLA agents and exposing critical safety blind spots before real-world deployment.

---

## 7. JailWAM: Jailbreaking World Action Models in Robot Control

**Authors:** Hanqing Liu, Songping Wang, Jiahuan Long, ..., Wen Yao, Yao Mu
**arXiv:** [2604.05498](https://arxiv.org/abs/2604.05498)
**Categories:** Robotics (cs.RO)

The World Action Model (WAM) can jointly predict future world states and actions, exhibiting stronger physical manipulation capabilities compared with traditional models. Such powerful physical interaction ability is a double-edged sword: if safety is ignored, it will directly threaten personal safety, property security and environmental safety. However, existing research pays extremely limited attention to the critical security gap: the vulnerability of WAM to jailbreak attacks. To fill this gap, we define the Three-Level Safety Classification Framework to systematically quantify the safety of robotic arm motions. Furthermore, we propose JailWAM, the first dedicated jailbreak attack and evaluation framework for WAM, which consists of three core components: (1) Visual-Trajectory Mapping, which unifies heterogeneous action spaces into visual trajectory representations and enables cross-architectural unified evaluation; (2) Risk Discriminator, which serves as a high-recall screening tool that optimizes the efficiency-accuracy trade-off when identifying destructive behaviors in visual trajectories; (3) Dual-Path Verification Strategy, which first conducts rapid coarse screening via a single-image-based video-action generation module, and then performs efficient and comprehensive verification through full closed-loop physical simulation. In addition, we construct JailWAM-Bench, a benchmark for comprehensively evaluating the safety alignment performance of WAM under jailbreak attacks. Experiments in RoboTwin simulation environment demonstrate that the proposed framework efficiently exposes physical vulnerabilities, achieving an 84.2% attack success rate on the state-of-the-art LingBot-VA. Meanwhile, robust defense mechanisms can be constructed based on JailWAM, providing an effective technical solution for designing safe and reliable robot control systems.

---

## 8. VLA-InfoEntropy: A Training-Free Vision-Attention Information Entropy Approach for Vision-Language-Action Models Inference Acceleration and Success

**Authors:** Chuhang Liu, Yayun He, Zuheng Kang, Xiaoyang Qu, Jianzong Wang
**arXiv:** [2604.05323](https://arxiv.org/abs/2604.05323)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision-Language-Action (VLA) models integrate visual perception, language understanding, and action decision-making for cross-modal semantic alignment, exhibiting broad application potential. However, the joint processing of high-dimensional visual features, complex linguistic inputs, and continuous action sequences incurs significant computational overhead and low inference efficiency, thereby hindering real-time deployment and reliability. To address this issue, we use image entropy to quantify the grayscale distribution characteristics of each visual token and introduce attention entropy to capture the distribution of attention scores over task-related text. Visual entropy identifies texture-rich or structurally informative regions, while attention entropy pinpoints semantically relevant tokens. Combined with timestep information, these metrics enable a dynamic transition strategy that shifts the model's focus from global visual features to attention-guided local informative regions. Thus, the resulting VLA-InfoEntropy method integrates spatial, semantic, and temporal cues to reduce redundancy while preserving critical content. Extensive experiments show that our method reduces inference parameters, accelerates inference speed, and outperforms existing approaches.

---

## 9. Action Images: End-to-End Policy Learning via Multiview Video Generation

**Authors:** Haoyu Zhen, Zixian Gao, Qiao Sun, ..., Yi-Ling Qiao, Chuang Gan
**arXiv:** [2604.06168](https://arxiv.org/abs/2604.06168)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

World action models (WAMs) have emerged as a promising direction for robot policy learning, as they can leverage powerful video backbones to model the future states. However, existing approaches often rely on separate action modules, or use action representations that are not pixel-grounded, making it difficult to fully exploit the pretrained knowledge of video models and limiting transfer across viewpoints and environments. In this work, we present Action Images, a unified world action model that formulates policy learning as multiview video generation. Instead of encoding control as low-dimensional tokens, we translate 7-DoF robot actions into interpretable action images: multi-view action videos that are grounded in 2D pixels and explicitly track robot-arm motion. This pixel-grounded action representation allows the video backbone itself to act as a zero-shot policy, without a separate policy head or action module. Beyond control, the same unified model supports video-action joint generation, action-conditioned video generation, and action labeling under a shared representation. On RLBench and real-world evaluations, our model achieves the strongest zero-shot success rates and improves video-action joint generation quality over prior video-space world models, suggesting that interpretable action images are a promising route to policy learning.

---

## 10. ICR-Drive: Instruction Counterfactual Robustness for End-to-End Language-Driven Autonomous Driving

**Authors:** Kaiser Hamid, Can Cui, Nade Liang
**arXiv:** [2604.05378](https://arxiv.org/abs/2604.05378)
**Categories:** Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Recent progress in vision-language-action (VLA) models has enabled language-conditioned driving agents to execute natural-language navigation commands in closed-loop simulation, yet standard evaluations largely assume instructions are precise and well-formed. In deployment, instructions vary in phrasing and specificity, may omit critical qualifiers, and can occasionally include misleading, authority-framed text, leaving instruction-level robustness under-measured. We introduce ICR-Drive, a diagnostic framework for instruction counterfactual robustness in end-to-end language-conditioned autonomous driving. ICR-Drive generates controlled instruction variants spanning four perturbation families: Paraphrase, Ambiguity, Noise, and Misleading, where Misleading variants conflict with the navigation goal and attempt to override intent. We replay identical CARLA routes under matched simulator configurations and seeds to isolate performance changes attributable to instruction language. Robustness is quantified using standard CARLA Leaderboard metrics and per-family performance degradation relative to the baseline instruction. Experiments on LMDrive and BEVDriver show that minor instruction changes can induce substantial performance drops and distinct failure modes, revealing a reliability gap for deploying embodied foundation models in safety-critical driving.

---
