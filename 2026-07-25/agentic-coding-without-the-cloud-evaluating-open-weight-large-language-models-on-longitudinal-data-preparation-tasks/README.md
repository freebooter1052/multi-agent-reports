# Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks
**Authors:** Mack Nixon, Liam Wright, Yevgeniya Kovalchuk, Alison Fang-Wei Wu, Martin Danka, Andy Boyd, David Bann
**Date Published:** 2026-07-23
**Link:** http://arxiv.org/abs/2607.21482v1

---

## 🎯 Problem Statement
- The research focuses on the constraint that using cloud-based LLMs for coding tasks on sensitive or personal data violates privacy and governance regulations, preventing data from being sent to external services.
- This is a significant bottleneck in research involving longitudinal population studies, where data preparation is complex but privacy is paramount.

## 🏗️ Architectural Overview & Technical Design
- The paper presents a framework designed to run locally using open-weight large language models, ensuring sensitive data never leaves the secure local environment.
- The system architecture involves an AI agent that generates R code to execute data preparation tasks, such as category harmonization and multi-wave merging.
- It utilizes 31-35B parameter consumer-grade models to act as the primary engine for generating the necessary cleaning scripts.

## 🛠️ Solution Approaches & Methodology
- The authors introduced an open-source evaluation framework (RRBench) comprising a curated ground-truth dataset from a British cohort study.
- They defined 20 specific data preparation tasks (involving the creation of 102 variables) to benchmark various models.
- The methodology includes automated routines for evaluating the LLM-produced R code and the resulting outputted data, achieving an average task completion rate of up to 87.9% with state-of-the-art open-weight models.

## 🌍 Societal Impact & Sector Benefits
- This research significantly benefits the healthcare, social science, and public health sectors by providing a secure, compliant way to leverage AI for data processing.
- By allowing researchers to securely prepare sensitive longitudinal data locally, it accelerates scientific discovery and ensures privacy compliance without relying on third-party cloud services.
