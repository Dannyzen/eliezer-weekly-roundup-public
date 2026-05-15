Feature: Remote drift and out-of-band reconciliation
  As the operator recovering from manual remote changes
  I want the workflow to detect and reconcile remote drift explicitly
  So that local checkpoints never silently diverge from NotebookLM reality

  Background:
    Given the local manifest records the canonical remote state for the target week

  Rule: Notebook identity drift is fail-closed
    Scenario: Fail closed when the recorded notebook id no longer exists remotely
      Given the manifest records a canonical notebook id for the current week
      And that notebook no longer exists or is no longer accessible remotely
      When the operator reruns the weekly NotebookLM sync
      Then the system should not silently create a replacement notebook
      And the run should require manual notebook drift resolution

  Rule: Source drift is repaired surgically
    Scenario: Reattach only sources that were removed out of band
      Given the manifest records attached remote sources for the current week
      And one recorded remote source was manually removed from the notebook
      When the operator reruns the weekly NotebookLM sync
      Then only the missing source should be reattached
      And unchanged sources should not be duplicated

  Rule: Visibility drift is surfaced before announcements
    Scenario: Detect out-of-band visibility changes before announcing publication
      Given the manifest says the current week's notebook is private
      And the notebook was manually made public outside the workflow
      When the operator runs the next sync or publication check
      Then the visibility drift should be surfaced explicitly
      And the workflow should not assume the earlier privacy state was preserved
