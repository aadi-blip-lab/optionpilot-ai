from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from upstox import client


app = FastAPI(
    title="OptionPilot API",
    version="0.5.0"
)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def home():

    return {
        "application": "OptionPilot API",
        "status": "running",
        "version": "0.5.0"
    }


# ==========================================================
# CONFIG
# ==========================================================

@app.get("/api/config")
def config():

    return {

        "application": "OptionPilot",

        "upstox": client.status()

    }


# ==========================================================
# PROFILE
# ==========================================================

@app.get("/api/profile")
def profile():

    return client.profile()


# ==========================================================
# LIVE MARKET
# ==========================================================

@app.get("/api/market")
def market():

    quote = client.get_ltp("NSE_INDEX|Nifty 50")

    try:

        data = quote["data"]["NSE_INDEX:Nifty 50"]

        return {

            "status": "success",

            "market": "LIVE",

            "nifty": {

                "ltp": data["last_price"],

                "previous_close": data["cp"],

                "change": round(
                    data["last_price"] - data["cp"],
                    2
                ),

                "change_percent": round(
                    ((data["last_price"] - data["cp"]) / data["cp"]) * 100,
                    2
                )

            },

            "timestamp": datetime.now(
                ZoneInfo("Asia/Kolkata")
            ).strftime("%H:%M:%S")

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

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
# HEALTH
# ==========================================================

@app.get("/health")
def health():

    return {

        "status": "healthy"

    }
