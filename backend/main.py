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


from datetime import datetime
from zoneinfo import ZoneInfo


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
