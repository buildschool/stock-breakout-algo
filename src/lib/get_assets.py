from trade_client import trade_client

def get_assets():
    api = trade_client()
    assets = api.list_assets()
    arr = []
    nyse_assets = [asset for asset in assets if asset.exchange == 'NYSE']
    nasdaq_assets = [asset for asset in assets if asset.exchange == 'NASDAQ']
    otc_assets = [asset for asset in assets if asset.exchange == 'OTC']
    for asset in nyse_assets:
        arr.append(asset)
    for asset in nasdaq_assets:
        arr.append(asset)
    for asset in otc_assets:
        arr.append(asset)
    return arr
