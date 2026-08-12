import assert from "node:assert/strict";

export function scoringContract(displayedScore, assetKey) {
  assert.equal(assetKey, "score-coin", "preserve the existing asset key");
  assert.equal(displayedScore(10.4, 0.4, 0), 11, "round the final score once");
  assert.equal(displayedScore(10.2, -0.4, 0), 10, "support bounded penalties");
  assert.equal(displayedScore(0, 0, 0), 0, "keep the zero boundary stable");
}
