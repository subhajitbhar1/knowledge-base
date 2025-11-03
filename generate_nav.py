from pathlib import Path

import yaml


def get_title_from_md(file_path: Path) -> str | None:
    """Extract title from markdown frontmatter or first heading."""
    try:
        with Path(file_path).open(encoding="utf-8") as f:
            content = f.read()

            # Try to get title from frontmatter
            if content.startswith("---"):
                lines = content.split("\n")
                for line in lines[1:]:
                    if line.strip() == "---":
                        break
                    if line.startswith("title:"):
                        title = line.replace("title:", "").strip()
                        return title.strip('"').strip("'")

            # Fallback to first H1 heading
            for line in content.split("\n"):
                if line.startswith("# "):
                    return line.replace("# ", "").strip()
    except Exception as e:
        print(f"Error getting title from {file_path}: {e}")
        raise e

    return None


def get_subtopic_title(dir_name: str) -> str:
    """Convert directory name to a nice title (e.g., python-lists -> Lists)."""
    # Remove common prefixes
    name = dir_name
    for prefix in ["python-", "py-"]:
        if name.startswith(prefix):
            name = name[len(prefix) :]
            break

    # Convert to title case
    return name.replace("-", " ").title()


def find_related_directories(docs_dir: Path, parent_file: Path) -> list[Path]:
    parent_name = parent_file.stem
    related_dirs = []

    for item in docs_dir.iterdir():
        if item.is_dir() and item.name.startswith(f"{parent_name}-"):
            related_dirs.append(item)

    return sorted(related_dirs)


def generate_nav(docs_dir: Path) -> list:
    nav = []

    nav.append({"Home": "index.md"})

    # Get all top-level markdown files (excluding index.md and special files)
    top_level_files = sorted(
        [
            item
            for item in docs_dir.iterdir()
            if item.is_file()
            and item.suffix == ".md"
            and item.name not in ["index.md", "CNAME", "robots.txt", "llms.txt"]
        ],
    )

    # Track which directories have been processed
    processed_dirs = set()

    for topic_file in top_level_files:
        # Get the title for this topic
        topic_title = (
            get_title_from_md(topic_file)
            or topic_file.stem.replace(
                "-",
                " ",
            ).title()
        )

        # Find related subdirectories (e.g., python-lists, python-tuples for python.md)
        related_dirs = find_related_directories(docs_dir, topic_file)

        if related_dirs:
            # This is a topic with subtopics
            topic_nav = [topic_file.name]  # Add the main topic file first

            for subdir in related_dirs:
                processed_dirs.add(subdir.name)

                # Get subtopic title
                subtopic_title = get_subtopic_title(subdir.name)

                # Get all markdown files in this subdirectory
                md_files = sorted(
                    [f for f in subdir.iterdir() if f.is_file() and f.suffix == ".md"],
                )

                if not md_files:
                    continue

                # Create subtopic structure
                subtopic_nav = []

                # Add index.md first if it exists
                index_file = subdir / "index.md"
                if index_file.exists():
                    subtopic_nav.append(f"{subdir.name}/index.md")

                # Add all other markdown files
                for md_file in md_files:
                    if md_file.name != "index.md":
                        subtopic_nav.append(f"{subdir.name}/{md_file.name}")

                # Add subtopic to topic nav
                if subtopic_nav:
                    topic_nav.append({subtopic_title: subtopic_nav})

            nav.append({topic_title: topic_nav})
        else:
            # Standalone topic file without subdirectories
            nav.append({topic_title: topic_file.name})

    # Handle any remaining directories that weren't linked to a parent file
    remaining_dirs = [
        item
        for item in docs_dir.iterdir()
        if item.is_dir() and item.name not in processed_dirs
    ]

    for subdir in sorted(remaining_dirs):
        topic_title = get_subtopic_title(subdir.name)

        # Get all markdown files
        md_files = sorted(
            [f for f in subdir.iterdir() if f.is_file() and f.suffix == ".md"],
        )

        if not md_files:
            continue

        topic_nav = []

        # Add index.md first if it exists
        index_file = subdir / "index.md"
        if index_file.exists():
            topic_nav.append(f"{subdir.name}/index.md")

        # Add all other markdown files
        for md_file in md_files:
            if md_file.name != "index.md":
                topic_nav.append(f"{subdir.name}/{md_file.name}")

        if topic_nav:
            nav.append({topic_title: topic_nav})

    return nav


def update_mkdocs_config(nav_structure: list):
    """Update mkdocs.yml with new navigation structure."""
    mkdocs_file = Path("mkdocs.yml")

    # Read existing config
    with open(mkdocs_file, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Update nav
    config["nav"] = nav_structure

    # Write back to file
    with open(mkdocs_file, "w", encoding="utf-8") as f:
        yaml.dump(
            config,
            f,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
        )

    print(f"✅ Updated {mkdocs_file} with {len(nav_structure)} navigation items")


def main():
    """Main function to generate and update navigation."""
    docs_dir = Path("docs")

    if not docs_dir.exists():
        print(f"❌ Error: {docs_dir} directory not found")
        return

    print("🔍 Scanning docs directory...")
    nav_structure = generate_nav(docs_dir)

    print(f"📝 Generated navigation with {len(nav_structure)} top-level items")

    print("💾 Updating mkdocs.yml...")
    update_mkdocs_config(nav_structure)

    print("✨ Done! Your navigation structure has been updated automatically.")


if __name__ == "__main__":
    main()
