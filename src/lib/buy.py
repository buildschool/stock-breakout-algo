from buy_stock import buy_stock
from get_stocks import get_stocks
from get_buying_power import get_buying_power
from get_if_market_day import get_if_market_day
from get_positions import get_positions
from prediction import predict_top_gainer
import pandas as pd
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
            if last['rsi'] < 70:
                if last['sma50'] > last['sma200']:
                    if last['relative_vol'] > 1.5:
                        arr.append(stock)
        try:
            print(arr)
            arr = sorted(arr, key=lambda df: df.iloc[-1]['weekly change'], reverse=True)
            power = get_buying_power()
            power = power / 10
            if power > 0:
                stock_to_buy = predict_top_gainer(arr)
                qty = math.floor(power / stock_to_buy['Close'].iloc[-1])
                buy_stock(stock_to_buy['symbol'].iloc[-1], qty)
        except Exception as e:
            print(e)

day = get_if_market_day()
if day == True:
    buy()
else:
    print('Not a market day')