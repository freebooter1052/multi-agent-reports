# EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents
**Authors:** Luigi Sigillo, Matteo Silvestri, Francesco Tabaro, Rajat Bhatnagar, Syed Irtaza Mubashar, Matt Jeffryes, Daljit Nijjer, Vittorio Perera, Ola Spjuth, Julio Saez-Rodriguez, Melissa Harrison, Fabio Petroni
**Date Published:** 2026-07-30
**Link:** http://arxiv.org/abs/2607.28229v1

---

## 🎯 Problem Statement
- **Core challenge:** AI programs are increasingly being used to search the web for scientific information, especially in biology. However, large databases of scientific papers (like Europe PMC) were built for humans, not AI. They require complex search terms and return entire papers instead of specific answers.
- **Why it is important:** Because AI agents have to read through thousands of full papers to find a single piece of evidence, it makes automated research very slow, expensive, and prone to errors.

## 🏗️ Architectural Overview & Technical Design
- **System breakdown:** The researchers introduced "EMBL AI Librarian," a special knowledge layer that acts as a translator between AI agents and the massive database of biology papers.
- **Data flow:** An AI agent asks a question in normal, everyday language. A central AI (Large Language Model) plans out several smaller search queries, runs them on the database, reads only the most relevant selected papers, and returns the exact evidence needed.
- **Technologies:** It uses an AI orchestrator to manage search engine interactions and text reading automatically.

## 🛠️ Solution Approaches & Methodology
- **Implementation steps:** The team built the system to connect with Europe PMC (a database with over 40 million records) and designed it to handle everything from planning searches to extracting text.
- **Evaluation:** They tested the Librarian on four different performance tests (benchmarks) including answering biology questions and verifying facts.
- **Key metrics:** When used for answering questions (ScholarQABench), it improved a key accuracy score (Citation F1) by over 16 points compared to previous methods. An AI agent using this tool scored about 8 points higher on a general biology test (LitQA2) than one using standard web search.

## 🌍 Societal Impact & Sector Benefits
- **Industry benefit:** This research greatly benefits the life sciences and healthcare sectors by giving AI assistants the ability to accurately understand biology literature.
- **Real-world use cases:** Practical applications include AI tools that can quickly help biologists design experiments, understand genetic sequences, or answer complex medical questions.
