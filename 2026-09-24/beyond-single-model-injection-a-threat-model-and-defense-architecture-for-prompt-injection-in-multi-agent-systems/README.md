# Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems
**Authors:** Rudrendu Kumar Paul, Sourav Nandy
**Date Published:** 2026-09-19
**Link:** http://arxiv.org/abs/2609.22949v1

---

## 🎯 Problem Statement
- Existing prompt injection research focuses on single-model chatbot scenarios, where an attacker manipulates one LLM through crafted input.
- Multi-agent systems amplify this threat through three mechanisms absent from single-model settings: inter-agent message passing creates injection channels invisible to perimeter defenses, shared tool access enables privilege escalation across agent boundaries, and trust propagation allows a compromised agent to influence upstream orchestrators.

## 🏗️ Architectural Overview & Technical Design
- Existing prompt injection research focuses on single-model chatbot scenarios, where an attacker manipulates one LLM through crafted input.
- Multi-agent systems amplify this threat through three mechanisms absent from single-model settings: inter-agent message passing creates injection channels invisible to perimeter defenses, shared tool access enables privilege escalation across agent boundaries, and trust propagation allows a compromised agent to influence upstream orchestrators.
- We construct a threat model enumerating 14 attack vectors across four categories: direct injection via user input (3 vectors), indirect injection via tool outputs (4 vectors), inter-agent injection via message passing (4 vectors), and cascading injection through orchestrator manipulation (3 vectors).

## 🛠️ Solution Approaches & Methodology
- Testing all 14 vectors against a 6-agent production-representative system, we find that 67% of agents are vulnerable to at least one scope violation even with system-prompt-level guardrails, and indirect injection via tool outputs succeeds in 43% of attempts.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.

---
