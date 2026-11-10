# Claude Capstone Demo

A synthetic VS Code/Python practice project demonstrating: agentic loop control, context compression, Claude Code-style configuration artifacts, and a Layer 3 orchestrator with SQLite state.

> Practice only: outputs are synthetic and must not be presented as evidence from your supplied capstone reference implementations.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest -v
python -m agentic_loop.main
python -m context_strategy.main
python -m orchestrator.main
```
