# AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis
**Authors:** Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho
**Date Published:** 2026-07-30
**Link:** http://arxiv.org/abs/2607.28618v1

---

## 🎯 Problem Statement
- Researchers in chemistry struggle to find specific information across many different scientific papers because search engines only return long lists of documents.
- This is a difficult problem because scientists and artificial intelligence (AI) agents have to manually read through papers to verify facts and combine answers from multiple sources.

## 🏗️ Architectural Overview & Technical Design
- The system, named AskChem, breaks down scientific papers into smaller, individual facts called "claims," rather than treating the whole paper as a single result.
- Each claim contains a clear statement, the exact source document it came from, and the specific quote proving it.
- AskChem organizes these claims using a structured hierarchy (taxonomy) for easy browsing and a network (evidence graph) that connects related claims together.

## 🛠️ Solution Approaches & Methodology
- The researchers built AskChem by processing 147,000 chemistry papers into 2.4 million individual claims.
- They created interfaces for both human scientists (a web website) and AI agents (code access) to easily search the database.
- They tested AskChem using a benchmark evaluation, finding that an AI system using their tool could correctly trace the source of information 100% of the time, outperforming other methods.

## 🌍 Societal Impact & Sector Benefits
- This research benefits the chemistry sector by making literature review much faster and more accurate for both scientists and automated AI tools.
- A practical use case is accelerating the discovery of new chemical compounds and materials by allowing researchers to instantly find and verify past experimental results.
