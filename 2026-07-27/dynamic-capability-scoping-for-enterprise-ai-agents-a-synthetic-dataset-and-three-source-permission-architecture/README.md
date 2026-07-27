# Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture
**Authors:** Halil Burak Noyan
**Date Published:** 2026-07-24
**Link:** http://arxiv.org/abs/2607.22445v1

---

## 🎯 Problem Statement
- AI agents in companies are often given too many permissions (like skeleton keys), meaning if they make a mistake or are tricked, they can cause a lot of damage.
- This is a big problem because it makes the whole computer system vulnerable to attacks, so we need a way to only give them the exact tools they need for a specific task.

## 🏗️ Architectural Overview & Technical Design
- The authors built a "three-source" security system that checks permissions dynamically (on-the-fly).
- When an AI agent tries to do something, the system checks its maximum allowed rules, looks at what the specific task actually requires, and blocks combinations that are forbidden by company policy.
- It uses a specialized classifier to understand the task context and can either block bad actions or just record them to help researchers learn.

## 🛠️ Solution Approaches & Methodology
- They created a massive synthetic dataset of 600 fake company tasks and labeled them with the minimum permissions needed, using a strict 15-tool system.
- They built this by separating the prompt creation from the permission labeling to avoid cheating or circular logic.
- They tested it thoroughly, showing it reduced security violations by 93% (from 46 down to 3) after tweaking the rules based on the dataset.

## 🌍 Societal Impact & Sector Benefits
- This makes AI much safer for businesses to use by drastically reducing the chance of an AI agent doing something harmful or unauthorized.
- Real-world applications include secure virtual assistants for HR or finance that can't accidentally leak sensitive company data.
