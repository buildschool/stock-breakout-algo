from get_assets import get_assets
from get_data import get_data
from datetime import datetime, timedelta
import shutil
import os

def batch_job():
    assets = get_assets()
    today = datetime.today()
    year_ago = today - timedelta(days=365)
    today = today.date()
    today = today
    year_ago = year_ago.date()
    folder_path = 'src/data/'
    folder = 'src/data/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
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