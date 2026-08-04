# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-04

### Shared-workspace mutation must invalidate stale agent state

Summary: SWE-Touch finds user-attributed repository changes in 59.0 percent of analyzed SWE-chat sessions. Validated Counter-Edits lower average resolve rate by 7.7 percentage points across nine models, and 63.3 percent of failed runs retain the conflicting code.

Analysis: [daily analysis](2026-08-04/reasoning.md#swe-touch-makes-shared-workspace-mutation-a-benchmarked-event)
Core sources: [paper](https://arxiv.org/abs/2608.02499v1), [repository](https://github.com/Trae1ounG/SWE-Touch), [dataset](https://huggingface.co/datasets/Trae1ounG/SWE-Touch)
Implementable now:
- add revision-aware reads and writes;
- emit external-mutation events;
- require conflict reconciliation and targeted revalidation.
Tools, repositories, and methodologies:
- SWE-Touch, Harbor, Mini-SWE-Agent, LiteLLM, filesystem event journals
Implementability score: 0.82

### Telemetry monitors are escalation signals, not correctness proof

Summary: A 2,823-episode study shows that one-class telemetry monitors can detect some trajectory drift cheaply, but organic fabrication transfer is weak and deployment shift can cause high false alarms.

Analysis: [daily analysis](2026-08-04/reasoning.md#telemetry-monitors-can-be-cheap-but-only-after-local-calibration)
Core sources: [paper](https://arxiv.org/abs/2608.02464v1), [traces and results](https://github.com/sunnydubey1111/agent-trajectory-sentinel)
Implementable now:
- emit typed step telemetry;
- calibrate healthy baselines per deployment;
- keep completion and source-grounding checks deterministic.
Tools, repositories, and methodologies:
- OpenTelemetry, OpenInference, CUSUM, Mahalanobis baselines, deterministic verifiers
Implementability score: 0.64

### Capability routing should choose the smallest sufficient runtime

Summary: Cloudflare Computer presents one SQLite-backed workspace across isolate and Linux-container backends, with common file and execution tools plus gated, audited operations.

Analysis: [daily analysis](2026-08-04/reasoning.md#cloudflare-computer-routes-capability-to-the-smallest-sufficient-runtime)
Core sources: [official changelog](https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/), [repository](https://github.com/cloudflare/computer)
Implementable now:
- classify actions by runtime capability;
- default narrow work to isolates;
- require a receipt for container escalation.
Tools, repositories, and methodologies:
- `@cloudflare/computer`, Durable Objects, DOFS, FUSE, capability manifests
Implementability score: 0.76

## Current implication

One event contract should bind workspace revisions, monitor alarms, backend escalation, and validation to the same trajectory identity. Without that binding, each feature can observe or change a different world.
