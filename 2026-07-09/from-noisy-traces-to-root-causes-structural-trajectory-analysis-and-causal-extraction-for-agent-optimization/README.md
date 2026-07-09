# From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization
**Authors:** Ying Chang, Jiahang Xu, Xuan Feng, Chenyuan Yang, Peng Cheng, Yuqing Yang
**Date Published:** 2026-07-08
**Link:** http://arxiv.org/abs/2607.07702v1

---

## 🎯 Problem Statement
- What is the core challenge, flaw, or gap in existing research that this paper is trying to solve?
The optimization of long-horizon autonomous agents increasingly relies on reflection-based mechanisms where an LLM acts as an optimizer to diagnose failures from execution traces. However, real execution traces are redundant and heterogeneous, causing overfitting to low-value failures. Furthermore, individual trajectories contain irrelevant steps, and naive context reduction methods (like truncation) discard causally important evidence, leading to misleading optimization signals.
- Why is this problem difficult or important?
It is difficult because identifying the true root cause of an agent's failure from a long, noisy sequence of actions requires isolating relevant causal links without losing essential context. It is important because accurate diagnosis is required to properly update the agent's policy; without it, the optimization process is inefficient and ineffective.

## 🏗️ Architectural Overview & Technical Design
- Provide a detailed breakdown of the system architecture, framework, or mathematical model introduced.
The authors introduce **STRACE (Structural TRajectory Analysis and Causal Extraction)**, a framework designed to construct high signal-to-noise optimization contexts for agent optimization.
- Describe how data flows through this system (input to output).
At the batch level, STRACE takes in a large collection of execution traces and mines failure patterns to filter redundant traces, retaining only representative failures. Within each selected trace, it parses the trajectory into a textual dependency graph. It then performs causal localization over this graph to remove non-causal steps and identify the exact root-cause module responsible for the failure, which is finally sent to the LLM optimizer for policy improvement.
- Mention any specific technologies, neural network layers, or algorithms leveraged.
STRACE leverages textual dependency graph construction, causal extraction algorithms, and LLM-based reflection and optimization mechanisms.

## 🛠️ Solution Approaches & Methodology
- What is the exact step-by-step methodology the authors used to implement their solution?
They developed a two-level filtering approach: first, batch-level mining of failure patterns to discard repetitive or noisy traces; second, instance-level causal localization within the retained traces using a textual dependency graph. The purified context highlighting the root cause is then fed into the LLM optimizer to refine the agent's prompt or policy.
- How did they train, test, or evaluate their approach? (Include key metrics or benchmarks used).
They evaluated STRACE against standard context-filtering baselines. On a challenging formal verification task (VeruSAGE-Bench), STRACE successfully optimized agents designed by human experts, improving the success rate by 1.4× (increasing it from 42.5% to 58.5%).

## 🌍 Societal Impact & Sector Benefits
- How does this research benefit society or its specialized industry sector?
By dramatically improving the efficiency and accuracy of self-optimizing AI agents, this research accelerates the development of reliable autonomous systems across various sectors, such as software engineering, data analysis, and robotics. It reduces the computational cost and time required to debug and improve complex AI workflows.
- What are the practical, real-world use cases or downstream applications of this work?
Practical applications include automated software testing and debugging, robust autonomous customer service agents, and complex long-horizon planning tasks in robotics and supply chain management, where identifying exactly why an automated plan failed is critical for continuous improvement.
