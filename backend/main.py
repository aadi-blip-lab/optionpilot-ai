import os
from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="OptionPilot API",
    version="0.2.0"
)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Restrict to your GitHub Pages domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# ENVIRONMENT VARIABLES
# ==========================================================

UPSTOX_CLIENT_ID = os.getenv("UPSTOX_CLIENT_ID")
UPSTOX_CLIENT_SECRET = os.getenv("UPSTOX_CLIENT_SECRET")
UPSTOX_REDIRECT_URI = os.getenv("UPSTOX_REDIRECT_URI")


# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def home():
    return {
        "application": "OptionPilot API",
        "status": "running",
        "version": "0.2.0"
    }


# ==========================================================
# CONFIG (Safe Information Only)
# ==========================================================

@app.get("/api/config")
def config():
    return {
        "client_id": UPSTOX_CLIENT_ID,
        "redirect_uri": UPSTOX_REDIRECT_URI
    }


# ==========================================================
# MARKET STATUS
# ==========================================================

@app.get("/api/status")
def status():

    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    weekday = now.weekday()

    current_minutes = now.hour * 60 + now.minute

    market_open = 9 * 60 + 15
    market_close = 15 * 60 + 30

    if weekday >= 5:
        market = "WEEKEND"

    elif current_minutes < market_open:
        market = "PRE_MARKET"

    elif current_minutes < market_close:
        market = "LIVE"

    else:
        market = "CLOSED"

    return {
        "market": market,
        "time": now.strftime("%H:%M:%S"),
        "date": now.strftime("%A, %d %B %Y")
    }


# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
