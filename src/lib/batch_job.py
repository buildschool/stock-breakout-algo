from get_assets import get_assets
from get_data import get_data
from datetime import datetime, timedelta
import talib

def batch_job():
    assets = get_assets()
    today = datetime.today()
    year_ago = today - timedelta(days=365)
    today = today.date()
    today = today
    year_ago = year_ago.date()
    folder_path = 'src/data/'
    if assets:
        for asset in assets:
            ticker = asset['Ticker']
            file_name = f'{ticker}.csv'
            try:
                df = get_data(ticker, today, year_ago)
                if df is not None:
                    if len(df) > 0:
                        df.to_csv(folder_path + file_name)
            except Exception as e:
                print(e)
    return True

out = batch_job()
print(out)