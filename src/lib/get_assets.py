from finviz.screener import Screener

def get_assets():
    try:
        filters = ['please add your own settings from fin is pypi'] 
        stock_list = Screener(filters=filters, table='Technical', order='-change')
        return stock_list
    except:
        print("No stocksfound")