from login import login
import robin_stocks

def sell_stock(symbol, qty):
    try:
        login()
        out = robin_stocks.robinhood.order_sell_market(symbol, qty)
        print(out)
        return out
    except Exception as e:
        print(e)