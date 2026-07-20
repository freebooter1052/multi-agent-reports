# Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs
**Authors:** Like Liu, Zhengzheng Xu, Haitao He, Hongzhe Li, Shuchang Zhang, Dian Shao
**Date Published:** 2026-07-17
**Link:** http://arxiv.org/abs/2607.16193v1

---

## 🎯 Problem Statement
- Multimodal large language models (MLLMs) struggle with Unmanned Aerial Vehicle (UAV) scenarios, particularly in reasoning about both the drone's own state and the external environment at the same time.
- This is a critical gap because drones need this dual-cognition (knowing where they are and what is around them across space and time) to operate safely and effectively in the real world.

## 🏗️ Architectural Overview & Technical Design
- The researchers introduced UAV-DualCog, a comprehensive testing framework (benchmark) containing both image and video tasks specifically for aerial scenarios.
- The framework uses scene-level 3D point clouds to automatically generate spatial data, feeding into thousands of question-and-answer pairs for evaluation.
- It tests how models handle viewpoint transformation (understanding what things look like from different angles), spatial grounding (pinpointing locations), and temporal localization (knowing when an event happened in a video).

## 🛠️ Solution Approaches & Methodology
- The team created an automated pipeline to build the dataset, ensuring it covers diverse scenes and hundreds of landmarks.
- They evaluated several existing MLLMs on this benchmark and found they performed poorly compared to human baselines, especially in self-state reasoning.
- To prove the usefulness of their data, they created a training set (UAV-DualCog-Train) and fine-tuned models on it, showing that training on this structured data significantly improves model performance.

## 🌍 Societal Impact & Sector Benefits
- Improving how AI models understand drone navigation and environment interaction makes autonomous drones safer and more reliable.
- Practical applications include better autonomous search and rescue operations, aerial delivery services, and environmental monitoring, where drones must independently navigate complex spaces.
