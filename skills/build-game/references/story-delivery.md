# Story delivery and traceability

Use a thin story for production work. It must create a testable player-visible increment, not merely a technical layer.

## Story contract

- **Outcome**: what changes for the player or creator.
- **Source requirement**: system/spec section or issue being satisfied.
- **Decision constraints**: relevant architecture rule and prohibited shortcuts.
- **Acceptance criteria**: observable and measurable.
- **Non-goals**: explicit exclusions.
- **Dependencies**: real prerequisites only.
- **Evidence**: unit/integration test, screenshot/preview, playtest, profile, or build result as appropriate.

Before implementation, verify the referenced requirement and decision still agree. If missing, create only the smallest necessary quick spec or decision note; do not manufacture a document chain for a trivial fix.

Implement in this order when applicable:

1. Domain types, rules, and content schema.
2. Deterministic rule tests and boundary cases.
3. Application orchestration and external adapters.
4. Scene/UI/audio feedback and accessibility.
5. Integration, playable smoke check, and performance evidence.

Finish only when every acceptance criterion maps to evidence. Report unmet criteria as remaining work; do not quietly narrow the story after implementation.
