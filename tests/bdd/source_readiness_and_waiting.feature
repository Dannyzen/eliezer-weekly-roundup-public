Feature: Source readiness, bounded waiting, and publication blocking
  As the operator waiting for NotebookLM ingestion to settle
  I want readiness polling to resume safely and block incomplete publication
  So that source processing lag never creates duplicate uploads or premature publication

  Background:
    Given attached sources have remote readiness states

  Rule: Waiting is bounded and resumable
    Scenario: Time out waiting for a required source that never becomes ready
      Given the current week has attached sources that are still processing
      And one required source remains unready past the configured readiness deadline
      When the operator runs the weekly NotebookLM sync
      Then the run should end in a retryable degraded state
      And already attached sources should remain checkpointed without re-upload

    Scenario: Resume readiness polling after a crash without reattaching sources
      Given all required sources are already attached for the current week
      And readiness polling stopped before every source became ready
      When the operator reruns the weekly NotebookLM sync
      Then the system should poll the existing remote source ids
      And no new source uploads should occur

  Rule: Friday publication requires complete readiness
    Scenario: Block Friday publication while a required source is still processing
      Given today is Friday
      And one required source for the current week is still processing
      When the operator requests publication
      Then publication should be blocked without changing the notebook privacy state
      And the operator should be told which source is still not ready
