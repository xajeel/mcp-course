from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-course")

@mcp.tool()
def add(a:int, b:int) -> int:
    return a + b
    
@mcp.tool()
def subtract(a:int, b:int) -> int:
    return a - b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    return a * b

@mcp.tool()
def devide(a:int, b:int) -> int:
    return a // b