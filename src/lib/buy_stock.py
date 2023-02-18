from rh.login import login
from robin_stocks.robinhood import rh

def buy_stock( symbol, qty):
    try:
        login()
        out = rh.order_buy_market(symbol, qty)
        print(out)
        return out
    except Exception as e:
        print(e)
        return None