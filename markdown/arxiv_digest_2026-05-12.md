# arXiv Daily Digest — 2026-05-12

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 42

---

## 1. How Mobile World Model Guides GUI Agents?

**Authors:** Weikai Xu, Kun Huang, Yunren Feng, ..., Xiaolin Hu, Bo An
**arXiv:** [2605.10347](https://arxiv.org/abs/2605.10347)
**Categories:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

Recent advances in vision-language models have enabled mobile GUI agents to perceive visual interfaces and execute user instructions, but reliable prediction of action consequences remains critical for long-horizon and high-risk interactions. Existing mobile world models provide either text-based or image-based future states, yet it remains unclear which representation is useful, whether generated rollouts can replace real environments, and how test-time guidance helps agents of different strengths. To answer the above questions, we filter and annotate mobile world-model data, then train world models across four modalities: delta text, full text, diffusion-based images, and renderable code. These models achieve SoTA performance on both MobileWorldBench and Code2WorldBench. Furthermore, by evaluating their downstream utility on AITZ, AndroidControl, and AndroidWorld, we obtain three findings. First, renderable code reconstruction achieves high in-distribution fidelity and provides effective multimodal supervision for data construction, while text-based feedback is more robust for online out-of-distribution (OOD) execution. Second, world-model-generated trajectories can provide transferable interaction experience in the training process and improve agents' end-to-end task performance, although these data do not preserve the original distribution. Last, for overconfident mobile agents with low action entropy, posterior self-reflection provides limited gains, suggesting that world models are more effective as prior perception or training supervision than as universal post-hoc verifiers.

---

## 2. LoopVLA: Learning Sufficiency in Recurrent Refinement for Vision-Language-Action Models

**Authors:** Boyang Shen, Kaixiang Yang, Hao Wang, ..., Qiang Li, Zhiwei Wang
**arXiv:** [2605.09948](https://arxiv.org/abs/2605.09948)
**Categories:** Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Current Vision-Language-Action (VLA) models typically treat the deepest representation of a vision-language backbone as universally optimal for action prediction. However, robotic manipulation is composed of many frequent closed-loop spatial adjustments, for which excessive abstraction may waste computation and weaken low-level geometric cues essential for precise control. Existing early-exit strategies attempt to reduce computation by stopping at predefined layers or applying heuristic rules such as action consistency, but they do not directly answer when a representation is actually sufficient for action. In this paper, we present LoopVLA, a recurrent VLA architecture that jointly learns representation refinement, action prediction, and sufficiency estimation. LoopVLA iteratively applies a shared Transformer block to refine multimodal tokens, and at each iteration produces both a candidate action and a sufficiency score that estimates whether further refinement is necessary. By sharing parameters across iterations, LoopVLA decouples refinement from absolute layer indices and grounds sufficiency estimation in the evolving representation itself. Since sufficiency has no direct supervision, we introduce a self-supervised distribution alignment objective, where intermediate confidence scores are trained to match the relative action quality across refinement steps, thereby linking sufficiency learning to policy optimization signals. Experiments on LIBERO, LIBERO-Plus, and VLA-Arena show that LoopVLA pushes the efficiency-performance frontier of VLA policies, reducing parameters by 45% and improving inference throughput by up to 1.7 times while matching or outperforming strong baselines in task success.

---

## 3. SKG-VLA: Scene Knowledge Graph Priors for Structured Scene Semantics and Multimodal Reasoning for Decision Making

**Authors:** Zeyu Li, Lei Li
**arXiv:** [2605.09343](https://arxiv.org/abs/2605.09343)
**Categories:** Artificial Intelligence (cs.AI)

Decision making in large-scale complaint handling systems increasingly relies on heterogeneous evidence, including complaint narratives, screenshots, order metadata, historical interactions, and platform policies. Existing complaint understanding systems mainly perform shallow classification or template matching over isolated modalities, while underutilizing explicit scene structure, rule knowledge, and cross-evidence dependencies. To address this limitation, we present SKG-VLA for multimodal complaint decision making. The core idea is to model each case as a structured complaint scene and represent its decision-relevant semantics with a \emph{Scene Knowledge Graph} (SKG), which organizes complaint entities, evidence items, policy clauses, temporal events, transactional states, and action-relevant relations into a unified graph. Based on SKG, we build a data synthesis pipeline that generates complaint scene descriptions, rule-consistent graph generalizations, question-answer supervision, and decision recommendations. We further construct a large-scale complaint scene dataset with both text-only and multimodal in-domain benchmarks. Finally, we adopt a three-stage training strategy -- domain-adaptive pre-training, task-oriented instruction fine-tuning, and end-to-end multimodal alignment -- to inject structured scene priors into a multimodal decision model. Experiments show that SKG-VLA consistently improves policy-grounded reasoning, complaint decision accuracy, long-tail generalization, and robustness under incomplete evidence.

---

## 4. MCP-Cosmos: World Model-Augmented Agents for Complex Task Execution in MCP Environments

**Authors:** Giridhar Ganapavarapu, Dhaval Patel
**arXiv:** [2605.09131](https://arxiv.org/abs/2605.09131)
**Categories:** Artificial Intelligence (cs.AI); Multiagent Systems (cs.MA)

The Model Context Protocol (MCP) has unified the interface between Large Language Models (LLMs) and external tools, yet a fundamental gap remains in how agents conceptualize the environments within which they operate. Current paradigms are bifurcated: Task-level planning often ignores execution-time dynamics, while reactive execution lacks long-horizon foresight. We present MCP-Cosmos, a framework that infuses generative World Models (WM) into the MCP ecosystem to enable predictive task automation. By unifying three disparate technologies, namely MCP, World Model, and Agent, we demonstrate that a "Bring Your Own World Model" (BYOWM) strategy allows agents to simulate state transitions and refine plans in a latent space before execution. We conducted experiments using two strategies, namely ReAct and SPIRAL with 2 planning models and 3 representative world models over 20+ MCP-Bench tasks. We observed improvements in Agent's environment interaction KPI such as tool success rate and tool parameter accuracy. The framework also offers new metrics such as Execution Quality to generate new insights about the effectiveness of world models compared to baseline.

---

## 5. ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models

**Authors:** Zuojin Tang, Haoyun Liu, Xinyuan Chang, ..., Zhiheng Ma, Gang Pan
**arXiv:** [2605.10819](https://arxiv.org/abs/2605.10819)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

Vision-language-action (VLA) models remain constrained by the scarcity of action-labeled robot data, whereas action-free videos provide abundant evidence of how the physical world changes. Latent action models offer a promising way to extract such priors from videos, but reconstruction-trained latent codes are not necessarily suitable for policy generation: they may predict future observations while lacking the structure needed to be reused or generated coherently with robot actions. We introduce ALAM (Algebraic Latent Action Model), an Algebraically Consistent Latent Action Model that turns temporal relations in action-free video into structural supervision. Given frame triplets, ALAM learns latent transitions that are grounded by reconstruction while being regularized by composition and reversal consistency, encouraging a locally additive transition space. For downstream VLA learning, we freeze the pretrained encoder and use its latent transition sequences as auxiliary generative targets, co-generated with robot actions under a joint flow-matching objective. This couples structured latent transitions with flow-based policy generation, allowing the policy to exploit ALAM's locally consistent transition geometry without requiring latent-to-action decoding. Representation probes show that ALAM reduces additivity and reversibility errors by 25-85 times over unstructured latent-action baselines and improves long-horizon cumulative reconstruction. When transferred to VLA policies, ALAM raises the average success rate from 47.9% to 85.0% on MetaWorld MT50 and from 94.1% to 98.1% on LIBERO, with consistent gains on real-world manipulation tasks. Ablations further confirm that the strongest improvements arise from the synergy between algebraically structured latent transitions and joint flow matching.

---

## 6. PhyGround: Benchmarking Physical Reasoning in Generative World Models

**Authors:** Juyi Lin, Arash Akbari, Yumei He, ..., Pu Zhao, Yanzhi Wang
**arXiv:** [2605.10806](https://arxiv.org/abs/2605.10806)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Generative world models are increasingly used for video generation, where learned simulators are expected to capture the physical rules that govern real-world dynamics. However, evaluating whether generated videos actually follow these rules remains challenging. Existing physics-focused video benchmarks have made important progress, but they still face three key challenges, including the coarse evaluation frameworks that hide law-specific failures, response biases and fatigue that undermine the validity of annotation judgments, and automated evaluators that are insufficiently physics-aware or difficult to audit. To address those challenges, we introduce PhyGround, a criteria-grounded benchmark for evaluating physical reasoning in video generation. The benchmark contains 250 curated prompts, each augmented with an expected physical outcome, and a taxonomy of 13 physical laws across solid-body mechanics, fluid dynamics, and optics. Each law is operationalized through observable sub-questions to enable per-law diagnostics. We evaluate eight modern video generation models through a large-scale, quality-controlled human study, grounded on social science lab experiment design. A total of 459 annotators provided 5,796 complete annotations and over 37.4K fine-grained labels; after quality control, the retained annotations exhibited high split-half model-ranking correlations (Spearman's rho > 0.90). To support reproducible automated evaluation, we release PhyJudge-9B, an open physics-specialized VLM judge. PhyJudge-9B achieves substantially lower aggregate relative bias than Gemini-3.1-Pro (3.3% vs. 16.6%). We release prompts, human annotations, model checkpoints, and evaluation code on the project page this https URL.

---

## 7. CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving

**Authors:** Minqing Huang, Yujiao Xiang, Zihan Liang, ..., Mu Yang, Gong Che
**arXiv:** [2605.10426](https://arxiv.org/abs/2605.10426)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving. However, existing reasoning mechanisms still struggle to provide planning-oriented intermediate representations: textual Chain-of-Thought (CoT) fails to preserve continuous spatiotemporal structure, while latent world reasoning remains difficult to use as a direct condition for action generation. In this paper, we propose CoWorld-VLA, a multi-expert world reasoning framework for autonomous driving, where world representations serve as explicit conditions to guide action planning. CoWorld-VLA extracts complementary world information through multi-source supervision and encodes it into expert tokens within the VLA, thereby providing planner-accessible conditioning signals. Specifically, we construct four types of tokens: semantic interaction, geometric structure, dynamic evolution, and ego trajectory tokens, which respectively model interaction intent, spatial structure, future temporal dynamics, and behavioral goals. During action generation, CoWorld-VLA employs a diffusion-based hierarchical multi-expert fusion planner, which is coupled with scene context throughout the joint denoising process to generate continuous ego trajectories. Experiments show that CoWorld-VLA achieves competitive results in both future scene generation and planning on the NAVSIM v1 benchmark, demonstrating strong performance in collision avoidance and trajectory accuracy. Ablation studies further validate the complementarity of expert tokens and their effectiveness as planning conditions for action generation. Code will be available at this https URL.

---

## 8. Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs

**Authors:** Jianchao Zhao, Huoren Yang, Yusong Hu, ..., Zhiheng Ma, Yihong Gong
**arXiv:** [2605.10094](https://arxiv.org/abs/2605.10094)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models show strong potential for general-purpose robotic manipulation, yet their closed-loop reliability often degrades under local deployment conditions. Existing evaluations typically treat test episodes as independent zero-shot trials. However, real robots often operate repeatedly in the same or slowly changing environments, where successful executions provide environment-verified evidence of reliable behavior patterns. We study this persistent-deployment setting, asking whether a partially competent frozen VLA can improve its reliability by reusing its successful test-time experience. We propose an online success-memory guided test-time adaptation framework for generative VLAs. During deployment, the robot stores progress-calibrated successful observation-action segments in a long-term memory. At inference, it retrieves state-relevant action chunks, filters inconsistent candidates via trajectory-level consistency, and aggregates them into an elite action prior. To incorporate this prior into action generation, we introduce confidence-adaptive prior guidance, which injects the elite prior into an intermediate state of the flow-matching action sampler and adjusts the guidance strength based on retrieval confidence. This design allows the frozen VLA to exploit environment-specific successful experience while preserving observation-conditioned generative refinement. This retrieve-then-steer mechanism enables lightweight, non-parametric test-time adaptation without requiring parameter updates. Simulation and real-world experiments show improved task success and closed-loop stability, especially in long-horizon and multi-stage tasks.

---

## 9. RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models

**Authors:** Weijia Liufu, Xiaoyu Guo, Ruiyi Chen, ..., Liang Lin, Xiaodan Liang
**arXiv:** [2605.09410](https://arxiv.org/abs/2605.09410)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models remain brittle in long-horizon, contact-rich manipulation because success-only imitation provides little supervision for execution drift, while failed rollouts are often discarded. We introduce RePO-VLA, a recovery-driven policy optimization framework that assigns distinct roles to success, recovery, and failure trajectories. RePO-VLA first applies Recovery-Aware Initialization (RAI), slicing recovery segments and resetting history so corrective actions depend on the current adverse state rather than the preceding failure. It then learns a Progress-Aware Semantic Value Function (PAS-VF), aligning spatiotemporal trajectory features with instructions and successful references. The resulting labels salvage useful failure prefixes via reliability decay, while low-value labels mark drift and terminal breakdowns, teaching differences among nominal, failed, and corrective actions. The data engine turns adverse states into planner-generated or human-collected corrective rollouts, teaching recovery to the success manifold. Value-Conditioned Refinement (VCR) trains the policy to prefer high-progress actions. At deployment, a fixed high value ($v=1.0$) biases actions toward the learned success manifold without online failure detectors or heuristic retries. We introduce FRBench, with standardized error injection and recovery-focused evaluation. Across simulated and real-world bimanual tasks, RePO-VLA improves robustness, raising adversarial success from 20% to 75% on average and up to 80% in scaled real-world trials.

---

## 10. Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models

**Authors:** Kai Zhao, Dongliang Nie, Yuchen Lin, ..., Deng-Ping Fan, Dan Zeng
**arXiv:** [2605.09241](https://arxiv.org/abs/2605.09241)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent this http URL, JEPA training is subject to a bias-variance this http URL sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial this http URL recent LeWorldModel (LeWM) shows that this issue can be alleviated bysimply constraining latent embeddings with an isotropic Gaussian this http URL, latent representations inherently lie on low-dimensional manifoldswithin a high-dimensional ambient space, and enforcing an isotropic Gaussianprior directly in this ambient space introduces an overly strong this http URL this work, we propose ame, which seeks a favorable operatingpoint on the bias-variance frontier by applying Gaussian constraints inmultiple random subspaces rather than in the originalembedding this http URL design relaxes the global constraint while preserving itsanti-collapse effect, leading to a better balance between trainingstability and representation this http URL experiments across fourcontinuous-control environments demonstrate that consistentlyoutperforms LeWM with very clear this http URL method is simple yet effective, and serves as a strong baseline for future JEPA-based world model this http URL code is available at this https URL.

---

## 11. Towards Backdoor-Based Ownership Verification for Vision-Language-Action Models

**Authors:** Ming Sun, Rui Wang, Xingrui Yu, ..., Xu Pan, Ivor Tsang
**arXiv:** [2605.09005](https://arxiv.org/abs/2605.09005)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action models (VLAs) support generalist robotic control by enabling end-to-end decision policies directly from multi-modal inputs. As trained VLAs are increasingly shared and adapted, protecting model ownership becomes essential for secure deployment and responsible open-source usage. In this paper, we present GuardVLA, the first backdoor-based ownership verification framework specifically designed for VLAs. GuardVLA embeds a stealthy and harmless backdoor watermark into the protected model during training by injecting secret messages into embodied visual data. For post-release verification, we propose a swap-and-detect mechanism, in which the trigger projector and an external classifier head are used to activate and detect the embedded backdoor based on prediction probabilities. Extensive experiments across multiple datasets, model architectures, and adaptation settings demonstrate that GuardVLA enables reliable ownership verification while preserving benign task performance. Further results show that the embedded watermark remains detectable under post-release model adaptation.

---

## 12. MolWorld: Molecule World Models for Actionable Molecular Optimization

**Authors:** Yang Qiao, Bo Pan, Hao-Wei Pang, ..., Liying Zhang, Liang Zhao
**arXiv:** [2605.08954](https://arxiv.org/abs/2605.08954)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Molecular optimization in drug discovery aims to discover molecules with improved target properties, but practical lead optimization often requires more than high predicted scores. A useful candidate should also be actionable: it should be reachable from known molecules through valid local structural transformations, so that it can be interpreted as a plausible revision within an evolving chemical series. Existing de novo and single-molecule optimization methods do not explicitly model such reachability, especially when both the target molecules and the intermediate molecules connecting them to known compounds are unknown. In this work, we formulate actionable molecular optimization as sequential expansion of a molecule-transfer graph, where nodes are molecules and edges encode valid local transformations. We propose MolWorld, a molecule world model-guided framework that treats the current molecule-transfer graph as an evolving search state. At each iteration, MolWorld selects local anchor contexts, generates candidate molecules conditioned on these contexts, evaluates their properties, and uses a learned world model to update the evolving molecule world by retaining admissible candidates and inserting them into the molecule-transfer graph. The expanded molecule world then guides subsequent optimization. Experiments on property optimization and docking-based tasks show that MolWorld discovers high-property molecules while maintaining substantially stronger structural connectivity, supporting actionable and sequential molecular design.

---

## 13. Probing the Impact of Scale on Data-Efficient, Generalist Transformer World Models for Atari

**Authors:** Jooyeon Kim
**arXiv:** [2605.08578](https://arxiv.org/abs/2605.08578)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Developing generalist systems that retain human-like data efficiency is a central challenge. While world models (WMs) offer a promising path, existing research often conflates architectural mechanisms with the independent impact of model \emph{scale}. In this work, we use a minimalist transformer world model to analyze scaling behaviors on the Atari 100k benchmark, using fixed offline datasets derived from a presupposed expert policy. Our results reveal that environments fundamentally fall into distinct scaling regimes, even when constrained by identical offline data budgets and model capacities. For individual tasks, some environments naturally allow models to pass the interpolation threshold, yielding monotonic improvements in the overparameterized regime, while others remain trapped in the classical regime, where larger world models degrade fidelity. In the unified setting, i.e., a single transformer trained on a suite of 26 Atari environments, we uncover that joint training stabilizes scaling dynamics, ensuring monotonic gains across all environments, regardless of their distinct inherent scaling regimes. Finally, we demonstrate that improved fidelity translates directly to downstream control, with policies learned entirely within the simulated dynamics achieving a median expert-random-normalized score of 0.770. Our findings suggest that future progress lies as much in precise scaling strategies as in architectural innovation.

---

## 14. LaWM: Least Action World Models for Long-Horizon Physical Consistency from Visual Observations

**Authors:** Qixin Xiao, Maani Ghaffari
**arXiv:** [2605.08279](https://arxiv.org/abs/2605.08279)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Learning predictive world models from visual observations is a core problem in embodied AI, with applications to model-based reinforcement learning and robotic planning. Existing latent world models typically generate future states with unconstrained neural transition functions, while modern video generation systems often prioritize perceptual plausibility or introduce physical structure through auxiliary losses, external guidance, or separate dynamics modules. As a result, long-horizon rollouts can remain weakly grounded in the physical principles that govern real dynamics, leading to compounding error, energy drift, and physically inconsistent futures. We propose Least Action World Models (LaWM), a latent world-modeling framework that operationalizes the Principle of Least Action in learned visual latent space: future rollouts are governed by a learned Lagrangian action functional rather than produced only by an unconstrained transition predictor. Our main technical realization is a latent variational integrator: LaWM encodes observations into learned generalized coordinates, learns a latent discrete Lagrangian over consecutive latent states, constructs a discrete action functional, and advances prediction by solving the corresponding discrete integration condition. Thus, physical structure is not merely used to score, regularize, or constrain a completed trajectory; it defines the latent transition rule itself. Because the transition is induced by a discrete variational principle, LaWM provides a structure-preserving bias for long-horizon visual prediction. Across physics-clean synthetic dynamics and embodied robot interaction benchmarks, LaWM improves physical invariance, background consistency, motion smoothness, and appearance and geometric prediction metrics over video-generation and world-model baselines.

---

## 15. Understanding Asynchronous Inference Methods for Vision-Language-Action Models

**Authors:** Ayoub Agouzoul
**arXiv:** [2605.08168](https://arxiv.org/abs/2605.08168)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models offer a promising path to generalist robot control, but their inference latency causes observation staleness when generated actions are executed asynchronously. Several methods have been proposed concurrently to mitigate this problem: inference-time inpainting (IT-RTC), training-time delay simulation (TT-RTC), future-state-aware conditioning (VLASH), and lightweight residual correction (A2C2). Each takes a fundamentally different approach, but they have so far been evaluated independently with different codebases, base policies, and protocols. We present a systematic comparison of these four methods under controlled conditions. We develop two unified codebases that integrate all methods with harmonized library and dataset versions, and we benchmark them on the Kinetix suite with MLPMixer policies and on the LIBERO manipulation benchmark with SmolVLA, sweeping inference delays up to $d=20$ control steps. A2C2's per-step residual correction is the most effective method on Kinetix, holding above 90% solve rate up to $d=8$, and also leads on LIBERO from $d=4$ onwards. IT-RTC is competitive at low delays but degrades sharply under long chunks ($H=30$) and high delays. TT-RTC is the most robust training-based method: stable across $d_\max$ choices, generalizes beyond its training delay distribution, and adds zero inference overhead. VLASH exhibits a clear low-delay vs. high-delay trade-off governed by the fine-tuning delay range $[0,d_\max]$. Code is available at this https URL

---

## 16. VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving

**Authors:** Rui Zhao, Haofeng Hu, Zhenhai Gao, Jiaqiao Liu, Gao Fei
**arXiv:** [2605.08133](https://arxiv.org/abs/2605.08133)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving, yet their reliance on implicit parametric knowledge limits generalization in long-tail scenarios. While Retrieval-Augmented Generation (RAG) offers a solution by accessing external expert priors, standard visual retrieval suffers from high latency and semantic ambiguity. To address these challenges, we propose \textbf{VLADriver-RAG}, a framework that grounds planning in explicit, structure-aware historical knowledge. Specifically, we abstract sensory inputs into spatiotemporal semantic graphs via a \textit{Visual-to-Scenario} mechanism, effectively filtering visual noise. To ensure retrieval relevance, we employ a \textit{Scenario-Aligned Embedding Model} that utilizes Graph-DTW metric alignment to prioritize intrinsic topological consistency over superficial visual similarity. These retrieved priors are then fused within a query-based VLA backbone to synthesize precise, disentangled trajectories. Extensive experiments on the Bench2Drive benchmark establish a new state-of-the-art, achieving a Driving Score of 89.12.

---

## 17. Latent Geometry Beyond Search: Amortizing Planning in World Models

**Authors:** Hoang Nguyen, Xiaohao Xu, Xiaonan Huang
**arXiv:** [2605.08732](https://arxiv.org/abs/2605.08732)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Modern vision-based world models can represent observations as compact yet expressive latent manifolds, but fast goal-oriented planning in these spaces remains challenging. This raises a central question: when does a learned representation simplify control, rather than merely enabling prediction? We study this question in a pretrained LeWorldModel, whose latent geometry is regularized for smoothness and uniformity. Our key insight is that, under such geometry, planning can be amortized into a latent inverse-dynamics mapping instead of requiring online search. We therefore replace iterative planning with a lightweight Goal-Conditioned Inverse Dynamics Model (GC-IDM) that maps the current latent state, goal latent state, and remaining horizon directly to the next action. Empirically, across four benchmark environments spanning navigation, contact-rich manipulation, and continuous control, our controller matches or exceeds CEM in seven of eight environment-protocol settings while reducing per-decision cost by 100-130x. A broader sweep over test-time planners (CEM, MPPI, iCEM, and gradient-based methods) shows that this result is not specific to a particular optimizer. These findings suggest that much of the structure recovered by test-time planning is already locally encoded in the latent representation. More broadly, our results indicate that sufficiently structured latent spaces can shift part of the planning burden from online optimization to learned inference.

---

## 18. Test-Time Training for Visual Foresight Vision-Language-Action Models

**Authors:** Sangwu Park, Wonjoong Kim, Yeonjun In, ..., Hongseok Kang, Chanyoung Park
**arXiv:** [2605.08215](https://arxiv.org/abs/2605.08215)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG); Robotics (cs.RO)

Visual Foresight VLA (VF-VLA) has become a prominent architectural choice in the recent VLA due to its impressive performance. Nevertheless, the inherent design of VF-VLA makes it particularly vulnerable to out-of-distribution (OOD) shifts. Because the quality of action directly depends on the accuracy of the predicted future visual information, OOD conditions affect both stages at once. To address this vulnerability, we propose Test-Time Training Visual Foresight VLA ($T^3$VF), a test-time training approach motivated by the observation that the predicted future image and its subsequent observation form a natural supervision pair. To further address the practical challenges that arise from indiscriminate test-time updates, we introduce an adaptive update filtering mechanism. Empirically, $T^3$VF mitigates the OOD vulnerability of VF-VLA at a modest additional inference cost, without requiring any architectural modification or auxiliary modules.

---

## 19. HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models

**Authors:** Qiuxuan Feng, Jiale Yu, Jiaming Liu, ..., Siwei Ma, Shanghang Zhang
**arXiv:** [2605.10942](https://arxiv.org/abs/2605.10942)
**Categories:** Robotics (cs.RO)

World Action Models (WAMs) have emerged as a promising paradigm for robot control by modeling physical dynamics. Current WAMs generally follow two paradigms: the "Imagine-then-Execute" approach, which uses video prediction to infer actions via inverse dynamics, and the "Joint Modeling" approach, which jointly models actions and video representations. Based on systematic experiments, we observe a fundamental trade-off between these paradigms: the former explicitly leverages world models for generalizable transit but lacks interaction precision, whereas the latter enables fine-grained, temporally coherent action generation but is constrained by the exploration space of the training distribution. Motivated by these findings, we propose HarmoWAM, an end-to-end WAM that fully leverages a world model to unify predictive and reactive control, enabling both generalizable transit and precise manipulation. Specifically, the world model provides spatio-temporal physical priors that condition two complementary action experts: a predictive expert that leverages latent dynamics for iterative action generation, and a reactive expert that directly infers actions from predicted visual evolution. To enable adaptive coordination, a Process-Adaptive Gating Mechanism is proposed to automatically determine the timing and location of switching between them. This allows the world model to drive the reactive expert to expand the exploration space and the predictive expert to perform precise interactions across different stages of a task. For evaluation, we construct three training-unseen test environments across six real-world robotic tasks, covering variations in background, position, and object semantics. Notably, HarmoWAM achieves strong zero-shot generalization across these scenarios, significantly outperforming prior state-of-the-art VLA models and WAMs by margins of 33% and 29%, respectively.

---

## 20. PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models

**Authors:** Xinyu Guo, Bin Xie, Wei Chai, ..., Zhengxing Wu, Xingyu Chen
**arXiv:** [2605.10925](https://arxiv.org/abs/2605.10925)
**Categories:** Robotics (cs.RO)

Large-scale pretraining has made Vision-Language-Action (VLA) models promising foundations for generalist robot manipulation, yet adapting them to downstream tasks remains necessary. However, the common practice of full fine-tuning treats pretraining as initialization and can shift broad priors toward narrow training-distribution patterns. We propose PriorVLA, a novel framework that preserves pretrained priors and learns to leverage them for effective adaptation. PriorVLA keeps a frozen Prior Expert as a read-only prior source and trains an Adaptation Expert for downstream specialization. Expert Queries capture scene priors from the pretrained VLM and motor priors from the Prior Expert, integrating both into the Adaptation Expert to guide adaptation. Together, PriorVLA updates only 25% of the parameters updated by full fine-tuning. Across RoboTwin 2.0, LIBERO, and real-world tasks, PriorVLA achieves stronger overall performance than full fine-tuning and state-of-the-art VLA baselines, with the largest gains under out-of-distribution (OOD) and few-shot settings. PriorVLA improves over pi0.5 by 11 points on RoboTwin 2.0-Hard and achieves 99.1% average success on LIBERO. Across eight real-world tasks and two embodiments, PriorVLA reaches 81% in-distribution (ID) and 57% OOD success with standard data. With only 10 demonstrations per task, PriorVLA reaches 48% ID and 32% OOD success, surpassing pi0.5 by 24 and 22 points, respectively.

---

## 21. Unified Noise Steering for Efficient Human-Guided VLA Adaptation

**Authors:** Junjie Lu, Xinyao Qin, Yuhua Jiang, ..., Min Xu, Li Zhao
**arXiv:** [2605.10821](https://arxiv.org/abs/2605.10821)
**Categories:** Robotics (cs.RO)

Diffusion-based vision-language-action (VLA) models have emerged as strong priors for robotic manipulation, yet adapting them to real-world distributions remains challenging. In particular, on-robot reinforcement learning (RL) is expensive and time-consuming, so effective adaptation depends on efficient policy improvement within a limited budget of real-world interactions. Noise-space RL lowers the cost by keeping the pretrained VLA fixed as a denoising generator while updating only a lightweight actor that predicts the noise. However, its performance is still limited due to inefficient autonomous exploration. Human corrective interventions can reduce this exploration burden, but they are naturally provided in action space, whereas noise-space finetuning requires supervision over noise variables. To address these challenges, we propose UniSteer, a Unified Noise Steering framework that combines human corrective guidance with noise-space RL through approximate action-to-noise inversion. Given a human corrective action, UniSteer inverts the frozen flow-matching decoder to recover a noise target, which provides supervised guidance for the same noise actor that is simultaneously optimized via reinforcement learning. Real-world experiments on diverse manipulation tasks show that UniSteer adapts more efficiently than strong noise-space RL and action-space human-in-the-loop baselines, improving the success rate from 20% to 90% in 66 minutes on average across four real-world adaptation tasks.

---

## 22. VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models

**Authors:** Hao Wang, Xiaobao Wei, Jingyang He, ..., Jian Tang, Shanghang Zhang
**arXiv:** [2605.10485](https://arxiv.org/abs/2605.10485)
**Categories:** Robotics (cs.RO)

Precise spatial reasoning is fundamental to robotic manipulation, yet the visual backbones of current vision-language-action (VLA) models are predominantly pretrained on 2D image data without explicit 3D geometric supervision, resulting in representations that lack accurate spatial awareness. Existing implicit spatial grounding methods partially address this by aligning VLA features with those of 3D-aware foundation models, but they rely on empirical layer search and perform alignment on LLM-level visual tokens where spatial structure has already been entangled with linguistic semantics, limiting both generalizability and geometric interpretability. We propose VEGA (Visual Encoder Grounding Alignment), a simple yet effective framework that directly aligns the output of the VLA's visual encoder with spatially-aware features from DINOv2-FiT3D, a DINOv2 model fine-tuned with multi-view consistent 3D Gaussian Splatting supervision. By performing alignment at the visual encoder output level, VEGA grounds spatial awareness before any linguistic entanglement occurs, offering a more interpretable and principled alignment target. The alignment is implemented via a lightweight projector trained with a cosine similarity loss alongside the standard action prediction objective, and is discarded at inference time, introducing no additional computational overhead. Extensive experiments on simulation benchmark and real-world manipulation tasks demonstrate that VEGA consistently outperforms existing implicit spatial grounding baselines, establishing a new state-of-the-art among implicit spatial grounding methods for VLA models.

---

## 23. Network-Efficient World Model Token Streaming

**Authors:** Shatadal Mishra, Ahmadreza Moradipari, Nejib Ammar
**arXiv:** [2605.09886](https://arxiv.org/abs/2605.09886)
**Categories:** Robotics (cs.RO)

Generative driving world models rely on compact latent state representations that must be efficiently transmitted and synchronized across distributed compute and connected vehicles. We study network-efficient streaming of a discrete world model state, where a stride-16 VQ-U-Net tokenizer (codebook size 8,192) maps each 288x512 frame to an 18x32 grid of token IDs (576 tokens/frame), equivalent to 936 bytes/frame under fixed-length coding. We consider a keyframe--delta protocol under strict per-message payload budgets and packet loss, and propose a fully online, label-free algorithm that prioritizes delta updates via cosine distance in codebook embedding space and triggers keyframes adaptively using a Hamming-drift threshold. The adaptive algorithm consistently improves the rate distortion frontier over periodic keyframes at matched bitrates: at 0.024 Mb/s (200-byte budget) dynamic-only embedding distortion drops from 0.0712 to 0.0661 (7.2\%), and at 0.036 Mb/s (400-byte budget) from 0.0427 to 0.0407 (4.8\%). Under 10\% delta packet loss at 200 bytes, dynamic-only distortion is 0.0757 versus 0.0789 for a matched periodic baseline. To connect state fidelity to world model usefulness, we train a lightweight next-token predictor and evaluate perplexity conditioned on streamed receiver states: at 0.024 Mb/s, dynamic-position perplexity improves from 206.0 to 193.1 (6.3\%), and at 0.036 Mb/s from 158.9 to 155.6 (2.1\%). These results support discrete token-state streaming as a practical systems layer for bandwidth-aware synchronization and improved downstream token-dynamics utility under vehicular networking constraints.

---

## 24. SABER: A Scalable Action-Based Embodied Dataset for Real-World VLA Adaptation

**Authors:** Narsimha Menga, Parikshit Sakurikar, Amirreza Rouhi, ..., Anoop Namboodiri, Sashi Reddi
**arXiv:** [2605.09613](https://arxiv.org/abs/2605.09613)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Robotic deployment in real-world environments depends on rich, domain-specific action data as much as on strong model architecture. General-purpose robot foundation models show modest performance in complex unseen tasks such as manipulation in a retail domain when applied out of the box. The root cause is a data gap: retail environments are structurally absent from general robot pretraining distributions, and the path to filling that gap through teleoperation is prohibitively expensive, logistically constrained, and difficult to scale. We introduce SABER, a high-fidelity retail robotics action dataset built from over 100 hours of natural in-store capture across multiple real grocery environments. Egocentric footage from head-mounted cameras records fine-grained hand activity at the point of interaction, while exocentric 360-degree scene footage from DreamVu's ALIA camera simultaneously observes all actors and activities across the entire space. This combination yields a uniquely complete picture of human retail behavior: dexterous hand activity, whole-body motion, and scene dynamics, all captured without staging, scripting, or teleoperation overhead. The SABER corpus contains 44.8K training samples across three action representation streams: 25K latent action sequences via LAPA-style encoding, 18.6K dexterous hand-pose trajectories retargeted to robot joint space, and 1.2K whole-body synchronized motion sequences retargeted to a humanoid embodiment. When applied to GR00T N1.6 via a shared-backbone multi-task post-training recipe, SABER yields a mean success rate of 29.3% across ten retail manipulation tasks -- more than 2.19x over fine-tuning baselines (13.4%). SABER demonstrates that the path to capable retail robots runs through better data, which can be collected today, at scale, without a robot in the loop. The dataset and code are available at this https URL

---

## 25. Preserving Foundational Capabilities in Flow-Matching VLAs through Conservative SFT

**Authors:** Tianyi Zhang, Shaopeng Zhai, Haoran Zhang, Fuxian Huang, Qi Zhang
**arXiv:** [2605.08879](https://arxiv.org/abs/2605.08879)
**Categories:** Robotics (cs.RO)

Unconstrained fine-tuning of flow-matching Vision-Language-Action (VLA) models drives dense parameter overwrites, degrading pre-trained capabilities. We present Conservative Supervised Fine-Tuning (ConSFT), an optimization objective that adapts to target distributions while mitigating catastrophic forgetting, requiring zero prior data or architectural overhead. By dynamically scaling learning signals based on model confidence, ConSFT suppresses excessive gradients from low-confidence samples to prevent disproportionate parameter updates, thereby bounding the intrinsic parameter disruption risk. Inspired by reinforcement learning's trust-region clipping, this formulation establishes a progressive learning dynamic to secure target convergence and prior capability retention, maintaining sparse parameter updates without relying on the parallel reference networks required by explicit regularization. We evaluate ConSFT on the LIBERO and RoboTwin benchmarks across state-of-the-art flow-matching VLAs ($\pi_0$, $\pi_{0.5}$, and GR00T-N1.6-3B). The method outperforms vanilla SFT in capability retention by an average absolute margin of over 20\%, matching the efficacy of data-heavy Experience Replay in a prior-data-free regime. Real-world robotic deployments confirm that ConSFT precludes spatial overfitting during downstream adaptation, preserving pre-trained physical skills while acquiring sequential target tasks.

---

## 26. ATAAT: Adaptive Threat-Aware Adversarial Tuning Framework against Backdoor Attacks on Vision-Language-Action Models

**Authors:** Kewei Chen, Yayu Long, Shuai Li, Mingsheng Shang
**arXiv:** [2605.08612](https://arxiv.org/abs/2605.08612)
**Categories:** Robotics (cs.RO)

Addressing the escalating security vulnerabilities in Vision-Language-Action (VLA) models, this study investigates backdoor attacks targeting the visual pathway. We identify a core obstacle causing the failure of traditional attack paradigms: "Gradient Interference." This phenomenon represents an optimization failure triggered by conflicting strategies during end-to-end training. To resolve this, we propose an Adaptive Threat-Aware Adversarial Tuning (ATAAT) framework. Through its core "Threat-Method Adaptive Mapping" mechanism, ATAAT intelligently selects the optimal gradient decoupling strategy based on the adversary's capabilities. Extensive experiments demonstrate that ATAAT exhibits significant advantages, achieving a highly robust Targeted Attack Success Rate (TASR > 80%) while maintaining extreme stealthiness with merely a 5% poisoning rate. It efficiently handles complex semantic-level triggers and achieves implicit decoupled attacks in data poisoning scenarios for the first time. This work reveals a critical security vulnerability in VLAs and provides theoretical and methodological support for future defense architectures.

---

## 27. Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models

**Authors:** Meng Zheng, Samhita Marri, Anwesa Choudhuri, ..., Girish Chowdhary, Ziyan Wu
**arXiv:** [2605.08434](https://arxiv.org/abs/2605.08434)
**Categories:** Robotics (cs.RO)

Vision-language-action (VLA) models provide a promising paradigm for scalable robotic manipulation, yet their reliance on success-only behavioral cloning leaves them brittle; lacking corrective training signals, minor execution errors rapidly compound into unrecoverable, out-of-distribution failures. To address this limitation, we propose Adaptive Failure-Informed Learning (AFIL), an end-to-end framework that leverages failure trajectories as adaptive negative guidance for diffusion- and flow-based VLA policies. AFIL uses a pretrained VLA to generate failure rollouts online, avoiding the need for handcrafted failure-mode design or human-in-the-loop recovery. It then jointly trains Dual Action Generators (DAGs) for successful and failed behaviors while sharing a common vision-language backbone, enabling efficient failure-aware policy learning with limited parameter overhead. During sampling, the failure generator adaptively steers action generation away from failure-prone regions and toward more reliable success modes, with guidance strength determined by the per-diffusion-step distance between success and failure distributions. Experiments across in-domain and out-of-domain robotic manipulation tasks, covering both short- and long-horizon settings, show that AFIL consistently improves task success rates and robustness over existing VLA baselines, demonstrating its effectiveness, efficiency, and generality.

---

## 28. CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models

**Authors:** Wenxuan Song, Han Zhao, Fuhao Li, ..., Donglin Wang, Haoang Li
**arXiv:** [2605.10903](https://arxiv.org/abs/2605.10903)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary objectives. To simultaneously achieve the enhanced capabilities of auxiliary training with the simplicity of standard SFT, we decouple the two objectives of auxiliary-objective SFT within the parameter space, namely, enhancing general capabilities and fitting task-specific action distributions. To deliver the goal, we only need to train the model to converge on a small-scale task set using two distinct training strategies, resulting in two finetuned models. The parameters' difference between the two models can then be interpreted as capability vectors provided by auxiliary objectives. These vectors are then merged with pretrained parameters to form a capability-enhanced meta model. Moreover, when standard SFT is augmented with a lightweight orthogonal regularization loss, the merged model attains performance comparable to auxiliary finetuned baselines with reduced computational overhead. Internal and external experiments demonstrate that our capability vectors (1) are effective and versatile across diverse models, (2) can generalize to novel environments and embodiments out of the box.

---

## 29. Is Your Driving World Model an All-Around Player?

**Authors:** Lingdong Kong, Ao Liang, Tianyi Yan, ..., Wei Tsang Ooi, Ziwei Liu
**arXiv:** [2605.10858](https://arxiv.org/abs/2605.10858)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally. Some generate photorealistic textures but violate basic physics; others maintain geometric consistency but fail when subjected to closed-loop planning. This disconnect exposes a critical gap: the field evaluates how real generated worlds appear, but rarely whether they behave realistically. We introduce WorldLens, a unified benchmark that measures world-model fidelity across the full spectrum, from pixel quality and 4D geometry to closed-loop driving and human perceptual alignment, through five complementary aspects and 24 standardized dimensions. Our evaluation of six representative models reveals that no existing approach dominates across all axes: texture-rich models violate geometry, geometry-aware models lack behavioral fidelity, and even the strongest performers achieve only 2-3 out of 10 on human realism ratings. To bridge algorithmic metrics with human perception, we further contribute WorldLens-26K, a 26,808-entry human-annotated preference dataset pairing numerical scores with textual rationales, and WorldLens-Agent, a vision-language evaluator distilled from these judgments that enables scalable, explainable auto-assessment. Together, the benchmark, dataset, and agent form a unified ecosystem for assessing generated worlds not merely by visual appeal, but by physical and behavioral fidelity.

---

## 30. DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving

**Authors:** Lingjun Zhang, Changjie Wu, Linzhe Shi, ..., Mu Xu, Hong Wang
**arXiv:** [2605.10564](https://arxiv.org/abs/2605.10564)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions. However, the reasoning mechanisms employed in most methods are direct adaptations from general domains, lacking in-depth exploration tailored to autonomous driving scenarios, particularly within visual reasoning modules. In this paper, we propose a driving world model that performs parallel prediction of latent semantic features for consecutive future frames in the bird's-eye-view (BEV) space, thereby enabling long-horizon modeling of future world states. We also introduce an efficient and adaptive text reasoning mechanism that utilizes additional social knowledge and reasoning capabilities to further improve driving performance in challenging long-tail scenarios. We present a novel, efficient, and effective approach that achieves state-of-the-art (SOTA) results on the closed-loop Bench2drive benchmark. Codes are available at: this https URL.

---

## 31. DeformMaster: An Interactive Physics-Neural World Model for Deformable Objects from Videos

**Authors:** Can Li, Zhoujian Li, Ren Li, ..., Jingmin Chen, Lei Sun
**arXiv:** [2605.09586](https://arxiv.org/abs/2605.09586)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

World models for deformable objects should recover not only geometry and appearance, but also underlying physical dynamics, interaction grounding, and material behavior. Learning such a model from real videos is challenging because deformable linear, planar, and volumetric objects evolve under high-dimensional deformation, noisy interactions, and complex material response. The model must therefore infer a physical state from visual observations, roll it forward under new interactions, and render the resulting dynamics with high visual fidelity. We present DeformMaster, a video-derived interactive physics--neural world model that turns real interaction videos into an online interactive model of deformable objects within a unified dynamics-and-appearance framework. DeformMaster preserves structured physical rollout while using a neural residual to compensate for unmodeled effects, grounds sparse hand motion as distributed compliant actuator for hand--continuum interaction, represents material response with spatially varying constitutive experts, and drives high-fidelity 4D appearance from the predicted physical evolution. Experiments on real-world deformable-object sequences demonstrate DeformMaster's ability to roll out future dynamics and render dynamic appearance, outperforming state-of-the-art baselines while supporting novel action rollout, material-parameter variation, and dynamic novel-view synthesis.

---

## 32. MAG-VLAQ: Multi-modal Aerial-Ground Query Aggregation for Cross-View Place Recognition

**Authors:** Zhengyi Xu, Yuhang Ming, Zhihao Zhan, ..., Javier Civera, Wanzeng Kong
**arXiv:** [2605.09418](https://arxiv.org/abs/2605.09418)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Multi-modal cross-view place recognition remains a fundamental challenge in computer vision and robotics due to the severe viewpoint, modality, and spatial-structure discrepancies between ground observations and aerial references. To address this challenge, we present MAG-VLAQ, a foundation-model-enhanced query aggregation framework for multi-modal aerial-ground cross-view place recognition. Specifically, our approach leverages pre-trained foundation models to extract dense visual tokens from both ground and aerial images, as well as expressive geometric tokens from ground LiDAR observations. These heterogeneous tokens are then projected into a shared embedding space for cross-modal alignment and fusion. As our main contribution, we propose ODE-conditioned VLAQ, which tightly couples neural ordinary differential equations (ODE)-based RGB-LiDAR fusion with vectors of locally aggregated queries (VLAQ). In this design, the VLAQ query centers are dynamically adapted according to the fused multi-modal state. This mechanism allows the final global descriptor to preserve globally learned retrieval prototypes while remaining responsive to scene-specific visual and geometric evidence, significantly improving aerial-ground matching. Extensive experiments on KITTI360-AG and nuScenes-AG validate the effectiveness of our proposed MAG-VLAQ. Notably, on KITTI360-AG, our MAG-VLAQ nearly doubles the state-of-the-art performance, achieving 61.1 Recall@1 in the satellite setting, compared with 34.5 from the closest competing approach.

---

## 33. DriveFuture: Future-Aware Latent World Models for Autonomous Driving

**Authors:** Yufeng Hong, Xiaotian Zhou, Yingyan Li, ..., Lei Yang, Ziying Song
**arXiv:** [2605.09701](https://arxiv.org/abs/2605.09701)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Existing latent world models for autonomous driving have opened a promising path toward future-aware driving intelligence. However, they typically treat future latent states as prediction targets or auxiliary signals, rather than directly conditioning trajectory planning. This can entangle current and future features in latent space. In this work, we propose DriveFuture, a future-aware latent world modeling framework for autonomous driving that explicitly learns planning-oriented foresight by conditioning the current latent state modeling process on future world states. Specifically, during training, the model first predicts future latent world states from the current latent state and ego action, and then refines the prediction against the ground-truth future latent state via cross-attention. The resulting future-aware latent serves as an explicit condition for a diffusion-based trajectory planner. During inference, DriveFuture conditions on the predicted future latent state instead of the ground-truth future state. DriveFuture achieves SOTA performance on the public NAVSIM benchmarks, reaching \textbf{55.5} EPDMS on NAVSIM-v2 {\textcolor{blue}{\textit{navhard}}}, \textbf{89.9} EPDMS on NAVSIM-v2 {\textcolor{blue}{\textit{navtest}}}, and \textbf{90.7} PDMS on NAVSIM-v1 {\textcolor{blue}{\textit{navtest}}}, respectively. These results suggest that the key to latent world modeling lies not merely in simulating future states, but more importantly in conditioning current decision-making on future states. Notably, as of April 2026, DriveFuture ranks \textbf{1st} on the \href{this https URL}{NAVSIM-v2 {\textcolor{blue}{\textit{navhard}}}} leaderboard and achieves SOTA performance on \href{this https URL}{NAVSIM-v1 {\textcolor{blue}{\textit{navtest}}}}.

---

## 34. ACWM-Phys: Investigating Generalized Physical Interaction in Action-Conditioned Video World Models

**Authors:** Haotian Xue, Yipu Chen, Liqian Ma, ..., Yuchen Zhu, Yongxin Che
**arXiv:** [2605.08567](https://arxiv.org/abs/2605.08567)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Action-conditioned world models (ACWMs) have shown strong promise for video prediction and decision-making. However, existing benchmarks are largely restricted to egocentric navigation or narrow, task-specific robotics datasets, offering only limited coverage of the rich physical interactions required for generalized world understanding. We introduce ACWM-Phys, a new benchmark for evaluating action-conditioned prediction under diverse physical dynamics in a clean, controllable simulation environment with a carefully designed action space. ACWM-Phys contains training and evaluation data spanning rigid-body dynamics, kinematics, deformable-object interactions, and particle dynamics. To evaluate both interpolation and generalization, we design in-distribution and out-of-distribution protocols with controlled shifts in interaction patterns or scene configurations. By building the benchmark in a fully controllable simulator, ACWM-Phys enables precise data collection, reproducible evaluation, and systematic analysis of model capabilities for physically grounded world modeling. Through systematic experiments on ACWM-DiT, we find that OoD generalization depends not only on the physical regime but also on effective task complexity: models generalize well on visually simple, low-dimensional interactions with clear geometric structure, but suffer larger drops on deformable contacts, high-dimensional control, and complex articulated motion. This suggests that the model still relies heavily on visual appearance patterns instead of fully learning the underlying physics. Ablations show that cross-attention improves high-dimensional action conditioning, causal VAEs outperform frame-wise encoders, and larger action spaces are harder to model but can improve generalization by providing richer control signals. These findings guide the design of physically grounded world models.

---

## 35. Do multimodal models imagine electric sheep?

**Authors:** Santhosh Kumar Ramakrishnan, Carl Vondrick, Raja Giryes, Philipp Krähenbühl, Vladlen Koltun
**arXiv:** [2605.09693](https://arxiv.org/abs/2605.09693)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Yes. We find that large multimodal models develop mental imagery when solving spatial puzzles, and they do imagine sheep when solving sheep puzzles. We fine-tune a Qwen3.5 VLM to solve twelve diverse visual reasoning tasks -- including tangram, jigsaw, sokoban, 3D mental rotation, and rush hour -- that require understanding geometry, spatial relationships, and the consequences of actions. By supervising the model to predict the open-loop sequence of actions to solve a puzzle from an initial state, we show that the model's activations after each action encode meaningful visual information about the intermediate state. This finding suggests that an imperfect visual world model begins to form as a byproduct of learning to select correct actions, in the absence of any explicit visual supervision. Building on this observation, we propose two ways to sharpen and use the mental images formed by the model. We find that integrating as few as sixteen visual tokens per step into the chain of thought improves the average solve rate from 83% to 89%, with particularly strong gains on reasoning-heavy tasks such as jigsaw and 3D mental rotation.

---

## 36. VECTOR-Drive: Tightly Coupled Vision-Language and Trajectory Expert Routing for End-to-End Autonomous Driving

**Authors:** Rui Zhao, Jianlin Yu, Zhenhai Gao, Jiaqiao Liu, Fei Gao
**arXiv:** [2605.08830](https://arxiv.org/abs/2605.08830)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

End-to-end autonomous driving requires models to understand traffic scenes, infer driving intent, and generate executable motion plans. Recent vision-language-action (VLA) models inherit semantic priors from large-scale vision-language pretraining, yet still face a coupling trade-off: fully shared backbones preserve multimodal interaction but may entangle language reasoning and trajectory prediction, whereas decou pled reasoning-action pipelines reduce task conflict but weaken semantic-motion coupling. We propose VECTOR-DRIVE, a tightly coupled VLA framework built on Qwen2.5-VL-3B. VECTOR-DRIVE keeps all tokens coupled through shared self attention and routes feed-forward computation according to token semantics. Vision and language tokens are processed by a Vision-Language Expert to preserve semantic priors, while target-point, ego-state, and noisy action tokens are routed to a Trajectory Expert for motion-specific computation. On the action-token pathway, a flow-matching planner refines noisy action tokens into future waypoints and speed profiles. This design couples semantic reasoning and motion planning within a single multimodal Transformer while separating task-specific FFN computation. On Bench2Drive, VECTOR-DRIVE achieves 88.91 Driving Score and outperforms representative end-to end and VLA-based baselines. Qualitative results and ablations further validate the benefits of shared attention, semantic-aware expert routing, progressive training, and flow-based action de coding.

---

## 37. Geometry Guided Self-Consistency for Physical AI

**Authors:** Yinwei Dai, Zhuofu Chen, Lijie Yang, Ravi Netravali
**arXiv:** [2605.08638](https://arxiv.org/abs/2605.08638)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

State-of-the-art physical AI models generate a chunk of actions per inference through diffusion or flow matching, iteratively refining an initial noise sample into an action trajectory. Because this inference process is inherently stochastic, committing to a single trajectory per round is brittle, and this brittleness compounds across the many sequential rounds that comprise a complete episode. We introduce KeyStone, an inference-time self-consistency method for diffusion-based action generation that draws $K$ candidate action chunks in parallel from a shared model context, clusters them in continuous action space, and returns the medoid of the largest cluster -- no additional model required. Two properties make this practical. First, the compact nature of action trajectories makes diffusion inference memory-bandwidth bound, leaving spare compute capacity to run $K$ chains in parallel with no additional wall-clock latency. Second, unlike token or pixel spaces where distance carries no semantic meaning and selection requires a learned judge, action chunks are geometrically structured such that Euclidean distance directly reflects physical similarity, making selection principled and judge-free. Across diverse vision-language-action models (VLAs) and world-action models (WAMs), KeyStone improves task success rates by up to \textbf{13.3\%} over single-trajectory sampling with negligible latency overhead, while having on par accuracy with model-based selectors at no training cost. We open source KeyStone at this https URL.

---

## 38. RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark

**Authors:** Huashuo Lei, Wenxuan Song, Huarui Zhang, ..., Yan Wang, Haoang Li
**arXiv:** [2605.10921](https://arxiv.org/abs/2605.10921)
**Categories:** Robotics (cs.RO)

Memory is a critical component of robotic intelligence, as robots must rely on past observations and actions to accomplish long-horizon tasks in partially observable environments. However, existing robotic memory benchmarks still lack multimodal annotations for memory formation, provide limited task coverage and structural complexity, and remain restricted to simulation without real-world evaluation. We address this gap with RoboMemArena, a large-scale benchmark of 26 tasks, with average trajectory lengths exceeding 1,000 steps per task and 68.9% of subtasks being memory-dependent. The generation pipeline leverages a vision-language model (VLM) to design and compose subtasks, generates full trajectories through atomic functions, and provides memory-related annotations, including subtask instructions and native keyframe annotations, while paired real-world memory tasks support physical evaluation. We further design PrediMem, a dual-system VLA in which a high-level VLM planner manages a memory bank with recent and keyframe buffers and uses a predictive coding head to improve sensitivity to task dynamics. Extensive experiments on RoboMemArena show that PrediMem outperforms all baselines and provides insights into memory management, model architecture, and scaling laws for complex memory systems.

---

## 39. Data-Asymmetric Latent Imagination and Reranking for 3D Robotic Imitation Learning

**Authors:** Lianghao Luo, Xizhou Bu, Ruyan Liu, ..., Hongbo Wang, Wei Li
**arXiv:** [2605.10166](https://arxiv.org/abs/2605.10166)
**Categories:** Robotics (cs.RO)

Robotic imitation learning typically assumes access to optimal demonstrations, yet real-world data collection often yields suboptimal, exploratory, or even failed trajectories. Discarding such data wastes valuable information about environment dynamics and failure modes, which can instead be leveraged to improve decision-making. While 3D policies reduce reliance on high-quality demonstrations through strong spatial generalization, they still require large-scale data to achieve high task success. To address this, we propose DALI-R, a Data-Asymmetric Latent Imagination and Reranking framework for 3D robotic imitation learning from mixed-quality trajectories. It learns a Latent World Model over 3D point clouds for imagined rollouts and a Task Completion Scorer that reranks candidate action chunks, improving decision-making without additional high-quality demonstrations. We instantiate DALI-R with both diffusion and efficient flow-matching policies and evaluate it on Adroit and MetaWorld benchmarks. Across the two evaluated 3D base policies, DALI-R achieves an average $6.8$\% improvement in success rate while incurring less than $0.7\times$ additional inference overhead.

---

## 40. StereoPolicy: Improving Robotic Manipulation Policies via Stereo Perception

**Authors:** Evans Han, Yunfan Jiang, Yingke Wang, ..., Li Fei-Fei, Ruohan Zhang
**arXiv:** [2605.09989](https://arxiv.org/abs/2605.09989)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV)

Recent advances in robot imitation learning have yielded powerful visuomotor policies capable of manipulating a wide variety of objects directly from monocular visual inputs. However, monocular observations inherently lack reliable depth cues and spatial awareness, which are critical for precise manipulation in cluttered or geometrically complex scenes. To address this limitation, we introduce StereoPolicy, a new visuomotor policy learning framework that directly leverages synchronized stereo image pairs to strengthen geometric reasoning, without requiring explicit 3D reconstruction or camera calibration. StereoPolicy employs pretrained 2D vision encoders to process each image independently and fuses the resulting representations through a Stereo Transformer. This design implicitly captures spatial correspondence and disparity cues. The framework integrates seamlessly with diffusion-based and pretrained vision-language-action (VLA) policies, delivering consistent improvements over RGB, RGB-D, point cloud, and multi-view baselines across three simulation benchmarks: RoboMimic, RoboCasa, and OmniGibson. We further validate StereoPolicy on real-robot experiments spanning both tabletop and bimanual mobile manipulation settings. Our results underscore stereo vision as a scalable and robust modality that bridges 2D pretrained representations with 3D geometric understanding for robotic manipulation.

---

## 41. Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning

**Authors:** Kewei Chen, Yayu Long, Mingsheng Shang
**arXiv:** [2605.09537](https://arxiv.org/abs/2605.09537)
**Categories:** Robotics (cs.RO)

Despite rapid progress in Vision-Language-Action (VLA) models for robotic control, instruction drift remains a persistent failure mode in long-horizon tasks. This paper reconceptualizes this phenomenon, positing that instruction drift is fundamentally a systematic sampling error: local greedy sampling is prone to collapsing into "Negative Pivotal Windows"--irreversible local optima with high local probability that sever global success pathways. To address this, we propose Context-Aware Power Sampling (CAPS), a training-free inference-time computation framework. CAPS leverages power distributions to sharpen global trajectory probabilities, enabling lookahead search over the model's conditional generative trajectory distribution. Furthermore, we introduce a metacognitive control mechanism based on Signal-to-Noise Ratio (SNR). This mechanism triggers adaptive MCMC search solely when drift risk is detected, enabling a dynamic transition from "intuitive fast thinking" to "rational slow search." Experiments on RoboTwin, Simpler-WindowX, and Libero-long benchmarks show that CAPS achieves substantial improvements over strong baselines, including OpenVLA and TACO, without parameter updates. These results support the effectiveness of adaptive inference-time computation for improving long-horizon robustness in embodied control.

---

## 42. ElasticFlow: One-Step Physics-Consistent Policy with Elastic Time Horizons for Language-Guided Manipulation

**Authors:** Kewei Chen, Yayu Long, Shuai Li, Mingsheng Shang
**arXiv:** [2605.08799](https://arxiv.org/abs/2605.08799)
**Categories:** Robotics (cs.RO)

Diffusion policies have demonstrated exceptional performance in embodied AI. However, their iterative denoising process results in high latency, and existing acceleration methods often sacrifice physical consistency. To address this, we propose ElasticFlow, a distillation-free, physics-consistent one-step policy framework. We reconstruct the Mean Field Theory by directly modeling the average velocity field, enabling a direct single-step mapping from noise to action. Addressing the Temporal Heterogeneity of robotic tasks, we introduce the Elastic Time Horizons mechanism. This mechanism effectively overcomes Spectral Bias by explicitly encoding control granularity, achieving efficient alignment between semantic instructions and physical execution horizons. Experiments on benchmarks such as LIBERO, CALVIN, and RoboTwin demonstrate that ElasticFlow achieves efficient 1-NFE inference (approximately 71Hz). Furthermore, it outperforms state-of-the-art methods, including OpenVLA and $\pi_0$, on long-horizon tasks, highlighting its potential for efficient, robust, and semantically aligned control.

---
