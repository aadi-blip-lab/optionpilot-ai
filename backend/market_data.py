"""
OptionPilot
Market Data Engine

Version: 1.0
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketSnapshot:

    nifty: Optional[float] = None

    sensex: Optional[float] = None

    banknifty: Optional[float] = None

    india_vix: Optional[float] = None

    market_status: str = "UNKNOWN"

    timestamp: str = ""


class MarketDataProvider:

    def get_snapshot(self) -> MarketSnapshot:
        """
        Returns the latest market snapshot.

        Every provider must implement this.
        """
        raise NotImplementedError


class DummyProvider(MarketDataProvider):

    def get_snapshot(self) -> MarketSnapshot:

        return MarketSnapshot(

            nifty=25000.00,

            sensex=82000.00,

            banknifty=56000.00,

            india_vix=12.5,

            market_status="TEST",

            timestamp=""

        )


provider = DummyProvider()


def get_market_data():

    return provider.get_snapshot()
