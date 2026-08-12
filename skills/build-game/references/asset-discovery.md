# Asset discovery and reuse

Use this workflow whenever a request involves or could benefit from sprites, textures, images, animations, tilemaps, levels, models, shaders, fonts, music, sound effects, voice, UI skins, icons, localization, or other game content.

1. Search the project before editing. Inspect likely directories such as `assets/`, `public/`, `static/`, `resources/`, `src/assets/`, scene folders, content manifests, loaders, atlases, and engine import metadata. Use fast filename searches first, then search asset keys and references in code.
2. Inventory relevant candidates by role, format, dimensions or duration, naming, variants, and current usage. For visual assets, inspect the actual files when tools allow; do not infer appearance from filenames alone.
3. Check technical compatibility: license/source metadata, resolution, aspect ratio, transparency, color space, atlas/frame data, compression, loop points, sample rate, target-device budget, and engine loader expectations.
4. Prefer a suitable existing asset and follow the project's established asset keys, loader path, scale, animation timing, audio routing, and attribution conventions.
5. If an asset needs a safe derivative such as cropping, resizing, recoloring, slicing, or format conversion, preserve the source and create a clearly named derived file only when the request authorizes implementation.
6. If no suitable asset exists, continue with an explicit placeholder when that keeps the feature playable. State what is missing and the exact requirements for a final asset. Generate or fetch a new asset only when requested or clearly necessary and authorized.
7. Remove no existing asset merely because it appears unused. Confirm references in code, manifests, scenes, dynamic key construction, and build tooling first.

Keep asset discovery proportional: a small UI change needs a targeted search; a new scene or visual direction needs a broader inventory. Record newly introduced assets and license/source information using the repository's existing convention.
