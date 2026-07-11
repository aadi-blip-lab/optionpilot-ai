"""
OptionPilot
Upstox Adapter

All Upstox-related code belongs here.
"""

import os

from config import (
    UPSTOX_CLIENT_ID,
    UPSTOX_CLIENT_SECRET,
    UPSTOX_REDIRECT_URI,
)


class UpstoxClient:

    def __init__(self):

        self.client_id = UPSTOX_CLIENT_ID

        self.client_secret = UPSTOX_CLIENT_SECRET

        self.redirect_uri = UPSTOX_REDIRECT_URI

        self.access_token = None


    def is_configured(self):

        return all([
            self.client_id,
            self.client_secret,
            self.redirect_uri
        ])


    def status(self):

        return {

            "configured": self.is_configured(),

            "logged_in": self.access_token is not None

        }


client = UpstoxClient()
