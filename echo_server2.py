from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

# mcp = FastMCP(name="EchoServer", stateless_http=True)

# REF: https://github.com/modelcontextprotocol/python-sdk/issues/1798
# THIS DID NOT WORK:
# mcp = FastMCP(
#     "EchoServer",
#     stateless_http=True,
#     transport_security=TransportSecuritySettings(
#         enable_dns_rebinding_protection=True,
#         allowed_hosts=["localhost:*", "127.0.0.1:*", "mcp01.onrender.com:*"],
#         allowed_origins=["http://localhost:*", "http://mcp01.onrender.com:*"],
#     )
# )

mcp = FastMCP(
    "EchoServer",
    stateless_http=True,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    )
)

@mcp.tool(description="An oauth echo tool")
def echo(message: str) -> str:
    return f"Echo from oauth mcp01: {message}"


