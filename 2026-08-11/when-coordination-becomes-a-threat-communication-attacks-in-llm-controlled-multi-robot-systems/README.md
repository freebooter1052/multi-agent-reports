# When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems
**Authors:** Zhen Huang, Zhihuang Liu, Weijia Shi, Yifan Yang, Weishang Wu, Zhiping Cai
**Date Published:** 2026-08-07
**Link:** http://arxiv.org/abs/2608.06830v1

---

## 🎯 Problem Statement
- To fill this gap, we formulate two communication attacks corresponding to distinct attacker access settings: the External Entry Point Attack and the Privileged In-System Attack.

## 🏗️ Architectural Overview & Technical Design
- Large Language Models (LLMs) are increasingly used as high-level planners in embodied multi-robot systems, enabling robots to interpret natural language instructions and coordinate executable actions.
- Existing multi-robot studies are further limited to preliminary analysis under the Decentralized Multi-agent System (DMAS) architecture, so it remains unclear whether these risks persist across other common communication architectures and how attacker access settings shape their propagation.
- Results show that unsafe information can turn into unsafe actions across all three architectures: DMAS reaches a 96.7\% entry endorsement rate and a 100\% post endorsement activation rate, HMAS-1 reaches a 97.8\% unsafe action success rate, and HMAS-2 triggers 88.3\% of task defined unsafe action slots.

## 🛠️ Solution Approaches & Methodology
- We evaluate both attacks across DMAS, HMAS-1, and HMAS-2 using three LLMs and five embodied multi-robot tasks.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.
