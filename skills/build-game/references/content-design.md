# Content and data-driven design

Use this reference for characters, abilities, items, levels, waves, dialogue, economy values, localization, or other authored content.

## Define stable schemas

Give records stable IDs independent from filenames and display names. Declare units, legal ranges, defaults, optional fields, references, and schema version. Validate content at startup or build time and report the record and field that failed.

Keep tunable values in data when designers should change them without rewriting behavior. Keep behavior families typed in code when arbitrary data would create an unsafe scripting language. Avoid one-off booleans when a small explicit enum or tagged variant expresses the rule.

## Keep content referentially safe

Validate duplicate IDs, missing references, cycles where forbidden, impossible unlocks, unsupported assets, localization keys, and platform restrictions. Centralize asset and content lookup rather than constructing fragile paths throughout scenes.

Version durable content and save data together when identifiers or meanings change. Provide aliases or migrations for renamed IDs that may exist in saves, replays, or network snapshots.

## Balance with evidence

State the intended role and tradeoff of each content family. Use explicit units and formulas. Test caps and boundaries, then run representative simulations for systems where interactions make manual reasoning unreliable. Simulation can detect dominance or dead content; observed play is still required for feel and clarity.

Keep economic sources, sinks, prices, rewards, and accumulation rates traceable. Never treat client-only tuning as secure for paid or scarce resources.

## Assets, localization, and provenance

Associate content with inspected asset keys and fallback behavior. Record source, licence, attribution, and modification notes using the repository convention. Confirm redistribution rights before placing assets in a public repository or release; private possession or technical extractability is not permission.

Keep player-facing text in localization data when multiple languages or post-release updates are in scope. Test expansion, pluralization, missing keys, and unsupported glyphs at representative viewports.
