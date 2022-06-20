from .client import Client

class Trade(Client):

    def __init__(self, api_key: str, secret_key: str, passphrase: str, simulate_trade: bool) -> None:
        super().__init__(api_key, secret_key, passphrase, simulate_trade)

    def order(
        self,
        instId=None,
        side=None,
        tdMode=None,
        ordType=None,
        sz=None,
        **kwargs
    ):
        """
        """
        endpoint = "/api/v5/trade/order"
        params = dict(
            instId=instId,
            tdMode=tdMode,
            ccy = kwargs.get("ccy", None),
            clOrdId=kwargs.get("clOrdId", None),
            tag=kwargs.get("tag", None),
            side=side,
            posSide=kwargs.get("posSide", None),
            ordType=ordType,
            sz=sz,
            px=kwargs.get("px", None),
            reduceOnly=kwargs.get("reduceOnly", None),
            tgtCcy=kwargs.get("tgtCcy", None),
            banAmend=kwargs.get("banAmend", None)
        )
        params = {k: v for k, v in params.items() if v is not None}
        return self._request("POST", endpoint, params)
