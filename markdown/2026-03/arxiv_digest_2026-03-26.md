# arXiv Daily Digest — 2026-03-26

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 11

---

## 1. AI-Supervisor: Autonomous AI Research Supervision via a Persistent Research World Model

**Authors:** Yunbo Long
**arXiv:** [2603.24402](https://arxiv.org/abs/2603.24402)
**Categories:** Artificial Intelligence (cs.AI)

Existing automated research systems operate as stateless, linear pipelines -- generating outputs without maintaining any persistent understanding of the research landscape they navigate. They process papers sequentially, propose ideas without structured gap analysis, and lack mechanisms for agents to verify, challenge, or refine each other's findings. We present \textbf{AI-Supervisor}, a multi-agent orchestration framework where specialized agents provide end-to-end AI research supervision driven by human interests -- from literature review through gap discovery, method development, evaluation, and paper writing -- through autonomous exploration and self-correcting updates of research knowledge. Unlike sequential pipelines, AI-Supervisor maintains a continuously evolving \emph{Research World Model}, implemented as a Knowledge Graph, that captures methods, benchmarks, known limitations, and unexplored gaps, serving as shared memory across all agents and enabling agents to explore and build upon a structured understanding of the research landscape. The framework introduces three architectural contributions: (1) \emph{structured gap discovery} that decomposes methods into core modules, validates their performance across benchmarks, and maps the specific gaps each module creates; (2) \emph{self-correcting discovery loops} that probe why modules succeed on certain problems and fail on others, whether benchmarks carry hidden biases, and whether evaluation protocols remain adequate for emerging challenges; and (3) \emph{self-improving development loops} governed by cross-domain mechanism search that iteratively targets failing modules by finding solutions from other scientific fields. All agents operate under a \emph{consensus mechanism} where independent findings are corroborated before being committed to the Research World Model.

---

## 2. DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving

**Authors:** Pengxuan Yang, Yupeng Zheng, Deheng Qian, ..., Yifeng Pan, Dongbin Zhao
**arXiv:** [2603.24587](https://arxiv.org/abs/2603.24587)
**Categories:** Machine Learning (cs.LG); Robotics (cs.RO)

We introduce DreamerAD, the first latent world model framework that enables efficient reinforcement learning for autonomous driving by compressing diffusion sampling from 100 steps to 1 - achieving 80x speedup while maintaining visual interpretability. Training RL policies on real-world driving data incurs prohibitive costs and safety risks. While existing pixel-level diffusion world models enable safe imagination-based training, they suffer from multi-step diffusion inference latency (2s/frame) that prevents high-frequency RL interaction. Our approach leverages denoised latent features from video generation models through three key mechanisms: (1) shortcut forcing that reduces sampling complexity via recursive multi-resolution step compression, (2) an autoregressive dense reward model operating directly on latent representations for fine-grained credit assignment, and (3) Gaussian vocabulary sampling for GRPO that constrains exploration to physically plausible trajectories. DreamerAD achieves 87.7 EPDMS on NavSim v2, establishing state-of-the-art performance and demonstrating that latent-space RL is effective for autonomous driving.

---

## 3. 3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, ..., Cong Huang, Kai Chen
**arXiv:** [2603.24393](https://arxiv.org/abs/2603.24393)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models leverage Multimodal Large Language Models (MLLMs) for robotic control, but recent studies reveal that MLLMs exhibit limited spatial intelligence due to training predominantly on 2D data, resulting in inadequate 3D perception for manipulation tasks. While recent approaches incorporate specialized 3D vision models such as VGGT to enhance spatial understanding, they employ diverse integration mechanisms without systematic investigation, leaving the optimal fusion strategy unclear. We conduct a comprehensive pilot study comparing nine VGGT integration schemes on standardized benchmarks and find that semantic-conditioned gated fusion, which adaptively balances 2D semantic and 3D geometric features based on task context, achieved the strongest performance among all nine evaluated fusion schemes in our pilot study. We present 3D-Mix, a plug-and-play module that integrates into diverse VLA architectures (GR00T-style and $\pi$-style) without modifying existing MLLM or action expert components. Experiments across six MLLM series (nine model variants, 2B--8B parameters) on SIMPLER and LIBERO show that 3D-Mix delivers consistent performance gains, averaging +7.0% on the out-of-domain (OOD) SIMPLER benchmark across all nine GR00T-style variants, establishing a principled approach for enhancing spatial intelligence in VLA systems.

---

## 4. SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation

**Authors:** Zhuoran Li, Zhiyang Li, Kaijun Zhou, Jinyu Gu
**arXiv:** [2603.24060](https://arxiv.org/abs/2603.24060)
**Categories:** Robotics (cs.RO)

Despite the promise of Vision-Language-Action (VLA) models as generalist robotic controllers, their robustness against perceptual noise and environmental variations in out-of-distribution (OOD) tasks remains fundamentally limited by the absence of long-term memory, causal failure attribution, and dynamic intervention capability. To address this, we propose SOMA, a Strategic Orchestration and Memory-Augmented System that upgrades frozen VLA policies for robust in-context adaptation without parameter fine-tuning. Specifically, SOMA operates through an online pipeline of contrastive Dual-Memory Retrieval-Augmented Generation (RAG), an Attribution-Driven Large-Language-Model (LLM) Orchestrator, and extensible Model Context Protocol (MCP) interventions, while an offline Memory Consolidation module continuously distills the execution traces into reliable priors. Experimental evaluations across three backbone models (pi0, pi0.5, and SmolVLA) on LIBERO-PRO and our proposed LIBERO-SOMA benchmarks demonstrate that SOMA achieves an average absolute success rate gain of 56.6%. This includes a significant absolute improvement of 89.1% in long-horizon task chaining. Project page and source code are available at: this https URL.

---

## 5. TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models

**Authors:** Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai, ..., Liang Lin, Guangrun Wang
**arXiv:** [2603.24584](https://arxiv.org/abs/2603.24584)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision--Language--Action (VLA) policies have shown strong progress in mapping language instructions and visual observations to robotic actions, yet their reliability degrades in cluttered scenes with distractors. By analyzing failure cases, we find that many errors do not arise from infeasible motions, but from instance-level grounding failures: the policy often produces a plausible grasp trajectory that lands slightly off-target or even on the wrong object instance. To address this issue, we propose TAG (Target-Agnostic Guidance), a simple inference-time guidance mechanism that explicitly reduces distractor- and appearance-induced bias in VLA policies. Inspired by classifier-free guidance (CFG), TAG contrasts policy predictions under the original observation and an object-erased observation, and uses their difference as a residual steering signal that strengthens the influence of object evidence in the decision process. TAG does not require modifying the policy architecture and can be integrated with existing VLA policies with minimal training and inference changes. We evaluate TAG on standard manipulation benchmarks, including LIBERO, LIBERO-Plus, and VLABench, where it consistently improves robustness under clutter and reduces near-miss and wrong-object executions.

---

## 6. Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving

**Authors:** Linbo Wang, Yupeng Zheng, Qiang Chen, ..., Yifeng Pan, Dongbin Zhao
**arXiv:** [2603.24581](https://arxiv.org/abs/2603.24581)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

We introduce Latent-WAM, an efficient end-to-end autonomous driving framework that achieves strong trajectory planning through spatially-aware and dynamics-informed latent world representations. Existing world-model-based planners suffer from inadequately compressed representations, limited spatial understanding, and underutilized temporal dynamics, resulting in sub-optimal planning under constrained data and compute budgets. Latent-WAM addresses these limitations with two core modules: a Spatial-Aware Compressive World Encoder (SCWE) that distills geometric knowledge from a foundation model and compresses multi-view images into compact scene tokens via learnable queries, and a Dynamic Latent World Model (DLWM) that employs a causal Transformer to autoregressively predict future world status conditioned on historical visual and motion representations. Extensive experiments on NAVSIM v2 and HUGSIM demonstrate new state-of-the-art results: 89.3 EPDMS on NAVSIM v2 and 28.9 HD-Score on HUGSIM, surpassing the best prior perception-free method by 3.2 EPDMS with significantly less training data and a compact 104M-parameter model.

---

## 7. Toward Physically Consistent Driving Video World Models under Challenging Trajectories

**Authors:** Jiawei Zhou, Zhenxin Zhu, Lingyi Du, ..., Haiyang Sun, Yu Li
**arXiv:** [2603.24506](https://arxiv.org/abs/2603.24506)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video generation models have shown strong potential as world models for autonomous driving simulation. However, existing approaches are primarily trained on real-world driving datasets, which mostly contain natural and safe driving scenarios. As a result, current models often fail when conditioned on challenging or counterfactual trajectories-such as imperfect trajectories generated by simulators or planning systems-producing videos with severe physical inconsistencies and artifacts. To address this limitation, we propose PhyGenesis, a world model designed to generate driving videos with high visual fidelity and strong physical consistency. Our framework consists of two key components: (1) a physical condition generator that transforms potentially invalid trajectory inputs into physically plausible conditions, and (2) a physics-enhanced video generator that produces high-fidelity multi-view driving videos under these conditions. To effectively train these components, we construct a large-scale, physics-rich heterogeneous dataset. Specifically, in addition to real-world driving videos, we generate diverse challenging driving scenarios using the CARLA simulator, from which we derive supervision signals that guide the model to learn physically grounded dynamics under extreme conditions. This challenging-trajectory learning strategy enables trajectory correction and promotes physically consistent video generation. Extensive experiments demonstrate that PhyGenesis consistently outperforms state-of-the-art methods, especially on challenging trajectories. Our project page is available at: this https URL.

---

## 8. CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents

**Authors:** Xiangru Jian, Shravan Nayak, Kevin Qinghong Lin, ..., Spandana Gella, Sai Rajeswar
**arXiv:** [2603.24440](https://arxiv.org/abs/2603.24440)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Computer-use agents (CUAs) hold great promise for automating complex desktop workflows, yet progress toward general-purpose agents is bottlenecked by the scarcity of continuous, high-quality human demonstration videos. Recent work emphasizes that continuous video, not sparse screenshots, is the critical missing ingredient for scaling these agents. However, the largest existing open dataset, ScaleCUA, contains only 2 million screenshots, equating to less than 20 hours of video. To address this bottleneck, we introduce CUA-Suite, a large-scale ecosystem of expert video demonstrations and dense annotations for professional desktop computer-use agents. At its core is VideoCUA, which provides approximately 10,000 human-demonstrated tasks across 87 diverse applications with continuous 30 fps screen recordings, kinematic cursor traces, and multi-layerfed reasoning annotations, totaling approximately 55 hours and 6 million frames of expert video. Unlike sparse datasets that capture only final click coordinates, these continuous video streams preserve the full temporal dynamics of human interaction, forming a superset of information that can be losslessly transformed into the formats required by existing agent frameworks. CUA-Suite further provides two complementary resources: UI-Vision, a rigorous benchmark for evaluating grounding and planning capabilities in CUAs, and GroundCUA, a large-scale grounding dataset with 56K annotated screenshots and over 3.6 million UI element annotations. Preliminary evaluation reveals that current foundation action models struggle substantially with professional desktop applications (~60% task failure rate). Beyond evaluation, CUA-Suite's rich multimodal corpus supports emerging research directions including generalist screen parsing, continuous spatial control, video-based reward modeling, and visual world models. All data and models are publicly released.

---

## 9. GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents

**Authors:** Yunzhe Wang, Runhui Xu, Kexin Zheng, ..., Soham Hans, Volkan Ustun
**arXiv:** [2603.24329](https://arxiv.org/abs/2603.24329)
**Categories:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Multimodal LLMs are increasingly deployed as perceptual backbones for autonomous agents in 3D environments, from robotics to virtual worlds. These applications require agents to perceive rapid state changes, attribute actions to the correct entities, and reason about concurrent multi-agent behaviors from a first-person perspective, capabilities that existing benchmarks do not adequately evaluate. We introduce GameplayQA, a framework for evaluating agentic-centric perception and reasoning through video understanding. Specifically, we densely annotate multiplayer 3D gameplay videos at 1.22 labels/second, with time-synced, concurrent captions of states, actions, and events structured around a triadic system of Self, Other Agents, and the World, a natural decomposition for multi-agent environments. From these annotations, we refined 2.4K diagnostic QA pairs organized into three levels of cognitive complexity, accompanied by a structured distractor taxonomy that enables fine-grained analysis of where models hallucinate. Evaluation of frontier MLLMs reveals a substantial gap from human performance, with common failures in temporal and cross-video grounding, agent-role attribution, and handling the decision density of the game. We hope GameplayQA stimulates future research at the intersection of embodied AI, agentic perception, and world modeling.

---

## 10. Unleashing Vision-Language Semantics for Deepfake Video Detection

**Authors:** Jiawen Zhu, Yunqi Miao, Xueyi Zhang, Jiankang Deng, Guansong Pang
**arXiv:** [2603.24454](https://arxiv.org/abs/2603.24454)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Recent Deepfake Video Detection (DFD) studies have demonstrated that pre-trained Vision-Language Models (VLMs) such as CLIP exhibit strong generalization capabilities in detecting artifacts across different identities. However, existing approaches focus on leveraging visual features only, overlooking their most distinctive strength -- the rich vision-language semantics embedded in the latent space. We propose VLAForge, a novel DFD framework that unleashes the potential of such cross-modal semantics to enhance model's discriminability in deepfake detection. This work i) enhances the visual perception of VLM through a ForgePerceiver, which acts as an independent learner to capture diverse, subtle forgery cues both granularly and holistically, while preserving the pretrained Vision-Language Alignment (VLA) knowledge, and ii) provides a complementary discriminative cue -- Identity-Aware VLA score, derived by coupling cross-modal semantics with the forgery cues learned by ForgePerceiver. Notably, the VLA score is augmented by an identity prior-informed text prompting to capture authenticity cues tailored to each identity, thereby enabling more discriminative cross-modal semantics. Comprehensive experiments on video DFD benchmarks, including classical face-swapping forgeries and recent full-face generation forgeries, demonstrate that our VLAForge substantially outperforms state-of-the-art methods at both frame and video levels. Code is available at this https URL.

---

## 11. Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis

**Authors:** Dayou Li, Jiuzhou Lei, Hao Wang, ..., Minghui Zheng, Zhiwen Fan
**arXiv:** [2603.13528](https://arxiv.org/abs/2603.13528)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

While recent foundation models have significantly advanced robotic manipulation, these systems still struggle to autonomously recover from execution errors. Current failure-learning paradigms rely on either costly and unsafe real-world data collection or simulator-based perturbations, which introduce a severe sim-to-real gap. Furthermore, existing visual analyzers predominantly output coarse, binary diagnoses rather than the executable, trajectory-level corrections required for actual recovery. To bridge the gap between failure diagnosis and actionable recovery, we introduce Dream2Fix, a framework that synthesizes photorealistic, counterfactual failure rollouts directly from successful real-world demonstrations. By perturbing actions within a generative world model, Dream2Fix creates paired failure-correction data without relying on simulators. To ensure the generated data is physically viable for robot learning, we implement a structured verification mechanism that strictly filters rollouts for task validity, visual coherence, and kinematic safety. This engine produces a high-fidelity dataset of over 120k paired samples. Using this dataset, we fine-tune a vision-language model to jointly predict failure types and precise recovery trajectories, mapping visual anomalies directly to corrective actions. Extensive real-world robotic experiments show our approach achieves state-of-the-art correction accuracy, improving from 19.7% to 81.3% over prior baselines, and successfully enables zero-shot closed-loop failure recovery in physical deployments.

---
