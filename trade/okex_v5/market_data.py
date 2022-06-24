from .client import Client

class MarketData(Client):
    """
    API of market information
    """

    def __init__(self, api_key: str, secret_key: str, passphrase: str, simulate_trade: bool) -> None:
        super().__init__(api_key, secret_key, passphrase, simulate_trade)

    def get_tickers(self, instType="SPOT", uly=None):
        """
        get market data of all products
        """
        endpoint = "/api/v5/market/tickers"
        params = {"instType": instType}
        if uly:
            params["uly"] = uly
        return self._request("GET", endpoint, params)

    def get_ticker(self, instId):
        """
        Retrieve the latest price snapshot,
        best bid/ask price, and trading volume in the last 24 hours.
        """
        endpoint = "/api/v5/market/ticker"
        params = {"instId": instId}
        return self._request("GET", endpoint, params)
