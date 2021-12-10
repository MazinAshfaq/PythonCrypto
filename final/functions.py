from pycoingecko import CoinGeckoAPI
import pandas as pd
import json
import plotly.graph_objs as go
import plotly
import plotly.express as px

# Create client 
cg = CoinGeckoAPI()

def fetchData(): 
    #Get coin data
    btc = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='1')
    eth = cg.get_coin_market_chart_by_id(id='ethereum',vs_currency='usd',days='1')

    #Grab prices from response
    btc_prices = btc['prices']
    eth_prices = eth['prices']

    #Format btc data and save to csv
    btc_df = pd.DataFrame(btc_prices, columns=['dateTime', 'price'])
    btc_df.dateTime = pd.to_datetime(btc_df.dateTime, unit='ms')
    btc_df.set_index('dateTime', inplace=True)
    btc_df.to_csv('btc_candle.csv')

    #Format eth data and save to csv
    eth_df = pd.DataFrame(eth_prices, columns=['dateTime', 'price'])
    eth_df.dateTime = pd.to_datetime(eth_df.dateTime, unit='ms')
    eth_df.set_index('dateTime', inplace=True)
    eth_df.to_csv('eth_candle.csv')

    #Load CSV data into variable
    eth_df = pd.read_csv('./eth_candle.csv')

    #Create Plot
    eth_chart = go.Figure(
        [go.Scatter(
        x = eth_df['dateTime'],
        y = eth_df['price'],
        )
    ]
    )

    #Load CSV data into variable
    btc_df = pd.read_csv('./btc_candle.csv')

    #Create Plot
    btc_chart = go.Figure(
        [go.Scatter(
        x = btc_df['dateTime'],
        y = btc_df['price'],
        )
    ]
    )

    #Convert Chart into json data 
    graph1JSON = json.dumps(btc_chart, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(eth_chart, cls=plotly.utils.PlotlyJSONEncoder)

    return [graph1JSON, graph2JSON]
