import yfinance as yf
import talib
import pandas as pd

def get_data(symbol, start_date, end_date):
    try:
        tick = yf.Ticker(symbol)
        fin = tick.history(period="1y", interval="1d", auto_adjust=True)
        df = pd.DataFrame(fin)
        if df.empty:
            return None
        else:
            df['weekly change'] = df['Close'].pct_change(5)
            df['monthly change'] = df['Close'].pct_change(20)
            df['yearly change'] = df['Close'].pct_change(250)
            avg_vol = df['Volume'].mean()
            df['relative_vol'] = df['Volume'] / avg_vol
            df['rsi'] = talib.RSI(df['Close'])
            df['symbol'] = symbol
            return df
    except Exception as e:
        print(e)
        return None