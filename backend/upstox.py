"""
OptionPilot
Upstox Client
"""

import os

import upstox_client
from upstox_client.rest import ApiException


class UpstoxClient:

    def __init__(self):

        self.client_id = os.getenv("UPSTOX_CLIENT_ID")

        self.client_secret = os.getenv("UPSTOX_CLIENT_SECRET")

        self.redirect_uri = os.getenv("UPSTOX_REDIRECT_URI")

        self.access_token = os.getenv("UPSTOX_ACCESS_TOKEN")

        configuration = upstox_client.Configuration()

        configuration.access_token = self.access_token

        self.api_client = upstox_client.ApiClient(configuration)

        self.market_api = upstox_client.MarketQuoteV3Api(
            self.api_client
        )

        self.user_api = upstox_client.UserApi(
            self.api_client
        )


    # =====================================================
    # STATUS
    # =====================================================

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


    # =====================================================
    # PROFILE
    # =====================================================

    def profile(self):

        try:

            response = self.user_api.get_profile()

            return response.to_dict()

        except ApiException as e:

            return {

                "error": str(e)

            }


    # =====================================================
    # LTP
    # =====================================================

    def get_ltp(self, instrument_key):

        try:

            response = self.market_api.get_ltp(

                instrument_key=instrument_key

            )

            return response.to_dict()

        except ApiException as e:

            return {

                "error": str(e)

            }


client = UpstoxClient()
