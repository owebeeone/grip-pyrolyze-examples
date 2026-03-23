# grip-pyrolyze-examples

Example scripts, notebooks, and small apps demonstrating `grip-pyrolyze` and PyRolyze.

- **PyPI project name:** `grip-pyrolyze-examples`
- **Import package:** `grip_pyrolyze_examples`
- **Build backend:** hatchling
- **License:** LGPL-2.1-or-later (see `LICENSE`)

Add runtime dependencies in `pyproject.toml` (`dependencies`) as you publish real examples (for example `grip-pyrolyze`, `pyrolyze`, `PySide6`).

## Local development

```bash
git clone git@github.com:owebeeone/grip-pyrolyze-examples.git
cd grip-pyrolyze-examples
pip install -e .
```

## Tests

```bash
uv run --with pytest --with pytest-cov pytest -q
```

## Build distributions

```bash
python -m pip install build
python -m build
```
