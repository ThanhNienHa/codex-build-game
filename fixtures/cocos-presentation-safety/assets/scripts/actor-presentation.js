export const MAX_VISUAL_OFFSET = 24;

function bounded(value, maximum) {
  return Math.max(-maximum, Math.min(maximum, value));
}

export function createActorView(authoritativeActor) {
  return {
    authoritativeActor,
    visualRoot: { x: 0, y: 0 },
  };
}

export function applyDeterministicCrowdOffset(view, peerIndex, maximum = MAX_VISUAL_OFFSET) {
  const safeMaximum = Math.max(0, maximum);
  const direction = peerIndex % 2 === 0 ? -1 : 1;
  const ring = Math.floor(peerIndex / 2) + 1;
  view.visualRoot.x = bounded(direction * ring * 8, safeMaximum);
  view.visualRoot.y = bounded((ring % 2 === 0 ? -1 : 1) * ring * 4, safeMaximum);
}

export function resetPresentation(view) {
  view.visualRoot.x = 0;
  view.visualRoot.y = 0;
}
