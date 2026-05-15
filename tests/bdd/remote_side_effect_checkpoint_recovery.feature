Feature: Remote side-effect checkpoint recovery
  As the infrastructure recovering from crashes at awkward moments
  I want remote side effects to be reconciled before they are repeated
  So that retries do not create duplicate share links, audio artifacts, or sources

  Background:
    Given remote NotebookLM side effects can succeed before the local manifest is updated

  Rule: Publication side effects are reused when possible
    Scenario: Recover an existing share link after a crash before manifest write
      Given publication created a share target remotely for the current week
      And the process crashed before the share target was recorded locally
      When the operator retries publication
      Then the workflow should discover and reuse the existing share target
      And no second conflicting share link should be created

    Scenario: Recover an audio artifact generated before a local crash
      Given an audio overview was generated for the current source revision
      And the process crashed before the audio artifact id was recorded locally
      When the Friday publication workflow is retried
      Then the existing matching audio artifact should be reused
      And the system should not generate a second audio artifact unnecessarily

  Rule: Uncertain source attachment is reconciled before retry
    Scenario: Reconcile an uncertain source upload after a client timeout
      Given a source attachment request timed out locally after NotebookLM may have accepted it
      When the operator reruns the weekly NotebookLM sync
      Then the system should reconcile remote source state before retrying attachment
      And duplicate source uploads should be avoided
