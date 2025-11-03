#!/bin/bash
set -e

# Install UV if not present
if ! command -v uv &> /dev/null; then
    echo "Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

echo "Installing dependencies with UV..."
uv sync

echo "Building site with MkDocs..."
uv run mkdocs build

echo "Build complete!"

