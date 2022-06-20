from okex_v5 import Market, Trade
import config


if __name__ == "__main__":
    api_key = config.API_KEY
    sec_key = config.SECRET_KEY
    passphrase = config.PASSPHRASE
    simulate_trade = config.SIMULATE_TRADE

    market = Market(api_key, sec_key, passphrase, simulate_trade)
    all_info = market.all(info_type="SWAP")
    # print("all info:", all_info.get("data"))

    print("start to trade:")
    trade = Trade(api_key, sec_key, passphrase, simulate_trade)
    res = trade.order(
        instId="BTC-USDT-SWAP",
        tdMode="isolated",
        side="buy",
        posSide="long",
        ordType="market",
        sz="1")
    print(res)
