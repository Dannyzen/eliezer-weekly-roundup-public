Feature: Sync locking and concurrency safety
  As an operator running automations and manual retries
  I want only one same-week sync to mutate shared state at a time
  So that the weekly notebook and manifest stay consistent under concurrency

  Background:
    Given the sync system stores a per-week lock alongside the manifest

  Rule: Only one same-week sync may hold the mutation lock
    Scenario: Allow only one same-week sync to mutate NotebookLM
      Given two sync processes start for the same week at the same time
      When both processes attempt to acquire the weekly sync lock
      Then only one process should mutate NotebookLM for that week
      And the other process should exit with a clear locked status

  Rule: Crash recovery restores progress without corrupting state
    Scenario: Reclaim a stale lock from a crashed sync
      Given a stale weekly sync lock remains after a crashed process
      When the operator reruns the weekly NotebookLM sync
      Then the stale lock should be reclaimed safely
      And the rerun should resume from the last durable checkpoint
