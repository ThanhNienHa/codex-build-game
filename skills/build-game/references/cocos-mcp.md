# Cocos MCP workflow

Use this reference only when the project is Cocos Creator or Cocos Engine, or the user explicitly asks for Cocos work.

1. Confirm the engine and version from project metadata before editing. Distinguish Cocos Creator from Cocos2d-x/native projects; their scene, asset, and build workflows differ.
2. Inspect the available MCP tool catalog for the installed Cocos MCP. Prefer it for opening/inspecting the project, enumerating assets, reading scene/node/component state, editing scenes or properties, and running editor-side checks. Use the tool's current schema rather than guessing tool names or arguments.
3. Before changing a scene, inspect its hierarchy, attached scripts/components, prefab links, asset references, and serialized properties through MCP when supported. Preserve editor-generated IDs and metadata.
4. For asset-related requests, use MCP asset/project inspection first, then follow `references/asset-discovery.md`. Reuse existing Cocos assets, prefabs, atlases, animations, materials, and import settings when suitable.
5. Keep gameplay rules in testable TypeScript/JavaScript or native modules and keep Cocos components thin. Do not hide authoritative state in a node, scene, or editor-only callback.
6. After playable changes, use Cocos Preview to verify the affected flow. Before every new preview run, use Cocos MCP to stop the previous preview and confirm it has shut down. If MCP cannot stop it, identify the exact project-owned preview session, process, or listening port before terminating it. Never use broad process-kill commands or stop the Cocos Editor, unrelated browsers, or other development servers.
7. Start only one fresh preview, check startup errors and the changed gameplay path, then stop it when validation is complete unless the user asks to leave it running.
8. Also run repository tests, type checks, and linting. If MCP is unavailable or fails, report the exact limitation and continue with a reversible file-level fallback only when safe.

Never invent an MCP operation, silently edit a running editor session, commit credentials, or overwrite a scene without first inspecting its current state.
