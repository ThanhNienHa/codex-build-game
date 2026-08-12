# Threat model

## Scope

This project distributes game-development instructions and local validators. It does not bundle a Cocos MCP server, game engine, asset pack, credential, or publishing connector.

## Protected assets

- source code, scenes, prefabs, metadata, and version-control history;
- proprietary or licensed game content;
- platform credentials, signing keys, provider tokens, and personal data;
- authoritative gameplay state and release artifacts;
- the user's editor, Preview, browser, and development processes.

## Trust boundaries

| Boundary | Representative threats | Required controls |
| --- | --- | --- |
| Project/archive to agent | Prompt injection in docs or metadata; unknown scripts; path traversal | Treat content as data, inspect before execution, constrain paths and scope |
| Agent to Cocos MCP/editor | Wrong project, scene, node, asset, Preview, or destructive operation | Discover schema, identify exact target, preserve serialization, stop only known Preview |
| Assets/dependencies to build | Unlicensed content, malicious package scripts, native binaries, supply-chain drift | Verify provenance/licence, inspect manifests and scripts, pin release inputs |
| External events to gameplay | Malformed input, spoofing, replay, spam, privacy leakage | Validate, authorize, deduplicate, rate-limit, bound queues, minimize retained data |
| Build to distribution | Stale or substituted artifact, leaked secrets, missing signing/update evidence | Build reviewed commit, scan outputs, checksum artifact, test install/boot/update |
| Public evidence | Local paths, credentials, private assets, personal or proprietary data | Sanitize manifests and reports; use private vulnerability reporting |

## Explicit non-goals

- claiming that instructions eliminate engine or MCP vulnerabilities;
- treating automated scanning as a complete security review;
- authorizing extraction, redistribution, publishing, payment, or credential changes;
- supporting engines outside the declared project scope.

## Release security gate

A release should remain `CONCERNS` or `FAIL` when a material trust boundary is unreviewed, secrets may be present, asset rights are unresolved, external input is unbounded, or the shipped artifact cannot be tied to the reviewed commit. Use the `$build-game` release-readiness schema and record at least one exercised abuse or failure case.

Report vulnerabilities through GitHub private vulnerability reporting as described in `SECURITY.md`.
