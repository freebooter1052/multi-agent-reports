# Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning
**Authors:** Lizhe Fang, Weizhou Shen, Tianyi Tang, Yisen Wang
**Date Published:** 2026-07-21
**Link:** http://arxiv.org/abs/2607.19345v1

---

## 🎯 Problem Statement
- Large Language Models (LLMs) often suffer from *repetitive copying* in long-context reasoning tasks. Instead of actually solving the problem, they simply copy large chunks of text from the prompt into their reasoning steps.
- This is a critical problem because as we use AI to process longer and more complex documents, this 'lazy' copying behavior leads to incorrect answers and inefficient reasoning, showing that the model isn't truly understanding or grounding its answers in the relevant facts.

## 🏗️ Architectural Overview & Technical Design
- The authors propose a reward shaping method called GEAR (Grounding Evidence-Aware Reward) used in Reinforcement Learning (RL) for LLMs.
- When a prompt is given, it is separated into two parts: task-relevant key evidence and irrelevant distractor context. The model generates an answer, and the GEAR framework evaluates this output.
- The system calculates a reward signal based not only on accuracy but also on how much the model's reasoning overlaps with the key evidence (a grounding reward) and penalizes overlap with irrelevant distractor context (a distractor penalty).

## 🛠️ Solution Approaches & Methodology
- First, the researchers built an automated pipeline to create training data where key evidence in documents is explicitly annotated.
- They then trained long-context LLMs using Reinforcement Learning with the GEAR reward signal. This means the AI receives positive feedback for relying on correct evidence and negative feedback for copying irrelevant text.
- The approach was tested across multiple model sizes and benchmark tests. They measured improvements in accuracy, reductions in repetitive copying, and the length of the reasoning generated.

## 🌍 Societal Impact & Sector Benefits
- This research significantly benefits the software engineering and AI development sectors by enabling more reliable and accurate long-document analysis tools.
- Practical applications include better AI assistants for legal document review, medical record analysis, and large-scale code base comprehension, where finding the true signal within massive amounts of noise is essential.
