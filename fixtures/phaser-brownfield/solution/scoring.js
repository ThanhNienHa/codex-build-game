export const SCORE_COIN_ASSET_KEY = "score-coin";

export function displayedScore(basePoints, comboBonus, eventBonus) {
  return Math.round(basePoints + comboBonus + eventBonus);
}
