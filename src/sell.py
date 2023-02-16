from lib.sell_stock import sell_stock
from lib.get_data import get_data
from lib.get_if_market_day import get_if_market_day
from lib.get_positions import get_positions
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

def sell():
    positions = get_positions()
    if positions:
        for position in positions:
            data = get_data(position.symbol)
            last = data.iloc[-1]
            if last['rsi'] > 70:
                if last['weekly change'] * 100 < 0:
                    if last['relative_vol'] < 1.5:
                        sell_stock(position.symbol, position.qty)
        return "Sell complete"
    else: 
        return "No positions to sell" 
    
day = get_if_market_day()
if day == True:
    sell()
else:
    print('Not a market day')