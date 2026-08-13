# Who Are You Explaining To? A Multi-Agent System for Audience-Aware XAI Narratives
**Authors:** Francesco Musicco, Danilo Danese, Giuseppe Fasano, Angela Lombardi, Alberto Carlo Maria Mancino, Tommaso Di Noia
**Date Published:** 2026-08-11
**Link:** http://arxiv.org/abs/2608.11033v1

---

## 🎯 Problem Statement
- Feature-attribution methods such as SHAP provide useful evidence about individual model predictions, but their numerical outputs are rarely sufficient for audiences with different expertise, goals, and risks of misinterpretation.
- In medical AI, the same local explanation must reach patients, clinicians, and data scientists through markedly different forms of communication, and naive verbalization through large language models (LLMs) is prone to weak grounding, conflation of attribution with causal language, and outputs that are persuasive without being faithful to the underlying model evidence.

## 🏗️ Architectural Overview & Technical Design
- Feature-attribution methods such as SHAP provide useful evidence about individual model predictions, but their numerical outputs are rarely sufficient for audiences with different expertise, goals, and risks of misinterpretation.
- In medical AI, the same local explanation must reach patients, clinicians, and data scientists through markedly different forms of communication, and naive verbalization through large language models (LLMs) is prone to weak grounding, conflation of attribution with causal language, and outputs that are persuasive without being faithful to the underlying model evidence.
- We introduce XstrAI, an audience-aware multi-agent framework that treats local explanations as fixed evidence and structures how it is communicated to each target reader.

## 🛠️ Solution Approaches & Methodology
- Feature-attribution methods such as SHAP provide useful evidence about individual model predictions, but their numerical outputs are rarely sufficient for audiences with different expertise, goals, and risks of misinterpretation.
- We evaluate XstrAI on diabetes and stroke risk prediction against 11 baselines, ranging from direct verbalization to a re-implementation of a state-of-the-art narrator.
- In both evaluations, XstrAI's narratives are consistently assigned to their intended audience by independent judges, and preferred over all baselines on Clinician and Patient audiences, with competitive performance on Data Scientist, where audience-conditioned single-prompt baselines lead..

## 🌍 Societal Impact & Sector Benefits
- By addressing the challenges mentioned, this research enhances the capabilities of AI and software engineering systems.
- Practical applications include more robust and efficient automated tools for developers.
