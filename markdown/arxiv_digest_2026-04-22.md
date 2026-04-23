# arXiv Daily Digest — 2026-04-22

**Mode:** direct
**Categories:** cs.AI, cs.LG, cs.RO, cs.CV
**Keywords:** VLA, world model, world action model
**Papers found:** 8

---

## 1. UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling

**Authors:** Boyu Chen, Yi Chen, Lu Qiu, ..., Yuying Ge, Yixiao Ge
**arXiv:** [2604.19734](https://arxiv.org/abs/2604.19734)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Scaling humanoid foundation models is bottlenecked by the scarcity of robotic data. While massive egocentric human data offers a scalable alternative, bridging the cross-embodiment chasm remains a fundamental challenge due to kinematic mismatches. We introduce UniT (Unified Latent Action Tokenizer via Visual Anchoring), a framework that establishes a unified physical language for human-to-humanoid transfer. Grounded in the philosophy that heterogeneous kinematics share universal visual consequences, UniT employs a tri-branch cross-reconstruction mechanism: actions predict vision to anchor kinematics to physical outcomes, while vision reconstructs actions to filter out irrelevant visual confounders. Concurrently, a fusion branch synergies these purified modalities into a shared discrete latent space of embodiment-agnostic physical intents. We validate UniT across two paradigms: 1) Policy Learning (VLA-UniT): By predicting these unified tokens, it effectively leverages diverse human data to achieve state-of-the-art data efficiency and robust out-of-distribution (OOD) generalization on both humanoid simulation benchmark and real-world deployments, notably demonstrating zero-shot task transfer. 2) World Modeling (WM-UniT): By aligning cross-embodiment dynamics via unified tokens as conditions, it realizes direct human-to-humanoid action transfer. This alignment ensures that human data seamlessly translates into enhanced action controllability for humanoid video generation. Ultimately, by inducing a highly aligned cross-embodiment representation (empirically verified by t-SNE visualizations revealing the convergence of human and humanoid features into a shared manifold), UniT offers a scalable path to distill vast human knowledge into general-purpose humanoid capabilities.

---

## 2. VLA Foundry: A Unified Framework for Training Vision-Language-Action Models

**Authors:** Jean Mercat, Sedrick Keh, Kushal Arora, ..., Shun Iwase, Katherine Liu
**arXiv:** [2604.19728](https://arxiv.org/abs/2604.19728)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG); Software Engineering (cs.SE)

We present VLA Foundry, an open-source framework that unifies LLM, VLM, and VLA training in a single codebase. Most open-source VLA efforts specialize on the action training stage, often stitching together incompatible pretraining pipelines. VLA Foundry instead provides a shared training stack with end-to-end control, from language pretraining to action-expert fine-tuning. VLA Foundry supports both from-scratch training and pretrained backbones from Hugging Face. To demonstrate the utility of our framework, we train and release two types of models: the first trained fully from scratch through our LLM-->VLM-->VLA pipeline and the second built on the pretrained Qwen3-VL backbone. We evaluate closed-loop policy performance of both models on LBM Eval, an open-data, open-source simulator. We also contribute usability improvements to the simulator and the STEP analysis tools for easier public use. In the nominal evaluation setting, our fully-open from-scratch model is on par with our prior closed-source work and substituting in the Qwen3-VL backbone leads to a strong multi-task table top manipulation policy outperforming our baseline by a wide margin. The VLA Foundry codebase is available at this https URL and all multi-task model weights are released on this https URL. Additional qualitative videos are available on the project website this https URL.

---

## 3. Safety-Critical Contextual Control via Online Riemannian Optimization with World Models

**Authors:** Tongxin Li
**arXiv:** [2604.19639](https://arxiv.org/abs/2604.19639)
**Categories:** Systems and Control (eess.SY); Artificial Intelligence (cs.AI)

Modern world models are becoming too complex to admit explicit dynamical descriptions. We study safety-critical contextual control, where a Planner must optimize a task objective using only feasibility samples from a black-box Simulator, conditioned on a context signal $\xi_t$. We develop a sample-based Penalized Predictive Control (PPC) framework grounded in online Riemannian optimization, in which the Simulator compresses the feasibility manifold into a score-based density $\hat{p}(u \mid \xi_t)$ that endows the action space with a Riemannian geometry guiding the Planner's gradient descent. The barrier curvature $\kappa(\xi_t)$, the minimum curvature of the conditional log-density $-\ln\hat{p}(\cdot\mid\xi_t)$, governs both convergence rate and safety margin, replacing the Lipschitz constant of the unknown dynamics. Our main result is a contextual safety bound showing that the distance from the true feasibility manifold is controlled by the score estimation error and a ratio that depends on $\kappa(\xi_t)$, both of which improve with richer context. Simulations on a dynamic navigation task confirm that contextual PPC substantially outperforms marginal and frozen density models, with the advantage growing after environment shifts.

---

## 4. RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation

**Authors:** Feng Jiang, Yang Chen, Kyle Xu, ..., Chen Xie, Ruihai Wu
**arXiv:** [2604.19092](https://arxiv.org/abs/2604.19092)
**Categories:** Robotics (cs.RO); Artificial Intelligence (cs.AI)

Recent advances in large-scale video world models have enabled increasingly realistic future prediction, raising the prospect of leveraging imagined videos for robot learning. However, visual realism does not imply physical plausibility, and behaviors inferred from generated videos may violate dynamics and fail when executed by embodied agents. Existing benchmarks begin to incorporate notions of physical plausibility, but they largely remain perception- or diagnostic-oriented and do not systematically evaluate whether predicted behaviors can be translated into executable actions that complete the intended task. To address this gap, we introduce RoboWM-Bench, a manipulation-centric benchmark for embodiment-grounded evaluation of video world models. RoboWM-Bench converts generated behaviors from both human-hand and robotic manipulation videos into embodied action sequences and validates them through robotic execution. The benchmark spans diverse manipulation scenarios and establishes a unified protocol for consistent and reproducible evaluation. Using RoboWM-Bench, we evaluate state-of-the-art video world models and find that reliably generating physically executable behaviors remains an open challenge. Common failure modes include errors in spatial reasoning, unstable contact prediction, and non-physical deformations. While finetuning on manipulation data yields improvements, physical inconsistencies still persist, suggesting opportunities for more physically grounded video generation for robots.

---

## 5. HELM: Harness-Enhanced Long-horizon Memory for Vision-Language-Action Manipulation

**Authors:** Zijian Zeng, Fei Ding, Huiming Yang, Xianwei Li
**arXiv:** [2604.18791](https://arxiv.org/abs/2604.18791)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

Vision-Language-Action (VLA) models fail systematically on long-horizon manipulation tasks despite strong short-horizon performance. We show that this failure is not resolved by extending context length alone in the current reactive execution setting; instead, it stems from three recurring execution-loop deficiencies: the memory gap, the verification gap, and the recovery gap. We present HELM, a model-agnostic framework that addresses these deficiencies with three components: an Episodic Memory Module (EMM) that retrieves key task history via CLIP-indexed keyframes, a learned State Verifier (SV) that predicts action failure before execution from observation, action, subgoal, and memory-conditioned context, and a Harness Controller (HC) that performs rollback and replanning. The SV is the core learning contribution: it consistently outperforms rule-based feasibility checks and ensemble uncertainty baselines, and its effectiveness depends critically on access to episodic memory. On LIBERO-LONG, HELM improves task success rate by 23.1 percentage points over OpenVLA (58.4% to 81.5%), while extending the context window to H=32 yields only a 5.4-point gain and same-budget LoRA adaptation remains 12.2 points below HELM. HELM also improves long-horizon performance on CALVIN and substantially boosts recovery success under controlled perturbations. Ablations and mechanism analyses isolate the contribution of each component, and we release LIBERO-Recovery as a perturbation-injection protocol for evaluating failure recovery in long-horizon manipulation.

---

## 6. Curiosity-Critic: Cumulative Prediction Error Improvement as a Tractable Intrinsic Reward for World Model Training

**Authors:** Vin Bhaskara, Haicheng Wang
**arXiv:** [2604.18701](https://arxiv.org/abs/2604.18701)
**Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Machine Learning (stat.ML)

Local prediction-error-based curiosity rewards focus on the current transition without considering the world model's cumulative prediction error across all visited transitions. We introduce Curiosity-Critic, which grounds its intrinsic reward in the improvement of this cumulative objective, and show that it reduces to a tractable per-step form: the difference between the current prediction error and the asymptotic error baseline of the current state transition. We estimate this baseline online with a learned critic co-trained alongside the world model; regressing a single scalar, the critic converges well before the world model saturates, redirecting exploration toward learnable transitions without oracle knowledge of the noise floor. The reward is higher for learnable transitions and collapses toward the baseline for stochastic ones, effectively separating epistemic (reducible) from aleatoric (irreducible) prediction error online. Prior prediction-error curiosity formulations, from Schmidhuber (1991) to learned-feature-space variants, emerge as special cases corresponding to specific approximations of this baseline. Experiments on a stochastic grid world show that Curiosity-Critic outperforms prediction-error and visitation-count baselines in convergence speed and final world model accuracy.

---

## 7. Mask World Model: Predicting What Matters for Robust Robot Policy Learning

**Authors:** Yunfan Lou, Xiaowei Chi, Xiaojie Zhang, ..., Pengwei Wang, Shanghang Zhang
**arXiv:** [2604.19683](https://arxiv.org/abs/2604.19683)
**Categories:** Robotics (cs.RO)

World models derived from large-scale video generative pre-training have emerged as a promising paradigm for generalist robot policy learning. However, standard approaches often focus on high-fidelity RGB video prediction, this can result in overfitting to irrelevant factors, such as dynamic backgrounds and illumination changes. These distractions reduce the model's ability to generalize, ultimately leading to unreliable and fragile control policies. To address this, we introduce the Mask World Model (MWM), which leverages video diffusion architectures to predict the evolution of semantic masks instead of pixels. This shift imposes a geometric information bottleneck, forcing the model to capture essential physical dynamics and contact relations while filtering out visual noise. We seamlessly integrate this mask dynamics backbone with a diffusion-based policy head to enable robust end-to-end control. Extensive evaluations demonstrate the superiority of MWM on the LIBERO and RLBench simulation benchmarks, significantly outperforming the state-of-the-art RGB-based world models. Furthermore, real-world experiments and robustness evaluation (via random token pruning) reveal that MWM exhibits superior generalization capabilities and robust resilience to texture information loss.

---

## 8. SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model

**Authors:** Zewei Zhou, Ruining Yang, Xuewei, ..., Lili Su, Jiaqi Ma
**arXiv:** [2604.19710](https://arxiv.org/abs/2604.19710)
**Categories:** Computer Vision and Pattern Recognition (cs.CV)

Vision-Language-Action (VLA) models offer a promising autonomous driving paradigm for leveraging world knowledge and reasoning capabilities, especially in long-tail scenarios. However, existing VLA models often struggle with the high latency in action generation using an autoregressive generation framework and exhibit limited robustness. In this paper, we propose SpanVLA, a novel end-to-end autonomous driving framework, integrating an autoregressive reasoning and a flow-matching action expert. First, SpanVLA introduces an efficient bridge to leverage the vision and reasoning guidance of VLM to efficiently plan future trajectories using a flow-matching policy conditioned on historical trajectory initialization, which significantly reduces inference time. Second, to further improve the performance and robustness of the SpanVLA model, we propose a GRPO-based post-training method to enable the VLA model not only to learn from positive driving samples but also to learn how to avoid the typical negative behaviors and learn recovery behaviors. We further introduce mReasoning, a new real-world driving reasoning dataset, focusing on complex, reasoning-demanding scenarios and negative-recovery samples. Extensive experiments on the NAVSIM (v1 and v2) demonstrate the competitive performance of the SpanVLA model. Additionally, the qualitative results across diverse scenarios highlight the planning performance and robustness of our model.

---
