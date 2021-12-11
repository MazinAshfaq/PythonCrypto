from pycoingecko import CoinGeckoAPI
import pandas as pd
import json
import plotly.graph_objs as go
import plotly
import plotly.express as px
from os import path

# Create client 
cg = CoinGeckoAPI()

def fetchChartData(coin): 
    #Get coin data
    coinData = cg.get_coin_market_chart_by_id(id=coin,vs_currency='usd',days='1')
    btc = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='1')
    eth = cg.get_coin_market_chart_by_id(id='ethereum',vs_currency='usd',days='1')

    #Grab prices from response
    coin_prices = coinData['prices']
    btc_prices = btc['prices']
    eth_prices = eth['prices']


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

    coinTable = df_market.to_html()
    # #Create table
    # coinTable = df_market.to_html(classes='table thead-dark table-striped table-bordered table-hover')
    coinTable = coinTable.replace("right", "center")
    coinTable = coinTable.replace("<table", "<table class=\"table table-striped \"")
    #Create Links from each coin to its page 

    return coinTable

def make_clickable(val):
    return '<a href='+val+'>'+val+'</a>'