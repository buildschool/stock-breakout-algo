from login import login
import robin_stocks

def get_positions():
    login()
    positions = robin_stocks.robinhood.build_holdings()
    return positions