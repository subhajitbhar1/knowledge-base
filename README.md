# Knowledge Base

A comprehensive knowledge base built with Material for MkDocs, featuring automatic navigation generation and breadcrumb support.

## Setup

Install dependencies using UV:

```bash
uv sync
```

## Usage

### Recommended Workflow (using just)

The project uses `just` for task automation. Here are the available commands:

```bash
# Generate navigation and start dev server
just dev

# Only generate navigation structure
just generate-nav

# Only start the dev server
just serve

# Build the site
just build
```

### Manual Workflow

If you prefer not to use `just`:

```bash
# Generate navigation structure
uv run python generate_nav.py

# Start the development server
uv run mkdocs serve

# Build the site
uv run mkdocs build
```

Then open your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Adding New Content

### Adding a New Article to an Existing Topic

1. Create a new markdown file in the appropriate directory (e.g., `docs/python-lists/my-new-article.md`)
2. Add frontmatter with title and metadata:

```markdown
---
title: My New Article Title
description: Brief description
meta:
  - name: robots
    content: index, follow
  - name: keywords
    content: python, lists, tutorial
---

# My New Article Title

Your content here...
```

3. Run `just generate-nav` to update the navigation automatically
4. The article will appear in the navigation under the appropriate section

### Adding a New Topic (e.g., Machine Learning)

1. Create a new topic page: `docs/machine-learning.md`
2. Create a directory for subtopics: `docs/machine-learning-basics/`
3. Add articles to the subtopic directory
4. Run `just generate-nav` to update the navigation automatically

The naming convention is important: subdirectories should be prefixed with the topic name (e.g., `machine-learning-basics`, `machine-learning-advanced`) to be automatically grouped under the `machine-learning.md` topic.

## Project Structure

```
.
├── docs/
│   ├── index.md                    # Home page
│   ├── python.md                   # Python topic page
│   ├── python-lists/               # Python Lists subtopic
│   │   ├── index.md
│   │   └── *.md                    # Individual articles
│   ├── python-tuples/              # Python Tuples subtopic
│   │   ├── index.md
│   │   └── *.md
│   └── python-async/               # Python Async subtopic
│       ├── index.md
│       └── *.md
├── overrides/
│   └── partials/
│       └── breadcrumbs.html        # Custom breadcrumb template
├── generate_nav.py                 # Automatic navigation generator
├── mkdocs.yml                      # MkDocs configuration
├── pyproject.toml                  # Python dependencies
├── justfile                        # Task automation
└── README.md                       # This file
```

## Navigation Structure

The navigation is automatically generated based on your file structure:

```
Knowledge Base (Home)
└── Python Articles
    ├── python.md
    ├── Lists
    │   ├── index.md
    │   └── [all list articles]
    ├── Tuples
    │   ├── index.md
    │   └── [all tuple articles]
    └── Async
        ├── index.md
        └── [all async articles]
```

## Breadcrumbs

Breadcrumbs are automatically generated for all pages except the home page:

- **Python page**: `Knowledge Base > Python Articles`
- **Lists index**: `Knowledge Base > Python Articles > Lists > Python Lists`
- **Individual article**: `Knowledge Base > Python Articles > Lists > [Article Title]`

## Features

- 🎨 Material Design theme
- 🌓 Dark/Light mode
- 🔍 Advanced search functionality
- 📱 Fully responsive
- 💻 Code syntax highlighting
- 🗺️ Automatic breadcrumb navigation
- 🔄 Automatic navigation generation
- 📊 Hierarchical content organization

## Workflow Summary

1. Add new markdown files to your docs directory
2. Run `just generate-nav` to update navigation
3. Run `just serve` to preview (or use `just dev` to do both)
4. Commit and deploy

That's it! The navigation structure updates automatically based on your file organization.

