from flask import Flask,render_template
from pycoingecko import CoinGeckoAPI

# Create client 
cg = CoinGeckoAPI()

cg.get_coins_list()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()