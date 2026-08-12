export function createActor(id, cell, targetId = null) {
  return Object.freeze({
    id,
    cell: Object.freeze({ column: cell.column, row: cell.row }),
    occupancyKey: `${cell.column}:${cell.row}`,
    hitRegion: Object.freeze({ radius: 18 }),
    targetId,
  });
}

export function snapshotActor(actor) {
  return JSON.parse(JSON.stringify(actor));
}
