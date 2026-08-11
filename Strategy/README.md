# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-11

### Provenance guards need recoverable denial paths

Summary: POLIS freezes 5,280 multi-agent episodes. A provenance guard produced 0 violations in 384 main-study episodes, blocked 51 attempts, and enabled safe completion in 44. In laundering scenarios, local-state enforcement admitted 22 of 96 violations while provenance enforcement admitted 0 of 96.

Analysis: [daily analysis](2026-08-11/sovereignty.md#multi-agent-governance-needs-provenance-aware-authority-and-a-recoverable-denial-path)
Core sources: [paper](https://arxiv.org/abs/2608.09828v1), [POLIS repository](https://github.com/abdullah-x-bd/polis)
Tools and methodologies worth exploring now: immutable authority roots, derivation chains, attempted-versus-realized effect logs, recoverable denials, laundering tests
Implementability score: 0.82

## Current implication

Authority provenance, denial recovery, delegation rules, and resource visibility are runtime controls, not prompt details.
