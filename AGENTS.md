# Repository Guidelines

## Project Structure & Module Organization
The `pytubefix/` package holds the downloader core, async clients, cipher helpers, and CLI entry point (`cli.py`). Subdirectories like `botGuard/` and `sig_nsig/` bundle JavaScript VM assets; `contrib/` contains provider-specific integrations, and `sabr/` keeps adaptive rate logic. Tests mirror the package in `tests/`, with `tests/mocks/` offering canned API replies. Publication assets live under `docs/`, while top-level scripts such as `build.sh` automate releases.

## Build, Test, and Development Commands
Use Poetry for environment management.
- `poetry install` — resolve dependencies and create the virtualenv.
- `poetry run pytest` — execute the full test suite.
- `poetry run pytest --cov=pytubefix` — measure coverage when preparing releases.
- `poetry run python -m pytubefix.cli --help` — sanity-check CLI entry points.
- `poetry build` — produce source and wheel artifacts before uploading.

## Coding Style & Naming Conventions
Follow standard PEP 8 conventions with 4-space indentation and descriptive snake_case names for modules, functions, and variables. Keep classes in CapWords form and resist abbreviations unless YouTube terminology demands it. The repo pins `black==19.10b0`; format with `poetry run black .` and confirm linting via `poetry run flake8`. Enable type hints where practical and align docstrings with the public API surface exposed under `pytubefix`.

## Testing Guidelines
Pytest drives the suite; place new cases alongside the module they cover using the `test_<module>.py` pattern. Prefer fixtures in `tests/conftest.py` and reuse mocks from `tests/mocks/` to avoid live network calls. Ensure new stream or cipher logic ships with regression tests, and target coverage parity by checking `poetry run pytest --cov=pytubefix --cov-report=term-missing` before submitting.

## Commit & Pull Request Guidelines
Keep commits focused and phrased in the imperative mood (`add fallback client retry`). Reference issues inline when available and group versioned release work via `build.sh`. Pull requests should summarize behavioral changes, list verification steps (`poetry run pytest`), call out API or CLI impacts, and attach screenshots for CLI UX adjustments when helpful. Link to relevant documentation updates under `docs/` and request review from maintainers owning the touched modules.
