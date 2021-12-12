from flask import Flask, render_template
import os
import functions

app = Flask(__name__)

@app.route("/")
def home():
    coinTable = functions.fetchCoins()
    return render_template("home.html", coinTable = coinTable)

@app.route("/<coin>")
def user(coin):
    coinData = functions.fetchChartData(coin)
    return render_template("chart.html", coin = coin, coinData=coinData)
    
if __name__ == "__main__":
    PORT = (os.getenv('PORT')) if os.getenv('PORT') else 8080 
    app.run(host='0.0.0.0',port=PORT, debug=True)