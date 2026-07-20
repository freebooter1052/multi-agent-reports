# Vision-Language Assistant for Emotional Reactions to Risky Driving
**Authors:** Harine Choi, Eun Hak Lee, Zhengzhong Tu
**Date Published:** 2026-07-17
**Link:** http://arxiv.org/abs/2607.16181v1

---

## 🎯 Problem Statement
- Existing autonomous driving and driver assistance systems excel at perceiving risks but fail to consider the human emotional experience and psychological responses during hazardous situations.
- This lack of emotional awareness can lead to systems that are technically correct but socially jarring or unhelpful, causing drivers to disengage or mistrust the technology.

## 🏗️ Architectural Overview & Technical Design
- The researchers developed the Keep Yelling Assistant (KYA), a system that combines computer vision and large language models (LLMs) to react emotionally to driving risks.
- The system's vision module uses a neural network (YOLOv8) to process dashcam footage, identifying vehicles and risky actions like sudden cut-ins.
- It then calculates structured metrics (like relative speed and distance) and feeds this "behavior log" into a language module (powered by models like ChatGPT-4o), which generates an emotionally appropriate verbal response based on pre-set driver preferences.

## 🛠️ Solution Approaches & Methodology
- The team built the two-part pipeline, using YOLOv8 variants optimized for dashcams to extract spatial and temporal driving cues.
- They evaluated the system using real-world dashcam videos of risky behaviors and conducted a study with 108 human participants.
- Participants rated different language models on how well their emotional responses aligned with different personas (e.g., neutral, angry, humorous), with the combination of YOLOv8s and ChatGPT-4o scoring highest.

## 🌍 Societal Impact & Sector Benefits
- This system paves the way for more empathetic and human-aligned artificial intelligence in vehicles, enhancing driver comfort and trust.
- In practice, it could be used in modern cars to provide personalized, emotionally intelligent feedback during stressful driving events, ultimately promoting a safer and calmer driving environment.
