# Agensh: Scaling Organizational Intelligence to 1,024 Agents
**Authors:** Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei
**Date Published:** 2026-09-22
**Link:** http://arxiv.org/abs/2609.26781v1

---

## 🎯 Problem Statement
- However, the scalability of current multi-agent harnesses is often constrained by a central orchestrator's capacity to allocate tasks and coordinate workers.

## 🏗️ Architectural Overview & Technical Design
- Several pioneering harness frameworks support multi-agent systems.
- To address this limitation, we introduce Agensh, a scalable self-organized multi-agent harness without a central orchestrator: concurrent workers execute a multi-agent cooperation loop, continuously gathering context, claiming and self-assigning sub-tasks, taking action and sharing findings, verifying results, and merging progress in an asynchronous manner.
- The loop is supported by the agentic organization infrastructure comprising three components: a shared workspace holds proposed, ongoing, and completed work; a message interface lets workers communicate; and shared context retains reusable findings and work intentions.

## 🛠️ Solution Approaches & Methodology
- To test the scalability of Agensh, we evaluate it on the five hardest ProgramBench tasks with GPT-5.6-sol (high).
- Scaling from 1 to 128 agents raises the mean final test-pass rate from 19.31% to 28.78%, an approximately 49% relative improvement.
- Larger organizations reach comparable test-pass rates earlier.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.

---
