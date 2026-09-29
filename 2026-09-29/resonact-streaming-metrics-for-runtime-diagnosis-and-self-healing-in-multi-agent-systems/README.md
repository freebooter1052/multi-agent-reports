# ResonAct: Streaming Metrics for Runtime Diagnosis and Self-Healing in Multi-Agent Systems
**Authors:** Tarun Chintada, Neelamadhav Gantayat, Ishaan Romil, Renuka Sindhgatta, Soujanya Soni, Sameep Mehta
**Date Published:** 2026-09-28
**Link:** http://arxiv.org/abs/2609.34701v1

---

## 🎯 Problem Statement
- Multi-agent systems (MAS) are increasingly used to automate enterprise workflows involving multiple specialized agents, external tools, and long-running task execution.
- Failures may arise from tool degradation, context propagation errors, coordination breakdowns, or repeated agent interactions that prevent task completion.

## 🏗️ Architectural Overview & Technical Design
- While existing observability frameworks provide traces and logs, diagnosis and remediation are largely performed after execution completes, limiting opportunities for recovery during runtime.
- We present ResonAct, a runtime self-healing framework that enables continuous monitoring, diagnosis, and remediation of multi-agent systems through streaming operational metrics.
- These metrics serve as runtime control signals for detecting anomalous execution patterns and localizing root causes using a structured failure model.

## 🛠️ Solution Approaches & Methodology
- We present ResonAct, a runtime self-healing framework that enables continuous monitoring, diagnosis, and remediation of multi-agent systems through streaming operational metrics.
- ResonAct ingests execution traces, agent interactions, and tool invocations into a streaming analytics layer that continuously derives task progress, context health, and tool reliability metrics.
- These metrics serve as runtime control signals for detecting anomalous execution patterns and localizing root causes using a structured failure model.

## 🌍 Societal Impact & Sector Benefits
- The framework operates as an external control plane, enabling intervention without modifying application agents or orchestration logic.


---
