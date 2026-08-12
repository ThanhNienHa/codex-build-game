# Case study: Cocos strategy game from recovered assets

## Context

- **Date:** 2026-08-12
- **Engine:** Cocos Creator 3.8.8
- **Stage:** Production, with polish and release gates still open
- **Process mode:** Lean feature delivery inside an existing production-stage project
- **Task:** Improve the readability of a dense 100-cell, two-team strategy battle built from a large private set of recovered character assets.

The game, source archive, and character assets are private. This report includes only anonymized workflow behavior and aggregate verification results.

## Why `$build-game` was used

The project combined deterministic board and combat rules, a large recovered Spine catalog, on-demand content loading, mobile portrait UI, Cocos scene integration, and live battle effects. A readability change had to separate overlapping characters without moving authoritative cells, occupancy, hit regions, or targeting.

The material risks were changing gameplay while fixing presentation, loading too much recovered content at once, and claiming release readiness from automated tests without observing a real battle.

## Skill behavior observed

`$build-game` guided the task to:

1. Confirm Cocos Creator 3.8.8 from project metadata before engine-specific work.
2. Inspect the existing asset catalog, Spine packages, loaders, scene hierarchy, and runtime references instead of creating replacement characters.
3. Keep the improvement presentation-only: the authoritative unit node and board state stayed fixed while secondary silhouettes received small deterministic visual offsets.
4. Preserve the local player and locked target as stable anchors, cap crowd offsets at 24 pixels, and keep distant actors unchanged.
5. Add a deterministic test covering anchor stability, offset diversity, and the maximum displacement. The test exposed a rounding edge case before the bound was corrected.
6. Use the installed Cocos MCP schema for editor and hierarchy inspection, asset refresh, Preview launch, screenshots, input simulation, and log checks.
7. Reject an editor-side cold Game View instance as battle evidence and target the project-owned Browser Preview window for the real combat smoke test.
8. Keep performance, complete visual polish, and Windows packaging as explicit follow-up gates instead of calling the game finished.

## Fresh verification evidence

The project's documented `npm run check` command was rerun on 2026-08-12 and completed successfully in approximately 47 seconds.

| Check | Fresh result |
| --- | --- |
| Cocos TypeScript diagnostics | PASS |
| Deterministic simulation suite | PASS: 119 named tests |
| Dense actor separation test | PASS: stable player and target anchors, moved secondary actors, bounded offsets |
| Balance suite | PASS: 864 mirrored matches |
| Balance runner verdict | PASS |

The task-recorded playable evidence, not rerun for this documentation update, showed:

- a Browser Preview with 100 cells and 12 recovered heroes;
- a real battle entered through Preview input;
- the skill row, projectiles and combat effects, and a respawn notice visible during play;
- mock gift controls disabled in the current lobby flow;
- content loaded on demand from a catalog of 118 actor families rather than loading the approximately 688 MiB recovered source set into memory at once.

A new Preview was not started solely for this case study. The playable evidence above is deliberately labeled historical, while the automated results are fresh.

## Verdict

**CONCERNS** for the current production milestone.

The bounded presentation change and deterministic gameplay checks pass, and a real Browser Preview battle was previously observed. A fresh Preview capture of the final dense-combat behavior, performance measurements under sustained effects, complete UI/VFX polish, and Windows packaging evidence are still required for a release-ready `PASS`.

## Demonstrated value

The skill produced a player-visible readability improvement without contaminating authoritative board state. It also caught a real rounding defect in the visual-offset bound and prevented editor-only state from being presented as playable proof.

This case suggests two reusable improvements:

- add a standard fixture for verifying that presentation offsets never mutate authoritative positions, occupancy, or hit regions;
- add a compact Cocos Preview evidence record containing preview identity, input path, observed state, console result, and whether the evidence is fresh or historical.

## Privacy

No proprietary code, assets, credentials, personal data, local machine paths, source archives, or distributable binaries are included in this report.
