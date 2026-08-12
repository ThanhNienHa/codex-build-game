# State management

Use this reference for gameplay state, reducers, scene transitions, save data, replay, rollback, or multiplayer authority.

## Establish ownership

Classify state before changing it:

- **Authoritative:** rules, positions, occupancy, health, inventory, timers, progression, and results.
- **Derived:** HUD models, availability, labels, previews, and cached queries reproducible from authoritative state.
- **Presentation-only:** animation phase, particles, camera shake, tween offsets, and temporary visual layout.
- **External:** persistence, network, analytics, platform identity, and provider payloads.

Give each authoritative value one owner. Scenes and UI may project state but must not independently decide gameplay outcomes. Presentation changes must not mutate logical positions, occupancy, targeting, hit regions, or saved snapshots.

## Model transitions explicitly

Represent lifecycle as explicit states and legal transitions. Reject or safely ignore commands that are invalid for the current phase. Centralize reset behavior so restart, death, reconnect, scene exit, and test teardown do not leave timers, listeners, or visual offsets behind.

Use pure functions or an established equivalent for rules. Return new snapshots or deliberate mutations owned by one system; do not allow hidden cross-scene mutation.

Model:

- time as an injected clock or explicit delta;
- randomness through a seedable source;
- input as validated commands;
- results as domain events or updated snapshots;
- identifiers as stable values independent from node instances.

## Persistence and compatibility

Define a versioned, minimal save schema. Validate on read, provide safe defaults for optional fields, and migrate known older versions deliberately. Never serialize engine nodes, callbacks, transient caches, or credentials.

Write saves atomically where possible. Treat corrupt, partial, future-version, and duplicate data as explicit cases. Keep persistence behind an adapter so rules can run in memory.

For multiplayer, state which process is authoritative, what clients predict, how commands are ordered, and how snapshots reconcile. Never let a visual client become authoritative accidentally.

## Replay and verification

Record the initial snapshot, deterministic seed, ordered commands, and relevant version when replay is valuable. A replay test should reproduce the same authoritative result without rendering.

Test:

- normal, minimum, maximum, and invalid transitions;
- repeated and duplicate commands;
- reset and re-entry;
- save round-trip and migration;
- seeded replay consistency;
- presentation updates leaving authoritative snapshots byte-for-byte or structurally unchanged.
