# Public fixtures

These small synthetic projects let maintainers evaluate `$build-game` without publishing private games or engine caches.

- `phaser-brownfield`: an existing Phaser-shaped score module with a rounding defect, a public SVG asset, a contract test, and a corrected reference implementation.
- `cocos-presentation-safety`: a Cocos Creator 3.8.8-shaped project that verifies visual crowd offsets cannot mutate authoritative cells, occupancy, hit regions, or targeting.

Run all deterministic fixture checks:

```text
python scripts/run_fixture_checks.py
```

The Phaser starter is intentionally expected to fail its focused contract test. The fixture runner treats that failure as proof the task is reproducible, then verifies the reference implementation passes. Fixtures are evaluation material, not production templates.
