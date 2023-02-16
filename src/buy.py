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
            last = stock.tail(1)
            if last['weekly change'] > 25:
                if last['rsi'] < 70:
                    if last['relative volume'] > 1.5:
                        arr.append(stock)
        try:
            arr = sorted(arr, reverse=True)
            power = get_buying_power()
            if power > 0:
                power = power / 10
                qty = power / arr.tail(1)['price']
                try:
                    positions = get_positions()
                    for position in positions:
                        if position.symbol == arr[0]['symbol']:
                            pass
                        else:
                            buy_stock(arr[0]['symbol'], qty)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

day = get_if_market_day()
if day == True:
    buy()
else:
    print('Not a market day')