# Chapter 3: First MCP Server

## What is an MCP Server?

An MCP server is a program that provides tools, resources, or prompts that AI models can use to extend their capabilities. Think of it as a bridge between the AI model and external functionality. The server communicates with AI clients using the standardized MCP protocol.

Key concepts:
- **Tools**: Functions that the AI can call to perform specific tasks
- **Protocol**: Standardized communication between server and client
- **Transport**: How messages are sent (stdio, HTTP, etc.)

## Project: Simple Calculator Server

You'll create a calculator server with four basic operations: addition, subtraction, multiplication, and division.

### File Structure
```
calculator/
├── server.py
└── (future chapters will add more files)
```

## Building the Calculator Server

### Step 1: Setting Up the Server

Create a new file called `server.py` in your calculator directory. We'll use the FastMCP library, which simplifies MCP server development.

```bash
uv add "mcp[cli]"
```

```python
from mcp.server.fastmcp import FastMCP

# Create a new MCP server instance
mcp = FastMCP("mcp-course")
```

The `FastMCP` class handles all the MCP protocol details for us. The name "mcp-course" identifies our server.

### Step 2: Creating a Helper Function

We'll create a utility function to format our responses consistently:

```python
def output_formator(number: int):
    return f"the answer is {number}"
```

This function takes a number and returns a formatted string. Having consistent output formatting makes our tools more user-friendly.

### Step 3: Implementing Calculator Tools

Now we'll create four tools using the `@mcp.tool()` decorator:

This decorator registers a function as an MCP tool. When decorated:
- The function becomes available to AI clients
- MCP automatically handles the communication protocol
- Type hints help clients understand expected parameters

#### Addition Tool
```python
@mcp.tool()
def add(a: int, b: int) -> str:
    ans = a + b
    return output_formator(ans)
```

#### Subtraction Tool
```python
@mcp.tool()
def subtract(a: int, b: int) -> str:
    ans = a - b
    return output_formator(ans)
```

#### Multiplication Tool
```python
@mcp.tool()
def multiply(a: int, b: int) -> str:
    ans = a * b
    return output_formator(ans)
```

#### Division Tool
```python
@mcp.tool()
def divide(a: int, b: int) -> str:
    ans = a // b  # Integer division
    return output_formator(ans)
```

**Note**: We're using integer division (`//`) to keep results as integers. In a production calculator, you might want to handle floating-point division and division by zero.

### Step 4: Running the Server

The final piece starts the server when the script is run directly:

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

The `stdio` (Explanation is given at the end) transport means the server communicates through standard input/output, which is common for MCP servers.

## Complete Server Code

Here's the complete `server.py` file:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-course")

def output_formator(number: int):
    return f"the answer is {number}"

@mcp.tool()
def add(a: int, b: int) -> str:
    ans = a + b
    return output_formator(ans)

@mcp.tool()
def subtract(a: int, b: int) -> str:
    ans = a - b
    return output_formator(ans)

@mcp.tool()
def multiply(a: int, b: int) -> str:
    ans = a * b
    return output_formator(ans)

@mcp.tool()
def divide(a: int, b: int) -> str:
    ans = a // b
    return output_formator(ans)

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

## Understanding the Code

### Server Lifecycle
1. Server starts and registers tools
2. AI client connects via stdio
3. Client can discover available tools
4. Client calls tools with parameters
5. Server executes tools and returns results

---

## MCP Transport Protocols

**Transport protocols** define how your MCP server and AI client communicate.

---

### 1. stdio (Standard Input/Output)

> **Analogy:** Like a **direct phone call** — instant, private, and two-way.

* Your program writes output to `stdout` and reads input from `stdin`.
* It's **direct and fast**, usually used when both processes are on the same machine.
* Common in CLI-based tools.
* **No network connection required**.
* Very efficient and low-latency.

**In MCP:**

The AI client spawns your server process and communicates via standard input/output streams — just like a terminal conversation.

---

### 2. SSE (Server-Sent Events)

> **Analogy:** Like **live notifications** — the server keeps pushing updates.

* Runs over **HTTP**.
* One-way communication: server → client.
* The client opens a persistent connection and keeps listening.
* Commonly used in web apps for **real-time updates** (e.g., news tickers, chat apps).

**In MCP:**

The AI client connects to a server (via a URL like `http://localhost:8000/mcp`) and receives a **stream of responses** from the server, like real-time updates.

---

### Summary Table

| Protocol | Analogy               | Direction | Requires Network | Use Case                       |
| -------- | --------------------- | --------- | ---------------- | ------------------------------ |
| `stdio`  | Phone call (terminal) | Two-way   | No             | Local dev, CLI tools, fast I/O |
| `SSE`    | Notifications (web)   | One-way   | Yes            | Remote tools, web integration  |

---
