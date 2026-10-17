# EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents
**Authors:** Luigi Sigillo, Matteo Silvestri, Francesco Tabaro, Rajat Bhatnagar, Syed Irtaza Mubashar, Matt Jeffryes, Daljit Nijjer, Vittorio Perera, Ola Spjuth, Julio Saez-Rodriguez, Melissa Harrison, Fabio Petroni
**Date Published:** 2026-07-30
**Link:** http://arxiv.org/abs/2607.28229v1

---

## 🎯 Problem Statement
- Current large databases of scientific papers, like Europe PMC, are designed for human readers, making it very difficult for artificial intelligence (AI) agents to search for and extract specific information.
- This is important because AI agents are increasingly being used to analyze life-sciences data, but they struggle to efficiently query databases that require complex keywords and full-paper reading.

## 🏗️ Architectural Overview & Technical Design
- The researchers introduce the EMBL AI Librarian, a "knowledge layer" that acts as an intelligent translator between AI agents and the Europe PMC database.
- An AI agent asks a question in normal, everyday language, and a large language model (LLM) breaks down this question into multiple smaller search queries.
- The system executes these queries on Europe PMC, reads the relevant papers, and returns exactly the evidence needed to answer the original question.

## 🛠️ Solution Approaches & Methodology
- The methodology involves using a single LLM to coordinate the entire process of planning searches, executing them, and extracting information from the text.
- The researchers evaluated the system using four different tests, including answering open-ended questions and verifying scientific claims.
- They measured performance using specific metrics (like Citation F1 score) and demonstrated significant improvements over existing baseline models.

## 🌍 Societal Impact & Sector Benefits
- This research benefits the biology and life-sciences sector by drastically improving the ability of AI tools to access and synthesize biological knowledge.
- Real-world applications include building more capable AI assistants that can accurately help biologists answer complex questions about genetics, proteins, or experimental protocols using the latest literature.
