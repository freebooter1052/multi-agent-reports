# Reachability-Certified Subteam Decomposition for Locally Interacting Multi-Agent MDPs
**Authors:** Xiangwu Wang, Chengwei Cao, Hongyuan Tang
**Date Published:** 2026-09-08
**Link:** http://arxiv.org/abs/2609.08366v1

---

## 🎯 Problem Statement
- Persistent communication limits force a multi-agent system to decide which agents may coordinate throughout a rollout.
- Current proximity alone is insufficient: separated agents may interact later, whereas a large pair reward may remain unreachable until it is heavily discounted.

## 🏗️ Architectural Overview & Technical Design
- We introduce Reachability-Certified Subteam Decomposition (RCSD) for finite multi-agent Markov decision processes with factorized physical dynamics, finite-range ordered pair rewards, and almost-sure motion bounds.

## 🛠️ Solution Approaches & Methodology
- 6 Experimental Design We evaluate RCSD through finite-MDP verification, exact partition utility when the certificate inputs are informative or incomplete, heuristic objective quality, partition-construction scaling, and sto- chastic two-dimensional transfer.
- We evaluate 4,500 instances from each family, each at 𝐿∈{2, 3}.
- At 𝐿= 2 we evaluate all 15 partitions of shape 2 + 2 + 1; at 𝐿= 3, all ten of shape 3 + 2.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.
