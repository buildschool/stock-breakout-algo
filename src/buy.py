from lib.buy_stock import buy_stock
from lib.get_stocks import get_stocks
from lib.get_buying_power import get_buying_power
from lib.get_if_market_day import get_if_market_day
from lib.get_positions import get_positions

def buy():
    stocks = get_stocks()
    arr = []
    if stocks:
        for stock in stocks:
            last = stock.iloc[-1]
            if last['weekly change'] * 100 > 25:
                if last['rsi'] < 70:
                    if last['relative_vol'] > 1.5:
                        arr.append(stock)
        try:
            arr = sorted(arr, reverse=True)
            power = get_buying_power()
            if power > 0:
                power = power / 10
                qty = power / arr[0]['close']
                try:
                    positions = get_positions()
                    for stock, j in enumerate(arr):
                        for position in enumerate(positions):
                            if position.symbol == arr[j]['symbol']:
                                arr.pop(j)
                            else:
                                pass
                    try:
                        buy_stock(arr[0]['symbol'], qty)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

day = get_if_market_day()
if day == True:
    buy()
else:
    print('Not a market day')