# arXiv Daily Digest — 2026-04-09

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 3

---

## 1. Telecom World Models: Unifying Digital Twins, Foundation Models, and Predictive Planning for 6G

**Authors:** Hang Zou, Yuzhi Yang, Lina Bariah, ..., Mehdi Bennis, Mérouane Debbah
**arXiv:** [2604.06882](https://arxiv.org/abs/2604.06882)
**Categories:** Robotics (cs.RO); Signal Processing (eess.SP); Systems and Control (eess.SY)

The integration of machine learning tools into telecom networks, has led to two prevailing paradigms, namely, language-based systems, such as Large Language Models (LLMs), and physics-based systems, such as Digital Twins (DTs). While LLM-based approaches enable flexible interaction and automation, they lack explicit representations of network dynamics. DTs, in contrast, offer a high-fidelity network simulation, but remain scenario-specific and are not designed for learning or decision-making under uncertainty. This gap becomes critical for 6G systems, where decisions must take into account the evolving network states, uncertainty, and the cascading effects of control actions across multiple layers. In this article, we introduce the {Telecom World Model}~(TWM) concept, an architecture for learned, action-conditioned, uncertainty-aware modeling of telecom system dynamics. We decompose the problem into two interacting worlds, a controllable system world consisting of operator-configurable settings and an external world that captures propagation, mobility, traffic, and failures. We propose a three-layer architecture, comprising a field world model for spatial environment prediction, a control/dynamics world model for action-conditioned Key Performance Indicator (KPI) trajectory prediction, and a telecom foundation model layer for intent translation and orchestration. We showcase a comparative analysis between existing paradigms, which demonstrates that TWM jointly provides telecom state grounding, fast action-conditioned roll-outs, calibrated uncertainty, multi-timescale dynamics, model-based planning, and LLM-integrated guardrails. Furthermore, we present a proof-of-concept on network slicing to validate the proposed architecture, showing that the full three-layer pipeline outperforms single-world baselines and accurately predicts KPI trajectories.

---

## 2. INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling

**Authors:** InSpatio Team, Donghui Shen, Guofeng Zhang, ..., Zhichao Ye, Ziqiang Zhao
**arXiv:** [2604.07209](https://arxiv.org/abs/2604.07209)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Building world models with spatial consistency and real-time interactivity remains a fundamental challenge in computer vision. Current video generation paradigms often struggle with a lack of spatial persistence and insufficient visual realism, making it difficult to support seamless navigation in complex environments. To address these challenges, we propose INSPATIO-WORLD, a novel real-time framework capable of recovering and generating high-fidelity, dynamic interactive scenes from a single reference video. At the core of our approach is a Spatiotemporal Autoregressive (STAR) architecture, which enables consistent and controllable scene evolution through two tightly coupled components: Implicit Spatiotemporal Cache aggregates reference and historical observations into a latent world representation, ensuring global consistency during long-horizon navigation; Explicit Spatial Constraint Module enforces geometric structure and translates user interactions into precise and physically plausible camera trajectories. Furthermore, we introduce Joint Distribution Matching Distillation (JDMD). By using real-world data distributions as a regularizing guide, JDMD effectively overcomes the fidelity degradation typically caused by over-reliance on synthetic data. Extensive experiments demonstrate that INSPATIO-WORLD significantly outperforms existing state-of-the-art (SOTA) models in spatial consistency and interaction precision, ranking first among real-time interactive methods on the WorldScore-Dynamic benchmark, and establishing a practical pipeline for navigating 4D environments reconstructed from monocular videos.

---

## 3. Evolution of Video Generative Foundations

**Authors:** Teng Hu, Jiangning Zhang, Hongrui Huang, ..., Ming-Hsuan Yang, Dacheng Tao
**arXiv:** [2604.06339](https://arxiv.org/abs/2604.06339)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

The rapid advancement of Artificial Intelligence Generated Content (AIGC) has revolutionized video generation, enabling systems ranging from proprietary pioneers like OpenAI's Sora, Google's Veo3, and Bytedance's Seedance to powerful open-source contenders like Wan and HunyuanVideo to synthesize temporally coherent and semantically rich videos. These advancements pave the way for building "world models" that simulate real-world dynamics, with applications spanning entertainment, education, and virtual reality. However, existing reviews on video generation often focus on narrow technical fields, e.g., Generative Adversarial Networks (GAN) and diffusion models, or specific tasks (e. g., video editing), lacking a comprehensive perspective on the field's evolution, especially regarding Auto-Regressive (AR) models and integration of multimodal information. To address these gaps, this survey firstly provides a systematic review of the development of video generation technology, tracing its evolution from early GANs to dominant diffusion models, and further to emerging AR-based and multimodal techniques. We conduct an in-depth analysis of the foundational principles, key advancements, and comparative strengths/limitations. Then, we explore emerging trends in multimodal video generation, emphasizing the integration of diverse data types to enhance contextual awareness. Finally, by bridging historical developments and contemporary innovations, this survey offers insights to guide future research in video generation and its applications, including virtual/augmented reality, personalized education, autonomous driving simulations, digital entertainment, and advanced world models, in this rapidly evolving field. For more details, please refer to the project at this https URL.

---
