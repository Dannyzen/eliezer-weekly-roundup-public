# Story: Report-linked NotebookLM podcast MVP

## User story
As an operator, I want to point the repo at a report markdown file and have the system create or reuse a remote NotebookLM notebook, generate an audio overview from that report, add the audio link back into the markdown, and optionally push the result to GitHub.

## Scope
- one command for one report markdown path
- derive a stable report identity from the markdown file path and title
- create or reuse a dedicated NotebookLM notebook for that report
- upload the report content and its cited URLs as NotebookLM sources
- generate and download one podcast artifact for the current report source revision
- write the podcast file next to the report markdown
- update the markdown with a managed audio section linking to the podcast
- persist a local manifest that records notebook and artifact ids
- optionally commit and push the changed markdown, audio file, and manifest to GitHub

## Non-scope
- full weekly orchestration across all reports
- rich public sharing workflows
- multi-user approval workflows
- syncing every BDD scenario already drafted in the resilience suite
- browser-driven authentication UX inside this repo

## Business rules
- the report markdown is the source of truth
- the managed audio block in markdown must be idempotent and replaceable
- the report source digest must ignore the managed audio block so reruns are stable
- if the source digest has not changed and the audio file already exists, the command should reuse the existing audio instead of generating a new podcast
- GitHub push must be opt-in
- the manifest must be committed with pushed output so notebook identity stays durable across machines

## MVP command surface
- `uv run eliezer-roundup generate-podcast <report_path>`
- optional flags:
  - `--push`
  - `--instructions <text>`
  - `--language <code>`
  - `--audio-format <deep-dive|brief|critique|debate>`
  - `--audio-length <short|medium|long>`
  - `--timeout-seconds <int>`

## Local state
Suggested manifest file: `.notebooklm-sync.json`

Per report entry should record:
- report path
- notebook id
- notebook title
- report source digest
- remote source ids
- audio artifact id
- audio path
- updated-at timestamp

## Acceptance targets
- a report markdown can be parsed for title, normalized source content, and cited URLs
- a managed audio section can be inserted and replaced deterministically
- the orchestrator can create notebook, add sources, generate audio, update markdown, and save manifest using a fake NotebookLM gateway in tests
- a no-op rerun with unchanged digest reuses the existing audio path
- the CLI exposes the operator command through uv
