from .trade_client import trade_client

def buy_stock( symbol, qty):
    api = trade_client()
    out = api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    return out
