# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-13

### Allocate skill evaluations instead of rewriting every candidate

Summary: COBRA-Skills uses a neural reward predictor plus LinearUCB to allocate a fixed evaluation budget across an evolving skill population. The paper reports 55 to 58 percent lower optimization cost than SkillOpt across six benchmarks and three target models.

Analysis: [daily analysis](2026-09-13/reasoning.md#allocate-skill-evaluations-instead-of-rewriting-every-candidate)
Core sources: [COBRA-Skills paper](https://arxiv.org/abs/2609.11682v1), [repository](https://github.com/Jerry-LuP/COBRA-Skills)
Tools and methodologies worth exploring now: candidate digests, frozen optimization sets, explicit evaluation budgets, UCB selection, evidence-grounded mutations, no-skill baselines, dry-run validation
Implementability score: 0.78

### Compress sibling sandbox state during model wait

Summary: AgentZip exploits template-relative and cross-sandbox memory redundancy, prefetches page restores, and schedules compression during LLM wait phases. The paper reports up to 8.7 times lower sandbox-owned memory but provides no public AgentZip implementation.

Analysis: [daily analysis](2026-09-13/reasoning.md#compress-sibling-sandbox-state-during-model-wait)
Core sources: [AgentZip paper](https://arxiv.org/abs/2609.11294v1), [related Zeroboot substrate](https://github.com/zerobootdev/zeroboot)
Tools and methodologies worth exploring now: worker-memory telemetry, fanout sweeps, copy-on-write templates, KSM, zram, zswap, wait-phase scheduling, restore-latency gates
Implementability score: 0.34

## Current implication

Make evaluation budget and worker resource state explicit runtime objects. Skill evolution is usable now with frozen evidence and cost accounting; AgentZip-style compression remains an architecture signal until its prototype or an independent implementation is available.
