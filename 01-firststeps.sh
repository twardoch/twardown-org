#!/usr/bin/env bash
# this_file: 01-firststeps.sh

set -e  # Exit on error

# Create LOG.md
cat > LOG.md << 'EOL'
---
this_file: LOG.md
---

# Development Log

## Initial Setup - $(date '+%Y-%m-%d')

- Created initial repository structure
- Set up basic configuration files
- Initialized Git repositories
EOL

# Create main README.md
cat > README.md << 'EOL'
---
this_file: README.md
---

# twardown-org

A collection of repositories related to twardown, an opinionated "Twardoch Markdown" flavor, plus associated tools.

## Components

- **twardown-docs**: Documentation for the twardown flavor and tooling
- **twardown-js**: unified.js-compatible plugin wrapper for various Unified/Remark plugins
- **twardown-py**: Python plugin for the Python Markdown ecosystem

## License

All components are licensed under the MIT License.

## Development

See individual repositories for development instructions.
EOL

# Function to initialize a Python repository
init_python_repo() {
    local repo_name=$1
    local repo_description=$2
    
    echo "Initializing $repo_name..."
    
    # Create directory if it doesn't exist
    mkdir -p "$repo_name"
    cd "$repo_name"
    
    # Initialize git if not already initialized
    if [ ! -d .git ]; then
        git init
    fi
    
    # Create pyproject.toml
    cat > pyproject.toml << EOL
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "$repo_name"
version = "0.1.0"
description = "$repo_description"
readme = "README.md"
requires-python = ">=3.8"
license = "MIT"
authors = [
    { name = "Adam Twardoch", email = "adam@twardoch.com" },
]

[project.urls]
Homepage = "https://github.com/twardoch/$repo_name"
Repository = "https://github.com/twardoch/$repo_name.git"

[tool.hatch.build.targets.wheel]
packages = ["src/$repo_name"]

[tool.pytest.ini_options]
addopts = "-ra -q"
testpaths = ["tests"]
EOL
    
    # Create src directory and package
    mkdir -p "src/$repo_name"
    touch "src/$repo_name/__init__.py"
    
    # Create tests directory
    mkdir -p "tests"
    touch "tests/__init__.py"
    
    # Create README.md
    cat > README.md << EOL
---
this_file: $repo_name/README.md
---

# $repo_name

$repo_description

## Installation

\`\`\`bash
pip install $repo_name
\`\`\`

## Usage

Documentation coming soon.

## License

MIT License
EOL
    
    # Create LICENSE
    cat > LICENSE << 'EOL'
MIT License

Copyright (c) 2024 Adam Twardoch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOL
    
    # Create .gitignore
    cat > .gitignore << 'EOL'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.env
.venv
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOL
    
    cd ..
}

# Function to initialize a JavaScript repository
init_js_repo() {
    local repo_name=$1
    local repo_description=$2
    
    echo "Initializing $repo_name..."
    
    # Create directory if it doesn't exist
    mkdir -p "$repo_name"
    cd "$repo_name"
    
    # Initialize git if not already initialized
    if [ ! -d .git ]; then
        git init
    fi
    
    # Create package.json
    cat > package.json << EOL
{
  "name": "$repo_name",
  "version": "0.1.0",
  "description": "$repo_description",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "test": "jest",
    "build": "babel src -d lib",
    "lint": "eslint src"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/twardoch/$repo_name.git"
  },
  "keywords": [
    "markdown",
    "remark",
    "unified"
  ],
  "author": "Adam Twardoch <adam@twardoch.com>",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/twardoch/$repo_name/issues"
  },
  "homepage": "https://github.com/twardoch/$repo_name#readme",
  "dependencies": {
    "unified": "^11.0.0",
    "remark-parse": "^11.0.0",
    "remark-stringify": "^11.0.0"
  },
  "devDependencies": {
    "@babel/cli": "^7.23.0",
    "@babel/core": "^7.23.0",
    "@babel/preset-env": "^7.23.0",
    "eslint": "^8.56.0",
    "jest": "^29.7.0"
  }
}
EOL
    
    # Create src directory
    mkdir -p src
    touch src/index.js
    
    # Create tests directory
    mkdir -p test
    touch test/index.test.js
    
    # Create README.md
    cat > README.md << EOL
---
this_file: $repo_name/README.md
---

# $repo_name

$repo_description

## Installation

\`\`\`bash
npm install $repo_name
\`\`\`

## Usage

Documentation coming soon.

## License

MIT License
EOL
    
    # Create LICENSE
    cat > LICENSE << 'EOL'
MIT License

Copyright (c) 2024 Adam Twardoch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOL
    
    # Create .gitignore
    cat > .gitignore << 'EOL'
# Node
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log
.env
.DS_Store
coverage/
.nyc_output/
dist/
lib/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOL
    
    cd ..
}

# Function to initialize a documentation repository
init_docs_repo() {
    local repo_name=$1
    local repo_description=$2
    
    echo "Initializing $repo_name..."
    
    # Create directory if it doesn't exist
    mkdir -p "$repo_name"
    cd "$repo_name"
    
    # Initialize git if not already initialized
    if [ ! -d .git ]; then
        git init
    fi
    
    # Create README.md
    cat > README.md << EOL
---
this_file: $repo_name/README.md
---

# $repo_name

$repo_description

## Structure

- \`/spec/\`: Formal specification of the twardown flavor
- \`/guides/\`: User guides and tutorials
- \`/examples/\`: Example documents and use cases
- \`/dev/\`: Development documentation

## License

MIT License
EOL
    
    # Create directory structure
    mkdir -p spec guides examples dev
    
    # Create initial documentation files
    touch spec/index.md guides/getting-started.md examples/basic.md dev/contributing.md
    
    # Create LICENSE
    cat > LICENSE << 'EOL'
MIT License

Copyright (c) 2024 Adam Twardoch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOL
    
    # Create .gitignore
    cat > .gitignore << 'EOL'
# Build output
_site/
.cache/
.temp/
dist/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOL
    
    cd ..
}

# Initialize all repositories
init_python_repo "twardown-py" "Python plugin for the Python Markdown ecosystem that provides an opinionated Markdown flavor"
init_js_repo "twardown-js" "unified.js-compatible plugin wrapper for various Unified/Remark plugins"
init_docs_repo "twardown-docs" "Documentation for the twardown Markdown flavor and associated tools"

# Initialize Git repositories and add remotes
for repo in twardown-py twardown-js twardown-docs; do
    cd "$repo"
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin "https://github.com/twardoch/$repo.git"
    cd ..
done

echo "Repository initialization complete. Please run 'git push -u origin main' in each repository to push to GitHub."
