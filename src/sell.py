from lib.sell_stock import sell_stock
from lib.get_assets import get_assets
from lib.get_data import get_data
from lib.get_positions import get_positions

def sell():
    positions = get_positions()
    if positions:
        for position in positions:
            data = get_data(position.symbol)
            last = data.tail(1)
            if last['rsi'] > 70:
                if last['weekly change'] < 0:
                    if last['relative volume'] < 1.5:
                        sell_stock(position.symbol, position.qty)
        return "Sell complete"
    else: 
        return "No positions to sell" 