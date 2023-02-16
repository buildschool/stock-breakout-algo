from .trade_client import trade_client
import talib

def get_data(symbol, start_date, end_date):
    try:
        api = trade_client()
        df = api.get_bars(symbol, '1D', start=end_date, end=start_date).df
        df['weekly change'] = df['close'].pct_change(5)
        df['monthly change'] = df['close'].pct_change(20)
        df['yearly change'] = df['close'].pct_change(250)
        avg_vol = df['volume'].mean()
        df['relative_vol'] = df['volume'] / avg_vol
        df['rsi'] = talib.RSI(df['close'])
        df['symbol'] = symbol
        return df
    except Exception as e:
        print(e)
        return None