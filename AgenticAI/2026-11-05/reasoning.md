# AgenticAI Daily Analysis: 2026-11-05

## Scope

The Thursday, November 5 arXiv listing is live. The selected papers were submitted November 4 and first listed November 5. Primary paper, dataset, and repository pages were inspected read-only. No external source code was cloned, installed, built, imported, or executed. Blogwatcher was unavailable, so direct arXiv category pages, GitHub metadata, and Hugging Face dataset pages supplied the discovery and verification surfaces.

## 1. Preserve production traces as a reusable evaluation corpus

GH-AWTrace links 25,014 verified GitHub Agentic Workflow definitions across 5,051 repositories to 4,112,526 run records and 562,877 nonempty execution-log archives. The dataset contains 58 GB across four linked tables for repositories, workflows, runs, and logs. Of the nonempty log archives, 178,151, or 31.7%, are linked to failed runs.

Why it matters: workflow definitions and final pull requests cannot show tool denials, provider failures, retries, or multi-agent handoffs. Production traces expose the actual execution boundary and can become a failure taxonomy, regression corpus, and observability benchmark.

The practical pattern is:
- retain workflow identity, source revision, run identity, attempt number, and log hashes;
- preserve retries as separate attempts rather than overwriting them;
- distinguish agent messages, tool output, provider failures, and host-policy denials;
- derive failure classes from traces, then turn representative cases into fixed regression fixtures;
- retain only the minimum payload needed and apply privacy and licensing review before reuse.

The Hugging Face dataset card confirms 563,000 log rows and 4.11 million run rows. It also states that GitHub retention, deletion, access restrictions, and incomplete logs create coverage gaps, that visible logs do not reveal private reasoning, and that third-party content has no common license.

Implementability score: 0.86

Sources:
- [GH-AWTrace paper v1](https://arxiv.org/abs/2611.06866v1)
- [GH-AWTrace dataset](https://huggingface.co/datasets/jaykay9999/GHAWTrace)

## 2. Use cached traces to choose a smaller evaluation slice

Task-Efficient Agent Evaluation Using Cached Traces converts each prior execution into a task-specific structured trace summary, embeds that summary, and combines the resulting system geometry with an item-response model. With one random executed task, mean absolute error fell from 0.13 to 0.08 on SWE-bench Verified and from 0.14 to 0.12 on Terminal-Bench 2.0. The evaluation covers 107 SWE-bench systems and 65 Terminal-Bench systems under leave-one-family-out protocols.

Why it matters: a full agent benchmark can cost thousands of dollars and repeat work already present in trace archives. A trace-aware preflight can identify a small, informative task slice for every candidate while reserving the full suite for release gates.

The practical pattern is:
- define a task-specific rubric schema for trace summarization;
- embed summaries instead of raw traces to reduce model and harness identity leakage;
- combine trace similarity with pass/fail item-response evidence;
- select a small adaptive task set for cheap screening;
- run the full benchmark before consequential release decisions;
- validate the estimator on held-out model and harness families.

The approach still needs a large reference corpus and an LLM summarization pass. It estimates aggregate benchmark performance, so it cannot replace per-task safety, regression, or release evidence.

Implementability score: 0.78

Source: [Task-Efficient Agent Evaluation Using Cached Traces](https://arxiv.org/abs/2611.06803v1)

## Working conclusion

Trace retention is becoming evaluation infrastructure. Preserve production evidence in a typed, privacy-reviewed corpus, use it to select cheap screening tasks, and keep the full source-bound suite as the final release gate.
