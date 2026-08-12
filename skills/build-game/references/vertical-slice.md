# Prototype, vertical slice, and playtesting

## Prototype

Use a disposable prototype to answer one risky question: Is the core verb fun? Does the control scheme work? Can the target device support the effect? Define the hypothesis and decision threshold first. Use placeholders and avoid production architecture unless required. End with `proceed`, `revise`, or `discard` and record why.

## Vertical slice

A vertical slice proves one representative loop end to end:

- understandable goal and input;
- authoritative rules and failure/recovery;
- representative art, UI, animation, audio, and game feel;
- real content/data loading and relevant save/network/platform boundary;
- deterministic rule tests and critical integration checks;
- target-device performance and lifecycle behavior;
- a clean boot-to-loop playable path.

Build the slice before committing a large backlog. If it changes the core loop, update design and architecture before creating more stories.

## Playtest evidence

Observe rather than coach. Record build/version, device, participant context, task, behavior, confusion, failure point, performance defects, and severity. Separate observation from interpretation and proposed fix.

For a meaningful slice, involve at least one person other than the implementer when available. The slice fails if the core loop cannot be completed, the goal is unclear without explanation, a critical fun blocker exists, or performance misses target. Missing external playtesting is `CONCERNS`, not fabricated `PASS`.
