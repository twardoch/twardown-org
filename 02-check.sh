#!/usr/bin/env bash
# this_file: 02-check.sh

set -e  # Exit on error

echo "=== Project Structure ==="
tree -a -I '.git|.venv|node_modules|__pycache__|*.pyc' > tree.txt
cat tree.txt

echo -e "\n=== Python Package Status ==="
cd twardown-py
echo "Python version:"
python --version
echo "Running tests:"
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    ~/.cargo/bin/uv venv
    source .venv/bin/activate
fi
~/.cargo/bin/uv pip install -e ".[dev]"
python -m pytest --cov=twardown_py tests/
echo "Running type checks:"
mypy src/twardown_py
echo "Running linting:"
ruff check .
ruff format --check .

echo -e "\n=== JavaScript Package Status ==="
cd ../twardown-js
echo "Node.js version:"
node --version
echo "npm version:"
npm --version
echo "Installing dependencies:"
npm install
echo "Running tests:"
npm test
echo "Running linting:"
npm run lint
npm run format:check

echo -e "\n=== Documentation Status ==="
cd ../twardown-docs
echo "Installing dependencies:"
npm install
echo "Running Markdown linting:"
npm run lint
echo "Running format check:"
npm run format:check
echo "Checking links:"
npm run check-links

echo -e "\n=== CI Status ==="
cd ..
echo "Checking GitHub Actions status:"
gh run list --repo twardoch/twardown-py --limit 1
gh run list --repo twardoch/twardown-js --limit 1
gh run list --repo twardoch/twardown-docs --limit 1
gh run list --repo twardoch/twardown-org --limit 1

echo -e "\n=== Git Status ==="
echo "Main repository:"
git status
echo -e "\nPython repository:"
cd twardown-py
git status
echo -e "\nJavaScript repository:"
cd ../twardown-js
git status
echo -e "\nDocumentation repository:"
cd ../twardown-docs
git status

cd ..
echo -e "\n=== Check Complete ===" 