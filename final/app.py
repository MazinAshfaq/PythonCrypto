from flask import Flask,render_template
from pycoingecko import CoinGeckoAPI
import json

# Create client 
cg = CoinGeckoAPI()

coinlist = cg.get_coins_list()
btc = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='3')
eth = cg.get_coin_market_chart_by_id(id='ethereum',vs_currency='usd',days='3')

json.dumps(btc, indent=4, sort_keys=True)
json.dumps(eth, indent=4, sort_keys=True)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", btc = btc, eth=eth )


if __name__ == "__main__":
    app.run()