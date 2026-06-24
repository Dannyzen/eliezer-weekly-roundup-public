# Daily AgenticAI Research Notes - 2026-06-24

## Thesis

The actionable signal today is that continuity and execution modality have to become runtime objects. Coding-agent handoff memory should be an event log with projections, and computer-use reliability should be measured as a matched GUI, CLI, and skill-coverage problem, not as generic agent accuracy.

## Top findings

### ESAA-Conversational turns agent handoff memory into an event log

ESAA-Conversational addresses a real failure in daily coding-agent work: one agent learns goals, decisions, open tasks, and rationale, then another agent starts from a private vendor-specific transcript and loses the operational state.

The proposed shape is simple and implementable. Capture visible conversation turns into an append-only `activity.jsonl`, then project deterministic read models such as `handoff.md`, `state.md`, `decisions.md`, and `tasks.json`. The paper explicitly separates mechanical capture from LLM judgment: the event capture path does not need inference, while durable decisions and tasks are curated intentionally.

Why it matters:

- multi-agent collaboration does not require agent-to-agent chat if every agent can read the same projected state;
- handoff files should be projections from a log, not ad hoc summaries written at the end of a session;
- event IDs, source turns, and projection hashes make conversational memory auditable;
- this fits local-first coding-agent workflows because the log can stay in the workspace.

Stack fit:

- Event-sourced agent runtime
- Memory systems
- Multi-agent orchestration
- Coding-agent continuity and handoff

Practical tools and methods worth exploring now:

- local JSONL or SQLite event stores for conversation turns;
- deterministic projectors for `handoff.md`, `state.md`, `decisions.md`, and `tasks.json`;
- workspace hooks that capture agent-visible turns without granting broad write authority;
- projection tests that prove a known event log regenerates the same handoff state;
- OpenTelemetry trace IDs carried from conversation events into file, git, and tool actions.

Implementability score: 0.88

The thin version is straightforward: append events, project state files, and require agents to consume the projections before acting. The harder version is cross-vendor capture with privacy boundaries, conflict resolution, and replayable curation.

Core source: https://arxiv.org/abs/2606.23752

### GUI vs CLI shows that skill coverage controls computer-use reliability

GUI vs. CLI isolates a question most computer-use benchmarks blur: is a GUI agent better because visual interaction is better, or because the CLI/tool path lacks enough skill coverage?

The benchmark uses 440 desktop tasks across 18 applications and 12 workflow categories. Both modalities receive identical goals, initial states, and final-state verifiers. The results are useful because they separate execution surface from benchmark confounds:

- strongest screen-only GUI agent: 59.1% full pass rate;
- strongest original-skill CLI agent: 48.2%;
- verifier-guided skill-augmented CLI agent: 69.3%.

That means the CLI deficit is not simply weak reasoning. It is often incomplete skill coverage. Once skills are expanded against verifiers, CLI can beat GUI on the same tasks. The product lesson is not "prefer CLI". It is "measure execution surfaces under matched verifiers, then improve the missing skill interface."

Why it matters:

- desktop-agent claims should report GUI-only, CLI-only, and hybrid results on the same tasks;
- skill libraries are execution surfaces, not documentation;
- final-state verifiers are the control point for improving skill coverage;
- a GUI/tool harness should track path choice, skill availability, verification, and recovery separately.

Stack fit:

- Skills as control
- GUI-tool path orchestration
- Agent harness architecture
- Trajectory-aware evaluation

Practical tools and methods worth exploring now:

- matched-task suites with one final-state verifier per task;
- GUI-only, original-skill CLI, augmented-skill CLI, and hybrid baselines;
- skill coverage maps by application, workflow category, and final-state verifier;
- trace labels for `gui_step`, `skill_call`, `verify`, `recover`, and `abstain`;
- held-out verifier-guided skill augmentation before promoting a skill to default retrieval.

Implementability score: 0.78

The evaluation method is implementable now with existing desktop sandboxes and verifiers. Building broad, safe, high-quality skill coverage across applications remains substantial engineering work.

Core source: https://arxiv.org/abs/2606.24551

## Watchlist

OpenThoughts-Agent is a strong open-data signal for training agentic models, but it belongs in a model-training pass rather than today's runtime-state update. PlanBench-XL is also worth revisiting for large-tool planning, especially because it measures retrieval-limited tool visibility and blocked tool paths.

Watchlist sources:

- OpenThoughts-Agent: https://arxiv.org/abs/2606.24855
- PlanBench-XL: https://arxiv.org/abs/2606.22388
