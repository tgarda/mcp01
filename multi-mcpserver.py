import contextlib
from fastapi import FastAPI
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

app = FastAPI(lifespan=lifespan)
app.mount("/echo", echo_mcp.streamable_http_app())
app.mount("/math", math_mcp.streamable_http_app())

# mcp = FastMCP("Community Chatters", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT) 
    #uvicorn.run(app, host="0.0.0.0", port=8000) 
    #mcp.run(transport="streamable-http")

