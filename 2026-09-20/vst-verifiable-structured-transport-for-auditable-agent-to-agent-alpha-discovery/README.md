# VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery
**Authors:** Yuqi Li, Siyuan Liu, Bingjun Liu
**Date Published:** 2026-09-07
**Link:** http://arxiv.org/abs/2609.07065v1

---

## 🎯 Problem Statement
- Agent-to-agent (A2A) alpha discovery is slowed by repeated feedback cycles between mining and evaluation agents, whose hand-offs, in contemporary LLM multi-agent systems, are free-form natural-language messages that carry no stable contract and cannot be replayed.
- We first restructure this communication as a structured agent-to-agent protocol of \emph{typed, causally addressable, unicast records}, so that the committed stream forms a causal trajectory.

## 🏗️ Architectural Overview & Technical Design
- We first restructure this communication as a structured agent-to-agent protocol of \emph{typed, causally addressable, unicast records}, so that the committed stream forms a causal trajectory.
- Structure is the enabling contribution, and its value is not accuracy.

## 🛠️ Solution Approaches & Methodology
- What typing provides is a state that can be schema-checked, replayed deterministically, and prevented by construction from leaking a forecast to an evaluator: auditability by construction, not an empirically stress-tested guarantee.
- On a CSI~1000 out-of-sample holdout, our single run is the only one among eight methods (seven baselines and ours) to hold a positive median annualized return and Sharpe at the factor level, though the median return \emph{in excess} of the benchmark stays negative for every method including ours; its development-selected top-20 portfolios reach a $0.71$ median holdout Sharpe, selected on a split inside the optimization horizon.

## 🌍 Societal Impact & Sector Benefits
- We report these single-run results descriptively, gross of costs, and are explicit about their limits throughout; in particular we do not isolate the effect of the leap machinery from the inherited search substrate, which we leave to future work..
