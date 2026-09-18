# AI Strategy and Sovereignty Analysis: 2026-09-18

## Freshness and evidence boundary

SkillAA was submitted as v1 on 17 September 2026 and first listed by arXiv on 18 September 2026. The primary paper and its public repository were inspected read-only. The repository was not cloned or executed.

## Gate persistent skill changes like code changes

### Finding

SkillAA treats an external skill library as an addressable graph rather than a flat document. Nodes separate when to use a skill, how to execute it, and when not to use it. Typed edges represent prerequisites, enhancements, and observed co-use. Failed and successful trajectories are compared to route a proposed repair to one graph object, or to NO_PATCH when evidence is insufficient or the failure was an execution lapse.

Each edit passes a Local Gate over affected examples. Related edits are rolled back as an atomic group if they break more than they fix. Surviving edits are merged and evaluated by an epoch-level Big Gate before the graph becomes the next committed state. The held-out test set never participates in patch generation or gate decisions.

With gpt-5.6-sol as teacher and student, the paper reports 81.5 percent on SearchQA, 66.7 percent on LiveMathematicianBench, and 91.2 percent on DocVQA, with the highest observed mean in each main setting.

### Why it matters

Persistent skills are executable policy. Blindly rewriting a skill after one failure converts a local mistake into shared future behavior. Safe improvement needs explicit edit targets, evidence, affected-case tests, atomic rollback, and a separate commit decision.

### Fit in the strategy

This extends skill admission control and agent self-improvement governance. The key object is not a better prompt. It is a versioned capability graph whose mutations follow the same discipline as code changes.

### Practical tools and methods worth exploring

- Split each skill into applicability, procedure, exclusion, and dependency objects with stable IDs.
- Preserve execution traces and validated usage records separately.
- Route failures to the smallest authorized edit surface or refuse to patch.
- Derive regression scope from graph reachability and observed usage.
- Require net improvement before commit, then evaluate the committed state on untouched holdouts.
- Store before and after content, evidence, affected examples, gate results, and graph hash in every receipt.

### Artifact status and caveat

The public repository has a populated `main` branch with configurations, benchmark manifests, graph code, scripts, tests, release verification, and local checks. It has no declared license and no releases. Reproduction requires paid API behavior and benchmark data, and the results use the same named model family for teacher and student. Treat the pattern as implementable governance architecture, not an independently replicated score claim.

Implementability score: 0.62

Core source: https://arxiv.org/abs/2609.20455v1
Artifact: https://github.com/Ziqiao-Shang/SkillAA

## Supporting operational signal: usage is inventory, not proof

GitHub added organization and enterprise usage metrics for skills, custom agents, MCP servers, slash commands, and plugins. The API reports top items and distinct-item counts. This is useful for finding what needs governance and evaluation, but interaction counts do not establish correctness, safety, or business value. Join usage telemetry to version, permission, outcome, incident, and rollback receipts before using it as a control signal.

Source: https://github.blog/changelog/2026-09-17-agentic-cli-customizations-now-in-the-usage-metrics-api

## Practical next steps

1. Give skill components stable object IDs and separate applicability from procedure.
2. Add affected-case regression gates and atomic rollback before any automated skill mutation.
3. Join usage counts to exact skill version, authority, outcome, and incident evidence.
