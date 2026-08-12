# Case study: Cocos parity rebuild

## Context

- **Date:** 2026-08-12
- **Engine:** Cocos Creator 3.8.8
- **Stage:** Production, with unresolved vertical-slice and release gates
- **Process mode:** Full planning and evidence review; no `studio-full` implementation round
- **Task:** Analyze an existing packaged two-team battle game and rebuild its behavior in a new Cocos project while replacing the character roster.

The source game and replacement assets are private. This report includes only workflow behavior and aggregated technical evidence.

## Why `$build-game` was used

The project mixed reverse engineering, deterministic combat simulation, scene/UI reconstruction, animation and audio mapping, Cocos integration, Preview checks, performance work, and Windows packaging. Historical reports and an older executable existed, but they did not prove that the current source was playable or behaviorally equivalent.

The main risk was false completion: treating passing fixtures, imported assets, a running process, or a smoke-test flag as proof of full parity.

## Skill behavior observed

`$build-game` guided the task to:

1. Detect a Cocos production-stage project with high-risk cross-system scope.
2. Inspect source evidence, rule ledgers, tests, assets, scene flow, Preview captures, and build provenance before accepting claims.
3. Preserve proprietary assets and existing serialized Cocos relationships instead of restructuring the project.
4. Separate deterministic domain parity from visible combat feel, UI, Preview, performance, and native release evidence.
5. Reject stale builds and reports as current evidence.
6. Keep the verdict at `FAIL` for release parity and `CONCERNS` for partial gameplay despite green automated checks.
7. Produce a dependency-ordered completion plan with explicit test and Fresh Preview gates before allowing a new PC build.

The completion path prioritized lifecycle clock behavior, player identity, result/continue flow, full UI interaction, deterministic traces, combat cadence, animation contracts, effects/audio, reliability, performance, and only then Windows packaging.

## Fresh verification evidence

The project's full automated check was rerun on 2026-08-12 and completed successfully in approximately 36 seconds.

| Check | Fresh result |
| --- | --- |
| Original data validation | PASS: 8 unit definitions, 16 heroes, 15 skills, 3 modes |
| Domain parity suite | PASS: 14 named suites, including simulation, replay, lifecycle, targeting, gifts, results, projectiles, and clock |
| Type check | PASS |
| Effect audit | PASS: 6 required Spine effects verified by hash |
| Audio audit | PASS: 30 source and packaged clips |
| Replacement roster audit | PASS: 24 animation records, comprising 8 units and 16 heroes |
| Package audit | PASS: zero localhost references in scanned source/scene roots |

Historical source-vs-rebuild evidence also recorded a 1001-checkpoint long combat trace match and focused unit, hero, skill, social, and result comparisons. Those historical artifacts were inspected but were not regenerated for this case-study update, so they are not presented as fresh verification.

## Playable evidence and limitation

Earlier Cocos Preview work exercised the flow from tutorial through battle, settings, ranking, result, and continue. Review of captures showed that a green input/state smoke result did not prove correct UI rendering or natural combat completion. Some states were reached through debug control rather than an unassisted player-visible loop.

A new Cocos Preview was not started solely to publish this case study because the active task was not currently executing and the case study must not imply a fresh playable pass. Therefore the current release-quality verdict remains unresolved.

## Verdict

**CONCERNS** for the rebuild as an active production project. **FAIL** for a release-ready 1:1 parity claim.

Automated rule, content, asset, and packaging checks are strong, but current Fresh Preview evidence, natural combat feel, complete UI rendering, performance/soak results, and a newly produced Windows build are still required.

## Demonstrated value

The skill's useful outcome was not a claim that the game was finished. It prevented a premature release verdict and converted mixed historical evidence into a bounded completion path with explicit gates.

This use exposed two improvements for future versions:

- capture a machine-readable evidence manifest that labels each artifact `fresh`, `historical`, or `not-rerun`;
- provide a standard Cocos Preview evidence template covering clean shutdown, new preview identity, real input, console errors, screenshots, and stop confirmation.

## Privacy

No proprietary code, assets, game name, source archive, credentials, personal data, local paths, or distributable binaries are included in this report.
