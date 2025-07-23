import os
import subprocess
from mcp.server.fastmcp import FastMCP 
import logging

logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger('mcp_use').setLevel(logging.CRITICAL)

mcp = FastMCP(name="DirectoryManager")

IGNORED = {'__pycache__', '.git', '.venv'}

def list_tree(path: str) -> str:
    """Return tree of path, ignoring certain directories."""
    lines = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORED]
        level = root.replace(path, '').count(os.sep)
        indent = "│   " * level
        lines.append(f"{indent}{'├── ' if level>0 else ''}{os.path.basename(root)}/")
        sub = "│   " * (level + 1)
        for f in files:
            lines.append(f"{sub}└── {f}")
    return "\n".join(lines)


@mcp.tool()
def show_directory(path: str) -> str:
    """List directory structure starting from path."""
    if not os.path.isdir(path):
        raise FileNotFoundError(f"{path} not found or not a directory")
    return list_tree(path)


@mcp.tool()
def create_file(path: str, content: str = "") -> str:
    """Create a new file with given content."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Created file {path}"


@mcp.tool()
def edit_file(path: str, new_content: str) -> str:
    """Overwrite an existing file with new content."""
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return f"Edited file {path}"


@mcp.tool()
def append_file(path: str, content: str) -> str:
    """Append content to an existing file."""
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    return f"Appended to {path}"


@mcp.tool()
def delete_file(path: str) -> str:
    """Delete a specified file."""
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    os.remove(path)
    return f"Deleted file {path}"


@mcp.tool()
def run_shell_command(command: str) -> str:
    """
    Run a terminal command and return the output.
    Example: "Run the command 'ls -la'"
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return f"Output:\n{result.stdout.strip()}"
    except subprocess.CalledProcessError as e:
        return f"Error:\n{e.stderr.strip()}"


if __name__ == "__main__":
    mcp.run(transport="stdio")