from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from typing import Any, Dict

# Create a stateless MCP server instance
# stateless_http=True means the server does not persist session state
# json_response=True ensures the server responds with JSON, which is suitable for an echo server
mcp = FastMCP(name="EchoServer", stateless_http=True, json_response=True)

@mcp.tool(description="A tool that echoes the entire payload sent to it.")
def echo(**kwargs: Any) -> Dict[str, Any]:
    """
    This tool accepts any keyword arguments and returns them as a dictionary,
    effectively echoing the payload. The use of **kwargs allows the tool to
    accept any valid JSON object as its input.
    """
    return kwargs

# Create a FastAPI application
app = FastAPI()

# Mount the MCP server application under the /mcp path
app.mount("/mcp", mcp.streamable_http_app())

if __name__ == "__main__":
    import uvicorn
    # Run the server using uvicorn, a fast ASGI server
    uvicorn.run(app, host="0.0.0.0", port=8000)
