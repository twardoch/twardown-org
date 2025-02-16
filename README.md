---
this_file: README.md
---

# twardown-org

A collection of repositories related to twardown, an opinionated "Twardoch Markdown" flavor, plus associated tools. The project aims to provide a consistent, modern Markdown experience across different ecosystems.

## Overview

Twardown is a carefully curated set of Markdown extensions and configurations that work together to provide an enhanced writing experience. Instead of requiring users to manually configure multiple plugins and options, Twardown provides a single, opinionated configuration that "just works."

## Components

- **twardown-docs**: Documentation and specification for the Twardown flavor, explaining the rationale behind choices and providing comprehensive examples
- **twardown-js**: A unified.js-compatible plugin that bundles carefully selected Remark plugins into a single, cohesive package
- **twardown-py**: A Python Markdown extension that provides equivalent functionality in the Python ecosystem

## Project Status

The project is in active development. Current focus:

- Defining the core Markdown extensions and features
- Implementing basic plugin infrastructure
- Setting up development environments and testing

## Development

Each component has its own repository with specific development instructions:

- See `twardown-docs/` for the specification and documentation
- See `twardown-js/` for the JavaScript implementation
- See `twardown-py/` for the Python implementation

!!! important
Run `sh ./02-check.sh` then implement the TODO and then run `sh ./03-up.sh`. Fix whatever fails (making it more robust), retry. 

## License

All components are licensed under the MIT License.
