# arXiv Daily Digest — 2026-04-20

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 3

---

## 1. AEGIS: Anchor-Enforced Gradient Isolation for Knowledge-Preserving Vision-Language-Action Fine-Tuning

**Authors:** Guransh Singh
**arXiv:** [2604.16067](https://arxiv.org/abs/2604.16067)
**Categories:** Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV)

Adapting pre-trained vision-language models (VLMs) for robotic control requires injecting high-magnitude continuous gradients from a flow-matching action expert into a backbone trained exclusively with cross-entropy. This cross-modal gradient asymmetry - the spectral dimensionality mismatch between low-rank MSE regression gradients and the high-dimensional semantic manifold sculpted by CE pre-training, causes rapid, severe erosion of the VLM's visual-question-answering (VQA) capability. Industry-standard defences either sever the gradient pathway entirely via stop gradient, discarding the rich continuous supervision, or restrict parameter capacity through low-rank adapters (LoRA) that constrain the rank of updates but not their direction, and thus still overwrite the pre-trained manifold. We introduce AEGIS (Anchor-Enforced Gradient Isolation System): a buffer-free, layer-wise orthogonal gradient projection framework that enables direct continuous MSE learning while preserving the pre-trained VQA manifold - without any co-training data or replay buffer. AEGIS pre-computes a static Gaussian reference anchor from masked VQA forward passes across all transformer layers, then at each training step constructs a Wasserstein-2 transport penalty that generates an anchor restoration gradient. A sequential dual-backward decomposes the task and anchor gradients; for each transformer layer, AEGIS applies a single Gram-Schmidt orthogonal projection that bends the task gradient away from the destructive direction while preserving its constructive content. The projection sheds less than 1% of gradient energy on average, yet eliminates the cumulative activation drift that drives severe forgetting.

---

## 2. Long-Term Memory for VLA-based Agents in Open-World Task Execution

**Authors:** Xu Huang, Weixin Mao, Yinhao Li, Hua Chen, Jiabao Zhao
**arXiv:** [2604.15671](https://arxiv.org/abs/2604.15671)
**Categories:** Robotics (cs.RO)

Vision-Language-Action (VLA) models have demonstrated significant potential for embodied decision-making; however, their application in complex chemical laboratory automation remains restricted by limited long-horizon reasoning and the absence of persistent experience accumulation. Existing frameworks typically treat planning and execution as decoupled processes, often failing to consolidate successful strategies, which results in inefficient trial-and-error in multi-stage protocols. In this paper, we propose ChemBot, a dual-layer, closed-loop framework that integrates an autonomous AI agent with a progress-aware VLA model (Skill-VLA) for hierarchical task decomposition and execution. ChemBot utilizes a dual-layer memory architecture to consolidate successful trajectories into retrievable assets, while a Model Context Protocol (MCP) server facilitates efficient sub-agent and tool orchestration. To address the inherent limitations of VLA models, we further implement a future-state-based asynchronous inference mechanism to mitigate trajectory discontinuities. Extensive experiments on collaborative robots demonstrate that ChemBot achieves superior operational safety, precision, and task success rates compared to existing VLA baselines in complex, long-horizon chemical experimentation.

---

## 3. Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions

**Authors:** Aggelos Psiris, Vasileios Argyriou, Evangelos K. Markakis, ..., Kostas Bekris, Arash Ajoudani adn Georgios Th. Papadopoulos
**arXiv:** [2604.15395](https://arxiv.org/abs/2604.15395)
**Categories:** Robotics (cs.RO)

Over the recent years, the field of robotics has been undergoing a transformative paradigm shift from fixed, single-task, domain-specific solutions towards adaptive, multi-function, general-purpose agents, capable of operating in complex, open-world, and dynamic environments. This tremendous advancement is primarily driven by the emergence of Foundation Models (FMs), i.e., large-scale neural-network architectures trained on massive, heterogeneous datasets that provide unprecedented capabilities in multi-modal understanding and reasoning, long-horizon planning, and cross-embodiment generalization. In this context, the current study provides a holistic, systematic, and in-depth review of the research landscape of FMs in robotics. In particular, the evolution of the field is initially delineated through five distinct research phases, spanning from the early incorporation of Natural Language Processing (NLP) and Computer Vision (CV) models to the current frontier of multi-sensory generalization and real-world deployment. Subsequently, a highly-granular taxonomic investigation of the literature is performed, examining the following key aspects: a) the employed FM types, including LLMs, VFMs, VLMs, and VLAs, b) the underlying neural-network architectures, c) the adopted learning paradigms, d) the different learning stages of knowledge incorporation, e) the major robotic tasks, and f) the main real-world application domains. For each aspect, comparative analysis and critical insights are provided. Moreover, a report on the publicly available datasets used for model training and evaluation across the considered robotic tasks is included. Furthermore, a hierarchical discussion on the current open challenges and promising future research directions in the field is incorporated.

---
