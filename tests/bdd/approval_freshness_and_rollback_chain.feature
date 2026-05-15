Feature: Approval freshness, publication intent, and rollback chain safety
  As the operator approving weekly publication
  I want approvals to stay tied to the current weekly state and reset after rollback
  So that stale human intent never authorizes the wrong payload or a reannouncement after revocation

  Background:
    Given publication requires explicit operator approval tied to the weekly state

  Rule: Approval expires when the weekly state changes
    Scenario: Expire publication approval when the source fingerprint changes after approval
      Given the operator approved publication for the current week's source fingerprint
      And the source fingerprint changes before publication occurs
      When the operator requests publication
      Then the old approval should be treated as expired
      And the operator should be asked for a fresh approval

  Rule: Rollback resets downstream trust
    Scenario: Block reannouncement after rollback until a fresh publication succeeds
      Given the current week was published and announced once
      And that publication was rolled back later
      When downstream distribution is evaluated again
      Then no further announcement should be prepared for that week
      And the system should wait for a fresh successful publication

  Rule: Drift invalidates earlier intent
    Scenario: Require fresh approval when visibility drift is detected before publication
      Given the operator already approved publication for the current week
      And the notebook visibility state drifted outside the workflow before publish completed
      When the operator requests publication again
      Then the previous approval should no longer be sufficient
      And the operator should be shown the detected visibility drift before reapproving
