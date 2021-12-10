from flask import Flask,render_template
from pycoingecko import CoinGeckoAPI
import pandas as pd
import json

# Create client 
cg = CoinGeckoAPI()

btc = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='3')
eth = cg.get_coin_market_chart_by_id(id='ethereum',vs_currency='usd',days='3')

btc_prices = btc['prices']
eth_prices = eth['prices']


btc_df = pd.DataFrame(btc_prices, columns=['dateTime', 'price'])
btc_df.dateTime = pd.to_datetime(btc_df.dateTime, unit='ms')
btc_df.set_index('dateTime', inplace=True)
btc_df.to_csv('btc_candle.csv')

eth_df = pd.DataFrame(eth_prices, columns=['dateTime', 'price'])
eth_df.dateTime = pd.to_datetime(eth_df.dateTime, unit='ms')
eth_df.set_index('dateTime', inplace=True)
eth_df.to_csv('eth_candle.csv')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", btc = btc_df, eth=eth_df)


if __name__ == "__main__":
    app.run()