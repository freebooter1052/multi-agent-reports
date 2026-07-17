# Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models
**Authors:** Patrik Wolf, Thomas Kleine Buening, Andreas Krause, Celestine Mendler-Dünner
**Date Published:** 2026-07-16
**Link:** http://arxiv.org/abs/2607.15277v1

---

## 🎯 Problem Statement
- Large Language Models (LLMs) often generate text that sounds confident but can be logically inconsistent when asked the same question in different ways. Specifically, the paper investigates if LLMs follow the basic math rule of probability: if you divide a group into smaller sub-groups, the sum of the probabilities for the sub-groups should equal the probability for the whole group.
- This problem is important because if LLMs don't follow basic logic and math rules, we cannot trust them to make reliable decisions or estimates, especially in critical real-world applications where accuracy matters.

## 🏗️ Architectural Overview & Technical Design
- The researchers use a system shaped like a "binary tree" (a structure that splits into two branches at each step) to test the LLMs. This tree divides a large population of people or things into smaller, more specific sub-groups (like dividing "all adults" into "men" and "women," then dividing them further).
- They feed prompts to the LLM asking for estimates about these specific sub-groups, and then use math to combine the LLM's answers back together to see if they add up correctly to the total group's estimate.
- Data flows by taking a main question, splitting it into smaller questions using the tree structure, getting the LLM's answers for each small question, and aggregating (adding up) those answers to compare with the LLM's answer to the main question. No new neural network layers are built; they test existing state-of-the-art models.

## 🛠️ Solution Approaches & Methodology
- Step 1: Create a mathematical tree that perfectly partitions (divides) a population into smaller groups. Step 2: Ask the LLM a question about the whole group. Step 3: Ask the LLM the exact same question, but for every smaller sub-group in the tree. Step 4: Add up the sub-group answers and see if they match the answer for the whole group.
- They tested their approach using various problem types on different top-tier AI models. They measured the "consistency gap"—the difference between the direct answer and the added-up answers—and found widespread violations of this basic consistency rule.

## 🌍 Societal Impact & Sector Benefits
- By revealing this "macro fallacy" (where adding up smaller estimates is often more accurate than asking for a big estimate directly), developers can design better, more accurate ways to ask LLMs questions (prompt engineering).
- In real-world use cases, this means AI tools used for data analysis, polling, or making predictions in business and science can be made more reliable and trustworthy by breaking big questions into smaller, specific pieces before asking the AI.
