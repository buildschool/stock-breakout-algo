from rh.login import login
import robin_stocks

def get_buying_power():
    try:
        login()
        buying_power = robin_stocks.robinhood.profiles.load_account_profile(info='buying_power')
        return buying_power
    except Exception as e:
        print(e)