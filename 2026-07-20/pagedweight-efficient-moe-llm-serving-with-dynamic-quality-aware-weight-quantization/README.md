# PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization
**Authors:** Yuchen Yang, Yifan Zhao, Anisha Dasgupta, Sasa Misailovic
**Date Published:** 2026-07-17
**Link:** http://arxiv.org/abs/2607.16184v1

---

## 🎯 Problem Statement
- Large Language Models that use a "Mixture-of-Experts" (MoE) design are highly efficient but require a massive amount of GPU memory for both their complex model weights and their growing context memory (KV cache) during operation.
- This memory conflict forces a difficult trade-off: either limit the size of the context memory or reduce the model's accuracy, which severely restricts how many requests the system can serve simultaneously.

## 🏗️ Architectural Overview & Technical Design
- PagedWeight is a novel memory management system that acts like a smart memory allocator for MoE models running on GPUs.
- It introduces dynamic weight quantization at runtime, meaning it shrinks (compresses) the model's expert weights on the fly to free up space specifically when the KV cache needs it.
- The system continuously monitors and balances the precision of the model weights against the available GPU memory, optimizing for task accuracy, memory consumption, and processing speed.

## 🛠️ Solution Approaches & Methodology
- The researchers implemented PagedWeight to navigate the complex trade-off between memory and quality during active model serving.
- They tested it across various memory-sensitive scenarios and compared it to existing static quantization baselines (methods that permanently compress the whole model).
- The results showed that PagedWeight achieved FP16-equivalent (high precision) accuracy while saving up to 72% of GPU memory and nearly doubling the system's throughput (processing speed).

## 🌍 Societal Impact & Sector Benefits
- This research significantly lowers the hardware costs and energy consumption required to run advanced AI models at scale.
- Real-world applications include cheaper and faster deployment of powerful AI assistants in cloud computing and enterprise environments, making advanced AI more accessible to businesses with limited hardware budgets.
