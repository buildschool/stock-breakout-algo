from .trade_client import trade_client

def buy_stock( symbol, qty):
    try:
        api = trade_client()
        out = api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(out)
        return out
    except Exception as e:
        print(e)
        return None