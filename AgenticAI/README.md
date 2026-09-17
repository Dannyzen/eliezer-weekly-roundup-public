# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-17

### Make deceptive task evidence a first-class evaluation dimension

Summary: AgentLSD evaluates six models on 11 web CTF challenges with paired clean and contaminated evidence. Clean agents captured 41 percent of flags; traps added about 20 turns and 2,000 reasoning tokens even when the final answer remained correct. Capability evaluation must vary evidence integrity, not only instructions.

Analysis: [daily analysis](2026-09-17/reasoning.md#make-deceptive-task-evidence-a-first-class-evaluation-dimension)
Core source: [AgentLSD paper](https://arxiv.org/abs/2609.19140v1)
Tools and methodologies worth exploring now: [AgentLSD](https://github.com/Golim/agent-lsd), paired clean-versus-contaminated fixtures, deterministic trap IDs, delivery telemetry, evidence-observation receipts
Implementability score: 0.88

### Treat tool progress as serving telemetry

Summary: Letting running tools report progress made cache-decision signals several times to an order of magnitude more accurate than pre-call predictors and reduced post-tool p90 TTFT by about 20.8 percent against LRU. The serving runtime should read tool lifecycle state without adding it to model context.

Analysis: [daily analysis](2026-09-17/reasoning.md#treat-tool-progress-as-serving-telemetry)
Core source: [tool-progress serving paper](https://arxiv.org/abs/2609.18849v1)
Tools and methodologies worth exploring now: [MCP progress](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress), OpenTelemetry span events, [Exgentic traces](https://huggingface.co/datasets/Exgentic/agent-llm-traces), vLLM, SGLang, Mooncake, Dynamo, TensorRT-LLM
Implementability score: 0.72

### Design one interface with explicit meaning for both readers

Summary: Affora's three controlled studies separate visual freedom from the declared controls, relationships, and state available to computer-use agents. The primary comparison improved completion by about 23 percentage points over baseline. Agent compatibility should be an executable property of the shared interface.

Analysis: [daily analysis](2026-09-17/reasoning.md#design-one-interface-with-explicit-meaning-for-both-readers)
Core source: [Affora paper](https://arxiv.org/abs/2609.19125v1)
Tools and methodologies worth exploring now: semantic HTML, ARIA and platform accessibility APIs, stable control identity, explicit state transitions, executable completion and recovery checks
Implementability score: 0.78

## Current implication

Do not make the model infer state that the environment already owns. Expose trustworthy progress and interface meaning to the runtime, while testing how adversarial evidence changes the trajectory.
