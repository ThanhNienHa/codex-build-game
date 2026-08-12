# Cocos presentation-safety fixture

Synthetic Cocos Creator 3.8.8-shaped task: fan overlapping actor silhouettes for readability without changing authoritative board state.

The pure rule fixture represents the intended engine boundary:

- `authoritative-state.js` owns cells, occupancy, hit regions, and targeting;
- `actor-presentation.js` owns bounded visual offsets and reset behavior;
- tests prove the authoritative snapshot is unchanged.

Run:

```text
node --test test/presentation.test.js
```

No Cocos Editor installation is required for the deterministic rule test. A real Cocos implementation must still use MCP and a clean Preview for playable evidence.
