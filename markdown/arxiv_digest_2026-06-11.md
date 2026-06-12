# arXiv Daily Digest — 2026-06-11

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 14

---

## 1. CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

**Authors:** Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg
**arXiv:** [2606.12352](https://arxiv.org/abs/2606.12352)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Multi-robot collaboration allows robots to efficiently take on a wide range of tasks, from moving a couch through a doorway to assembling structures on a construction site. However, achieving such coordination in mobile multi-robot settings remains challenging: centralized methods conditioned on the combined observations of a team scale poorly with team size, and decentralized methods that train one policy per robot often require explicit alignment procedures or information sharing at inference time to overcome partial observability. Our key insight is that the visuomotor priors of pretrained vision-language-action (VLA) models should enable reactive, decentralized collaboration from each robot's local observations alone, without these inference-time assumptions. We propose CHORUS, a framework that adapts a single VLA backbone to control diverse, multi-robot teams. At inference time, each robot runs an independent copy of CHORUS, conditioned only on its own observations and a robot-identifying prompt. In real-world experiments including mobile tape measurement, library book handovers, and laundry basket lifting, CHORUS achieves a 64% point improvement over decentralized, from-scratch models, improves reactivity to teammate behavior by 40% points, and outperforms centralized baselines. Together, these results show that a shared VLA backbone is capable of achieving decentralized multi-robot collaboration, without per-robot policies or inter-robot communication at inference.

---

## 2. Making Foresight Actionable: Repurposing Representation Alignment in World Action Models

**Authors:** Lu Qiu, Yizhuo Li, Yi Chen, ..., Yixiao Ge, Xihui Liu
**arXiv:** [2606.12217](https://arxiv.org/abs/2606.12217)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Robotics (cs.RO)

World Action Models (WAMs) offer a promising route for robot manipulation by using video generation models to model future scene evolution before producing control actions. However, our empirical observations reveal a phenomenon: generating plausible visual futures does not always guarantee the extraction of accurate actions. To diagnose this failure, we conduct action-head attention analysis and causal interventions. We find that the action decoder fails to focus on task-relevant interaction regions and remains sensitive to perturbations in task-irrelevant areas. This reveals a representation mismatch: hidden states optimized for visual reconstruction are not inherently organized in a form useful for low-level action control. In this paper, we propose AGRA, an Action-Grounded Representation Alignment objective that regularizes the world-action interface by aligning intermediate video diffusion features with spatially coherent semantic representations from a foundation visual encoder. We evaluate AGRA on real-world manipulation tasks. Experiments show that AGRA makes world model representations more action-grounded: by focusing the action decoder on the correct interaction regions, it improves object localization accuracy and affordance understanding, and makes the policy more robust to perturbations in task-irrelevant regions. As a result, AGRA consistently improves both in-distribution performance and out-of-distribution generalization over the baseline world action model.

---

## 3. Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning

**Authors:** Chuanke Pang, Junyi Huang, Zhijun Zhao, ..., Kun Xu, Xilun Ding
**arXiv:** [2606.12109](https://arxiv.org/abs/2606.12109)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot generalization in robotic manipulation, yet the vast majority of pre-trained pipelines remain strictly confined to low-DoF parallel grippers. Adapting these rich semantic priors to high-DoF dexterous hands introduces a severe morphology gap, direct end-to-end joint fine-tuning inherently causes catastrophic forgetting of spatial reasoning and acute action manifold collapse due to data scarcity. In this paper, we present InDex, a novel, data-efficient adaptation framework rooted in cross-morphology semantic inheritance. Rather than discarding the pre-trained 1-DoF parallel grasp output, we repurpose it as a continuous, macroscopic virtual grasp intent proxy to sequentialize the control topology. We implement a two-stage decoupled learning architecture: the first stage parameter-efficiently aligns the VLA backbone to predict continuous arm trajectories and the scalar grasp intent; the second stage freezes this spatial backbone and leverages an intent-conditioned denoising diffusion head to decode fine-grained joint articulations for multi-fingered end-effectors. Extensive simulation benchmarks across a suite of multi-stage, contact-rich dexterous manipulation tasks demonstrate that InDex effectively masters intricate skills with minimal demonstration data, substantially outperforming monolithic baselines while preserving the robust spatial generalizability of the original VLA prior.

---

## 4. Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering

**Authors:** Hyun Joe Jeong, Gokul Swamy, Andrea Bajcsy
**arXiv:** [2606.12299](https://arxiv.org/abs/2606.12299)
**Categories:** Robotics (cs.RO); Machine Learning (cs.LG)

Vision-Language-Action (VLA) models provide a natural language interface to robot control, but the mapping from language to behavior is often brittle and unintuitive: semantically similar instructions can induce drastically different behaviors, while some capabilities may not be elicitable through prompting alone. As a result, both human instructions and zero-shot language models can fail to reliably steer VLAs toward successful task execution. In this work, we propose a framework that interactively searches for language sequences that improve closed-loop VLA task performance, distills these sequences into a test-time language feedback policy (LFP), and learns an improvement head that predicts when language steering will improve performance. We conformalize this improvement head to prevent harmful steering interventions, where the LFP decreases task performance relative to the original instruction on out-of-distribution scenarios. Crucially, our approach operates on arbitrary frozen pre-trained VLAs, requiring neither access to the original training distribution nor fine-tuning of the underlying model. On seen environments, our conformalized LFP improves base VLA performance by 24.7% in simulation and 65.0% in hardware. On visual and semantic perturbations, our conformalized LFP has strong harmlessness guarantees, and produces recovery behaviors not observed with open-loop prompting.

---

## 5. DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model

**Authors:** Pankhuri Vanjani, Zhuoyue Li, Jakub Suliga, ..., Xinkai Jiang, Rudolf Lioutikov
**arXiv:** [2606.12105](https://arxiv.org/abs/2606.12105)
**Categories:** Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)

Vision-language-action (VLA) models inherit a shared synchronous clock from vision-language pretraining, processing every input at one rate. This is misaligned with physical interaction, where a high-frequency modality changes at hundreds of hertz, vision evolves more slowly, and language stays constant across an episode. A synchronous VLA oversamples slow modalities, undersamples fast ones, and caps action generation at the lowest effective frequency. We hypothesize that decoupling temporal processing per modality, letting each update and retain information at its own sensor rate, yields stronger representations and more robust control. We present DAM-VLA, which maintains per-modality latent buffers refreshed at sensor rates and read continuously by the action head, integrating new high-frequency modalities through gated cross-attention that leaves the pretrained backbone intact. Across seven contact-rich real-world manipulation tasks, DAM-VLA more than doubles the average success rate of the strongest synchronous baseline (95.2\% vs.\ 40.95\%) while sustaining smooth, reactive 100\,Hz control. Project website: \href{this https URL}{this http URL}

---

## 6. TacCoRL: Integrating Tactile Feedback into VLA via Simulation

**Authors:** Siyu Ma, Yuqi Liang, Chang Yu, ..., Yin Yang, Chenfanfu Jiang
**arXiv:** [2606.11743](https://arxiv.org/abs/2606.11743)
**Categories:** Robotics (cs.RO); Graphics (cs.GR); Machine Learning (cs.LG)

Vision-language-action (VLA) models provide strong visual, language, and action priors for robot manipulation, but visual observations alone often miss the local contact state required for contact-rich tasks. We present TacCoRL, a scalable framework that injects Tactile feedback into VLA policies and improves them through sim-real Co-training and simulation-based reinforcement learning (RL), without requiring large-scale tactile pretraining or extensive real-world contact exploration. The key idea is not only adding touch as an input, but learning how contact readings should modulate action responses in near-failure states that are rare in demonstrations and risky to collect on hardware. We use a real-aligned simulator as a closed-loop training environment for contact interaction. Mixed simulated and real trajectories first warm-start tactile-conditioned actions in the pretrained policy. Reinforcement learning with verifiable task rewards then optimizes the policy using simulated contact rollouts. It reinforces tactile-conditioned actions that lead to task completion, while a supervised objective on real trajectories keeps the refined policy anchored to deployment visual, tactile, and action distributions. The resulting policy transfers directly to the real robot without privileged simulation state or online real-world RL. Across four bimanual contact-rich tasks, the final visuo-tactile policy achieves an average success rate of 72.5%, compared to baseline of 50.0%. Result videos and more details are available at this https URL

---

## 7. World Pilot: Steering Vision-Language-Action Models with World-Action Priors

**Authors:** Zefu Lin, Rongxu Cui, Junjia Xu, ..., Lue Fan, Zhaoxiang Zhang
**arXiv:** [2606.12403](https://arxiv.org/abs/2606.12403)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models inherit semantic grounding from large-scale pretraining and perform competently across in-distribution manipulation tasks. This grounding, however, is built on static image-text pairs, whereas manipulation is a continuous, contact-rich process whose dynamics this pretraining cannot capture. We present World Pilot, a VLA framework that augments the policy with priors from a World-Action Model (WAM), routed into the decision chain through two complementary pathways. Latent Steering conditions the perception layer on a scene-evolution latent, and Action Steering supplies an anticipated trajectory as a motion prior to the action generator. Together the two priors equip the VLA with an anticipated view of the scene and a trajectory-level motion hint alongside its semantic conditioning, and the scene-evolution prior remains effective even when supplied by a video-pretrained world model that has not been action-post-trained. World Pilot attains a state-of-the-art Total success rate of 84.7% on the LIBERO-Plus zero-shot OOD benchmark and the highest success rate on every real-robot setting across four manipulation tasks, with the largest margins under shifts in viewpoint, geometry, deformable state, and pose. Project Website: this https URL

---

## 8. APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies

**Authors:** Kechun Xu, Zhenjie Zhu, Anzhe Chen, Rong Xiong, Yue Wang
**arXiv:** [2606.12366](https://arxiv.org/abs/2606.12366)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models that couple pretrained Vision-Language Models (VLMs) with continuous action experts have achieved strong manipulation performance, yet generalization to out-of-distribution (OOD) language instructions remains poor. A known challenge is the structural imbalance in VLA data, where language is far less diverse than visual and action content, making policies prone to visual shortcuts. While discrete-action methods mitigate this through vision-language co-training, continuous action experts lack such protection: they start from random initialization and learn entirely from imbalanced data, producing noisy gradients that corrupt the VLM and fail to exploit its language capability. We address this from a Bayesian perspective, factorizing the policy into a language-agnostic Vision-Action (VA) prior and a language-conditioned VLA likelihood, and propose APT, a two-stage training method emphasizing Action expert PreTraining. In Stage 1, the action expert is pretrained as a VA prior on vision-action pairs from a frozen VLM, bypassing the language imbalance. In Stage 2, language tokens are injected through a gated fusion mechanism that integrates VLM features while preserving the learned visuomotor prior. APT applies to mainstream VLA architectures, including the $\pi$ and GR00T-style architectures. Comprehensive experiments validate that APT achieves consistent gains on unseen instructions and compositional tasks. Project Page: this https URL

---

## 9. PLUME: Probabilistic Latent Unified World Modeling and Parameter Estimation for Multi-Finger Manipulation

**Authors:** Abhinav Kumar, Soshi Iba, Rana Soltani Zarrin, Dmitry Berenson
**arXiv:** [2606.11396](https://arxiv.org/abs/2606.11396)
**Categories:** Robotics (cs.RO)

Dexterous manipulation with multi-finger hands can be sensitive to physical parameters such as object shape, pose, and friction coefficients. While simulation enables large-scale data collection with known parameter values, simulation-trained policies must still handle uncertainty at deployment, where the true parameters and therefore the true dynamics are unknown. Standard domain randomization strategies may be insufficient for precise tasks like screwdriver turning, as manipulation strategies may need to change depending on specific parameter values. To address this, we propose Probabilistic Latent Unified world Modeling and parameter Estimation (PLUME), a world model that jointly learns to evolve a belief over parameter values as well as the system dynamics conditioned on those parameters. We learn a latent space to jointly represent multiple qualitatively different physical parameters along with rewards, themselves functions of partially-observable variables, to inform planning. Our novel learning framework leads to efficient alignment of the world model to true dynamics through online parameter inference as opposed to re-training or fine-tuning. We evaluate our method on simulated screwdriver turning, valve turning, bucket lifting, and disk flicking tasks, as well as a hardware screwdriver turning task, where we achieve successful zero-shot transfer of our simulation-trained policy and outperform state-of-the-art offline reinforcement learning and world-model-augmented behavior cloning baselines. Please see our website at this https URL for videos.

---

## 10. Slots, Transitions, Loops: Learning Composable World Models for ARC

**Authors:** Gege Gao, Bernhard Schölkopf, Andreas Geiger
**arXiv:** [2606.12316](https://arxiv.org/abs/2606.12316)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

ARC tests in-context rule induction: given a few input-output demonstrations, a model must infer the hidden rule and apply it to a new query. While many approaches express ARC rules through language, code, or symbolic programs, ARC itself is visual-symbolic: rules appear as grid transitions over objects, colors, shapes, and spatial relations. We introduce Loop-OWM, an object-centric world-modeling architecture that learns these rules as composable transitions over structured states. It combines color-prototype slots, demonstration-conditioned task summaries, and a looped transition model with dense propagation and slot-conditioned correction. On both ARC-1 and ARC-2, Loop-OWM outperforms non-looped and looped baselines with comparable or fewer parameters. These results suggest that ARC rules can be learned not only as language descriptions or searched programs, but also as transitions over visual-symbolic world states.

---

## 11. World Model Self-Distillation: Training World Models to Solve General Tasks

**Authors:** Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan, Paolo Favaro
**arXiv:** [2606.12072](https://arxiv.org/abs/2606.12072)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Pretrained video generators are promising visual world models that exhibit emergent task-solving abilities; however, their reliance on detailed textual descriptions limits their direct use for planning and decision-making. Existing approaches either outsource this reasoning to language or vision-language models, or rely on supervised fine-tuning with paired task-execution videos, which are costly to collect and difficult to scale. We propose a scalable framework that elicits task-solving ability in such models by combining self-distillation with reinforcement learning. Given an unlabeled scene image, a vision-language model generates a candidate task and a detailed step-by-step solution. The solution conditions a pretrained video diffusion model, the Demonstrator; we distill its behavior into an Executor conditioned only on the image and a short task prompt. This transfers execution knowledge from caption-guided generation to instruction-conditioned task solving without curated task-video supervision. We further improve the Executor with reinforcement learning from VLM feedback, exploiting the asymmetry between judging whether a sampled video satisfies a task and generating the solution. Experiments on our proposed WorldTasks-Benchmark and the DreamGen robotics benchmark show that the Executor surpasses the Demonstrator under our VLM-based evaluation protocol and transfers competitively to robotic tasks.

---

## 12. Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models

**Authors:** Yifu Yuan, Yaoting Huang, Xianze Yao, ..., Han Hu, Jianye Hao
**arXiv:** [2606.11324](https://arxiv.org/abs/2606.11324)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

We introduce Embodied-R1.5, a unified Embodied Foundation Model (EFM) that integrates comprehensive embodied reasoning capabilities, spanning embodied cognition, task planning, correction, and pointing, within a single architecture toward general physical intelligence. Leveraging three automated data construction pipelines to significantly expand the data coverage of critical capabilities, we build a large-scale data system of over 15B tokens, and design a multi-task balanced RL recipe to alleviate heterogeneous task conflicts. We further introduce a Planner-Grounder-Corrector (PGC) closed-loop framework that enables a single model to autonomously execute and self-correct over long-horizon tasks. With only 8B parameters, Embodied-R1.5 achieves SOTA on 16 out of 24 embodied VLM benchmarks, surpassing leading models like Gemini-Robotics-ER-1.5 and GPT-5.4. Benefiting from the internalized embodied capabilities, Embodied-R1.5 can be fine-tuned into a VLA with only a small amount of data, outperforming leading VLA models like $\pi_{0.5}$ across 4 popular manipulation benchmark suites. We further conduct extensive zero-shot real-robot experiments, validating performance in instruction following, affordance grounding, articulated object manipulation, and long-horizon complex tasks, demonstrating strong generalization to the physical world. We open-source model weights, datasets, training code, and EmbodiedEvalKit, an evaluation framework tailored for embodied tasks, to facilitate future research in EFMs.

---

## 13. VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving

**Authors:** Jin Yao, Dhruva Dixith Kurra, Tom Lampo, ..., Danhua Guo, Burhan Yaman
**arXiv:** [2606.12396](https://arxiv.org/abs/2606.12396)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them. Existing approaches either inject features from a frozen 3D foundation model without an objective that ensures the policy uses them, or constrain geometry with sparse box and map losses that provide no dense spatial signal. We introduce VLGA, the first vision-language-action model supervised to reconstruct the dense 3D world it drives through. VLGA introduces geometry as a fourth modality alongside vision, language, and action through a dedicated expert supervised by a per-pixel pointmap regression loss against LiDAR. Extensive experiments conducted on challenging nuScenes and Bench2Drive datasets for open-loop and closed-loop evaluations, respectively, show the superiority of VLGA over counterpart VLA methods. In particular, on open-loop nuScenes, VLGA sets a new state of the art among VLA methods without ego status, with the lowest L2 (0.50\,m average) and 3-second collision rate (0.18\%). On closed-loop Bench2Drive, VLGA attains the state-of-the-art driving score of 79.08, +0.71 over the strongest prior VLA, at comparable efficiency and comfort.

---

## 14. LAST: Bridging Vision-Language and Action Manifolds via Gromov-Wasserstein Alignment

**Authors:** Huaihai Lyu, Chaofan Chen, Yuheng Ji, ..., Shanghang Zhang, Changsheng Xu
**arXiv:** [2606.11221](https://arxiv.org/abs/2606.11221)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

We take a Gromov-Wasserstein perspective on Vision-Language-Action (VLA) learning, where the goal is to make the relational geometry of action representations compatible with the semantic geometry of VL embeddings. However, this alignment is non-trivial due to the mathematical heterogeneity between the domains: the semantic space of vision-language is topologically linear and isotropic, whereas the physical manifold of robotic action is non-Euclidean and anisotropic. Their disjoint metric structures render direct regression ill-posed. To resolve this incompatibility, we introduce LAST (Lie-algebraic Action Space Tokenizer), which reconstructs the action space to establish local metric compatibility with the VL modality via a two-stage transformation: (1) Global Topological Linearization: linearizing the action manifold via Lie-algebraic mapping, converting trajectories into a fixed-length, physically additive representation. (2) Local Metric Discretization: hierarchically discretizing the representation into schemas and whitened residuals, yielding approximately isotropic local charts that are statistically aligned with the semantic metric. By resolving the structural mismatch at both global and local levels, LAST enables VLA models with superior convergence and generalizability.

---
