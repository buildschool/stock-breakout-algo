from buy_stock import buy_stock
from get_stocks import get_stocks
from get_buying_power import get_buying_power
from get_if_market_day import get_if_market_day
import math
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

def buy():
    stocks = get_stocks()
    arr = []
    if stocks:
        for stock in stocks:
            last = stock.iloc[-1]
            arr.append(stock)
        try:
            arr = sorted(arr, key=lambda df: df.iloc[-1]['weekly change'], reverse=True)
            power = get_buying_power()
            power = math.floor(float(power) / 10)
            if power > 0:
                arr = sorted(arr, key=lambda df: df.iloc[-1]['rsi'], reverse=False)
                qty = math.floor(power / arr[0]['Close'].iloc[-1])
                buy_stock(arr[0]['symbol'].iloc[-1], qty)
        except Exception as e:
            print(e)

day = get_if_market_day()
if day == True:
    buy()
else:
    print('Not a market day')