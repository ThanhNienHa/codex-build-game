import test from "node:test";
import { displayedScore, SCORE_COIN_ASSET_KEY } from "../src/scoring.js";
import { scoringContract } from "./scoring.contract.js";

test("displayed score preserves fractional rewards until the final rounding boundary", () => {
  scoringContract(displayedScore, SCORE_COIN_ASSET_KEY);
});
