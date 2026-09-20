# Learning How Much to Collaborate: Difficulty-Aware Topology Selection for Multi-Agent Code Generation
**Authors:** Yunsong Hong
**Date Published:** 2026-09-12
**Link:** http://arxiv.org/abs/2609.13890v1

---

## 🎯 Problem Statement
- Multi-agent systems for code generation are deployed with a single communication topology, chosen once for every problem.
- Evaluating five topologies on 614 problems from APPS, HumanEval+ and LiveCodeBench, we find that the advantage of hierarchical collaboration over a single agent grows from 2.4 points of pass@1 on the easiest third of problems to 21.1 points on the hardest third, while its token cost stays about ten times higher.
- We propose the Difficulty-Aware Topology Selector (DATS), which predicts each topology's probability of solving a problem and selects the one maximising predicted success minus cost.

## 🏗️ Architectural Overview & Technical Design
- We propose the Difficulty-Aware Topology Selector (DATS), which predicts each topology's probability of solving a problem and selects the one maximising predicted success minus cost.

## 🛠️ Solution Approaches & Methodology
- Because the cost penalty is a single scalar recalibrable without retraining, routers compare at equal spend: under this budget-matched protocol six cost-aware methods span 21.6 percentage points, and two baselines leading DATS fall behind once calibrated to it.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.
