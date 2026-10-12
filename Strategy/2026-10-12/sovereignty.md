# Daily Strategy Research: 2026-10-12

## Scope

This scan covers the arXiv batch first listed on Monday, October 12, 2026. Both selected papers are immutable v1 submissions from Friday, October 9, 2026. No external source code was executed.

## Thesis

Agent authority crosses two under-governed boundaries: model-generated arguments entering tools, and persistent artifacts re-entering future sessions. Both boundaries need evidence-bearing gates before effects occur.

## ToFu: compile tool metadata into security tests

ToFu treats tool metadata as a partial semantic specification. It maps argument descriptions and schemas to a 74-sanitizer, CWE-guided corpus, generates schema-valid fuzzing harnesses, and checks runtime observations or sanitized outcomes.

Across 273 open-source MCP servers containing 3,405 tools, ToFu reports 253 verified bugs affecting 343 tools in 118 servers. The failures include path traversal, log injection, exfiltration, and command bypass.

### Why it matters

Schemas prove shape, not safe meaning. An argument can satisfy JSON Schema and still direct a tool outside its documented path, network, data, or command boundary. Tool admission should therefore compile metadata into negative tests and observed-effect assertions.

### Strategy fit

- Agent gateway governance
- Tool admission control
- MCP supply-chain testing
- Context-to-execution integrity

### Practical methods worth exploring

- Map tool argument descriptions to path, URL, SQL, shell, identifier, and scope classes.
- Generate schema-valid adversarial inputs before catalog admission.
- Observe filesystem, process, and network effects where the runtime permits introspection.
- Bind every finding to the exact tool version, metadata snapshot, sanitizer, input, and effect trace.
- Re-run the suite when tool metadata, implementation, permissions, or dependencies change.

### Evidence and caveat

The paper provides the full sanitizer corpus and evaluated-repository list in its appendices, but no public implementation artifact was found. The current method fuzzes one tool interface at a time. Stateful multi-call attacks and coverage inside external components such as Chromium require additional instrumentation.

Implementability score: **0.72**

Core source:
- [ToFu paper v1](https://arxiv.org/abs/2610.13651v1)

Duplicate status: extension of prior MCP admission and harness-security work. The new primitive is compiling tool metadata into semantic oracles.

## SkillRelayGuard: restore artifact provenance before reuse

SkillRelayBench models cross-session attacks carried by files, configurations, cached data, and database records. It includes 270 adversarial cases from 30 two-stage scenarios across ten domains.

Across seven model configurations using Codex CLI, Gemini CLI, and Claude Code, attack success ranges from 46.7% to 77.4%, while full attack-chain success ranges from 35.6% to 61.1%. SkillRelayGuard restores artifact origin and supporting evidence at read time, then adds advisory review before execution. Across three guarded settings, it reduces aggregate attack success from 69.5% to 10.9% and attack-chain success from 54.8% to 10.0%, while legitimate task completion rises from 79.6% to 87.5%.

### Why it matters

A fresh conversation is not a fresh trust boundary when old artifacts survive. Persistent objects can carry instructions, unauthorized data scope, and false evidence into later tasks. Provenance must travel with the object and return to the agent when the object is read.

### Strategy fit

- Persistent-state agent control
- Memory authority
- Untrusted data boundaries
- Pre-execution review

### Practical methods worth exploring

- Record producer skill, session, principal, source inputs, intended scope, and supporting evidence for every retained artifact.
- Restore that context when a later skill reads the artifact.
- Treat artifact content as data until a current task authorizes an effect.
- Review the exact proposed operation against the current request and artifact lineage before execution.
- Preserve guard advice, agent decision, final request, and external receipt as one evidence chain.

### Evidence and caveat

The public [SkillRelay repository](https://github.com/Dianshu-Liao/SkillRelay) has a populated benchmark and implementation tree with 15,197 paths, Docker isolation, dry-run support, and explicit output evidence. GitHub reports no license. The study relies on model judges, stochastic agent runs, one guarded configuration per scaffold, and a Codex-only ablation. The repository also states that operation review is advisory and does not cover arbitrary local file changes, local SQLite publication, or model-gateway traffic.

Implementability score: **0.79**

Core sources:
- [SkillRelay paper v1](https://arxiv.org/abs/2610.13227v1)
- [SkillRelay repository](https://github.com/Dianshu-Liao/SkillRelay)

Duplicate status: extension of persistent-state and memory-authority research. The new control is read-time provenance restoration paired with pre-effect review.

## Working conclusion

Schemas and persisted files are both representations, not authority. Promote them into action only after semantic checks, provenance restoration, and effect-level review bind the representation to the current request.
