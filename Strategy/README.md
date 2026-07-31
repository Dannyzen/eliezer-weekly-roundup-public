# Strategy

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Friday, 2026-07-31

### AISPA makes system prompts reviewable policy artifacts

Summary: AISPA audits system-prompt spans across eight user-protection dimensions. In 88 commercial products, roughly 40 percent contained at least one problematic instruction and only about 24 percent covered all dimensions. The expanded public corpus is usable for discovery, but it does not guarantee prompt authenticity or freshness and removes reviewer-source fields.

Analysis: [dated sovereignty analysis](2026-07-31/sovereignty.md#aispa-makes-system-prompts-auditable-governance-artifacts)
Core sources: [paper](https://arxiv.org/abs/2607.28617v1), [System Prompt Index](https://systempromptindex.com/), [public data repository](https://github.com/XiangningLin/SystemPromptIndex)
Implementable now:
- version prompts with source, product, model, date, digest, and approval identity;
- preserve span, dimension, reviewer class, confidence, and methodology version;
- connect protective claims to behavioral tests and problematic instructions to release gates;
- invalidate approvals when prompt semantics change.
Tools, repositories, and methodologies:
- AISPA taxonomy, System Prompt Index, Git diffs, prompt manifests, policy-as-code review, behavioral regression suites
Implementability score: 0.80

## Current implication

A system prompt can shape identity, incentives, action defaults, and user treatment. Treat it as versioned application policy, and never separate an audit result from source authenticity, reviewer identity, methodology, and runtime evidence.
