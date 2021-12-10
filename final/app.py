from flask import Flask,render_template
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
    app.run(debug=True)