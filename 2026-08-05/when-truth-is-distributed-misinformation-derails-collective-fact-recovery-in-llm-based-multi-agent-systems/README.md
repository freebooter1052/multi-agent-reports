# When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems
**Authors:** Chenfei Yan, Zeyang Yue, Feifei Zhao, Erliang Lin, Lu Jia, Haibo Tong, Mingyang Lyu, Chengyi Sun, Yi Zeng
**Date Published:** 2026-08-04
**Link:** http://arxiv.org/abs/2608.03421v1

---

## 🎯 Problem Statement
- The paper tackles the issue of misinformation spreading within LLM-based multi-agent systems where agents communicate to reach a consensus.
- This is critical because errors from a single deceptive agent can propagate through the network, corrupting the final collective decision and making the system unreliable.

## 🏗️ Architectural Overview & Technical Design
- The framework introduced is called Hi-Agreement, which compares scenarios of all-honest agents against scenarios with one deceptive agent holding key information.
- The system flows through multi-stage voting, where agents share observations, adopt testimonies, and propagate information to reach a final endpoint.
- It leverages homogeneous LLM-based agents operating within object-movement environments to track how information lineage affects the group's consensus.

## 🛠️ Solution Approaches & Methodology
- The researchers set up 120 object-movement tasks using 5-agent systems, strictly pairing honest networks with deceptive ones.
- They evaluated the aggregation process by tracing how agents adopted testimonies and how false evidence propagated through the system over multiple communication rounds.
- The evaluation metric focused on the aggregate truth recovery rate, tracking the drop in accuracy when deception was introduced.

## 🌍 Societal Impact & Sector Benefits
- By understanding how misinformation propagates in AI networks, developers can build more robust and trustworthy autonomous systems.
- Real-world applications include secure multi-agent systems for financial trading, autonomous driving fleets, and automated decision-making pipelines.
