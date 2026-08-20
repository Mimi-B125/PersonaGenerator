"""
README_updater.py

Automated cross-platform utility for updating file tree representations 
and dynamic metadata metrics inside README.md for PersonaGenerator.
"""

import os
import re
import sys
from pathlib import Path
from typing import Set, List, Tuple


# Configurable Exclusions (Files and Folders to omit from ASCII Tree)
DEFAULT_EXCLUDES: Set[str] = {
    ".git",
    "__pycache__",
    "md",
    ".pytest_cache",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "dist",
    "build",
    "*.pyc",
    "*.md"  # Prevents recursive tree bloat from generated markdown outputs
}

# Visual Extension Indicators for LLM/Python Codebase
FILE_ICONS = {
    ".py": "🐍",
    ".ps1": "📜",
    ".json": "📋",
    ".yaml": "⚙️",
    ".yml": "⚙️",
    ".txt": "📄",
    ".md": "📝",
    ".gitignore": "🙈",
    "LICENSE": "⚖️"
}


def load_gitignore_patterns(root_dir: Path) -> Set[str]:
    """
    Parses local .gitignore file to dynamic tree exclusion sets.
    """
    gitignore_path = root_dir / ".gitignore"
    patterns = set(DEFAULT_EXCLUDES)
    
    if gitignore_path.exists():
        with open(gitignore_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    # Strip trailing slashes for clean path matching
                    patterns.add(line.rstrip("/"))
                    
    return patterns


def should_exclude(path: Path, root_dir: Path, exclude_patterns: Set[str]) -> bool:
    """
    Checks if a given path matches any exclusion or gitignore rules.
    """
    rel_path = path.relative_to(root_dir)
    name = path.name

    for pattern in exclude_patterns:
        if pattern.startswith("*"):
            if name.endswith(pattern[1:]):
                return True
        elif name == pattern or str(rel_path) == pattern:
            return True
            
    return False


def get_file_icon(path: Path) -> str:
    """
    Maps file extensions to clean terminal indicators.
    """
    if path.is_dir():
        return "📁"
    return FILE_ICONS.get(path.suffix.lower(), FILE_ICONS.get(path.name, "📄"))


def generate_ascii_tree(
    dir_path: Path, 
    root_dir: Path, 
    exclude_patterns: Set[str], 
    prefix: str = ""
) -> Tuple[List[str], int, int]:
    """
    Recursively builds an ASCII tree while counting total Python modules and assets.
    """
    lines = []
    file_count = 0
    dir_count = 0

    # Filter directory contents based on active exclusion rules
    contents = [
        p for p in sorted(dir_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        if not should_exclude(p, root_dir, exclude_patterns)
    ]

    pointers = ["├── "] * (len(contents) - 1) + ["└── "] if contents else []

    for pointer, path in zip(pointers, contents):
        icon = get_file_icon(path)
        
        if path.is_dir():
            dir_count += 1
            lines.append(f"{prefix}{pointer}{icon} {path.name}/")
            extension = "│   " if pointer == "├── " else "    "
            sub_lines, sub_files, sub_dirs = generate_ascii_tree(
                path, root_dir, exclude_patterns, prefix=prefix + extension
            )
            lines.extend(sub_lines)
            file_count += sub_files
            dir_count += sub_dirs
        else:
            file_count += 1
            lines.append(f"{prefix}{pointer}{icon} {path.name}")

    return lines, file_count, dir_count


def update_readme():
    """
    Executes atomic reading, tree generation, and tag replacement inside README.md.
    """
    root_dir = Path(__file__).parent.resolve()
    readme_path = root_dir / "README.md"

    if not readme_path.exists():
        print(f"❌ Error: Could not locate README.md at root directory [{root_dir}]")
        sys.exit(1)

    # 1. Load Exclusions and Generate ASCII Payload
    exclude_patterns = load_gitignore_patterns(root_dir)
    tree_lines, file_count, dir_count = generate_ascii_tree(root_dir, root_dir, exclude_patterns)
    
    tree_structure = "\n".join(tree_lines)
    tree_block = f"```text\nPersonaGenerator/\n{tree_structure}\n```"

    # 2. Read Existing Readme Data
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 3. Check and Replace Content Markers
    start_marker = "<!-- TREE_START -->"
    end_marker = "<!-- TREE_END -->"

    if start_marker not in content or end_marker not in content:
        print(f"⚠️ Warning: Target markers `{start_marker}` and `{end_marker}` not found in README.md.")
        print("Please insert the comment markers inside README.md where you want the tree rendered.")
        sys.exit(0)

    pattern = re.compile(
        f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", 
        flags=re.DOTALL
    )
    
    updated_block = f"{start_marker}\n{tree_block}\n{end_marker}"
    new_content = pattern.sub(updated_block, content)

    # 4. Atomic Write Back
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("🎉 Success! Updated project architecture tree inside README.md.")
    print(f"📊 Statistics: Parsed {dir_count} directories and {file_count} active core assets.")


if __name__ == "__main__":
    update_readme()