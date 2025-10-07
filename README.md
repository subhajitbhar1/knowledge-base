# Knowledge Base Blog

A simple, beautiful blog built with Material for MkDocs.

## Setup

Create a virtual environment and install dependencies using UV:

```bash
uv venv
uv pip install mkdocs-material
```

## Usage

### Start the development server

```bash
source .venv/bin/activate
mkdocs serve
```

Then open your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Build the site

```bash
source .venv/bin/activate
mkdocs build
```

The static site will be generated in the `site/` directory.

## Adding Blog Posts

Create a new markdown file in `docs/blog/posts/` with frontmatter:

```markdown
---
date: 2025-10-07
categories:
  - Tutorial
---

# Your Post Title

Your content here...
```

## Project Structure

```
.
├── docs/
│   ├── index.md              # Home page
│   └── blog/
│       └── posts/
│           └── welcome.md    # Sample blog post
├── mkdocs.yml                # MkDocs configuration
├── pyproject.toml            # Python dependencies
└── README.md                 # This file
```

## Features

- 🎨 Material Design theme
- 🌓 Dark/Light mode
- 📝 Blog plugin
- 🔍 Search functionality
- 📱 Fully responsive
- 💻 Code syntax highlighting

That's it! Keep it simple and start writing.

