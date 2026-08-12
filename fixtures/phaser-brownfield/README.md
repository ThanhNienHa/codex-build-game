# Phaser brownfield score fixture

Synthetic maintenance task: the result screen rounds every score component before summing, so fractional rewards can disappear. Preserve the existing module boundary and asset key, make the smallest correction, run the focused contract test, and describe a browser smoke check for the result screen.

Project facts:

- engine metadata: Phaser 3.90.0;
- existing public asset key: `score-coin`;
- starter implementation: `src/scoring.js`;
- contract: `test/scoring.contract.test.js`;
- reference implementation used only by repository conformance: `solution/scoring.js`.

Run the starter reproduction:

```text
node --test test/scoring.contract.test.js
```

It is expected to fail until the starter is corrected. The public SVG was created for this fixture and is licensed under CC0-1.0 as recorded in `public/assets/ASSET-LICENSES.md`.
