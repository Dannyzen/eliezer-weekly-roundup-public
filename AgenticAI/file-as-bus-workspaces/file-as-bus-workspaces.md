# File-as-Bus Workspaces

## Overview

The strongest finding from the last 7 days is that durable workspace state is becoming the real substrate for serious long-horizon agents.

The clearest proof point is **AiScientist**. The paper and repo both make the same argument: long-horizon performance is not mainly blocked on another increment of local reasoning quality. It is blocked on whether the system can preserve evolving project state across comprehension, planning, implementation, experimentation, debugging, and verification without collapsing into transcript soup.

The key move is a **permission-scoped File-as-Bus workspace**. The orchestrator keeps only thin control state: stage summaries, directives, and a compact workspace map. Specialists repeatedly re-ground on durable artifacts such as plans, code, experiment logs, paper analyses, and validation outputs. That is a much better default than asking every handoff to compress the project back into chat.

## Core innovation

The innovation is not “use files.” That part is obvious.

The real innovation is treating files as the **coordination bus** and the **system of record**:
- a top-level orchestrator keeps control thin instead of carrying the whole run in active context
- a compact workspace map gives agents a lightweight index into the run state
- specialists read only the artifacts relevant to their task instead of inheriting giant conversational residue
- artifact regions are permission-scoped so multi-agent work does not silently stomp on itself
- implementation, experimentation, and validation outputs remain inspectable after the run ends

This produces what the paper calls **thin control over thick state**.

## Why it matters

This matters because most long-running agents fail for boring infrastructure reasons:
- important decisions are trapped inside one agent’s short-lived context window
- later agents cannot tell which plan or result is authoritative
- experiment evidence is not preserved in a way that changes later decisions
- verification happens against stale summaries instead of current artifacts
- operators cannot resume, diff, or audit a run without replaying the whole conversation

AiScientist shows that this is not a side concern. It is a major performance lever.

The paper reports:
- **33.73 average PaperBench score**
- **81.82 Any Medal% on MLE-Bench Lite**
- removing File-as-Bus drops PaperBench by **6.41 points**
- removing File-as-Bus drops MLE-Bench Lite Any Medal% by **31.82 points**

That is why this won the week over other strong findings. It changes how the runtime should be built, not just how one subsystem should be tuned.

## How it fits into the agentic stack

### Orchestration layer
The orchestrator becomes a stage manager, not a giant memory blob. It advances the workflow, assigns tasks, and checks verification gates.

### State layer
The workspace becomes durable external state with explicit artifact boundaries, instead of chat being the hidden source of truth.

### Memory layer
File-as-Bus is a practical form of external memory with provenance, inspectability, and low ambiguity about what changed.

### Observability layer
Artifact histories, logs, and validation bundles create a much better replay and audit surface than a raw transcript alone.

### Multi-agent coordination layer
Permission-scoped write regions and artifact contracts reduce silent interference between specialists.

## What is implementable now

You can apply the pattern immediately:
- create a `workspace-map.md` or equivalent manifest that lists authoritative artifacts and their roles
- require every delegated task to declare a read set, write set, and verification target
- store plans, experiment results, debugging notes, and decision logs as first-class files
- keep coordinator summaries short and regenerate them from artifacts when possible
- separate append-only evidence logs from editable planning files
- permission-scope which agents may edit summaries, plans, code, or validation outputs
- finish runs with an exportable validation bundle that can be resumed or audited later

## What remains conceptual

Several pieces still need deeper work:
- portable conventions for workspace-map schemas across different agent runtimes
- cleaner artifact contracts for many-agent parallelism at larger scale
- stronger automatic verification that summaries faithfully reflect artifact state
- unification of workspace artifacts, trace telemetry, and benchmark evidence into one evidence plane
- better patterns for spanning local files, object stores, and remote sandboxes without losing legibility

## Practical tools, repos, or methodologies worth trying now

### Tools and repos
- [AiScientist repo](https://github.com/AweAI-Team/AiScientist)
- [AiScientist paper](https://arxiv.org/abs/2604.13018)
- [PaperBench](https://github.com/openai/frontier-evals/tree/main/project/paperbench)
- [MLE-Bench](https://github.com/openai/mle-bench)

### Methodologies
- artifact-first delegation
- stage-gated orchestration
- workspace maps as the run index
- permission-scoped write regions
- append-only experiment and validation logs
- progressive disclosure of thick state instead of giant handoff prompts

## Implementation complexity

Medium.

This does not require a frontier-model breakthrough. It requires runtime discipline: explicit artifact contracts, workspace indexing, write permissions, verification gates, and operators who treat the filesystem as the coordination surface instead of a byproduct.

## Implementability score

0.92

## Strategic implications for this stack

This reinforces a useful worldview update: **the moat is shifting from prompt cleverness to state architecture**.

Implications:
- the product boundary for serious agents is increasingly the workspace/runtime design, not the chat shell
- long-horizon systems should be designed around recoverability, inspectability, and artifact continuity
- multi-agent systems become much more credible when their collaboration is visible on disk instead of hidden in context windows
- the right question is not “how do I make the agent remember more?” but “what state deserves to become durable, inspectable, and shared?”
- sovereignty and reliability both improve when project state is legible to operators and portable across runtimes

## Core source links

- AiScientist paper: https://arxiv.org/abs/2604.13018
- AiScientist HTML paper: https://arxiv.org/html/2604.13018v1
- AiScientist repo: https://github.com/AweAI-Team/AiScientist
- AiScientist README: https://raw.githubusercontent.com/AweAI-Team/AiScientist/main/README.md

## Especially useful secondary sources

- Hugging Face Daily Papers listing for the release-week signal: https://huggingface.co/papers
- PaperBench as the reproduction benchmark context: https://github.com/openai/frontier-evals/tree/main/project/paperbench
- MLE-Bench as the long-horizon engineering benchmark context: https://github.com/openai/mle-bench

## Working conclusion

If a long-horizon agent system cannot survive the loss of its transcript, it is not really stateful. File-as-Bus wins because it makes the durable workspace—not the conversation—the thing that remembers.