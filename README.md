# grip-pyrolyze-examples

Example scripts, notebooks, and small apps demonstrating `grip-pyrolyze` and PyRolyze.

- **PyPI project name:** `grip-pyrolyze-examples`
- **Import path:** `grip_pyrolyze.examples.demo` (extends the `grip_pyrolyze` namespace alongside the `grip-pyrolyze` package)
- **Build backend:** hatchling
- **License:** LGPL-2.1-or-later (see `LICENSE`)

The PySide6 GRIP demo from `grip-py-demo` lives at import path `grip_pyrolyze.examples.demo`. Run it after install:

```bash
grip-pyrolyze-demo
```

or `python -m grip_pyrolyze.examples.demo.main` with `PYTHONPATH=src`.

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
