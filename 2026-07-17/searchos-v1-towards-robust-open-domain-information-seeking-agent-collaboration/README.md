# SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration
**Authors:** Yuyao Zhang, Junjie Gao, Zhengxian Wu, Jiaming Fan, Jin Zhang, Shihan Ma, Yao Yao, Weiran Qi, Chuyan Jin, Guiyu Ma, Xingzhong Xu, Kai Yang, Ji-Rong Wen, Zhicheng Dou
**Date Published:** 2026-07-16
**Link:** http://arxiv.org/abs/2607.15257v1

---

## 🎯 Problem Statement
- When AI agents search the web for information, they often get stuck in repetitive loops if they can't find the answer right away. They forget what they have already tried, waste their search budget, and fail to give complete answers.
- This is difficult because keeping track of a long history of searches, failures, and clues is hard for current AI systems, making them fragile and unreliable for complex research tasks.

## 🏗️ Architectural Overview & Technical Design
- The paper introduces **SearchOS**, a system designed to act like an operating system for multiple AI search agents. It changes how agents remember things by turning hidden search history into a clear, shared database.
- It uses a **Search-Oriented Context Management (SOCM)** system, which includes a "Frontier Task" (what to do next), an "Evidence Graph" (how facts connect), a "Coverage Map" (what is missing), and a "Failure Memory" (what didn't work).
- Data flows from the AI agent to a "Middleware Harness" (a tool that intercepts and records the agent's actions), which updates the shared memory. Then, a scheduler assigns new tasks to agents based on what is still missing, running them in parallel (at the same time) to speed things up.

## 🛠️ Solution Approaches & Methodology
- Step 1: Formulate the search task as filling out a table where every fact must have a cited source. Step 2: Use the SOCM system to track all progress and failures. Step 3: Deploy multiple AI agents that work simultaneously, taking tasks from the scheduler and avoiding past mistakes using the Failure Memory.
- They evaluated SearchOS on complex search benchmarks like WideSearch and GISA. They measured metrics like accuracy and completeness, showing that SearchOS outperformed all other single and multi-agent systems tested.

## 🌍 Societal Impact & Sector Benefits
- This research significantly improves the ability of AI to act as a reliable research assistant, saving time and resources for humans who need to find complex information online.
- Practical applications include automated literature reviews for scientists, deep background research for journalists, and robust data-gathering tools for businesses, all of which will become much more efficient and less prone to getting stuck in errors.
