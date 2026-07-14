# Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data
**Authors:** Shikai Qiu, Marc Finzi, Yujia Zheng, Kun Zhang, Andrew Gordon Wilson
**Date Published:** 2026-07-13
**Link:** http://arxiv.org/abs/2607.11883v1

---

## 🎯 Problem Statement
- Large AI models (like LLMs) have millions or billions of parameters, making them very large and hard to compress (shrink down) without losing what they learned. Existing methods try to compress the model's parameters directly or compress the exact sequence of training data.
- This is a big problem because parameter-based methods don't care how much information the model *actually* learned, they just look at size. On the other hand, compressing the data sequence gets way too large if the data is random or messy (high entropy), like normal text or images. We need a way to measure and compress models based on the actual knowledge they acquired, not just their size or the exact data they saw.

## 🏗️ Architectural Overview & Technical Design
- The paper introduces a new framework called "requential coding." Think of it like a teacher and a student. The teacher model generates or selects training examples based on the student model's own current knowledge distribution.
- The flow of data works like this: instead of saving the whole training sequence, the student's "code" (compressed version) only records the specific examples the teacher picked. More importantly, it only costs "bits" (computer memory) when the teacher and student disagree on an answer.
- The underlying mathematical model uses PAC-Bayes bounds, which is a statistical way to guarantee how well a machine learning model will perform on new, unseen data based on how compressible it is.

## 🛠️ Solution Approaches & Methodology
- The authors implemented requential coding by having a teacher model guide a student model. They record the choices made by the teacher and calculate the bits needed to store the disagreements between them.
- They tested this approach on large language models (up to a billion parameters) and compared it to other compression methods (like post-training quantization, which just rounds off the numbers in the model).
- Key metrics included the length of the resulting code and the generalization guarantee (how well the model proves it can handle new data). They showed their method creates much smaller codes than previous methods, especially as models get larger.

## 🌍 Societal Impact & Sector Benefits
- For the tech and software engineering sectors, this means we can better understand exactly how much "real" information large AI models are learning, separating the signal from the noise.
- Practically, this could lead to more efficient ways to train, compress, and deploy massive AI models on smaller devices (like phones or edge servers) by proving they can be highly compressed while still guaranteeing they will work correctly in real-world applications.
