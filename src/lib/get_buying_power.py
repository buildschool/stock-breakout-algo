from .trade_client import trade_client

def get_buying_power():
    client = trade_client()
    account = client.get_account()
    buying_power = float(account.buying_power)
    return buying_power
