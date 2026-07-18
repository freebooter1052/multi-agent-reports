# Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models
**Authors:** Patrik Wolf, Thomas Kleine Buening, Andreas Krause, Celestine Mendler-Dünner
**Date Published:** 2026-07-16
**Link:** http://arxiv.org/abs/2607.15277v1

---

## 🎯 Problem Statement
- The paper investigates whether Large Language Models (LLMs) follow basic rules of probability when they generate answers. Specifically, if you ask an LLM a question about a whole group, its answer should match what you get if you ask it about smaller parts of that group and add the answers together (the law of total probability).
- This is an important problem because if LLMs aren't consistent like this, their answers might not be reliable, especially when making predictions or estimations based on prompts.

## 🏗️ Architectural Overview & Technical Design
- The authors use a system of "binary trees" to test the LLMs. Imagine taking a large group of people and splitting them into two smaller groups, and then splitting those again and again. This is what they do with their test questions.
- The input is a prompt asking the LLM to make an estimate for a specific group. The output is the LLM's estimate. The system then takes the estimates for the smaller groups and uses math to combine them and check if they match the estimate for the whole group.
- They tested this on state-of-the-art frontier models (which are the newest and most powerful LLMs available).

## 🛠️ Solution Approaches & Methodology
- The step-by-step method involves recursively dividing a population into smaller parts. They then give the LLMs descriptions of these smaller groups and ask for estimates.
- They then add up all the estimates from the smaller groups to see if they equal the estimate for the big group. They call this checking for "statistical self-consistency."
- Interestingly, they found a "macro fallacy": the combined answers from the smaller groups were often more accurate compared to human data than asking the LLM about the big group directly. They tested this across different types of problems and different ways of structuring the questions.

## 🌍 Societal Impact & Sector Benefits
- This research helps the tech industry build more reliable and trustworthy AI systems. By understanding where LLMs make these math-like errors, developers can improve how models are trained and how questions (prompts) are asked.
- Practical applications include better automated tools for estimating data, more accurate AI assistants, and a new way to test how good an LLM is without needing a perfect "answer key" to compare against.
