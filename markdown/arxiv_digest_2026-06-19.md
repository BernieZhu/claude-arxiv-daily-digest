# arXiv Daily Digest — 2026-06-19

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 18

---

## 1. Reward as An Agent for Embodied World Models

**Authors:** Pu Li, Zhigang Lin, Qiang Wu, ..., Fei Wang, Shan You
**arXiv:** [2606.19990](https://arxiv.org/abs/2606.19990)
**Categories:** Artificial Intelligence (cs.AI)

While RL has become a promising tool for refining world models, existing methods largely rely on conservative rollouts near the training distribution, limiting exploration, behavioral diversity, and richer dynamic discovery. In this work, we challenge this conservative paradigm. We argue that the core limitation is not exploration itself, but the lack of reliable verification strategies to support broader exploration. Without reliable verification, expanded exploration becomes highly susceptible to reward hacking, where policies exploit imperfect rewards without achieving genuine improvement. To evaluate this motivation, we instantiate our method in embodied world models, where physical plausibility, and task completion provide a rigorous testbed for scalable RL under complex dynamics. On the verification side, we introduce Reward as an Agent, an agentic reward framework that actively evaluates generated behaviors to provide robust reward signals and mitigate reward hacking under distribution shifts. On the exploration side, we introduce Dynamic-Aware Rollout Diversification through DynDiff-GRPO, which explicitly expands action-space exploration to diversify trajectories, broaden state-action coverage, and encourage richer embodied behaviors beyond conservative rollout regimes. By unifying Reward as an Agent with DynDiff-GRPO, we enable RL on a more reliable reward foundation with substantially diversified sampling, effectively mitigating reward hacking while yielding significant accuracy gains across multiple open-source world models, thereby demonstrating that broader exploration can scale successfully when grounded in robust verification.

---

## 2. Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think

**Authors:** Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, ..., Duy M. H. Nguyen, Ngo Anh Vien
**arXiv:** [2606.20246](https://arxiv.org/abs/2606.20246)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have revolutionized robotic manipulation, yet their multi-billion parameter architectures impose prohibitive computational burdens during downstream fine-tuning and real-time inference. In this work, we reveal a highly non-trivial architectural characteristic of these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being trained on diverse physical trajectories, they exhibit severe layer-wise representational redundancy. To exploit this, we introduce a structural compression pipeline that is entirely training-free, bypassing the need of existing methods to load full-scale models to learn optimized token reductions or dynamic layer selectors. Instead, using only a single forward pass via Centered Kernel Alignment to identify redundant layer features, we remove twin layers to permanently compress the model depth by up to 50% across both the VLM backbone and the continuous control policy head. Downstream fine-tuning of this streamlined architecture yields a dual acceleration benefit: a 40-50% reduction in training time and up to 30% faster real-time inference, while matching or exceeding full-scale base model performance. We comprehensively validate our method across three simulation benchmarks (LIBERO, RoboCasa, SimplerEnv) and 10 diverse real-world manipulation tasks across 4 unique robotic embodiments. These results prove that advanced VLAs require significantly fewer layers than previously assumed, offering a highly compute-efficient paradigm for scalable robot learning.

---

## 3. Sensorimotor World Models: Perception for Action via Inverse Dynamics

**Authors:** Petr Ivashkov, Randall Balestriero, Bernhard Schölkopf
**arXiv:** [2606.20104](https://arxiv.org/abs/2606.20104)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Perception for action suggests that representations of the world should be shaped not by visual fidelity alone, but by their relevance for actions. At the same time, latent JEPA-style world models advocate learning compact predictive states from high-dimensional observations to facilitate the prediction of future states, but end-to-end training of these models is nontrivial because representations may collapse if our only goal is to construct a latent state that is easy to predict. We introduce a sensorimotor world model (SMWM): a latent world model trained end-to-end with inverse dynamics regularization. This single regularizer addresses both issues: it prevents representation collapse and induces action-aligned representations. By forcing latent states to preserve information about the action underlying a transition, it biases the model toward the controllable degrees of freedom of the environment while discarding uncontrollable distractors. This yields stable latent world models trained from offline, reward-free trajectories, without frozen encoders, exponential moving averages, or complex latent regularizers. Empirically, SMWM learns compact, interpretable latent spaces and enables competitive planning performance across simple 2D and 3D control tasks.

---

## 4. Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory

**Authors:** Jinghan Yang, Yunchao Zhang, Wang Yuan, ..., Zhengyang Hu, Yanchao Yang
**arXiv:** [2606.19998](https://arxiv.org/abs/2606.19998)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet they remain black boxes whose physical interactions can cause irreversible harm, making generalizable and interpretable failure detection essential. We observe that successful and failed rollouts carry systematically different information-theoretic signatures. Building on this, we formalize VLA control as a closed-loop information pipeline and derive the Triple Information-theoretic (Tri-Info) signals that capture whether actions remain diverse, temporally consistent, and coupled to state transitions. Across six VLA models and three benchmark environments, Tri-Info matches the strongest baselines in-domain. Moreover, Tri-Info transfers across architectures, environments, and the sim-to-real gap without retraining, reaching 83\% accuracy on real-world tasks where prior detectors collapse to chance. This establishes Tri-Info as a simple yet powerful method that not only detects failures with strong cross-domain generalization, but also delivers interpretable diagnostics of the underlying failure modes.

---

## 5. MemoryWAM: Efficient World Action Modeling with Persistent Memory

**Authors:** Sizhe Yang, Juncheng Mu, Tianming Wei, ..., Jiangmiao Pang, Huazhe Xu
**arXiv:** [2606.20562](https://arxiv.org/abs/2606.20562)
**Categories:** Robotics (cs.RO)

Robust robotic manipulation in the real world requires not only an understanding of the current observation, but also memory and dynamics modeling. World action models (WAMs) possess these capabilities by jointly modeling visual foresight and actions conditioned on both current and historical observations, making them a promising paradigm for robotic manipulation. However, existing WAMs face a fundamental trade-off: methods with efficient inference typically condition only on a bounded window of recent observations and therefore struggle in non-Markovian environments, whereas methods that preserve long histories incur time and space costs that grow substantially with sequence length. To address this challenge, we introduce MemoryWAM, a world action model with efficient persistent memory. MemoryWAM uses a hybrid memory design that combines recent frames, event-boundary anchor frames, and compact gist tokens that summarize long-range history. A tailored attention mechanism enables retrieval of both detailed short-term context and compressed long-term context, supporting memory-dependent decision-making with reduced inference latency and GPU memory usage. Across long-horizon, memory-dependent manipulation tasks in both simulation and the real world, MemoryWAM outperforms strong vision-language-action (VLA) and WAM baselines while maintaining favorable computational efficiency.

---

## 6. Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems

**Authors:** Yandong Wang, Jiaqian Yu, Xiongfeng Peng, ..., Mingbo Zhao, Chao Zhang
**arXiv:** [2606.20285](https://arxiv.org/abs/2606.20285)
**Categories:** Robotics (cs.RO)

Vision-language-action (VLA) models show strong capabilities in single and dual-arm robotic manipulation. Prior works show coordinated bimanual behaviors can emerge from end-to-end learning, leveraging large vision-language backbones with continuous action prediction. However, as bimanual tasks become tightly coupled and execution constraints become critical, implicit coordination alone is insufficient to ensure reliable, interpretable, and stable behavior.
In this work, we propose Co-VLA, a coordination-aware bimanual manipulation framework introducing explicit structural priors into VLA models. We instantiate our method on a state-of-the-art vision-language backbone by replacing its monolithic action head with a Structured Action Expert (SAE) designed for bimanual coordination. Specifically, we introduce explicit structure at the action generation level with a modular coordination-aware loss that shapes shared and residual latents according to task-specific structures. The shared latent encodes task-level coordination intent, while residual latents capture execution adjustments for each arm.
At deployment, a Latent-Aware Controller (LAC) interprets the learned representations to modulate synchronization strength, execution asymmetry, smoothness, and safety constraints in real time. LAC operates at the joint-command level and remains compatible with standard control pipelines without requiring force or impedance control. Experiments across simulation and real-world benchmarks show Co-VLA significantly outperforms monolithic baselines, achieving a 27% success rate gain in tight-coordination tasks, more than doubling performance in OOD real-world scenarios (from 13% to 27%), and reducing task completion time by up to 25%.

---

## 7. SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour

**Authors:** Kaixin Lan, Ze Wang, Hongyi Li, ..., Yongbin Jin, Hongtao Wang
**arXiv:** [2606.19928](https://arxiv.org/abs/2606.19928)
**Categories:** Robotics (cs.RO)

While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model. This framework embeds symmetry directly into both the world model and the actor-critic networks. In real-world tests, the robot leaps across a 2.13 m gap and climbs a 1.63 m platform, breaking records for quadruped parkour. Furthermore, the framework exhibits robust geometric generalization to unseen mirrored terrains and exceptional zero-shot transferability across diverse outdoor environments. These results demonstrate that symmetry equivariance is an effective structural prior for pushing the physical boundaries of learned legged locomotion.

---

## 8. EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models

**Authors:** Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, ..., An Thai Le, Ngo Anh Vien
**arXiv:** [2606.19784](https://arxiv.org/abs/2606.19784)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for generalist robot manipulation, yet they lack geometric inductive biases: policies trained at specific orientations require substantially more data to generalize across rotational configurations. We present \textsc{EquiVLA}, the first general framework for end-to-end $\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a frozen vision-language backbone with a flow-matching Diffusion Transformer action head. \textsc{EquiVLA} introduces \textsc{EquiPerceptor}, which produces approximately $\mathrm{SO}(2)$-equivariant visual representations from frozen ViT features; and \textsc{EquiActor}, an exactly $\mathrm{SO}(2)$-equivariant flow-matching Diffusion Transformer action head. Together, they establish an approximate $\mathrm{SO}(2)$ equivariance chain from camera observations to predicted action sequences. Instantiated on GR00T~N1.5 and evaluated across four LIBERO suites, CALVIN ABCD$\to$D, and five real-robot tasks on Mobile ALOHA, \textsc{EquiVLA} achieves $92.6\%$ average success on LIBERO (vs. $78.1\%$ baseline), an average sequence length of $4.03$ on CALVIN (vs. $3.45$), and improves real-robot success from $54\%$ to $72\%$.

---

## 9. ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?

**Authors:** Yuyang Zhang, Wenyao Zhang, Zekun Qi, ..., Wenjun Zeng, Xin Jin
**arXiv:** [2606.19531](https://arxiv.org/abs/2606.19531)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

World Action Models (WAMs) commonly rely on video generation to bridge visual world modeling and robot control. However, video-based WAMs face three coupled limitations: dense multi-frame future tokens make inference costly, full video prediction spends capacity on action-irrelevant temporal and appearance details, and long-horizon future imagination may introduce errors that mislead action prediction. These issues raise a simple question: Does world action model really need video generation? We propose ImageWAM, a simple WAM framework that repurposes pretrained image editing models for robot action prediction. In contrast to video generation, image editing provides a better-matched prior: it only needs to model a target-frame transformation, focuses on action-relevant current-to-target visual differences, and grounds task instructions to localized visual changes through edit pretraining. In practice, ImageWAM does not decode the target frame at inference time; instead, it conditions a flow-matching action expert on the KV caches produced by image-editing denoising, using them as a compact world-action context. ImageWAM outperforms standard VLA baselines and matching competitive WAMs without additional policy pretraining across different simulator and real-world experiments. It also reduces FLOPs to 1/6 and latency to 1/4 of video-based WAMs. Attention analysis further shows that editing caches focus on task-relevant change regions, supporting image editing as an effective alternative to video-based world-action modeling.

---

## 10. Current World Models Lack a Persistent State Core

**Authors:** Jinpeng Lu, Dexu Zhu, Haoyuan Shi, ..., Yong Dai, Xiaozhu Ju
**arXiv:** [2606.20545](https://arxiv.org/abs/2606.20545)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires an internal world state that keeps evolving over time, decoupled from observation, so that objects endure and events run to their conclusions whether or not a camera is watching, much as the moon holds to its orbit when no one is looking. This requirement is a blind spot of existing benchmarks, which reward surface properties such as fidelity, motion, and camera controllability while never asking whether a generated world keeps evolving once it is unobserved. We introduce \textbf{WRBench}, the first systematic diagnostic benchmark that treats camera motion as an intervention on observability and resolves evaluation into a human-calibrated chain that asks whether the camera executes the requested interaction, whether the scene stays continuous and identifiable while in view, and whether a returning target remains consistent with the event that was set in motion. Across 9{,}600 videos from 23 models spanning four control paradigms, one finding proves stubborn: current systems maintain the observed world as a tracking shot, resuming a returning target in the state at which it was abandoned rather than advancing the event while it went unseen. Because this failure recurs across control paradigms, model families, and increments of scale, robust world-state evolution does not follow from cleaner imagery, tighter control, richer geometric priors, or sheer parameter count We therefore argue that the stability of the physical state kernel and the consistency of worldlines under viewpoint intervention should become first-class objectives of world-model design, so that a world model captures how the world will unfold rather than how the next frame appears.

---

## 11. EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies

**Authors:** Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, ..., Yao Mu, Tai Wang
**arXiv:** [2606.20092](https://arxiv.org/abs/2606.20092)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded or unobservable over time. While existing memory-augmented methods utilize historical context, they either suffer from severe information bottlenecks, incur high latency via decoupled dual systems, or rely on unselective buffers that accumulate massive visual redundancies. To address these limitations, we introduce EventVLA, an end-to-end framework founded on the concept of sparse visual evidence memory that comprises two core components: foundational visual anchors to retain initial and short-term contexts, and a dynamic Keyframe Evidence Memory (KEM) module. Specifically, KEM directly predicts future keyframe probabilities from the VLA's latent embeddings to autonomously capture and store sparse, task-critical visual events. This foresight-driven mechanism empowers the policy to dynamically evaluate the future causal utility of current observations, preserving transient visual evidence before it becomes unobservable. Furthermore, we propose RoboTwin-MeM, a diagnostic benchmark specifically designed to evaluate non-Markovian manipulation tasks with interactive visual evidence. Extensive evaluations show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks, EventVLA achieves an average success rate improvement of +40% over state-of-the-art memory-augmented VLAs.

---

## 12. Holo-World: Unified Camera, Object and Weather Control for Video World Model

**Authors:** Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, ..., Chunfeng Wang, Xiaoyan Sun
**arXiv:** [2606.20083](https://arxiv.org/abs/2606.20083)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video world models are moving toward preserving an observed world under controllable camera and object motion while allowing its environmental state to change. Yet these controls remain isolated, and weather generation typically relies on a source video or reconstructed scene that already specifies future structure. We study a first-frame-anchored source-to-state setting, where the model starts from a single image and follows explicit camera and object controls and an optional weather instruction, then generates a video that either preserves the source world or transfers it to a target weather state. To address these challenges, we first build HoloStateData, a state video dataset that turns diverse videos into unified control samples for camera, object, and weather supervision. Second, we introduce Holo-World, a unified controllable video world model that jointly controls scene from a single image. Its Unified Scene Adapter factorizes world preservation and weather transfer into distinct parameter subspaces, using rendered background, geometry buffers, and object controls to maintain controlled scene structure while modeling weather-dependent appearance and particle effects. Additionally, Scene-Weather Decomposed CFG guides scene and weather residuals separately, strengthening target weather effects without over-amplifying the full condition. Quantitative and qualitative experiments demonstrate that Holo-World maintains precise camera and object control with consistent scene structure while transferring scenes into diverse target weather state, outperforming video-to-video weather editing baselines on weather-state generation. Our project page is available at \url{this https URL}.

---

## 13. SurgVista: Long-Horizon Surgical World Modeling with Plausible Instrument-Tissue Dynamics

**Authors:** Wentao Pan, Wuyang Li, Shengyuan Liu, ..., Hengyu Liu, Yixuan Yuan
**arXiv:** [2606.19889](https://arxiv.org/abs/2606.19889)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Scaling robot policy learning for autonomous surgery is challenging, as expert demonstrations are expensive and in vivo exploration poses substantial safety risks. Surgical world models address this by generating realistic, action-conditioned future frames from an initial observation, but existing methods exhibit two persistent failure modes: spatial interaction incoherence, where visible instrument contact fails to induce spatially consistent tissue deformation, and temporal fidelity collapse, where prediction errors compound across autoregressive rollouts and progressively corrupt visual quality. We present SurgVista, a surgical world model that mitigates both failures through two training recipes. Deformation Consistency Regularization extracts scene-point trajectories from training videos and enforces cross-frame coherence through latent contrastive learning, strengthening physically consistent instrument-tissue dynamics. Drift Adaptation Training mitigates long-horizon drift by perturbing conditioning frames with online prediction residuals and photometric augmentations calibrated to long-horizon drift statistics, sustaining visual fidelity over extended rollouts. To enable rigorous evaluation, we further introduce SurgWorld-Bench, featuring diverse procedure types, long-range rollouts, and decoupled metrics for instrument-motion accuracy and tissue-response fidelity. Extensive experiments show that SurgVista consistently outperforms state-of-the-art methods across visual quality, temporal consistency, and interaction fidelity, with gains widening as the prediction horizon grows.

---

## 14. Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models

**Authors:** Navin Ranjan, Andreas Savakis
**arXiv:** [2606.19565](https://arxiv.org/abs/2606.19565)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

We propose Mix-QVLA, a task-evidence-aware mixed-precision PTQ framework for VLA models. Mix-QVLA anchors each quantized variant to the full-precision action-token reference decision and evaluates whether quantization preserves task-relevant evidence across key VLA functional boundaries. It computes normalized gradient-weighted task-evidence maps from boundary activations and compares full-precision and quantized maps using evidence-mass and attribution-distribution distortion, capturing changes in both the strength and allocation of decision-supporting evidence. A soft-bottleneck objective aggregates boundary-level degradation into layer-wise sensitivity scores. Mix-QVLA further models sensitivity throughout task execution, capturing phase-dependent shifts in layer importance rather than assuming a fixed sensitivity profile. The resulting evidence- and time-aware scores guide mixed-precision bit allocation under model-size and BitOps budgets. Extensive evaluations on OpenVLA-style policies show that Mix-QVLA improves the accuracy-efficiency trade-off of low-bit VLA deployment. On LIBERO, Mix-QVLA reduces OpenVLA-OFT memory from 15.4 GB to 4.1 GB, retains 96.3 average success compared with 97.1 for the BF16 model, and achieves a 1.52x inference speedup.

---

## 15. Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving

**Authors:** Shihao Ji, HongXi Li, Zihui Song, Mingyu Li
**arXiv:** [2606.20274](https://arxiv.org/abs/2606.20274)
**Categories:** Artificial Intelligence (cs.AI)

Scaling end-to-end autonomous driving to complex, open-world environments requires perceptual models that generalize to anomalous scenarios and planners that produce kinematically valid trajectories. Existing paradigms face a distinct dichotomy between representational efficiency and generalization capacity. Dense models (e.g., occupancy networks), while geometrically robust, incur critical computational bottlenecks and struggle with high-level semantic reasoning. Conversely, sparse, query-based planners are efficient but reliant on closed-set definitions, rendering them vulnerable to out-of-distribution (OOD) events. Although recent Vision-Language-Action (VLA) models offer open-vocabulary reasoning, their autoregressive, discrete token generation fundamentally conflicts with the continuous, high-frequency control requirements of vehicle dynamics. To address this, we propose Lagrange, an open-vocabulary, computationally sparse driving framework based on Masked Latent Fields (MLF). Rather than relying on dense volumetric reconstructions or closed-set query mechanisms, Lagrange exploits Vision-Language Models (VLMs) to encode class-agnostic object proposals into continuous semantic visual tokens. We introduce an intent-driven masked cross-attention module that temporally filters irrelevant entities, decoding the attended tokens into an implicit continuous energy field defined over spatial coordinates. By framing decision-making as a Lagrangian action minimization problem spanning this energy field, we enforce strict compliance with vehicle kinematics while executing collision avoidance. Extensive offline evaluations on both standard (nuScenes) and long-tail (CODA) benchmarks demonstrate that Lagrange establishes a promising framework for robust, interpretable, and kinematically feasible open-world autonomy.

---

## 16. Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation

**Authors:** Jianing Guo, Fangzheng Chen, Zihao Mao, ..., Huijie Zhao, Simin Li
**arXiv:** [2606.20135](https://arxiv.org/abs/2606.20135)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Flow matching has emerged as a standard paradigm for robotic manipulation owing to its strong expressive power for modelling complex, multimodal action distributions, alongside similar approaches like diffusion policy. However, existing methods rely on discretized action chunks, making them brittle to demonstrations collected at heterogeneous control frequencies and prone to temporally inconsistent actions that degrade control stability. In this paper, we propose Frequency-Aware Flow Matching (FAFM), which outputs continuous, temporally consistent actions. To handle heterogeneous frequency input, we transform discrete action sequences into the frequency domain with the discrete cosine transform (DCT), perform flow matching over the resulting coefficients, and reconstruct continuous actions via cosine basis expansion. To generate temporally consistent actions, we regularize the first-order temporal derivative to promote smooth actions. This corresponds to a Sobolev-type constraint that suppresses high-frequency errors and discourages abrupt action changes. Our FAFM is simple, introduces no additional network parameters and applies to standalone flow-matching policies and vision-language action models. Across synthetic toy benchmark, obstacle avoidance, LapGym, and LIBERO, FAFM improves success rates, multimodal expressivity, motion smoothness, convergence speed, robustness to mechanical bias and mixed-frequency input. These gains are consistent when deployed on a real-world Franka robot. Code available at this https URL.

---

## 17. FlexLAM: Resolving the Bottleneck Trade-off in Latent Action Learning

**Authors:** Takanori Yoshimoto, Yang Hu, Naruya Kondo, Tatsuya Matsushima
**arXiv:** [2606.19408](https://arxiv.org/abs/2606.19408)
**Categories:** Machine Learning (cs.LG); Robotics (cs.RO)

Latent actions provide a compact interface between action-free video and downstream decision-making, yet existing Latent Action Models (LAMs) force every transition through a fixed-capacity bottleneck. We identify a bottleneck trade-off: overly tight codes can discard transition cues needed for action alignment, while overly loose codes preserve additional transition variation that must be resolved when alignment labels are scarce or narrowly distributed. FlexLAM replaces this fixed capacity with variable-length latent actions trained by nested dropout, yielding prefix-valid codes that capture compact transition structure first and add detail only when needed, without new architectures or losses. A single FlexLAM matches or surpasses separately trained fixed-capacity LAMs at every evaluated token budget under standard scarce-label supervision and under a low-return single-task alignment stress test, indicating that FlexLAM is not merely adjustable at inference time but learns a better latent-action interface at the same token budgets. The same model supports inference-time token-budget adjustment without retraining, and FlexLAM improves Ego4D transition reconstruction. These results suggest that variable-length latent actions are an architecture-free, drop-in upgrade to the fixed-capacity bottleneck in latent action models, latent-action world models, and video-pretrained action interfaces.

---

## 18. Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation

**Authors:** Zhenghao "Mark'' Peng, Honglin He, Quanyi Li, Yukai Ma, Bolei Zhou
**arXiv:** [2606.20458](https://arxiv.org/abs/2606.20458)
**Categories:** Robotics (cs.RO)

Learning-based planners for sidewalk navigation can generate diverse candidate trajectories in real time, yet their scoring functions often fail to select the best trajectory in challenging situations, outputting trajectories that make the mobile robot drive onto grass, toward pedestrians, or in the wrong direction, even when better candidates exist in the same set. We call this the trajectory scoring gap: in real-world sidewalk navigation, the gap between an anchor-based planner's top choice and the best possible candidate is substantial, likely due to limited high-level scene understanding capability of the planner. Rather than replacing the planner with an end-to-end Vision-Language-Action model, we propose a VLM-Planner interface that uses a VLM to select a candidate index from the planner's proposal set and then fuse it with the planner's initial output. However, VLMs take 1--3s per query and so cannot directly drive a 5--20Hz control loop. We contribute a training-free, latency-resilient trajectory-level fusion layer that turns a stale VLM selection into real-time planner scoring via geometric similarity with exponential decay. On $\sim$2,000 challenging real-world scenarios (e.g., junctions, pedestrian encounters), VLM selection achieves 30% ADE reduction versus the planner's best selection, while the planner remains competitive in routine situations. In simulation, Score Fusion maintains >80% success rate with delays up to 5s. We demonstrate the full system on a mobile robot navigating challenging campus sidewalks with varied network latency.

---
