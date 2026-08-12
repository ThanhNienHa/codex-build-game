# Production and runtime integration

Use this reference for scenes, engine integration, assets, audio, performance, builds, or release-facing runtime work.

## Keep engine code thin

Treat scenes and engine components as adapters: translate lifecycle and input into application commands, then render derived state. Keep authoritative rules testable without booting the engine.

Inspect the established scene, prefab, loader, and dependency structure before editing. Preserve serialized IDs and links. Centralize asset keys and follow the project's ownership conventions rather than introducing a parallel architecture.

## Make lifecycle explicit

For every scene or runtime service, define creation, activation, pause, resume, reset, exit, and disposal. Remove listeners and timers, release retained references, cancel stale async work, and return pooled objects. Verify repeated scene entry and match restart, not only first boot.

## Manage assets deliberately

Follow `references/asset-discovery.md`. Validate asset existence, compatibility, source or licence, importer settings, and current references. Load representative content for the vertical slice, then choose preload, demand-load, streaming, atlasing, or pooling from measured needs.

Do not load a complete asset catalog merely because it exists. Establish memory and load-time budgets. Give missing or failed assets an explicit fallback that keeps diagnostics visible.

## Protect gameplay from presentation

Apply animation, tween, camera, crowd separation, and hit effects below an actor visual root or equivalent presentation boundary. Do not move the authoritative node or logical transform to solve readability. Reset presentation offsets on reuse, death, scene exit, and respawn.

## Set measurable budgets

Choose budgets from the target device and game needs:

- frame time and sustained FPS;
- memory and peak allocation;
- initial and transition load time;
- draw calls, texture switches, particles, lights, and expensive effects;
- concurrent voices and audio latency;
- queue lengths, retained callbacks, and pool capacity;
- package size and downloaded content.

Profile a representative busy state on the slowest supported target. A development machine idle scene is not performance evidence.

## Verify builds

Run the project's documented type-check, lint, tests, and build. Then boot the produced artifact when release or packaging is in scope. Distinguish editor Preview, development build, and release artifact evidence. Record platform, engine version, commit, command, result, and known limitations.
