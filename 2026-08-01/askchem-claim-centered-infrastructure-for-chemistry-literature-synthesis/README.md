# AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis
**Authors:** Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho
**Date Published:** 2026-07-30
**Link:** http://arxiv.org/abs/2607.28618v1

---

## 🎯 Problem Statement
- **Core challenge:** When chemists want to summarize existing research, they have to piece together information scattered across many different publications. Current search engines only give a list of whole documents.
- **Why it is important:** This means scientists and AI computer programs have to waste time finding the exact information, checking where it came from, and putting it together manually. This makes scientific discovery slower.

## 🏗️ Architectural Overview & Technical Design
- **System breakdown:** The researchers created "AskChem," a new search system that focuses on specific facts (called "claims") rather than whole papers. Each research paper is broken down into small, individual facts.
- **Data flow:** When a user or AI searches, the system looks through a database of these facts. Each fact is stored with a direct link (DOI) and a quote pointing back to the original source.
- **Technologies:** The system organizes these facts using a structured category system (taxonomy) and an "evidence graph" that connects related facts. It allows AI programs to connect directly using special interfaces (like REST, SDK, and MCP).

## 🛠️ Solution Approaches & Methodology
- **Implementation steps:** The team took 147,000 chemistry papers and extracted 2.4 million individual facts to build their database.
- **Evaluation:** They tested it using a benchmark test called AskChem-Bench by having an AI (GPT-5.5) read and answer questions.
- **Key metrics:** The AI using AskChem provided sources that could be found 100% of the time (compared to 88.3% without it) and had the highest density of correct citations among five tested systems.

## 🌍 Societal Impact & Sector Benefits
- **Industry benefit:** This tool greatly benefits the chemistry and materials science sectors by making it much faster to find and verify scientific facts.
- **Real-world use cases:** It can be used to build better AI research assistants that help scientists discover new medicines or materials more quickly and reliably.
