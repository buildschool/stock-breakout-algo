import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import os

def trade_client():
    load_dotenv()
    api = None
    if os.getenv('PAPER') == True:
        api = tradeapi.REST(os.getenv("ALPACA_PAPER_API_KEY"), os.getenv("ALPACA_PAPER_SECRET_KEY"), api_version='v2')
    else:
        api = tradeapi.REST(os.getenv("ALPACA_LIVE_API_KEY"), os.getenv("ALPACA_LIVE_SECRET_KEY"), api_version='v2')
    return api