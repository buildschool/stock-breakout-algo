from login import login
import robin_stocks

def get_positions():
    login()
    positions = robin_stocks.robinhood.get_open_stock_positions()
    return positions