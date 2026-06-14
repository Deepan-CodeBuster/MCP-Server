from fastapi import FastAPI
from weather import mcp

app = FastAPI()

@app.get("/")
async def health():
    return {
        "status": "healthy",
        "service": "weather-mcp"
    }

mcp_app = mcp.streamable_http_app()

app.mount("/mcp", mcp_app)