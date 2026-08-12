export const SCORE_COIN_ASSET_KEY = "score-coin";

// Brownfield defect: rounding each component can discard fractional rewards.
export function displayedScore(basePoints, comboBonus, eventBonus) {
  return Math.round(basePoints) + Math.round(comboBonus) + Math.round(eventBonus);
}
