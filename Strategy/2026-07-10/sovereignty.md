# Strategy Sovereignty Analysis, 2026-07-10

## Executive signal

The strongest sovereignty finding today is Prismata’s contextual least-privilege design for web agents. It treats prompt injection as a confinement problem across both observation and capability, not only as malicious text that the model should recognize.

## Prismata confines both what a web agent sees and what it can do

Prismata addresses cross-site prompt injection by deriving task-specific labels over page structure, redacting or restricting untrusted content, and gating actions to the privileges required for the current task. Its core idea is structural: labeling errors should only reduce privilege, and mechanical enforcement should keep untrusted content from expanding the agent’s authority.

The paper evaluates recent web-agent attacks, including adaptive variants. Its main attack setting reports average attack success falling from 85.5% to 0.7% while preserving benign task utility. The broader contribution is the control boundary: a defense should limit both the content exposed to planning and the actions reachable from that content.

Why it matters:
- model-level prompt-injection defenses still ask the model to reason correctly after exposure;
- browser pages mix developer-owned structure, user-generated content, and third-party content in one observation surface;
- least privilege must apply to observations and effects together;
- structural confinement can fail closed when task-policy inference is uncertain.

Fit in the stack:
- agent gateway and execution-control plane;
- untrusted-data boundaries;
- browser and computer-use agent security;
- evidence-to-effect authorization.

## What to implement now

- classify DOM regions by origin and trust class before planner exposure;
- derive an action allowlist from the user’s task and current authenticated surface;
- redact unneeded untrusted content or expose it through a narrow typed read path;
- bind each effectful action to the page element, trust label, task scope, and policy verdict that authorized it;
- add regression fixtures for reviews, comments, ads, messages, and marketplace listings that attempt to trigger off-task actions;
- fail closed when an ambiguous label could widen capability.

Tools and methodologies worth exploring:
- BrowserGym or equivalent structured DOM/action traces;
- Biba-style integrity labels adapted to agent observations;
- Cedar, OPA, OpenFGA, or narrow policy code for task-scoped action allowlists;
- WebArena and WASP-style attack fixtures;
- OpenTelemetry spans connecting content origin, derived label, planner exposure, action request, and effect.

## What remains hard

- dynamic trust derivation over arbitrary sites is meaningful architecture work;
- a redacted observation can still leak adversarial influence through allowed summaries or bounded strings;
- task-derived action policies need good identity and scope resolution before they can safely authorize purchases, messages, permission changes, or credential-bearing flows;
- no public implementation repository was identified during this scan, so the paper is a design reference rather than try-now software.

Implementability score: **0.55**

Core source:
- Prismata: Confining Cross-Site Prompt Injection in Web Agents: https://arxiv.org/abs/2607.08147v1

## Strategic conclusion

Prompt injection will not be solved by better refusal prose. The durable boundary is contextual least privilege: classify what the agent may observe, derive what the task may authorize, and mechanically prevent untrusted content from widening either surface.
