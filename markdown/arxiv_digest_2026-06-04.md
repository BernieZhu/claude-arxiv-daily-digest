# arXiv Daily Digest — 2026-06-04

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 11

---

## 1. MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models

**Authors:** Zhichao Yang, Yuanze Hu, Haojie Hao, ..., Yihang Lou, Yan Bai
**arXiv:** [2606.04627](https://arxiv.org/abs/2606.04627)
**Categories:** Artificial Intelligence (cs.AI)

Mobile agents are increasingly expected to operate everyday applications from screenshots and language goals, where reliable control requires reasoning over screen affordances, multi-step navigation, and future state changes. However, many agents externalize this computation as long textual chains of thought, which slows interaction, increases supervision cost, and complicates deployment. We introduce MIRAGE, a framework that learns continuous latent reasoning representations from visible textual reasoning traces. MIRAGE transfers explicit reasoning into compact hidden states, enabling the agent to reason internally without decoding long rationales. It also incorporates a generative world-model objective: latent reasoning vectors are aligned with future screenshots, encouraging the agent to anticipate upcoming interface states before acting. This turns hidden computation into both a compressed thought representation and a forward-looking model of environment dynamics. At inference time, MIRAGE reasons in continuous latent space, reducing token generation while improving execution efficiency. On AndroidWorld, MIRAGE matches explicit chain-of-thought supervised fine-tuning in the 4B ablation with a 3-5x lower decoded-token budget and improves a comparable instruction-tuned baseline by 10.2 points; on AndroidControl, it improves action grounding while generating over 75% fewer tokens.

---

## 2. VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training

**Authors:** Siyuan Yang, Linzheng Guo, Ouyang Lu, ..., Chenjia Bai, Xuelong Li
**arXiv:** [2606.04708](https://arxiv.org/abs/2606.04708)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Universal Manipulation Interface (UMI) enables scalable real-world robot data collection without hardware-specific teleoperation, yet leveraging UMI data to train large-scale Vision-Language-Action (VLA) models remains fundamentally challenging. We identify two critical mismatches: wrist-mounted fisheye views, with severe radial distortion and local gripper-centric perspectives, are out-of-distribution for pretrained VLMs; and human-collected trajectories frequently violate kinematic limits, incur collisions, or exceed controller bandwidth, teaching VLA policies physically infeasible actions. To address the challenges, we present VISTA, a framework that bridges this dual gap through three synergistic components. (i)~UMI-VQA, the first large-scale VQA dataset tailored to wrist-mounted fisheye observations, aligns VLM representations to the distorted visual regime via auxiliary vision-language supervision. (ii)~A systematic physical-validation pipeline performs a data-completeness pre-check and scores each valid trajectory for trajectory continuity, self-collision risk, and execution fidelity before it enters training. (iii)~A two-stage co-training recipe jointly learns vision-language grounding on UMI-VQA and action prediction on validated trajectories. Our experiments empirically show that incorporating UMI-VQA consistently improves downstream policy performance, and that physical-validation scores are strongly predictive of deployment success. On diverse simulation and real-world manipulation tasks, VISTA significantly outperforms strong baselines including $\pi_{0.5}$, LingBot-VLA, and Wall-X. We release the physical-validation pipeline, UMI-VQA, validated trajectory data, and the pre-trained model for the community.

---

## 3. Generalization of World Models under Environmental Variability for Vision-based Quadrotor Navigation

**Authors:** Luca Zanatta, Grzegorz Malczyk, Kostas Alexis
**arXiv:** [2606.05015](https://arxiv.org/abs/2606.05015)
**Categories:** Robotics (cs.RO)

World models, learned generative models that predict how an environment evolves, have become a promising tool for sample-efficient robot learning. Yet how robust they are to environmental variability remains poorly understood. To address this, we conduct a systematic study using vision-based quadrotor navigation as a testbed problem, training DreamerV3-based world models under varying levels of environmental randomness and evaluating them across all levels through cross-environment validation, spanning both Self-Supervised Learning (SSL) pretraining and Reinforcement Learning (RL) fine-tuning. We then deploy all world models and associated navigation policies on a real quadrotor in unseen environments, including an open-loop run where the model receives just 2.5s of real sensory input before all sensors are cut off, leaving the system to navigate entirely in imagination over a 12m traverse. Our results show that world model robustness during SSL pretraining is a strong predictor of sim-to-real transfer: every model that generalized well in cross-environment SSL validation deployed successfully in the real world, passing through gaps as narrow as 0.67m, whereas the model that dominated simulation policy evaluation failed on the real platform. We further identify (a) the discrete latent size and (b) the training-sequence length as the dominant factors governing world model quality.

---

## 4. Potential-Guided Flow Matching for Vision-Language-Action Policy Improvement

**Authors:** Yunpeng Mei, Jiakai He, Hongjie Cao, ..., Jie Chen, Gang Wang
**arXiv:** [2606.04968](https://arxiv.org/abs/2606.04968)
**Categories:** Robotics (cs.RO)

Large vision-language-action (VLA) policies are increasingly trained as conditional generative models over action chunks. Yet deployment produces mixed-quality experience-successful demonstrations, partial completions, recoverable mistakes, and failures-that is difficult to use with standard imitation. Full behavior cloning (BC) imitates failures, filtered BC discards useful sub-trajectories, and offline reinforcement learning adds a large critic. We introduce ForesightFlow, a self-guided flow-matching policy that augments each generated action chunk with a learned success-potential trajectory. The same flow proposes and scores candidate actions, enabling best-of-$K$ inference without an external critic. The key issue is that policy improvement and value calibration require different supervision: advantage weighting should emphasize high-quality actions, but applying the same weights to potential coordinates suppresses failure gradients and creates overconfident scores. We address this with decoupled advantage-weighted flow matching, applying exponentiated advantage weights only to action velocities while training potential velocities uniformly. We further derive a one-step boundary estimator for conditional flow matching, allowing advantage computation with a single stop-gradient forward pass. Across five BEHAVIOR-1K simulation tasks and five real-world bimanual tasks, ForesightFlow improves over imitation baselines, matches the strongest separate-critic baseline in simulation success, improves real-world success, and reduces training compute by $38\%$. Ablations show that decoupling prevents value hallucination, the one-step estimator preserves candidate-ranking fidelity, and self-guided sampling improves long-horizon execution.

---

## 5. WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation

**Authors:** Ning Yang, Yan Huang, Kaiwen Peng, ..., Jing Liu, Nianfeng Liu
**arXiv:** [2606.04907](https://arxiv.org/abs/2606.04907)
**Categories:** Robotics (cs.RO)

Visual navigation requires generating smooth and collision-free trajectories under complex geometric and physical constraints. Existing reactive policies that directly map observations to actions lack anticipatory reasoning, limiting their ability to proactively avoid obstacles. While visual imagination offers predictive foresight, conventional modular approaches separate scene prediction from policy learning, often leading to error accumulation and inefficient inference. To address these limitations, we propose WAM-Nav, a Latent World-Action Model for embodied visual navigation that jointly learns action generation and latent visual foresight, enabling more robust and foresighted navigation decisions without compromising inference efficiency. Specifically, WAM-Nav utilizes a shared Diffusion Transformer for asymmetric joint diffusion to concurrently generate long-horizon actions and short-horizon visual foresight, reducing the inference latency and visual error accumulation inherent in multi-step autoregressive rollouts. To further encourage smooth and consistent trajectory generation, we introduce a dual-stream contextual conditioning mechanism that integrates episode-level ego-motion history with sequential visual observations. Combined with a unified goal alignment module that preserves balanced representations across goal types, WAM-Nav naturally supports Image-Goal, Point-Goal, and No-Goal exploration within a single policy. Extensive experiments on the challenging ClutterScenes and InternScenes benchmarks demonstrate strong generalization of WAM-Nav, particularly on Image-Goal and Point-Goal navigation, where it improves success rates by 15.7% and 3.3%, respectively. Real-world deployment further validates effective zero-shot sim-to-real transfer, achieving an average 85% task success rate across diverse indoor and outdoor environments.

---

## 6. MAD: Mapping-Aware World Models for Agile Quadrotor Flight

**Authors:** Xinhong Zhang, Runqing Wang, Yunfan Ren, ..., Jie Chen, Gang Wang
**arXiv:** [2606.04534](https://arxiv.org/abs/2606.04534)
**Categories:** Robotics (cs.RO)

Agile quadrotor flight in cluttered scenes requires more than a reactive mapping from a depth image to a control command: the vehicle must remember which regions have been observed, infer nearby occupied space, and act under partial visibility and tight latency. In this paper, we present Mapping-Aware Dreamer (MAD), a geometry-aware world model for vision-based quadrotor flight. Instead of using raw-image reconstruction as the main self-supervised objective, MAD learns recurrent latent dynamics that reconstruct robocentric occupancy and visibility grid maps together with proprioceptive states. This design forces the latent state to encode local geometry, visibility history, and ego-motion in a form that is directly relevant to collision avoidance. MAD is trained in DiffAero using a GPU-parallel map-construction module that provides high-throughput supervision for occupancy and visibility. The learned representation is used in three policy-learning modes: imagination-based MAD-Dreamer and feature-extractor variants based on PPO and SHAC. Across visual navigation and racing tasks, MAD-based agents achieve higher success rates, faster flight, and better cross-task transfer than corresponding vision-only baselines. The model also produces interpretable map predictions and accurate ego-motion estimates from depth observations. We further deploy the learned policy on a physical quadrotor with an Intel RealSense D435i and demonstrate safe indoor and outdoor flight under limited sensing, reaching 9.66 m/s in simulation and 5.05 m/s in real-world forest experiments. These results show that mapping-aware world models provide a practical middle ground between modular aerial navigation and end-to-end learning.

---

## 7. OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics

**Authors:** Zhuoyuan Wu, Jun Gao
**arXiv:** [2606.04463](https://arxiv.org/abs/2606.04463)
**Categories:** Robotics (cs.RO)

We present OSCAR, a precise action-conditioned video world model that generalizes across different robot embodiments and enables robot policy evaluation. Existing video world models face three main challenges for real-world robot evaluation: limited scenario diversity in current robot training datasets, imprecise action following, and poor generalization across embodiments for broad adoption. We tackle these challenges from two perspectives. At its core is a large-scale standardized data pipeline that curates, filters, and deduplicates broad robotics and egocentric human datasets, yielding a clean joint-training dataset that spans diverse tasks, scenarios, actions, and robot embodiments. To condition the video model, we adopt 2D kinematic skeleton rendering as a unified conditioning representation that generalizes across different robot arms or even human hands. We finetune the Cosmos-Predict2.5-2B model on a single GH200 GPU. Our model achieves significant improvement on action following, appearance quality, and motion consistency, compared to existing baselines, which either have a much larger model size or require more GPUs. We further deploy OSCAR to evaluate robot policies from RoboArena. Extensive experiments demonstrate the significant correlation between our virtual policy evaluation in OSCAR and real-world evaluation, paving the way for the future where robot policies can be purely evaluated in virtual generated worlds.

---

## 8. CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization

**Authors:** Tewodros Ayalew, Matthew Jeung, Samuel Wheeler, ..., Michael Maire, Matthew R. Walter
**arXiv:** [2606.04130](https://arxiv.org/abs/2606.04130)
**Categories:** Robotics (cs.RO)

We introduce CLAW, a fully end-to-end self-supervised framework for learning a world model jointly with continuous latent action representations directly from action-free videos. Our approach leverages adversarial latent regularization and diffusion-based video generation to capture structured and semantically meaningful action representations while modeling rich, predictive environment dynamics, without relying on any action labels or annotations. By simultaneously training the Latent Action Model and world model, CLAW learns to reason about how inferred actions induce environment transitions from visual observations alone. We show that the resulting latent action world model supports both imitation learning from observation and goal-directed planning. In imitation learning, latent actions extracted from raw videos enable behavior cloning. For planning, CLAW generates sequences of latent actions and maps them to executable actions to reach desired goals. Extensive experiments across diverse tasks and embodiments demonstrate that CLAW produces semantically meaningful latent action representations, supports effective action transfer, and enables planning and imitation from observation, outperforming existing methods.

---

## 9. 3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training

**Authors:** Jiaxin Shi, Xidong Zhang, Fucai Zhu, ..., Siyu Zhu, Weihao Yuan
**arXiv:** [2606.04436](https://arxiv.org/abs/2606.04436)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Robotics (cs.RO)

We propose a 3D-thinking-guided co-training framework that enables vision-language-action (VLA) models to perform 3D spatial reasoning implicitly during action prediction. Our core insight is that 3D geometry perception and 3D spatial reasoning are distinct capabilities that can be disentangled and injected at different feature hierarchies. During training, three tightly coupled components work in concert primarily within the latent space: (1) To gain geometric priors, a latent 3D geometry perception module aligns intermediate visual features with a 3D foundation model, acquiring low-level geometric cues without architectural modifications to the VLM backbone. (2) Complementing this, an online 3D reasoning distillation module mitigates the prompt-induced reasoning gap via a shared reasoning anchor token. During 3D VLM co-training, this anchor is emitted as the first output token to robustly encode spatial priors. During VLA training, it serves as an input token inserted between the task and action instructions, transferring high-level spatial thinking from explicit teacher reasoning prompts to student action prompts without chain-of-thought text generation. (3) These disentangled geometric and reasoning features are then united by a spatially augmented action integration, which jointly injects them into the action-query tokens as hierarchical spatial conditions to prevent action shortcuts. At deployment, our method retains only its lightweight adapters to perform implicit 3D reasoning, discarding the 3D foundation model and the teacher branch used for supervision. Consequently, it operates purely on 2D images without 3D sensors, external models, or explicit text generation while preventing catastrophic forgetting of the pretrained VLM, achieving state-of-the-art performance on LIBERO, LIBERO-PLUS, SimplerEnv, and real-world manipulation tasks.

---

## 10. Dive into the Scene: Breaking the Perceptual Bottleneck in Vision-Language Decision Making via Focus Plan Generation

**Authors:** Boyuan Xiao, Bohong Chen, Yumeng Li, ..., Yao-Xiang Ding, Kun Zhou
**arXiv:** [2606.04046](https://arxiv.org/abs/2606.04046)
**Categories:** Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG); Robotics (cs.RO)

In embodied vision-language decision making tasks such as robotic manipulation and navigation, Vision-Language and Vision-Language-Action Models (VLMs & VLAs) are powerful tools with different benefits: VLMs are better at long-term planning, while VLAs are better at reactive control. However, their performance is limited by the same perceptual bottleneck: visual hallucinations arise due to the models' inability to distinguish task-relevant objects from distractors. In principle, accurate identification and focus on critical objects while filtering out irrelevant ones is the key to break this limitation. A straightforward solution is one-step focus: directly attending to essential objects. However, this approach proves ineffective because effective focus inherently requires deep scene understanding. To this end, we propose SceneDiver, a coarse-to-fine focus plan generation method for VLMs leveraging their long-term planning abilities, that first constructs a holistic scene graph to establish initial comprehension, then progressively decomposes the task into simpler sub-problems through an iterative cycle of recognition, understanding, and analysis. To enable reactive control, we also design a lightweight adapter for distilling the deliberate focus ability into VLAs. Evaluations on standard embodied AI benchmarks confirm that our method substantially reduces visual hallucinations for both VLMs and VLAs, while preserving computational efficiency in tasks requiring fast execution. Our code and data are released at: this https URL.

---

## 11. HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning

**Authors:** Amirhosein Alian, Yongqiang Zhao, Shiyi Gu, ..., Haitham Bou-Ammar, Shan Luo
**arXiv:** [2606.04825](https://arxiv.org/abs/2606.04825)
**Categories:** Robotics (cs.RO)

Despite the importance of tactile sensing for reliable manipulation, most existing Vision-Language-Action (VLA) datasets remain vision-only, and those that do incorporate tactile information typically lack the joint combination of task diversity, language conditioning, and action trajectories. Furthermore, existing teleoperation pipelines rarely provide haptic feedback to the operator, despite its established role in demonstration quality and manipulation stability. In this work, we present HapTile, a contact-grounded visuotactile manipulation dataset that advances beyond vision-only trajectory datasets by embedding physical interaction sensing at two levels: fingertip tactile feedback at the robot end-effector, and haptic-informed demonstrations at the teleoperator side. The data collection platform integrates haptic feedback directly into the teleoperation controller, enabling the operator to perceive contact interactions in real time. It is built around a standard and reproducible robotic system equipped with custom-designed fingertip tactile sensors. The dataset comprises everyday manipulation tasks spanning a broad range of contact-rich skills, including pick-and-place, folding, pressing, stacking, and other routine activities. Each task is paired with language instructions that condition the policy on the manipulation objective, together with synchronized visuotactile observations and action trajectories. In addition, we provide a benchmarking study on contact-rich policy learning using two baseline models to evaluate the effectiveness of the proposed contact-grounded dataset. The dataset and additional details are available on our website: this http URL.

---
