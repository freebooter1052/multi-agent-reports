# Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation
**Authors:** Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu, Hokin Deng, Ziyang Gong, Xuanyi Zhou, Huacan Wang, Xiangchao Yan, Wanghan Xu, Wenlong Zhang, Shaofeng Zhang, Yue Zhou, Yifan Yang, Zhihang Zhong, Xue Yang
**Date Published:** 2026-07-09
**Link:** http://arxiv.org/abs/2607.08758v1

---

## 🎯 Problem Statement
- Current benchmarks for AI systems fail to evaluate scientific lineage competence, which is the ability to track how scientific ideas inherit mechanisms, repair limitations, and recombine earlier work.
- Existing evaluations focus heavily on factual retrieval and fluency, missing the structural inheritance that drives true scientific progress.

## 🏗️ Architectural Overview & Technical Design
- IdeaGene-Bench (IG-Bench) is organized around the IdeaGene framework, which represents each paper or proposal as a set of minimal, typed, evidence-grounded Idea Genome objects.
- A GenomeDiff aligns these objects to record inheritance, mutation, loss, external import, and novel insertion.
- The framework models idea evolution using six operational evolutionary dynamics.
- It comprises 1,961 golden lineage traces, 1,085 curated Idea Genome objects, and 920 pairwise GenomeDiff records across 10 scientific domains.

## 🛠️ Solution Approaches & Methodology
- The benchmark includes two evaluations: IG-Exam for closed-form lineage reasoning (42 task types, 1,029 instances) and IG-Arena for lineage-grounded idea generation.
- IG-Arena utilizes a lineage-conditioned Population-Evolution Score (PES) to test whether generated proposals coherently inherit Idea Genome objects and offer meaningful selection value.
- The authors evaluated 14 LLM-based scientist systems, analyzing exact accuracy on lineage reasoning and observing compositional bottlenecks.
- The methodology revealed that structured lineage context reshuffles system rankings, as strong baseline systems struggled to keep parent choice, driver assignment, and verification flags jointly consistent.

## 🌍 Societal Impact & Sector Benefits
- Facilitates the development of advanced AI research assistants that can trace and generate genuine scientific innovations rather than superficial text similarities.
- Downstream applications include automated literature review, hypothesis generation, and accelerating scientific discovery across research domains.
