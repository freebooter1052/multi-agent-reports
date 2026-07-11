# UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks
**Authors:** Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang, Manyuan Zhang, Xihui Liu
**Date Published:** 2026-07-09
**Link:** http://arxiv.org/abs/2607.08768v1

---

## 🎯 Problem Statement
- The rapid development of large language models and multimodal large language models has led to proactive agents that can operate everyday tools and assist users in real-world environments. However, existing benchmarks struggle to evaluate these agents effectively because they rely on sandboxed environments and single-turn evaluation paradigms.
- Furthermore, current scenario-based task taxonomies mix multiple model capabilities within the same task category, which makes it incredibly difficult to identify the root causes of an agent's failure. This gap necessitates a more robust, capability-driven benchmark for dynamic, real-world settings.

## 🏗️ Architectural Overview & Technical Design
- UniClawBench is a capability-driven benchmark built around five foundational model capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination.
- The system evaluates agents in live Docker containers instead of relying on static, pre-recorded answers. Data flows from the agent's actions into a live container where fine-grained, step-by-step completion checkpoints track progress.
- The evaluation architecture comprises an executor agent, a hidden supervisor agent, and a user agent, working together in a closed-loop strategy to simulate realistic multi-turn human feedback without leaking grading criteria.

## 🛠️ Solution Approaches & Methodology
- The researchers designed 400 bilingual real-world tasks based on the five foundational model capabilities.
- They evaluated state-of-the-art models under multiple agent frameworks to disentangle base model capabilities from framework-level design choices.
- The evaluation methodology uses live Docker containers and a closed-loop multi-agent evaluation strategy to safely and dynamically grade the agents based on fine-grained completion checkpoints, allowing comprehensive comparisons across models and frameworks.

## 🌍 Societal Impact & Sector Benefits
- By providing a robust, real-world benchmark for proactive AI agents, this research benefits the software development and AI engineering sectors by enabling more reliable and capable automated assistants.
- Practical use cases include improving AI-driven customer support bots, automated data analysis tools, and complex workflow automation systems that require reliable cross-platform coordination and multi-turn reasoning in dynamic environments.
