# arXiv Daily Digest — 2026-04-28

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 10

---

## 1. CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies

**Authors:** Fan Du, Feng Yan, Jianxiong Wu, ..., Fei Wang, Heng Yang
**arXiv:** [2604.24622](https://arxiv.org/abs/2604.24622)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Flow-based vision-language-action (VLA) policies offer strong expressivity for action generation, but suffer from a fundamental inefficiency: multi-step inference is required to recover action structure from uninformative Gaussian noise, leading to a poor efficiency-quality trade-off under real-time constraints. We address this issue by rethinking the role of the starting point in generative action modeling. Instead of shortening the sampling trajectory, we propose CF-VLA, a coarse-to-fine two-stage formulation that restructures action generation into a coarse initialization step that constructs an action-aware starting point, followed by a single-step local refinement that corrects residual errors. Concretely, the coarse stage learns a conditional posterior over endpoint velocity to transform Gaussian noise into a structured initialization, while the fine stage performs a fixed-time refinement from this initialization. To stabilize training, we introduce a stepwise strategy that first learns a controlled coarse predictor and then performs joint optimization. Experiments on CALVIN and LIBERO show that our method establishes a strong efficiency-performance frontier under low-NFE (Number of Function Evaluations) regimes: it consistently outperforms existing NFE=2 methods, matches or surpasses the NFE=10 $\pi_{0.5}$ baseline on several metrics, reduces action sampling latency by 75.4%, and achieves the best average real-robot success rate of 83.0%, outperforming MIP by 19.5 points and $\pi_{0.5}$ by 4.0 points. These results suggest that structured, coarse-to-fine generation enables both strong performance and efficient inference. Our code is available at this https URL.

---

## 2. Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment

**Authors:** Kaijun Zhou, Qiwei Chen, Da Peng, ..., Xijun Li, Jinyu Gu
**arXiv:** [2604.24447](https://arxiv.org/abs/2604.24447)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models are promising for generalist robot control, but on-robot deployment is bottlenecked by real-time inference under tight cost and energy budgets. Most prior evaluations rely on desktop-grade GPUs, obscuring the trade-offs and opportunities offered by heterogeneous edge accelerators (GPUs/XPUs/NPUs). We present a systematic analysis for low-cost VLA deployment via model-hardware co-characterization. First, we build a cross-accelerator leaderboard and evaluate model-hardware pairs under CET (Cost, Energy, Time), showing that right-sized edge devices can be more cost-/energy-efficient than flagship GPUs while meeting control-rate constraints. Second, using in-depth profiling, we uncover a consistent two-phase inference pattern: a compute-bound VLM backbone followed by a memory-bound Action Expert, which induces phase-dependent underutilization and hardware inefficiency. Finally, guided by these insights, we propose DP-Cache and V-AEFusion to reduce diffusion redundancy and enable asynchronous pipeline parallelism, achieving up to 2.9x speedup on GPUs and 6x on edge NPUs with only marginal success degradation. The example leaderboard website is available at: this https URL.

---

## 3. AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation

**Authors:** Kai Yang, Zedong Chu, Yingnan Guo, ..., Xing Li, Mu Xu
**arXiv:** [2604.24086](https://arxiv.org/abs/2604.24086)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

While Vision-Language-Action (VLA) models have been demonstrated possessing strong zero-shot generalization for robot control, their massive parameter sizes typically necessitate cloud-based deployment. However, cloud deployment introduces network jitter and inference latency, which can induce severe spatiotemporal misalignment in mobile navigation under continuous displacement, so that the stale intents expressed in past ego frames may become spatially incorrect in the current frame and lead to collisions. To address this issue, we propose AsyncShield, a plug-and-play asynchronous control framework. AsyncShield discards traditional black-box time-series prediction in favor of a deterministic physical white-box spatial mapping. By maintaining a temporal pose buffer and utilizing kinematic transformations, the system accurately converts temporal lag into spatial pose offsets to restore the VLA's original geometric intent. To balance intent restoration fidelity and physical safety, the edge adaptation is formulated as a constrained Markov decision process (CMDP). Solved via the PPO-Lagrangian algorithm, a reinforcement learning adapter dynamically trades off between tracking the VLA intent and responding to high-frequency LiDAR obstacle avoidance hard constraints. Furthermore, benefiting from a standardized universal sub-goal interface, domain randomization, and perception-level adaptation via Collision Radius Inflation, AsyncShield operates as a lightweight, plug-and-play module. Simulation and real-world experiments demonstrate that, without fine-tuning any cloud-based foundation models, the framework exhibits zero-shot and robust generalization capabilities, effectively improving the success rate and physical safety of asynchronous navigation.

---

## 4. Emotion-Conditioned Short-Horizon Human Pose Forecasting with a Lightweight Predictive World Model

**Authors:** Jingni Huang, Peter Bloodsworth
**arXiv:** [2604.23532](https://arxiv.org/abs/2604.23532)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Short-term human pose prediction plays a crucial role in interactive systems, assistive robots, and emotion-aware human-computer interaction[1-3]. While current trajectory prediction models primarily rely on geometric motion cues, they often overlook the underlying emotional signals influencing human motion dynamics[4-5]. This paper investigates whether facial expression-derived emotion embeddings can provide auxiliary conditional signals for short-term pose prediction. To further evaluate multimodal conditionation in a recursive prediction setting, we propose a lightweight autoregressive predictive world model that performs 15-step rolling pose prediction. This framework combines pose keypoints with emotion embeddings through a learnable gating mechanism and performs autoregressive unfolding prediction using a recurrent sequence model based on a two-layer LSTM architecture. Experiments were conducted on two small-scale pose-emotion video datasets: controlled motion sequences with minimal facial expression changes and, natural emotion-driven motion sequences with considerable facial expression changes. The results show that simple multimodal fusion does not consistently improve prediction accuracy, while normalized gating fusion significantly enhances the performance of emotion-driven motion sequences. Furthermore, counterfactual perturbation experiments demonstrate that the predicted trajectory exhibits measurable sensitivity to changes in multimodal input, suggesting that facial expression embeddings act as auxiliary conditional signals rather than redundant features. In summary, these results indicate that incorporating facial expression-derived emotion embeddings into emotion-conditional short-term pose prediction based on a lightweight predictive world model architecture is a feasible approach.

---

## 5. Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines

**Authors:** Ziyao Wang, Bingying Wang, Hanrong Zhang, ..., Wanghao Ye, Ang Li
**arXiv:** [2604.23001](https://arxiv.org/abs/2604.23001)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Despite remarkable progress in Vision--Language--Action (VLA) models, a central bottleneck remains underexamined: the data infrastructure that underlies embodied learning. In this survey, we argue that future advances in VLA will depend less on model architecture and more on the co-design of high-fidelity data engines and structured evaluation protocols. To this end, we present a systematic, data-centric analysis of VLA research organized around three pillars: datasets, benchmarks, and data engines. For datasets, we categorize real-world and synthetic corpora along embodiment diversity, modality composition, and action space formulation, revealing a persistent fidelity-cost trade-off that fundamentally constrains large-scale collection. For benchmarks, we analyze task complexity and environment structure jointly, exposing structural gaps in compositional generalization and long-horizon reasoning evaluation that existing protocols fail to address. For data engines, we examine simulation-based, video-reconstruction, and automated task-generation paradigms, identifying their shared limitations in physical grounding and sim-to-real transfer. Synthesizing these analyses, we distill four open challenges: representation alignment, multimodal supervision, reasoning assessment, and scalable data generation. Addressing them, we argue, requires treating data infrastructure as a first-class research problem rather than a background concern.

---

## 6. RL Token: Bootstrapping Online RL with Vision-Language-Action Models

**Authors:** Charles Xu, Jost Tobias Springenberg, Michael Equi, ..., Sergey Levine, Liyiming Ke
**arXiv:** [2604.23073](https://arxiv.org/abs/2604.23073)
**Categories:** Machine Learning (cs.LG); Robotics (cs.RO)

Vision-language-action (VLA) models can learn to perform diverse manipulation skills "out of the box," but achieving the precision and speed that real-world tasks demand requires further fine-tuning -- for example, via reinforcement learning (RL). We introduce a lightweight method that enables sample-efficient online RL fine-tuning of pretrained VLAs using just a few hours of real-world practice. We (1) adapt the VLA to expose an "RL token," a compact readout representation that preserves task-relevant pretrained knowledge while serving as an efficient interface for online RL, and (2) train a small actor-critic head on this RL token to refine the actions, while anchoring the learned policy to the VLA. Online RL with the RL token (RLT) makes it possible to fine-tune even large VLAs with RL quickly and efficiently. Across four real-robot tasks (screw installation, zip tie fastening, charger insertion, and Ethernet insertion), RLT improves the speed on the hardest part of the task by up to 3x and raises success rates significantly within minutes to a few hours of practice. It can even surpass the speed of human teleoperation on some of the tasks.

---

## 7. $M^2$-VLA: Boosting Vision-Language Models for Generalizable Manipulation via Layer Mixture and Meta-Skills

**Authors:** Siyao Xiao, Yuhong Zhang, Zhifang Liu, ..., Jia Jia, Haoqian Wang
**arXiv:** [2604.24182](https://arxiv.org/abs/2604.24182)
**Categories:** Robotics (cs.RO)

Current Vision-Language-Action (VLA) models predominantly rely on end-to-end fine-tuning. While effective, this paradigm compromises the inherent generalization capabilities of Vision-Language Models (VLMs) and incurs catastrophic forgetting. To address these limitations, we propose $M^2$-VLA, which demonstrates that a generalized VLM is able to serve as a powerful backbone for robotic manipulation directly. However, it remains a key challenge to bridge the gap between the high-level semantic understanding of VLMs and the precise requirements of robotic control. To overcome this, we introduce the Mixture of Layers (MoL) strategy that selectively extracts task-critical information from dense semantic features. Furthermore, to facilitate efficient trajectory learning under constrained model capacity, we propose a Meta Skill Module (MSM) that integrates strong inductive biases. Extensive experiments in both simulated and real-world environments demonstrate the effectiveness of our approach. Furthermore, generalization and ablation studies validate the architecture's zero-shot capabilities and confirm the contribution of each key component. Our code and pre-trained models will be made publicly available.

---

## 8. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

**Authors:** Qi Li, Bo Yin, Weiqi Huang, ..., Weihao Yu, Xinchao Wang
**arXiv:** [2604.23775](https://arxiv.org/abs/2604.23775)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied intelligence. This shift raises a new class of safety challenges, stemming from the embodied nature of VLA systems, including irreversible physical consequences, a multimodal attack surface across vision, language, and state, real-time latency constraints on defense, error propagation over long-horizon trajectories, and vulnerabilities in the data supply chain. Yet the literature remains fragmented across robotic learning, adversarial machine learning, AI alignment, and autonomous systems safety. This survey provides a unified and up-to-date overview of safety in Vision-Language-Action models. We organize the field along two parallel timing axes, attack timing (training-time vs. inference-time and defense timing (training-time vs. inference-time, linking each class of threat to the stage at which it can be mitigated. We first define the scope of VLA safety, distinguishing it from text-only LLM safety and classical robotic safety, and review the foundations of VLA models, including architectures, training paradigms, and inference mechanisms. We then examine the literature through four lenses: Attacks, Defenses, Evaluation, and Deployment. We survey training-time threats such as data poisoning and backdoors, as well as inference-time attacks including adversarial patches, cross-modal perturbations, semantic jailbreaks, and freezing attacks. We review training-time and runtime defenses, analyze existing benchmarks and metrics, and discuss safety challenges across six deployment domains. Finally, we highlight key open problems, including certified robustness for embodied trajectories, physically realizable defenses, safety-aware training, unified runtime safety architectures, and standardized evaluation.

---

## 9. Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models

**Authors:** Jimin Lee, Huiwon Jang, Myungkyu Koo, Jungwoo Park, Jinwoo Shin
**arXiv:** [2604.23272](https://arxiv.org/abs/2604.23272)
**Categories:** Robotics (cs.RO)

Humans understand and interact with the real world by relying on diverse physical feedback beyond visual perception. Motivated by this, recent approaches attempt to incorporate physical sensory signals into Vision-Language-Action models (VLAs). However, they typically focus on a single type of physical signal, failing to capture the heterogeneous and complementary nature of real-world interactions. In this paper, we propose MoSS, a modular sensory stream framework that adapts VLAs to leverage multiple sensory signals for action prediction. Specifically, we introduce decoupled modality streams that integrate heterogeneous physical signals into the action stream via joint cross-modal self-attention. To enable stable incorporation of new modalities, we adopt a two-stage training scheme that freezes pretrained VLA parameters in the early stage. Furthermore, to better capture contact interaction dynamics, we incorporate an auxiliary task that predicts future physical signals. Through extensive real-world experiments, we demonstrate that MoSS successfully augments VLAs to leverage diverse physical signals (i.e., tactile and torque), integrating multiple signals to achieve synergistic performance gains.

---

## 10. Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training

**Authors:** Suning Huang, Jiaqi Shao, Ke Wang, ..., Mac Schwager, Jeannette Bohg
**arXiv:** [2604.23121](https://arxiv.org/abs/2604.23121)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Have you ever post-trained a generalist vision-language-action (VLA) policy on a small demonstration dataset, only to find that it stops responding to new instructions and is limited to behaviors observed during post-training? We identify this phenomenon as lock-in: after low-data, supervised fine-tuning (SFT), the policy becomes overly specialized to the post-training data and fails to generalize to novel instructions, manifesting as concept lock-in (fixation on training objects/attributes) and spatial lock-in (fixation on training spatial targets). Many existing remedies introduce additional supervision signals, such as those derived from foundation models or auxiliary objectives, or rely on augmented datasets to recover generalization. In this paper, we show that the policy's internal pre-trained knowledge is sufficient: DeLock mitigates lock-in by preserving visual grounding during post-training and applying test-time contrastive prompt guidance to steer the policy's denoising dynamics according to novel instructions. Across eight simulation and real-world evaluations, DeLock consistently outperforms strong baselines and matches or exceeds the performance of a state-of-the-art generalist policy post-trained with substantially more curated demonstrations.

---
