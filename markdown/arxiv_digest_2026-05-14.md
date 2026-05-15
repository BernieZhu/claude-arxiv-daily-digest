# arXiv Daily Digest — 2026-05-14

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 15

---

## 1. D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models

**Authors:** Yucheng Guo, Yongjian Guo, Zhong Guan, ..., Junwu Xiong, Yicheng Gong
**arXiv:** [2605.13276](https://arxiv.org/abs/2605.13276)
**Categories:** Artificial Intelligence (cs.AI); Robotics (cs.RO)

The rapid evolution of Embodied AI has enabled Vision-Language-Action (VLA) models to excel in multimodal perception and task execution. However, applying Reinforcement Learning (RL) to these massive models in large-scale distributed environments faces severe systemic bottlenecks, primarily due to the resource conflict between high-fidelity physical simulation and the intensive VRAM/bandwidth demands of deep learning. This conflict often leaves overall throughput constrained by execution-phase inefficiencies. To address these challenges, we propose D-VLA, a high-concurrency, low-latency distributed RL framework for large-scale embodied foundation models. D-VLA introduces "Plane Decoupling," physically isolating high-frequency training data from low-frequency weight control to eliminate interference between simulation and optimization. We further design a four-thread asynchronous "Swimlane" pipeline, enabling full parallel overlap of sampling, inference, gradient computation, and parameter distribution. Additionally, a dual-pool VRAM management model and topology-aware replication resolve memory fragmentation and optimize communication efficiency. Experiments on benchmarks like LIBERO show that D-VLA significantly outperforms mainstream RL frameworks in throughput and sampling efficiency for billion-parameter VLA models. In trillion-parameter scalability tests, our framework maintains exceptional stability and linear speedup, providing a robust system for high-performance general-purpose embodied agents.

---

## 2. Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models

**Authors:** Zixing Lei, Changxing Liu, Yichen Xiong, ..., Weixin Li, Siheng Chen
**arXiv:** [2605.13119](https://arxiv.org/abs/2605.13119)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action (VLA) models are effective robot action executors, but they remain limited on long-horizon tasks due to the dual burden of extended closed-loop planning and diverse physical operations. We therefore propose VLAs-as-Tools, a strategy that distributes this burden across a high-level vision language model (VLM) agent for temporal reasoning and a family of specialized VLA tools for diverse local physical operations. The VLM handles scene analysis, global planning, and recovery, while each VLA tool executes a bounded subtask. To tightly couple agent planning with VLA tool execution in long-horizon tasks, we introduce a VLA tool-family interface that exposes explicit tool selection and in-execution progress feedback, enabling efficient event-triggered agent replanning without continuous agent polling. To obtain diverse specialized VLA tools that faithfully follow agent invocations, we further propose Tool-Aligned Post-Training (TAPT), which constructs invocation-aligned training units for instruction following and adopts tool-family residual adapters for efficient tool specialization. Experiments show that VLAs-as-Tools improves the success rate of $\pi_{0.5}$ by 4.8 points on LIBERO-Long and 23.1 points on RoboTwin, and further enhances invocation fidelity by 15.0 points as measured by Non-biased Rate. Code will be released.

---

## 3. Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue

**Authors:** Vardhan Dongre, Dilek Hakkani-Tür
**arXiv:** [2605.12920](https://arxiv.org/abs/2605.12920)
**Categories:** Multiagent Systems (cs.MA); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Effective collaboration between embodied agents requires more than acting in a shared environment; it demands communication grounded in each agent's evolving understanding of the world. When agents can only partially observe their surroundings, coordination without communication is provably hard, but communication can, in principle, bridge this gap by allowing agents to share observations and align their world models. In this work, we examine whether LLM-based embodied agents actually realize the ability to communicate. We extend PARTNR, a benchmark for collaborative household robotics, with a natural-language dialogue channel that enables two agents with partial observability to communicate during task execution. To evaluate whether dialogue leads to genuine world-model alignment rather than superficial coordination, we propose a framework for measuring world-model alignment defined over per-agent world graphs: observation convergence (do private world models align over time?), information novelty (do messages convey what the partner lacks?), and belief-sensitive messaging (do agents model what their partner knows?). Our experiments across three LLMs reveal that dialogue reduces action conflicts 40 to 83 percentage points but degrades task success relative to silent coordination. Using our metrics, we characterize the gap between superficial coordination and genuine world-model alignment, and identify where current models fall on this spectrum.

---

## 4. Learning POMDP World Models from Observations with Language-Model Priors

**Authors:** Valentin Six, Frederik Panse, Mathis Fajeau, ..., Philipp Hennig, Bernhard Schölkopf
**arXiv:** [2605.13740](https://arxiv.org/abs/2605.13740)
**Categories:** Machine Learning (cs.LG)

Whether navigating a building, operating a robot, or playing a game, an agent that acts effectively in an environment must first learn an internal model of how that environment works. Partially-observable Markov decision processes (POMDPs) provide a flexible modeling class for such internal world models, but learning them from observation-action trajectories alone is challenging and typically requires extensive environment interaction. We ask whether language-model priors can reduce costly interaction by leveraging prior knowledge, and introduce \emph{Pinductor} (POMDP-inductor): an LLM proposes candidate POMDP models from a few observation-action trajectories and iteratively refines them to optimize a belief-based likelihood score. Despite using strictly less information, \emph{Pinductor} matches the performance and sample efficiency of LLM-based POMDP learning methods that assume privileged access to the hidden state, while significantly surpassing the sample efficiency of tabular POMDP baselines. Further results show that performance scales with LLM capability and degrades gracefully as semantic information about the environment is withheld. Together, these results position language-model priors as a practical tool for sample-efficient world-model learning under partial observability, and a step toward generalist agents in real-world environments. Code is available at this https URL.

---

## 5. JEDI: Joint Embedding Diffusion World Model for Online Model-Based Reinforcement Learning

**Authors:** Jing Yu Lim, Rushi Shah, Zarif Ikram, ..., Tze-Yun Leong, Dianbo Liu
**arXiv:** [2605.13013](https://arxiv.org/abs/2605.13013)
**Categories:** Machine Learning (cs.LG)

Diffusion world models have recently become competitive for online model-based reinforcement learning, but current approaches expose a tension: pixel diffusion is effective but computationally expensive while the latest latent diffusion approach improves efficiency yet performs subpar. The latter also relies on separately trained latents rather than the end-to-end world-model objectives that have driven much of modern MBRL progress. In particular, JEPA-style predictive representation learning has emerged as an especially promising direction for world modeling and MBRL. Concurrently, diffusion-style objectives have gained traction across multiple domains, with iterative refinement as a promising approach for multimodal and stochastic targets. Taken together, these trends motivate Joint Embedding DIffusion (JEDI), the first online end-to-end latent diffusion world model. JEDI learns its latent space directly from the diffusion denoising loss with a JEPA framework, using denoising to learn and predict future latents rather than relying on reconstruction and pretrained models. We provide a theoretical motivation showing that conventional JEPA objectives induce a predictive information bottleneck, and that conditional diffusion denoising admits a closely related predictive-compression decomposition. Empirically, JEDI is competitive on Atari100k and outperforms the baseline with seperately trained latents where directly comparable. Relative to the pixel diffusion baseline, JEDI uses 43% less VRAM, over 3$\times$ faster world-model sampling, and 2.5$\times$ faster training. JEDI also exhibits a markedly different task-level performance profile from the pixel baseline, suggesting that end-to-end predictive latents change more than compute alone.

---

## 6. Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs

**Authors:** Jiahui Niu, Kefan Gu, Yucheng Zhao, ..., Ying Wang, Huawei Li
**arXiv:** [2605.13778](https://arxiv.org/abs/2605.13778)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Diffusion-based vision-language-action models (dVLAs) are promising for embodied intelligence but are fundamentally limited in real-time deployment by the high latency of full inference. We propose Realtime-VLA FLASH, a speculative inference framework that eliminates most full inference calls during replanning by introducing a lightweight draft model with parallel verification via the main model's Action Expert and a phase-aware fallback mechanism that reverts to the full inference pipeline when needed. This design enables low-latency, high-frequency replanning without sacrificing reliability. Experiments show that on LIBERO, FLASH largely preserves task performance by replacing many 58.0 ms full-inference rounds with speculative rounds as fast as 7.8 ms, lowering task-level average inference latency to 19.1 ms (3.04x speedup). We additionally demonstrate effectiveness on real-world conveyor-belt sorting, highlighting its practical impact for latency-critical embodied tasks.

---

## 7. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, ..., Cong Huang, Kai Chen
**arXiv:** [2605.13757](https://arxiv.org/abs/2605.13757)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) policies are commonly trained from dense robot demonstration trajectories, often collected through teleoperation, by sampling every recorded frame as if it provided equally useful supervision. We argue that this convention creates a temporal supervision imbalance: long low-change segments dominate the training stream, while manipulation-critical transitions such as alignment, contact, grasping, and release appear only sparsely. We introduce FrameSkip, a data-layer frame selection framework that scores trajectory frames using action variation, visual-action coherence, task-progress priors, and gripper-transition preservation, then remaps training samples toward high-importance frames under a target retention ratio. Because FrameSkip operates only in the dataloader, it leaves the VLA architecture, action head, training objective, and inference procedure unchanged. Across RoboCasa-GR1, SimplerEnv, and LIBERO, FrameSkip improves the success-retention trade-off over full-frame training and simpler frame selection variants, achieving a macro-average success rate of 76.15% across the three benchmarks compared with 66.50% for full-frame training while using a compressed trajectory view that retains 20% of unique frames in the main setting.

---

## 8. Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models

**Authors:** Yiran Ling, Qing Lian, Jinghang Li, ..., Jie Liu, Lei Zhang
**arXiv:** [2605.13632](https://arxiv.org/abs/2605.13632)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

In this paper, we propose GTA-VLA(Guide, Think, Act), an interactive Vision-Language-Action (VLA) framework that enables spatially steerable embodied reasoning by allowing users to guide robot policies with explicit visual cues. Existing VLA models learn a direct "Sense-to-Act" mapping from multimodal observations to robot actions. While effective within the training distribution, such tightly coupled policies are brittle under out-of-domain (OOD) shifts and difficult to correct when failures occur. Although recent embodied Chain-of-Thought (CoT) approaches expose intermediate reasoning, they still lack a mechanism for incorporating human spatial guidance, limiting their ability to resolve visual ambiguities or recover from mistakes. To address this gap, our framework allows users to optionally guide the policy with spatial priors, such as affordance points, boxes, and traces, which the subsequent reasoning process can directly condition on. Based on these inputs, the model generates a unified spatial-visual Chain-of-Thought that integrates external guidance with internal task planning, aligning human visual intent with autonomous decision-making. For practical deployment, we further couple the reasoning module with a lightweight reactive action head for efficient action execution. Extensive experiments demonstrate the effectiveness of our approach. On the in-domain SimplerEnv WidowX benchmark, our framework achieves a state-of-the-art 81.2% success rate. Under OOD visual shifts and spatial ambiguities, a single visual interaction substantially improves task success over existing methods, highlighting the value of interactive reasoning for failure recovery in embodied control. Details of the project can be found here: this https URL

---

## 9. RotVLA: Rotational Latent Action for Vision-Language-Action Model

**Authors:** Qiwei Li, Xicheng Gong, Xinghang Li, ..., Jiahuan Zhou, Yadong Mu
**arXiv:** [2605.13403](https://arxiv.org/abs/2605.13403)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Latent Action Models (LAMs) have emerged as an effective paradigm for handling heterogeneous datasets during Vision-Language-Action (VLA) model pretraining, offering a unified action space across embodiments. However, existing LAMs often rely on discrete quantization encode and decode pipelines, which can lead to trivial frame reconstruction behavior, limited representational capacity, and a lack of physically meaningful structure. We introduce RotVLA, a VLA framework built on a continuous rotational latent action representation. Latent actions are modeled as elements of SO(n), providing continuity, compositionality, and structured geometry aligned with real-world action dynamics. A triplet frame learning framework further enforces meaningful temporal dynamics while avoiding degeneration. RotVLA consists of a VLM backbone and a flow-matching action head, pretrained on large-scale cross-embodiment robotic datasets and human videos with latent-action supervision. For downstream robot control, the flow-matching head is extended into a unified action expert that jointly denoises latent and robot actions. Here, latent actions serve as a latent planner, providing high-level guidance that conditions action generation. With only 1.7B parameters and 1700+ hours of pretraining data, RotVLA achieves 98.2% on LIBERO and 89.6% / 88.5% on RoboTwin2.0 under clean and randomized settings, respectively. It also demonstrates strong real-world performance on manipulation tasks, consistently outperforming existing VLA models.

---

## 10. BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning

**Authors:** Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, Xiangyu Xu
**arXiv:** [2605.13382](https://arxiv.org/abs/2605.13382)
**Categories:** Robotics (cs.RO)

While autoregressive (AR) Vision-Language-Action (VLA) models have demonstrated formidable reasoning capabilities in robotic tasks, their sequential decoding process often incurs high inference latency and may amplify error accumulation during long-horizon execution. Discrete Diffusion Language Models (dLLMs) provide a promising alternative through parallel token refinement, but their practical deployment in robotics remains limited by repeated denoising function evaluations (NFEs) and the difficulty of directly applying standard KV caching to bidirectional iterative decoding. To bridge these paradigms, we propose BlockVLA, a framework that adapts pretrained AR backbones into an efficient discrete diffusion policy through a block diffusion paradigm. BlockVLA maintains autoregressive dependencies at the block level while enabling parallel denoising within each block, thereby combining global causal coherence with local parallel generation. This design enables prefix KV-cache reuse across completed blocks, reduces the effective cost of iterative denoising, and provides a smoother transition from AR pretraining to diffusion-based policy fine-tuning. We conduct extensive evaluations on the LIBERO and SimplerEnv benchmarks. Experimental results demonstrate that our BlockVLA achieves a 3.3$\times$ inference acceleration over standard discrete diffusion baselines. Furthermore, our model exhibits superior training efficiency, with success rates converging substantially faster than baselines, a gain that is particularly pronounced in complex, long-horizon tasks, where BlockVLA achieves significant performance gains in the early stages of training. This work establishes Block Diffusion as a robust bridge between large-scale pretrained AR models and efficient, high-frequency real-time robotic control.

---

## 11. What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models

**Authors:** Yuanfang Peng, Jingjing Fu, Chuheng Zhang, ..., Jun Zhang, Rui Wang
**arXiv:** [2605.13105](https://arxiv.org/abs/2605.13105)
**Categories:** Robotics (cs.RO)

Reinforcement learning (RL) fine-tuning has shown promise for Vision-Language-Action (VLA) models in robotic manipulation, but deployment-time visual shifts pose practical challenges. A key difficulty is that standard task rewards supervise task success, but offer limited guidance on whether a visual change is task-irrelevant or changes the behavior required for manipulation. We propose PAIR-VLA (Paired Action Invariance & Sensitivity for Visually Robust VLA), an RL fine-tuning framework to address this difficulty by adding two auxiliary objectives over paired visual variants during PPO optimization: an invariance term that reduces the discrepancy between action distributions for a task-preserving pair (e.g., different distractors), and a sensitivity objective that encourages separable action distributions for a task-altering pair (e.g., target object in a different pose). Together, these objectives turn visual variants from mere observation diversity into behavior-level guidance on policy responses during RL fine-tuning. We evaluate on ManiSkill3 across two representative VLA architectures, OpenVLA and $\pi_{0.5}$, under diverse out-of-distribution visual shifts including unseen distractors, texture changes, target object pose variation, viewpoint shifts, and lighting changes. Our method consistently improves over standard PPO, achieving average improvements of 16.62% on $\pi_{0.5}$ and 9.10% on OpenVLA. Notably, ablations further show generalization across visual shifts: invariance guidance learned from distractor and texture variants transfers to target-pose and lighting shifts, while adding sensitivity guidance on target-pose variants further improves robustness to nuisance shifts, highlighting the broader transferability of behavior-level RL guidance.

---

## 12. MindVLA-U1: VLA Beats VA with Unified Streaming Architecture for Autonomous Driving

**Authors:** Yuzhou Huang, Benjin Zhu, Hengtong Lu, ..., Yan Xie, Hongsheng Li
**arXiv:** [2605.12624](https://arxiv.org/abs/2605.12624)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Autonomous driving has progressed from modular pipelines toward end-to-end unification, and Vision-Language-Action (VLA) models are a natural extension of this journey beyond Vision-to-Action (VA). In practice, driving VLAs have often trailed VA on planning quality, suggesting that the difficulty is not simply model scale but the interface through which semantic reasoning, temporal context, and continuous control are combined. We argue that this gap reflects how VLA has been built -- as isolated subtask improvements that fail to compose coherent driving capabilities -- rather than what VLA is. We present MindVLA-U1, the first unified streaming VLA architecture for autonomous driving. A unified VLM backbone produces AR language tokens (optional) and flow-matching continuous action trajectories in a single forward pass over one shared representation, preserving the natural output form of each modality. A full streaming design processes the driving video framewise rather than as fixed video-action chunks under costly temporal VLM modeling. Planned trajectories evolve smoothly across frames while a learned streaming memory channel carries temporal context and updates. The unified architecture enables fast/slow systems on dense & sparse MoT backbones via flexible self-attention context management, and exposes a measurable language-control path for action: language-predicted driving intents steers the action diffusion via classifier-free guidance (CFG), turning language-side intent into control signals for continuous action planning. On the long-tail WOD-E2E benchmark, MindVLA-U1 surpasses experienced human drivers for the first time (8.20 RFS vs. 8.13 GT RFS) with 2 diffusion steps, achieves state-of-the-art planning ADEs over prior VA/VLA by large margins, and matches VA latency (16 FPS vs. RAP's 18 FPS at 1B scale) while preserving natural language interfaces for human-vehicle interaction.

---

## 13. AttenA+: Rectifying Action Inequality in Robotic Foundation Models

**Authors:** Daojie Peng, Fulong Ma, Jiahang Cao, ..., Boyu Zhou, Jun Ma
**arXiv:** [2605.13548](https://arxiv.org/abs/2605.13548)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Existing robotic foundation models, while powerful, are predicated on an implicit assumption of temporal homogeneity: treating all actions as equally informative during optimization. This "flat" training paradigm, inherited from language modeling, remains indifferent to the underlying physical hierarchy of manipulation. In reality, robot trajectories are fundamentally heterogeneous, where low-velocity segments often dictate task success through precision-demanding interactions, while high-velocity motions serve as error-tolerant transitions. Such a misalignment between uniform loss weighting and physical criticality fundamentally limits the performance of current Vision-Language-Action (VLA) models and World-Action Models (WAM) in complex, long-horizon tasks. To rectify this, we introduce AttenA+, an architecture-agnostic framework that prioritizes kinematically critical segments via velocity-driven action attention. By reweighting the training objective based on the inverse velocity field, AttenA+ naturally aligns the model's learning capacity with the physical demands of manipulation. As a plug-and-play enhancement, AttenA+ can be integrated into existing backbones without structural modifications or additional parameters. Extensive experiments demonstrate that AttenA+ significantly elevates the ceilings of current state-of-the-art models. Specifically, it improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to 92.4% (+0.6%) on RoboTwin 2.0. Real-world validation on a Franka manipulator further showcases its robustness and cross-task generalization. Our work suggests that mining the intrinsic structural priors of action sequences offers a highly efficient, physics-aware complement to standard scaling laws, paving a new path for general-purpose robotic control.

---

## 14. What Limits Vision-and-Language Navigation ?

**Authors:** Yunheng Wang, Yuetong Fang, Taowen Wang, ..., Zecui Zeng, Renjing Xu
**arXiv:** [2605.13328](https://arxiv.org/abs/2605.13328)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

Vision-and-Language Navigation (VLN) is a cornerstone of embodied intelligence. However, current agents often suffer from significant performance degradation when transitioning from simulation to real-world deployment, primarily due to perceptual instability (e.g., lighting variations and motion blur) and under-specified instructions. While existing methods attempt to bridge this gap by scaling up model size and training data, we argue that the bottleneck lies in the lack of robust spatial grounding and cross-domain priors. In this paper, we propose StereoNav, a robust Vision-Language-Action framework designed to enhance real-world navigation consistency. To address the inherent gap between synthetic training and physical execution, we introduce Target-Location Priors as a persistent bridge. These priors provide stable visual guidance that remains invariant across domains, effectively grounding the agent even when instructions are vague. Furthermore, to mitigate visual disturbances like motion blur and illumination shifts, StereoNav leverages stereo vision to construct a unified representation of semantics and geometry, enabling precise action prediction through enhanced depth awareness. Extensive experiments on R2R-CE and RxR-CE demonstrate that StereoNav achieves state-of-the-art egocentric RGB performance, with SR and SPL scores of 81.1% and 68.3%, and 67.5% and 52.0%, respectively, while using significantly fewer parameters and less training data than prior scaling-based approaches. More importantly, real-world robotic deployments confirm that StereoNav substantially improves navigation reliability in complex, unstructured environments. Project page: this https URL.

---

## 15. Action Emergence from Streaming Intent

**Authors:** Pengfei Jing, Victor Shea-Jay Huang, Hengtong Lu, ..., Yan Xie, Benjin Zhu
**arXiv:** [2605.12622](https://arxiv.org/abs/2605.12622)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

We formalize action emergence as a target capability for end-to-end autonomous driving: the ability to generate physically feasible, semantically appropriate, and safety-compliant actions in arbitrary, long-tail traffic scenes through scene-conditioned reasoning rather than retrieval or interpolation of learned scene-action mappings. We show that previous paradigms cannot deliver action emergence: autoregressive trajectory decoders collapse the inherently multimodal future into a single averaged output, while diffusion and flow-matching generators express multimodality but are not steerable by reasoned intent. We propose Streaming Intent as a concrete way to approach action emergence: a mechanism that makes driving intent (i) semantically streamed through a continuous chain-of-thought that causally derives the intent from scene understanding, and (ii) temporally streamed across clips so that intent commitments remain coherent along the driving horizon. We realize Streaming Intent in a VLA model we call SI (Streaming Intent). SI autoregressively decodes a four-step chain-of-thought and emits an intent token; the decoded intent then drives classifier-free guidance (CFG) on a flow-matching action head, requiring only two denoising steps to generate the final trajectory. On the Waymo End-to-End benchmark, SI achieves competitive aggregate performance, with an RFS score of 7.96 on the validation set and 7.74 on the test set. Beyond aggregate metrics, the model demonstrates -- to our knowledge for the first time in a fully end-to-end VLA -- intent-faithful controllability: for a fixed scene, varying the intent class at inference yields qualitatively distinct yet consistently high-quality plans, arising purely from data-driven learning without any pre-built trajectory bank or hand-coded post-hoc selector.

---
