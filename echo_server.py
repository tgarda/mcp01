from mcp.server.fastmcp import FastMCP

# mcp = FastMCP(name="EchoServer", stateless_http=True)

mcp = FastMCP(
    "EchoServer",
    stateless_http=True,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=["localhost:*", "127.0.0.1:*", "mcp01.onrender.com:*"],
        allowed_origins=["http://localhost:*", "http://mcp01.onrender.com:*"],
    )
)

@mcp.tool(description="A simple echo tool")
def echo(message: str) -> str:
    return f"Echo: {message}"


