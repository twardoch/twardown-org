# Twardown: Consistent Markdown Authoring and Processing

Twardown is a project dedicated to providing a consistent and modern Markdown authoring and processing experience. It defines an opinionated flavor of Markdown, "Twardoch Markdown," which bundles a curated set of extensions and configurations. The goal is to offer a "just works" solution for writers and developers who need reliable and feature-rich Markdown processing across different environments, primarily JavaScript and Python.

This repository, `twardown-org`, serves as the central hub for the Twardown project. It manages the core components as Git submodules:

*   **`twardown-docs`**: Contains the official specification for Twardoch Markdown, along with user guides, examples, and developer documentation. If you want to understand what features Twardown supports and how they behave, this is the place to start.
*   **`twardown-js`**: A JavaScript library, specifically a `unified.js`/`remark` plugin, that implements the Twardown specification. It's designed for easy integration into Node.js projects, static site generators, and other JavaScript-based Markdown workflows.
*   **`twardown-py`**: A Python package that provides an extension for the popular `markdown` library. This allows Python applications to process Twardoch Markdown consistently with its JavaScript counterpart.

## Why Use Twardown?

*   **Consistency:** Get the same Markdown rendering results whether you're working in a Python backend or a JavaScript frontend.
*   **Opinionated but Comprehensive:** Twardown makes choices for you, selecting a suite of modern Markdown features (like GFM tables, task lists, frontmatter) so you don't have to piece them together from numerous plugins.
*   **Modern Features, Pre-configured:** Enjoy an enhanced writing experience with useful extensions enabled out-of-the-box.
*   **Clear Specification:** The `twardown-docs` provide a clear reference for all supported syntax and behavior.

## Installation

The `twardown-org` repository itself is not an installable package. To use Twardown, you'll install the specific library for your environment:

### Python (`twardown-py`)

The Python component of Twardown is available as a package. You can install it using pip:

```bash
pip install twardown-py
```
*(The `pyproject.toml` within the `twardown-py` submodule will define the exact package name on PyPI. The `src/twardown/` directory in *this* `twardown-org` repository seems to be for a separate tool or the core project utility, also named `twardown` as per its own `pyproject.toml`.)*

### JavaScript (`twardown-js`)

The JavaScript component is available as an npm package:

```bash
npm install twardown-js
```
*(The `package.json` within the `twardown-js` submodule will define the exact package name on npm).*

## Basic Usage

Below are conceptual examples. For detailed API and usage, please refer to the documentation within the `twardown-js` and `twardown-py` repositories, and the examples in `twardown-docs`.

### Python (`twardown-py`)

```python
import markdown
# Assuming twardown-py registers itself or provides a direct extension class
# from twardown_py.core import TwardownExtension # Example, actual import may vary

md_text = """
---
title: My Document
---
# Hello Twardown

This is **bold** and *italic*.

- [ ] Task 1
- [x] Task 2
"""

# Option 1: If twardown-py registers its extension name
# html = markdown.markdown(md_text, extensions=['twardown'])

# Option 2: Using the extension class directly
# html = markdown.markdown(md_text, extensions=[TwardownExtension()])

# The exact usage will depend on how twardown-py is packaged and documented.
# For now, let's assume a registered name based on the main project's pyproject.toml for "twardown"
# This might be incorrect for the submodule.
html = markdown.markdown(md_text, extensions=['twardown']) # Placeholder
print(html)
```

### JavaScript (`twardown-js`)

```javascript
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import twardownPlugin from 'twardown-js'; // Example, actual import may vary
import remarkHtml from 'remark-html';

const mdText = `
---
title: My Document
---
# Hello Twardown

This is **bold** and *italic*.

*   [ ] Task 1
*   [x] Task 2
`;

async function processMarkdown(markdownContent) {
  const file = await unified()
    .use(remarkParse)
    .use(twardownPlugin) // Apply Twardown's remark plugin
    .use(remarkHtml)
    .process(markdownContent);
  return String(file);
}

processMarkdown(mdText).then(html => {
  console.log(html);
});
```

---

## Technical Details

This section outlines the architecture of the Twardown project and its components.

### Project Structure (`twardown-org`)

The `twardown-org` repository acts as a meta-repository, orchestrating the development of the different Twardown components. It utilizes **Git submodules** to incorporate:

*   `twardown-docs/`: Contains the Markdown specification, user guides, and examples.
*   `twardown-js/`: The JavaScript implementation (Remark plugin).
*   `twardown-py/`: The Python implementation (Python-Markdown extension).

Key files in this main `twardown-org` repository include:
*   `.gitmodules`: Defines the submodule paths and repository URLs.
*   `pyproject.toml`: Manages the Python environment and dependencies for the Python-based package defined in `src/twardown/` within this repository. This package (named `twardown`) seems to be a CLI tool or core utility for the Twardown ecosystem, with dependencies like `markdown`, `rich`, `pydantic`, `loguru`, and `fire`.
*   Shell scripts (`01-firststeps.sh`, `02-check.sh`, `03-up.sh`): Used for project initialization, health checks, and development workflow automation.

### Python Component (`twardown-py` Submodule)

The `twardown-py` component, developed in its submodule, is a Python package designed as an extension for the `markdown` library.

