from mcp_use import MCPClient

def make_client() -> MCPClient:

    config = {
        "mcpServers": {
            "mcp01": {
                "command": "uv",
                "args": ["run", "server/server.py"],
                "env": {
                    "PYTHONUNBUFFERED": "1"
                }
            }
        }
    }

    return MCPClient.from_dict(config)
