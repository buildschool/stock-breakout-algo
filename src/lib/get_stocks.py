import pandas as pd
import os

def get_stocks():
    folder_path = 'src/data/'
    dfs = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath)
            dfs.append(df)
    return dfs
