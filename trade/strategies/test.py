import time
import threading

from ..okex_v5 import MarketData, Trade, Account
from ..config import okex_config

class Test(threading.Thread):
    """
    test strategy
    """

    def __init__(self):
        self.api_key = okex_config["api_key"]
        self.sec_key = okex_config["secret_key"]
        self.passphrase = okex_config["passphrase"]
        self.simulate_trade = okex_config["simulate_trade"]
        self.market = MarketData(
            self.api_key, self.sec_key, self.passphrase, self.simulate_trade)
        self.trade = Trade(
            self.api_key, self.sec_key, self.passphrase, self.simulate_trade)
        self.account = Account(
            self.api_key, self.sec_key, self.passphrase, self.simulate_trade)
        super().__init__()

    def get_price(self):
        """
        get last price
        """
        tickers = self.market.get_ticker(instId="ETH-USDT-SWAP")
        # print("tickers info:", tickers.get("data"))
        last_price = tickers.get("data")[0]["last"]
        # print("price:", last_price)
        return last_price

    def cancel_pending_orders(self):
        """
        cancel pending orders
        """
        orders = self.trade.get_order_list()
        for order in orders:
            self.trade.cancel_order(instId="ETH-USDT-SWAP", ordId=order["ordId"])
            time.sleep(0.1)


    def get_account(self):
        balance = self.account.get_balance("USDT")
        return balance.get("data")[0]["details"][0]["availEq"]

    def order(self, side, px):
        """
        """
        res = self.trade.place_order(
            instId="ETH-USDT-SWAP",
            tdMode="isolated",
            side=side,
            ordType="limit",
            px=px,
            sz="1")
        print(res)

    def test_trade(self):
        balance = self.get_account()
        if float(balance) > 800:
            last_price = self.get_price()
            self.order(side="buy", px=last_price)
            time.sleep(0.1)
            new_price = float(self.get_price())*1.00005
            self.order(side="sell", px=str(new_price))
            time.sleep(0.1)
            print(f"new order: sell: {last_price}, buy: {new_price}")
        else:
            time.sleep(20)

    def run(self):
        self.cancel_pending_orders()
        res = self.account.set_leverage(lever=10, mgnMode="isolated", instId="ETH-USDT-SWAP")
        i = 0
        while True:
            try:
                self.test_trade()
                time.sleep(0.2)
                i += 1
                if i >= 200:
                    self.cancel_pending_orders()
                    i = 0
            except Exception as err:
                print("trade error: ", err)

