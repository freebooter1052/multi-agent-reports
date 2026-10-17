# Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks
**Authors:** Mack Nixon, Liam Wright, Yevgeniya Kovalchuk, Alison Fang-Wei Wu, Martin Danka, Andy Boyd, David Bann
**Date Published:** 2026-07-23
**Link:** http://arxiv.org/abs/2607.21482v1

---

## 🎯 Problem Statement
- What is the core challenge, flaw, or gap in existing research that this paper is trying to solve?
Researchers often can't use powerful, cloud-based AI tools to help write code for data preparation because they are working with highly sensitive personal data that cannot legally be sent over the internet to external servers.
- Why is this problem difficult or important?
Preparing large datasets is a very slow and difficult bottleneck in research. If researchers could safely use AI to help, it would drastically speed up important scientific discoveries, but privacy rules strictly prevent using standard cloud AI tools.

## 🏗️ Architectural Overview & Technical Design
- Provide a detailed breakdown of the system architecture, framework, or mathematical model introduced.
The researchers designed a testing framework called RRBench. It is built to evaluate "open-weight" AI models—these are AI models that can be downloaded and run completely locally on a researcher's own computer, meaning no data ever goes to the cloud.
- Describe how data flows through this system (input to output).
The system feeds the local AI model a specific data preparation task (like merging different datasets or standardizing categories). The AI model then outputs computer code (specifically R code). This code is automatically run and evaluated against a known, correct dataset to see if it worked.
- Mention any specific technologies, neural network layers, or algorithms leveraged.
The framework tests large language models (LLMs) that have 31 to 35 billion parameters and are capable of running on standard consumer-grade computer hardware, using automated routines to check the R programming code they generate.

## 🛠️ Solution Approaches & Methodology
- What is the exact step-by-step methodology the authors used to implement their solution?
The authors created a real-world testing environment using actual data cleaning scripts from a British population study. They defined 20 specific tasks (creating 102 variables) and then ran various local AI models to see if they could write the correct code to solve these tasks.
- How did they train, test, or evaluate their approach? (Include key metrics or benchmarks used).
They tested several different AI models and measured their "average task completion" rate. They found that the best local models performed very well, successfully completing up to 87.9% of the complex data preparation tasks.

## 🌍 Societal Impact & Sector Benefits
- How does this research benefit society or its specialized industry sector?
This research greatly benefits the healthcare and social science sectors by proving that researchers can safely use AI to speed up their work without violating privacy laws or putting sensitive patient data at risk.
- What are the practical, real-world use cases or downstream applications of this work?
A real-world use case is a hospital research team using a local AI model to quickly clean and organize years of confidential patient records, allowing them to discover new medical trends much faster and entirely securely.
