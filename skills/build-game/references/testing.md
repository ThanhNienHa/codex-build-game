# Testing and playable verification

Choose tests from the player risk, not from file type. Keep the suite deterministic and proportional.

## Test in layers

1. **Rule tests:** pure formulas, state transitions, caps, invalid input, seeded randomness, and boundary cases.
2. **Content validation:** schemas, stable IDs, references, assets, legal ranges, and migrations.
3. **Adapter contracts:** engine callbacks, storage, network, platform payloads, and error handling with fixtures.
4. **Replay or integration tests:** ordered commands across multiple systems, reset, reconnect, and snapshot consistency.
5. **Scene/UI smoke:** boot, render, input, resize, scene change, cleanup, and one representative loop.
6. **Playable check:** exercise the affected player path in Preview or the real build and inspect relevant logs.
7. **Performance and soak:** measure a representative busy state, repeated rounds, or long session when the change can affect budgets or lifecycle.

Small fixes rarely need every layer. Release and cross-system work usually do.

## Preserve determinism

Inject time and seeded randomness. Avoid tests that depend on wall-clock sleeps, unordered collections, live services, or arbitrary frame timing. Assert player-relevant state and invariants instead of engine implementation details.

For presentation-only changes, snapshot authoritative state before and after the visual operation. Verify logical position, occupancy, targeting, hit regions, and saved data remain unchanged. Also test offset bounds and reset behavior.

## Verify evidence honestly

Run the repository's documented format, lint, type-check, tests, and build command. Report the exact checks executed and separate:

- `fresh`: run against the current change;
- `historical`: inspected but not rerun;
- `not-run`: required or useful but unavailable;
- `not-applicable`: outside the accepted scope.

Do not call a game playable because it compiles or a process stays alive. Observe the affected flow, real input, visible result, and relevant console state. Use `MANUAL CHECK NEEDED` when interaction cannot be verified.

For claims about fun, clarity, difficulty, or onboarding, record an observed playtest with the task, player context, result, and confusion points. Automated checks do not prove subjective quality.

When configured, use `references/evidence.md` to create a machine-readable evidence manifest and Cocos Preview report.
