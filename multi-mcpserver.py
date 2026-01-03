import contextlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from echo_server import mcp as echo_mcp
from math_server import mcp as math_mcp
import os

#Create a combined lifespan to manage both session managers
@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(echo_mcp.session_manager.run())
        await stack.enter_async_context(math_mcp.session_manager.run())
        yield

# to run on render.com
PORT = os.environ.get("PORT", 10000)

allowed_hosts = [
    "localhost",  # for local development
    "127.0.0.1",  # for local development
    os.environ.get("RENDER_EXTERNAL_HOSTNAME", "mcp01.onrender.com") # the full Render domain
]

echo_subapp = echo_mcp.streamable_http_app()
echo_subapp.add_middleware(
    TrustedHostMiddleware, allowed_hosts=allowed_hosts
)

math_subapp = math_mcp.streamable_http_app()
math_subapp.add_middleware(
    TrustedHostMiddleware, allowed_hosts=allowed_hosts
)

app = FastAPI(lifespan=lifespan)
# app.mount("/echo", echo_mcp.streamable_http_app())
# app.mount("/math", math_mcp.streamable_http_app())
app.mount("/echo", echo_subapp)
app.mount("/math", math_subapp)

@app.get("/")
async def root():
    return {"message": "Hello MCP World"}

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=allowed_hosts
)
# app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1", "mcp01.onrender.com"]
# )

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:10000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )



# mcp = FastMCP("Community Chatters", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="0.0.0.0", port=PORT) 
    uvicorn.run(app, host="0.0.0.0", port=10000) 
    #uvicorn.run(app, host="0.0.0.0", port=8000) 
    #mcp.run(transport="streamable-http")

