from .okex_v5 import MarketData, Trade
import config


if __name__ == "__main__":
    api_key = config.API_KEY
    sec_key = config.SECRET_KEY
    passphrase = config.PASSPHRASE
    simulate_trade = config.SIMULATE_TRADE

    market = MarketData(api_key, sec_key, passphrase, simulate_trade)
    all_info = market.all(instType="SWAP")
    # print("all info:", all_info.get("data"))
    # data = all_info.get("data")
    # for i, x in enumerate(data):
    #     print(i, x.get("instType"), x.get("instId"))

    print("start to trade:")
    trade = Trade(api_key, sec_key, passphrase, simulate_trade)
    res = trade.place_order(
        instId="DOGE-USDT-SWAP",
        tdMode="isolated",
        side="buy",
        ordType="market",
        sz="1")
    print(res)

