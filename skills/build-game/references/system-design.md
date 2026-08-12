# System design and GDD

## Map systems first

For a new game or multi-system feature, list systems with responsibility, inputs, outputs, dependencies, player-facing purpose, MVP priority, and status. Order foundation and core-loop dependencies before presentation and meta progression. Flag circular ownership and duplicate authoritative state.

## Match documentation to scope

For a change under roughly one focused session, use a quick spec:

- outcome and player benefit;
- rules/change;
- non-goals;
- affected systems, data, and assets;
- acceptance criteria and playable check.

For a substantial gameplay system, cover:

1. **Overview**: responsibility and boundaries.
2. **Player fantasy**: intended decisions and feelings.
3. **Detailed rules**: states, transitions, timing, priority, failure, and recovery.
4. **Formulas**: variables, units, ranges, clamping, and examples.
5. **Edge cases**: pause, retry, disconnect, invalid content, and limits.
6. **Dependencies**: bidirectional inputs/outputs and authoritative owner.
7. **Tuning knobs**: data location, defaults, safe ranges, and live-change constraints.
8. **Acceptance criteria**: measurable rule, integration, feedback, and performance evidence.

Also define game-feel targets: response latency, anticipation, active/recovery timing, camera/audio/VFX feedback, and accessibility alternatives.

Before implementation, check for contradictions, dominant strategies, unbounded economies, cognitive overload, and output ranges incompatible with downstream inputs. Keep documents short enough to guide actual work.
