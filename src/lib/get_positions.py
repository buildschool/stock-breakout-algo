from trade_client import trade_client

def get_positions():
    client = trade_client()
    positions = client.list_positions()
    return positions