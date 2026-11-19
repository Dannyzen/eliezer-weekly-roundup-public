# AgenticAI Daily Analysis: 2026-11-19

## Scope

This scan covers sources first listed by arXiv on 19 November 2026 and submitted on 18 November 2026. External repositories were inspected through GitHub metadata, trees, and README files only. No external source was cloned, installed, built, imported, or executed.

## 1. Gate personal-agent updates against the incumbent

Safe Personal RSI treats reusable instruction changes as release candidates. It runs both the proposed and current instructions against executable safety and task cases, repeats failures, uses rollback to diagnose candidate edits, and keeps the incumbent when no candidate passes.

The benchmark contains 29 cases across email, calendar, health, and marketplace work, with separate probes for authorization reuse, memory, and tool-output injection. Across three models and two risky edits, the procedure rejected 20 of 21 update attempts. In one admitted repair, reported attack violations fell from 10.7% to 0% and safe completion rose from 89.7% to 100%. A stronger cross-model transfer reduced violations from 69.0% to 17.9%, which is material improvement rather than proof of safety.

Why it matters: self-improvement should be a candidate promotion workflow, not a live rewrite. The incumbent is the control, safety and utility are separate gates, repeated failures produce repair evidence, and inability to prove improvement leaves production unchanged.

Fits into the stack: harness evaluation, prompt release management, personal-agent safety, and regression control.

Practical methods worth exploring now:
- version every reusable instruction set and keep the incumbent runnable;
- run matched safety and utility fixtures before promotion;
- repeat failures and retain candidate-versus-incumbent traces;
- use rollback tests to isolate the harmful edit;
- fail closed when no candidate clears both gates;
- test runtime memory deletion and OAuth scope separately from prompt quality.

Artifact status: paper only in this scan. The paper describes an executable benchmark but does not provide a verified public implementation URL.

Evidence limit: the evaluation covers 29 cases and prompt updates only. Model weights and runtime code remain fixed, and the transferred repair still leaves 17.9% attack violations under the stronger test.

Implementability score: 0.72

Core source: [Safe Personal RSI v1](https://arxiv.org/abs/2611.23651v1)

## 2. Make agent memory visible, scoped, and reversible

MemoSync treats memory as an operable shared object rather than hidden context. The agent proposes candidates and reports use; the developer reviews, edits, scopes, selects, and can stop misapplication. A separate post-turn audit checks whether selected memories shaped, violated, or had no visible effect.

The research began with 12 developers, then ran a between-subjects study with 132 participants and a week-long deployment with nine developers. MemoSync produced the highest mean developer-agent memory alignment and higher task performance than the two baselines. Participants performed more monitoring and control actions without a detected increase in perceived workload.

Why it matters: memory reliability needs an interface for proposal, approval, selection, citation, audit, history, and reversal. Retrieval quality alone cannot tell an operator what the agent stored, what entered this turn, or whether it was followed.

Fits into the stack: local-first memory, human control surfaces, coding-agent continuity, and memory observability.

Tools and patterns worth exploring now:
- [SLEEPYBQ/MemoSync](https://github.com/SLEEPYBQ/MemoSync), inspected read-only;
- personal, project, and session scopes;
- version history and append-only lifecycle events;
- pre-turn memory selection receipts;
- inline memory citations plus an independent post-turn audit;
- local SQLite and Markdown projections for inspectability and portability.

Artifact status: contents inspected read-only. The public MIT repository has a populated `main` branch, local-first storage documentation, Codex and Claude integrations, tests, and release notes.

Evidence limit: the controlled study uses fixed tasks and an LLM evaluator for part of the alignment measurement. The field deployment covers nine developers for one week.

Implementability score: 0.86

Core sources: [MemoSync paper v1](https://arxiv.org/abs/2611.24165v1), [MemoSync repository](https://github.com/SLEEPYBQ/MemoSync)

## Working conclusion

The immediate pattern is release engineering for agent state. Candidate instructions and memories should be proposed, inspected, tested, versioned, and reversible before they shape future actions.
