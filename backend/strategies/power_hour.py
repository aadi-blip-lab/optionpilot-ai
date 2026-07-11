"""
OptionPilot

Power Hour Strategy

Version 1.0
"""


from dataclasses import dataclass

from market_data import MarketSnapshot

from config import (


    MAX_CAPITAL_PER_TRADE,

    DAILY_MAX_LOSS,

    MIN_CONFIDENCE_SCORE

)


@dataclass

class StrategyResult:

    signal: str

    confidence: int

    reason: str

    capital: int

    allowed: bool


class PowerHourStrategy:


    def evaluate(self, market: MarketSnapshot):

        """
        Version 1

        Dummy logic.

        Real indicators come later.
        """

        confidence = 0

        reasons = []


        # -----------------------
        # Market Status
        # -----------------------

        if market.market_status == "LIVE":

            confidence += 20

            reasons.append("Market Live")


        # -----------------------
        # India VIX
        # -----------------------

        if market.india_vix is not None:

            if market.india_vix < 15:

                confidence += 15

                reasons.append("Low Volatility")


        # -----------------------
        # Dummy Trend
        # -----------------------

        if market.nifty is not None:

            confidence += 25

            reasons.append("Trend Filter Passed")


        # -----------------------
        # Dummy Volume
        # -----------------------

        confidence += 20

        reasons.append("Volume OK")


        # -----------------------
        # Dummy Option Chain
        # -----------------------

        confidence += 20

        reasons.append("OI Confirmation")


        signal = "NO TRADE"

        allowed = False


        if confidence >= MIN_CONFIDENCE_SCORE:

            signal = "BUY"

            allowed = True


        return StrategyResult(

            signal=signal,

            confidence=confidence,

            reason=", ".join(reasons),

            capital=MAX_CAPITAL_PER_TRADE,

            allowed=allowed

        )


strategy = PowerHourStrategy()
