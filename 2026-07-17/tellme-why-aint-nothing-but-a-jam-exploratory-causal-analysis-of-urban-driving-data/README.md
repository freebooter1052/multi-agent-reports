# teLLMe Why (Ain't Nothing but a Jam): Exploratory Causal Analysis of Urban Driving Data
**Authors:** Qiwei Li, Jorge Ortiz
**Date Published:** 2026-07-16
**Link:** http://arxiv.org/abs/2607.15254v1

---

## 🎯 Problem Statement
- City traffic agencies have a lot of video data from cars (dashcams), but they mostly just watch it. It is very hard to use this video data to answer "what if" questions (causal questions), like "What if it rains, how much worse will traffic get?" because they can't easily run real-world experiments to test it.
- This is important because understanding *why* traffic happens, not just *that* it happens, is necessary to make cities safer and less congested.

## 🏗️ Architectural Overview & Technical Design
- The system, called **teLLMe**, takes structured data (like a table of events) created from dashcam videos and uses it to figure out cause-and-effect relationships.
- A user asks a question in plain English. A Large Language Model (LLM) translates this question into a specific mathematical "causal query."
- The system uses algorithms (like the PC algorithm and linear regression via a tool called DoWhy) to analyze the data and calculate the cause-and-effect. The final output is a "Causal Card" that explains the findings in simple language along with the math behind it.

## 🛠️ Solution Approaches & Methodology
- Step 1: Start with a table of traffic events from dashcam data. Step 2: Use the LLM to turn a user's natural language question into a formal causal query. Step 3: Run structure learning algorithms to map out how different events (like weather and traffic density) might affect each other. Step 4: Estimate the actual impact using linear regression.
- The authors evaluated the system using case studies on real traffic data (BDD-derived events). They checked if the system could correctly identify logical relationships (like rain causing slower traffic) while clearly showing the uncertainty in the data.

## 🌍 Societal Impact & Sector Benefits
- This tool helps urban planners and traffic engineers make better, data-driven decisions to reduce traffic jams and improve road safety without having to run expensive or dangerous real-world experiments.
- Real-world use cases include city governments using dashcam data to optimize traffic light timings during bad weather, or quickly understanding the root causes of accidents at specific intersections to redesign them safely.
