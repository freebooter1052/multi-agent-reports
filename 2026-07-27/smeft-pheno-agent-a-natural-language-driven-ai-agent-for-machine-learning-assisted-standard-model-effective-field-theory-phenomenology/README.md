# SMEFT-Pheno-Agent: a natural-language-driven AI agent for machine-learning-assisted Standard Model Effective Field Theory phenomenology
**Authors:** Yu-Chen Guo, Jie Wang, Ji-Chong Yang
**Date Published:** 2026-07-24
**Link:** http://arxiv.org/abs/2607.22331v1

---

## 🎯 Problem Statement
- Physicists studying the Standard Model (the rules of the universe) have to use many complex, disconnected software tools to test their theories at places like particle colliders.
- It is incredibly difficult and time-consuming to manually connect all these different programs and ensure the math and data formatting are correct at every step.

## 🏗️ Architectural Overview & Technical Design
- The system is a Python-based workflow managed by an AI agent that understands plain English instructions.
- Data flows through twelve automated steps, starting from reading the initial configuration, generating simulated particle collisions, picking machine learning models, and finally doing statistics.
- It strictly relies on validated physics software (like MadGraph5 and Pythia) to do the actual math, while the AI just writes the instruction files to link them together.

## 🛠️ Solution Approaches & Methodology
- The researchers programmed the AI agent to interpret user intent and automatically generate the necessary code and parameter files to run the next step in the sequence.
- Once simulated data is created, the AI suggests the best mathematical features and machine learning algorithms to analyze it.
- To ensure accuracy, the AI is locked out of changing core physics rules and must log every single decision it makes into a readable receipt before running anything.

## 🌍 Societal Impact & Sector Benefits
- This tool dramatically speeds up advanced physics research by automating the tedious coding work, allowing scientists to focus on the actual science.
- It ensures that complex experiments are perfectly reproducible and traceable, which is vital for verifying massive discoveries in high-energy physics.
