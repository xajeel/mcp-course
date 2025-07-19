# Chapter 4: First MCP Client

## What is an MCP Client?

An **MCP client** is like a remote control for your MCP server. Just like how you use a TV remote to control your television, an MCP client controls and communicates with MCP servers.

Simple analogy: If your MCP server is a restaurant kitchen, the MCP client is the waiter who takes orders from customers and brings them to the kitchen.

The client:
- Connects to MCP servers
- Discovers what tools are available
- Sends requests to use those tools
- Receives results back from the server

### Client vs Server Roles
- **Server**: Provides tools and does the actual work (like the calculator functions)
- **Client**: Requests work to be done and receives results (like asking for calculations)

## Project: Simple Calculator Server Client

You'll create a simple client that connects to your calculator server and can discover the available tools (add, subtract, multiply, divide).

### File Structure
```
calculator/
├── server.py    (from Chapter 3)
└── client.py    (new file)
```

## Building the Calculator Client

### Step 1: Setting Up the Client

```bash
uv add mcp-use
```

```python
from mcp_use import MCPClient
```
This imports the MCP client library that handles all the communication protocol for us.

---

### Step 2: Configuration Dictionary
The `config` dictionary tells the client how to find and start your server:

```python
config = {
    "mcpServers": {
        "calculator": {
            "command": "uv",
            "args": ["run", "server.py"],
            "env": {
                "PYTHONUNBUFFERED": "1"
            }
        }
    }
}
```

Let's understand each part:

- **`"mcpServers"`**: This section lists all the servers this client can connect to
- **`"calculator"`**: This is the name we give to our server (you can choose any name)
- **`"command": "uv"`**: This tells the client to use the `uv` command to run the server
- **`"args": ["run", "server.py"]`**: These are the arguments passed to the command (`uv run server.py`)
- **`"env"`**: Environment variables for the server
- **`"PYTHONUNBUFFERED": "1"`**: This ensures output appears immediately (no buffering)

---

### Step 3: Creating the Client

```python
return MCPClient.from_dict(config)
```
This creates an actual MCP client using our configuration.

---

## Complete Client Code

Here's the complete `client.py` file:

```python
from mcp_use import MCPClient

def make_client() -> MCPClient:
    config = {
        "mcpServers": {
            "calculator": {
                "command": "uv",
                "args": ["run", "server.py"],
                "env": {
                    "PYTHONUNBUFFERED": "1"
                }
            }
        }
    }
    
    return MCPClient.from_dict(config)
```

---

## How Client-Server Communication Works

Think of it like ordering food:

1. **Client connects** (You call the restaurant)
2. **Server starts** (Restaurant answers and is ready to take orders)
3. **Client discovers tools** (You ask "What's on the menu?")
4. **Server lists tools** (Restaurant tells you: pizza, burgers, pasta)
5. **Client calls tools** (You order: "One pizza, please")
6. **Server processes** (Kitchen makes the pizza)
7. **Server returns result** (Restaurant delivers your pizza)

---

## Understanding the Configuration

### Environment Variables
```python
"env": {
    "PYTHONUNBUFFERED": "1"
}
```
This is like telling Python: "Don't wait to show output, show it immediately." It helps with debugging and real-time communication.


### Configuration-Based Setup
Instead of hardcoding connection details, we use a configuration dictionary. This makes it easy to:
- Connect to different servers
- Change server settings
- Add more servers later

---