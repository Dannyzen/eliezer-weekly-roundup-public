# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-08

The governance signal is consistent: models can propose estimates, delegation, skills, and memories. Runtime-owned contracts decide what executes or persists.

### Treat time budgets as runtime contracts

Summary: AgentTime shows that duration instructions do not reliably produce useful work for the requested period. External schedulers need to own deadlines, cancellation, progress evidence, and active-work accounting.

Analysis: [daily strategy analysis](2026-10-08/sovereignty.md#treat-time-budgets-as-runtime-contracts)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.09944v1), [repository](https://github.com/michaelofengenden/agenttimebench)
Tools and methodologies worth exploring now: scheduler deadlines, heartbeats, cancellation, active-versus-idle metrics, score-versus-time curves
Implementability score: 0.90

### Make concurrency an earned execution mode

Summary: Dynamic concurrency helped some long, decomposable coding tasks and harmed bounded ones. Parallel execution needs an explicit admission rule and parent-owned integration proof.

Analysis: [daily strategy analysis](2026-10-08/sovereignty.md#make-concurrency-an-earned-execution-mode)
Durable topic: [Governed Workflow Substrates](governed-workflow-substrates/governed-workflow-substrates.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.10263v1), [trajectory artifact](https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact)
Tools and methodologies worth exploring now: decomposability checks, shared-state risk scoring, single-writer lanes, join deadlines, cumulative gates
Implementability score: 0.86

### Require admission evidence before skill reuse

Summary: Passive downstream reuse leaves many skills untested. SkillSandbox turns admission into a paired execution test in a novel scenario.

Analysis: [daily strategy analysis](2026-10-08/sovereignty.md#require-admission-evidence-before-skill-reuse)
Durable topic: [Skill Admission Control](skill-admission-control/skill-admission-control.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.10088v1), [implementation snapshot](https://anonymous.4open.science/r/skillsandbox-647C/)
Tools and methodologies worth exploring now: versioned skill claims, synthesized scenarios, paired executions, rejection reasons, reversible admission
Implementability score: 0.74

### Bind learned memory to source artifacts

Summary: Artifact-grounded memory can improve quality and cost, but learned relations need source IDs, versions, lineage, and supersession state before they become durable authority.

Analysis: [daily strategy analysis](2026-10-08/sovereignty.md#bind-learned-memory-to-source-artifacts)
Durable topic: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md)
Core source: [paper v1](https://arxiv.org/abs/2610.10091v1)
Tools and methodologies worth exploring now: origin-bound records, source-version checks, claim confidence, supersession, contradiction tests
Implementability score: 0.65

## Current implication

External contracts should own time, delegation, skill admission, and memory authority. This keeps autonomy measurable, reversible, and reviewable.

Latest roundup: [2026-10-08](../roundups/2026-10-08.md).
