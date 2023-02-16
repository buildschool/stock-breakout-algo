from .trade_client import trade_client

def sell_stock(symbol, qty):
    api = trade_client()
    out = api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    return out