# arXiv Daily Digest — 2026-04-06

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 8

---

## 1. InCoder-32B-Thinking: Industrial Code World Model for Thinking

**Authors:** Jian Yang, Wei Zhang, Jiajun Wu, ..., Bryan Dai, Weifeng Lv
**arXiv:** [2604.03144](https://arxiv.org/abs/2604.03144)
**Categories:** Hardware Architecture (cs.AR); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Industrial software development across chip design, GPU optimization, and embedded systems lacks expert reasoning traces showing how engineers reason about hardware constraints and timing semantics. In this work, we propose InCoder-32B-Thinking, trained on the data from the Error-driven Chain-of-Thought (ECoT) synthesis framework with an industrial code world model (ICWM) to generate reasoning traces. Specifically, ECoT generates reasoning chains by synthesizing the thinking content from multi-turn dialogue with environmental error feedback, explicitly modeling the error-correction process. ICWM is trained on domain-specific execution traces from Verilog simulation, GPU profiling, etc., learns the causal dynamics of how code affects hardware behavior, and enables self-verification by predicting execution outcomes before actual compilation. All synthesized reasoning traces are validated through domain toolchains, creating training data matching the natural reasoning depth distribution of industrial tasks. Evaluation on 14 general (81.3% on LiveCodeBench v5) and 9 industrial benchmarks (84.0% in CAD-Coder and 38.0% on KernelBench) shows InCoder-32B-Thinking achieves top-tier open-source results across all this http URL Optimization

---

## 2. Hierarchical Planning with Latent World Models

**Authors:** Wancong Zhang, Basile Terver, Artem Zholus, ..., Yann LeCun, Nicolas Ballas
**arXiv:** [2604.03208](https://arxiv.org/abs/2604.03208)
**Categories:** Machine Learning (cs.LG)

Model predictive control (MPC) with learned world models has emerged as a promising paradigm for embodied control, particularly for its ability to generalize zero-shot when deployed in new environments. However, learned world models often struggle with long-horizon control due to the accumulation of prediction errors and the exponentially growing search space. In this work, we address these challenges by learning latent world models at multiple temporal scales and performing hierarchical planning across these scales, enabling long-horizon reasoning while substantially reducing inference-time planning complexity. Our approach serves as a modular planning abstraction that applies across diverse latent world-model architectures and domains. We demonstrate that this hierarchical approach enables zero-shot control on real-world non-greedy robotic tasks, achieving a 70% success rate on pick-&-place using only a final goal specification, compared to 0% for a single-level world model. In addition, across physics-based simulated environments including push manipulation and maze navigation, hierarchical planning achieves higher success while requiring up to 4x less planning-time compute.

---

## 3. VoxelCodeBench: Benchmarking 3D World Modeling Through Code Generation

**Authors:** Yan Zheng, Florian Bordes
**arXiv:** [2604.02580](https://arxiv.org/abs/2604.02580)
**Categories:** Machine Learning (cs.LG)

Evaluating code generation models for 3D spatial reasoning requires executing generated code in realistic environments and assessing outputs beyond surface-level correctness. We introduce a platform VoxelCode, for analyzing code generation capabilities for 3D understanding and environment creation. Our platform integrates natural language task specification, API-driven code execution in Unreal Engine, and a unified evaluation pipeline supporting both automated metrics and human assessment. To demonstrate its utility, we construct VoxelCodeBench, a benchmark of voxel manipulation tasks spanning three reasoning dimensions: symbolic interpretation, geometric construction, and artistic composition. Evaluating leading code generation models, we find that producing executable code is far easier than producing spatially correct outputs, with geometric construction and multi-object composition proving particularly challenging. By open-sourcing our platform and benchmark, we provide the community with extensible infrastructure for developing new 3D code generation benchmarks and probing spatial reasoning in future models.

---

## 4. The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling

**Authors:** Takuya Shiba
**arXiv:** [2604.03191](https://arxiv.org/abs/2604.03191)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Scaling Vision-Language-Action (VLA) models by upgrading the vision encoder is expected to improve downstream manipulation performance--as it does in vision-language modeling. We show that this expectation fails when actions are represented as discrete tokens, and explain why through an information-theoretic principle we call the Compression Gap: in any visuomotor pipeline, scaling behavior is governed by the location of the tightest information bottleneck. When actions are continuous (e.g., Diffusion Policy), the vision encoder is the binding constraint, and upgrading it directly improves performance. When actions are discretized through a fixed-capacity codebook (e.g., OAT), the codebook becomes the binding constraint, and encoder improvements cannot propagate past it--regardless of how rich the upstream representation is. We validate this principle on the LIBERO benchmark with three lines of evidence: a factorial experiment showing that encoder upgrades improve Diffusion Policy by over 21 percentage points while OAT gains are substantially attenuated across model scales; an encoder quality gradient across four encoders confirming that Diffusion Policy tracks encoder quality monotonically while OAT remains flat; and a codebook size experiment demonstrating that relaxing codebook capacity partially recovers encoder sensitivity, providing causal evidence for the bottleneck hypothesis. Our findings reveal that scaling in Physical AI requires identifying where information bottlenecks lie in the pipeline, rather than uniformly increasing model or data size.

---

## 5. Open-Loop Planning, Closed-Loop Verification: Speculative Verification for VLA

**Authors:** Zihua Wang, Zhitao Lin, Ruibo Li, ..., Siya Mi, Xiu-Shen Wei
**arXiv:** [2604.02965](https://arxiv.org/abs/2604.02965)
**Categories:** Robotics (cs.RO); Computation and Language (cs.CL)

Vision-Language-Action (VLA) models, as large foundation models for embodied control, have shown strong performance in manipulation tasks. However, their performance comes at high inference cost. To improve efficiency, recent methods adopt action chunking, which predicts a sequence of future actions for open-loop execution. Although effective for reducing computation, open-loop execution is sensitive to environmental changes and prone to error accumulation due to the lack of close-loop feedback. To address this limitation, we propose Speculative Verification for VLA Control (SV-VLA), a framework that combines efficient open-loop long-horizon planning with lightweight closed-loop online verification. Specifically, SV-VLA uses a heavy VLA as a low-frequency macro-planner to generate an action chunk together with a planning context, while a lightweight verifier continuously monitors execution based on the latest observations. Conditioned on both the current observation and the planning context, the verifier compares the planned action against a closed-loop reference action and triggers replanning only when necessary. Experiments demonstrate that SV-VLA combines the efficiency of chunked prediction with the robustness of closed-loop control, enabling efficient and reliable VLA-based control in dynamic environments. Code is available: this https URL.

---

## 6. ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving

**Authors:** Zihao Sheng, Xin Ye, Jingru Luo, Sikai Chen, Liu Ren
**arXiv:** [2604.02714](https://arxiv.org/abs/2604.02714)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

End-to-end autonomous driving models based on Vision-Language-Action (VLA) architectures have shown promising results by learning driving policies through behavior cloning on expert demonstrations. However, imitation learning inherently limits the model to replicating observed behaviors without exploring diverse driving strategies, leaving it brittle in novel or out-of-distribution scenarios. Reinforcement learning (RL) offers a natural remedy by enabling policy exploration beyond the expert distribution. Yet VLA models, typically trained on offline datasets, lack directly observable state transitions, necessitating a learned world model to anticipate action consequences. In this work, we propose a unified understanding-and-generation framework that leverages world modeling to simultaneously enable meaningful exploration and provide dense supervision. Specifically, we augment trajectory prediction with future RGB and depth image generation as dense world modeling objectives, requiring the model to learn fine-grained visual and geometric representations that substantially enrich the planning backbone. Beyond serving as a supervisory signal, the world model further acts as a source of intrinsic reward for policy exploration: its image prediction uncertainty naturally measures a trajectory's novelty relative to the training distribution, where high uncertainty indicates out-of-distribution scenarios that, if safe, represent valuable learning opportunities. We incorporate this exploration signal into a safety-gated reward and optimize the policy via Group Relative Policy Optimization (GRPO). Experiments on the NAVSIM and nuScenes benchmarks demonstrate the effectiveness of our approach, achieving a state-of-the-art PDMS score of 93.7 and an EPDMS of 88.8 on NAVSIM. The code and demo will be publicly available at this https URL.

---

## 7. Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model

**Authors:** Peiyan Li, Yixiang Chen, Yuan Xu, ..., Liang Wang, Tieniu Tan
**arXiv:** [2604.03181](https://arxiv.org/abs/2604.03181)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Robotic manipulation requires understanding both the 3D spatial structure of the environment and its temporal evolution, yet most existing policies overlook one or both. They typically rely on 2D visual observations and backbones pretrained on static image--text pairs, resulting in high data requirements and limited understanding of environment dynamics. To address this, we introduce MV-VDP, a multi-view video diffusion policy that jointly models the 3D spatio-temporal state of the environment. The core idea is to simultaneously predict multi-view heatmap videos and RGB videos, which 1) align the representation format of video pretraining with action finetuning, and 2) specify not only what actions the robot should take, but also how the environment is expected to evolve in response to those actions. Extensive experiments show that MV-VDP enables data-efficient, robust, generalizable, and interpretable manipulation. With only ten demonstration trajectories and without additional pretraining, MV-VDP successfully performs complex real-world tasks, demonstrates strong robustness across a range of model hyperparameters, generalizes to out-of-distribution settings, and predicts realistic future videos. Experiments on Meta-World and real-world robotic platforms demonstrate that MV-VDP consistently outperforms video-prediction--based, 3D-based, and vision--language--action models, establishing a new state of the art in data-efficient multi-task manipulation.

---

## 8. Learning Task-Invariant Properties via Dreamer: Enabling Efficient Policy Transfer for Quadruped Robots

**Authors:** Junyang Liang, Yuxuan Liu, Yabin Chang, ..., Changxin Huang, Jianqiang Li
**arXiv:** [2604.02911](https://arxiv.org/abs/2604.02911)
**Categories:** Robotics (cs.RO)

Achieving quadruped robot locomotion across diverse and dynamic terrains presents significant challenges, primarily due to the discrepancies between simulation environments and real-world conditions. Traditional sim-to-real transfer methods often rely on manual feature design or costly real-world fine-tuning. To address these limitations, this paper proposes the DreamTIP framework, which incorporates Task-Invariant Properties learning within the Dreamer world model architecture to enhance sim-to-real transfer capabilities. Guided by large language models, DreamTIP identifies and leverages Task-Invariant Properties, such as contact stability and terrain clearance, which exhibit robustness to dynamic variations and strong transferability across tasks. These properties are integrated into the world model as auxiliary prediction targets, enabling the policy to learn representations that are insensitive to underlying dynamic changes. Furthermore, an efficient adaptation strategy is designed, employing a mixed replay buffer and regularization constraints to rapidly calibrate to real-world dynamics while effectively mitigating representation collapse and catastrophic forgetting. Extensive experiments on complex terrains, including Stair, Climb, Tilt, and Crawl, demonstrate that DreamTIP significantly outperforms state-of-the-art baselines in both simulated and real-world environments. Our method achieves an average performance improvement of 28.1% across eight distinct simulated transfer tasks. In the real-world Climb task, the baseline method achieved only a 10\ success rate, whereas our method attained a 100% success rate. These results indicate that incorporating Task-Invariant Properties into Dreamer learning offers a novel solution for achieving robust and transferable robot locomotion.

---
