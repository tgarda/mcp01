from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# mcp = FastMCP(name="MathServer", stateless_http=True)

mcp = FastMCP(
    "MathServer",
    stateless_http=True,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=["localhost:*", "127.0.0.1:*", "mcp01.onrender.com:*"],
        allowed_origins=["http://localhost:*", "http://mcp01.onrender.com:*"],
    )
)

@mcp.tool(description="A simple add tool")
def add_two(n: int) -> int:
    return n + 2

