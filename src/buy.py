from lib.buy_stock import buy_stock
from lib.get_stocks import get_stocks
from lib.get_buying_power import get_buying_power
from lib.get_if_market_day import get_if_market_day
from lib.get_positions import get_positions
import pandas as pd
import math

def buy():
    stocks = get_stocks()
    arr = []
    if stocks:
        for stock in stocks:
            last = stock.iloc[-1]
            if last['rsi'] < 70:
                if last['relative_vol'] > 1.5:
                    arr.append(stock)
        try:
            arr = sorted(arr, key=lambda df: df.iloc[-1]['weekly change'], reverse=True)
            power = get_buying_power()
            power = power / 10
            if power > 0:
                positions = get_positions()
                end_arr = []
                if len(arr) > 1:
                    end_arr = arr
                    # for stock in arr:
                    #     for position in positions:
                    #         if position.symbol == stock[0]['symbol']:
                    #             pass
                    #         else:
                    #             end_arr.append(stock)
                    if len(end_arr) == 1:
                        qty = math.floor(float(power / end_arr[len(end_arr) - 1]['close'].iloc[-1]))
                        buy_stock(end_arr.iloc[-1]['symbol'], qty)
                    elif len(end_arr) > 1:
                        print(end_arr[len(end_arr) - 1]['close'].iloc[-1])
                        qty = math.floor(float(power / end_arr[len(end_arr) - 1]['close'].iloc[-1]))
                        buy_stock(end_arr[len(end_arr) - 1]['symbol'].iloc[-1], qty)
                elif len(arr) == 1:
                    end_arr = arr
                    print(end_arr[len(end_arr) - 1]['close'].iloc[-1])
                    qty = math.floor(power / end_arr[len(end_arr) - 1]['close'].iloc[-1])
                    buy_stock(end_arr[len(end_arr) - 1]['symbol'].iloc[-1], qty)
        except Exception as e:
            print(e)

day = get_if_market_day()
if day == True:
    buy()
else:
    print('Not a market day')