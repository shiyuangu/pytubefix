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

## Repo Insights (2025-01-06)
- `pytubefix/__main__.py`: defines the synchronous `YouTube` interface, orchestrating HTML fetch via `request`, metadata parsing from `extract`, and stream instantiation using the Borg-style `Monostate`. Falls back across clients and manages OAuth/po-token handling before exposing `StreamQuery`.
- `pytubefix/async_youtube.py`: mirrors the sync client but swaps network IO for `AsyncHTTPClient`, reusing the same extraction pipeline and fallback logic while keeping a shared async session singleton.
- `pytubefix/streams.py`: `Stream` objects wrap player manifest entries, parsing mime info, codecs, size, SABR metadata, and exposing download helpers (`download`, `seq_stream`) that rely on `request.stream` and adaptive bitrate utilities in `sabr`.
- `pytubefix/innertube.py`: houses client definitions for Innertube API (headers, tokens, requirements) plus `InnerTube` class with OAuth/po-token caching and request helpers (`player`, `next`, `browse`, etc.).
- `pytubefix/cli.py`: CLI entrypoint wiring argparse commands to common download flows (audio-only, resolution selection, ffmpeg merging) and progress reporting.
- `pytubefix/contrib/playlist.py`: playlist abstraction that paginates via `InnerTube.browse`, reuses `DeferredGeneratorList`, and instantiates `YouTube` objects per video; sibling modules handle channel/search.
- `pytubefix/request.py` & `async_http_client.py`: synchronous and async HTTP helpers adding retrying range requests, sequential segment support, and size discovery used by stream downloads.
- Key support modules: `extract.py` (HTML/player parsing, cipher setup, metadata), `cipher.py`/`jsinterp.py` (signature decipher), `helpers.py` (filename sanitizing, caching, logging), `botGuard/bot_guard.py` (Node-backed poToken generation), `sabr/` (server-assisted adaptive bitrate logic).
