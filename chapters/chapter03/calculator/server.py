from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-course")

def output_formator(number: int):
    return f"the asnwer is {number}"


@mcp.tool()
def add(a:int, b:int) -> str:
    ans = a + b
    return output_formator(ans)
    
@mcp.tool()
def subtract(a:int, b:int) -> str:
    ans = a - b
    return output_formator(ans)

@mcp.tool()
def multiply(a:int, b:int) -> str:
    ans = a * b
    return output_formator(ans)

@mcp.tool()
def devide(a:int, b:int) -> str:
    ans = a // b
    return output_formator(ans)

if __name__ == "__main__":
    mcp.run(transport="stdio")

