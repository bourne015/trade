from .client import Client

class Account(Client):
    """
    Account
    """

    def __init__(self, api_key: str, secret_key: str, passphrase: str, simulate_trade: bool) -> None:
        super().__init__(api_key, secret_key, passphrase, simulate_trade)

    def get_balance(self, ccy=None):
        endpoint = "/api/v5/account/balance"
        params = dict(
            ccy=ccy
        )
        return self._request("GET", endpoint, params)

    def set_leverage(self, lever, mgnMode="isolated", instId=None, ccy=None, posSide=None):
        """
        """
        endpoint = "/api/v5/account/set-leverage"
        params = dict(
            instId=instId,
            ccy=ccy,
            lever=lever,
            mgnMode=mgnMode,
            posSide=posSide
        )
        return self._request("POST", endpoint, params)