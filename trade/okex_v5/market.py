from .client import Client

class Market(Client):
    """
    API of market information
    """

    def __init__(self, api_key: str, secret_key: str, passphrase: str, simulate_trade: bool) -> None:
        super().__init__(api_key, secret_key, passphrase, simulate_trade)

    def all(self, info_type="SPOT", uly=None):
        """
        get market data of all products
        """
        endpoint = "/api/v5/market/tickers"
        params = {"instType": info_type}
        if uly:
            params["uly"] = uly
        return self._request("GET", endpoint, params)
