"""
OptionPilot
Upstox API Client
"""
import upstox_client
from upstox_client.rest import ApiException
import os
import requests


class UpstoxClient:

    BASE_URL = "https://api.upstox.com/v2"

    def __init__(self):

        self.client_id = os.getenv("UPSTOX_CLIENT_ID")

        self.client_secret = os.getenv("UPSTOX_CLIENT_SECRET")

        self.redirect_uri = os.getenv("UPSTOX_REDIRECT_URI")

        self.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

    def is_configured(self):

        return all([
            self.client_id,
            self.client_secret,
            self.redirect_uri,
            self.access_token
        ])

    def status(self):

        return {
            "configured": self.is_configured(),
            "logged_in": self.access_token is not None
        }

    def headers(self):

        return {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

    def profile(self):

        response = requests.get(
            f"{self.BASE_URL}/user/profile",
            headers=self.headers(),
            timeout=15
        )

        return response.json()


client = UpstoxClient()
