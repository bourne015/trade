from .client import Client

class Trade(Client):

    def __init__(self, api_key: str, secret_key: str, passphrase: str, simulate_trade: bool) -> None:
        super().__init__(api_key, secret_key, passphrase, simulate_trade)

    def place_order(
        self,
        instId=None,
        side=None,
        tdMode=None,
        ordType=None,
        sz=None,
        **kwargs
    ):
        """
        You can place an order only if you have sufficient funds.
        """
        endpoint = "/api/v5/trade/order"
        params = dict(
            instId=instId,
            tdMode=tdMode,
            ccy=kwargs.get("ccy", None),
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

    def place_multiple_orders(self):
        """
        Place orders in batches.
        Maximum 20 orders can be placed at a time.
        Request parameters should be passed in the form of an array.
        """
        endpoint = "/api/v5/trade/batch-orders"

    def cancel_order(self, instId: str, ordId=None, clOrdId=None):
        """
        Cancel an incomplete order.
        """
        endpoint = "/api/v5/trade/cancel-order"
        if ordId is None and clOrdId is None:
            return None
        params = dict(
            instId=instId,
            ordId=ordId,
            clOrdId=clOrdId
        )
        return self._request("POST", endpoint, params)

    def cancel_multiple_orders(self, instId: str, ordId=None, clOrdId=None):
        """
        Cancel incomplete orders in batches.
        Maximum 20 orders can be canceled at a time.
        Request parameters should be passed in the form of an array.
        """
        endpoint = "/api/v5/trade/cancel-order"
        if ordId is None and clOrdId is None:
            return None
        params = dict(
            instId=instId,
            ordId=ordId,
            clOrdId=clOrdId
        )
        return self._request("POST", endpoint, params)

    def close_positions(self):
        """
        Close all positions of an instrument via a market order.
        """
        endpoint = "/api/v5/trade/close-position"

    def get_order_details(self):
        """
        Retrieve order details.
        """
        endpoint = "/api/v5/trade/order"

    def get_order_list(
        self,
        instType=None,
        uly=None,
        instId=None,
        ordType=None,
        state=None,
        after=None,
        before=None,
        limit=None
    ):
        """
        Retrieve all incomplete orders under the current account.
        """
        endpoint = "/api/v5/trade/orders-pending"
        params = dict(
            instType=instType,
            uly=uly,
            instId=instId,
            ordType=ordType,
            state=state,
            after=after,
            before=before,
            limit=limit
        )
        res = self._request("GET", endpoint, params)
        return res["data"]

    def place_algo_order(self):
        """
        The algo order includes trigger order, oco order,
        conditional order,iceberg order, twap order and trailing order.
        """
        endpoint = "/api/v5/trade/order-algo"

    def cancel_algo_order(self):
        """
        Cancel unfilled algo orders (not including Iceberg order, TWAP order, Trailing Stop order).
        A maximum of 10 orders can be canceled at a time.
        Request parameters should be passed in the form of an array.
        """
        endpoint = "/api/v5/trade/cancel-algos"

    def cancel_advance_algo_order(self):
        """
        Cancel unfilled algo orders (including Iceberg order, TWAP order, Trailing Stop order).
        A maximum of 10 orders can be canceled at a time.
        Request parameters should be passed in the form of an array.
        """
        endpoint = "/api/v5/trade/cancel-advance-algos"

    def get_algo_order_list(self):
        """
        Retrieve a list of untriggered Algo orders under the current account.
        """
        endpoint = "/api/v5/trade/orders-algo-pending"
