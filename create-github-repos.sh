#!/usr/bin/env bash
# this_file: create-github-repos.sh

set -e  # Exit on error

# Function to create a GitHub repository
create_github_repo() {
    local repo_name=$1
    local description=$2
    
    echo "Creating GitHub repository: $repo_name..."
    
    # Create the repository on GitHub
    gh repo create "twardoch/$repo_name" --public --description "$description" || true
    
    # Navigate to the repository directory
    cd "$repo_name"
    
    # Set up the remote and push
    git branch -M main
    git remote remove origin || true
    git remote add origin "https://github.com/twardoch/$repo_name.git"
    git push -u origin main
    
    cd ..
}

# Create the repositories
create_github_repo "twardown-docs" "Documentation for the Twardown Markdown flavor and associated tools"
create_github_repo "twardown-js" "unified.js-compatible plugin wrapper for various Unified/Remark plugins"
create_github_repo "twardown-py" "Python plugin for the Python Markdown ecosystem"

# Create the main repository
gh repo create "twardoch/twardown-org" --public --description "Collection of repositories related to Twardown, an opinionated Markdown flavor" || true
git branch -M main
git remote remove origin || true
git remote add origin "https://github.com/twardoch/twardown-org.git"
git push -u origin main

echo "GitHub repositories created and code pushed successfully." 