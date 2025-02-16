#!/usr/bin/env bash
# this_file: 03-up.sh

set -e  # Exit on error

# Function to check if a file has been modified
check_modified() {
    local file=$1
    if git diff --quiet "$file"; then
        echo "No changes in $file"
        return 1
    else
        echo "Changes detected in $file"
        return 0
    fi
}

# Function to commit changes in a repository
commit_changes() {
    local repo_name=$1
    local log_file="LOG.md"
    local readme_file="README.md"
    local commit_msg=""
    
    # Check if files have been modified
    if check_modified "$log_file"; then
        commit_msg="${commit_msg}Update LOG.md with recent changes"
    fi
    
    if check_modified "$readme_file"; then
        if [ -n "$commit_msg" ]; then
            commit_msg="${commit_msg}, "
        fi
        commit_msg="${commit_msg}Update README.md with project status"
    fi
    
    # If no specific files were modified, use a generic message
    if [ -z "$commit_msg" ]; then
        commit_msg="Update repository files"
    fi
    
    # Add and commit changes
    git add .
    git commit -m "$commit_msg" || true
    git push
    
    # Wait for CI to start
    sleep 5
    
    # Check CI status
    echo "Checking CI status for $repo_name..."
    gh run list --repo "twardoch/$repo_name" --limit 1
}

echo "=== Updating Repositories ==="

# Update main repository
echo -e "\nUpdating main repository..."
if check_modified "LOG.md" || check_modified "README.md" || check_modified "TODO.md"; then
    git add LOG.md README.md TODO.md
    git commit -m "Update documentation files"
    git push
fi

# Update Python repository
echo -e "\nUpdating Python repository..."
cd twardown-py
commit_changes "twardown-py"

# Update JavaScript repository
echo -e "\nUpdating JavaScript repository..."
cd ../twardown-js
commit_changes "twardown-js"

# Update documentation repository
echo -e "\nUpdating documentation repository..."
cd ../twardown-docs
commit_changes "twardown-docs"

# Return to main directory and update submodules
cd ..
git submodule update --remote
git add twardown-py twardown-js twardown-docs
git commit -m "Update submodule references" || true
git push

echo -e "\n=== Update Complete ==="
echo "Please check CI status in GitHub Actions:"
echo "https://github.com/twardoch/twardown-py/actions"
echo "https://github.com/twardoch/twardown-js/actions"
echo "https://github.com/twardoch/twardown-docs/actions"
echo "https://github.com/twardoch/twardown-org/actions" 