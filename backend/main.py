from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OptionPilot API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # We'll restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "application": "OptionPilot API",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/api/status")
def status():
    return {
        "market": "PRE_OPEN",
        "session": "Morning",
        "countdown": "00:45:21",
        "connected": True,
        "broker": "Upstox (Coming Soon)"
    }
