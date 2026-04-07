# arXiv Daily Digest — 2026-03-24

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 22

---

## 1. RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models

**Authors:** Dongyoung Kim, Sumin Park, Woomin Song, ..., Jaehyung Kim, Younggyo Seo
**arXiv:** [2603.21341](https://arxiv.org/abs/2603.21341)
**Categories:** Artificial Intelligence (cs.AI)

Improving embodied reasoning in multimodal-large-language models (MLLMs) is essential for building vision-language-action models (VLAs) on top of them to readily translate multimodal understanding into low-level actions. Accordingly, recent work has explored enhancing embodied reasoning in MLLMs through supervision of vision-question-answering type. However, these approaches have been reported to result in unstable VLA performance, often yielding only marginal or even negative gains. In this paper, we propose a more systematic MLLM training framework RoboAlign that reliably improves VLA performance. Our key idea is to sample action tokens via zero-shot natural language reasoning and refines this reasoning using reinforcement learning (RL) to improve action accuracy. As a result, RoboAlign bridges the modality gap between language and low-level actions in MLLMs, and facilitate knowledge transfer from MLLM to VLA. To validate the effectiveness of RoboAlign, we train VLAs by adding a diffusion-based action head on top of an MLLM backbone and evaluate them on major robotics benchmarks. Remarkably, by performing RL-based alignment after SFT using less than 1\% of the data, RoboAlign achieves performance improvements of 17.5\%, 18.9\%, and 106.6\% over SFT baselines on LIBERO, CALVIN, and real-world environments, respectively.

---

## 2. ARYA: A Physics-Constrained Composable & Deterministic World Model Architecture

**Authors:** Seth Dobrin, Lukasz Chmiel
**arXiv:** [2603.21340](https://arxiv.org/abs/2603.21340)
**Categories:** Artificial Intelligence (cs.AI); Distributed, Parallel, and Cluster Computing (cs.DC)

This paper presents ARYA, a composable, physics-constrained, deterministic world model architecture built on five foundational principles: nano models, composability, causal reasoning, determinism, and architectural AI safety. We demonstrate that ARYA satisfies all canonical world model requirements, including state representation, dynamic prediction, causal and physical awareness, temporal consistency, generalization, learnability, and planning and control. Unlike monolithic foundation models, the ARYA foundation model implements these capabilities through a hierarchical system-of-system-of-systems of specialized nano models, orchestrated by AARA (ARYA Autonomous Research Agent), an always-on cognitive daemon that executes a continuous sense-decide-act-learn loop. The nano model architecture provides linear scaling, sparse activation, selective untraining, and sub-20-second training cycles, resolving the traditional tension between capability and computational efficiency. A central contribution is the Unfireable Safety Kernel: an architecturally immutable safety boundary that cannot be disabled or circumvented by any system component, including its own self-improvement engine. This is not a social or ethical alignment statement; it is a technical framework ensuring human control persists as autonomy increases. Safety is an architectural constraint governing every operation, not a policy layer applied after the fact. We present formal alignment between ARYA's architecture and canonical world model requirements, and report summarizing its state-of-the-art performance across 6 of 9 competitive benchmarks head-to-head with GPT-5.2, Opus 4.6, and V-JEPA-2. All with zero neural network parameters, across seven active industry domain nodes spanning aerospace, pharma manufacturing, oil and gas, smart cities, biotech, defense, and medical devices.

---

## 3. WorldCache: Content-Aware Caching for Accelerated Video World Models

**Authors:** Umair Nawaz, Ahmed Heakl, Ufaq Khan, ..., Salman Khan, Fahad Shahbaz Khan
**arXiv:** [2603.22286](https://arxiv.org/abs/2603.22286)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)

Diffusion Transformers (DiTs) power high-fidelity video world models but remain computationally expensive due to sequential denoising and costly spatio-temporal attention. Training-free feature caching accelerates inference by reusing intermediate activations across denoising steps; however, existing methods largely rely on a Zero-Order Hold assumption i.e., reusing cached features as static snapshots when global drift is small. This often leads to ghosting artifacts, blur, and motion inconsistencies in dynamic scenes. We propose \textbf{WorldCache}, a Perception-Constrained Dynamical Caching framework that improves both when and how to reuse features. WorldCache introduces motion-adaptive thresholds, saliency-weighted drift estimation, optimal approximation via blending and warping, and phase-aware threshold scheduling across diffusion steps. Our cohesive approach enables adaptive, motion-consistent feature reuse without retraining. On Cosmos-Predict2.5-2B evaluated on PAI-Bench, WorldCache achieves \textbf{2.3$\times$} inference speedup while preserving \textbf{99.4\%} of baseline quality, substantially outperforming prior training-free caching approaches. Our code can be accessed on \href{this https URL}{World-Cache}.

---

## 4. ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

**Authors:** Haichao Zhang, Yijiang Li, Shwai He, ..., Ang Li, Yun Fu
**arXiv:** [2603.22281](https://arxiv.org/abs/2603.22281)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG); Robotics (cs.RO)

Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning over uniformly sampled frames, but they are not ideal as standalone dense predictors due to compute-driven sparse sampling, a language-output bottleneck that compresses fine-grained interaction states into text-oriented representations, and a data-regime mismatch when adapting to small action-conditioned datasets. We propose a VLM-guided JEPA-style latent world modeling framework that combines dense-frame dynamics modeling with long-horizon semantic guidance via a dual-temporal pathway: a dense JEPA branch for fine-grained motion and interaction cues, and a uniformly sampled VLM \emph{thinker} branch with a larger temporal stride for knowledge-rich guidance. To transfer the VLM's progressive reasoning signals effectively, we introduce a hierarchical pyramid representation extraction module that aggregates multi-layer VLM representations into guidance features compatible with latent prediction. Experiments on hand-manipulation trajectory prediction show that our method outperforms both a strong VLM-only baseline and a JEPA-predictor baseline, and yields more robust long-horizon rollout behavior.

---

## 5. What Do World Models Learn in RL? Probing Latent Representations in Learned Environment Simulators

**Authors:** Xinyu Zhang
**arXiv:** [2603.21546](https://arxiv.org/abs/2603.21546)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

World models learn to simulate environment dynamics from experience, enabling sample-efficient reinforcement learning. But what do these models actually represent internally? We apply interpretability techniques--including linear and nonlinear probing, causal interventions, and attention analysis--to two architecturally distinct world models: IRIS (discrete token transformer) and DIAMOND (continuous diffusion UNet), trained on Atari Breakout and Pong. Using linear probes, we find that both models develop linearly decodable representations of game state variables (object positions, scores), with MLP probes yielding only marginally higher R^2, confirming that these representations are approximately linear. Causal interventions--shifting hidden states along probe-derived directions--produce correlated changes in model predictions, providing evidence that representations are functionally used rather than merely correlated. Analysis of IRIS attention heads reveals spatial specialization: specific heads attend preferentially to tokens overlapping with game objects. Multi-baseline token ablation experiments consistently identify object-containing tokens as disproportionately important. Our findings provide interpretability evidence that learned world models develop structured, approximately linear internal representations of environment state across two games and two architectures.

---

## 6. FluidWorld: Reaction-Diffusion Dynamics as a Predictive Substrate for World Models

**Authors:** Fabien Polly
**arXiv:** [2603.21315](https://arxiv.org/abs/2603.21315)
**Categories:** Machine Learning (cs.LG)

World models learn to predict future states of an environment, enabling planning and mental simulation. Current approaches default to Transformer-based predictors operating in learned latent spaces. This comes at a cost: O(N^2) computation and no explicit spatial inductive bias. This paper asks a foundational question: is self-attention necessary for predictive world modeling, or can alternative computational substrates achieve comparable or superior results? I introduce FluidWorld, a proof-of-concept world model whose predictive dynamics are governed by partial differential equations (PDEs) of reaction-diffusion type. Instead of using a separate neural network predictor, the PDE integration itself produces the future state prediction. In a strictly parameter-matched three-way ablation on unconditional UCF-101 video prediction (64x64, ~800K parameters, identical encoder, decoder, losses, and data), FluidWorld is compared against both a Transformer baseline (self-attention) and a ConvLSTM baseline (convolutional recurrence). While all three models converge to comparable single-step prediction loss, FluidWorld achieves 2x lower reconstruction error, produces representations with 10-15% higher spatial structure preservation and 18-25% more effective dimensionality, and critically maintains coherent multi-step rollouts where both baselines degrade rapidly. All experiments were conducted on a single consumer-grade PC (Intel Core i5, NVIDIA RTX 4070 Ti), without any large-scale compute. These results establish that PDE-based dynamics, which natively provide O(N) spatial complexity, adaptive computation, and global spatial coherence through diffusion, are a viable and parameter-efficient alternative to both attention and convolutional recurrence for world modeling.

---

## 7. RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models

**Authors:** Zihao Zheng, Hangyu Cao, Jiayu Chen, ..., Guojie Luo, Xiang Chen
**arXiv:** [2603.20711](https://arxiv.org/abs/2603.20711)
**Categories:** Distributed, Parallel, and Cluster Computing (cs.DC); Machine Learning (cs.LG); Robotics (cs.RO)

Vision-Language-Action (VLA) models are mainstream in embodied intelligence but face high inference costs. Edge-Cloud Collaborative (ECC) deployment offers an effective fix by easing edge-device computing pressure to meet real-time needs. However, existing ECC frameworks are suboptimal for VLA models due to two challenges: (1) Diverse model structures hinder optimal ECC segmentation point identification; (2) Even if the optimal split point is determined, changes in network bandwidth can cause performance drift. To address these issues, we propose a novel ECC deployment framework for various VLA models, termed RoboECC. Specifically, we propose a model-hardware co-aware segmentation strategy to help find the optimal segmentation point for various VLA models. Moreover, we propose a network-aware deployment adjustment approach to adapt to the network fluctuations for maintaining optimal performance. Experiments demonstrate that RoboECC achieves a speedup of up to 3.28x with only 2.55x~2.62x overhead.

---

## 8. Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models

**Authors:** Zhilong Zhang, Haoxiang Ren, Yihao Sun, ..., Pierre-Luc Bacon, Yang Yu
**arXiv:** [2603.20607](https://arxiv.org/abs/2603.20607)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models show strong generalization for robotic control, but finetuning them with reinforcement learning (RL) is constrained by the high cost and safety risks of real-world interaction. Training VLA models in interactive world models avoids these issues but introduces several challenges, including pixel-level world modeling, multi-view consistency, and compounding errors under sparse rewards. Building on recent advances across large multimodal models and model-based RL, we propose VLA-MBPO, a practical framework to tackle these problems in VLA finetuning. Our approach has three key design choices: (i) adapting unified multimodal models (UMMs) for data-efficient world modeling; (ii) an interleaved view decoding mechanism to enforce multi-view consistency; and (iii) chunk-level branched rollout to mitigate error compounding. Theoretical analysis and experiments across simulation and real-world tasks demonstrate that VLA-MBPO significantly improves policy performance and sample efficiency, underscoring its robustness and scalability for real-world robotic deployment.

---

## 9. Do World Action Models Generalize Better than VLAs? A Robustness Study

**Authors:** Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, ..., Xingyue Quan, Yingxue Zhang
**arXiv:** [2603.22078](https://arxiv.org/abs/2603.22078)
**Categories:** Robotics (cs.RO)

Robot action planning in the real world is challenging as it requires not only understanding the current state of the environment but also predicting how it will evolve in response to actions. Vision-language-action (VLA), which repurpose large-scale vision-language models for robot action generation using action experts, have achieved notable success across a variety of robotic tasks. Nevertheless, their performance remains constrained by the scope of their training data, exhibiting limited generalization to unseen scenarios and vulnerability to diverse contextual perturbations. More recently, world models have been revisited as an alternative to VLAs. These models, referred to as world action models (WAMs), are built upon world models that are trained on large corpora of video data to predict future states. With minor adaptations, their latent representation can be decoded into robot actions. It has been suggested that their explicit dynamic prediction capacity, combined with spatiotemporal priors acquired from web-scale video pretraining, enables WAMs to generalize more effectively than VLAs. In this paper, we conduct a comparative study of prominent state-of-the-art VLA policies and recently released WAMs. We evaluate their performance on the LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and language perturbations. Our results show that WAMs achieve strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus. While VLAs such as $\pi_{0.5}$ can achieve comparable robustness on certain tasks, they typically require extensive training with diverse robotic datasets and varied learning objectives. Hybrid approaches that partially incorporate video-based dynamic learning exhibit intermediate robustness, highlighting the importance of how video priors are integrated.

---

## 10. VP-VLA: Visual Prompting as an Interface for Vision-Language-Action Models

**Authors:** Zixuan Wang, Yuxin Chen, Yuqi Liu, ..., Shu Liu, Jiaya Jia
**arXiv:** [2603.22003](https://arxiv.org/abs/2603.22003)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models typically map visual observations and linguistic instructions directly to robotic control signals. This "black-box" mapping forces a single forward pass to simultaneously handle instruction interpretation, spatial grounding, and low-level control, often leading to poor spatial precision and limited robustness in out-of-distribution scenarios. To address these limitations, we propose VP-VLA, a dual-system framework that decouples high-level reasoning and low-level execution via a structured visual prompting interface. Specifically, a "System 2 Planner" decomposes complex instructions into sub-tasks and identifies relevant target objects and goal locations. These spatial anchors are then overlaid directly onto visual observations as structured visual prompts, such as crosshairs and bounding boxes. Guided by these prompts and enhanced by a novel auxiliary visual grounding objective during training, a "System 1 Controller" reliably generates precise low-level execution motions. Experiments on the Robocasa-GR1-Tabletop benchmark and SimplerEnv simulation demonstrate that VP-VLA improves success rates by 5% and 8.3%, surpassing competitive baselines including QwenOFT and GR00T-N1.6.

---

## 11. CounterScene: Counterfactual Causal Reasoning in Generative World Models for Safety-Critical Closed-Loop Evaluation

**Authors:** Bowen Jing, Ruiyang Hao, Weitao Zhou, Haibao Yu
**arXiv:** [2603.21104](https://arxiv.org/abs/2603.21104)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Generating safety-critical driving scenarios requires understanding why dangerous interactions arise, rather than merely forcing collisions. However, existing methods rely on heuristic adversarial agent selection and unstructured perturbations, lacking explicit modeling of interaction dependencies and thus exhibiting a realism--adversarial trade-off. We present CounterScene, a framework that endows closed-loop generative BEV world models with structured counterfactual reasoning for safety-critical scenario generation. Given a safe scene, CounterScene asks: what if the causally critical agent had behaved differently? To answer this, we introduce causal adversarial agent identification to identify the critical agent and classify conflict types, and develop a conflict-aware interactive world model in which a causal interaction graph is used to explicitly model dynamic inter-agent dependencies. Building on this structure, stage-adaptive counterfactual guidance performs minimal interventions on the identified agent, removing its spatial and temporal safety margins while allowing risk to emerge through natural interaction propagation. Extensive experiments on nuScenes demonstrate that CounterScene achieves the strongest adversarial effectiveness while maintaining superior trajectory realism across all horizons, improving long-horizon collision rate from 12.3% to 22.7% over the strongest baseline with better realism (ADE 1.88 vs.2.09). Notably, this advantage further widens over longer rollouts, and CounterScene generalizes zero-shot to nuPlan with state-of-the-art realism.

---

## 12. Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness

**Authors:** Ziou Hu, Xiangtong Yao, Yuan Meng, Zhenshan Bing, Alois Knoll
**arXiv:** [2603.21017](https://arxiv.org/abs/2603.21017)
**Categories:** Robotics (cs.RO)

Diffusion policies excel at visuomotor control but often fail catastrophically under severe out-of-distribution (OOD) disturbances, such as unexpected object displacements or visual corruptions. To address this vulnerability, we introduce the Dream Diffusion Policy (DDP), a framework that deeply integrates a diffusion world model into the policy's training objective via a shared 3D visual encoder. This co-optimization endows the policy with robust state-prediction capabilities. When encountering sudden OOD anomalies during inference, DDP detects the real-imagination discrepancy and actively abandons the corrupted visual stream. Instead, it relies on its internal "imagination" (autoregressively forecasted latent dynamics) to safely bypass the disruption, generating imagined trajectories before smoothly realigning with physical reality. Extensive evaluations demonstrate DDP's exceptional resilience. Notably, DDP achieves a 73.8% OOD success rate on MetaWorld (vs. 23.9% without predictive imagination) and an 83.3% success rate under severe real-world spatial shifts (vs. 3.3% without predictive imagination). Furthermore, as a stress test, DDP maintains a 76.7% real-world success rate even when relying entirely on open-loop imagination post-initialization.

---

## 13. ROI-Driven Foveated Attention for Unified Egocentric Representations in Vision-Language-Action Systems

**Authors:** Xinhai Sun, Xiang Shi, Menglin Zou, Wenlong Huang
**arXiv:** [2603.20668](https://arxiv.org/abs/2603.20668)
**Categories:** Robotics (cs.RO)

The development of embodied AI systems is increasingly constrained by the availability and structure of physical interaction data. Despite recent advances in vision-language-action (VLA) models, current pipelines suffer from high data collection cost, limited cross-embodiment alignment, and poor transfer from internet-scale visual data to robot control.
We propose a region-of-interest (ROI) driven engineering workflow that introduces an egocentric, geometry-grounded data representation. By projecting end-effector poses via forward kinematics (FK) into a single external camera, we derive movement-aligned hand-centric ROIs without requiring wrist-mounted cameras or multi-view systems. Unlike directly downsampling the full frame, ROI is cropped from the original image before resizing, preserving high local information density for contact-critical regions while retaining global context.
We present a reproducible pipeline covering calibration, synchronization, ROI generation, deterministic boundary handling, and metadata governance. The resulting representation is embodiment-aligned and viewpoint-normalized, enabling data reuse across heterogeneous robots. We argue that egocentric ROI serves as a practical data abstraction for scalable collection and cross-embodiment learning, bridging internet-scale perception and robot-specific control.

---

## 14. StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models

**Authors:** Kartikay Milind Pangaonkar, Prabin Rath, Omkar Patil, Nakul Gopalan
**arXiv:** [2603.20659](https://arxiv.org/abs/2603.20659)
**Categories:** Robotics (cs.RO)

Large scale pre-training on text and image data along with diverse robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes. However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors and physical obstructions in the robot's workspace. Existing policy improvement methods finetune base VLAs to improve generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy performance by manipulating the environment's initial state using VLM-based in-context reasoning. StageCraft takes policy rollout videos and success labels as input and leverages VLM's reasoning ability to infer which objects in the initial state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work. We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and improves its performance with more in-context samples. Videos of StageCraft in effect can be found at this https URL .

---

## 15. DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models

**Authors:** Zhide Zhong, Junfeng Li, Junjie He, ..., Liuqing Yang, Haoang Li
**arXiv:** [2603.22280](https://arxiv.org/abs/2603.22280)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision-Language-Action (VLA) models map visual observations and language instructions directly to robotic actions. While effective for simple tasks, standard VLA models often struggle with complex, multi-step tasks requiring logical planning, as well as precise manipulations demanding fine-grained spatial perception. Recent efforts have incorporated Chain-of-Thought (CoT) reasoning to endow VLA models with a ``thinking before acting'' capability. However, current CoT-based VLA models face two critical limitations: 1) an inability to simultaneously capture low-level visual details and high-level logical planning due to their reliance on isolated, single-modal CoT; 2) high inference latency with compounding errors caused by step-by-step autoregressive decoding. To address these limitations, we propose DualCoT-VLA, a visual-linguistic CoT method for VLA models with a parallel reasoning mechanism. To achieve comprehensive multi-modal reasoning, our method integrates a visual CoT for low-level spatial understanding and a linguistic CoT for high-level task planning. Furthermore, to overcome the latency bottleneck, we introduce a parallel CoT mechanism that incorporates two sets of learnable query tokens, shifting autoregressive reasoning to single-step forward reasoning. Extensive experiments demonstrate that our DualCoT-VLA achieves state-of-the-art performance on the LIBERO and RoboCasa GR1 benchmarks, as well as in real-world platforms.

---

## 16. Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models

**Authors:** Meiqi Wu, Zhixin Cai, Fufangchen Zhao, ..., Zeming Liu, Kaiqi Huang
**arXiv:** [2603.22212](https://arxiv.org/abs/2603.22212)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Video--based world models have emerged along two dominant paradigms: video generation and 3D reconstruction. However, existing evaluation benchmarks either focus narrowly on visual fidelity and text--video alignment for generative models, or rely on static 3D reconstruction metrics that fundamentally neglect temporal dynamics. We argue that the future of world modeling lies in 4D generation, which jointly models spatial structure and temporal evolution. In this paradigm, the core capability is interactive response: the ability to faithfully reflect how interaction actions drive state transitions across space and time. Yet no existing benchmark systematically evaluates this critical dimension. To address this gap, we propose Omni--WorldBench, a comprehensive benchmark specifically designed to evaluate the interactive response capabilities of world models in 4D settings. Omni--WorldBench comprises two key components: Omni--WorldSuite, a systematic prompt suite spanning diverse interaction levels and scene types; and Omni--Metrics, an agent-based evaluation framework that quantifies world modeling capabilities by measuring the causal impact of interaction actions on both final outcomes and intermediate state evolution trajectories. We conduct extensive evaluations of 18 representative world models across multiple paradigms. Our analysis reveals critical limitations of current world models in interactive response, providing actionable insights for future research. Omni-WorldBench will be publicly released to foster progress in interactive 4D world modeling.

---

## 17. From Part to Whole: 3D Generative World Model with an Adaptive Structural Hierarchy

**Authors:** Bi'an Du, Daizong Liu, Pufan Li, Wei Hu
**arXiv:** [2603.21557](https://arxiv.org/abs/2603.21557)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Single-image 3D generation lies at the core of vision-to-graphics models in the real world. However, it remains a fundamental challenge to achieve reliable generalization across diverse semantic categories and highly variable structural complexity under sparse supervision. Existing approaches typically model objects in a monolithic manner or rely on a fixed number of parts, including recent part-aware models such as PartCrafter, which still require a labor-intensive user-specified part count. Such designs easily lead to overfitting, fragmented or missing structural components, and limited compositional generalization when encountering novel object layouts. To this end, this paper rethinks single-image 3D generation as learning an adaptive part-whole hierarchy in the flexible 3D latent space. We present a novel part-to-whole 3D generative world model that autonomously discovers latent structural slots by inferring soft and compositional masks directly from image tokens. Specifically, an adaptive slot-gating mechanism dynamically determines the slot-wise activation probabilities and smoothly consolidates redundant slots within different objects, ensuring that the emergent structure remains compact yet expressive across categories. Each distilled slot is then aligned to a learnable, class-agnostic prototype bank, enabling powerful cross-category shape sharing and denoising through universal geometric prototypes in the real world. Furthermore, a lightweight 3D denoiser is introduced to reconstruct geometry and appearance via unified diffusion objectives. Experiments show consistent gains in cross-category transfer and part-count extrapolation, and ablations confirm complementary benefits of the prototype bank for shape-prior sharing as well as slot-gating for structural adaptation.

---

## 18. Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations

**Authors:** Liu hung ming
**arXiv:** [2603.20327](https://arxiv.org/abs/2603.20327)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Video world models trained with Joint Embedding Predictive Architectures (JEPA) acquire rich spatiotemporal representations by predicting masked regions in latent space rather than reconstructing pixels. This removes the visual verification pathway of generative models, creating a structural interpretability gap: the encoder has learned physical structure inaccessible in any inspectable form. Existing probing methods either operate in continuous space without a structured intermediate layer, or attach generative components whose parameters confound attribution of behavior to the encoder.
We propose the AI Mother Tongue (AIM) framework as a passive quantization probe: a lightweight, vocabulary-free probe that converts V-JEPA 2 continuous latent vectors into discrete symbol sequences without task-specific supervision or modifying the encoder. Because the encoder is kept completely frozen, any symbolic structure in the AIM codebook is attributable entirely to V-JEPA 2 pre-trained representations -- not to the probe.
We evaluate through category-contrast experiments on Kinetics-mini along three physical dimensions: grasp angle, object geometry, and motion temporal structure. AIM symbol distributions differ significantly across all three experiments (chi^2 p < 10^{-4}; MI 0.036--0.117 bits, NMI 1.2--3.9% of the 3-bit maximum; JSD up to 0.342; codebook active ratio 62.5%). The experiments reveal that V-JEPA 2 latent space is markedly compact: diverse action categories share a common representational core, with semantic differences encoded as graded distributional variations rather than categorical boundaries. These results establish Stage 1 of a four-stage roadmap toward an action-conditioned symbolic world model, demonstrating that structured symbolic manifolds are discoverable properties of frozen JEPA latent spaces.

---

## 19. Understanding Behavior Cloning with Action Quantization

**Authors:** Haoqun Cao, Tengyang Xie
**arXiv:** [2603.20538](https://arxiv.org/abs/2603.20538)
**Categories:** Machine Learning (cs.LG); Machine Learning (stat.ML)

Behavior cloning is a fundamental paradigm in machine learning, enabling policy learning from expert demonstrations across robotics, autonomous driving, and generative models. Autoregressive models like transformer have proven remarkably effective, from large language models (LLMs) to vision-language-action systems (VLAs). However, applying autoregressive models to continuous control requires discretizing actions through quantization, a practice widely adopted yet poorly understood theoretically. This paper provides theoretical foundations for this practice. We analyze how quantization error propagates along the horizon and interacts with statistical sample complexity. We show that behavior cloning with quantized actions and log-loss achieves optimal sample complexity, matching existing lower bounds, and incurs only polynomial horizon dependence on quantization error, provided the dynamics are stable and the policy satisfies a probabilistic smoothness condition. We further characterize when different quantization schemes satisfy or violate these requirements, and propose a model-based augmentation that provably improves the error bound without requiring policy smoothness. Finally, we establish fundamental limits that jointly capture the effects of quantization error and statistical complexity.

---

## 20. UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos

**Authors:** Gu Zhang, Qicheng Xu, Haozhe Zhang, ..., Hang Zhao, Huazhe Xu
**arXiv:** [2603.22264](https://arxiv.org/abs/2603.22264)
**Categories:** Robotics (cs.RO)

Dexterous manipulation remains challenging due to the cost of collecting real-robot teleoperation data, the heterogeneity of hand embodiments, and the high dimensionality of control. We present UniDex, a robot foundation suite that couples a large-scale robot-centric dataset with a unified vision-language-action (VLA) policy and a practical human-data capture setup for universal dexterous hand control. First, we construct UniDex-Dataset, a robot-centric dataset over 50K trajectories across eight dexterous hands (6--24 DoFs), derived from egocentric human video datasets. To transform human data into robot-executable trajectories, we employ a human-in-the-loop retargeting procedure to align fingertip trajectories while preserving plausible hand-object contacts, and we operate on explicit 3D pointclouds with human hands masked to narrow kinematic and visual gaps. Second, we introduce the Function-Actuator-Aligned Space (FAAS), a unified action space that maps functionally similar actuators to shared coordinates, enabling cross-hand transfer. Leveraging FAAS as the action parameterization, we train UniDex-VLA, a 3D VLA policy pretrained on UniDex-Dataset and finetuned with task demonstrations. In addition, we build UniDex-Cap, a simple portable capture setup that records synchronized RGB-D streams and human hand poses and converts them into robot-executable trajectories to enable human-robot data co-training that reduces reliance on costly robot demonstrations. On challenging tool-use tasks across two different hands, UniDex-VLA achieves 81% average task progress and outperforms prior VLA baselines by a large margin, while exhibiting strong spatial, object, and zero-shot cross-hand generalization. Together, UniDex-Dataset, UniDex-VLA, and UniDex-Cap provide a scalable foundation suite for universal dexterous manipulation.

---

## 21. ROBOGATE: Adaptive Failure Discovery for Safe Robot Policy Deployment via Two-Stage Boundary-Focused Sampling

**Authors:** Byungjin Kim
**arXiv:** [2603.22126](https://arxiv.org/abs/2603.22126)
**Categories:** Robotics (cs.RO)

Deploying learned robot manipulation policies in industrial settings requires rigorous pre-deployment validation, yet exhaustive testing across high-dimensional parameter spaces is intractable. We present ROBOGATE, a deployment risk management framework that combines physics-based simulation with a two-stage adaptive sampling strategy to efficiently discover failure boundaries in the operational parameter space. Stage 1 employs Latin Hypercube Sampling (LHS) across an 8-dimensional parameter space to establish a coarse failure landscape from 20,000 uniformly distributed experiments. Stage 2 applies boundary-focused sampling that concentrates 10,000 additional experiments in the 30-70% success rate transition zone, enabling precise failure boundary mapping. Using NVIDIA Isaac Sim with Newton physics, we evaluate a scripted pick-and-place controller on two robot embodiments -- Franka Panda (7-DOF) and UR5e (6-DOF) -- across 30,000 total experiments. Our logistic regression risk model achieves an AUC of 0.780 on the combined dataset (vs. 0.754 for Stage 1 alone), identifies a closed-form failure boundary equation, and reveals four universal danger zones affecting both robot platforms. We further demonstrate the framework on VLA (Vision-Language-Action) model evaluation, where Octo-Small achieves 0.0% success rate on 68 adversarial scenarios versus 100% for the scripted baseline -- a 100-point gap that underscores the challenge of deploying foundation models in industrial settings. ROBOGATE is open-source and runs on a single GPU workstation.

---

## 22. Speedup Patch: Learning a Plug-and-Play Policy to Accelerate Embodied Manipulation

**Authors:** Zhichao Wu, Junyin Ye, Zhilong Zhang, ..., Lei Yuan, Yang Yu
**arXiv:** [2603.20658](https://arxiv.org/abs/2603.20658)
**Categories:** Robotics (cs.RO)

While current embodied policies exhibit remarkable manipulation skills, their execution remains unsatisfactorily slow as they inherit the tardy pacing of human demonstrations. Existing acceleration methods typically require policy retraining or costly online interactions, limiting their scalability for large-scale foundation models. In this paper, we propose Speedup Patch (SuP), a lightweight, policy-agnostic framework that enables plug-and-play acceleration using solely offline data. SuP introduces an external scheduler that adaptively downsamples action chunks provided by embodied policies to eliminate redundancies. Specifically, we formalize the optimization of our scheduler as a Constrained Markov Decision Process (CMDP) aimed at maximizing efficiency without compromising task performance. Since direct success evaluation is infeasible in offline settings, SuP introduces World Model based state deviation as a surrogate metric to enforce safety constraints. By leveraging a learned world model as a virtual evaluator to predict counterfactual trajectories, the scheduler can be optimized via offline reinforcement learning. Empirical results on simulation benchmarks (Libero, Bigym) and real-world tasks validate that SuP achieves an overall 1.8x execution speedup for diverse policies while maintaining their original success rates.

---
