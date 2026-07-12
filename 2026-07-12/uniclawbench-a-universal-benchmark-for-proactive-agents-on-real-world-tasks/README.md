# UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks
**Authors:** Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang, Manyuan Zhang, Xihui Liu
**Date Published:** 2026-07-09
**Link:** http://arxiv.org/abs/2607.08768v1

---

## 🎯 Problem Statement
- Existing benchmarks struggle to evaluate proactive agents effectively due to reliance on sandboxed environments and single-turn evaluation paradigms.
- The scenario-based task taxonomies in current benchmarks mix multiple model capabilities within the same task category, making it difficult to pinpoint the root causes of agent failures.

## 🏗️ Architectural Overview & Technical Design
- UniClawBench is a capability-driven benchmark designed to evaluate proactive agents in dynamic, real-world settings.
- It evaluates agents in live Docker containers using fine-grained, step-by-step completion checkpoints instead of static, pre-recorded answers.
- The framework introduces a closed-loop evaluation strategy comprising an executor agent, a hidden supervisor agent, and a user agent to simulate realistic multi-turn human feedback without leaking grading criteria.
- It evaluates across five foundational capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination.

## 🛠️ Solution Approaches & Methodology
- The authors designed 400 bilingual real-world tasks based on the five foundational model capabilities.
- They evaluated state-of-the-art models under multiple agent frameworks to disentangle base model capabilities from framework-level design choices.
- The evaluation strategy utilizes multi-turn human feedback simulations to comprehensively assess performance in dynamic environments.
- Extensive comparisons were conducted across models and frameworks to demonstrate how base capabilities and framework designs jointly shape real-world performance.

## 🌍 Societal Impact & Sector Benefits
- This benchmark significantly improves the evaluation of AI agents, accelerating the development of reliable proactive assistants for real-world automation.
- Practical use cases include more robust software engineering tools, automated digital assistants, and complex system orchestration where understanding agent failure modes is critical.
