# Theory of Scene: Breaking the Symmetry Trap in Multi-Agent LLM Coordination
**Authors:** Liangqi Yuan, Wenzhi Fang, Shiqiang Wang, Christopher G. Brinton
**Date Published:** 2026-09-26
**Link:** http://arxiv.org/abs/2609.32939v1

---

## 🎯 Problem Statement
- Multi-agent systems built on large language models (LLMs) are largely homogeneous, as their agents behave alike even across distinct LLMs.
- We show that when such agents act concurrently without communication, they collide on targets they must split and diverge on targets they must take together, a double failure we term the symmetry trap.

## 🏗️ Architectural Overview & Technical Design
- Multi-agent systems built on large language models (LLMs) are largely homogeneous, as their agents behave alike even across distinct LLMs.
- We propose Theory of Scene (ToS), a training-free reasoning schema in which each agent reads its public role, the only difference between the agents, and the task context they all observe.
- We evaluate on DivvyBench, a controlled environment we introduce, whose target types make an episode Competitive, Cooperative, or Mixed across Tabletop, Airspace, and Household scenarios, and on two established agentic benchmarks, GovSim and Overcooked.

## 🛠️ Solution Approaches & Methodology
- We evaluate on DivvyBench, a controlled environment we introduce, whose target types make an episode Competitive, Cooperative, or Mixed across Tabletop, Airspace, and Household scenarios, and on two established agentic benchmarks, GovSim and Overcooked.
- ToS outperforms all six baselines on every benchmark, and each baseline falls far behind it in at least one setting.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.


---
