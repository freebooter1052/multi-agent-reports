# EasyBCI Agent: Towards Universal Neural Data Preprocessing for Brain-Computer Interfaces
**Authors:** Yu Zhu, Runkai Zhao, Zhimin Zhou, Jinyu Cai, Zhouheng Yao, Chutian Zhang, Peiyuan Li, Xiaoxing Zhang, Qihao Zheng, Jiamin Wu, Mianxin Liu, Chi Zhang, Bin Min, Lei Bai, Chengyu Li, Jingpeng Wu, Chunfeng Song
**Date Published:** 2026-07-31
**Link:** http://arxiv.org/abs/2607.29007v1

---

## 🎯 Problem Statement
- Brain-Computer Interfaces (BCIs) read brain waves so people can control devices with their thoughts. But right now, cleaning up those raw brain signals (preprocessing) has to be done manually by experts, which takes a long time and is hard to repeat perfectly.
- While some AI agents can write code, they aren't built to handle the strict rules needed for medical data (like never exposing raw patient data directly to the AI) and lack the specific scientific knowledge needed.

## 🏗️ Architectural Overview & Technical Design
- The team built **EasyBCI**, a two-part AI agent system designed specifically for brain data.
- **The Plan Agent:** This part looks at a summary of the data (a "Data Fingerprint") without ever seeing the raw, sensitive brain waves. It then picks the best scientific steps from past research to clean the data.
- **The Execution Agent:** This part actually writes the computer code to do the cleaning, runs it, and fixes its own mistakes until the data is clean. It also saves good solutions to use again later.

## 🛠️ Solution Approaches & Methodology
- They designed EasyBCI to handle six different types of brain signals (like EEG).
- It includes two "decision gates" where a human expert checks the work, making sure no hidden errors ruin the results.
- **Testing:** They tested it on EEG data to see if a computer could still understand the brain signals after EasyBCI cleaned them. The results showed that EasyBCI's automated cleaning was actually better than pipelines built by human experts and beat out general-purpose coding AIs.

## 🌍 Societal Impact & Sector Benefits
- EasyBCI makes it much faster and cheaper to build Brain-Computer Interfaces because labs won't need as many highly specialized data experts just to clean data.
- This could speed up the development of thought-controlled devices for people with disabilities and improve the overall reliability of neurotechnology research.
