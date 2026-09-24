# Proxifield: Decentralized Multi-Agent Communication through Semantic Proximity
**Authors:** Pradyumna Tambwekar, Yenchia Feng, Deep Patel, Karime Maamari
**Date Published:** 2026-09-16
**Link:** http://arxiv.org/abs/2609.20889v1

---

## 🎯 Problem Statement
- As LLM capabilities have expanded, multi-agent communication has emerged as an increasingly active area of research.
- Prevailing protocols often adopt rigid structures that introduce coordination bottlenecks and can degrade as the number of agents increases.

## 🏗️ Architectural Overview & Technical Design
- Prevailing protocols often adopt rigid structures that introduce coordination bottlenecks and can degrade as the number of agents increases.
- We introduce Proxifield, a round-adaptive multi-agent protocol with decentralized agent decision-making that constructs sparse communication graphs from the evolving semantic proximity of agents.
- Without model training or a centralized planner, Proxifield connects agents using four routing signals derived at inference time: direct address, information needs, plan alignment, and information complementarity.

## 🛠️ Solution Approaches & Methodology
- We compare Proxifield with two representative coordination baselines, a centralized Star protocol and a decentralized Shared Context protocol, across two domains: Drone Search and Rescue and the collective-reasoning benchmark HiddenBench.
- We first ablate base-model capability and find that, in both domains, the performance of Proxifield improves with model size (35B -> 397B parameter model) and Proxifield outperforms all baselines at the largest scale.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.

---
