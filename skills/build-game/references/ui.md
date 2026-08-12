# UI and feedback

Use this reference for HUDs, menus, onboarding, controls, combat readability, feedback, or accessibility.

## Render a projection of state

Build a small view model from authoritative state. UI may request actions and display outcomes, but it must not own health, currency, cooldown completion, inventory, match phase, or win conditions.

For every important action or event, make three things clear:

1. **Attribution:** who or what caused it.
2. **Reaction:** what changed visually or audibly now.
3. **Consequence:** what state, opportunity, or risk changed.

Prioritize primary feedback over decoration. Bound toasts, damage numbers, overlays, animations, sounds, and queued transitions so bursts cannot hide controls or exhaust memory.

## Design hierarchy and states

Keep the current goal, critical resources, actionable controls, threats, and results readable at the target viewport. Define idle, hover/focus, pressed, selected, disabled, loading, empty, error, and success states where applicable.

Use layout rules that tolerate localization, safe areas, aspect ratios, text scaling, and dynamic content. In dense combat, preserve the local actor and selected target as stable visual anchors; fan or reduce secondary chrome without moving logical actors.

## Input and accessibility

Support the project's required keyboard, pointer, touch, or controller path. Keep hit targets large enough for the target device, maintain focus order, avoid color-only meaning, provide readable contrast, and expose reduced-motion or volume controls when scope requires them.

Do not trap gameplay behind hover-only information. Debounce accidental repeat input without making controls feel unresponsive. Explain unavailable actions at the point of use when useful.

## Verify the UI

Test view-model derivation independently. Smoke-test boot, resize, scene re-entry, and one complete interaction path. Inspect actual screenshots or Preview at target aspect ratios. Use a short observed playtest to support claims about clarity or discoverability; a snapshot alone cannot prove that a player understands the UI.
