"""
OptionPilot
Configuration

Single place for all project settings.
"""

import os


# ==========================================================
# APPLICATION
# ==========================================================

APP_NAME = "OptionPilot"
APP_VERSION = "1.0.0"


# ==========================================================
# UPSTOX
# ==========================================================

UPSTOX_CLIENT_ID = os.getenv("UPSTOX_CLIENT_ID")

UPSTOX_CLIENT_SECRET = os.getenv("UPSTOX_CLIENT_SECRET")

UPSTOX_REDIRECT_URI = os.getenv("UPSTOX_REDIRECT_URI")


# ==========================================================
# MARKET
# ==========================================================

MARKET_OPEN_HOUR = 9
MARKET_OPEN_MINUTE = 15

MARKET_CLOSE_HOUR = 15
MARKET_CLOSE_MINUTE = 30


# ==========================================================
# STRATEGY
# ==========================================================

START_TRADING_HOUR = 9
START_TRADING_MINUTE = 30

STOP_NEW_TRADE_HOUR = 14
STOP_NEW_TRADE_MINUTE = 45

POWER_HOUR_START = (15, 0)
POWER_HOUR_END = (15, 25)


# ==========================================================
# RISK MANAGEMENT
# ==========================================================

MAX_CAPITAL_PER_TRADE = 1000

DAILY_MAX_LOSS = 100

DAILY_TARGET_PROFIT = 200

MAX_OPEN_POSITIONS = 1

MAX_TRADES_PER_DAY = 5


# ==========================================================
# CONFIDENCE ENGINE
# ==========================================================

MIN_CONFIDENCE_SCORE = 85
