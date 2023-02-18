import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import os

load_dotenv()

def trade_client():
    api = None
    if os.getenv('PAPER') == "True":
        api = tradeapi.REST(os.getenv("ALPACA_PAPER_API_KEY"), os.getenv("ALPACA_PAPER_SECRET_KEY"), base_url=os.getenv('ALPACA_PAPER_ENDPOINT'))
    else:
        api = tradeapi.REST(os.getenv("ALPACA_LIVE_API_KEY"), os.getenv("ALPACA_LIVE_SECRET_KEY"), base_url=os.getenv('ALPACA_LIVE_ENDPOINT'))
    return api