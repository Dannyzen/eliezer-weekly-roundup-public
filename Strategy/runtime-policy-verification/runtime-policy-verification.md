# Runtime Policy Verification

Last updated: 2026-11-18

## Overview

Agent governance has a missing runtime layer. Policies are usually written as long natural-language documents, while execution gates need fast, attributable decisions. The Verifier Foundation Model (VFM) shows a credible bridge: encode the agent trace once, score hundreds of atomic policy criteria in parallel, and return an independent YES, NO, or N/A verdict for each rule.

This is the strongest finding of the week because it turns policy text into an operational verification surface. ReTrace reduces repeated planning cost, HEAMS broadens memory evaluation, CapLite constrains prompt-injected writes, and Copilot Evals makes regression testing accessible. VFM sits underneath all of them as a reusable pre-execution or post-step policy check.

## Core innovation

VFM uses tree attention over one shared context and target. Each policy criterion is an isolated branch that can see the trace but cannot see other criteria. A small classification head produces per-rule probabilities for YES, NO, and N/A.

The paper reports:

- 394,000 training tuples covering more than 321,000 distinct criterion strings;
- 0.885 trace-level FAIL F1 on 543 held-out DynaBench dialogues, versus 0.720 for DynaGuard-4B;
- the violated rule ranked first on 97.6 percent of failing traces and within the top three on all failing traces;
- 0.946 FAIL F1 when the top three suspected rules were escalated to a 26B chain-of-thought judge;
- 1.81 seconds to score 1,000 criteria against a roughly 4,000-token trace on one H100, using 10.5 GB of VRAM.

The important innovation is attribution. A generic safety score says a trace looks risky. VFM identifies which rule appears violated, which makes escalation, approval, audit, and policy repair practical.

## Why it matters

Prompt instructions are weak enforcement. Static policy reviews are stale as soon as models, tools, prompts, skills, or runtime context change. Large generative judges can reason about policy, but they are expensive and slow when every trace must be checked against hundreds of rules.

VFM suggests a two-stage control plane:

1. A compact verifier screens every action or completed step against the active policy bundle.
2. Uncertain or high-risk criteria escalate to a stronger judge or a human approval gate.

This changes natural-language policy from passive documentation into executable monitoring. It also keeps policy authorship separate from the model being governed.

## Fit in the agentic stack

VFM belongs in the Strategy control plane between trace capture and action authority.

```text
agent proposal or trace
        |
        v
canonical policy bundle -> atomic criteria
        |
        v
VFM per-rule verdicts and confidence
        |
        +--> allow low-risk satisfied actions
        +--> deny deterministic violations
        +--> escalate uncertain or high-impact rules
        |
        v
approval or execution receipt with rule-level evidence
```

It complements existing layers:

- **Capability admission** decides which model, skill, MCP server, or tool may enter the system.
- **Owned evals** decide whether a configuration deserves promotion before deployment.
- **Runtime policy verification** checks each live trace against the policy bundle.
- **Deterministic execution control** remains the final authority for identity, arguments, data scope, and side effects.

VFM should inform an execution gate. It should not become the sole authority for irreversible actions.

## What to try now

### 1. Build a canonical atomic policy bundle

Rewrite one real workflow policy as short, positively phrased, trace-checkable questions. Keep stable IDs, owners, risk classes, versions, and deterministic fallback behavior. Retain the original source clause for every decomposition.

### 2. Run VFM in shadow mode

Use the released `spitis/vfm` package and VFM-0.6B or VFM-4B checkpoint against retained traces. Do not block actions initially. Measure false passes, false blocks, N/A rates, latency, and rule localization against human labels.

### 3. Add tiered escalation

Send high-risk violations, low-confidence results, and N/A verdicts to a stronger judge or human reviewer. The paper's DynaBench cascade is the useful pattern: the compact verifier narrows a large policy bundle to the few rules worth expensive review.

### 4. Bind verdicts to receipts

Store the policy bundle version, criterion IDs, model and checkpoint identity, thresholds, verdict probabilities, escalated decision, and eventual effect. This makes a runtime decision replayable when policy or model behavior changes.

### 5. Promote only measured policy families

Calibrate per domain before enforcement. Financial, medical, privacy, tool-use, and data-retention rules have different false-pass costs. One global threshold is unlikely to be defensible.

## Practical tools and methodologies

- [spitis/vfm](https://github.com/spitis/vfm): Apache-2.0 code, benchmark preparation, evaluation scripts, tests, and inference API.
- [VFM-0.6B](https://huggingface.co/spitis/VFM-0.6B): lower-cost checkpoint for local shadow evaluation.
- [VFM-4B](https://huggingface.co/spitis/VFM-4B): stronger checkpoint used for the main runtime results.
- [CriteriaBank](https://huggingface.co/datasets/spitis/CriteriaBank): pretraining corpus and a reference for criterion shape.
- DynaBench-style trace-level FAIL scoring plus top-k rule localization.
- Owned red-team traces with paired compliant and violating variants.
- Per-policy-family threshold calibration and human-reviewed escalation queues.

Artifact status: repository contents, README, benchmark manifests, model links, and tests were inspected read-only. No external source was cloned, installed, imported, built, or executed.

## Implementation complexity

**Medium to high.** The inference API is straightforward, and the public repository includes weights, tests, manifests, and evaluation scripts. Reliable use requires policy decomposition, domain labels, threshold calibration, trace normalization, a low-latency serving path, escalation, and receipt storage.

A useful shadow-mode pilot is normal engineering. A production enforcement layer is operationally sophisticated.

## Weakest point and guardrail

The unflattering fact is that VFM still produced 19 to 26 percent false passes on gold violations in the real INSURE-Dial evaluation, often with high confidence. CriteriaBank pretraining also did not help that domain after finetuning, and the paper says zero-shot calibration is not yet strong enough.

This is survivable because the strongest use is triage and localization, not autonomous final authority. The guardrail is concrete: start in shadow mode, calibrate on owned traces, escalate high-risk or uncertain rules, and keep deterministic authorization outside the verifier.

## Implementability score

**0.76**

The model, data, tests, and inference path are public and usable now. Production enforcement still needs domain-specific evaluation, serving infrastructure, policy lifecycle management, and deterministic fallback controls.

## Strategic implications

Danny's product model should treat policy as a versioned runtime object, not prose attached to a release. The durable system has four linked artifacts:

1. the source policy;
2. an atomic criterion bundle with stable identities;
3. runtime verdicts tied to exact traces and effects;
4. an escalation or execution receipt.

This supports a product position stronger than generic guardrails. The system can show which rule was active, what evidence triggered it, how uncertainty was handled, and which authority allowed or denied the effect.

The next product question is whether every material action can produce a rule-level verification receipt before authority is exercised.

## Core sources

- [Runtime Verification of Multiple Natural Language Criteria for Agent Governance, arXiv v1](https://arxiv.org/abs/2611.23074v1)
- [VFM source repository](https://github.com/spitis/vfm)
- [NeurIPS 2026 paper listing](https://neurips.cc/virtual/2026/loc/atlanta/session/137656)
- [CriteriaBank dataset](https://huggingface.co/datasets/spitis/CriteriaBank)
