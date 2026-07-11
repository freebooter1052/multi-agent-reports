# Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation
**Authors:** Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu, Hokin Deng, Ziyang Gong, Xuanyi Zhou, Huacan Wang, Xiangchao Yan, Wanghan Xu, Wenlong Zhang, Shaofeng Zhang, Yue Zhou, Yifan Yang, Zhihang Zhong, Xue Yang
**Date Published:** 2026-07-09
**Link:** http://arxiv.org/abs/2607.08758v1

---

## 🎯 Problem Statement
- Scientific ideas inherit mechanisms, repair known limitations, and recombine pieces of earlier work, similar to biological genomes. However, current AI benchmarks do not effectively evaluate whether AI systems can follow or comprehend this complex inheritance structure.
- This limitation makes it difficult to assess AI models on their ability to perform true scientific lineage reasoning and to generate new ideas that coherently descend from existing research literature.

## 🏗️ Architectural Overview & Technical Design
- The authors introduce IdeaGene-Bench (IG-Bench), organized around the IdeaGene framework.
- In this architecture, each paper or proposal is represented as a set of minimal, typed, evidence-grounded 'Idea Genome' objects. Data flows through a structure called GenomeDiff, which aligns these objects to record evolutionary dynamics.
- The system models six operational evolutionary dynamics: inheritance, mutation, loss, external import, and novel insertion, creating a graph-like lineage trace of scientific concepts across 10 domains.

## 🛠️ Solution Approaches & Methodology
- The researchers created a benchmark with 1,961 golden lineage traces, 1,085 curated Idea Genome objects, and 920 pairwise GenomeDiff records.
- They structured evaluations into two parts: IG-Exam, which tests closed-form lineage reasoning across 42 task types; and IG-Arena, which evaluates generative proposals using a lineage-conditioned Population-Evolution Score (PES).
- They evaluated 14 state-of-the-art LLM-based scientist agents on these tasks, discovering a "compositional bottleneck" where even the strongest system reached only 27.3% exact accuracy on lineage reasoning.

## 🌍 Societal Impact & Sector Benefits
- This benchmark benefits the AI and scientific research sectors by providing a rigorous way to measure and improve how AI systems understand and synthesize scientific literature.
- Practical use cases include AI-assisted scientific discovery tools, advanced literature review systems that can trace the evolutionary history of an algorithm, and automated researchers capable of proposing valid, novel hypotheses grounded in existing lineages.
