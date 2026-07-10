# Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation
**Authors:** Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu, Hokin Deng, Ziyang Gong, Xuanyi Zhou, Huacan Wang, Xiangchao Yan, Wanghan Xu, Wenlong Zhang, Shaofeng Zhang, Yue Zhou, Yifan Yang, Zhihang Zhong, Xue Yang
**Date Published:** 2026-07-09
**Link:** http://arxiv.org/abs/2607.08758v1

---

## 🎯 Problem Statement
- They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes.

## 🏗️ Architectural Overview & Technical Design
- Current benchmarks still say little about whether AI systems can follow this inheritance structure.
- IG-Bench is organized around the IdeaGene framework: each paper or proposal is represented as a set of minimal, typed, evidence-grounded Idea Genome objects, and a GenomeDiff aligns these objects to record inheritance, mutation, loss, external import, and novel insertion under six operational evolutionary dynamics.
- The strongest system reaches only 27.3% exact accuracy on lineage reasoning, and structured lineage context reshuffles system rankings rather than helping every participant uniformly..

## 🛠️ Solution Approaches & Methodology
- IG-Exam (42 task types, 1,029 instances) tests closed-form lineage reasoning across Idea Genome abstraction, inheritance tracing, evolutionary reasoning, and lineage verification.
- IG-Arena evaluates generation with a lineage-conditioned Population-Evolution Score(PES), asking whether a proposal can be inserted as a coherent descendant of a given lineage population: it should inherit the right Idea Genome objects, vary meaningfully from nearby work, and offer selection value for future research.

## 🌍 Societal Impact & Sector Benefits
- IG-Arena evaluates generation with a lineage-conditioned Population-Evolution Score(PES), asking whether a proposal can be inserted as a coherent descendant of a given lineage population: it should inherit the right Idea Genome objects, vary meaningfully from nearby work, and offer selection value for future research.
