# AgenticAI Daily Analysis - 2026-07-23

## Verdict

The strongest implementation signal is that agent work should be graded at two boundaries before it earns authority: the capability package before loading, and the produced artifact after execution.

OpenSkillRisk makes skill admission measurable against real marketplace packages. DocOps makes final document state deterministically testable instead of trusting screenshots or model judgment.

## Scan boundary

- arXiv exposed a real Thursday, 2026-07-23 listing section across AI, language, machine learning, software engineering, security, multi-agent systems, distributed systems, and human-computer interaction.
- OpenSkillRisk and DocOps were submitted on 2026-07-22 and first listed on 2026-07-23.
- Primary PDFs were downloaded as documents on Bigs and checked with `pdftotext -layout`.
- Hugging Face Daily Papers, GitHub Trending, official web releases, and GitHub metadata were checked. `blogwatcher-cli` was unavailable, so the scan did not depend on it.
- Public artifacts were inspected read-only through GitHub metadata, recursive trees, README files, licenses, and Hugging Face metadata. No external repository was cloned, installed, built, imported, or executed.

## Skill safety needs end-to-end admission tests

Core sources: [OpenSkillRisk paper](https://arxiv.org/abs/2607.20121v1), [repository](https://github.com/Miaow-Lab/OpenSkillRisk), [dataset](https://huggingface.co/datasets/Miaow-Lab/OpenSkillRisk)

Submission: 2026-07-22 13:24:09 UTC. First listed: 2026-07-23.

### What it found

OpenSkillRisk packages 263 risky skills from public marketplaces into controlled tasks and sandboxes. The set contains 139 unconditionally malicious skills and 124 context-dependent risky skills across seven threat classes: control-plane hijacking, authority expansion, data harvesting, execution bootstrapping, persistence implantation, outbound exfiltration, and external state manipulation.

The study evaluates three mainstream CLI harnesses and thirteen models. No tested configuration is reliable. The safest reported configurations still execute unsafe actions in about 17 percent of cases. Recognition is not intervention: one Gemini CLI configuration reports 72.62 percent awareness while still producing a 26.62 percent attack success rate.

A generated guard skill helps only when explicitly loaded. Passive loading is weak. Active loading also raises average over-defense on 40 benign skills from 1.88 percent to 22.50 percent. The result argues against treating another prose skill as the main safety boundary.

The public MIT repository has a populated main branch, benchmark runners, policy and judging code, sandbox builders, and a separately hosted dataset. Full evaluation requires isolated runtime setup and provider credentials. The artifact was inspected read-only, not executed.

### Why it matters

Static review, skill metadata, and isolated detonation each catch different failures. The admission contract should combine them, then verify that runtime policy intervenes before the first unsafe effect. A warning emitted after an unsafe artifact exists is not safety.

### Fit in the stack

- **Skills as control:** skills need identity, static review, sandbox detonation, composition tests, and runtime admission.
- **Harness evaluation:** score recognition, intervention timing, unsafe effects, completion, and over-defense separately.
- **Supply chain:** a real marketplace package is evidence, not trusted authority.
- **Execution control:** enforce side-effect policy below the skill prompt.

### Implementable now

1. Import the seven-class taxonomy into the skill registry.
2. Build a small local benchmark from approved, synthetic, and quarantined packages.
3. Run packages with fake credentials, marker files, network traps, and event receipts.
4. Grade the first unsafe attempted effect, not only final text.
5. Require explicit runtime policy for authority expansion, persistence, exfiltration, and remote state changes.

Tools and methodologies worth exploring:

- OpenSkillRisk, SkillSpector, sandbox detonation, fake-secret canaries, syscall and network traces, policy-as-code, approval replay

Implementability score: **0.82**

The benchmark and dataset are public and licensed. The score stays below 0.9 because faithful evaluation needs provider credentials, isolated sandboxes, and local policy mappings.

## Document agents need deterministic artifact verification

Core sources: [DocOps paper](https://arxiv.org/abs/2607.19865v1), [repository](https://github.com/icip-cas/DocOps), [project page](https://docopsbench.github.io)

Submission: 2026-07-22 07:52:59 UTC. First listed: 2026-07-23.

### What it found

DocOps treats Word, Excel, PowerPoint, and PDF files as stateful artifacts. Its 210 tasks span 50 atomic edits, 40 short compositions, 60 single-document workflows, and 60 cross-document workflows. Each task carries a deterministic verifier that checks final native state, including validity, formulas, styles, outlines, bookmarks, and structural metadata.

The best reported model-and-harness configuration, GPT-5.5 with Codex and document skills, passes 0.671 of all tasks. Performance falls toward zero on complex long-range workflows. The analysis identifies three recurring failures: long-term state tracking collapse, shallow semantic verification, and destructive flattening of document structure.

The public Apache-2.0 repository is substantial: 210 Harbor tasks, deterministic tests, document-operation skills, wrappers for four harnesses, and bundled Docker image archives. It has 16,055 recursive tree entries. This is a reproducible benchmark, but the runtime footprint is material and the paper does not cover collaborative or live-service workflows.

### Why it matters

A document agent can produce plausible visible text while damaging formulas, metadata, styles, references, or unrelated regions. Release evidence should come from the native artifact, not the agent narrative or a screenshot.

### Fit in the stack

- **Trajectory evaluation:** pair process traces with deterministic final-state checks.
- **Artifact release:** bind verifier output to the exact document digest.
- **Harness comparison:** hold model, tasks, skills, and budget constant while changing the harness.
- **Regression testing:** preserve before-and-after artifacts plus invariant failures.

### Implementable now

1. Select ten tasks matching current document workflows.
2. Run a fixed model with and without document skills across two harnesses.
3. Add invariants for untouched formulas, styles, bookmarks, metadata, and object trees.
4. Store source digest, output digest, verifier version, failed assertions, and trace ID.
5. Promote passing tasks into the permanent release suite.

Tools and methodologies worth exploring:

- DocOps, Harbor, native-format parsers, structural diffing, deterministic tests, artifact digests, skill-on versus skill-off ablations

Implementability score: **0.88**

The benchmark is complete, licensed, and directly usable. The main cost is the container and document-tooling footprint, not missing methodology.

## Watchlist not promoted

- [JANUS](https://arxiv.org/abs/2607.19913v1) predicts delayed safety risk from partial trajectories. It is promising, but requires guard-model training and does not displace today’s more immediately testable admission and artifact gates.
- [ChainWatch](https://arxiv.org/abs/2607.19432v1) models multi-step MCP attacks with a six-stage kill chain and HMM, but demonstrates only five representative scenarios and exposes no verified implementation artifact.
- [NEXUS](https://arxiv.org/abs/2607.19356v1) reports a fast four-way runtime intervention policy, but the abstract page has an anomalous May submission timestamp for a July identifier and was not promoted without cleaner source chronology.

## Working conclusion

Agents should not earn trust from package descriptions or polished outputs. Admit capabilities through sandboxed effect tests, then release artifacts through deterministic native-state checks.
