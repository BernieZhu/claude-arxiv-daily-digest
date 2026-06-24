# arXiv Daily Digest — 2026-06-23

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 50

---

## 1. Self-Evolving Cognitive Framework via Causal World Modeling for Embodied Scientific Intelligence

**Authors:** Yi Yu, Tetsunari Inamura
**arXiv:** [2606.22449](https://arxiv.org/abs/2606.22449)
**Categories:** Artificial Intelligence (cs.AI); Robotics (cs.RO)

Current embodied world models are primarily optimized for predictive objectives, limiting their ability to generalize under distribution shifts and reason systematically about unseen situations and hypothetical interventions. We argue that embodied intelligence should move beyond predictive world modeling toward self-evolving cognitive systems that continually construct and refine internal causal representations through interaction with the environment. To this end, we propose a self-evolving cognitive framework via causal world modeling for embodied scientific intelligence, which integrates three complementary components: causal world modeling, intervention-driven causal reasoning, and continual cognitive refinement. The proposed framework continuously revises and expands its internal causal world model through causal discovery, intervention-driven feedback, and counterfactual reasoning, supporting continual cognitive refinement and enabling cognition itself to evolve over time. Furthermore, we reinterpret embodied interaction not merely as a means of trajectory optimization, but as an epistemic process for causal hypothesis generation, intervention-driven experimentation, and continual knowledge acquisition. This work provides a conceptual and theoretical foundation for a transition from predictive intelligence toward epistemic intelligence, in which intelligence emerges through the continual construction, revision, and refinement of causal world models via interaction with the environment. Accordingly, an intervention-driven causal-epistemic benchmarking paradigm is suggested for evaluating self-evolving embodied scientific intelligence.

---

## 2. Reference-Free Assessment of Physical Consistency in World Model-based Video Generation

**Authors:** Yun Oh, Sukmin Yun
**arXiv:** [2606.22363](https://arxiv.org/abs/2606.22363)
**Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG); Robotics (cs.RO)

We introduce reference-free measures for evaluating the physical consistency of generated videos, combining relative and absolute approaches to assess fidelity. Although tools like WorldGym or WorldEval enable robotic simulation via video generation, physical fidelity gaps often prevent these environments from accurately reproducing real-world task success rates of VLA models. Unlike existing evaluation methods, which require costly human voting (Elo) or unavailable ground-truth references (FVD), our approach utilizes DROID-SLAM and SEA-RAFT to quantify physical inconsistencies, motivated by WorldScore. Videos filtered using our relative consistency assessment show an improvement in task success rates of over 8%, effectively narrowing the simulation-to-reality gap. Furthermore, our absolute assessment enables spatio-temporal localization, providing visualization of when and where physical artifacts occur.

---

## 3. Nous: A Predictive World Model for Long-Term Agent Memory

**Authors:** Pranav Singh
**arXiv:** [2606.22030](https://arxiv.org/abs/2606.22030)
**Categories:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Information Retrieval (cs.IR); Machine Learning (cs.LG)

We present Nous, a novel agent memory architecture grounded in the principle that knowledge is prediction, not storage. Rather than persisting facts as database records, vector embeddings, or knowledge-graph triples, Nous maintains a predictive world model: a collection of categorical probability distributions, called dimensions, one per entity-attribute pair observed in conversation. Each incoming observation is scored by its information-theoretic surprise S = -log2 P(obs | D), and the distribution is updated via a closed-form Bayesian posterior. The primary stored artifact is the delta, a record of the shift from prior to posterior belief, rather than the fact itself. Forgetting emerges naturally as entropy decay toward the uniform distribution, and identity resolution is handled through mutual information between entity dimension sets. Evaluated on the LoCoMo long-term conversational memory benchmark across ten conversations (1,540 questions) using GPT-4o-mini as backbone, Nous achieves F1 of 63.50 (single-hop), 55.32 (multi-hop), 58.57 (temporal), and 62.50 (open-domain). Against A-MEM's self-reported GPT-4o-mini numbers, Nous shows substantial gains in three of four categories, though we note that independent citations of A-MEM's results disagree with each other on category assignment, a reproducibility issue we discuss openly rather than resolve unilaterally. We additionally compare against BeliefMem, a concurrently developed system built on the same core premise of belief-based rather than deterministic memory; on the same benchmark and backbone, Nous's self-reported numbers exceed BeliefMem's self-reported numbers on all four categories, though we flag several uncontrolled differences between the two evaluation pipelines that prevent this from being a fully controlled comparison. Nous requires no external vector database or graph engine.

---

## 4. Social World Model for Lifelong Social Intelligence

**Authors:** Yu Luo
**arXiv:** [2606.21315](https://arxiv.org/abs/2606.21315)
**Categories:** Artificial Intelligence (cs.AI)

Social intelligence is a core competency for language agents, yet current research primarily focuses on static capability evaluation rather than how these skills are continuously shaped and accumulated. This gap calls for a shift toward sustainable learning paradigms. Currently, two methodological pain points exist: social interaction trajectories lack unified structured representations to form iterable learning signals, and capability improvement and retention are typically studied in isolation, hindering the assessment of continuous evolution.
To bridge this gap, we propose the Social World Model. We decompose social interaction into five dimensions (scene setting, observation, mental state, action, and dialogue) to build a closed-loop learning framework. In this setup, agents collect interaction experiences, convert them into preference signals for model updating, and redeploy the updated policy for continued learning. Additionally, we provide a reusable data synthesis mechanism and a lifelong learning benchmark, transforming social capabilities from an "object of evaluation" into an "object of sustainable training".
Validating our framework on the ASCENT-Bench, the interactively trained Qwen2.5-7B model outperforms its baseline across all five core metrics. Notably, it matches the closed-source Gemini 3 Flash in completion rate, exceeds it in pass rate, and achieves zero forgetting across three difficulty levels. Unlike prior works that merely report static comparisons or capability decay, this end-to-end approach provides a trainable, verifiable, and retainable pathway, demonstrating that small open-source models can sustainably acquire competitive social coordination capabilities.

---

## 5. SignVLA: Real-Time Sign Language-Guided Robotic Manipulation via Attention LSTM and Vision-Language-Action Models

**Authors:** Ningwei Bai, Xinyu Tan, Harry Gardner, ..., Monkgogi Galeitsiwe, Zezhi Tang
**arXiv:** [2606.20857](https://arxiv.org/abs/2606.20857)
**Categories:** Artificial Intelligence (cs.AI); Machine Learning (cs.LG); Robotics (cs.RO)

Vision-Language-Action (VLA) models enable robots to execute manipulation tasks from natural-language instructions grounded in visual observations. However, existing VLA interfaces primarily rely on speech or text input, limiting accessibility for deaf, hard-of-hearing, and speech-impaired users. We present SignVLA, a real-time sign-language-guided VLA framework for accessible human-robot interaction. The system introduces a modular sign-to-text interface that converts visual sign gestures into semantic instructions compatible with downstream VLA policies. Given video streams, SignVLA extracts hand landmark features and employs an attention-enhanced Long Short-Term Memory (LSTM) network to capture temporal gesture dynamics for alphabet- and command-level sign recognition. A temporal stabilization module further improves prediction consistency in real-time interaction this http URL generated instruction sequence is then passed to a downstream VLA policy for sign-conditioned robotic manipulation. Experimental results demonstrate stable real-time sign recognition and successful execution of manipulation tasks driven by sign-language inputs. Our findings suggest that lightweight temporal sign recognition can serve as an effective and practical accessibility layer for multimodal embodied intelligence.

---

## 6. RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models

**Authors:** Ulas Berk Karli, Tesca Fitzgerald
**arXiv:** [2606.23617](https://arxiv.org/abs/2606.23617)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models are commonly fine-tuned through passive imitation learning, where additional demonstrations are collected for tasks where the policy performs poorly. This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. In this paper, we propose an active, continual learning paradigm for VLAs. We demonstrate that active, uncertainty-guided data collection leads to more efficient fine-tuning than when using passively-collected demonstrations. However, we also find that fine-tuning only on actively-collected recovery data leads to catastrophic forgetting. We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. Overall, our work contributes an empirical study of active continual learning for autoregressive VLAs, establishing that uncertainty-guided recovery demonstrations can improve adaptation efficiency while also revealing open challenges when targeted new data is incorporated into large robot policies.

---

## 7. AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control

**Authors:** Yutian Cheng, Xiaojian Ma, Xianhao Wang, ..., Shuai Li, Qing Li
**arXiv:** [2606.23079](https://arxiv.org/abs/2606.23079)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Neural world models coupled with model predictive control (MPC) replan at every environment step to bound accumulated prediction error, but this incurs substantial computational overhead. Reusing a cached plan reduces this overhead, yet its effectiveness depends on how prediction mismatch propagates through the local dynamics. We analyze this trade-off with a perturbation-based dynamic-regret framework and show that stale-plan penalties scale with the reuse tolerance, the accumulated mismatch since the last replanning step, and the local dynamics sensitivity. Based on this structure, we propose AdaReP, a training-free wrapper that adapts the replanning tolerance online using the current deviation from the cached rollout and a local sensitivity estimate, without modifying the learned world model or planner. Across image-space planning, latent-space control, and real-world robotic manipulation, AdaReP substantially reduces planner-side computation while maintaining comparable task performance, including over 80% fewer queries on a 50-trial physical robot study.

---

## 8. Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models

**Authors:** Linghan Chen, Kaiyan Ji, Minyu Guo
**arXiv:** [2606.22966](https://arxiv.org/abs/2606.22966)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Cryptography and Security (cs.CR)

Many recent vision-language-action (VLA) policies adopt an imagine-then-act design. A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. A downstream oracle, such as a safety gate, a visual model-predictive-control (MPC) planner, or an imagine-then-check verifier, consumes z~ as a prediction of the future. The robustness of the policy therefore does not entail the robustness of systems that rely on the WAM. The underlying phenomenon is an asymmetry. Corrupting the imagination is easy, since it requires only displacing z~ from its natural-future manifold. Steering it precisely is hard, since it must reach a specified on-manifold target. We adopt a capability-based threat model with an L-infinity-bounded observation perturbation. The attacker applies projected gradient descent through the fully differentiable observation-to-imagination map. The same off-manifold property motivates a parameter-free denoiser detector. We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. Untargeted corruption is roughly 60x stronger than random and is detected at AUC 1.0. Targeted control remains bounded. An adaptive attacker evades detection only by forgoing corruption. The reactive policy remains robust to corrupted imagination. A native imagination-driven MPC, however, exhibits the first adversary-specific task failure (at epsilon=0.01, success 0.70 versus 0.05; Fisher p < 10^-4).

---

## 9. Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning

**Authors:** Tianqi Du, Qi Zhang, Yifei Wang, Yisen Wang
**arXiv:** [2606.21775](https://arxiv.org/abs/2606.21775)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Recently, world models have emerged as a promising paradigm for building intelligent agents by learning predictive models that estimate future environment states conditioned on observations and actions. In particular, JEPA-style latent world models provide an efficient alternative to pixel space prediction by learning action-conditioned dynamics in compact representation spaces. However, existing latent world models typically rely on one-step prediction and must be recursively rolled out for long-horizon planning, which leads to compounding errors and a mismatch between training objectives and downstream planning tasks. To address this limitation, we propose Variable-length Latent World Models (VLWMs), a framework that learns to predict future latent states conditioned on action sequences of variable lengths. Instead of training only on one-step transitions, VLWMs directly model temporally extended dynamics, allowing the same predictor to evaluate action plans over different horizons. We further introduce a curriculum training strategy that progressively expands the action horizon, stabilizing optimization from short-range dynamics to long-range prediction. At test time, we design planning methods tailored to VLWMs to better exploit their variable-length predictive capabilities. Experiments on long-horizon control tasks show that VLWMs significantly improve latent space world models, achieving 13\% average improvement over the state-of-the-art LeWM across different datasets, with especially large gains on tasks requiring extended planning. These results suggest that VLWM provides a simple yet effective paradigm for improving long-horizon prediction and planning in latent world models.

---

## 10. Imitation from Heterogeneous Demonstrations using Grounded Latent-Action World Models

**Authors:** Tianyou Wang, Anson Lei, Joe Watson, Ingmar Posner
**arXiv:** [2606.21672](https://arxiv.org/abs/2606.21672)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Imitation learning has emerged as a powerful paradigm for learning visuomotor policies, but its generalisation and stability are limited by the scale and quality of demonstration data needed. A promising direction is to leverage more abundant but heterogeneous data sources, which differ in action space and often lack action labels altogether. Existing co-training approaches that combine heterogeneous data sources rely on heuristic and hand-engineered alignment techniques. In contrast, we argue that action representations should be grounded in prediction: actions that produce the same effect on the environment should share the same representation, regardless of their sources. To this end, we instantiate this principle by using a grounded latent-action world model (GLAM), a pair of generative models with a shared latent action space across data sources that is grounded by predicting future observations consistently across sources. This latent action space is used to train downstream behavioural cloning (BC) policies which map observations to latent actions and decode them back to robot actions, providing a paradigm for learning from heterogeneous data. Empirically, we demonstrate that GLAM successfully learns an aligned latent action space that facilitates action transfer across data sources with and without action labels. Across five manipulation tasks in simulation and in the real world, GLAM-aligned policies significantly outperform BC baselines and prior latent-action methods, achieving an average of +48% improvement in task success rate with the same data-scarce setting. Videos and code are available at this https URL.

---

## 11. Decoupling the Declarative from the Procedural in Vision-Language-Action Models

**Authors:** Nikolaos Tsagkas, Andreas Sochopoulos, Chris Xiaoxuan Lu, Oisin Mac Aodha, Alexandros Kouris
**arXiv:** [2606.21496](https://arxiv.org/abs/2606.21496)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Deploying generalist robotic agents in the real world requires transferable skills. Specifically, a policy trained to clone a behavior from object-specific demonstrations must generalize beyond that object, otherwise data collection requirements become intractable. Recently, fine-tuning of pre-trained billion-parameter Vision-Language Models (VLMs), initially on large-scale robot datasets and then on fewer scenario-specific demonstrations, has emerged as the predominant paradigm for designing Vision-Language-Action (VLA) models. While these policies achieve state-of-the-art manipulation performance in-distribution, they remain brittle to minor spatial, semantic, and task variations. In this work, we address the inability of current models to decouple the declarative (i.e., concepts and entity semantics) from the procedural knowledge (i.e., how to do something) encoded in their parameters, which is a fundamental bottleneck for zero-shot skill transfer to novel objects. To address this, we propose w$^{2}$VLA, a new VLA model with restructured information flow. Rather than feeding all multimodal tokens from the VLM encoder into a large, opaque transformer-based action expert, our approach modulates the robot state sequence with visual, spatial, and skill information in a compositional and interpretable manner. Unlike popular, state-of-the-art VLAs, we show that our modular approach successfully decouples knowledge representations, enabling robust behavior cloning and unprecedented zero-shot skill transfer capabilities across dissimilar, unseen objects.

---

## 12. Inverting the Bellman Equation: From $Q$-Values to World Models

**Authors:** Alistair Letcher, Mattie Fellows, Alexander D. Goldie, ..., Jakob N. Foerster, Oliver Richardson
**arXiv:** [2606.21173](https://arxiv.org/abs/2606.21173)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Model-based and model-free reinforcement learning are traditionally viewed as separate paradigms: instead of learning a model of the transition kernel $P$, model-free agents typically estimate value functions tied to a specific policy and reward. In this paper, we challenge this dichotomy by proving that value-based agents trained on a sufficiently rich set of reward functions, e.g. using goal-conditioned RL, implicitly encode a unique and accurate world model. To extract this model in practice, we introduce \textit{$P$-learning}, an inverse analogue to $Q$-learning that samples from an agent's $Q$-values, policies and rewards to decode its internal model of the environment. We then provide sufficient conditions on the type and number of goals for which agents encode the true kernel $P$, covering both stochastic and deterministic MDPs over finite or continuous state spaces. Even when our assumptions are violated, we empirically demonstrate that agents trained on a handful of reward functions encode accurate dynamics in $\texttt{Reacher}$, $\texttt{MountainCar}$ and stochastic variants of $\texttt{FourRooms}$. Surprisingly, we find that policies trained exclusively on a \texttt{Reacher} agent's implicit world model are quasi-optimal on out-of-distribution, velocity-based goals despite position-only training -- suggesting that agents contain hidden generalisation capabilities and providing a new lens into the connection between model-based, model-free, and goal-conditioned RL.

---

## 13. FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation

**Authors:** Duc Minh Nguyen, Nghiem Tuong Diep, Binh Gia Nguyen, ..., An Thai Le, Ngo Anh Vien
**arXiv:** [2606.20867](https://arxiv.org/abs/2606.20867)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models enable general-purpose robotic control via large-scale multimodal pretraining, yet their effectiveness under few-shot imitation learning remains limited. We conduct a systematic stress test of state-of-the-art VLA models and show that performance degrades sharply as demonstrations are reduced, revealing a key weakness of existing adaptation strategies. To address this, we introduce FOCA, a future-oriented conditioning framework for data-efficient VLA adaptation. FOCA combines explicit prediction of task-grounded future interaction embeddings with implicit alignment to future goal observations, enabling long-horizon reasoning in latent space without pixel-level prediction. This formulation naturally supports action-free co-training with synthetic videos from video world models and can be interpreted as learning a future-conditioned value-like representation. Extensive experiments demonstrate FOCA achieves 95.7% success with 20 demonstrations on LIBERO, improves 7-12% on RoboCasa, and delivers up to 26% absolute gains on real robots, establishing a new state of the art in few-shot VLA adaptation.

---

## 14. One Image is All You Need: Agentic One-Shot Image Generation via Text-Based World Models for Long-Tail Spatial Perception

**Authors:** Keqin Zeng, Shuting Su, Shihao Lin, Ziyue Li, Rui Zhao
**arXiv:** [2606.20764](https://arxiv.org/abs/2606.20764)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Graphics (cs.GR); Machine Learning (cs.LG)

Reliable spatial decision automation, such as autonomous driving and maritime surveillance, critically depends on robust visual perception. However, real-world spatiotemporal data exhibits severe heterogeneity, often manifesting as extreme long-tail distributions for safety-critical scenarios. This data scarcity induces dataset shift that degrades detection performance and pose safety risks. While synthetic data generation offers a potential solution, existing generative approaches, such as diffusion models and Generative Adversarial Networks (GANs), often lack explicit spatial grounding and structural constraints, resulting in spatial and physical inconsistencies in generated scenes. To address these challenges, we introduce WMGen-v1, an agentic text-based world model framework for long-tail spatial data generation. WMGen-v1 employs a Large Vision-Language Model (LVLM) to construct a structured scene representation from a single reference image, while a Large Language Model (LLM) performs guidance-based scene expansion under physical plausibility and commonsense constraints. Subsequently, conditioned on the structured semantic representations produced by this reasoning process, a diffusion model generates diverse and physically grounded long-tail training data. Experiments on internal industrial datasets, ROADWork, and LaRS benchmarks demonstrate that WMGen-v1 outperforms baseline approaches. Notably, detectors trained solely on WMGen-v1 synthetic data approach real-only performance on aggregate dataset-level metrics, highlighting its potential to alleviate long-tail data scarcity for downstream spatial perception.

---

## 15. Learning a Normal World Model for Few-Shot Boundary-Calibrated Abnormality Detection

**Authors:** Weizhi Nie, Weichao Liu, Weijie Wang, Yuting Su
**arXiv:** [2606.22261](https://arxiv.org/abs/2606.22261)
**Categories:** Machine Learning (cs.LG); Computer Science and Game Theory (cs.GT)

Abnormality detection in complex systems faces two practical barriers: abnormal labels are scarce, and binary labels do not quantify how far an event has departed from normal behavior. We study a normal-world modeling formulation for this setting. Instead of learning a large and incomplete space of abnormal classes, the model learns the normal world from abundant normal events and uses a few abnormal examples only to calibrate the boundary of normality. We instantiate this idea as a Hypergraph Entropic Normal-World Model. The model represents multivariate sensor windows as context-conditioned hypergraphs, where hyperedges capture high-order relations among groups of variables. It then defines abnormality by an entropy-aware normal-world energy that combines temporal prediction surprise, hypergraph consistency surprise, and latent normal-manifold departure. On the NASA C-MAPSS turbofan degradation benchmark, the proposed full energy achieves strong zero-shot and few-shot performance across all four subsets and reaches AUROC 0.9983 on FD004, the most complex setting with multiple operating conditions and fault modes. Beyond standard detection metrics, we introduce mechanistic validation tests to probe whether the energy encodes normal-world structure rather than a superficial input-output mapping. The learned energy accepts unseen healthy engines, increases along degradation trajectories, and sharply penalizes context-mismatched cross-variable coupling breaks. These results suggest that normal-world energy can serve as an anomaly score, a graded risk measure, and a testable representation of normal system behavior under severe abnormal-label scarcity.

---

## 16. VegSim: A Geospatial World Model for Scenario-Conditioned Vegetation Simulation

**Authors:** Irene Iele, Elena Mulero Ayllón, Paolo Soda, Matteo Tortora
**arXiv:** [2606.21961](https://arxiv.org/abs/2606.21961)
**Categories:** Machine Learning (cs.LG)

Vegetation monitoring under climate stress requires answering not only how it will evolve given the expected weather, but how it would respond to alternative meteorological conditions. Forecasting models return the expected vegetation state for the observed weather and cannot answer these scenario-conditioned questions, because future weather is fixed to the recorded trajectory. We present VegSim, a geospatial world model for scenario-conditioned vegetation simulation. VegSim infers a latent vegetation state from sparse satellite-derived NDVI histories, past meteorological covariates, and static spatial context, propagates it forward under future weather forcing through recurrent latent dynamics, and decodes predictive NDVI quantiles at each lead time. Because future forcing enters as a controllable input, the same trained model supports probabilistic forecasting under observed weather and conditional simulation under user-defined meteorological forcing, without supervision on scenario responses. We evaluate VegSim on GreenEarthNet across in-distribution data and spatial, temporal, and joint spatial-temporal shift, where it achieves strong point and probabilistic accuracy against time series and Earth observation forecasting baselines while using a compact architecture. We then simulate vegetation responses across Europe under four meteorological scenarios, and in a France summer 2022 case study, obtaining spatially coherent patterns consistent with known sensitivity to temperature and precipitation. The code is available at this https URL.

---

## 17. VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models

**Authors:** Florian Seligmann, Emiliyan Gospodinov, Enes Ulas Dincer, Gerhard Neumann
**arXiv:** [2606.21386](https://arxiv.org/abs/2606.21386)
**Categories:** Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action models (VLAs) achieve state-of-the-art performance on many robotic manipulation tasks, yet they can still behave unpredictably in out-of-distribution scenarios. Runtime failure detection is therefore essential for the safe real-world deployment of VLAs. However, existing task failure detectors require computationally expensive action sampling, are based on architectural assumptions that limit their applicability to VLAs, or need access to failure rollouts. We propose VLA-FAIL, a lightweight and broadly applicable failure detection framework for VLAs that combines two novel failure detectors with minimal overhead, without requiring failure data. The first, last-layer Mahalanobis distance (LLMD), detects out-of-distribution states by measuring token-wise deviations in last-layer features relative to the training data. The second, action chunk consistency (ACC), exploits the temporal overlap induced by receding-horizon control and detects failures when consecutive action chunks become inconsistent. To capture the trade-off between detection accuracy and detection latency, we introduce AUCPDT, a threshold-independent metric that jointly evaluates precision, recall, and detection time. Through extensive real-world and simulation experiments, we demonstrate that LLMD and ACC capture complementary failure modes whose combination enables reliable and early failure detection across diverse tasks, frequently outperforming significantly more expensive baseline methods.

---

## 18. SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors

**Authors:** Pratyaksh Rao, Wancong Zhang, Randall Balestriero, Yann LeCun, Giuseppe Loianno
**arXiv:** [2606.23444](https://arxiv.org/abs/2606.23444)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Accurate dynamics models are critical for informed decision-making in robotic systems, particularly for agile aerial vehicles operating under uncertainty. Neural network dynamics models are attractive for capturing complex nonlinear effects, but existing predictive approaches struggle with long-horizon forecasting because their autoregressive rollout mechanism amplifies errors over time. Joint Embedding Predictive Architectures (JEPAs) offer a compelling alternative by modeling dynamics in latent space, yet prior JEPA-style methods for robot navigation have been studied primarily for kinematic-level planning, with limited investigation in high-frequency control. In this work, we introduce the JEPA-style model for real-time quadrotor control. The proposed approach combines a latent dynamics model with a novel physics-inspired prober that maps frozen latents to interpretable state, enabling physically grounded long-horizon prediction. Additionally, we combine the learned model with a sampling-based optimal control solution to take advantage of its predictive capabilities for real-time control on embedded hardware. Finally, to reduce the dependence on expensive and unsafe real-world data collection, we develop a structured pipeline for automated dataset generation. Extensive open-loop and outdoor closed-loop experiments demonstrate accurate prediction, robust zero-shot sim-to-real transfer, and strong generalization across diverse operating conditions.

---

## 19. ASCII Art Turns LLMs into VLA Controllers

**Authors:** Yitao Jiang, Roy Xing, Luyang Zhao, ..., Muhao Chen, Devin Balkcom
**arXiv:** [2606.21470](https://arxiv.org/abs/2606.21470)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Vision--Language--Action (VLA) controllers are often built by extending vision--language models (VLMs) with action supervision, relying on multimodal backbones with large data and compute requirements. We demonstrate that a text-only large language model (LLM) can be adapted into a VLA-style controller when visual observations are rendered into a text input using an ASCII representation. This ASCII-as-vision interface enables existing training and deployment stacks for LLMs to efficiently condition on visual state, follow natural-language instructions, and produce constrained, executable actions. We fine-tune and compare multiple LLMs and VLMs across model families and scales, using both expert demonstrations from a planning-based teacher, as well as DAgger for iterative improvement. In a 2D manipulation benchmark, in both simulation and on a physical manipulator, the resulting controllers can identify task-relevant entities and plan feasible action sequences. Our results suggest that ASCII rendering can serve as a lightweight, interpretable modality bridge from images to text, complementing conventional VLA pipelines, and opening directions for VLA research with text-only backbones.

---

## 20. NAC: Neural Action Codec for Vision-Language-Action Models

**Authors:** Ahad Jawaid, Yu Xiang
**arXiv:** [2606.21372](https://arxiv.org/abs/2606.21372)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Vision-language-action (VLA) models rely on discrete action tokenizers to bridge continuous robot control and autoregressive sequence modeling, yet existing tokenizers often trade off between compression, latency, and downstream performance. We revisit this design through the lens of neural audio codecs-convolutional encoder-decoder architectures with residual vector quantization that serve as the standard front end for audio foundation models. Motivated by their success, we introduce the Neural Action Codec (NAC), which treats short robot action trajectories as multi-channel 1D signals and compresses them using a multi-scale RVQGAN architecture. We observe that audio-specific mel-spectrogram objectives are ill-suited for kinematic signals; however, by replacing them with simple time-domain and non-mel spectral reconstruction losses, audio-codec-style models can autoencode actions with high fidelity without substantial architectural changes. NAC provides a compact, ordered token space via offset codebooks, enabling standard autoregressive policies to operate over short, structured sequences. Meanwhile, a Vocos-style decoder with an ISTFT head and adversarial discriminators recovers smooth, detailed trajectories. Across LIBERO-10, RoboMimic, and a suite of real-world manipulation tasks, NAC achieves lower reconstruction error and higher success rates than binning, FAST, and prior VQ-based tokenizers at comparable or better compression rates. These results demonstrate that repurposed neural audio codecs offer a strong, practical backbone for learned action tokenization in modern VLAs.

---

## 21. LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

**Authors:** Rongxu Cui, Zongzheng Zhang, Jingrui Pang, ..., Ya-Qin Zhang, Hao Zhao
**arXiv:** [2606.23686](https://arxiv.org/abs/2606.23686)
**Categories:** Robotics (cs.RO)

Despite the impressive manipulation capabilities of Vision-Language-Action (VLA) models, their operational safety under strict constraints remains largely unverified. To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity. To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. Leveraging this infrastructure, we curate a large-scale dataset of 19,664 strictly collision-free demonstrations with extensive domain randomization. We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. Our analysis reveals a critical generalization-safety tension: although high-diversity training fosters safer trajectories, task success remains fundamentally bottlenecked by sub-optimal trajectory synthesis and semantic misalignment. By providing a scalable pipeline, a robust dataset, and profound failure-mode insights, LIBERO-Safety establishes a crucial foundation for developing safe and reliable VLA models.

---

## 22. Flatness Preserves Instruction Following in Vision-Language-Action Models

**Authors:** Haochen Zhang, Yonatan Bisk
**arXiv:** [2606.23641](https://arxiv.org/abs/2606.23641)
**Categories:** Robotics (cs.RO)

Vision-language-action (VLA) models have the potential for open-world generalization by leveraging pretrained vision-language representations, yet downstream finetuning on limited robot data often degrades these representations, leading to brittle policies that ignore language instructions in favor of visual shortcuts, a failure mode we term instruction blindness. We hypothesize that standard finetuning with limited data applies gradients to a sparse set of points, which manifests as a sharp loss landscape with high-curvature minima. We propose to address this directly through flatness-preserving optimization while finetuning on the exact same data, where learning a flatter landscape results in a model more robust to perturbations in the weight space. Specifically, we demonstrate that simply applying sharpness-aware minimization during VLA finetuning significantly improves instruction following by over 60% across multiple simulation and real-world benchmarks without additional data, architectural modification, or retraining. We further analyze the effect of selective sharpness, quantify its effects, and show that our approach is complementary to existing guidance techniques. Project page can be found at this https URL.

---

## 23. dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models

**Authors:** Yuhao Wu, Yitian Liu, Weijie Shen, ..., Wenbo Ding, Yao Mu
**arXiv:** [2606.23623](https://arxiv.org/abs/2606.23623)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have established a powerful paradigm for generalist robotic manipulation by grounding control into the semantic reasoning of VLMs. Prevailing architectures typically model actions continuously via diffusion or flow processes, or discretely through either autoregressive generation or parallel decoding. Recently, Discrete Diffusion VLAs (dVLAs) have emerged as a distinct alternative, unifying vision, language, and action into a single discrete token space via masked generative modeling. While combining iterative refinement with unified representations, its training has thus far been restricted to Supervised Fine-Tuning (SFT), leaving the potential of Reinforcement Learning (RL) for further policy refinement largely unexplored. A fundamental challenge in RL for dVLAs is that the marginal probability of the final action generated by dVLAs remains intractable. To solve this problem, we propose \textbf{dVLA-RL}, shifting the learning objective from the marginal action probability to the joint probability of the sampled generation path. Specifically, by modeling the denoising process as a Markov Decision Process (MDP), we mathematically formulate this path probability as a product of step-wise transitions. This trajectory-level objective provides a unified formulation that natively accommodates variable denoising steps. Leveraging this intrinsic fexibility, we introduce a unified step scheduling approach for complex multi-task learning, tailoring denoising steps to specific task complexities to maximize both success rates and computational effciency. Extensive evaluations demonstrate that our approach achieves a success rate of \textbf{99.7\%} on LIBERO. Furthermore, it establishes strong VLA-based results on RoboTwin 2.0 by delivering a \textbf{30.6\%} improvement over the SFT baseline, remaining competitive with strong World-Action Model baselines.

---

## 24. KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies

**Authors:** Yihan Zeng, Minghao Ye, Yiyuan Chen, ..., Zike Yan, Zhongyu Li
**arXiv:** [2606.23589](https://arxiv.org/abs/2606.23589)
**Categories:** Robotics (cs.RO)

Long-horizon robot manipulation remains challenging because similar observations may occur at different execution stages, while the appropriate action depends on previously completed operations. Memory can address this ambiguity by enabling policies to infer task progress from execution history. However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. In this work, we propose propose KEMO, a lightweight plug-in memory framework that automatically selectively preserves keyframes associated with task-relevant state changes for VLA policies. KEMO combines robot kinematics with visual filtering to detect events, encodes the selected keyframes as compact temporally ordered memory tokens, and integrates them with current visual features through cross-attention and gated residual fusion for VLA training. The detected events also define higher-weight training samples near critical transitions. We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). Compared with the memory-free baseline (e.g., $\pi_{0.5}$), KEMO improves aggregate Task Success Rate by 23.6\% and Stage Completion Rate by 34.1\%. Ablations show that event-driven keyframe selection outperforms uniform sampling and recent-frame retention, while the proposed gated fusion and keyframe-aligned loss weighting provide complementary gains.

---

## 25. BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation

**Authors:** Jinsong Lin, Chi kit Ng, Zhiyong Xiong, ..., Huxin Gao, Hongliang Ren
**arXiv:** [2606.23531](https://arxiv.org/abs/2606.23531)
**Categories:** Robotics (cs.RO)

Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic navigation.

---

## 26. IOI: Decoupling Kinematics and Physics for Interactive World Models

**Authors:** Chengyu Bai, Peidong Jia, Tiecheng Guo, ..., Jian Tang, Shanghang Zhang
**arXiv:** [2606.23296](https://arxiv.org/abs/2606.23296)
**Categories:** Robotics (cs.RO)

Developing generalist embodied agents requires interactive environments providing visually realistic feedback and accurate action-conditioned dynamics. Interactive world models address this by simulating such complex dynamics. However, purely data-driven methods struggle to ensure precise control alignment and physically plausible visual feedback due to a lack of explicit structural constraints. To address this, we propose IOI, a hybrid interactive world model integrating analytical kinematic priors with learned physical dynamics. Unlike data-driven approaches prone to spatiotemporal drift, IOI introduces explicit kinematic guidance, computing forward kinematics from action sequences for accurate motion trajectories. These trajectories are rendered into synchronized front, side, and top orthographic projections, eliminating the need for extrinsic camera calibration. A Multi-view Kinematic Aggregation and Injection module fuses these geometric cues and injects them into the video generator, providing geometry-consistent guidance. Conditioning video generation on these deterministic trajectories establishes a synergy between the analytical simulator and the world model. Decoupling deterministic motion into the kinematic prior frees the generator to model stochastic physical interactions. Experiments on the RoboTwin benchmark validate IOI across kinematic fidelity, out-of-distribution (OOD) generalization, and policy evaluation. IOI achieves state-of-the-art simulation performance and robust zero-shot generalization to unseen OOD tasks. Furthermore, IOI serves as a reliable policy evaluator, yielding success rates closely aligning with ground-truth physics simulators. On real-world platforms, policies trained on IOI-synthesized data match those trained on teleoperation demonstrations, solidifying its practical value for embodied policy learning.

---

## 27. Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation

**Authors:** Yang Yang, Yuchuang Tong, Zhengtao Zhang, ..., Kehu Yang, Miao Xin
**arXiv:** [2606.23280](https://arxiv.org/abs/2606.23280)
**Categories:** Robotics (cs.RO)

Automated Reward Design (ARD) aims to replace manual reward engineering in reinforcement learning with language-driven reward function synthesis. However, existing approaches based on large language models (LLMs) remain inherently correlation-driven, relying on iterative environmental feedback to refine reward hypotheses for each specific task. This paradigm not only results in inefficient reasoning but also makes LLMs susceptible to semantically plausible yet causally spurious reward components, leading to ineffective optimization. To address these limitations, we propose the Causal Reward World Model (CRWM), which explicitly models the causal topological relationships between candidate reward components and task-targeted physical variables through offline pre-training on multi-task interaction data. Based on a coarse-to-fine pre-training strategy, we introduce a joint optimization module that integrates Explicit Mechanism Decoupling with Confidence-Aware Soft Fusion to refine coarse structural priors using micro-level trajectories, thereby constructing a robust and interpretable causal skeleton. During inference, LLMs leverage CRWM as a task-irrelevant causal prior to constrain the reward generation, enabling zero-shot reward function design. Our work opens up a new white-box paradigm for the ARD problem. Extensive experiments on complex continuous control benchmarks demonstrate that CRWM generates executable reward functions without feedback-driven reward refinement, significantly reducing the design latency for acquiring new robotic skills while matching or surpassing state-of-the-art performance, and further exhibits strong generalization capabilities across unseen tasks and diverse robotic embodiments.

---

## 28. Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models

**Authors:** Pinhao Song, Ze Fu, Yutong Hu, Renaud Detry
**arXiv:** [2606.23147](https://arxiv.org/abs/2606.23147)
**Categories:** Robotics (cs.RO)

We propose Assistron, a shared autonomy model that leverages Vision-Language-Action (VLA) models to assist the user in daily activities. Our approach is grounded in two core principles: (1)~minimizing human cognitive and physical effort by leveraging VLA-driven autonomy for macro-movements, and (2)~prioritizing human intervention specifically at critical failure points. Driven by the user's verbal language commands, Assistron utilizes the VLA to autonomously execute macro-reaching trajectories, saving users' effort. In contact-rich interactions where VLAs tend to fail, Assistron employs a phase-aware interaction detection mechanism and solicits the user to intervene, in turn adjusting the VLA's action generation via flow matching guidance. Critically, our formulation eliminates the need for VLA fine-tuning, protecting its broad behavioral priors from catastrophic forgetting and ensuring the model does not become a narrow specialist. We validate our approach on a comprehensive multi-task scene recovery benchmark encompassing diverse daily manipulation skills. Empirical results demonstrate that Assistron significantly improves task success rates over pure autonomous baselines while significantly reducing human cognitive and physical workload compared to traditional teleoperation, offering a scalable, smooth, and effortless paradigm for assistive manipulation. The code is available in this https URL.

---

## 29. Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents

**Authors:** Haoran Zhang, Yifu Lu, Boyang Wang, ..., Mengdi Wang, Odest Chadwicke Jenkins
**arXiv:** [2606.23085](https://arxiv.org/abs/2606.23085)
**Categories:** Robotics (cs.RO)

Long-horizon tasks are common in real-world robotic deployments, yet failure detection for such tasks remains underexplored. Detecting failures in long-horizon robotic tasks is particularly challenging because failure onset is often ambiguous and dense temporal annotations are typically unavailable. We present Foresight, a failure detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model. Foresight is trained using only final task-level success or failure labels. By leveraging predictive world-model embeddings, our method provides a unified framework for failure detection across different policies. We further use functional conformal prediction (FCP) to calibrate detection thresholds adaptively. We evaluate Foresight with state-of-the-art vision-language-action policies in simulation on LIBERO-Long, ManiSkill-Long, and BEHAVIOR-1K, compare it against state-of-the-artfailure detection methods, and validate it on real robots with three long-horizon tasks on a ReactorX-200 arm and one task on a Franka arm. Our results suggest that action-conditioned world-model embeddings provide a scalable representation for reliable failure monitoring in long-horizon manipulation.

---

## 30. Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA

**Authors:** Michael Piseno, Guy Tevet, C. Karen Liu
**arXiv:** [2606.22836](https://arxiv.org/abs/2606.22836)
**Categories:** Robotics (cs.RO)

We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist camera. The end-effector occupies a large and consistent region of the wrist view and masking it allows for embodiment-agnostic visual reasoning. Cloak renders a mask in simulation from the robot's known geometry, accurately and in real time, with no segmentation or generative models. During training, we augment the mask so the model generalizes to embodiments unseen at training time. We demonstrate the recipe with Cloak-VLA, a VLA trained with Cloak on a single parallel-jaw gripper dataset. No data of new embodiments is ever collected. Cloak-VLA transfers zero-shot to various unseen embodiments, including another gripper, another arm, and a five-fingered hand, while preserving the source embodiment's performance. By decoupling the wrist view from its own embodiment, Cloak allows data to outlive the hardware it was collected on.

---

## 31. UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models

**Authors:** Lin Sun, Zhiwei Guan, Conglin Wang, ..., Jiale Cao, Lige Liu
**arXiv:** [2606.22794](https://arxiv.org/abs/2606.22794)
**Categories:** Robotics (cs.RO)

Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. Moreover, because the action expert receives only the VLM's final-layer representation at a single fixed frequency, rich intermediate features are discarded, limiting both information coupling and manipulation precision. Inspired by multi-timescale neural processing in the human brain, we introduce UniFS, a unified fast-to-slow architecture that resolves these challenges through three key designs. First, we stratify the VLM layers into groups with progressively decreasing update frequencies, enabling shallow layers to capture fast-changing dynamics while deeper layers cache stable semantic context. Second, a latent vector inversion mechanism re-routes the interaction order between multi-scale VLM features and the action expert, aligning fast-varying representations with fine-grained action decoding and slow-varying ones with coarse planning. Third, a multi-level supervision strategy enforces a coarse-to-fine learning hierarchy across temporal scales. Together, these designs enable richer cross-frequency information transfer within a single backbone, while the low-frequency pathways additionally preserve temporal context across steps. Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). Real-robot experiments on a Franka platform further validate its practical applicability. Code is opensourced at this https URL.

---

## 32. Temporal Logic Guidance for Action-Only Diffusion Policies with World Models

**Authors:** Moritz Zoellner, Anastasios Manganaris, Rohan Paleja
**arXiv:** [2606.22729](https://arxiv.org/abs/2606.22729)
**Categories:** Robotics (cs.RO)

Diffusion policies enable multimodal robot behavior but offer limited ability to choose among behavior modes at inference time, even though such control is desirable in human-robot settings. Prior solutions to this lack of control have utilized Signal Temporal Logic (STL) to express human intentions and provide corresponding guidance for diffusion policy inference. However, these approaches can only guide diffusion policies that jointly generate future actions and states, increasing both complexity and runtime. We propose a novel guidance method for action-only diffusion policies that uses a separate learned world model to enable differentiable evaluation of STL robustness, with its gradient then injected into the diffusion process. This steers behavior toward constraint satisfaction without retraining, improving constraint adherence while preserving task performance. On the Can Transport task from Robomimic, our method maintains 100% task success while reducing constraint violations from over 80% for baseline methods to 4%. We also discuss extensions toward improved robustness and more complex constraints.

---

## 33. Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data

**Authors:** Yangtao Chen, Zixuan Chen, Peiyang Wang, ..., Jieqi Shi, Yang Gao
**arXiv:** [2606.22136](https://arxiv.org/abs/2606.22136)
**Categories:** Robotics (cs.RO)

Scaling dexterous manipulation requires generalization across objects, scenes, and tasks, yet existing data sources face a trade-off between scale and scene/embodiment alignment: teleoperation data is well aligned with robot deployment but expensive to collect; simulation is scalable but limited by the sim-to-real gap; and real egocentric videos scale effectively but remain misaligned with robot deployment. We propose Wh0, a framework that uses generative video world models as scalable and controllable sources of egocentric human-hand manipulation data to unlock the manipulation capabilities of pretrained dexterous VLA models. Conditioned on language, objects, and scenes, Wh0 uses a generative world model to produce WM-H, a 50k-episode dataset of egocentric human-object interaction videos. Wh0 then converts the generated videos into robot-trainable supervision through hand motion reconstruction and visual editing. Co-trained with a limited amount of real robot data, WM-H adapts pretrained VLA models to dexterous manipulation deployment. Across 18 real-world dexterous manipulation tasks, compared with a model post-trained only on robot data, Wh0 improves zero-shot success on unseen tasks from 8.3% to 38.9%. Ablation studies further show that scalable generation and scene/embodiment alignment are key drivers of performance gains. Videos and open-source code can be found on our project website: this https URL.

---

## 34. UniviewVLA: A Unified Multiview Vision-Language-Action Model with World Modeling

**Authors:** Tao Xu, Runhao Zhang, Zhijian Huang, ..., Guang Chen, Jinghui Lu
**arXiv:** [2606.21501](https://arxiv.org/abs/2606.21501)
**Categories:** Robotics (cs.RO)

Occluded tasks remain a bottleneck in robot manipulation. Existing solutions either deploy additional physical cameras requiring training-inference camera parity, or rely on explicit 3D reconstruction with high computational cost. Moreover, both approaches rely on standard agent-view and wrist-view observations, while failing to capture occlusion information and future scene evolution. To this end, we propose UniviewVLA, a unified multiview Vision-Language-Action model with world modeling, which infers multiview scene evolution for action prediction from only standard two-camera observations. We demonstrate that by leveraging generated multiview future views from the world model, UniviewVLA reveals occluded cues and models future scene evolution, improving action prediction and removing the need for extra hardware or explicit reconstruction. Besides, to accelerate inference while preserving prediction accuracy, UniviewVLA develops Motion-Informative Token Compression, which compresses each generated view from 625 to 16 tokens and reduces per-view latency from 6-7s to 0.2-0.3s. UniviewVLA also proposes training-free Action-Entropy View Selection, which dynamically identifies the most action-informative view at different inference stages. Extensive experiments show that UniviewVLA achieves 95.8% on LIBERO and 4.60 on CALVIN ABCD to D, both standard occlusion-free benchmarks. On customized occlusion-focused tasks, it improves success rate from 40.0% to 73.3%, and average real-robot success rate by 33.4 points, demonstrating stronger occlusion-focused performance without sacrificing standard occlusion-free benchmarks.

---

## 35. MV-WAM: Manifold-Aware World Action Model with Value Augmentation

**Authors:** Jintao Chen, Peidong Jia, Qingpo Wuwu, ..., Jian Tang, Shanghang Zhang
**arXiv:** [2606.21088](https://arxiv.org/abs/2606.21088)
**Categories:** Robotics (cs.RO)

Achieving robust and generalizable manipulation across diverse environments remains a fundamental challenge in embodied robotics. Recent world action models achieve strong in-domain performance, yet their gains do not extend proportionally to out-of-distribution scenarios. We attribute this to a structural mismatch between visual and action modalities, whose intrinsically heterogeneous manifolds cause joint optimization to disproportionately degrade action robustness under distribution shift. To address this, we propose MV-WAM, a novel end-to-end framework that jointly models visual prediction, action generation, and value estimation designed to effectively leverage video priors during both training and inference for enhanced action generalization. Key to this unification is a cross-modality causal mask that hierarchically grounds actions in predicted video frames and value function tokens in both modalities. To further narrow the generalization gap, MV-WAM adopts a manifold-aware optimization scheme that explicitly accounts for the structural heterogeneity across modalities. Finally, MV-WAM introduces a progress-value regulation mechanism that estimates task completion and detects misalignment between predicted frames and generated actions, enabling the policy to autonomously identify execution deviations and recover through value-guided rollback. On the RoboTwin simulation, MV-WAM achieves a 55.7% mean success rate on random scenarios without any randomized action supervision, outperforming the strongest baseline by 29.3%. MV-WAM achieves a 77.5% mean success rate across four real-world tasks of varying difficulty on a dual-arm robot. Our results demonstrate that manifold-aware cross-modal alignment is essential for robust policy generalization, offering a path toward deployable robotic manipulation.

---

## 36. World Action Models: A Survey

**Authors:** Qiuhong Shen, Shihua Zhang, Yue Liao, ..., Shuicheng Yan, Xinchao Wang
**arXiv:** [2606.20781](https://arxiv.org/abs/2606.20781)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

World Action Models (WAMs) are embodied predictive-action models that make a forecast of the future available to action. Recent WAMs repurpose large video generation models, and a parallel line relies on language or vision-language backbones without a video-generation core. This rapid expansion has blurred the boundary among broad world models, video generation models, action-grounded video world models, Vision-Language-Action policies, and WAMs. This survey gives the field a common account. It first clarifies these boundaries, then organizes existing works through two complementary views. The first view asks what each method is required to generate, spanning rendered futures, latent futures, and video-generation-free action reasoning. The second view decomposes each method by predictive substrate, backbone, action coupling, and deployment regime. This anatomy supports a unified discussion of interactability, causality, persistence, physical plausibility, and generalization, followed by data, evaluation, and open challenges. Across these axes, a consistent design pattern emerges: WAMs are not simply video generators with action heads, but predictive-action methods whose design choices trade representational richness against compute, memory, latency, and action-label cost. The field is moving toward methods that generate less of the future while preserving what control requires. The survey homepage is available at this https URL.

---

## 37. Perturbation-Based Uncertainty for Failure Detection in Vision-Language-Action Models

**Authors:** Yousung Lee, Dongsoo Har
**arXiv:** [2606.20754](https://arxiv.org/abs/2606.20754)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have shown strong performance in robotic manipulation, but reliable uncertainty quantification remains challenging, particularly under distribution shift. Unlike autoregressive policies, many modern VLA models generate continuous actions through regression or flow-based generation, where explicit predictive probabilities are unavailable. Moreover, existing approaches often rely on stochastic action sampling or supervised failure labels, limiting their applicability across diverse pretrained VLA models. In this work, we propose a label-free and model-agnostic framework for inference-time uncertainty estimation through hidden activation perturbations, motivated by Bayesian perspectives on local model variations. Specifically, we inject Gaussian perturbations into transformer hidden activations and estimate epistemic signals from disagreement across perturbed action predictions. Experiments on LIBERO and LIBERO-PRO show that perturbation-based uncertainty consistently improves failure detection under distribution shift compared to sampling-based uncertainty, providing a practical uncertainty signal for VLA models.

---

## 38. SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model

**Authors:** Kai Tang, Peidong Jia, Zhong Chu, ..., Jian Tang, Shanghang Zhang
**arXiv:** [2606.20698](https://arxiv.org/abs/2606.20698)
**Categories:** Robotics (cs.RO)

Safe control is a prerequisite for real-world embodied intelligence, for which safe reinforcement learning has emerged as a promising paradigm. However, existing safe reinforcement learning methods either require costly real-world exploration or depend on hand-crafted safety functions. Neither scales to vision-language-action models deployed in open-world physical environments. We propose SafeDojo, the first model-based safe reinforcement learning framework for vision-language-action policies designed to learn safe actions through world model-based imagination. Specifically, SafeDojo performs online reinforcement learning on top of an interactive video world model. The world model generates action-conditioned future predictions, from which a tailored ResNet success classifier estimates per-step task progress from imagined frames and a lightweight safety head predicts per-step safety costs from latent context together with the proposed action chunk, enabling simultaneous assessment of task execution and trajectory safety. The decoupled task-reward and safety-cost signals are balanced through a Lagrangian-based constrained GRPO objective, enabling coordinated improvement of task success and safety under explicit constraints. On SafeLIBERO, SafeDojo achieves the best aggregate task success, safe success, and execution efficiency among inference-time safety, model-free RL, and model-based RL baselines, with the best average safe-success rate on both levels and an 8.25 percentage-point improvement over the strongest baseline on Level I. Real-world Franka deployment further shows the best average task and safe-success rates across five tasks. Our results position world model-based safe reinforcement learning as a scalable and generalizable path toward safe embodied intelligence.

---

## 39. A Watermark for Vision-Language-Action and World Action Models

**Authors:** Yule Liu, Shuai Liu, Jiaheng Wei, Xinlei He
**arXiv:** [2606.23574](https://arxiv.org/abs/2606.23574)
**Categories:** Cryptography and Security (cs.CR); Robotics (cs.RO)

Vision-language-action (VLA) models and world-action models (WAM) are the generative models now driving general-purpose robot control, turning raw camera input directly into motor commands. They are increasingly deployed as black-box services, where a partner runs the policy through an interface while the owner keeps the weights private. Training such a model takes proprietary data and heavy computational power, making the deployed model itself a valuable intellectual property.
To address this, we propose the \emph{keyed latent-provenance verification} method, which fingerprints the policy through the seed of the Gaussian noise vector that the models draw before generation. At the injection stage, the owner swaps this seed for a keyed one with the same distribution as ordinary noise, so the fingerprinted actions are statistically identical to those of an ordinary run and an adversary watching the output finds no signal to detect or remove. At the verification stage, the owner runs the suspect model under authorized access and records the action channels the robot executes, a partial and possibly post-processed view of the policy's output. From this view, the verifier recovers the seed by gradient-based maximum a posteriori (MAP) optimization, tests it for the secret key to score each rollout, and aggregates these scores into a single decision on whether the suspect model belongs to the owner.
We evaluate the method on two representative models across two robot suites. The experiments cover detection of the fingerprint, identification of which of several keys a suspect carries, robustness to a range of attacks, and an analysis of why the design works. Across both models, the fingerprint can be detected reliably with little change to task performance, and it remains detectable under output-side removal attacks and weight-level edits.

---

## 40. Compression and Retrieval: Implicit Memory Retrieval for Video World Models

**Authors:** Zhan Peng, Jie Ma, Huiqiang Sun, ..., Jun Liang, Jing Li
**arXiv:** [2606.23105](https://arxiv.org/abs/2606.23105)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video world models hold promise for simulating interactive environments, yet maintaining consistent long-term memory across complex camera trajectories remains a critical challenge. Existing methods typically rely on computationally expensive context scaling or rigid heuristic retrieval mechanisms, which lacks generalization to varying camera trajectories and environments. In this paper, we propose Compression and Retrieval (CaR), an attention-driven implicit memory retrieval mechanism to overcome these limitations. By injecting viewpoint information via positional encoding, our method performs flexible memory retrieval through attention computation. To efficiently process extended contexts with minimal computational overhead, we further introduce a lightweight context compression network. Furthermore, we construct SceneFly, a large-scale synthetic dataset featuring realistic camera trajectories and frame-level annotations to train and evaluate long-horizon video world models. Extensive experiments demonstrate that our approach achieves state-of-the-art results on established benchmarks and exhibits strong generalization to open-domain scenes.

---

## 41. PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models

**Authors:** Xianghui Wang, Feng Chen, Wenbo Zhang, ..., Changsheng Li, Yinjie Lei
**arXiv:** [2606.22540](https://arxiv.org/abs/2606.22540)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency. While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic \textbf{policy efficiency} of these models remains largely unexplored. Policy efficiency is fundamentally affected by two factors, namely the effective executable length of predicted action chunks and the total physical steps required to complete a task. These two factors jointly determine the total number of forward inference calls during execution. We observe that current VLA policies struggle with planning unreliability and action redundancy, suffering from severe prediction degradation at the tail of action chunks and tending to generate unnecessarily redundant physical steps. To address this, we propose \textbf{PolicyTrim}, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps. For reliable chunk extension, we employ a dynamic exploration strategy that explicitly rewards the successful completion of longer executable lengths, progressively pushing the trustworthy prediction horizon to its empirical limit. For step efficiency, we design a redundancy-aware reward that directly favors successful task completions with fewer steps while penalizing unreproducible shortcuts, effectively eliminating redundant physical actions. Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3$\times$ and reduces physical execution steps by 51.4\%. Ultimately, our framework delivers up to a 5.83$\times$ end-to-end deployment speedup without compromising task success rates.

---

## 42. Semi-Supervised Vision-Language-Action Model

**Authors:** Hongyang He, Jiuming Liu, Victor Sanchez
**arXiv:** [2606.21493](https://arxiv.org/abs/2606.21493)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Emerging Technologies (cs.ET)

Vision-Language-Action (VLA) models enable robots to predict actions directly from visual observations and language instructions, but adapting them to new environments still depends on costly action-labeled demonstrations. To reduce this dependence, we study semi-supervised VLA adaptation under limited supervision signals, where only a small portion of trajectories contain robot actions and the remaining trajectories provide action-unlabeled vision-language observations. Unlike standard semi-supervised learning, the missing supervision is an embodied action signal that must be visually grounded, language-consistent, physically feasible, and temporally stable. To address this problem, we propose SemiVLA, a self-distilled teacher-student framework that learns from reliable pseudo-actions on unlabeled trajectories. SemiVLA introduces a VLA-specific reliability controller to assess vision-language alignment, action feasibility, and temporal transition consistency, and further updates the teacher through a Bottleneck-Projected Alignment Update to avoid noisy feedback contamination. With OpenVLA as the backbone, SemiVLA consistently improves multiple PEFT strategies across LIBERO and CALVIN. Under 10\% labeled trajectories, SemiVLA with Selective LoRA achieves 89.0\% average success on LIBERO, outperforming supervised LoRA by 8.0 points without extra inference cost.

---

## 43. BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving

**Authors:** Zhe Shuai, Xiaopeng Xie, Yikun Zeng
**arXiv:** [2606.21172](https://arxiv.org/abs/2606.21172)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video world models are increasingly used in autonomous driving to forecast future scene evolution and provide future-aware spatio-temporal representations for downstream action prediction. In perception-to-action pipelines, these representations can directly influence ego-vehicle waypoint planning, making the learned future dynamics a critical security-sensitive component. Despite their promise, the training-time security risks of autonomous-driving video world models remain largely unexplored. We present BadDreamer, a transferable spatio-temporal backdoor attack that targets the perception side of this pipeline. Unlike conventional backdoors that manipulate image labels, prompt outputs, or action supervision, BadDreamer poisons the learned transition dynamics of a video world model. It constructs trigger-erasure sequences in which an oncoming yellow delivery rider is visible in the observed context frames but erased from the future frames. After fine-tuning on a small fraction of such sequences, the compromised world model learns a hidden conditional association: when the physical trigger appears, it hallucinates a future where the rider disappears and the road appears clear. We further show that this corrupted future-aware representation can transfer to the downstream action module without directly modifying ego-trajectory labels, inducing unsafe non-evasive waypoint predictions. Our experiments instantiate this attack on a representative open-source perception-to-action pipeline, revealing a representation-level safety risk in autonomous-driving video world models and highlighting the need for backdoor-aware validation beyond clean generation quality.

---

## 44. Active Inference as the Test-Time Scaling Law for Physical AI Agents

**Authors:** Omar Hashash, Christo Kurisummoottil Thomas, Walid Saad, ..., Karl Friston, Adeel Razi
**arXiv:** [2606.22813](https://arxiv.org/abs/2606.22813)
**Categories:** Artificial Intelligence (cs.AI)

In this paper, a novel test-time scaling law for physical artificial intelligence (AI) agents is introduced. This scaling law enables physical AI agents to reason with their world models to generalize in unforeseen scenarios at test time. The derived scaling law is grounded in the first principle of active inference, which equips agents with the general objective to survive in the real world, under which their specific task objectives are subsumed. Active inference achieves this by providing the reasoning to resolve prediction errors that arise when the agent encounters unforeseen situations outside its training distribution, enabling generalization in non-stationary environments. The proposed scaling law captures this by dynamically updating the agent's policy with this reasoning at test time. This policy update is modeled as a soft Bayesian inference process in which beliefs about the policy are updated using the reasoning that reduces expected prediction errors under allowable policies as a likelihood. The resulting posterior policy admits a biological interpretation, recovering the scaling mechanism that engages the brain's basal ganglia and prefrontal cortex at test time. To solve this analytically intractable problem, a variational inference solution minimizing free energy bounds is developed. This solution extends to enable learning beyond training by reinforcing new instances, resolved at test time, in both the policy and world model. Unlike existing scaling laws constrained by model size and training data, the derived solution scales with the continuous real-world experience of a physical AI agent. Simulation results on an autonomous driving task demonstrate that the proposed solution outperforms model-free Q-learning and model-based Bayesian reinforcement learning, achieving robust generalization to unforeseen scenarios while improving inference efficiency by over 36%.

---

## 45. Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving

**Authors:** Zisheng Chen, Yuping Qiu, Jianhua Han, ..., Hang Xu, Xiaodan Liang
**arXiv:** [2606.22913](https://arxiv.org/abs/2606.22913)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Recent Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving by incorporating reasoning for better interpretability and planning quality. However, most existing approaches directly generate the final trajectory without explicitly examining its future consequences, which limits their reliability in complex and dynamic environments. To address this limitation, we propose IRR-Drive (Intend, Reflect, Refine), an adaptive multimodal reflection framework for autonomous driving. Specifically, to tightly couple high-level reasoning with physical constraints, IRR-Drive first generates a preliminary textual intention and anticipates potential interactions by predicting future semantic bird's-eye view (BEV) representations. This dual-modality (Text + BEV) reflection space explicitly models anticipated scene evolution, enabling the model to rigorously self-correct and refine its initial intent before generating the final trajectory. Furthermore, to balance planning performance and computational efficiency, we construct reflection-oriented training data and design an adaptive reflection reward, enabling the model to adaptively select its reasoning mode according to scene complexity. Instead of using reasoning primarily as an auxiliary interpretation, IRR-Drive directly integrates an adaptive reflection mechanism into the planning framework, enabling grounded, decision-aware trajectory correction that is driven by scene complexity. Our method achieves state-of-the-art performance on the NAVSIM benchmark in both PDMS and EPDMS. Extensive experiments demonstrate the effectiveness of our multimodal reflection framework and validate the efficacy of the proposed adaptive reflection strategy.

---

## 46. PoLAR: Factorizing Extent and Mode in Latent Actions for Robot Policy Learning

**Authors:** Youngjoon Jeong, Jihwan Yu, Minsoo Jo, Junha Chun, Taesup Kim
**arXiv:** [2606.21139](https://arxiv.org/abs/2606.21139)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Latent action pretraining learns representations of visual change from pairs of observations, but existing methods typically encode each transition as a single unstructured representation that entangles transition extent and transition mode. We introduce Polar Latent Actions with Radial structure (PoLAR), which imposes a radial-direction structure on latent actions, encouraging radius to encode transition extent and direction to retain transition mode. PoLAR uses temporal offset between two observations as a weak proxy for transition extent, encouraging latent action from observation pairs separated by larger temporal gaps to occupy larger radii. We instantiate this structure in hyperbolic space, whose expanding volume with radius offers a natural fit for more diverse transition modes at larger extents. Across in-task and large-scale pretraining settings, PoLAR improves downstream policy performance in simulation and real-world robot experiments, outperforming latent action baselines and strong pretrained VLAs. These results suggest that the geometry of the latent action space is an important design choice for transferring visual pretraining to downstream robot policy learning.

---

## 47. MemoryVAM: Integrating Memory into Video Action Model for Robot Manipulation

**Authors:** Yuxin Jiang, Chang Yu, Yunuo Chen, ..., Nishank Gite, Chenfanfu Jiang
**arXiv:** [2606.20679](https://arxiv.org/abs/2606.20679)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Video-world-model policies learn action-relevant representations by predicting future observations. However, they condition on only a short observation window, which renders long-horizon manipulation non-Markovian when the correct action depends on earlier events that are no longer visible. We present MemoryVAM, an episodic memory mechanism for video-world-model policies. We employ a Recap-Cue (RC) module, in which a Perceiver-based Recap Compressor maps per-frame CLIP embeddings into compact memory tokens, and a lightweight Cue Gate estimates task completion from memory and language. These tokens are injected into both the video backbone and the action decoder, aligning policy imagination with episode progress and conditioning actions on history. Our model trains the memory module with video prediction, a delta-reconstruction auxiliary loss, and episode-boundary supervision, requiring no per-frame progress labels. The same mechanism applies to UNet and Diffusion Transformer (DiT) backbones by changing only the cross-attention injection interface. On LIBERO-Mem, our model improves average success from 5% to 42.5%. On real robots, it achieves 78.3% success on counting tasks, 80.0% on spatial recall, and 75.0% on sequential tracking. Project page: this https URL

---

## 48. Inductive Generalization for Robotic Manipulation

**Authors:** Annabella Macaluso, Haochen Zhang, Ishaan Masilamony, Yingshan Chang, Yonatan Bisk
**arXiv:** [2606.20999](https://arxiv.org/abs/2606.20999)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Understanding the generalization capabilities of visuomotor policies is essential in the development of capable robotic agents. Generalizable models learn structures that transfer across domains. However, in practice, visuomotor policies test performance by interpolation on known distributions using unstructured domain shifts (e.g. lighting, clutter, diverse objects). We argue that to measure generalization capabilities we must instead test the inductive capacity of policies on progressively harder, out-of-distribution task variants. We call this inductive generalization, drawing directly on how axis-based evaluation has revealed inherent generalization limitations in language models (e.g. sequence length, counting) arXiv:2502.00197 . We provide a reusable and formal evaluation protocol for measuring inductive generalization in any manipulation policy, and establish baselines showing that existing paradigms fail this test; e.g. SoTA Vision-Language-Action models and find that policies that appear to generalize to prior domain shifts (distractors, etc) fail inductive generalization tests. These results expose a class of learning challenges orthogonal to those addressed by data and model scaling in robot learning, yet are imperative to solve in order to realize general purpose robots.

---

## 49. LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation

**Authors:** Jiaming Liu, Yinxi Wang, Chenyang Gu, ..., Hao Tang, Shanghang Zhang
**arXiv:** [2606.23685](https://arxiv.org/abs/2606.23685)
**Categories:** Robotics (cs.RO)

Human-hand demonstrations provide a direct and scalable source of physical interaction data for robot learning. While manual retargeting is indispensable for establishing kinematic action correspondence across different morphologies, robust transfer requires going beyond geometry to address the underlying alignment of physical dynamics between human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-robot action learning paradigm that extends reasoning-before-acting VLA by aligning human-hand and robot demonstrations in a shared latent reasoning space. Rather than mimicking human kinematics, LaST-HD trains an auxiliary action-conditioned world model on unpaired human-hand and robot trajectories to synthesize unified latent targets. After aligning cross-embodiment representations in this shared forward-dynamics space, these targets supervise LaST-HD's latent reasoning process, enabling it to internalize shared physical dynamics and drive efficient human-hand action learning. Moreover, we develop Out-of-Lab (OOL) Glove, a low-cost motion-capture glove tailored to LaST-HD for human-hand data collection. The captured human data provide precise keypoints and serve as universal action supervision across grippers and dexterous hands. Armed with the aligned latent space and high-fidelity human-hand data, we develop a progressive mixed-to-human training recipe comprising mixed human-robot co-training and human-hand online correction post-training. Through mixed co-training, LaST-HD improves generalization to novel objects, scenes, and positions using only human-hand demonstrations. With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.

---

## 50. Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation

**Authors:** Bruno Machado, Alexandre Chapin, Emmanuel Dellandrea, Liming Chen
**arXiv:** [2606.23420](https://arxiv.org/abs/2606.23420)
**Categories:** Robotics (cs.RO)

Flow matching has recently become a new standard for behavior cloning in robotic manipulation. However, state-of-the-art flow matching policies suffer from a systematic structural mismatch: they rely on a globally fixed isotropic source distribution despite the strongly fragmented and heteroscedastic structure of robotic action spaces. This agnostic initialization forces the model to learn highly entangled vector fields, bottlenecking training efficiency and limiting overall policy performance. To address this limitation, we introduce Latent Action Guided Flow Matching (LAFM), a novel framework that replaces the monolithic Gaussian with an adaptive library of learned prior distributions. By grounding these distributions using a latent action model, LAFM maps current observations to discrete motion primitives, selecting a specialized base distribution that provides an informed, structurally aligned initialization for the denoising process. This dynamic adaptivity naturally accommodates heteroscedasticity in human demonstrations and makes transport trajectories shorter and less entangled. Empirically, LAFM substantially outperforms standard flow matching formulations, increasing task success rates by 23.4% in real-world robotic deployments and by 10.4% on the LIBERO-90 benchmark. Furthermore, we demonstrate that LAFM achieves state-of-the-art results, surpassing massively pre-trained vision-language-action models while utilizing significantly smaller architectures.

---
