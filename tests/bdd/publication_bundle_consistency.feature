Feature: Publication bundle consistency and downstream package safety
  As the infrastructure preparing the weekly output package
  I want share targets, audio artifacts, and week identity to stay aligned
  So that downstream readers always receive one coherent weekly package

  Background:
    Given downstream readers receive a weekly package built from the canonical notebook state

  Rule: Bundle components must agree on one weekly revision
    Scenario: Build a publication bundle from one canonical week, share target, and audio artifact
      Given the current week has one canonical notebook id
      And the manifest records one canonical share target and one current audio artifact
      When the system prepares the weekly publication bundle
      Then the bundle should reference only that week's canonical share target
      And the bundle should reference the matching current audio artifact

  Rule: Missing bundle components block downstream packaging
    Scenario: Block bundle generation when the share target or local audio path is missing
      Given the current week is otherwise ready for distribution
      And either the share target or the local audio path is missing from durable state
      When the system prepares the weekly publication bundle
      Then bundle generation should be blocked
      And the operator should be told which bundle component is missing

  Rule: Corrections invalidate stale bundles
    Scenario: Invalidate a saved bundle when a correction changes the audio source revision
      Given a weekly publication bundle was already prepared
      And a correction changes the source revision that the audio should represent
      When the operator prepares the bundle again
      Then the older bundle should be treated as stale
      And a replacement bundle should be prepared from the corrected weekly state
