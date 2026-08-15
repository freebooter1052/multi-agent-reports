# StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems
**Authors:** Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
**Date Published:** 2026-08-13
**Link:** http://arxiv.org/abs/2608.13317v1

---

## 🎯 Problem Statement
- However, text introduces a discrete bottleneck.
- However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability.

## 🏗️ Architectural Overview & Technical Design
- Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens.
- However, text introduces a discrete bottleneck.
- Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text.

## 🛠️ Solution Approaches & Methodology
- However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability.
- We propose StateBridge, a training-free latent communication approach that aligns the sender's final-layer hidden states to the receiver's input space via a closed-form orthogonal transformation.
- We evaluate StateBridge on math reasoning, code generation, and question answering with four models from two families.

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.
