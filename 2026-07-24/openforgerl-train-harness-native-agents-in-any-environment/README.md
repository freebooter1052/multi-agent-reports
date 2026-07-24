# OpenForgeRL: Train Harness-native Agents in Any Environment
**Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao
**Date Published:** 2026-07-23
**Link:** http://arxiv.org/abs/2607.21557v1

---

## 🎯 Problem Statement
- Modern AI agents use complex tools and setups (like Claude Code or Codex) to reason and act, but these complex setups make it hard to train the agents from start to finish using standard open-source tools.
- This is a difficult problem because existing training systems (like RL frameworks) cannot easily handle these complex, multi-step actions without special integration.

## 🏗️ Architectural Overview & Technical Design
- The authors introduce OpenForgeRL, an open-source framework designed to train these complex agents directly in diverse environments.
- Data flows from the agent's actions through a lightweight proxy that records the steps, while a Kubernetes orchestrator runs each training session in its own separate remote container.
- It leverages standard Reinforcement Learning (RL) codebases (such as veRL) and containerization to manage large-scale training efficiently.

## 🛠️ Solution Approaches & Methodology
- The researchers decoupled the training process from the actual running of the agent (inference). They built a proxy to handle model calls and record them as training data.
- They trained and evaluated the agents across different scenarios, including tool-using agents and agents that browse the web or use computer interfaces.
- The approach was tested on benchmarks like ClawEval, QwenClawBench, OSWorld-Verified, and WebVoyager, showing that OpenForgeRL models outperformed similar-sized open baselines.

## 🌍 Societal Impact & Sector Benefits
- By making it easier to train complex AI agents using open-source tools, this research democratizes advanced AI development for researchers and developers globally.
- Practical use cases include creating more reliable automated assistants for web browsing, data analysis, and software development, which can boost productivity across various tech industries.
