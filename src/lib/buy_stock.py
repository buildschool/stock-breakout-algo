from login import login
import robin_stocks

def buy_stock( symbol, qty):
    try:
        login()
        out = robin_stocks.robinhood.order_buy_market(symbol, qty)
        print(out)
        return out
    except Exception as e:
        print(e)
        return None