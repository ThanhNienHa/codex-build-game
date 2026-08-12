import test from "node:test";
import { displayedScore, SCORE_COIN_ASSET_KEY } from "../solution/scoring.js";
import { scoringContract } from "./scoring.contract.js";

test("reference correction satisfies the unchanged score contract", () => {
  scoringContract(displayedScore, SCORE_COIN_ASSET_KEY);
});
