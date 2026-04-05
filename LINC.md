---
linc-agent-version: 1
type: project
---

# linc-openhands — OpenHands Agentic SDK Testing Ground

Testing integration of [OpenHands SDK](https://github.com/OpenHands/software-agent-sdk) into the LINC ecosystem.

## Build Commands

- `uv sync` — Install dependencies
- `uv run ruff check .` — Lint check
- `uv run ruff format .` — Format check
- `uv run pytest` — Run tests
- `uv run mypy src` — Type check

## Operational Notes

- This project is used to experiment with OpenHands agents, tools, and conversations.
- LLM configuration should be handled via environment variables (e.g., `LLM_API_KEY`).
- Workspace is restricted to the project root unless specified otherwise.

## Architecture

- `src/linc_openhands/` — Core SDK integration logic.
- `test_sdk.py` — Initial verification script.
- `tests/` — standard pytest directory.
