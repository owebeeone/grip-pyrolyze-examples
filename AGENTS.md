# AGENTS

## Scope
This file defines repository-specific coding instructions for `grip-pyrolyze-examples`.

## Design Rules
- Prefer `@dataclass` for classes that primarily hold state.
- Keep example entrypoints small and readable; factor shared helpers into submodules when duplication grows.
- Keep type annotations complete and precise so IDE inference remains strong.

## Paths in version control
- Do not store absolute filesystem paths in any committed file; use paths relative to this repository (the `grip-pyrolyze-examples` submodule root). If a path would cross into a parent monorepo checkout, truncate to the closest submodule root instead of embedding machine-specific prefixes.

## Development Process (TDD)
Use a strict red/green/refactor workflow for behavior that is tested (non-trivial example logic, helpers, or packaged utilities).

1. Red: Add or update tests first, run the smallest relevant target, confirm failure.
2. Green: Minimal change to pass.
3. Refactor: Preserve behavior.
4. Re-run focused tests, then the full suite when touching shared code.

## Test Commands
- Focused tests: `uv run --with pytest --with pytest-cov pytest <test-path> -q`
- Full suite: `uv run --with pytest --with pytest-cov pytest -q`
