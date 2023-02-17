from trade_client import trade_client

def sell_stock(symbol, qty):
    try:
        api = trade_client()
        out = api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print(out)
        return out
    except Exception as e:
        print(e)