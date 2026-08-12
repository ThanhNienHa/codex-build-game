import assert from "node:assert/strict";
import test from "node:test";
import { createActor, snapshotActor } from "../assets/scripts/authoritative-state.js";
import {
  applyDeterministicCrowdOffset,
  createActorView,
  MAX_VISUAL_OFFSET,
  resetPresentation,
} from "../assets/scripts/actor-presentation.js";

test("crowd offsets remain presentation-only, deterministic, bounded, and resettable", () => {
  const actor = createActor("secondary-1", { column: 4, row: 7 }, "target-1");
  const before = snapshotActor(actor);
  const view = createActorView(actor);

  applyDeterministicCrowdOffset(view, 9);
  const first = { ...view.visualRoot };
  applyDeterministicCrowdOffset(view, 9);

  assert.deepEqual(view.visualRoot, first);
  assert.ok(Math.abs(view.visualRoot.x) <= MAX_VISUAL_OFFSET);
  assert.ok(Math.abs(view.visualRoot.y) <= MAX_VISUAL_OFFSET);
  assert.notDeepEqual(view.visualRoot, { x: 0, y: 0 });
  assert.deepEqual(snapshotActor(actor), before);

  resetPresentation(view);
  assert.deepEqual(view.visualRoot, { x: 0, y: 0 });
  assert.deepEqual(snapshotActor(actor), before);
});
