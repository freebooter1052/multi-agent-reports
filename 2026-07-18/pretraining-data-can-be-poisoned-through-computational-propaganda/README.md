# Pretraining Data Can Be Poisoned through Computational Propaganda
**Authors:** Victoria Graf, Hannaneh Hajishirzi, Noah A. Smith, David Kohlbrenner, Kyle Lo
**Date Published:** 2026-07-16
**Link:** http://arxiv.org/abs/2607.15267v1

---

## 🎯 Problem Statement
- The core challenge is that bad actors could secretly insert malicious information (poison) into the massive amounts of data used to train Large Language Models (LLMs).
- This is difficult and important because most AI models are trained on text scraped from the internet. If this data is poisoned, the AI might learn harmful behaviors that are very hard for developers to find and fix before the AI is released to the public.

## 🏗️ Architectural Overview & Technical Design
- The paper looks at the entire pipeline of how an LLM is trained: from crawling the web for data, to curating and filtering that data, to actually pretraining the neural network.
- The "input" is the poisoned content added to the internet by a malicious user. The "output" is the trained AI model that might now have dangerous behaviors.
- The authors introduce a new analytical tool called "HalfLife," which is designed to measure how likely it is that this poisoned content actually makes it through the filtering process and into the final training data.

## 🛠️ Solution Approaches & Methodology
- The authors demonstrate that attackers don't need to hack major websites like Wikipedia. They can just use normal, public discussion forums to inject their bad data into the web.
- They then use their new HalfLife tool to analyze web-crawled datasets. They test to see if the malicious content they created would survive the normal data curation process and end up in the final dataset used for training.
- Their key evaluation is seeing if these "poison injections" are successfully included in pretraining data at a massive, web-scale level.

## 🌍 Societal Impact & Sector Benefits
- By exposing this security flaw, this research helps the cybersecurity and AI safety sectors build stronger defenses against data poisoning attacks.
- Practical, real-world use cases include developing better filters for AI training data, ensuring that the AI systems we use for coding, writing, and research are safe, unbiased, and not manipulated by malicious groups.
