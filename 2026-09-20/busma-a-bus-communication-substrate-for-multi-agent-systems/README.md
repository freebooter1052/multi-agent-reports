# BusMA: A Bus Communication Substrate for Multi-Agent Systems
**Authors:** Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
**Date Published:** 2026-09-14
**Link:** http://arxiv.org/abs/2609.15054v1

---

## 🎯 Problem Statement
- However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors.
- We introduce four intents: discussion, challenge, guidance, and request for explanation, which support fine-grained communication among agents.

## 🏗️ Architectural Overview & Technical Design
- Existing systems typically adopt Hierarchical Manager-Worker (HMW) or Router-based Message Passing (RMP) structures as their communication protocol.
- However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors.
- Inspired by bus architectures in computer systems, we propose BusMA, a communication framework that allows any agent to address other agents through a shared channel, i.e., the Bus.

## 🛠️ Solution Approaches & Methodology
- To evaluate the effectiveness of BusMA, we conduct extensive experiments with two frontier LLMs across 13 tasks spanning visual reasoning, mathematical reasoning, and knowledge retrieval demonstrate that BusMA consistently outperforms state-of-the-art HMW and RMP methods..

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.
