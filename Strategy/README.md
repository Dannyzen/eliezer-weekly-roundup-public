# Strategy

The latest daily scan is 2026-11-28. Its thesis is that source channels and evaluation generators are part of the authority and evidence boundary.

## Latest findings

### Bind workspace context to source authority

Summary: Pydantic AI v2.77.0 keeps repository files below operator authority out of model instructions. Low-authority skills, memory, and repository context arrive through tools or attributed data.

Analysis: [Bind workspace context to source authority](2026-11-28/sovereignty.md#1-bind-workspace-context-to-source-authority)

Core sources: [Pydantic AI v2.77.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.77.0), [authority-aware workspace PR](https://github.com/pydantic/pydantic-ai/pull/11837)

Implementable now:
- per-file authority and provenance
- instruction-channel admission controls
- tool-mediated low-authority reads
- planted-instruction channel tests

Implementability score: **0.93**

### Evaluate monitors across attack-policy envelopes

Summary: The same held-out monitor produced false-negative rates from 0.5% to 23.0% depending on attack method and optimization. One weak attacker can create false confidence.

Analysis: [Evaluate monitors across attack-policy envelopes](2026-11-28/sovereignty.md#2-evaluate-monitors-across-attack-policy-envelopes)

Core source: [Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934v1)

Implementable now:
- versioned attack policies and budgets
- proxy-monitor development with a held-out target
- method and optimization sweeps
- full false-negative envelopes with clean utility

Implementability score: **0.78**

## Browse

- [Daily synthesis](../roundups/2026-11-28.md)
- [Dated Strategy analysis](2026-11-28/sovereignty.md)
- [November 27 weekly synthesis](../roundups/2026-11-27.md)
- [Untrusted data boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
- [Evaluation containment](evaluation-containment-control-plane/evaluation-containment-control-plane.md)
