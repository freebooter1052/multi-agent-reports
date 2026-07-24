# Benchmarking Agents for Proving Theorems in Quantum Algorithms and Quantum Information
**Authors:** Lei Zhang, Yusheng Zhao, Yimeng Cao, Ranyiliu Chen, Mingrui Jing, Jizhe Lai, Ziao Tang, Jingu Xie, Hongshun Yao, Xuanqiang Zhao, Guocheng Zhen, Chengkai Zhu, Xin Wang
**Date Published:** 2026-07-23
**Link:** http://arxiv.org/abs/2607.21533v1

---

## 🎯 Problem Statement
- While formal verification (checking if code or math is completely error-free) is becoming useful for quantum computing, we don't yet know how well AI agents can write these complex, machine-checked mathematical proofs.
- This is important because quantum algorithms are highly complex and prone to subtle human errors, making automated, verified proofs critical for reliable quantum software.

## 🏗️ Architectural Overview & Technical Design
- The paper introduces two new benchmarking frameworks, Lean-QuantumAlg-Bench and Lean-QIT-Bench, built using the Lean 4 theorem prover language.
- The system takes an AI model's proposed proof as input and runs it through a deterministic proof checker combined with semantic review to verify its correctness.
- The architecture tests AI models in two settings: a basic task-only setting, and a library-augmented deduction (LAD) setting where the AI has access to a verified domain library.

## 🛠️ Solution Approaches & Methodology
- The authors created 76 theorem-completion tasks (36 for algorithms, 40 for information theory) and assigned difficulty weights to each before testing.
- They evaluated four major AI models (GPT-5.5, Kimi K3, DeepSeek V4-Pro, MiniMax M3) by having them attempt to solve the proofs.
- Success was measured using deterministic proof checking, showing that giving the models access to a verified library (LAD) improved their scores by up to 15.9 points.

## 🌍 Societal Impact & Sector Benefits
- Improving AI's ability to prove quantum theorems accelerates the development of reliable quantum computers, which could eventually solve problems in chemistry and medicine that are impossible today.
- Real-world applications include building error-free quantum software compilers and discovering new, verified quantum algorithms for the tech sector.
