# Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents
**Authors:** Paul Kassianik, Blaine Nelson, Yaron Singer
**Date Published:** 2026-07-16
**Link:** http://arxiv.org/abs/2607.15263v1

---

## 🎯 Problem Statement
- Existing methods for evaluating AI security agents mostly focus on whether the agent successfully completes a task (like finding a vulnerability), assuming they have unlimited time and computing power (budget).
- This gap is important because, in the real world, every action an AI takes—like analyzing code, using a tool, or asking for more data—costs money and computational resources. Knowing only the success rate isn't enough to know if an AI is practical to use.

## 🏗️ Architectural Overview & Technical Design
- The evaluation framework tests AI models on two types of tasks: offensive (red-team, like finding hacks) and defensive (blue-team, like investigating security alerts).
- The system inputs challenging security scenarios (like Cybench tasks or Splunk BOTS v1 investigations) to the AI models. The output is not just a pass/fail score, but a detailed breakdown of how much compute time and tool usage the AI spent to get its result.
- The architecture is designed to compare different Language Models at fixed cost levels, rather than just looking at their absolute best performance.

## 🛠️ Solution Approaches & Methodology
- The authors test various language models on specific security challenges. Instead of giving them unlimited tries, they track the "inference spend" (how much the AI thinks) and "tool spend" (how many external tools it uses).
- They evaluate offensive agents on hacking challenges (CTFs) and defensive agents on Security Operations Center (SOC) investigation tasks.
- A key finding was that giving an AI more computing power helps it hack better, but for defending, success relies more on using tools smartly and navigating data carefully rather than just "thinking" longer.

## 🌍 Societal Impact & Sector Benefits
- This research greatly benefits the cybersecurity industry by providing a more realistic way to evaluate which AI models are actually useful and cost-effective for protecting networks and data.
- Real-world applications include helping companies choose the right AI for their security teams based on their budget, and guiding AI developers to build models that aren't just smart, but also efficient in how they use security tools.
