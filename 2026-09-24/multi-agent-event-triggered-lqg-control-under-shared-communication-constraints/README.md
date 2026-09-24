# Multi-Agent Event-Triggered LQG Control under Shared Communication Constraints
**Authors:** Zahra Hashemi, Dipankar Maity
**Date Published:** 2026-09-18
**Link:** http://arxiv.org/abs/2609.21974v1

---

## 🎯 Problem Statement
- Although the agent dynamics are decoupled, the communication decisions are coupled through the shared network constraint, leading to a constrained multi-agent scheduling problem.
- Based on this structure, we develop a centralized receding-horizon scheduling framework and reformulate the resulting problem as a mixed-integer linear program (MILP) using a closed-form characterization of the estimation-error covariance.

## 🏗️ Architectural Overview & Technical Design
- Based on this structure, we develop a centralized receding-horizon scheduling framework and reformulate the resulting problem as a mixed-integer linear program (MILP) using a closed-form characterization of the estimation-error covariance.
- To improve scalability, we derive a window-based skip-pruning condition that safely fixes consecutive transmission decisions to zero before solving the MILP, and we propose an auction-inspired scheduler based on one-step transmission-benefit scores.
- Numerical results show that the proposed model predictive control (MPC) scheduler achieves the best trade-off between control performance and communication cost, while the auction-based scheduler attains performance close to MPC with substantially lower computational complexity..

## 🛠️ Solution Approaches & Methodology
- The approach is evaluated using specific experiments outlined in the paper.

## 🌍 Societal Impact & Sector Benefits
- To improve scalability, we derive a window-based skip-pruning condition that safely fixes consecutive transmission decisions to zero before solving the MILP, and we propose an auction-inspired scheduler based on one-step transmission-benefit scores.

---
