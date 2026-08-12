# Gameplay systems

Use this reference for core loops, combat, progression, economy, AI, or interconnected mechanics. Keep the design proportional to the affected system.

## Start from the player outcome

Define:

- the player goal and the decision they make;
- the input or event that expresses that decision;
- immediate readable feedback;
- the authoritative state change;
- the failure, recovery, and retry path;
- the measurable signal that the loop works.

Describe the shortest complete loop before listing features. If the fun, controls, or feasibility is uncertain, prototype that uncertainty before building supporting progression.

## Specify each rule

For every material rule, record:

1. Preconditions and legal inputs.
2. Authoritative owner of the state.
3. Formula or transition, including units and rounding.
4. Caps, floors, cooldowns, and resource costs.
5. Invalid, simultaneous, and boundary behavior.
6. Player-facing feedback and recovery.
7. Tuning values that belong in validated data.
8. Deterministic tests and playable evidence.

Keep rules independent from scenes, rendering, storage, analytics, and platform SDKs. Pass time and randomness explicitly. Prefer commands that express intent and events that record results.

## Build systems in thin slices

Start with one rule, one content record, one feedback path, and one test. Connect a representative end-to-end slice before expanding breadth.

For combat, establish damage ownership, targeting, range, timing, interruption, death, and respawn before adding many abilities. For board or tactics games, separate logical cells, pathing, occupancy, hit regions, and targeting from visual position, tweening, camera, or crowd offsets.

For progression, define the reason to return, the pacing, unlock conditions, catch-up or recovery, and the maximum useful accumulation. Do not add progression to compensate for an unproven core loop.

For economy, map every source, sink, stock, exchange, and reset. Model affordability and accumulation over time. Protect paid or scarce resources with server authority when applicable. Treat monetization, trading, and durable inventory as `full` scope.

For AI, specify observable goals, legal knowledge, decision cadence, deterministic tie-breaking, and fallback behavior. Test decisions as rules before evaluating feel in play.

## Check system interactions

Map upstream inputs and downstream consumers when three or more systems interact. Identify which system owns truth, which systems derive projections, and which transitions may race or replay. Bound timers, queues, summons, effects, projectiles, and retained history.

Reject a system-level `PASS` unless its rules pass deterministic checks and the representative player loop has been observed. Use playtests for clarity, feel, difficulty, and fun; unit tests cannot prove those qualities.
