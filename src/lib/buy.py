from buy_stock import buy_stock
from get_stocks import get_stocks
from get_buying_power import get_buying_power
from get_if_market_day import get_if_market_day
from get_positions import get_positions
from batch_job import batch_job
import pandas as pd
import math
import warnings
from dotenv import load_dotenv
import os

load_dotenv()

# Ignore warnings
warnings.filterwarnings("ignore")

def buy():
    fraction = os.getenv('FRACTION')
    fraction = float(fraction)
    out = batch_job()
    if out == True:
        stocks = get_stocks()
        print("Stocks:")
        for stock in stocks:
            print(stock['symbol'].iloc[-1])
        arr = []
        if stocks:
            for stock in stocks:
                last = stock.iloc[-1]
                if last['sma50'] > last['sma200']:
                    arr.append(stock)
            positions = get_positions()
            symbols = list(positions.keys())
            out = []
            for symbol in symbols:
                for stock in arr:
                    if symbol == stock['symbol'].iloc[-1]:
                        continue
                    else:
                        out.append(stock)
            try:    
                out = sorted(out, key=lambda df: df.iloc[-1]['rsi'], reverse=False)
                power = get_buying_power()
                power = math.floor(float(power) / fraction)
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