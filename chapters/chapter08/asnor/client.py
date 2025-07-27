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