*   **Core Implementation**:
    *   The main logic typically resides in a `core.py` file within the `twardown_py` package (e.g., `twardown-py/src/twardown_py/core.py`).
    *   It would define an `Extension` class (e.g., `TwardownPyExtension`) that registers various processors (Inline, Block, Tree, Pre/Postprocessors) to implement Twardown-specific Markdown features.
*   **Features (based on analysis of `twardown-org/src/twardown/core.py` which serves as a reference or is the actual core)**:
    *   Standard Markdown: Paragraphs, bold, italic, links, images, inline code.
    *   Extended Syntax: Fenced/indented code blocks, ordered/unordered lists, task lists (`[ ]`, `[x]`), YAML Front Matter, table enhancements, custom `++inserted text++` syntax.
*   **Development Stack**:
    *   Build System: `hatchling` (defined in `twardown-py/pyproject.toml`).
    *   Testing: `pytest`.
    *   Linting & Formatting: `Ruff`.
    *   Type Checking: `Mypy`.

### JavaScript Component (`twardown-js` Submodule)

The `twardown-js` component, developed in its submodule, is a JavaScript library intended to be a `unified.js`/`remark` plugin.

*   **Core Goal**: To bundle curated Remark plugins and configurations to implement the Twardown Markdown specification.
*   **Features (anticipated)**: CommonMark, GFM features, YAML Front Matter, linting, Twardown-specific syntax.
*   **Development Stack**:
    *   Package Management: `npm` (`package.json`).
    *   Build/Transpilation: `Babel`.
    *   Testing: `Jest`.
    *   Linting: `ESLint`.

### Documentation Component (`twardown-docs` Submodule)

The `twardown-docs` submodule houses all documentation for the Twardown project: specification, user guides, examples, and developer documentation.

---

## Coding and Contributing

We welcome contributions to Twardown!

### Getting Started with Development

1.  **Clone with Submodules:**
    ```bash
    git clone --recurse-submodules https://github.com/twardoch/twardown-org.git
    cd twardown-org
    ```

2.  **Initialize/Update Submodules (if cloned non-recursively or to update):**
    ```bash
    git submodule update --init --recursive
    ```
    To pull the latest changes from the `main` branch of each submodule (recommended after fetching updates for `twardown-org`):
    ```bash
    git submodule foreach git checkout main
    git submodule foreach git pull origin main
    ```

### Development Workflow & Scripts

This project includes shell scripts in the `twardown-org` root to streamline development:

*   **`02-check.sh`**:
    *   **Purpose**: Comprehensive health-check script (tests, linters, type checkers) for sub-projects.
    *   **Usage**: `./02-check.sh` (all) or `./02-check.sh --repo=twardown-py` (specific).
    *   **Requires**: `tree`, `python`, `node`, `npm`, `gh` (GitHub CLI).
*   **`03-up.sh`**:
    *   **Purpose**: Automates committing/pushing changes (especially `LOG.md`/`README.md` updates) in submodules and updating submodule references in `twardown-org`.
    *   **Usage**: `./03-up.sh` (all), `./03-up.sh --repo=twardown-py` (specific), with `--dry-run`, `--skip-ci` options.
    *   Logs to `update.log`.

### Key Files for Tracking

*   **`LOG.md`**: Present in each repository/submodule. Document your changes here.
*   **`TODO.md`**: In `twardown-org` root for high-level project tasks.

### Coding Conventions

*   **Python (`twardown-py`)**: PEP 8, `Ruff` (lint/format), `Mypy` (types). Configured in its `pyproject.toml`.
*   **JavaScript (`twardown-js`)**: Common JS best practices, `ESLint`, `Prettier`. Configured in its `package.json` or ESLint config.
*   **Magic Records**: Maintain `this_file: path/to/file.ext` comments.
*   **Commit Messages**: Clear, descriptive, reference issues if applicable.

### Submitting Changes (General Flow)

1.  **Navigate & Branch**: `cd` into the relevant submodule (e.g., `twardown-py`) and create a feature branch.
2.  **Develop**: Implement your changes.
3.  **Local Checks**: Run tests and linters within the submodule.
4.  **Project-Level Check**: From `twardown-org` root, run `./02-check.sh --repo=<submodule-name>`.
5.  **Update `LOG.md`**: In the submodule, document your changes in `LOG.md`.
6.  **Commit & Push Submodule**: Commit changes in the submodule and push the branch to its remote repository (e.g., `github.com/twardoch/twardown-py`).
7.  **Pull Request (Submodule)**: Open a PR for your branch in the submodule's repository.
8.  **Update `twardown-org` (Post-Submodule PR Merge)**:
    *   Once the submodule PR is merged, ensure your local `twardown-org` is up-to-date (`git checkout main; git pull`).
    *   Update the submodule pointer:
        ```bash
        cd twardown-org # Ensure you are in the root
        # Ensure the submodule itself is on its main branch and updated
        (cd twardown-py && git checkout main && git pull) # Example for twardown-py
        # Then, back in twardown-org root
        git add twardown-py # Stage the new commit hash for the submodule
        git commit -m "Update twardown-py to latest by merging PR #XYZ"
        git push origin main
        ```
    *   The `./03-up.sh` script can also assist in parts of this process, particularly if run *before* pushing the submodule changes (it can commit and push submodule changes, then you'd make a PR, then update `twardown-org`).

## License

All components of the Twardown project (`twardown-org` itself, `twardown-docs`, `twardown-js`, `twardown-py`) are licensed under the **MIT License**. See the `LICENSE` file in each respective repository for full details.
