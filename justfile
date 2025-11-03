# Generate navigation structure automatically
@generate-nav:
    uv run python generate_nav.py

# Serve the MkDocs site locally
@serve:
    uv run mkdocs serve

# Build the site
@build:
    uv run mkdocs build

# Generate nav and serve (recommended workflow)
@dev:
    just generate-nav
    just serve
