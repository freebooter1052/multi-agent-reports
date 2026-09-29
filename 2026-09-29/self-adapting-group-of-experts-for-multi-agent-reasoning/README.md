# Self-Adapting Group of Experts for Multi-Agent Reasoning
**Authors:** Mohammad Atif Quamar, Nurbek Tastan, Karthik Nandakumar, Junpei Komiyama
**Date Published:** 2026-09-28
**Link:** http://arxiv.org/abs/2609.35412v1

---

## 🎯 Problem Statement
- Existing frameworks often adapt communication by changing this context while leaving individual prompts fixed, even when a problem calls for different skills.
- We study whether agents' initial responses can identify a strategy better suited to the current problem and guide its transfer to other agents.
- This transfer uses only the agents' original system prompts, without access to the problem or generated solutions.

## 🏗️ Architectural Overview & Technical Design
- Multi-agent systems bring together language model agents with different roles to propose, review, and refine solutions.
- Each agent's response depends on its model's capabilities, the reasoning strategy defined by its system prompt, and the information in its input context.
- Existing frameworks often adapt communication by changing this context while leaving individual prompts fixed, even when a problem calls for different skills.

## 🛠️ Solution Approaches & Methodology
- Experiments across multiple agent backbones and reasoning benchmarks show that SAGE achieves higher average accuracy than the evaluated baselines.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.


---
