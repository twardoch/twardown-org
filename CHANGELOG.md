# Changelog

All notable changes to twardown-org (the Twardown meta-repository) are recorded
here. The format follows [Keep a Changelog](https://keepachangelog.com/), and the
project uses [semantic versioning](https://semver.org/) driven by git tags.

## [Unreleased]

### Added

- Feature conformance matrix in the README, showing which Twardown features each
  implementation (`twardown-py`, `twardown-js`) supports.
- Project icon at `docs/assets/icon.png` — a single-line drawing of one string
  gathering the three components.
- `.gitignore` covering Python build/test artifacts and generated files
  (`update.log`, `tree.txt`).

### Changed

- Bumped the `twardown-docs` submodule pointer to its `v1.0.0` release.

## [1.0.1] — Prior release

Meta-repository coordinating the Twardown family through git submodules:

- `twardown-docs` — the specification, guides, and examples.
- `twardown-js` — the `unified`/`remark` implementation.
- `twardown-py` — the `Python-Markdown` implementation.
- Development scripts (`01-firststeps.sh`, `02-check.sh`, `03-up.sh`) for
  initializing, health-checking, and updating submodules.
- A reference `src/twardown/` package scaffold with `pytest` tests.

Earlier informal history lives in `LOG.md`.
