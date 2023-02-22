from finviz.screener import Screener

def get_assets():
    try:
        filters = ['sh_price_u5', 'ta_change_u20', 'sh_relvol_o1.5', 'ta_sma50_sa200'] 
        stock_list = Screener(filters=filters, table='Technical', order='-change')
        return stock_list
    except:
        try:
            filters = ['sh_price_u5', 'ta_change_u10', 'sh_relvol_o1.5', 'ta_sma50_sa200'] 
            stock_list = Screener(filters=filters, table='Technical', order='-change')
            return stock_list
        except:
            filters = ['sh_price_u5', 'ta_change_u10', 'sh_relvol_o1.5'] 
            stock_list = Screener(filters=filters, table='Technical', order='-change')
            return stock_list