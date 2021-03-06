from pycoingecko import CoinGeckoAPI
import pandas as pd
import json
import plotly.graph_objs as go
import plotly
from os import path

# Create client 
cg = CoinGeckoAPI()

def fetchChartData(coin): 
    #Get coin data
    coinData = cg.get_coin_market_chart_by_id(id=coin,vs_currency='usd',days='1')

    #Grab prices from response
    coin_prices = coinData['prices']

    #Format coin data and save to csv
    coin_df = pd.DataFrame(coin_prices, columns=['dateTime', 'price'])
    coin_df.dateTime = pd.to_datetime(coin_df.dateTime, unit='ms')
    coin_df.set_index('dateTime', inplace=True)

    #Create Plot
    coin_chart = go.Figure(
        [go.Scatter(
        x = coin_df.index,
        y = coin_df.price,
        )
    ]
    )
    # Convert graph to json to make it easier to pass 
    coinGraphJSON = json.dumps(coin_chart, cls=plotly.utils.PlotlyJSONEncoder)

    return coinGraphJSON

def fetchCoins():

    #Fetch All Coin Prices
    coin_market = cg.get_coins_markets(vs_currency='usd')

    #Create dataframe
    df_market = pd.DataFrame(coin_market, columns=['id','current_price'])
    df_market.rename(columns = {'id':'Coin-Name', 'current_price':'Current-Price'}, inplace = True) 
    df_market = df_market.style.format({'Coin-Name' : make_clickable})
    #Create table
    coinTable = df_market.to_html()
    coinTable = coinTable.replace("right", "center")
    coinTable = coinTable.replace("<table", "<table class=\"table table-striped \"")

    return coinTable

#Function To create links
def make_clickable(val):
    return '<a href='+val+'>'+val+'</a>'