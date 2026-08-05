# MDGAM-Based Cooperative Task Scheduling for Communication-Constrained Distributed Multi-Agent Systems
**Authors:** Licheng Wang, Mingtao Huang, Yuan Shen
**Date Published:** 2026-08-01
**Link:** http://arxiv.org/abs/2608.00648v1

---

## 🎯 Problem Statement
- The research solves the challenge of cooperative task scheduling for distributed multi-robot systems operating under strict communication constraints.
- This is important because real-world robots often have limited communication range and only partial observations, making global coordination difficult.

## 🏗️ Architectural Overview & Technical Design
- The system architecture features the Multi-Decoder Graph Attention Model (MDGAM) policy model paired with a Group Relative Multi-Agent Policy Gradient (GRMAPG) training algorithm.
- Input data (local observations) is processed through an extended graph attention mechanism that jointly updates node and edge features, outputting both task-selection decisions and communication messages.
- The framework uses neural network decoders to handle these outputs without relying on a centralized critic network.

## 🛠️ Solution Approaches & Methodology
- The researchers designed MDGAM to allow agents to communicate efficiently and make scheduling decisions based on local data.
- They trained the system using GRMAPG, which constructs advantages from equivalent task-planning instances to simplify multi-agent reinforcement learning.
- The approach was evaluated by comparing task-completion performance against existing heuristic and learning-based methods across different problem scales and communication ranges.

## 🌍 Societal Impact & Sector Benefits
- This research directly benefits industries relying on multi-robot fleets, such as logistics, manufacturing, and search-and-rescue operations.
- Practical use cases include coordinating warehouse robots, autonomous drone swarms for disaster response, and efficient factory automation.
