# Chapter 08: Building a File Client for ASNOR

## Introduction

We will build a client for our ASNOR file management server from previous Chapter. We will create a sophisticated client that connects to our file server and provides enhanced file management capabilities.

The code here is same as the code in the previous `client.py` files for the calculator project. You can skip this part and can write the code directly.

## Project Overview: ASNOR Client

### What We'll Create

We will build a client system that includes:

**Core Client Features:**
- Connect to our ASNOR file server
- Execute complex file operations
- Handle large file lists efficiently
- Progress reporting for operations


## Project Structure

We will expand our ASNOR project with a dedicated client:

```
asnor/
├── server.py    # Our file management server from Chapter 07
└── client.py    # New client implementation
```

## Implementation: Building the File Client

### Understanding the Client Code

Let's examine our `client.py` implementation:

```python
from mcp_use import MCPClient

def make_client() -> MCPClient:
    config = {
        "mcpServers": {
            "asnor": {
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

### Breaking Down the Code

**1. Import Statement**
```python
from mcp_use import MCPClient
```
- We import `MCPClient` from the `mcp_use` library
- This library provides a simplified interface for MCP client operations
- It handles the complexities of MCP protocol communication

**2. Client Configuration**
```python
config = {
    "mcpServers": {
        "asnor": {
            "command": "uv",
            "args": ["run", "server.py"],
            "env": {
                "PYTHONUNBUFFERED": "1"
            }
        }
    }
}
```

**Configuration Breakdown:**
- **`mcpServers`**: Dictionary containing all MCP servers we want to connect to
- **`"mcp01"`**: A unique identifier for our ASNOR server
- **`"command": "uv"`**: Uses the `uv` Python package manager to run our server
- **`"args": ["run", "server.py"]`**: Arguments passed to uv to execute our server
- **`"env"`**: Environment variables for the server process
- **`"PYTHONUNBUFFERED": "1"`**: Ensures output appears immediately (no buffering)

**3. Client Creation**
```python
return MCPClient.from_dict(config)
```
- Creates and returns an MCPClient instance using our configuration
- The client is now ready to connect to our ASNOR server

## How the Client Works

### Connection Process
1. **Configuration Loading**: The client reads our server configuration
2. **Process Starting**: Launches our server.py using `uv run`
3. **Protocol Handshake**: Establishes MCP communication protocol
4. **Tool Discovery**: Discovers available tools from our server
5. **Ready State**: Client is ready to execute server tools

### Environment Variables Importance
```python
"env": {
    "PYTHONUNBUFFERED": "1"
}
```

**Why This Matters:**
- **Real-time Output**: Without unbuffered output, we might not see server responses immediately
- **Debugging**: Makes it easier to debug issues between client and server
- **User Experience**: Provides immediate feedback for operations

--- 

## Extending the Client

### Adding More Servers
We can add more servers but thi code willonly cover one for simple implementation.

```python
config = {
    "mcpServers": {
        "file_server": {
            "command": "uv",
            "args": ["run", "server.py"]
        },
        "calculator_server": {
            "command": "uv", 
            "args": ["run", "calculator_server.py"]
        }
    }
}
```

### Custom Environment Variables
```python
"env": {
    "PYTHONUNBUFFERED": "1",
    "DEBUG_MODE": "true",
    "LOG_LEVEL": "INFO"
}
```
---

## Summary

We have learned to create a MCP client that connects to our ASNOR file server. We have discovered how:

- **Simple Configuration**: A few lines of code create powerful client capabilities
- **Process Management**: Clients handle server lifecycle automatically  
- **Tool Integration**: Seamless access to all server tools through unified interface
- **Environment Control**: Proper environment setup ensures reliable operation

---