# Chapter 07: Building ASNOR - A CLI-Based File Management Agent

## Introduction

We will build a basic version of a CLI-based agent called **ASNOR** (AI System for Navigation, Organization & Retrieval). ASNOR will serve as our personal file assistant, capable of managing files and directories with intelligent conversation-based commands.

This project represents a significant step forward in our MCP journey, as we will create a practical tool that combines file system operations with AI-powered natural language understanding.

## Project Overview: Personal File Assistant

### What We'll Build

We will create a comprehensive file management system that includes:

**Core File Operations:**
- Create, read, update, and delete files
- Directory navigation and visualization
- File search capabilities
- Text file content manipulation
- Shell command execution

**Tools We'll Implement:**
- `show_directory(path)` - Display directory structure in tree format
- `create_file(filepath, content)` - Create new files with content
- `edit_file(filepath, new_content)` - Overwrite existing files
- `append_file(filepath, content)` - Add content to existing files
- `delete_file(filepath)` - Remove files from the system
- `run_shell_command(command)` - Execute terminal commands

### Why ASNOR?

ASNOR represents the evolution from simple calculator tools to practical, real-world applications. This agent will:
- Understand natural language requests for file operations
- Provide intelligent feedback and error handling
- Execute complex multi-step file management tasks
- Serve as a foundation for more advanced AI assistants

## Project Structure

We will keep our structure simple and focused:

```
asnor/
└── server.py    # Complete MCP server with all file management tools
```

We're consolidating everything into a single server file to demonstrate how powerful MCP servers can be when they provide comprehensive functionality within a specific domain.

## Implementation: Building the File Management Server

### Step 1: Server Setup and Configuration

Let's examine our `server.py` implementation:

```python
import os
import subprocess
from mcp.server.fastmcp import FastMCP 
import logging

logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger('mcp_use').setLevel(logging.CRITICAL)

mcp = FastMCP(name="DirectoryManager")

IGNORED = {'__pycache__', '.git', '.venv'}
```

**Key Components:**
- **FastMCP Server**: Our main server instance named "DirectoryManager"
- **Logging Configuration**: Suppresses verbose logging for cleaner output
- **IGNORED Directories**: Filters out system directories that shouldn't be displayed

### Step 2: Directory Visualization Tool

```python
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
```

**What This Does:**
- Creates a visual tree representation of directory structures
- Filters out unwanted system directories
- Uses Unicode characters for professional tree formatting
- Provides clear hierarchy visualization

### Step 3: File Creation and Management

```python
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
```

**File Management Features:**
- **Smart Directory Creation**: Automatically creates parent directories if they don't exist
- **UTF-8 Encoding**: Ensures proper handling of international characters
- **Error Handling**: Provides clear feedback when files don't exist
- **Flexible Operations**: Support for both overwriting and appending content

### Step 4: File Deletion and Shell Commands

```python
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
```

**Advanced Features:**
- **Safe File Deletion**: Verifies file existence before deletion
- **Shell Integration**: Executes system commands with proper error handling
- **Output Capture**: Returns both successful output and error messages
- **Security Considerations**: Uses subprocess.run for safer command execution

## Understanding ASNOR's Capabilities

### 1. Intelligent Directory Navigation
ASNOR can display directory structures in a clean, tree-like format that makes it easy to understand project organization:

```
project/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
└── README.md
```

### 2. Comprehensive File Operations
- **Create**: Generate new files with initial content
- **Edit**: Completely replace file contents
- **Append**: Add content to existing files
- **Delete**: Remove files safely with verification

### 3. Shell Command Integration
Execute system commands directly through natural language:
- "Run the command 'ls -la' to see detailed file information"
- "Execute 'git status' to check repository status"
- "Run 'python main.py' to execute the script"

### 4. Error Handling and Feedback
ASNOR provides clear, informative responses:
- Success confirmations with specific file paths
- Detailed error messages when operations fail
- Helpful suggestions for resolving issues


## Security Considerations

When building file management systems like ASNOR, we must consider:

### 1. Path Validation
- Always validate file paths to prevent directory traversal attacks
- Use absolute paths when possible
- Restrict operations to specific directories if needed

### 2. Command Execution Safety
- The `run_shell_command` tool should be used carefully
- Consider implementing command whitelisting for production use
- Always capture and handle both stdout and stderr

### 3. File Permissions
- Respect system file permissions
- Handle permission errors gracefully
- Consider user context when performing operations


## Summary

We have successfully built ASNOR, a comprehensive file management agent that demonstrates the power of MCP servers for real-world applications. We have learned to:

- Create sophisticated MCP servers with multiple interconnected tools
- Implement file system operations with proper error handling
- Design user-friendly interfaces for complex operations
- Integrate shell command execution safely
- Build practical AI assistants for everyday tasks

---